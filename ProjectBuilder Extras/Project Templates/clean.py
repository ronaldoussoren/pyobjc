#!/usr/bin/env python

"""
Cleans noise files out of the Project Template tree.

Noise includes '.DS_Store', all files that include a '~' character,
and all user specific Project Builder information.   User specific
Project Builder files -- the files ending in '.pbxuser' -- will cause
a corrupted, but mostly working, project to be created from the
templates.
"""

import sys
import os
import re

nastyFileExprs = map(re.compile, ['^.DS_Store$', '.*~.*$', '.*.pbxuser$'])
def killNasties(irrelevant, dirName, names):
    for aName in names:
        if len(filter(lambda expr, aName=aName: expr.match(aName), nastyFileExprs)):
            path = os.path.join(dirName, aName)
            os.remove( path )
            print "Removed '%s'" % path

os.path.walk(".", killNasties, None)
