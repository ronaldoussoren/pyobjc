#!/bin/sh
# We don't use '-a', because we don't want to muck with permissions on the
# server.
rsync --progress -C -e ssh --delete  -v -z -rltgoD --exclude 'cvs-snapshots' docroot/ "${1:-bbum}@shell.sourceforge.net:/home/groups/p/py/pyobjc/htdocs/"

# Permissions are hosed anyway, fix them up afterwards
# The redirection of stderr was added to ignore error messages about not 
# being able to change the permissions of files owned by others
ssh "${1:-bbum}@shell.sourceforge.net" "chmod -R g+w /home/groups/p/py/pyobjc/htdocs  2>/dev/null"
