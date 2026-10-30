import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSEntityDescription(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreData.NSEntityDescription.isAbstract)
        self.assertArgIsBOOL(CoreData.NSEntityDescription.setAbstract_, 0)

        self.assertResultIsBOOL(CoreData.NSEntityDescription.isKindOfEntity_)
