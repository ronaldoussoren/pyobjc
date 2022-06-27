from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKSourceQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKSourceQuery.initWithSampleType_samplePredicate_completionHandler_,
            2,
            b"v@@@",
        )
