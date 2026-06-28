import Automator
from PyObjCTools.TestSupport import TestCase


class TestAMWorkflowView(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Automator.AMWorkflowView.isEditable)
        self.assertArgIsBOOL(Automator.AMWorkflowView.setEditable_, 0)
