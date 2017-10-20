from PyObjCTools.TestSupport import *
from AppKit import *
import sys


class TestNSWindowTabGroup (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        # Use subclass for testing because these methods aren't present
        # on the main class.

        class TestNSWindowTabGroupHelper (NSWindowTabGroup):
            def isOverviewVisible(self): return 1
            def setOverviewVisible_(self, v): pass

            def isTabBarVisible(self): return 1
            def setTabBarVisible_(self, v): pass

        self.assertResultIsBOOL(TestNSWindowTabGroupHelper.isOverviewVisible)
        self.assertArgIsBOOL(TestNSWindowTabGroupHelper.setOverviewVisible_, 0)

        self.assertResultIsBOOL(TestNSWindowTabGroupHelper.isTabBarVisible)
        self.assertArgIsBOOL(TestNSWindowTabGroupHelper.setTabBarVisible_, 0)


if __name__ == "__main__":
    main()
