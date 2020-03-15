import AppKit
from PyObjCTools.TestSupport import TestCase


class ContantTest(TestCase):
    def testNSFloatingWindowLevel(self):
        # NSFloatingWindowLevel is a define in Objective-C, up-to 1.0rc1
        # we didn't correctly pick up this define due to a bug in the code.
        self.assertHasAttr(AppKit, "NSFloatingWindowLevel")
        self.assertIsInstance(AppKit.NSFloatingWindowLevel, int)

    def testNSAnyEventMask(self):
        self.assertEqual(AppKit.NSAnyEventMask, AppKit.NSUIntegerMax)

    def testNSViewFrameDidChangeNotification(self):
        self.assertHasAttr(AppKit, "NSViewFrameDidChangeNotification")
        self.assertIsInstance(AppKit.NSViewFrameDidChangeNotification, str)

    def testNSUpArrowFunctionKey(self):
        self.assertHasAttr(AppKit, "NSUpArrowFunctionKey")
        self.assertIsInstance(AppKit.NSUpArrowFunctionKey, str)
