#!/usr/bin/env python
# coding=utf-8
"""
This script will build the site and serve it locally on port 5500. It will watch for changes
to site code and rebuild the site when changes are detected. If your browser has a livereload
plugin, the site will be automatically reloaded once built.
"""

import glob
import os
from pathlib import Path

from livereload import Server
from livereload.watcher import Watcher

from generate import run


class CustomWatcher(Watcher):

    def is_glob_changed(self, path, ignore=None):
        for f in glob.glob(path, recursive=True):
            if self.is_file_changed(f, ignore):
                return True
        return False


base_dir = os.path.realpath(Path(__file__).parent.parent)
build_dir = os.path.join(base_dir, 'build')

# Which paths should trigger a rebuild?
paths = [
    'data',
    'static',
    'templates'
]


def build():
    """
    The server.watch function called below does not allow parameters to be passed in.
    By wrapping the call to run, we can disable minification when serving the site
    locally to make debugging easier.
    """
    run(html_minify=False)


# Always build before starting the server
build()

server = Server(watcher=CustomWatcher())

# Watch files and re-generate on changes
for path in paths:
    full_path = os.path.join(base_dir, path)
    server.watch('../{}/**/*'.format(path), build)

server.serve(root=build_dir)
