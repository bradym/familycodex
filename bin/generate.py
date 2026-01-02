#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from pathlib import Path

import htmlmin
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


class GenerateSite:
    def __init__(self):
        self.base_dir = os.path.realpath(Path(__file__).parent.parent)
        self.template_dir = os.path.join(self.base_dir, "templates")
        self.data_dir = os.path.join(self.base_dir, "data")
        self.build_dir = os.path.join(self.base_dir, "build")
        self.static_dir = os.path.join(self.base_dir, "static")
        self.env = Environment(
            extensions=["jinja2.ext.debug"],
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(["html", "xml"]),
        )
        self.data = {}
        self.html_minify = True

        required_dirs = [self.template_dir, self.data_dir, self.static_dir]

        for folder in required_dirs:
            if not os.path.isdir(folder):
                raise FileNotFoundError(folder)

        if not os.path.isdir(self.build_dir):
            os.mkdir(self.build_dir)

    def generate_family_pages(self):
        for item in self.data["family"]:
            dest = Path(self.build_dir).joinpath(f"{item}.html")
            render_data = {"family": self.data["family"][item], "nav": self.data["nav"]}
            self.generate_page(render_data, dest, "family.j2")

    def generate_index(self):
        render_data = self.data
        dest = Path(self.build_dir).joinpath("index.html")
        self.generate_page(render_data, dest, "index.j2")

    def generate_page(self, data, dest, template):
        html = self.env.get_template(template).render(data)
        if self.html_minify:
            html = htmlmin.minify(html, remove_comments=True)

        with open(dest, "w") as f:
            f.write(html)

    def clean(self):
        """Delete the contents of the build folder."""
        if os.path.isdir(self.build_dir):
            shutil.rmtree(self.build_dir)
            os.mkdir(self.build_dir)

        media_dir = os.path.join(self.base_dir, "media")

        if os.path.isdir(self.build_dir) and os.path.isdir(media_dir):
            symlink_path = os.path.join(self.build_dir, "media")
            os.symlink(media_dir, symlink_path)

    def copy_static(self):
        """Copies code in the static folder to the build directory without modification."""
        for current_dir in [
            os.path.join(self.base_dir, "node_modules"),
            self.static_dir,
        ]:
            for root, dirs, files in os.walk(current_dir):
                for item in files:
                    source = os.path.join(root, item)
                    base = os.path.basename(root)

                    if base == "static":
                        dest_dir = self.build_dir
                    elif "node_modules" in root:
                        node_module = (
                            root.split("node_modules")[1].lstrip("/").split("/")[0]
                        )
                        dest_dir = os.path.join(
                            self.build_dir, node_module, os.path.basename(root)
                        )
                    else:
                        dest_dir = os.path.join(self.build_dir, os.path.basename(root))

                    if not os.path.isdir(dest_dir):
                        os.makedirs(dest_dir)

                    dest = os.path.join(dest_dir, item)
                    shutil.copyfile(source, dest)

    def load_families(self, include_fake_data=False):
        """
        Loop through families folder and load yaml data and stories into data object.
        """
        md = markdown.Markdown(extensions=["markdown.extensions.meta"])
        self.data = {"family": {}, "nav": []}

        root = Path(f"{self.data_dir}/families")

        for current_family_path in root.iterdir():
            current_family = current_family_path.stem
            current_root = root.joinpath(current_family)
            data_file = current_root.joinpath(f"{current_family}.yaml")

            if not data_file.exists():
                continue

            with open(data_file, "r", encoding="utf-8") as f:
                current_data = yaml.safe_load(f)

            if (
                not include_fake_data
                and "fake" in current_data
                and current_data["fake"]
            ):
                continue

            story_path = current_root.joinpath("stories")
            if story_path.is_dir():
                if "stories" not in current_data:
                    current_data["stories"] = []

                for story in story_path.iterdir():
                    with open(story, "r", encoding="utf-8") as f:
                        # content = md.convert(f.read())
                        current_story = {
                            "content": md.convert(f.read()),
                            "id": story.stem,
                        }

                        for key in md.Meta:
                            current_story[key] = "\n".join(md.Meta[key])

                        current_data["stories"].append(current_story)

            self.data["family"][current_family] = current_data
            self.data["nav"].append(
                {"href": f"/{current_family}.html", "text": current_data["name"]}
            )
        self.data["nav"].sort(key=lambda item: item["text"].casefold())

    def set_minify(self, html_minify):
        """Setter for the html_minify property. Used to disable html minification when built via the local server."""
        self.html_minify = html_minify


def run(html_minify=True, include_unpublished_data=False):
    """
    This function is what actually runs all the functions to generate the site. It is imported and used in
    serve.py to avoid having different behavior when generating as a one-time task vs when running the local
    server during development.
    """
    generator = GenerateSite()
    generator.set_minify(html_minify)
    generator.clean()
    generator.copy_static()
    generator.load_families(include_unpublished_data)
    generator.generate_index()
    generator.generate_family_pages()

    print("Site generation complete")


if __name__ == "__main__":
    run()
