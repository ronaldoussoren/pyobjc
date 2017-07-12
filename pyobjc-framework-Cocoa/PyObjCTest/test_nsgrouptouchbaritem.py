from PyObjCTools.TestSupport import *

import AppKit

class TestNSGroupTouchBarItem (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSGroupTouchBarItem.prefersEqualWidths)
        self.assertArgIsBOOL(AppKit.NSGroupTouchBarItem.setPrefersEqualWidths_, 0)


if __name__ == "__main__":
    main()
