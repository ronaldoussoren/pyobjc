import Automator
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAMWorkspace(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(Automator.AMWorkspace.runWorkflowAtPath_withInput_error_, 2)
