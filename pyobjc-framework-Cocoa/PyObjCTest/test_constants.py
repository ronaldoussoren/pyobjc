import AppKit
from PyObjCTools.TestSupport import TestCase


class ContantTest(TestCase):
    def test_floating_window_level(self):
        # NSFloatingWindowLevel is a define in Objective-C, up-to 1.0rc1
        # we didn't correctly pick up this define due to a bug in the code.
        self.assertHasAttr(AppKit, "NSFloatingWindowLevel")
        self.assertIsInstance(AppKit.NSFloatingWindowLevel, int)

    def test_anyeventmask(self):
        self.assertEqual(AppKit.NSAnyEventMask, AppKit.NSUIntegerMax)

    def test_nsview_frameditchange_notification(self):
        self.assertHasAttr(AppKit, "NSViewFrameDidChangeNotification")
        self.assertIsInstance(AppKit.NSViewFrameDidChangeNotification, str)

    def test_nsuparrowfunctionkey(self):
        self.assertHasAttr(AppKit, "NSUpArrowFunctionKey")
        self.assertIsInstance(AppKit.NSUpArrowFunctionKey, str)
