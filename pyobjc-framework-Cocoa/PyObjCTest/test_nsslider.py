import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSlider(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSlider.allowsTickMarkValuesOnly)
        self.assertArgIsBOOL(AppKit.NSSlider.setAllowsTickMarkValuesOnly_, 0)
        self.assertResultIsBOOL(AppKit.NSSlider.acceptsFirstMouse_)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSSlider.isVertical)
        self.assertArgIsBOOL(AppKit.NSSlider.setVertical_, 0)
        self.assertArgIsSEL(
            AppKit.NSSlider.sliderWithValue_minValue_maxValue_target_action_, 4, b"v@:@"
        )
