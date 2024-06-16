from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKGAD7Assessment(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKGAD7AssessmentRisk)
        self.assertEqual(HealthKit.HKGAD7AssessmentRiskNoneToMinimal, 1)
        self.assertEqual(HealthKit.HKGAD7AssessmentRiskMild, 2)
        self.assertEqual(HealthKit.HKGAD7AssessmentRiskModerate, 3)
        self.assertEqual(HealthKit.HKGAD7AssessmentRiskSevere, 4)

        self.assertIsEnumType(HealthKit.HKGAD7AssessmentAnswer)
        self.assertEqual(HealthKit.HKGAD7AssessmentAnswerNotAtAll, 0)
        self.assertEqual(HealthKit.HKGAD7AssessmentAnswerSeveralDays, 1)
        self.assertEqual(HealthKit.HKGAD7AssessmentAnswerMoreThanHalfTheDays, 2)
        self.assertEqual(HealthKit.HKGAD7AssessmentAnswerNearlyEveryDay, 3)
