from PyObjCTools.TestSupport import *
from AppKit import *
import sys

class TestNSWindowTabGroup (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(NSWindowTabGroup.isOverviewVisible)
        self.assertArgIsBOOL(NSWindowTabGroup.setOverviewVisible_, 0)

        self.assertResultIsBOOL(NSWindowTabGroup.isTabBarVisible)
        self.assertArgIsBOOL(NSWindowTabGroup.setTabBarVisible_, 0)


if __name__ == "__main__":
    main()
