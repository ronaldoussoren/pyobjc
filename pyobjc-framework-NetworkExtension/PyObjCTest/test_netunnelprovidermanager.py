from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNETunnelProviderManager (TestCase):
        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NETunnelProviderManager.loadAllFromPreferencesWithCompletionHandler_, 0, b'v@@')


if __name__ == "__main__":
    main()
