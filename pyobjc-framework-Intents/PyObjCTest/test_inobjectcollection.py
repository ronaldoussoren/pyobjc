from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINObjectCollection(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(Intents.INObjectCollection.usesIndexedCollation)
        self.assertArgIsBOOL(Intents.INObjectCollection.setUsesIndexedCollation_, 0)
