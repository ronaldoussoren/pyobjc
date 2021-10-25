import AutomaticAssessmentConfiguration
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAssessmentApplication(TestCase):
    @min_os_level("12.0")
    def testClasses(self):
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAssessmentApplication, objc.objc_class
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentApplication.requiresSignatureValidation
        )
        self.assertArgIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentApplication.setRequiresSignatureValidation_,
            0,
        )
