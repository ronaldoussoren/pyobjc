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
            NSException.raise_format_('ExceptionName', 'Format: %s %d', 'hello', 42)

        except TypeError:
            raise

        except objc.error, e:
            self.assertEquals(e._pyobjc_info_['name'], 'ExceptionName')
            self.assertEquals(e._pyobjc_info_['reason'], 'Format: hello 42')


class TestNSException (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSGenericException, unicode)
        self.failUnlessIsInstance(NSRangeException, unicode)
        self.failUnlessIsInstance(NSInvalidArgumentException, unicode)
        self.failUnlessIsInstance(NSInternalInconsistencyException, unicode)
        self.failUnlessIsInstance(NSMallocException, unicode)
        self.failUnlessIsInstance(NSObjectInaccessibleException, unicode)
        self.failUnlessIsInstance(NSObjectNotAvailableException, unicode)
        self.failUnlessIsInstance(NSDestinationInvalidException, unicode)
        self.failUnlessIsInstance(NSPortTimeoutException, unicode)
        self.failUnlessIsInstance(NSInvalidSendPortException, unicode)
        self.failUnlessIsInstance(NSInvalidReceivePortException, unicode)
        self.failUnlessIsInstance(NSPortSendException, unicode)
        self.failUnlessIsInstance(NSPortReceiveException, unicode)
        self.failUnlessIsInstance(NSOldStyleException, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(NSAssertionHandlerKey, unicode)

    @expectedFailure
    def testUncaughtExceptionHandler(self):
        self.fail("NSSetUncaughtExceptionHandler")

    def testNoAssert(self):
        self.failIf(hasattr(Foundation, 'NSAssert5'))
        self.failIf(hasattr(Foundation, 'NSAssert4'))
        self.failIf(hasattr(Foundation, 'NSAssert3'))
        self.failIf(hasattr(Foundation, 'NSAssert2'))
        self.failIf(hasattr(Foundation, 'NSAssert1'))
        self.failIf(hasattr(Foundation, 'NSAssert'))
        self.failIf(hasattr(Foundation, 'NSParameterAssert'))
        self.failIf(hasattr(Foundation, 'NSCAssert5'))
        self.failIf(hasattr(Foundation, 'NSCAssert4'))
        self.failIf(hasattr(Foundation, 'NSCAssert3'))
        self.failIf(hasattr(Foundation, 'NSCAssert2'))
        self.failIf(hasattr(Foundation, 'NSCAssert1'))
        self.failIf(hasattr(Foundation, 'NSCAssert'))
        self.failIf(hasattr(Foundation, 'NSCParameterAssert'))
    
    def testMethods(self):
        self.failUnlessArgIsPrintf(NSException.raise_format_, 1)

        self.failUnlessArgIsPrintf(NSAssertionHandler.handleFailureInMethod_object_file_lineNumber_description_, 4)
        self.failUnlessArgIsPrintf(NSAssertionHandler.handleFailureInFunction_file_lineNumber_description_, 3)


if __name__ == '__main__':
    main()
