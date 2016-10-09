import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariExtensionManager (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(SafariServices.SFSafariExtensionManager.getStateOfSafariExtensionWithIdentifier_completionHandler_, 1, b'v@@')


if __name__ == "__main__":
    main()

