import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSDockTile(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSDockTile.showsApplicationBadge)
        self.assertArgIsBOOL(AppKit.NSDockTile.setShowsApplicationBadge_, 0)

    def testConstants(self):
        self.assertEqual(AppKit.NSAppKitVersionNumberWithDockTilePlugInSupport, 1001.0)

    @min_sdk_level("10.10")
    def testProtocol(self):
        objc.protocolNamed("NSDockTilePlugIn")
