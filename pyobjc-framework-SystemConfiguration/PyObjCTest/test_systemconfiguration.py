'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
from SystemConfiguration import *

class TestSystemConfiguration (TestCase):
    def testConstants(self):
        self.assertEqual(kSCStatusOK,  0)
        self.assertEqual(kSCStatusFailed,  1001)
        self.assertEqual(kSCStatusInvalidArgument,  1002)
        self.assertEqual(kSCStatusAccessError,  1003)
        self.assertEqual(kSCStatusNoKey,  1004)
        self.assertEqual(kSCStatusKeyExists,  1005)
        self.assertEqual(kSCStatusLocked,  1006)
        self.assertEqual(kSCStatusNeedLock,  1007)
        self.assertEqual(kSCStatusNoStoreSession,  2001)
        self.assertEqual(kSCStatusNoStoreServer,  2002)
        self.assertEqual(kSCStatusNotifierActive, 2003)
        self.assertEqual(kSCStatusNoPrefsSession, 3001)
        self.assertEqual(kSCStatusPrefsBusy, 3002)
        self.assertEqual(kSCStatusNoConfigFile, 3003)
        self.assertEqual(kSCStatusNoLink, 3004)
        self.assertEqual(kSCStatusStale, 3005)
        self.assertEqual(kSCStatusMaxLink, 3006)
        self.assertEqual(kSCStatusReachabilityUnknown, 4001)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCFErrorDomainSystemConfiguration, unicode)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        err = SCCopyLastError()
        self.assertTrue(isinstance(err, CFErrorRef))


    def testFunctions(self):

        err = SCError()
        self.assertIsInstance(err, (int, long))

        err = SCErrorString(kSCStatusNoLink);
        self.assertIsInstance(err, bytes)



if __name__ == "__main__":
    main()
