import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSAtomicStore(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSAtomicStore.load_)
        self.assertArgIsOut(CoreData.NSAtomicStore.load_, 0)
        self.assertResultIsBOOL(CoreData.NSAtomicStore.save_)
        self.assertArgIsOut(CoreData.NSAtomicStore.save_, 0)
