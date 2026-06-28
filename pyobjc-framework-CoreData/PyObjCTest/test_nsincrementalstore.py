import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSIncrementalStore(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreData.NSIncrementalStore.loadMetadata_)
        self.assertArgIsOut(CoreData.NSIncrementalStore.loadMetadata_, 0)
        self.assertArgIsOut(
            CoreData.NSIncrementalStore.executeRequest_withContext_error_, 2
        )
        self.assertArgIsOut(
            CoreData.NSIncrementalStore.newValuesForObjectWithID_withContext_error_, 2
        )
        self.assertArgIsOut(
            CoreData.NSIncrementalStore.newValueForRelationship_forObjectWithID_withContext_error_,
            3,
        )
        self.assertArgIsOut(
            CoreData.NSIncrementalStore.obtainPermanentIDsForObjects_error_, 1
        )
