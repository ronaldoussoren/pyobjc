from PyObjCTools.TestSupport import TestCase
import HealthKit


class HKPHQ9Assessment(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKPHQ9AssessmentRisk)
        self.assertEqual(HealthKit.HKPHQ9AssessmentRiskNoneToMinimal, 1)
        self.assertEqual(HealthKit.HKPHQ9AssessmentRiskMild, 2)
        self.assertEqual(HealthKit.HKPHQ9AssessmentRiskModerate, 3)
        self.assertEqual(HealthKit.HKPHQ9AssessmentRiskModeratelySevere, 4)
        self.assertEqual(HealthKit.HKPHQ9AssessmentRiskSevere, 5)

        self.assertIsEnumType(HealthKit.HKPHQ9AssessmentAnswer)
        self.assertEqual(HealthKit.HKPHQ9AssessmentAnswerNotAtAll, 0)
        self.assertEqual(HealthKit.HKPHQ9AssessmentAnswerSeveralDays, 1)
        self.assertEqual(HealthKit.HKPHQ9AssessmentAnswerMoreThanHalfTheDays, 2)
        self.assertEqual(HealthKit.HKPHQ9AssessmentAnswerNearlyEveryDay, 3)
        self.assertEqual(HealthKit.HKPHQ9AssessmentAnswerPreferNotToAnswer, 4)
