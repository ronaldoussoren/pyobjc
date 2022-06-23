from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKObserverQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKObserverQuery.initWithSampleType_predicate_updateHandler_,
            2,
            b"v@@?@",
        )  # XXX
        self.assertArgIsBlock(
            HealthKit.HKObserverQuery.initWithQueryDescriptors_updateHandler_,
            1,
            b"v@@@?@",
        )  # XXX
