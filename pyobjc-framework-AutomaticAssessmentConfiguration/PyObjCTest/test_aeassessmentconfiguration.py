import AutomaticAssessmentConfiguration
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAssessmentConfiguration(TestCase):
    @min_os_level("10.15.4")
    def testClasses(self):
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAssessmentConfiguration, objc.objc_class
        )
