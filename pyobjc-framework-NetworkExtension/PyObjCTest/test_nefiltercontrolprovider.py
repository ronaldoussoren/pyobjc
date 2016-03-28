from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEFilterControlProvider (TestCase):
        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NEFilterControlProvider.handleRemediationForFlow_completionHandler_, 1, b'v@')
            self.assertArgIsBlock(NetworkExtension.NEFilterControlProvider.handleNewFlow_completionHandler_, 1, b'v@')


if __name__ == "__main__":
    main()
