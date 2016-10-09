from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTitlebarAccessoryViewController (TestCase):
    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSTitlebarAccessoryViewController.isHidden)
        self.assertArgIsBOOL(NSTitlebarAccessoryViewController.setHidden_, 0)

if __name__ == "__main__":
    main()
