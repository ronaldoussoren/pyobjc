import AutomaticAssessmentConfiguration
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAssessmentConfiguration(TestCase):
    @min_os_level("10.15.4")
    def testClasses(self):
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration, objc.objc_class
        )

    @min_os_level("26.1")
    def test_methods26_1(self):
        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration.allowsAccessibilityKeyboard
        )
        self.assertArgIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration.setAllowsAccessibilityKeyboard_,
            0,
        )

        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration.allowsAccessibilityLiveCaptions
        )
        self.assertArgIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration.setAllowsAccessibilityLiveCaptions_,
            0,
        )

        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration.allowsAccessibilityReader
        )
        self.assertArgIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration.setAllowsAccessibilityReader_,
            0,
        )
