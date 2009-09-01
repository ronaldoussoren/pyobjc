
from PyObjCTools.TestSupport import *
from ServiceManagement import *

class TestSMErrors (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.failUnlessIsInstance(kSMErrorDomainIPC, unicode)
        self.failUnlessIsInstance(kSMErrorDomainFramework, unicode)
        self.failUnlessIsInstance(kSMErrorDomainLaunchd, unicode)

        self.failUnlessEqual(kSMErrorInternalFailure, 2)
        self.failUnlessEqual(kSMErrorInvalidSignature, 3)
        self.failUnlessEqual(kSMErrorAuthorizationFailure, 4)
        self.failUnlessEqual(kSMErrorToolNotValid, 5)
        self.failUnlessEqual(kSMErrorJobNotFound, 6)
        self.failUnlessEqual(kSMErrorServiceUnavailable, 7)
        self.failUnlessEqual(kSMErrorJobPlistNotFound, 8)
        self.failUnlessEqual(kSMErrorJobMustBeEnabled, 9)

if __name__ == "__main__":
    main()
