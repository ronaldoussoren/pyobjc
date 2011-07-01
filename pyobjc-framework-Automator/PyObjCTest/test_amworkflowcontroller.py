
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkflowController (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(AMWorkflowController.canRun)
        self.assertResultIsBOOL(AMWorkflowController.isRunning)
        self.assertResultIsBOOL(AMWorkflowController.isPaused)

if __name__ == "__main__":
    main()
