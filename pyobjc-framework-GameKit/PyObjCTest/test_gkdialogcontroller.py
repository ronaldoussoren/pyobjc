import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKDialogController(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(GameKit.GKDialogController.presentViewController_)
