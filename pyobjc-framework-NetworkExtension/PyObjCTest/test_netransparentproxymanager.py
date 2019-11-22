from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNETransparentProxyManager(TestCase):
        @min_os_level("10.15")
        def testMethods10_15(self):
            self.assertArgIsBlock(
                NetworkExtension.NETransparentProxyManager.loadAllFromPreferencesWithCompletionHandler_,
                0,
                b"v@@",
            )


if __name__ == "__main__":
    main()
