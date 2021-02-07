from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCEventViewController(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            GameController.GCEventViewController.controllerUserInteractionEnabled
        )
        self.assertArgIsBOOL(
            GameController.GCEventViewController.setControllerUserInteractionEnabled_, 0
        )
