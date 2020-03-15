import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSliderAccessory(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSSliderAccessory.isEnabled)
        self.assertArgIsBOOL(AppKit.NSSliderAccessory.setEnabled_, 0)

        self.assertArgIsBlock(
            AppKit.NSSliderAccessoryBehavior.behaviorWithHandler_, 0, b"v@"
        )
