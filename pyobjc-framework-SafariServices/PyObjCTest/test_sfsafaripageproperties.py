import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariPageProperties (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(SafariServices.SFSafariPageProperties.usesPrivateBrowsing)
            self.assertResultIsBOOL(SafariServices.SFSafariPageProperties.isActive)


if __name__ == "__main__":
    main()

