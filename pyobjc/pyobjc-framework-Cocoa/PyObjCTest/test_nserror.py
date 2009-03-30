from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSErrorHelper (NSObject):
    def attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_(self, a, b, c, d, e): pass
    def attemptRecoveryFromError_optionIndex_(self, a, b): return 1


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
        self.failUnlessArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 1, objc._C_NSUInteger)
        self.failUnlessArgIsSEL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 3, 'v@:' + objc._C_NSBOOL + '^v')
        self.failUnlessArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 4, '^v')

        self.failUnlessResultIsBOOL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_)
        self.failUnlessArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_, 1, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
