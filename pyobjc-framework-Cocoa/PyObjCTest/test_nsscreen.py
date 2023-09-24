import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSScreen(TestCase):
    def testMethods(self):
        m = AppKit.NSScreen.supportedWindowDepths.__metadata__()
        self.assertTrue(m["retval"]["c_array_delimited_by_null"])

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(AppKit.NSScreenColorSpaceDidChangeNotification, str)

    @min_os_level("10.7")
    def testMethods10_7(self):
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

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(AppKit.NSScreen.screensHaveSeparateSpaces)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSScreen.canRepresentDisplayGamut_)

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertArgIsSEL(AppKit.NSScreen.displayLinkWithTarget_selector_, 1, b"v@:@")
