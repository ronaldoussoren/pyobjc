from PyObjCTools.TestSupport import *

import AutomaticAssessmentConfiguration

class TestFramework (TestCase):
    @min_os_level('10.15.4')
    def testClasses(self):
        AutomaticAssessmentConfiguration.AEAssessmentConfiguration

    @min_os_level('10.15.4')
    def testMethods(self):
        self.assertArgIsBlock(AutomaticAssessmentConfiguration.AEAssessmentSession.endWithCompletion_, 0, b'v@')
        self.assertArgIsBlock(AutomaticAssessmentConfiguration.AEAssessmentSession.beginSessionWithConfiguration_completion_, 1, b'v@@')
