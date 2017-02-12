import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariToolbarItem (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBOOL(SafariServices.SFSafariToolbarItem.setEnabled_withBadgeText_, 0)
            self.assertArgIsBOOL(SafariServices.SFSafariToolbarItem.setEnabled_, 0)


if __name__ == "__main__":
    main()

