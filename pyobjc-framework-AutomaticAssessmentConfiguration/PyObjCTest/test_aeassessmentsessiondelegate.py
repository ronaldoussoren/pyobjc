import AutomaticAssessmentConfiguration
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAEAssessmentSessionDelegateHelper(AutomaticAssessmentConfiguration.NSObject):
    def assessmentSessionDidBegin_(self, a):
        pass

    def assessmentSessionDidFailToBegin_error_(self, a, b):
        pass

    def assessmentSessionDidInterrupt_error_(self, a, b):
        pass

    def assessmentSessionDidEnd_(self, a):
        pass


class TestAEAssessmentSessionDelegate(TestCase):
    @min_sdk_level("10.15.4")
    def testProtocols(self):
        self.assertProtocolExists("AEAssessmentSessionDelegate")
