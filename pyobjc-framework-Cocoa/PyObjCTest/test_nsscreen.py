import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSScreen(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSScreenTouchCapabilities)
        self.assertEqual(AppKit.NSScreenTouchCapabilitiesNone, 0)
        self.assertEqual(AppKit.NSScreenTouchCapabilitiesMultiTouch, 1 << 0)

    def test_constants(self):
        self.assertIsInstance(AppKit.NSScreenColorSpaceDidChangeNotification, str)

    def test_methods(self):
        m = AppKit.NSScreen.supportedWindowDepths.__metadata__()
        self.assertTrue(m["retval"]["c_array_delimited_by_null"])

        self.assertResultHasType(
            AppKit.NSScreen.convertRectToBacking_, AppKit.NSRect.__typestr__
        )
        self.assertArgHasType(
            AppKit.NSScreen.convertRectToBacking_, 0, AppKit.NSRect.__typestr__
        )
        self.assertResultHasType(
            AppKit.NSScreen.convertRectFromBacking_, AppKit.NSRect.__typestr__
        )
        self.assertArgHasType(
            AppKit.NSScreen.convertRectFromBacking_, 0, AppKit.NSRect.__typestr__
        )
        self.assertResultHasType(
            AppKit.NSScreen.backingAlignedRect_options_, AppKit.NSRect.__typestr__
        )
        self.assertArgHasType(
            AppKit.NSScreen.backingAlignedRect_options_, 0, AppKit.NSRect.__typestr__
        )

        self.assertResultIsBOOL(AppKit.NSScreen.screensHaveSeparateSpaces)

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertResultIsBOOL(AppKit.NSScreen.canRepresentDisplayGamut_)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsSEL(AppKit.NSScreen.displayLinkWithTarget_selector_, 1, b"v@:@")
