import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


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
        self.assertEqual(
            AutomaticAssessmentConfiguration.AEAssessmentErrorRequiredParticipantsNotAvailable,
            5,
        )

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AENotInstalledParticipantsKey, str
        )
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AERestrictedSystemParticipantsKey, str
        )
