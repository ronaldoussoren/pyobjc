from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCMotion(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(GameController.GCMotion, objc.objc_class)

    @min_os_level("10.10")
    def test_structs(self):
        v = GameController.GCAcceleration()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)

        v = GameController.GCRotationRate()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)

        v = GameController.GCQuaternion()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)
        self.assertIsInstance(v.w, float)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBlock(GameController.GCMotion.valueChangedHandler, b"v@")
        self.assertArgIsBlock(GameController.GCMotion.setValueChangedHandler_, 0, b"v@")

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(GameController.GCMotion.hasAttitudeAndRotationRate)

    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(GameController.GCMotion.sensorsRequireManualActivation)

        self.assertResultIsBOOL(GameController.GCMotion.sensorsActive)
        self.assertArgIsBOOL(GameController.GCMotion.setSensorsActive_, 0)

        self.assertResultIsBOOL(GameController.GCMotion.hasAttitude)
        self.assertResultIsBOOL(GameController.GCMotion.hasRotationRate)

        self.assertResultIsBOOL(GameController.GCMotion.hasGravityAndUserAcceleration)
