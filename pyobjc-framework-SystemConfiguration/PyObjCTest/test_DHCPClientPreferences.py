from PyObjCTools.TestSupport import *

from SystemConfiguration import *


class TestDHCPClientPreferences (TestCase):
    def testFunctions(self):
        self.assertRaises(ValueError, DHCPClientPreferencesSetApplicationOptions,
                b"org.pyobjc.TestSuite".decode('latin1'), [9, 10, 0], 4)

        r = DHCPClientPreferencesSetApplicationOptions(
                b"org.pyobjc.TestSuite".decode('latin1'), [9, 10, 0, 9], 4)
        self.assertTrue(r is True or r is False)

        r, count = DHCPClientPreferencesCopyApplicationOptions(b"com.apple.SystemPreferences".decode('latin1'), None)
        self.assertTrue(r is objc.NULL)
        self.assertTrue(count == 0)

if __name__ == "__main__":
    main()
