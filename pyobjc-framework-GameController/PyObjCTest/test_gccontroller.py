from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)
import objc
import GameController


class TestGCController(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(GameController.GCController, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBlock(
            GameController.GCController.controllerPausedHandler, b"v@"
        )
        self.assertArgIsBlock(
            GameController.GCController.setControllerPausedHandler_, 0, b"v@"
        )

        self.assertResultIsBOOL(GameController.GCController.isAttachedToDevice)
        # self.assertArgIsBOOL(GameController.GCController.setAttachedToDevice_, 0)

        self.assertArgIsBlock(
            GameController.GCController.startWirelessControllerDiscoveryWithCompletionHandler_,
            0,
            b"v",
        )

    @expectedFailureIf(os_release() == "10.11")
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            GameController.GCEventViewController.controllerUserInteractionEnabled
        )
        self.assertArgIsBOOL(
            GameController.GCEventViewController.setControllerUserInteractionEnabled_, 0
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(GameController.GCController.isSnapshot)

    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(GameController.GCController.supportsHIDDevice_)

    @min_os_level("10.9")
    def test_constants(self):
        self.assertIsInstance(GameController.GCControllerDidConnectNotification, str)
        self.assertIsInstance(GameController.GCControllerDidDisconnectNotification, str)
        self.assertEqual(GameController.GCControllerPlayerIndexUnset, -1)

    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(
            GameController.GCControllerDidBecomeCurrentNotification, str
        )
        self.assertIsInstance(
            GameController.GCControllerDidStopBeingCurrentNotification, str
        )
