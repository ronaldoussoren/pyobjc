from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINObjectCollection(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(Intents.INObjectCollection.usesIndexedCollation)
        self.assertArgIsBOOL(Intents.INObjectCollection.setUsesIndexedCollation_, 0)
