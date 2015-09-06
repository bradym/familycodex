familycodex
===========

Familycodex is a site for sharing family history artifacts such as
documents, videos, photos and audio recordings.

Site Structure
--------------

  - Homepage is a list of families in the system with links to family subdomains (www.familycodex.net)
  - Family subdomain lists people in family and links to individual pages (smith.familycodex.net, mitchell.familycodex.net, etc)
  - Individual page includes embedded documents/audio/video/photos (smith.familycodex.net/gramps.html)

Development Details
-------------------

- PHP Framework: `Laravel <http://laravel.com/>`_
- Recommended development environment: `Homestead <http://laravel.com/docs/master/homestead>`_

Getting the site running locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Clone this repo
- Install `VirtualBox <https://www.virtualbox.org/wiki/Downloads>`_
- Install `Vagrant <https://www.vagrantup.com/>`_
- Add entries to your hosts file

  - 192.168.10.10       www.familycodex.dev smith.familycodex.dev mitchell.familycodex.dev

- SSH into the VM: vagrant ssh

- Run: familycodex/artisan local:setup


