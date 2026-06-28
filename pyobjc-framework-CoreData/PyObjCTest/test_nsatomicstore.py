import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSAtomicStore(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreData.NSAtomicStore.load_)
        self.assertArgIsOut(CoreData.NSAtomicStore.load_, 0)
        self.assertResultIsBOOL(CoreData.NSAtomicStore.save_)
        self.assertArgIsOut(CoreData.NSAtomicStore.save_, 0)
