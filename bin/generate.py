#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from pathlib import Path

import htmlmin
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


class GenerateSite:

    def __init__(self):
        self.base_dir = os.path.realpath(Path(__file__).parent.parent)
        self.template_dir = os.path.join(self.base_dir, 'templates')
        self.data_dir = os.path.join(self.base_dir, 'data')
        self.build_dir = os.path.join(self.base_dir, 'build')
        self.static_dir = os.path.join(self.base_dir, 'static')
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.data = {}
        self.html_minify = True

        required_dirs = [self.template_dir, self.data_dir, self.static_dir]

        for folder in required_dirs:
            if not os.path.isdir(folder):
                raise FileNotFoundError(folder)

        if not os.path.isdir(self.build_dir):
            os.mkdir(self.build_dir)

    def generate_page(self, template_name, item):
        """Render the given template and write it to disk."""
        self.data['current_item'] = item
        dest = os.path.join(self.build_dir, '{}.html'.format(item))
        template = '{}.j2'.format(template_name)

        html = self.env.get_template(template).render(self.data)

        if self.html_minify:
            html = htmlmin.minify(html, remove_comments=True)

        with open(dest, 'w') as f:
            f.write(html)

    def clean(self):
        """Delete the contents of the build folder."""
        shutil.rmtree(self.build_dir)
        os.mkdir(self.build_dir)

    def copy_static(self):
        """Copies code in the static folder to the build directory without modification."""
        for current_dir in [os.path.join(self.base_dir, 'node_modules'), self.static_dir]:

            for root, dirs, files in os.walk(current_dir):

                for item in files:
                    source = os.path.join(root, item)
                    base = os.path.basename(root)

                    if base == 'static':
                        dest_dir = self.build_dir
                    elif 'node_modules' in root:
                        node_module = root.split('node_modules')[1].lstrip('/').split('/')[0]
                        dest_dir = os.path.join(self.build_dir, node_module, os.path.basename(root))
                    else:
                        dest_dir = os.path.join(self.build_dir, os.path.basename(root))

                    if not os.path.isdir(dest_dir):
                        os.makedirs(dest_dir)

                    dest = os.path.join(dest_dir, item)
                    shutil.copyfile(source, dest)

    def load_data(self):
        """
        This loops through all yaml files in the data directory and loads the data into a
        class property for later use.
        """
        for root, dirs, files in os.walk(self.data_dir):
            for item in files:

                data_type = os.path.basename(root)
                full_path = os.path.join(root, item)
                name = os.path.splitext(item)[0]

                if data_type not in self.data:
                    self.data[data_type] = {}

                with open(full_path, 'rb') as f:
                    self.data[data_type][name] = yaml.load(f)

    def set_minify(self, html_minify):
        """Setter for the html_minify property. Used to disable html minification when built via the local server."""
        self.html_minify = html_minify


def run(html_minify=True):
    """
    This function is what actually runs all the functions to generate the site. It is imported and used in
    serve.py to avoid having different behavior when generating as a one-time task vs when running the local
    server during development.
    """
    generator = GenerateSite()
    generator.set_minify(html_minify)
    generator.clean()
    generator.copy_static()
    generator.load_data()
    generator.generate_page('index', 'index')

    for item in generator.data['people']:
        generator.generate_page('person', item)

    print('Site generation complete')


if __name__ == '__main__':
    run()
