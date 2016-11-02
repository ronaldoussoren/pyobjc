from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSliderAccessory (TestCase):
    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSSliderAccessory.isEnabled)
        self.assertArgIsBOOL(NSSliderAccessory.setEnabled_, 0)

        self.assertArgIsBlock(NSSliderAccessoryBehavior.behaviorWithHandler_, 0, b'v@')

if __name__ == "__main__":
    main()
