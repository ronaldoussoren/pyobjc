from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSSlider (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSSlider.allowsTickMarkValuesOnly)
        self.assertArgIsBOOL(NSSlider.setAllowsTickMarkValuesOnly_, 0)
        self.assertResultIsBOOL(NSSlider.acceptsFirstMouse_)

if __name__ == "__main__":
    main()
