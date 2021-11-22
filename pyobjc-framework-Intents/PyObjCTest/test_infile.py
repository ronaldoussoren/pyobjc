from PyObjCTools.TestSupport import TestCase
import Intents


class TestINFile(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Intents.INFile.removedOnCompletion)
        self.assertArgIsBOOL(Intents.INFile.setRemovedOnCompletion_, 0)
