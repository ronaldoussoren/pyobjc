from PyObjCTools.TestSupport import *
from SystemConfiguration import *
from Foundation import NSMutableDictionary

try:
    unicode
except NameError:
    unicode = str

class TestSCPreferencesPath (TestCase):

    def testFunctions(self):
        ref = SCPreferencesCreate(None, "pyobjc.test", "pyobjc.test")
        self.assertIsInstance(ref, SCPreferencesRef)

        r = SCPreferencesAddValue(ref, "use",
                NSMutableDictionary.dictionaryWithDictionary_(
                    { "python2": True, "python3": False }))
        self.assertTrue(r)

        v = SCPreferencesPathCreateUniqueChild(ref, "/")
        self.assertIsInstance(v, unicode)

        v = SCPreferencesPathGetValue(ref, "/use")
        self.assertIsInstance(v, NSDictionary)

        v = SCPreferencesPathSetValue(ref, "/use", dict(python2=True, python3=True))
        self.assertTrue(v is True)

        v = SCPreferencesPathSetLink(ref, "/use_python", "/use")
        self.assertTrue(v is True)

        v = SCPreferencesPathGetLink(ref, "/use_python")
        self.assertEqual(v, "/use")

        v = SCPreferencesPathRemoveValue(ref, "/use")
        self.assertTrue(v is True)

if __name__ == "__main__":
    main()
