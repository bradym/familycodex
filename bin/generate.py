#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

import htmlmin
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


class GenerateSite:

    def __init__(self):

        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.template_dir = os.path.join(self.base_dir, 'templates')
        self.data_dir = os.path.join(self.base_dir, 'data')
        self.build_dir = os.path.join(self.base_dir, 'build')
        self.static_dir = os.path.join(self.base_dir, 'static')
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.html_minify = True

        if not os.path.isdir(self.template_dir):
            raise FileNotFoundError(self.template_dir)

        if not os.path.isdir(self.data_dir):
            raise FileNotFoundError(self.data_dir)

        if not os.path.isdir(self.build_dir):
            os.mkdir(self.build_dir)

        self.data = {}

    def get_build_path(self, what):
        return os.path.join(self.build_dir, '{}'.format(what))

    def write_file(self, template, path):
        html = self.env.get_template(template).render(self.data)

        if self.html_minify:
            html = htmlmin.minify(html, remove_comments=True)

        with open(path, 'w') as f:
            f.write(html)

    def generate_page(self, template_name, item):
        self.data['current_item'] = item
        dest = self.get_build_path('{}.html'.format(item))
        template = '{}.j2'.format(template_name)
        self.write_file(template, dest)

    def clean(self):
        for root, dirs, files in os.walk(self.build_dir, topdown=False):
            for item in files:
                path = os.path.join(root, item)
                os.remove(path)
            for item in dirs:
                path = os.path.join(root, item)
                if not os.path.islink:
                    os.rmdir(path)

    def copy_static(self):

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
        self.html_minify = html_minify


def run(html_minify=True):
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
