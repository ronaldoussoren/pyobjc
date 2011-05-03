from PyObjCTools.TestSupport import *
from SystemConfiguration import *

#from SecurityFoundation import SFAuthorization

class TestSCPreferences (TestCase):
    def testConstants(self):
        self.assertEqual(kSCPreferencesNotificationCommit, 1<<0)
        self.assertEqual(kSCPreferencesNotificationApply, 1<<1)

    def testFunctions(self):
        self.assertIsInstance(SCPreferencesGetTypeID(), (int, long))

        ref = SCPreferencesCreate(None, "pyobjc.test", "pyobjc.test")
        self.assertIsInstance(ref, SCPreferencesRef)

        self.assertResultIsBOOL(SCPreferencesLock)
        self.assertArgIsBOOL(SCPreferencesLock, 1)
        v = SCPreferencesLock(ref, False)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(SCPreferencesUnlock)
        v = SCPreferencesUnlock(ref)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(SCPreferencesCommitChanges)
        v = SCPreferencesCommitChanges(ref)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(SCPreferencesApplyChanges)
        v = SCPreferencesApplyChanges(ref)
        self.assertIsInstance(v, bool)

        r = SCPreferencesGetSignature(ref)
        self.assertIsInstance(r, CFDataRef)

        r = SCPreferencesCopyKeyList(ref)
        self.assertIsInstance(r, CFArrayRef)

        l = []
        def callback(ref, key, ctx):
            l.append([ref, key, ctx])
            print key
        ctx = object()

        v = SCPreferencesSetCallback(ref, callback, ctx)
        self.assertTrue(v is True)

        self.assertResultIsBOOL(SCPreferencesAddValue)
        r = SCPreferencesAddValue(ref, "use_python3", False)
        self.assertTrue(r is True)

        v = SCPreferencesGetValue(ref, "use_python3")
        self.assertTrue(v is False)

        v = SCPreferencesGetValue(ref, "use_python4")
        self.assertTrue(v is None)

        self.assertResultIsBOOL(SCPreferencesSetValue)
        r = SCPreferencesSetValue(ref, "use_python3", "on newyearsday")
        self.assertTrue(r is True)

        self.assertResultIsBOOL(SCPreferencesRemoveValue)
        r = SCPreferencesRemoveValue(ref, "use_python3")

        self.assertResultIsBOOL(SCPreferencesScheduleWithRunLoop)
        rl = CFRunLoopGetCurrent()
        r = SCPreferencesScheduleWithRunLoop(ref, rl, kCFRunLoopCommonModes)
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, False)

        self.assertResultIsBOOL(SCPreferencesUnscheduleFromRunLoop)
        r = SCPreferencesUnscheduleFromRunLoop(ref, rl, kCFRunLoopCommonModes)


        SCPreferencesSynchronize(ref)



    @expectedFailure
    def testSecurityIntegreation(self):
        self.fail("Need Security framework wrappers")
        #aref = SFAuthorization.authorization().authorizationRef ()
        # XXX: Security frameworks aren't wrapped yet
        aref = None
        ref = SCPreferencesCreateWithAuthorization(None, "pyobjc.test", "pyobjc.test", aref)
        self.assertIsInstance(ref, SCPreferencesRef)



    
            



if __name__ == "__main__":
    main()
