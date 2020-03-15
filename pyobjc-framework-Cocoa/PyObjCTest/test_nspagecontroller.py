import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSPageControllerHelper(AppKit.NSObject):
    def pageController_frameForObject_(self, p, f):
        return 1


class TestNSPageController(TestCase):
    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(AppKit.NSPageControllerTransitionStyleStackHistory, 0)
        self.assertEqual(AppKit.NSPageControllerTransitionStyleStackBook, 1)
        self.assertEqual(AppKit.NSPageControllerTransitionStyleHorizontalStrip, 2)

    def testProtocols(self):

        self.assertResultHasType(
            TestNSPageControllerHelper.pageController_frameForObject_,
            AppKit.NSRect.__typestr__,
        )

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("NSPageControllerDelegate")
