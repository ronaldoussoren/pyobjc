from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSPopoverTouchBarItem (TestCase):
    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSPopoverTouchBarItem.showsCloseButton)
        self.assertArgIsBOOL(NSPopoverTouchBarItem.setShowsCloseButton_, 0)

if __name__ == "__main__":
    main()
