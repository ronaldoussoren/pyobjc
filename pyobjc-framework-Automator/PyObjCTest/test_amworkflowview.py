import Automator
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAMWorkflowView(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Automator.AMWorkflowView.isEditable)
        self.assertArgIsBOOL(Automator.AMWorkflowView.setEditable_, 0)
