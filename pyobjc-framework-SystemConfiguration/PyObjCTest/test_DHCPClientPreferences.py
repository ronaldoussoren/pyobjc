from PyObjCTools.TestSupport import *

from SystemConfiguration import *


class TestDHCPClientPreferences (TestCase):
    def testFunctions(self):
        self.assertRaises(ValueError, DHCPClientPreferencesSetApplicationOptions, 
                u"org.pyobjc.TestSuite", [9, 10, 0], 4)

        r = DHCPClientPreferencesSetApplicationOptions( 
                u"org.pyobjc.TestSuite", [9, 10, 0, 9], 4)
        self.assertTrue(r is True or r is False)

        r, count = DHCPClientPreferencesCopyApplicationOptions(u"com.apple.SystemPreferences", None)
        self.assertTrue(r is objc.NULL)
        self.assertTrue(count == 0)

if __name__ == "__main__":
    main()
