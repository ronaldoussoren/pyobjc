import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKDialogController(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKDialogController.presentViewController_)
