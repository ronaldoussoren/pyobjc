from PyObjCTools.TestSupport import *
from SystemConfiguration import *

class TestSCPreferencesSetSpecific (TestCase):
    def testFunctions(self):
        ref = SCPreferencesCreate(None, "pyobjc.test", "pyobjc.test")
        self.assertIsInstance(ref, SCPreferencesRef)

        v = SCPreferencesSetComputerName(ref, "my host", kCFStringEncodingUTF8)
        self.assertTrue(isinstance(v, bool))

        v = SCPreferencesSetLocalHostName(ref, "my.host.private")
        self.assertTrue(isinstance(v, bool))

        # NOTE: Do not commit changes, that would mess with the computer running
        # the tests


if __name__ == "__main__":
    main()
