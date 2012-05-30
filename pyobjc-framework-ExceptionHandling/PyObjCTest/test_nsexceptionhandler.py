
from PyObjCTools.TestSupport import *
from ExceptionHandling import *

try:
    unicode
except NameError:
    unicode = str

class TestNSExceptionHandlerHelper (NSObject):
    def exceptionHandler_shouldLogException_mask_(self, h, e, m):
        return False

    def exceptionHandler_shouldHandleException_mask_(self, h, e, m):
        return False


class TestNSExceptionHandler (TestCase):
    def testProtocols(self):
        self.assertIsInstance(protocols.NSExceptionHandlerDelegate, objc.informal_protocol)

        self.assertResultIsBOOL(TestNSExceptionHandlerHelper.exceptionHandler_shouldLogException_mask_)
        self.assertArgHasType(TestNSExceptionHandlerHelper.exceptionHandler_shouldLogException_mask_, 2, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSExceptionHandlerHelper.exceptionHandler_shouldHandleException_mask_)
        self.assertArgHasType(TestNSExceptionHandlerHelper.exceptionHandler_shouldHandleException_mask_, 2, objc._C_NSUInteger)

    def testConstants(self):
        self.assertIsInstance(NSUncaughtSystemExceptionException, unicode)
        self.assertIsInstance(NSUncaughtRuntimeErrorException, unicode)
        self.assertIsInstance(NSStackTraceKey, unicode)

        self.assertEqual(NSLogUncaughtExceptionMask, 1 << 0)
        self.assertEqual(NSHandleUncaughtExceptionMask, 1 << 1)
        self.assertEqual(NSLogUncaughtSystemExceptionMask, 1 << 2)
        self.assertEqual(NSHandleUncaughtSystemExceptionMask, 1 << 3)
        self.assertEqual(NSLogUncaughtRuntimeErrorMask, 1 << 4)
        self.assertEqual(NSHandleUncaughtRuntimeErrorMask, 1 << 5)
        self.assertEqual(NSLogTopLevelExceptionMask, 1 << 6)
        self.assertEqual(NSHandleTopLevelExceptionMask, 1 << 7)
        self.assertEqual(NSLogOtherExceptionMask, 1 << 8)
        self.assertEqual(NSHandleOtherExceptionMask, 1 << 9)

        self.assertEqual(NSLogAndHandleEveryExceptionMask,
                (NSLogUncaughtExceptionMask|NSLogUncaughtSystemExceptionMask|NSLogUncaughtRuntimeErrorMask|NSHandleUncaughtExceptionMask|NSHandleUncaughtSystemExceptionMask|NSHandleUncaughtRuntimeErrorMask|NSLogTopLevelExceptionMask|NSHandleTopLevelExceptionMask|NSLogOtherExceptionMask|NSHandleOtherExceptionMask))

        self.assertEqual(NSHangOnUncaughtExceptionMask, 1 << 0)
        self.assertEqual(NSHangOnUncaughtSystemExceptionMask, 1 << 1)
        self.assertEqual(NSHangOnUncaughtRuntimeErrorMask, 1 << 2)
        self.assertEqual(NSHangOnTopLevelExceptionMask, 1 << 3)
        self.assertEqual(NSHangOnOtherExceptionMask, 1 << 4)

        self.assertEqual(NSHangOnEveryExceptionMask, (NSHangOnUncaughtExceptionMask|NSHangOnUncaughtSystemExceptionMask|NSHangOnUncaughtRuntimeErrorMask|NSHangOnTopLevelExceptionMask|NSHangOnOtherExceptionMask))



    def testFunctions(self):
        NSExceptionHandlerResume

if __name__ == "__main__":
    main()
