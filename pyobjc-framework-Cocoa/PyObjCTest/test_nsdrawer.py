import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSDrawerHelper(AppKit.NSObject):
    def drawerShouldOpen_(self, sender):
        return 1

    def drawerShouldClose_(self, sender):
        return 1

    def drawerWillResizeContents_toSize_(self, a, b):
        return 1


class TestNSDrawer(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSDrawerClosedState, 0)
        self.assertEqual(AppKit.NSDrawerOpeningState, 1)
        self.assertEqual(AppKit.NSDrawerOpenState, 2)
        self.assertEqual(AppKit.NSDrawerClosingState, 3)

        self.assertIsInstance(AppKit.NSDrawerWillOpenNotification, str)
        self.assertIsInstance(AppKit.NSDrawerDidOpenNotification, str)
        self.assertIsInstance(AppKit.NSDrawerWillCloseNotification, str)
        self.assertIsInstance(AppKit.NSDrawerDidCloseNotification, str)

    def testMethods(self):
        self.assertArgHasType(
            AppKit.NSDrawer.setMinContentSize_, 0, AppKit.NSSize.__typestr__
        )

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("NSDrawerDelegate")

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSDrawerHelper.drawerShouldOpen_)
        self.assertResultIsBOOL(TestNSDrawerHelper.drawerShouldClose_)
        self.assertResultHasType(
            TestNSDrawerHelper.drawerWillResizeContents_toSize_,
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSDrawerHelper.drawerWillResizeContents_toSize_,
            1,
            AppKit.NSSize.__typestr__,
        )
