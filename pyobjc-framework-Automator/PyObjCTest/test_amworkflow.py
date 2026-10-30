import Automator
from PyObjCTools.TestSupport import TestCase


class TestAMWorkflow(TestCase):
    def test_methods(self):
        self.assertArgIsOut(Automator.AMWorkflow.runWorkflowAtURL_withInput_error_, 2)
        self.assertArgIsOut(Automator.AMWorkflow.initWithContentsOfURL_error_, 1)
        self.assertResultIsBOOL(Automator.AMWorkflow.writeToURL_error_)
        self.assertArgIsOut(Automator.AMWorkflow.writeToURL_error_, 1)
        self.assertResultIsBOOL(Automator.AMWorkflow.setValue_forVariableWithName_)
