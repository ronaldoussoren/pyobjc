import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSEntityDescription(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSEntityDescription.isAbstract)
        self.assertArgIsBOOL(CoreData.NSEntityDescription.setAbstract_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(CoreData.NSEntityDescription.isKindOfEntity_)
