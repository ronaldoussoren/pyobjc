from PyObjCTools.TestSupport import TestCase, min_os_level
import SystemConfiguration


class TestSystemConfiguration(TestCase):
    def testConstants(self):
        self.assertEqual(SystemConfiguration.kSCStatusOK, 0)
        self.assertEqual(SystemConfiguration.kSCStatusFailed, 1001)
        self.assertEqual(SystemConfiguration.kSCStatusInvalidArgument, 1002)
        self.assertEqual(SystemConfiguration.kSCStatusAccessError, 1003)

        self.assertEqual(SystemConfiguration.kSCStatusNoKey, 1004)
        self.assertEqual(SystemConfiguration.kSCStatusKeyExists, 1005)
        self.assertEqual(SystemConfiguration.kSCStatusLocked, 1006)
        self.assertEqual(SystemConfiguration.kSCStatusNeedLock, 1007)

        self.assertEqual(SystemConfiguration.kSCStatusNoStoreSession, 2001)
        self.assertEqual(SystemConfiguration.kSCStatusNoStoreServer, 2002)
        self.assertEqual(SystemConfiguration.kSCStatusNotifierActive, 2003)

        self.assertEqual(SystemConfiguration.kSCStatusNoPrefsSession, 3001)
        self.assertEqual(SystemConfiguration.kSCStatusPrefsBusy, 3002)
        self.assertEqual(SystemConfiguration.kSCStatusNoConfigFile, 3003)
        self.assertEqual(SystemConfiguration.kSCStatusNoLink, 3004)
        self.assertEqual(SystemConfiguration.kSCStatusStale, 3005)
        self.assertEqual(SystemConfiguration.kSCStatusMaxLink, 3006)

        self.assertEqual(SystemConfiguration.kSCStatusReachabilityUnknown, 4001)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(
            SystemConfiguration.kCFErrorDomainSystemConfiguration, str
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(SystemConfiguration.kSCStatusConnectionNoService, 5001)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(SystemConfiguration.kSCStatusConnectionIgnore, 5002)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        err = SystemConfiguration.SCCopyLastError()
        self.assertTrue(isinstance(err, SystemConfiguration.CFErrorRef))

    def testFunctions(self):
        err = SystemConfiguration.SCError()
        self.assertIsInstance(err, int)

        err = SystemConfiguration.SCErrorString(SystemConfiguration.kSCStatusNoLink)
        self.assertIsInstance(err, bytes)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SystemConfiguration)
