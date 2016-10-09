import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariWindow (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(SafariServices.SFSafariWindow.getActiveTabWithCompletionHandler_, 0, b'v@')

            self.assertArgIsBOOL(SafariServices.SFSafariWindow.openTabWithURL_makeActiveIfPossible_completionHandler_, 1)
            self.assertArgIsBlock(SafariServices.SFSafariWindow.openTabWithURL_makeActiveIfPossible_completionHandler_, 2, b'v@')


            self.assertArgIsBlock(SafariServices.SFSafariWindow.getToolbarItemWithCompletionHandler_, 0, b'v@')


if __name__ == "__main__":
    main()

