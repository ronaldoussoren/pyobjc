
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGError (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGErrorSuccess, 0)
        self.failUnlessEqual(kCGErrorFirst, 1000)
        self.failUnlessEqual(kCGErrorFailure, kCGErrorFirst)
        self.failUnlessEqual(kCGErrorIllegalArgument, 1001)
        self.failUnlessEqual(kCGErrorInvalidConnection, 1002)
        self.failUnlessEqual(kCGErrorInvalidContext, 1003)
        self.failUnlessEqual(kCGErrorCannotComplete, 1004)
        self.failUnlessEqual(kCGErrorNameTooLong, 1005)
        self.failUnlessEqual(kCGErrorNotImplemented, 1006)
        self.failUnlessEqual(kCGErrorRangeCheck, 1007)
        self.failUnlessEqual(kCGErrorTypeCheck, 1008)
        self.failUnlessEqual(kCGErrorNoCurrentPoint, 1009)
        self.failUnlessEqual(kCGErrorInvalidOperation, 1010)
        self.failUnlessEqual(kCGErrorNoneAvailable, 1011)
        self.failUnlessEqual(kCGErrorApplicationRequiresNewerSystem, 1015)
        self.failUnlessEqual(kCGErrorApplicationNotPermittedToExecute, 1016)
        self.failUnlessEqual(kCGErrorApplicationIncorrectExecutableFormatFound, 1023)
        self.failUnlessEqual(kCGErrorApplicationIsLaunching, 1024)
        self.failUnlessEqual(kCGErrorApplicationAlreadyRunning, 1025)
        self.failUnlessEqual(kCGErrorApplicationCanOnlyBeRunInOneSessionAtATime, 1026)
        self.failUnlessEqual(kCGErrorClassicApplicationsMustBeLaunchedByClassic, 1027)
        self.failUnlessEqual(kCGErrorForkFailed, 1028)
        self.failUnlessEqual(kCGErrorRetryRegistration, 1029)
        self.failUnlessEqual(kCGErrorLast, kCGErrorRetryRegistration)

if __name__ == "__main__":
    main()
