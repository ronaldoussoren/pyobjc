from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKVerifiableClinicalRecordQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKVerifiableClinicalRecordQuery.initWithRecordTypes_predicate_resultsHandler_,
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKVerifiableClinicalRecordQuery.initWithRecordTypes_sourceTypes_predicate_resultsHandler_,
            3,
            b"v@@@",
        )
