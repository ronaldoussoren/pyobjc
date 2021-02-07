from PyObjCTools.TestSupport import TestCase
import SystemConfiguration


class TestSCPreferencesSetSpecific(TestCase):
    def testFunctions(self):
        ref = SystemConfiguration.SCPreferencesCreate(
            None, "pyobjc.test", "pyobjc.test"
        )
        self.assertIsInstance(ref, SystemConfiguration.SCPreferencesRef)

        v = SystemConfiguration.SCPreferencesSetComputerName(
            ref, "my host", SystemConfiguration.kCFStringEncodingUTF8
        )
        self.assertTrue(isinstance(v, bool))

        v = SystemConfiguration.SCPreferencesSetLocalHostName(ref, "my.host.private")
        self.assertTrue(isinstance(v, bool))

        # NOTE: Do not commit changes, that would mess with the computer running
        # the tests
