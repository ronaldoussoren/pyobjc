import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase


class TestAEErrors(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAssessmentErrorDomain, str
        )

        self.assertIsEnumType(AutomaticAssessmentConfiguration.AEAssessmentErrorCode)
        self.assertEqual(AutomaticAssessmentConfiguration.AEAssessmentErrorUnknown, 1)
        self.assertEqual(
            AutomaticAssessmentConfiguration.AEAssessmentErrorUnsupportedPlatform, 2
        )
        self.assertEqual(
            AutomaticAssessmentConfiguration.AEAssessmentErrorMultipleParticipantsNotSupported,
            3,
        )
        self.assertEqual(
            AutomaticAssessmentConfiguration.AEAssessmentErrorConfigurationUpdatesNotSupported,
            4,
        )
