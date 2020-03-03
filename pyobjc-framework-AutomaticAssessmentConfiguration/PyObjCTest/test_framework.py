import AutomaticAssessmentConfiguration
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAEAssessmentSessionDelegateHelper(AutomaticAssessmentConfiguration.NSObject):
    def assessmentSessionDidBegin_(self, a):
        pass

    def assessmentSessionDidFailToBegin_error_(self, a, b):
        pass

    def assessmentSessionDidInterrupt_error_(self, a, b):
        pass

    def assessmentSessionDidEnd_(self, a):
        pass


class TestFramework(TestCase):
    @min_os_level("10.15.4")
    def testClasses(self):
        AutomaticAssessmentConfiguration.AEAssessmentConfiguration

    # @min_os_level('10.15.4')
    # def testMethods(self):
    #    # Gone in SDK 11.4 beta 2
    #    self.assertArgIsBlock(AutomaticAssessmentConfiguration.AEAssessmentSession.endWithCompletion_, 0, b'v@')  # noqa: B950
    #    self.assertArgIsBlock(AutomaticAssessmentConfiguration.AEAssessmentSession.beginSessionWithConfiguration_completion_, 1, b'v@@')  # noqa: B950

    @min_sdk_level("10.15.4")
    def testProtocols(self):
        objc.protocolNamed(
            "AutomaticAssessmentConfiguration.AEAssessmentSessionDelegate"
        )
