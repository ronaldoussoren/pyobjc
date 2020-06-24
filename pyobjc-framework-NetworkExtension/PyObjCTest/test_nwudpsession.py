from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNWTCPConnection(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(NetworkExtension.NWUDPSessionStateInvalid, 0)
        self.assertEqual(NetworkExtension.NWUDPSessionStateWaiting, 1)
        self.assertEqual(NetworkExtension.NWUDPSessionStatePreparing, 2)
        self.assertEqual(NetworkExtension.NWUDPSessionStateReady, 3)
        self.assertEqual(NetworkExtension.NWUDPSessionStateFailed, 4)
        self.assertEqual(NetworkExtension.NWUDPSessionStateCancelled, 5)

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(NetworkExtension.NWUDPSession.isViable)
        self.assertResultIsBOOL(NetworkExtension.NWUDPSession.hasBetterPath)

        self.assertArgIsBlock(
            NetworkExtension.NWUDPSession.setReadHandler_maxDatagrams_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            NetworkExtension.NWUDPSession.writeDatagram_completionHandler_, 1, b"v@"
        )
