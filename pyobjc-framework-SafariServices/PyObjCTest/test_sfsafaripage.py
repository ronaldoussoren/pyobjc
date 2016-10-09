import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariPage (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(SafariServices.SFSafariPage.getPagePropertiesWithCompletionHandler_, 0, b'v@')


if __name__ == "__main__":
    main()

