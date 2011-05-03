#!/usr/bin/python

import os, sys

TMPL="""
from PyObjCTools.TestSupport import *
from %(framework)s import *

class Test%(basename)s (TestCase):
    def testIncomplete(self):
        self.fail("Add header tests for <%(framework)s/%(basename)s.h>")

if __name__ == "__main__":
    main()
"""

def main():
    framework = sys.argv[1]

    if framework[0] == '/':
        dirpath = os.path.join(framework, 'Headers')
        framework = os.path.basename(framework)[:-10]

    else:
        dirpath = '/System/Library/Frameworks/%s.framework/Headers'%(framework,)

    for fn in os.listdir(dirpath):
        basename = os.path.splitext(fn)[0]
        outfn = 'test_%s.py'%(basename.lower())

        if not os.path.exists(outfn):
            print outfn
            fd = open(outfn, 'w')
            fd.write(TMPL % locals() )
            fd.close()


if __name__ == "__main__":
    main()
