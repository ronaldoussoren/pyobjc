from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSSlider (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSSlider.allowsTickMarkValuesOnly)
        self.assertArgIsBOOL(NSSlider.setAllowsTickMarkValuesOnly_, 0)
        self.assertResultIsBOOL(NSSlider.acceptsFirstMouse_)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSSlider.isVertical)
        self.assertArgIsBOOL(NSSlider.setVertical_, 0)
        self.assertArgIsSEL(NSSlider.sliderWithValue_minValue_maxValue_target_action_, 4, b'v@:@')

if __name__ == "__main__":
    main()
