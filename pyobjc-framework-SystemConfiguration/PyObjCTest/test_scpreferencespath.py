from PyObjCTools.TestSupport import TestCase
import SystemConfiguration


class TestSCPreferencesPath(TestCase):
    def testFunctions(self):
        ref = SystemConfiguration.SCPreferencesCreate(
            None, "pyobjc.test", "pyobjc.test"
        )
        self.assertIsInstance(ref, SystemConfiguration.SCPreferencesRef)

        r = SystemConfiguration.SCPreferencesAddValue(
            ref,
            "use",
            SystemConfiguration.NSMutableDictionary.dictionaryWithDictionary_(
                {"python2": True, "python3": False}
            ),
        )
        self.assertTrue(r)

        v = SystemConfiguration.SCPreferencesPathCreateUniqueChild(ref, "/")
        self.assertIsInstance(v, str)

        v = SystemConfiguration.SCPreferencesPathGetValue(ref, "/use")
        self.assertIsInstance(v, SystemConfiguration.NSDictionary)

        v = SystemConfiguration.SCPreferencesPathSetValue(
            ref, "/use", {"python2": True, "python3": True}
        )
        self.assertTrue(v is True)

        v = SystemConfiguration.SCPreferencesPathSetLink(ref, "/use_python", "/use")
        self.assertTrue(v is True)

        v = SystemConfiguration.SCPreferencesPathGetLink(ref, "/use_python")
        self.assertEqual(v, "/use")

        v = SystemConfiguration.SCPreferencesPathRemoveValue(ref, "/use")
        self.assertTrue(v is True)
