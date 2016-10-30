import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFContentBlockerManager (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(SafariServices.SFSafariApplication.getActiveWindowWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(SafariServices.SFSafariApplication.openWindowWithURL_completionHandler_, 1, b'v@')
            self.assertArgIsBlock(SafariServices.SFSafariApplication.showPreferencesForExtensionWithIdentifier_completionHandler_, 1, b'v@')


if __name__ == "__main__":
    main()

