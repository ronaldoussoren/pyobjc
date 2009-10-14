'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
from SystemConfiguration import *

class TestSystemConfiguration (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kSCStatusOK,  0)
        self.failUnlessEqual(kSCStatusFailed,  1001)
        self.failUnlessEqual(kSCStatusInvalidArgument,  1002)
        self.failUnlessEqual(kSCStatusAccessError,  1003)
        self.failUnlessEqual(kSCStatusNoKey,  1004)
        self.failUnlessEqual(kSCStatusKeyExists,  1005)
        self.failUnlessEqual(kSCStatusLocked,  1006)
        self.failUnlessEqual(kSCStatusNeedLock,  1007)
        self.failUnlessEqual(kSCStatusNoStoreSession,  2001)
        self.failUnlessEqual(kSCStatusNoStoreServer,  2002)
        self.failUnlessEqual(kSCStatusNotifierActive, 2003)
        self.failUnlessEqual(kSCStatusNoPrefsSession, 3001)
        self.failUnlessEqual(kSCStatusPrefsBusy, 3002)
        self.failUnlessEqual(kSCStatusNoConfigFile, 3003)
        self.failUnlessEqual(kSCStatusNoLink, 3004)
        self.failUnlessEqual(kSCStatusStale, 3005)
        self.failUnlessEqual(kSCStatusMaxLink, 3006)
        self.failUnlessEqual(kSCStatusReachabilityUnknown, 4001)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kCFErrorDomainSystemConfiguration, unicode)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        err = SCCopyLastError()
        self.failUnless(isinstance(err, CFErrorRef))


    def testFunctions(self):

        err = SCError()
        self.failUnlessIsInstance(err, (int, long))

        err = SCErrorString(kSCStatusNoLink);
        self.failUnlessIsInstance(err, str)



if __name__ == "__main__":
    main()
