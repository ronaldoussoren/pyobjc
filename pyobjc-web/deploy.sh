#!/bin/sh
rsync --progress -C -e ssh --delete -a -v -z  docroot/ shell.sourceforge.net:/home/groups/p/py/pyobjc/htdocs/

