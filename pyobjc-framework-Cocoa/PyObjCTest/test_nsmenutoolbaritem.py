from PyObjCTools.TestSupport import *
import AppKit


class TestNSMenuToolbarItem(TestCase):
    @min_sdk_level("10.15")
    def test_nethods10_15(self):
        self.assertResultIsBOOL(AppKit.NSMenuToolbarItem.showsIndicator)
        self.assertArgIsBOOL(AppKit.NSMenuToolbarItem.setShowsIndicator_, 0)


if __name__ == "__main__":
    main()
