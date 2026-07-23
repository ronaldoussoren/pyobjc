from PyObjCTools.TestSupport import TestCase, NoObjCClass
import SystemConfiguration
import os


class TestSCPreferences(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SystemConfiguration.SCPreferencesNotification)
        self.assertEqual(SystemConfiguration.kSCPreferencesNotificationCommit, 1 << 0)
        self.assertEqual(SystemConfiguration.kSCPreferencesNotificationApply, 1 << 1)

    def test_functions(self):
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

        def callback(ref, tp, ctx):
            lst.append((ref, tp, ctx))

        ctx = object()

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            SystemConfiguration.SCPreferencesSetCallback()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            SystemConfiguration.SCPreferencesSetCallback(NoObjCClass(), callback, ctx)

        v = SystemConfiguration.SCPreferencesSetCallback(ref, callback, ctx)
        self.assertTrue(v is True)

        rl = SystemConfiguration.CFRunLoopGetCurrent()
        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesScheduleWithRunLoop)
        r = SystemConfiguration.SCPreferencesScheduleWithRunLoop(
            ref, rl, SystemConfiguration.kCFRunLoopCommonModes
        )

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

        SystemConfiguration.SCPreferencesApplyChanges(ref)

        SystemConfiguration.CFRunLoopRunInMode(
            SystemConfiguration.kCFRunLoopDefaultMode, 1.0, False
        )

        if os.geteuid() == 0:
            self.assertGreater(len(lst), 0)

            for item in lst:
                self.assertEqual(len(item), 3)
                self.assertIs(item[0], ref)
                self.assertIs(
                    item[1], SystemConfiguration.kSCPreferencesNotificationApply
                )
                self.assertIs(item[2], ctx)

            def callback_raises(*args):
                raise RuntimeError("callback error")

            v = SystemConfiguration.SCPreferencesSetCallback(ref, callback_raises, ctx)
            self.assertTrue(v is True)

            SystemConfiguration.SCPreferencesApplyChanges(ref)

            with self.assertRaisesRegex(RuntimeError, "callback error"):
                SystemConfiguration.CFRunLoopRunInMode(
                    SystemConfiguration.kCFRunLoopDefaultMode, 1.0, False
                )

        self.assertResultIsBOOL(SystemConfiguration.SCPreferencesUnscheduleFromRunLoop)
        r = SystemConfiguration.SCPreferencesUnscheduleFromRunLoop(
            ref, rl, SystemConfiguration.kCFRunLoopCommonModes
        )

        SystemConfiguration.SCPreferencesSynchronize(ref)

        SystemConfiguration.SCPreferencesSetDispatchQueue

    def test_security_integration(self):
        self.assertResultIsCFRetained(
            SystemConfiguration.SCPreferencesCreateWithAuthorization
        )
