import AutomaticAssessmentConfiguration
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAEAssessmentSession(TestCase):
    @min_os_level("10.15.4")
    def testClasses(self):
        self.assertIsInstance(
            AutomaticAssessmentConfiguration.AEAssessmentSession, objc.objc_class
        )

    @min_os_level("10.15.4")
    def test_methods(self):
        self.assertResultIsBOOL(
            AutomaticAssessmentConfiguration.AEAssessmentSession.isActive
        )
