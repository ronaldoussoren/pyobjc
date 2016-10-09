import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariTab (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(SafariServices.SFSafariTab.getActivePageWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(SafariServices.SFSafariTab.getPagesWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(SafariServices.SFSafariTab.activateWithCompletionHandler_, 0, b'v')


if __name__ == "__main__":
    main()

