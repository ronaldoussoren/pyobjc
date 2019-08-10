import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariExtension(TestCase):
        @min_os_level("10.14.4")
        def testMethods(self):
            self.assertArgIsBlock(
                SafariServices.SFSafariExtension.getBaseURIWithCompletionHandler_,
                0,
                b"v@",
            )


if __name__ == "__main__":
    main()
