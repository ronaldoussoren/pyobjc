import ExceptionHandling
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSExceptionHandlerHelper(ExceptionHandling.NSObject):
    def exceptionHandler_shouldLogException_mask_(self, h, e, m):
        return False

    def exceptionHandler_shouldHandleException_mask_(self, h, e, m):
        return False


class TestNSExceptionHandler(TestCase):
    def testProtocols(self):
        # self.assertIsInstance(protocols.NSExceptionHandlerDelegate, objc.informal_protocol)

        self.assertResultIsBOOL(
            TestNSExceptionHandlerHelper.exceptionHandler_shouldLogException_mask_
        )
        self.assertArgHasType(
            TestNSExceptionHandlerHelper.exceptionHandler_shouldLogException_mask_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSExceptionHandlerHelper.exceptionHandler_shouldHandleException_mask_
        )
        self.assertArgHasType(
            TestNSExceptionHandlerHelper.exceptionHandler_shouldHandleException_mask_,
            2,
            objc._C_NSUInteger,
        )

    def testConstants(self):
        self.assertIsInstance(ExceptionHandling.NSUncaughtSystemExceptionException, str)
        self.assertIsInstance(ExceptionHandling.NSUncaughtRuntimeErrorException, str)
        self.assertIsInstance(ExceptionHandling.NSStackTraceKey, str)

        self.assertEqual(ExceptionHandling.NSLogUncaughtExceptionMask, 1 << 0)
        self.assertEqual(ExceptionHandling.NSHandleUncaughtExceptionMask, 1 << 1)
        self.assertEqual(ExceptionHandling.NSLogUncaughtSystemExceptionMask, 1 << 2)
        self.assertEqual(ExceptionHandling.NSHandleUncaughtSystemExceptionMask, 1 << 3)
        self.assertEqual(ExceptionHandling.NSLogUncaughtRuntimeErrorMask, 1 << 4)
        self.assertEqual(ExceptionHandling.NSHandleUncaughtRuntimeErrorMask, 1 << 5)
        self.assertEqual(ExceptionHandling.NSLogTopLevelExceptionMask, 1 << 6)
        self.assertEqual(ExceptionHandling.NSHandleTopLevelExceptionMask, 1 << 7)
        self.assertEqual(ExceptionHandling.NSLogOtherExceptionMask, 1 << 8)
        self.assertEqual(ExceptionHandling.NSHandleOtherExceptionMask, 1 << 9)

        self.assertEqual(
            ExceptionHandling.NSLogAndHandleEveryExceptionMask,
            (
                ExceptionHandling.NSLogUncaughtExceptionMask
                | ExceptionHandling.NSLogUncaughtSystemExceptionMask
                | ExceptionHandling.NSLogUncaughtRuntimeErrorMask
                | ExceptionHandling.NSHandleUncaughtExceptionMask
                | ExceptionHandling.NSHandleUncaughtSystemExceptionMask
                | ExceptionHandling.NSHandleUncaughtRuntimeErrorMask
                | ExceptionHandling.NSLogTopLevelExceptionMask
                | ExceptionHandling.NSHandleTopLevelExceptionMask
                | ExceptionHandling.NSLogOtherExceptionMask
                | ExceptionHandling.NSHandleOtherExceptionMask
            ),
        )

        self.assertEqual(ExceptionHandling.NSHangOnUncaughtExceptionMask, 1 << 0)
        self.assertEqual(ExceptionHandling.NSHangOnUncaughtSystemExceptionMask, 1 << 1)
        self.assertEqual(ExceptionHandling.NSHangOnUncaughtRuntimeErrorMask, 1 << 2)
        self.assertEqual(ExceptionHandling.NSHangOnTopLevelExceptionMask, 1 << 3)
        self.assertEqual(ExceptionHandling.NSHangOnOtherExceptionMask, 1 << 4)

        self.assertEqual(
            ExceptionHandling.NSHangOnEveryExceptionMask,
            (
                ExceptionHandling.NSHangOnUncaughtExceptionMask
                | ExceptionHandling.NSHangOnUncaughtSystemExceptionMask
                | ExceptionHandling.NSHangOnUncaughtRuntimeErrorMask
                | ExceptionHandling.NSHangOnTopLevelExceptionMask
                | ExceptionHandling.NSHangOnOtherExceptionMask
            ),
        )

    def testFunctions(self):
        ExceptionHandling.NSExceptionHandlerResume
