from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCExtendedGamepadSnapshot(TestCase):
    def test_constants(self):
        self.assertEqual(GameController.GCExtendedGamepadSnapshotDataVersion1, 0x0100)
        self.assertEqual(GameController.GCExtendedGamepadSnapshotDataVersion2, 0x0101)

    @min_os_level("10.14.4")
    def test_constants_10_14_4(self):
        self.assertIsInstance(
            GameController.GCCurrentExtendedGamepadSnapshotDataVersion, int
        )

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(GameController.GCExtendedGamepadSnapshot, objc.objc_class)

    @min_os_level("10.9")
    def testFunctions(self):
        self.assertResultIsBOOL(
            GameController.GCExtendedGamepadSnapShotDataV100FromNSData
        )
        self.assertArgIsOut(
            GameController.GCExtendedGamepadSnapShotDataV100FromNSData, 0
        )

        self.assertArgIsOut(
            GameController.GCExtendedGamepadSnapShotDataV100FromNSData, 0
        )

    @min_os_level("10.9")
    def test_structs(self):
        self.assertEqual(
            GameController.GCExtendedGamepadSnapShotDataV100.__struct_pack__, 1
        )

        v = GameController.GCExtendedGamepadSnapShotDataV100()
        self.assertIsInstance(v.version, int)
        self.assertIsInstance(v.size, int)
        self.assertIsInstance(v.dpadX, float)
        self.assertIsInstance(v.dpadY, float)
        self.assertIsInstance(v.buttonA, float)
        self.assertIsInstance(v.buttonB, float)
        self.assertIsInstance(v.buttonX, float)
        self.assertIsInstance(v.buttonY, float)
        self.assertIsInstance(v.leftShoulder, float)
        self.assertIsInstance(v.rightShoulder, float)
        self.assertIsInstance(v.leftThumbstickX, float)
        self.assertIsInstance(v.leftThumbstickY, float)
        self.assertIsInstance(v.rightThumbstickX, float)
        self.assertIsInstance(v.rightThumbstickY, float)
        self.assertIsInstance(v.leftTrigger, float)
        self.assertIsInstance(v.rightTrigger, float)

    @min_os_level("10.14.1")
    def test_structs_10_14_1(self):
        # XXX: Introduced in the 10.14.4 SDK
        self.assertEqual(
            GameController.GCExtendedGamepadSnapshotData.__struct_pack__, 1
        )

        v = GameController.GCExtendedGamepadSnapshotData()
        self.assertIsInstance(v.version, int)
        self.assertIsInstance(v.size, int)
        self.assertIsInstance(v.dpadX, float)
        self.assertIsInstance(v.dpadY, float)
        self.assertIsInstance(v.buttonA, float)
        self.assertIsInstance(v.buttonB, float)
        self.assertIsInstance(v.buttonX, float)
        self.assertIsInstance(v.buttonY, float)
        self.assertIsInstance(v.leftShoulder, float)
        self.assertIsInstance(v.rightShoulder, float)
        self.assertIsInstance(v.leftThumbstickX, float)
        self.assertIsInstance(v.leftThumbstickY, float)
        self.assertIsInstance(v.rightThumbstickX, float)
        self.assertIsInstance(v.rightThumbstickY, float)
        self.assertIsInstance(v.leftTrigger, float)
        self.assertIsInstance(v.rightTrigger, float)

        self.assertEqual(v.supportsClickableThumbsticks, False)
        self.assertEqual(v.leftThumbstickButton, False)
        self.assertEqual(v.rightThumbstickButton, False)

    @min_os_level("10.14.4")
    def test_functions_10_14_4(self):
        self.assertArgIsOut(GameController.GCExtendedGamepadSnapshotDataFromNSData, 0)
        self.assertResultIsBOOL(GameController.GCExtendedGamepadSnapshotDataFromNSData)

        self.assertArgIsIn(GameController.NSDataFromGCExtendedGamepadSnapshotData, 0)
