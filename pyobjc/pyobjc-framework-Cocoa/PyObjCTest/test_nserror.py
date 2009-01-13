from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSError (TestCase):
    def testConstants(self):
        self.failUnless( isinstance(NSCocoaErrorDomain, unicode) )
        self.failUnless( isinstance(NSPOSIXErrorDomain, unicode) )
        self.failUnless( isinstance(NSOSStatusErrorDomain, unicode) )
        self.failUnless( isinstance(NSMachErrorDomain, unicode) )
        self.failUnless( isinstance(NSUnderlyingErrorKey, unicode) )
        self.failUnless( isinstance(NSLocalizedDescriptionKey, unicode) )
        self.failUnless( isinstance(NSLocalizedFailureReasonErrorKey, unicode) )
        self.failUnless( isinstance(NSLocalizedRecoverySuggestionErrorKey, unicode) )
        self.failUnless( isinstance(NSLocalizedRecoveryOptionsErrorKey, unicode) )
        self.failUnless( isinstance(NSRecoveryAttempterErrorKey, unicode) )
        self.failUnless( isinstance(NSStringEncodingErrorKey, unicode) )
        self.failUnless( isinstance(NSURLErrorKey, unicode) )
        self.failUnless( isinstance(NSFilePathErrorKey, unicode) )

    def testAttemptRecovery(self):
        class TestNSErrorHelper1 (NSObject):
            def attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_(
                    self, error, recoveryOptionIndex, delegate, didRecoverSelector,
                    contextInfo):
                pass

            def attemptRecoveryFromError_optionIndex_(self, error, index):
                pass

        obj = TestNSErrorHelper1.alloc().init()
        m = obj.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_.__metadata__()
        self.assertEquals(m['retval']['type'], objc._C_VOID)
        self.assertEquals(m['arguments'][0]['type'], objc._C_ID)
        self.assertEquals(m['arguments'][1]['type'], objc._C_SEL)
        self.assertEquals(m['arguments'][2]['type'], objc._C_ID)
        self.failUnless(m['arguments'][3]['type'] in (objc._C_UINT, objc._C_ULNG, objc._C_ULNG_LNG))
        self.assertEquals(m['arguments'][4]['type'], objc._C_ID)
        self.assertEquals(m['arguments'][5]['type'], objc._C_SEL)
        self.assertEquals(m['arguments'][6]['type'], objc._C_PTR + objc._C_VOID)

        m = obj.attemptRecoveryFromError_optionIndex_.__metadata__()
        self.assertEquals(m['retval']['type'], objc._C_NSBOOL)
        self.assertEquals(m['arguments'][0]['type'], objc._C_ID)
        self.assertEquals(m['arguments'][1]['type'], objc._C_SEL)
        self.assertEquals(m['arguments'][2]['type'], objc._C_ID)
        self.failUnless(m['arguments'][3]['type'] in (objc._C_UINT, objc._C_ULNG, objc._C_ULNG_LNG))

if __name__ == "__main__":
    main()
