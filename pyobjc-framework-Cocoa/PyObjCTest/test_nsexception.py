from PyObjCTools.TestSupport import *
import objc

from Foundation import *
import Foundation

class TestNSExceptionInteraction(TestCase):
    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            a = NSException.alloc().initWithName_reason_userInfo_( u"Bogus", u"A bad reason", { u"foo" : u"bar" } )

    def testFormat(self):
        try:
            NSException.raise_format_('ExceptionName', 'Format: %s %d', b'hello', 42)

        except TypeError:
            raise

        except objc.error, e:
            self.assertEqual(e._pyobjc_info_['name'], 'ExceptionName')
            self.assertEqual(e._pyobjc_info_['reason'], 'Format: hello 42')


class TestNSException (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSGenericException, unicode)
        self.assertIsInstance(NSRangeException, unicode)
        self.assertIsInstance(NSInvalidArgumentException, unicode)
        self.assertIsInstance(NSInternalInconsistencyException, unicode)
        self.assertIsInstance(NSMallocException, unicode)
        self.assertIsInstance(NSObjectInaccessibleException, unicode)
        self.assertIsInstance(NSObjectNotAvailableException, unicode)
        self.assertIsInstance(NSDestinationInvalidException, unicode)
        self.assertIsInstance(NSPortTimeoutException, unicode)
        self.assertIsInstance(NSInvalidSendPortException, unicode)
        self.assertIsInstance(NSInvalidReceivePortException, unicode)
        self.assertIsInstance(NSPortSendException, unicode)
        self.assertIsInstance(NSPortReceiveException, unicode)
        self.assertIsInstance(NSOldStyleException, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSAssertionHandlerKey, unicode)

    @expectedFailure
    def testUncaughtExceptionHandler(self):
        self.fail("NSSetUncaughtExceptionHandler")

    def testNoAssert(self):
        self.assertNotHasAttr(Foundation, 'NSAssert5')
        self.assertNotHasAttr(Foundation, 'NSAssert4')
        self.assertNotHasAttr(Foundation, 'NSAssert3')
        self.assertNotHasAttr(Foundation, 'NSAssert2')
        self.assertNotHasAttr(Foundation, 'NSAssert1')
        self.assertNotHasAttr(Foundation, 'NSAssert')
        self.assertNotHasAttr(Foundation, 'NSParameterAssert')
        self.assertNotHasAttr(Foundation, 'NSCAssert5')
        self.assertNotHasAttr(Foundation, 'NSCAssert4')
        self.assertNotHasAttr(Foundation, 'NSCAssert3')
        self.assertNotHasAttr(Foundation, 'NSCAssert2')
        self.assertNotHasAttr(Foundation, 'NSCAssert1')
        self.assertNotHasAttr(Foundation, 'NSCAssert')
        self.assertNotHasAttr(Foundation, 'NSCParameterAssert')
    def testMethods(self):
        self.assertArgIsPrintf(NSException.raise_format_, 1)

        self.assertArgIsPrintf(NSAssertionHandler.handleFailureInMethod_object_file_lineNumber_description_, 4)
        self.assertArgIsPrintf(NSAssertionHandler.handleFailureInFunction_file_lineNumber_description_, 3)


if __name__ == '__main__':
    main()
