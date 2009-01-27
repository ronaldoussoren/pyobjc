
from PyObjCTools.TestSupport import *
from ExceptionHandling import *

class TestNSExceptionHandlerHelper (NSObject):
    def exceptionHandler_shouldLogException_mask_(self, h, e, m):
        return False

    def exceptionHandler_shouldHandleException_mask_(self, h, e, m):
        return False


class TestNSExceptionHandler (TestCase):
    def testProtocols(self):
        self.failUnlessIsInstance(protocols.NSExceptionHandlerDelegate, objc.informal_protocol)

        self.failUnlessResultIsBOOL(TestNSExceptionHandlerHelper.exceptionHandler_shouldLogException_mask_)
        self.failUnlessArgHasType(TestNSExceptionHandlerHelper.exceptionHandler_shouldLogException_mask_, 2, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSExceptionHandlerHelper.exceptionHandler_shouldHandleException_mask_)
        self.failUnlessArgHasType(TestNSExceptionHandlerHelper.exceptionHandler_shouldHandleException_mask_, 2, objc._C_NSUInteger)

    def testConstants(self):
        self.failUnlessIsInstance(NSUncaughtSystemExceptionException, unicode)
        self.failUnlessIsInstance(NSUncaughtRuntimeErrorException, unicode)
        self.failUnlessIsInstance(NSStackTraceKey, unicode)

        self.failUnlessEqual(NSLogUncaughtExceptionMask, 1 << 0)
        self.failUnlessEqual(NSHandleUncaughtExceptionMask, 1 << 1)
        self.failUnlessEqual(NSLogUncaughtSystemExceptionMask, 1 << 2)
        self.failUnlessEqual(NSHandleUncaughtSystemExceptionMask, 1 << 3)
        self.failUnlessEqual(NSLogUncaughtRuntimeErrorMask, 1 << 4)
        self.failUnlessEqual(NSHandleUncaughtRuntimeErrorMask, 1 << 5)
        self.failUnlessEqual(NSLogTopLevelExceptionMask, 1 << 6)
        self.failUnlessEqual(NSHandleTopLevelExceptionMask, 1 << 7)
        self.failUnlessEqual(NSLogOtherExceptionMask, 1 << 8)
        self.failUnlessEqual(NSHandleOtherExceptionMask, 1 << 9)

        self.failUnlessEqual(NSLogAndHandleEveryExceptionMask,
                (NSLogUncaughtExceptionMask|NSLogUncaughtSystemExceptionMask|NSLogUncaughtRuntimeErrorMask|NSHandleUncaughtExceptionMask|NSHandleUncaughtSystemExceptionMask|NSHandleUncaughtRuntimeErrorMask|NSLogTopLevelExceptionMask|NSHandleTopLevelExceptionMask|NSLogOtherExceptionMask|NSHandleOtherExceptionMask))

        self.failUnlessEqual(NSHangOnUncaughtExceptionMask, 1 << 0)
        self.failUnlessEqual(NSHangOnUncaughtSystemExceptionMask, 1 << 1)
        self.failUnlessEqual(NSHangOnUncaughtRuntimeErrorMask, 1 << 2)
        self.failUnlessEqual(NSHangOnTopLevelExceptionMask, 1 << 3)
        self.failUnlessEqual(NSHangOnOtherExceptionMask, 1 << 4)

        self.failUnlessEqual(NSHangOnEveryExceptionMask, (NSHangOnUncaughtExceptionMask|NSHangOnUncaughtSystemExceptionMask|NSHangOnUncaughtRuntimeErrorMask|NSHangOnTopLevelExceptionMask|NSHangOnOtherExceptionMask))



    def testFunctions(self):
        NSExceptionHandlerResume

if __name__ == "__main__":
    main()
