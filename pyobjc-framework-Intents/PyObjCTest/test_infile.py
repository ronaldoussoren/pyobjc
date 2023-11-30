from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINFile(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(Intents.INFile.removedOnCompletion)
        self.assertArgIsBOOL(Intents.INFile.setRemovedOnCompletion_, 0)
