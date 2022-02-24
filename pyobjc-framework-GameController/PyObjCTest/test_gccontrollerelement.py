from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCControllerElement(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameController.GCSystemGestureState)

    def test_constants(self):
        self.assertEqual(GameController.GCSystemGestureStateEnabled, 0)
        self.assertEqual(GameController.GCSystemGestureStateAlwaysReceive, 1)
        self.assertEqual(GameController.GCSystemGestureStateDisabled, 2)

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(GameController.GCControllerElement, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(GameController.GCControllerElement.isAnalog)

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            GameController.GCControllerElement.isBoundToSystemGesture
        )
