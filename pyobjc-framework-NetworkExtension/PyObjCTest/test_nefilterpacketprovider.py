from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import NetworkExtension

NEFilterPacketHandler = (
    objc._C_NSInteger
    + objc._C_ID
    + objc._C_ID
    + objc._C_NSInteger
    + objc._C_IN
    + objc._C_PTR
    + objc._C_VOID
    + objc._C_LNG
)


class TestNEFilterPacketProvider(TestCase):
    def test_constants(self):
        self.assertEqual(NetworkExtension.NEFilterPacketProviderVerdictAllow, 0)
        self.assertEqual(NetworkExtension.NEFilterPacketProviderVerdictDrop, 1)
        self.assertEqual(NetworkExtension.NEFilterPacketProviderVerdictDelay, 2)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBlock(
            NetworkExtension.NEFilterPacketProvider.packetHandler, NEFilterPacketHandler
        )
        self.assertArgIsBlock(
            NetworkExtension.NEFilterPacketProvider.setPacketHandler_,
            0,
            NEFilterPacketHandler,
        )
