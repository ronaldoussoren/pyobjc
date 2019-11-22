from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEFilterDataProvider(TestCase):
        @min_os_level("10.15")
        def testMethods10_15(self):
            self.assertArgIsBlock(
                NetworkExtension.NEFilterDataProvider.applySettings_completionHandler_,
                1,
                b"v@",
            )


if __name__ == "__main__":
    main()
