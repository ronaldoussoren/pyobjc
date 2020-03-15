import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSButton(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSButton.isBordered)
        self.assertArgIsBOOL(AppKit.NSButton.setBordered_, 0)
        self.assertResultIsBOOL(AppKit.NSButton.isTransparent)
        self.assertArgIsBOOL(AppKit.NSButton.setTransparent_, 0)
        self.assertArgIsOut(AppKit.NSButton.getPeriodicDelay_interval_, 0)
        self.assertArgIsOut(AppKit.NSButton.getPeriodicDelay_interval_, 1)
        self.assertResultIsBOOL(AppKit.NSButton.performKeyEquivalent_)
        self.assertResultIsBOOL(AppKit.NSButton.allowsMixedState)
        self.assertArgIsBOOL(AppKit.NSButton.setAllowsMixedState_, 0)
        self.assertArgIsBOOL(AppKit.NSButton.setShowsBorderOnlyWhileMouseInside_, 0)
        self.assertResultIsBOOL(AppKit.NSButton.showsBorderOnlyWhileMouseInside)
        self.assertArgIsBOOL(AppKit.NSButton.highlight_, 0)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSButton.isSpringLoaded)
        self.assertArgIsBOOL(AppKit.NSButton.setSpringLoaded_, 0)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSButton.imageHugsTitle)
        self.assertArgIsBOOL(AppKit.NSButton.setImageHugsTitle_, 0)

        self.assertArgIsSEL(
            AppKit.NSButton.buttonWithTitle_image_target_action_, 3, b"v@:@"
        )
        self.assertArgIsSEL(AppKit.NSButton.buttonWithTitle_target_action_, 2, b"v@:@")
        self.assertArgIsSEL(AppKit.NSButton.buttonWithImage_target_action_, 2, b"v@:@")
        self.assertArgIsSEL(
            AppKit.NSButton.checkboxWithTitle_target_action_, 2, b"v@:@"
        )
        self.assertArgIsSEL(
            AppKit.NSButton.radioButtonWithTitle_target_action_, 2, b"v@:@"
        )
