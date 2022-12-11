# familycodex

Familycodex is a site for sharing family history artifacts such as documents, videos, photos and audio recordings.

## Site Architecture

This codebase is used to generate a static site, which is uploaded to [GitHub Pages](https://pages.github.com/).

## Site Structure

### build

When `generate.py` is run, the output goes here. There is no value to having this folder in version control, so it's in the .gitignore.

### bin

The bin folder is home to the various scripts that help with the generation of the site:

* `generate.py` is the script that generates the html files that get uploaded to s3.
* `serve.py` is for running a local server while working on the site.

### data

Rather than using a database, data is stored here in [yaml](http://yaml.org/) files. Each couple has a yaml file in the families folder, and each page not about a family (ie: index page) has a yaml file in the pages folder.

Why yaml? It's easy to read, easy to write, allows comments, is very flexible and has there are good, simple python libraries fo reading yaml. It also helps keep the codebase simple.

### media

The media folder is home to audio, documents and photos uploaded to s3. It would be a bad idea to have this folder checked into git due to the size, so it's in the .gitignore. It is only used locally when adding new media to the site.

### static

This is where custom javascript, css, and any other static site-related assets go. The contents of this folder are copied to the build folder without any modification.

### templates

The templates folder contains [jinja](https://jinja.palletsprojects.com/en/3.1.x/) templates that are used to render the site.

* base.j2 - Overall HTML structure for the site, index.j2 and person.j2 extend this template.

* index.j2 - The template for the homepage of the site.

* family.j2 - The template for the family pages.

* audio.j2, documents.j2, photos.j2, stories.j2 and videos.j2 are the different tabs on the family pages. Separating them from family.j2 makes it easier to focus on one thing at a time when working on the site, and keeps the template sizes more manageable.
