from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKAnchoredObjectQuery(TestCase):
    def test_constants(self):
        self.assertEqual(HealthKit.HKAnchoredObjectQueryNoAnchor, 0)

    def test_methods(self):
        self.assertResultIsBlock(
            HealthKit.HKAnchoredObjectQuery.updateHandler, b"v@@@@@"
        )
        self.assertArgIsBlock(
            HealthKit.HKAnchoredObjectQuery.setUpdateHandler_, 0, b"v@@@@@"
        )

        self.assertArgIsBlock(
            HealthKit.HKAnchoredObjectQuery.initWithType_predicate_anchor_limit_completionHandler_,
            4,
            b"v@@Q@",
        )
        self.assertArgIsBlock(
            HealthKit.HKAnchoredObjectQuery.initWithQueryDescriptors_anchor_limit_resultsHandler_,
            3,
            b"v@@@@@",
        )
