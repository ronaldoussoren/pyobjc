import objc
import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSUserInterfaceCompression(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(
            AppKit.NSUserInterfaceCompressionOptions.containsOptions_
        )
        self.assertResultIsBOOL(
            AppKit.NSUserInterfaceCompressionOptions.intersectsOptions_
        )
        self.assertResultIsBOOL(AppKit.NSUserInterfaceCompressionOptions.isEmpty)
        # self.assertArgIsBOOL(AppKit.NSUserInterfaceCompressionOptions.setEmpty_)

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("NSUserInterfaceCompression")
