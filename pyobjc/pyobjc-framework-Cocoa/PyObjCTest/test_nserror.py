from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSErrorHelper (NSObject):
    def attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_(self, a, b, c, d, e): pass
    def attemptRecoveryFromError_optionIndex_(self, a, b): return 1


class TestNSError (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSCocoaErrorDomain, unicode)
        self.assertIsInstance(NSPOSIXErrorDomain, unicode)
        self.assertIsInstance(NSOSStatusErrorDomain, unicode)
        self.assertIsInstance(NSMachErrorDomain, unicode)
        self.assertIsInstance(NSUnderlyingErrorKey, unicode)
        self.assertIsInstance(NSLocalizedDescriptionKey, unicode)
        self.assertIsInstance(NSLocalizedFailureReasonErrorKey, unicode)
        self.assertIsInstance(NSLocalizedRecoverySuggestionErrorKey, unicode)
        self.assertIsInstance(NSLocalizedRecoveryOptionsErrorKey, unicode)
        self.assertIsInstance(NSRecoveryAttempterErrorKey, unicode)
        self.assertIsInstance(NSStringEncodingErrorKey, unicode)
        self.assertIsInstance(NSURLErrorKey, unicode)
        self.assertIsInstance(NSFilePathErrorKey, unicode)
        self.assertIsInstance(NSHelpAnchorErrorKey, unicode)

    def testAttemptRecovery(self):
        self.assertArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 1, objc._C_NSUInteger)
        self.assertArgIsSEL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 3, b'v@:' + objc._C_NSBOOL + b'^v')
        self.assertArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 4, b'^v')

        self.assertResultIsBOOL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_)
        self.assertArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_, 1, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
