import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFUniversalLink(TestCase):
        @min_os_level("10.15")
        def testMethods(self):
            self.assertResultIsBOOL(SafariServices.SFUniversalLink.isEnabled)
            self.assertArgIsBOOL(SafariServices.SFUniversalLink.setEnabled_, 0)


if __name__ == "__main__":
    main()
