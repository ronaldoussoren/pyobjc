import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTask(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSTaskTerminationReason)
        self.assertEqual(Foundation.NSTaskTerminationReasonExit, 1)
        self.assertEqual(Foundation.NSTaskTerminationReasonUncaughtSignal, 2)

    def test_constants(self):
        self.assertIsInstance(Foundation.NSTaskDidTerminateNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSTask.suspend)
        self.assertResultIsBOOL(Foundation.NSTask.resume)
        self.assertResultIsBOOL(Foundation.NSTask.isRunning)

        self.assertArgIsBlock(Foundation.NSTask.setTerminationHandler_, 0, b"v@")
        self.assertResultIsBlock(Foundation.NSTask.terminationHandler, b"v@")

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsOut(
            Foundation.NSTask.launchedTaskWithExecutableURL_arguments_error_terminationHandler_,
            2,
        )
        self.assertArgIsBlock(
            Foundation.NSTask.launchedTaskWithExecutableURL_arguments_error_terminationHandler_,
            3,
            b"v@",
        )
