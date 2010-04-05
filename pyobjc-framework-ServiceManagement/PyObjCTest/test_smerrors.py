
from PyObjCTools.TestSupport import *
from ServiceManagement import *

class TestSMErrors (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertIsInstance(kSMErrorDomainIPC, unicode)
        self.assertIsInstance(kSMErrorDomainFramework, unicode)
        self.assertIsInstance(kSMErrorDomainLaunchd, unicode)

        self.assertEqual(kSMErrorInternalFailure, 2)
        self.assertEqual(kSMErrorInvalidSignature, 3)
        self.assertEqual(kSMErrorAuthorizationFailure, 4)
        self.assertEqual(kSMErrorToolNotValid, 5)
        self.assertEqual(kSMErrorJobNotFound, 6)
        self.assertEqual(kSMErrorServiceUnavailable, 7)
        self.assertEqual(kSMErrorJobPlistNotFound, 8)
        self.assertEqual(kSMErrorJobMustBeEnabled, 9)

if __name__ == "__main__":
    main()
