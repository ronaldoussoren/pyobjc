from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSErrorHelper (NSObject):
    def attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_(self, a, b, c, d, e): pass
    def attemptRecoveryFromError_optionIndex_(self, a, b): return 1


class TestNSError (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSCocoaErrorDomain, unicode)
        self.failUnlessIsInstance(NSPOSIXErrorDomain, unicode)
        self.failUnlessIsInstance(NSOSStatusErrorDomain, unicode)
        self.failUnlessIsInstance(NSMachErrorDomain, unicode)
        self.failUnlessIsInstance(NSUnderlyingErrorKey, unicode)
        self.failUnlessIsInstance(NSLocalizedDescriptionKey, unicode)
        self.failUnlessIsInstance(NSLocalizedFailureReasonErrorKey, unicode)
        self.failUnlessIsInstance(NSLocalizedRecoverySuggestionErrorKey, unicode)
        self.failUnlessIsInstance(NSLocalizedRecoveryOptionsErrorKey, unicode)
        self.failUnlessIsInstance(NSRecoveryAttempterErrorKey, unicode)
        self.failUnlessIsInstance(NSStringEncodingErrorKey, unicode)
        self.failUnlessIsInstance(NSURLErrorKey, unicode)
        self.failUnlessIsInstance(NSFilePathErrorKey, unicode)
        self.failUnlessIsInstance(NSHelpAnchorErrorKey, unicode)

    def testAttemptRecovery(self):
        self.failUnlessArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 1, objc._C_NSUInteger)
        self.failUnlessArgIsSEL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 3, 'v@:' + objc._C_NSBOOL + '^v')
        self.failUnlessArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 4, '^v')

        self.failUnlessResultIsBOOL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_)
        self.failUnlessArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_, 1, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
