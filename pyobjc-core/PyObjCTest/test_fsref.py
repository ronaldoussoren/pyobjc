from __future__ import unicode_literals
from PyObjCTools.TestSupport import *
import objc

from PyObjCTest.fsref import *

import sys
if sys.version_info[0] == 3:
    unicode = str

class TestFSRef (TestCase):
    def testBasicInterface(self):
        self.assertArgIsIn(OC_TestFSRefHelper.pathForFSRef_, 0)
        self.assertArgIsOut(OC_TestFSRefHelper.getFSRef_forPath_, 0)

    def testResult(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        self.assertIsInstance(ref.data, bytes)
        self.assertIsInstance(ref.as_pathname(), unicode)

        try:
            from Carbon.File import FSRef

        except ImportError:
            pass

        else:
            self.assertIsInstance(ref.as_carbon(), FSRef)

    def testArg(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, unicode)
        self.assertEqual(p, "/Library")

    def testInput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.pathForFSRef_(ref)
        self.assertIsInstance(p, unicode)
        self.assertEqual(p, "/Library")

    def testOutput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.getFSRef_forPath_(None, "/Library")
        self.assertIsInstance(ref, objc.FSRef)

        # Verify the fsref contents:
        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, unicode)
        self.assertEqual(p, "/Library")


if __name__ == "__main__":
    main()
