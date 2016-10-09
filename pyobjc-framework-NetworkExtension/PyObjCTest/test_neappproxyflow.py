from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEAppProxyFlow (TestCase):

        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorNotConnected, 1)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorPeerReset, 2)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorHostUnreachable, 3)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorInvalidArgument, 4)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorAborted, 5)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorRefused, 6)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorTimedOut, 7)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorInternal, 8)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorDatagramTooLarge, 9)
            self.assertEqual(NetworkExtension.NEAppProxyFlowErrorReadAlreadyPending, 10)

            self.assertIsInstance(NetworkExtension.NEAppProxyErrorDomain, unicode)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NEAppProxyFlow.openWithLocalEndpoint_completionHandler_, 1, b'v@')


if __name__ == "__main__":
    main()
