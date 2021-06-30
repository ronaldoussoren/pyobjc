from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGError(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGErrorSuccess, 0)
        self.assertEqual(Quartz.kCGErrorFirst, 1000)
        self.assertEqual(Quartz.kCGErrorFailure, Quartz.kCGErrorFirst)
        self.assertEqual(Quartz.kCGErrorIllegalArgument, 1001)
        self.assertEqual(Quartz.kCGErrorInvalidConnection, 1002)
        self.assertEqual(Quartz.kCGErrorInvalidContext, 1003)
        self.assertEqual(Quartz.kCGErrorCannotComplete, 1004)
        self.assertEqual(Quartz.kCGErrorNameTooLong, 1005)
        self.assertEqual(Quartz.kCGErrorNotImplemented, 1006)
        self.assertEqual(Quartz.kCGErrorRangeCheck, 1007)
        self.assertEqual(Quartz.kCGErrorTypeCheck, 1008)
        self.assertEqual(Quartz.kCGErrorNoCurrentPoint, 1009)
        self.assertEqual(Quartz.kCGErrorInvalidOperation, 1010)
        self.assertEqual(Quartz.kCGErrorNoneAvailable, 1011)
        self.assertEqual(Quartz.kCGErrorApplicationRequiresNewerSystem, 1015)
        self.assertEqual(Quartz.kCGErrorApplicationNotPermittedToExecute, 1016)
        self.assertEqual(Quartz.kCGErrorApplicationIncorrectExecutableFormatFound, 1023)
        self.assertEqual(Quartz.kCGErrorApplicationIsLaunching, 1024)
        self.assertEqual(Quartz.kCGErrorApplicationAlreadyRunning, 1025)
        self.assertEqual(
            Quartz.kCGErrorApplicationCanOnlyBeRunInOneSessionAtATime, 1026
        )
        self.assertEqual(
            Quartz.kCGErrorClassicApplicationsMustBeLaunchedByClassic, 1027
        )
        self.assertEqual(Quartz.kCGErrorForkFailed, 1028)
        self.assertEqual(Quartz.kCGErrorRetryRegistration, 1029)
        self.assertEqual(Quartz.kCGErrorLast, Quartz.kCGErrorRetryRegistration)

    @min_os_level("12.0")
    def testFunctions(self):
        self.assertArgIsFunction(Quartz.CGErrorSetCallback, 0, b"v", True)
