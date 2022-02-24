from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)
import objc
import GameController


class TestGCMicroGamepadSnapshot(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameController.GCMicroGamepadSnapshotDataVersion)

    @expectedFailureIf(os_release() == "10.11")
    @min_os_level("10.11")
    def testClasses(self):
        self.assertIsInstance(GameController.GCMicroGamepadSnapshot, objc.objc_class)

    @min_os_level("10.11")
    def testStructs(self):
        self.assertEqual(
            GameController.GCMicroGamepadSnapShotDataV100.__struct_pack__, 1
        )

        v = GameController.GCMicroGamepadSnapShotDataV100()
        self.assertIsInstance(v.version, int)
        self.assertIsInstance(v.size, int)
        self.assertIsInstance(v.dpadX, float)
        self.assertIsInstance(v.dpadY, float)
        self.assertIsInstance(v.buttonA, float)
        self.assertIsInstance(v.buttonX, float)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.14")
    def testStructs10_14_4(self):
        self.assertEqual(GameController.GCMicroGamepadSnapshotData.__struct_pack__, 1)

        v = GameController.GCMicroGamepadSnapshotData()
        self.assertIsInstance(v.version, int)
        self.assertIsInstance(v.size, int)
        self.assertIsInstance(v.dpadX, float)
        self.assertIsInstance(v.dpadY, float)
        self.assertIsInstance(v.buttonA, float)
        self.assertIsInstance(v.buttonX, float)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] in ("10.9", "10.10", "10.11"))
    @min_os_level("10.9")
    def testFunctions(self):
        self.assertResultIsBOOL(GameController.GCMicroGamepadSnapShotDataV100FromNSData)
        self.assertArgIsOut(GameController.GCMicroGamepadSnapShotDataV100FromNSData, 0)
        self.assertArgIsIn(GameController.NSDataFromGCMicroGamepadSnapShotDataV100, 0)

    @min_os_level("10.14.4")
    def testFunctions10_14_4(self):
        self.assertResultIsBOOL(GameController.GCMicroGamepadSnapshotDataFromNSData)
        self.assertArgIsOut(GameController.GCMicroGamepadSnapshotDataFromNSData, 0)
        self.assertArgIsIn(GameController.NSDataFromGCMicroGamepadSnapshotData, 0)

    def test_constants(self):
        self.assertEqual(GameController.GCMicroGamepadSnapshotDataVersion1, 0x0100)

    @min_os_level("10.14.4")
    def test_constants10_14_4(self):
        self.assertIsInstance(
            GameController.GCCurrentMicroGamepadSnapshotDataVersion, int
        )
