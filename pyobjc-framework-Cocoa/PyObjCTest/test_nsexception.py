import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSExceptionInteraction(TestCase):
    def testRepeatedAllocInit(self):
        for _ in range(1, 1000):
            _ = Foundation.NSException.alloc().initWithName_reason_userInfo_(
                "Bogus", "A bad reason", {"foo": "bar"}
            )

    def testFormat(self):
        try:
            Foundation.NSException.raise_format_(
                "ExceptionName", "Format: %s %d", b"hello", 42
            )

        except TypeError:
            raise

        except objc.error as e:
            self.assertEqual(e._pyobjc_info_["name"], "ExceptionName")
            self.assertEqual(e._pyobjc_info_["reason"], "Format: hello 42")


class TestNSException(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSGenericException, str)
        self.assertIsInstance(Foundation.NSRangeException, str)
        self.assertIsInstance(Foundation.NSInvalidArgumentException, str)
        self.assertIsInstance(Foundation.NSInternalInconsistencyException, str)
        self.assertIsInstance(Foundation.NSMallocException, str)
        self.assertIsInstance(Foundation.NSObjectInaccessibleException, str)
        self.assertIsInstance(Foundation.NSObjectNotAvailableException, str)
        self.assertIsInstance(Foundation.NSDestinationInvalidException, str)
        self.assertIsInstance(Foundation.NSPortTimeoutException, str)
        self.assertIsInstance(Foundation.NSInvalidSendPortException, str)
        self.assertIsInstance(Foundation.NSInvalidReceivePortException, str)
        self.assertIsInstance(Foundation.NSPortSendException, str)
        self.assertIsInstance(Foundation.NSPortReceiveException, str)
        self.assertIsInstance(Foundation.NSOldStyleException, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Foundation.NSAssertionHandlerKey, str)

    def testUncaughtExceptionHandler(self):
        self.assertArgIsFunction(
            Foundation.NSSetUncaughtExceptionHandler, 0, b"v@", True
        )
        self.assertResultIsFunction(Foundation.NSGetUncaughtExceptionHandler, b"v@")

    def testNoAssert(self):
        self.assertNotHasAttr(Foundation, "NSAssert5")
        self.assertNotHasAttr(Foundation, "NSAssert4")
        self.assertNotHasAttr(Foundation, "NSAssert3")
        self.assertNotHasAttr(Foundation, "NSAssert2")
        self.assertNotHasAttr(Foundation, "NSAssert1")
        self.assertNotHasAttr(Foundation, "NSAssert")
        self.assertNotHasAttr(Foundation, "NSParameterAssert")
        self.assertNotHasAttr(Foundation, "NSCAssert5")
        self.assertNotHasAttr(Foundation, "NSCAssert4")
        self.assertNotHasAttr(Foundation, "NSCAssert3")
        self.assertNotHasAttr(Foundation, "NSCAssert2")
        self.assertNotHasAttr(Foundation, "NSCAssert1")
        self.assertNotHasAttr(Foundation, "NSCAssert")
        self.assertNotHasAttr(Foundation, "NSCParameterAssert")

    def testMethods(self):
        self.assertArgIsPrintf(Foundation.NSException.raise_format_, 1)

        self.assertArgIsPrintf(
            Foundation.NSAssertionHandler.handleFailureInMethod_object_file_lineNumber_description_,  # noqa: B950
            4,
        )
        self.assertArgIsPrintf(
            Foundation.NSAssertionHandler.handleFailureInFunction_file_lineNumber_description_,
            3,
        )
