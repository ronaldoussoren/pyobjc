import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSPageControllerHelper(AppKit.NSObject):
    def pageController_frameForObject_(self, p, f):
        return 1


class TestNSPageController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSPageControllerTransitionStyle)

    def test_constants(self):
        self.assertEqual(AppKit.NSPageControllerTransitionStyleStackHistory, 0)
        self.assertEqual(AppKit.NSPageControllerTransitionStyleStackBook, 1)
        self.assertEqual(AppKit.NSPageControllerTransitionStyleHorizontalStrip, 2)

    @min_sdk_level("10.10")
    def test_protocols10_10(self):
        self.assertProtocolExists("NSPageControllerDelegate", AppKit)

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestNSPageControllerHelper.pageController_frameForObject_,
            AppKit.NSRect.__typestr__,
        )
