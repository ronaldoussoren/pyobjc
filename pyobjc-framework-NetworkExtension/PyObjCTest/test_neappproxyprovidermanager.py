from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEAppProxyProviderManager (TestCase):
        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NEAppProxyProviderManager.loadAllFromPreferencesWithCompletionHandler_, 0, b'v@@')


if __name__ == "__main__":
    main()
