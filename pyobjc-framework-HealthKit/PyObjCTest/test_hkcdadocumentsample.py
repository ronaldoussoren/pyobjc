from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKCDADocumentSample(TestCase):
    def test_constants13_0(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathCDATitle, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathCDAPatientName, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathCDAAuthorName, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathCDACustodianName, str)
        self.assertIsInstance(HealthKit.HKDetailedCDAValidationErrorKey, str)

    def test_methods(self):
        self.assertArgIsOut(
            HealthKit.HKCDADocumentSample.CDADocumentSampleWithData_startDate_endDate_metadata_validationError_,
            4,
        )
