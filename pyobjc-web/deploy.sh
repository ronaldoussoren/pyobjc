#!/bin/sh
# We don't use '-a', because we don't want to muck with permissions on the
# server.
rsync --progress -C -e ssh --delete  -v -z -rltgoD --exclude 'cvs-snapshots' docroot/ "${1:-bbum}@shell.sourceforge.net:/home/groups/p/py/pyobjc/htdocs/"

