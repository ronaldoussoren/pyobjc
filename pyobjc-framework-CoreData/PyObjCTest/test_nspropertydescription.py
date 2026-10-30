import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSPropertyDescription(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreData.NSPropertyDescription.isOptional)
        self.assertArgIsBOOL(CoreData.NSPropertyDescription.setOptional_, 0)

        self.assertResultIsBOOL(CoreData.NSPropertyDescription.isTransient)
        self.assertArgIsBOOL(CoreData.NSPropertyDescription.setTransient_, 0)

        self.assertResultIsBOOL(CoreData.NSPropertyDescription.isIndexed)
        self.assertArgIsBOOL(CoreData.NSPropertyDescription.setIndexed_, 0)

        self.assertResultIsBOOL(CoreData.NSPropertyDescription.isIndexedBySpotlight)
        self.assertArgIsBOOL(CoreData.NSPropertyDescription.setIndexedBySpotlight_, 0)
        self.assertResultIsBOOL(CoreData.NSPropertyDescription.isStoredInExternalRecord)
        self.assertArgIsBOOL(
            CoreData.NSPropertyDescription.setStoredInExternalRecord_, 0
        )
