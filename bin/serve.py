#!/usr/bin/env python
import os
from livereload import Server
from livereload.watcher import Watcher
from generate import run
import glob


class CustomWatcher(Watcher):

    def is_glob_changed(self, path, ignore=None):
        for f in glob.glob(path, recursive=True):
            if self.is_file_changed(f, ignore):
                return True
        return False


base_dir = os.path.dirname(os.path.realpath(__file__))
build_dir = os.path.join(base_dir, 'build')

# Which paths should trigger a rebuild?
paths = [
    'data',
    'node_modules',
    'static',
    'templates'
]


# The server.watch function called below does not allow parameters to be passed in.
# By wrapping the call to run, we can disable minification when serving the site
# locally to make debugging easier.
def build():
    run(html_minify=False)


# Always build before starting the server
build()

server = Server(watcher=CustomWatcher())

# Watch files and re-generate on changes
for path in paths:
    full_path = os.path.join(base_dir, path)
    server.watch('./{}/**/*'.format(path), build)

server.serve(root=build_dir)
