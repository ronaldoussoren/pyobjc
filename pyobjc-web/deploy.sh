#!/bin/sh
rsync --progress -C -e ssh --delete -a -v -z  docroot/ "${1:-bbum}@shell.sourceforge.net:/home/groups/p/py/pyobjc/htdocs/"

