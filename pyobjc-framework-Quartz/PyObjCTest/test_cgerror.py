
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGError (TestCase):
    def testConstants(self):
        self.assertEqual(kCGErrorSuccess, 0)
        self.assertEqual(kCGErrorFirst, 1000)
        self.assertEqual(kCGErrorFailure, kCGErrorFirst)
        self.assertEqual(kCGErrorIllegalArgument, 1001)
        self.assertEqual(kCGErrorInvalidConnection, 1002)
        self.assertEqual(kCGErrorInvalidContext, 1003)
        self.assertEqual(kCGErrorCannotComplete, 1004)
        self.assertEqual(kCGErrorNameTooLong, 1005)
        self.assertEqual(kCGErrorNotImplemented, 1006)
        self.assertEqual(kCGErrorRangeCheck, 1007)
        self.assertEqual(kCGErrorTypeCheck, 1008)
        self.assertEqual(kCGErrorNoCurrentPoint, 1009)
        self.assertEqual(kCGErrorInvalidOperation, 1010)
        self.assertEqual(kCGErrorNoneAvailable, 1011)
        self.assertEqual(kCGErrorApplicationRequiresNewerSystem, 1015)
        self.assertEqual(kCGErrorApplicationNotPermittedToExecute, 1016)
        self.assertEqual(kCGErrorApplicationIncorrectExecutableFormatFound, 1023)
        self.assertEqual(kCGErrorApplicationIsLaunching, 1024)
        self.assertEqual(kCGErrorApplicationAlreadyRunning, 1025)
        self.assertEqual(kCGErrorApplicationCanOnlyBeRunInOneSessionAtATime, 1026)
        self.assertEqual(kCGErrorClassicApplicationsMustBeLaunchedByClassic, 1027)
        self.assertEqual(kCGErrorForkFailed, 1028)
        self.assertEqual(kCGErrorRetryRegistration, 1029)
        self.assertEqual(kCGErrorLast, kCGErrorRetryRegistration)

if __name__ == "__main__":
    main()
