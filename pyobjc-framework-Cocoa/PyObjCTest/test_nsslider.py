from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSSlider (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSlider.allowsTickMarkValuesOnly)
        self.failUnlessArgIsBOOL(NSSlider.setAllowsTickMarkValuesOnly_, 0)
        self.failUnlessResultIsBOOL(NSSlider.acceptsFirstMouse_)

if __name__ == "__main__":
    main()
