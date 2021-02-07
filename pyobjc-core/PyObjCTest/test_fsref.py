import objc
from PyObjCTest.fsref import OC_TestFSRefHelper
from PyObjCTools.TestSupport import TestCase


class TestFSRef(TestCase):
    def testBasicInterface(self):
        self.assertArgIsIn(OC_TestFSRefHelper.pathForFSRef_, 0)
        self.assertArgIsOut(OC_TestFSRefHelper.getFSRef_forPath_, 0)

    def testResult(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        self.assertIsInstance(ref.data, bytes)
        self.assertIsInstance(ref.as_pathname(), str)

        try:
            from Carbon.File import FSRef

        except ImportError:
            pass

        else:
            self.assertIsInstance(ref.as_carbon(), FSRef)

    def testArg(self):
        return  #
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, str)
        self.assertEqual(p, "/Library")

    def testInput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_("/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.pathForFSRef_(ref)
        self.assertIsInstance(p, str)
        self.assertEqual(p, "/Library")

    def testOutput(self):
        return  # XX
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.getFSRef_forPath_(None, "/Library")
        self.assertIsInstance(ref, objc.FSRef)

        # Verify the fsref contents:
        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, str)
        self.assertEqual(p, "/Library")
