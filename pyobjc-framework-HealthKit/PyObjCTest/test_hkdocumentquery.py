from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKDocumentQuery(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKDocumentQuery.includeDocumentData)
        self.assertArgIsBOOL(
            HealthKit.HKDocumentQuery.initWithDocumentType_predicate_limit_sortDescriptors_includeDocumentData_resultsHandler_,
            4,
        )
        self.assertArgIsBlock(
            HealthKit.HKDocumentQuery.initWithDocumentType_predicate_limit_sortDescriptors_includeDocumentData_resultsHandler_,
            5,
            b"v@@Z@",
        )
