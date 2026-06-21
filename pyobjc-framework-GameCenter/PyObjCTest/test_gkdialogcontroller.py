import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKDialogController(TestCase):
    @min_os_level("10.8")
    def test_classes10_8(self):
        self.assertIsInstance(GameCenter.GKDialogController, objc.objc_class)

        self.assertResultIsBOOL(GameCenter.GKDialogController.presentViewController_)

    @min_os_level("10.8")
    def test_protocols10_8(self):
        self.assertProtocolExists("GKViewController", GameCenter)
