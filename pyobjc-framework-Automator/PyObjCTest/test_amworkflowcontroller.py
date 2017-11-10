
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMWorkflowController (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(AMWorkflowController.canRun)
        self.assertResultIsBOOL(AMWorkflowController.isRunning)
        self.assertResultIsBOOL(AMWorkflowController.isPaused)

    #@min_sdk_level('10.13')
    @min_os_level('10.13')
    def testProtocols(self):
        objc.protocolNamed('AMWorkflowControllerDelegate')

if __name__ == "__main__":
    main()
