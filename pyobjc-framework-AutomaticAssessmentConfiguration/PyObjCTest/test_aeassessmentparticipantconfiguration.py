import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAssessmentParticipantConfiguration(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentParticipantConfiguration.allowsNetworkAccess
        )
        self.assertArgIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentParticipantConfiguration.setAllowsNetworkAccess_,
            0,
        )
