from PyObjCTools.TestSupport import TestCase
import SystemConfiguration


class TestDHCPClientPreferences(TestCase):
    def test_functions(self):
        self.assertRaises(
            ValueError,
            SystemConfiguration.DHCPClientPreferencesSetApplicationOptions,
            "org.pyobjc.TestSuite",
            [9, 10, 0],
            4,
        )

        r = SystemConfiguration.DHCPClientPreferencesSetApplicationOptions(
            "org.pyobjc.TestSuite", [9, 10, 0, 9], 4
        )
        self.assertTrue(r is True or r is False)

        r, count = SystemConfiguration.DHCPClientPreferencesCopyApplicationOptions(
            "com.apple.SystemPreferences", None
        )
        self.assertIs(r, None)
        self.assertTrue(count == 0)
