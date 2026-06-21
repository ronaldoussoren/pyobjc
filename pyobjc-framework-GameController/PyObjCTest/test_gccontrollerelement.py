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
    def test_classes(self):
        self.assertIsInstance(GameController.GCControllerElement, objc.objc_class)

    @min_os_level("10.9")
    def test_methods(self):
        self.assertResultIsBOOL(GameController.GCControllerElement.isAnalog)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            GameController.GCControllerElement.isBoundToSystemGesture
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            GameController.GCControllerElement.isBoundToSystemGesture
        )
