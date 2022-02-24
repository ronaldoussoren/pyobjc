import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTask(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSTaskTerminationReason)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSTask.suspend)
        self.assertResultIsBOOL(Foundation.NSTask.resume)
        self.assertResultIsBOOL(Foundation.NSTask.isRunning)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(Foundation.NSTask.setTerminationHandler_, 0, b"v@")
        self.assertResultIsBlock(Foundation.NSTask.terminationHandler, b"v@")

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(
            Foundation.NSTask.launchedTaskWithExecutableURL_arguments_error_terminationHandler_,
            2,
        )
        self.assertArgIsBlock(
            Foundation.NSTask.launchedTaskWithExecutableURL_arguments_error_terminationHandler_,
            3,
            b"v@",
        )

    def testConstants(self):
        self.assertIsInstance(Foundation.NSTaskDidTerminateNotification, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSTaskTerminationReasonExit, 1)
        self.assertEqual(Foundation.NSTaskTerminationReasonUncaughtSignal, 2)
