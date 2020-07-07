from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCControllerTouchpad(TestCase):
    def test_constants(self):
        self.assertEqual(GameController.GCTouchStateUp, 0)
        self.assertEqual(GameController.GCTouchStateDown, 1)
        self.assertEqual(GameController.GCTouchStateMoving, 2)

    @min_os_level("10.16")
    def test_methods(self):
        self.assertResultIsBlock(
            GameController.GCControllerTouchpad.touchDown, b"vfff" + objc._C_NSBOOL
        )
        self.assertArgIsBlock(
            GameController.GCControllerTouchpad.setTouchDown_,
            0,
            b"vfff" + objc._C_NSBOOL,
        )

        self.assertResultIsBlock(
            GameController.GCControllerTouchpad.touchMoved, b"vfff" + objc._C_NSBOOL
        )
        self.assertArgIsBlock(
            GameController.GCControllerTouchpad.setTouchMoved_,
            0,
            b"vfff" + objc._C_NSBOOL,
        )

        self.assertResultIsBlock(
            GameController.GCControllerTouchpad.touchUp, b"vfff" + objc._C_NSBOOL
        )
        self.assertArgIsBlock(
            GameController.GCControllerTouchpad.setTouchUp_, 0, b"vfff" + objc._C_NSBOOL
        )

        self.assertResultIsBOOL(
            GameController.GCControllerTouchpad.reportsAbsoluteTouchSurfaceValues
        )
        self.assertArgIsBOOL(
            GameController.GCControllerTouchpad.setReportsAbsoluteTouchSurfaceValues_, 0
        )

        self.assertArgIsBOOL(
            GameController.GCControllerTouchpad.setValueForXAxis_yAxis_touchDown_buttonValue_,
            2,
        )
