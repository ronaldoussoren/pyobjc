from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKDialogController(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(GameCenter.GKDialogController.presentViewController_)

    def test_protocols(self):
        self.assertProtocolExists("GKViewController", GameCenter)
