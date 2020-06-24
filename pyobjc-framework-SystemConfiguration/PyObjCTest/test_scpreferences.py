from PyObjCTools.TestSupport import TestCase, min_os_level
import SystemConfiguration


# from SecurityFoundation import SFAuthorization
class TestSCPreferences(TestCase):
    def testConstants(self):
        self.assertEqual(SystemConfiguration.kSCPreferencesNotificationCommit, 1 << 0)
        self.assertEqual(SystemConfiguration.kSCPreferencesNotificationApply, 1 << 1)

    def testFunctions(self):
        self.assertIsInstance(SystemConfiguration.SCPreferencesGetTypeID(), int)

        ref = SystemConfiguration.SCPreferencesCreate(
            None, "pyobjc.test", "pyobjc.test"
        )
        self.assertIsInstance(ref, SystemConfiguration.SCPreferencesRef)

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesLock)
        self.assertArgIsBOOL(SystemConfiguration.SCPreferencesLock, 1)
        v = SystemConfiguration.SCPreferencesLock(ref, False)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesUnlock)
        v = SystemConfiguration.SCPreferencesUnlock(ref)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesCommitChanges)
        v = SystemConfiguration.SCPreferencesCommitChanges(ref)
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesApplyChanges)
        v = SystemConfiguration.SCPreferencesApplyChanges(ref)
        self.assertIsInstance(v, bool)

        r = SystemConfiguration.SCPreferencesGetSignature(ref)
        self.assertIsInstance(r, SystemConfiguration.CFDataRef)

        r = SystemConfiguration.SCPreferencesCopyKeyList(ref)
        self.assertIsInstance(r, SystemConfiguration.CFArrayRef)

        lst = []

        def callback(ref, key, ctx):
            lst.append([ref, key, ctx])

        ctx = object()

        v = SystemConfiguration.SCPreferencesSetCallback(ref, callback, ctx)
        self.assertTrue(v is True)

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesAddValue)
        r = SystemConfiguration.SCPreferencesAddValue(ref, "use_python3", False)
        self.assertTrue(r is True)

        v = SystemConfiguration.SCPreferencesGetValue(ref, "use_python3")
        self.assertTrue(v is False)

        v = SystemConfiguration.SCPreferencesGetValue(ref, "use_python4")
        self.assertTrue(v is None)

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesSetValue)
        r = SystemConfiguration.SCPreferencesSetValue(
            ref, "use_python3", "on newyearsday"
        )
        self.assertTrue(r is True)

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesRemoveValue)
        r = SystemConfiguration.SCPreferencesRemoveValue(ref, "use_python3")

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesScheduleWithRunLoop)
        rl = SystemConfiguration.CFRunLoopGetCurrent()
        r = SystemConfiguration.SCPreferencesScheduleWithRunLoop(
            ref, rl, SystemConfiguration.kCFRunLoopCommonModes
        )
        SystemConfiguration.CFRunLoopRunInMode(
            SystemConfiguration.kCFRunLoopDefaultMode, 1.0, False
        )

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesUnscheduleFromRunLoop)
        r = SystemConfiguration.SCPreferencesUnscheduleFromRunLoop(
            ref, rl, SystemConfiguration.kCFRunLoopCommonModes
        )

        SystemConfiguration.SCPreferencesSynchronize(ref)

    def testSecurityIntegreation(self):
        self.assertResultIsCFRetained(
            SystemConfiguration.SCPreferencesCreateWithAuthorization
        )

    @min_os_level("10.6")
    def testFunctions10_6(self):
        SystemConfiguration.SCPreferencesSetDispatchQueue
