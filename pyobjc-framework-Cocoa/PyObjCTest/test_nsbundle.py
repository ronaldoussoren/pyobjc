import AppKit
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSBundle(TestCase):
    def testMethods(self):
        b = AppKit.NSBundle.mainBundle()
        # Test on an instance because AppKit.NSBundle has class methods
        # that interfere with this test
        self.assertResultIsBOOL(b.load)
        self.assertResultIsBOOL(b.isLoaded)
        self.assertResultIsBOOL(b.unload)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AppKit.NSBundle.loadNibNamed_owner_topLevelObjects_)
        self.assertArgIsOut(AppKit.NSBundle.loadNibNamed_owner_topLevelObjects_, 2)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(AppKit.NSBundle.preflightAndReturnError_)
        self.assertArgIsOut(AppKit.NSBundle.preflightAndReturnError_, 0)
        self.assertResultIsBOOL(AppKit.NSBundle.loadAndReturnError_)
        self.assertArgIsOut(AppKit.NSBundle.loadAndReturnError_, 0)

    def testConstants(self):
        self.assertEqual(AppKit.NSBundleExecutableArchitectureI386, 0x00000007)
        self.assertEqual(AppKit.NSBundleExecutableArchitecturePPC, 0x00000012)
        self.assertEqual(AppKit.NSBundleExecutableArchitectureX86_64, 0x01000007)
        self.assertEqual(AppKit.NSBundleExecutableArchitecturePPC64, 0x01000012)
        self.assertEqual(AppKit.NSBundleExecutableArchitectureARM64, 0x0100000C)

        self.assertIsInstance(AppKit.NSBundleDidLoadNotification, str)
        self.assertIsInstance(AppKit.NSLoadedClasses, str)

    def testDefines(self):
        self.assertHasAttr(Foundation, "NSLocalizedString")
        self.assertHasAttr(Foundation, "NSLocalizedStringFromTable")
        self.assertHasAttr(Foundation, "NSLocalizedStringFromTableInBundle")
        self.assertHasAttr(Foundation, "NSLocalizedStringWithDefaultValue")
