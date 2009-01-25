from PyObjCTools.TestSupport import *
from SystemConfiguration import *
from Foundation import NSMutableDictionary

class TestSCPreferencesPath (TestCase):

    def testFunctions(self):
        ref = SCPreferencesCreate(None, "pyobjc.test", "pyobjc.test")
        self.failUnlessIsInstance(ref, SCPreferencesRef)

        r = SCPreferencesAddValue(ref, "use", 
                NSMutableDictionary.dictionaryWithDictionary_(
                    { "python2": True, "python3": False }))
        self.failUnless(r)

        v = SCPreferencesPathCreateUniqueChild(ref, "/")
        self.failUnlessIsInstance(v, unicode)

        v = SCPreferencesPathGetValue(ref, "/use")
        self.failUnlessIsInstance(v, CFDictionaryRef)

        v = SCPreferencesPathSetValue(ref, "/use", dict(python2=True, python3=True))
        self.failUnless(v is True)

        v = SCPreferencesPathSetLink(ref, "/use_python", "/use")
        self.failUnless(v is True)

        v = SCPreferencesPathGetLink(ref, "/use_python")
        self.failUnlessEqual(v, "/use")

        v = SCPreferencesPathRemoveValue(ref, "/use")
        self.failUnless(v is True)

if __name__ == "__main__":
    main()
