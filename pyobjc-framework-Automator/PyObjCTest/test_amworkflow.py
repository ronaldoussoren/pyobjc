
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkflow (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsOut(AMWorkflow.runWorkflowAtURL_withInput_error_, 2)
        self.assertArgIsOut(AMWorkflow.initWithContentsOfURL_error_, 1)
        self.assertResultIsBOOL(AMWorkflow.writeToURL_error_)
        self.assertArgIsOut(AMWorkflow.writeToURL_error_, 1)
        self.assertResultIsBOOL(AMWorkflow.setValue_forVariableWithName_)

if __name__ == "__main__":
    main()
