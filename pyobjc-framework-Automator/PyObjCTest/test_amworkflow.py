
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkflow (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessArgIsOut(AMWorkflow.runWorkflowAtURL_withInput_error_, 2)
        self.failUnlessArgIsOut(AMWorkflow.initWithContentsOfURL_error_, 1)
        self.failUnlessResultIsBOOL(AMWorkflow.writeToURL_error_)
        self.failUnlessArgIsOut(AMWorkflow.writeToURL_error_, 1)
        self.failUnlessResultIsBOOL(AMWorkflow.setValue_forVariableWithName_)

if __name__ == "__main__":
    main()
