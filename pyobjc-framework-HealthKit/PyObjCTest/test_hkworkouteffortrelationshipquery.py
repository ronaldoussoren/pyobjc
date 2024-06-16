from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKWorkoutEffortRelationshipQuery(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKWorkoutEffortRelationshipQueryOptions)
        self.assertEqual(HealthKit.HKWorkoutEffortRelationshipQueryOptionsDefault, 0)
        self.assertEqual(
            HealthKit.HKWorkoutEffortRelationshipQueryOptionsMostRelevant, 1 << 0
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertArgIsBlock(
            HealthKit.HKWorkoutEffortRelationshipQuery.initWithPredicate_anchor_options_resultsHandler_,
            3,
            b"v@@@@",
        )
