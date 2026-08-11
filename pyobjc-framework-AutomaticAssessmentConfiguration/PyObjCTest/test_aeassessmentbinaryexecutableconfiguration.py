import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAssessmentBinaryExecutableConfiguration(TestCase):
    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentBinaryExecutableConfiguration.isRequired
        )
        self.assertArgIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentBinaryExecutableConfiguration.setRequired_,
            0,
        )
