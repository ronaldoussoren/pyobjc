from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameController.GCControllerPlayerIndex)

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

    @min_os_level("10.12")
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

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(GameController.GCController.supportsHIDDevice_)

    @min_os_level("11.3")
    def testMethods11_3(self):
        self.assertResultIsBOOL(
            GameController.GCController.shouldMonitorBackgroundEvents
        )
        self.assertArgIsBOOL(
            GameController.GCController.setShouldMonitorBackgroundEvents_, 0
        )

    @min_os_level("10.9")
    def test_constants(self):
        self.assertIsInstance(GameController.GCControllerDidConnectNotification, str)
        self.assertIsInstance(GameController.GCControllerDidDisconnectNotification, str)
        self.assertEqual(GameController.GCControllerPlayerIndexUnset, -1)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(
            GameController.GCControllerDidBecomeCurrentNotification, str
        )
        self.assertIsInstance(
            GameController.GCControllerDidStopBeingCurrentNotification, str
        )

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(
            GameController.GCControllerUserCustomizationsDidChangeNotification, str
        )
