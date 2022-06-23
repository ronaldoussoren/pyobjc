from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKSourceQuery(TestCase):
    def test_methods(self):
        self.assertIsInstance(
            HealthKit.HKSourceQuery.initWithSampleType_samplePredicate_completionHanlder_,
            2,
            b"v@@@",
        )
