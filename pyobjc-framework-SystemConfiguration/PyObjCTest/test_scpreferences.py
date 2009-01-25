from PyObjCTools.TestSupport import *
from SystemConfiguration import *

#from SecurityFoundation import SFAuthorization

class TestSCPreferences (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kSCPreferencesNotificationCommit, 1<<0)
        self.failUnlessEqual(kSCPreferencesNotificationApply, 1<<1)

    def testFunctions(self):
        self.failUnlessIsInstance(SCPreferencesGetTypeID(), (int, long))

        ref = SCPreferencesCreate(None, "pyobjc.test", "pyobjc.test")
        self.failUnlessIsInstance(ref, SCPreferencesRef)

        self.failUnlessResultIsBOOL(SCPreferencesLock)
        self.failUnlessArgIsBOOL(SCPreferencesLock, 1)
        v = SCPreferencesLock(ref, False)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessResultIsBOOL(SCPreferencesUnlock)
        v = SCPreferencesUnlock(ref)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessResultIsBOOL(SCPreferencesCommitChanges)
        v = SCPreferencesCommitChanges(ref)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessResultIsBOOL(SCPreferencesApplyChanges)
        v = SCPreferencesApplyChanges(ref)
        self.failUnlessIsInstance(v, bool)

        r = SCPreferencesGetSignature(ref)
        self.failUnlessIsInstance(r, CFDataRef)

        r = SCPreferencesCopyKeyList(ref)
        self.failUnlessIsInstance(r, CFArrayRef)

        l = []
        def callback(ref, key, ctx):
            l.append([ref, key, ctx])
            print key
        ctx = object()

        v = SCPreferencesSetCallback(ref, callback, ctx)
        self.failUnless(v is True)

        self.failUnlessResultIsBOOL(SCPreferencesAddValue)
        r = SCPreferencesAddValue(ref, "use_python3", False)
        self.failUnless(r is True)

        v = SCPreferencesGetValue(ref, "use_python3")
        self.failUnless(v is False)

        v = SCPreferencesGetValue(ref, "use_python4")
        self.failUnless(v is None)

        self.failUnlessResultIsBOOL(SCPreferencesSetValue)
        r = SCPreferencesSetValue(ref, "use_python3", "on newyearsday")
        self.failUnless(r is True)

        self.failUnlessResultIsBOOL(SCPreferencesRemoveValue)
        r = SCPreferencesRemoveValue(ref, "use_python3")

        self.failUnlessResultIsBOOL(SCPreferencesScheduleWithRunLoop)
        rl = CFRunLoopGetCurrent()
        r = SCPreferencesScheduleWithRunLoop(ref, rl, kCFRunLoopCommonModes)
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, False)

        self.failUnlessResultIsBOOL(SCPreferencesUnscheduleFromRunLoop)
        r = SCPreferencesUnscheduleFromRunLoop(ref, rl, kCFRunLoopCommonModes)


        SCPreferencesSynchronize(ref)



    def testSecurityIntegreation(self):
        self.fail("Need Security framework wrappers")
        #aref = SFAuthorization.authorization().authorizationRef ()
        # XXX: Security frameworks aren't wrapped yet
        aref = None
        ref = SCPreferencesCreateWithAuthorization(None, "pyobjc.test", "pyobjc.test", aref)
        self.failUnlessIsInstance(ref, SCPreferencesRef)



    
            



if __name__ == "__main__":
    main()
