from PyObjCTools.TestSupport import *
from AppKit import *
import sys

class TestNSWindowTabGroup (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.asssertResultIsBOOL(NSWindowTabGroup.isOverviewVisible)
        self.asssertArgIsBOOL(NSWindowTabGroup.setOverviewVisible_, 0)

        self.asssertResultIsBOOL(NSWindowTabGroup.isTabBarVisible)
        self.asssertArgIsBOOL(NSWindowTabGroup.setTabBarVisible_, 0)


if __name__ == "__main__":
    main()
