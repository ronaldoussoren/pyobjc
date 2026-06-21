import Automator
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAMWorkflowController(TestCase):
    @min_os_level("10.5")
    def test_methods(self):
        self.assertResultIsBOOL(Automator.AMWorkflowController.canRun)
        self.assertResultIsBOOL(Automator.AMWorkflowController.isRunning)
        self.assertResultIsBOOL(Automator.AMWorkflowController.isPaused)

    @min_sdk_level("10.13")
    def test_protocols(self):
        self.assertProtocolExists("AMWorkflowControllerDelegate", Automator)
