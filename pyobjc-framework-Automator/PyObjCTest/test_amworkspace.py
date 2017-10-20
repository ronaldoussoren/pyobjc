from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkspace (TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(AMWorkspace.runWorkflowAtPath_withInput_error_, 2)

if __name__ == "__main__":
    main()
