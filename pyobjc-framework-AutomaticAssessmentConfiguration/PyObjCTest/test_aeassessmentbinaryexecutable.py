import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAssessmentBinaryExecutable(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentBinaryExecutable.requiresSignatureValidation
        )
        self.assertArgIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentBinaryExecutable.setRequiresSignatureValidation_,
            0,
        )
