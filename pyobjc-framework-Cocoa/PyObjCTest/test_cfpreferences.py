import os

import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestPreferences(TestCase):
    def testGetting(self):
        v = CoreFoundation.CFPreferencesCopyAppValue(
            "Default Window Settings", "com.apple.Terminal"
        )
        self.assertIsInstance(v, str)
        self.assertResultIsBOOL(CoreFoundation.CFPreferencesGetAppBooleanValue)
        self.assertArgHasType(CoreFoundation.CFPreferencesGetAppBooleanValue, 2, b"o^Z")
        v, valid = CoreFoundation.CFPreferencesGetAppBooleanValue(
            "SecureKeyboardEntry", "com.apple.Terminal", None
        )
        self.assertTrue(valid)
        self.assertIsInstance(v, bool)
        self.assertArgHasType(CoreFoundation.CFPreferencesGetAppIntegerValue, 2, b"o^Z")
        v, valid = CoreFoundation.CFPreferencesGetAppIntegerValue(
            "ABMetaDataChangeCount", "com.apple.AddressBook", None
        )
        # self.assertTrue(valid)
        self.assertIsInstance(v, int)
        v = CoreFoundation.CFPreferencesCopyValue(
            "Default Window Settings",
            "com.apple.Terminal",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertIsInstance(v, str)
        v = CoreFoundation.CFPreferencesCopyMultiple(
            None,
            "com.apple.Terminal",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        v = CoreFoundation.CFPreferencesCopyMultiple(
            ["AutoFocus", "WindowCloseAction"],
            "com.apple.Terminal",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        self.assertResultIsBOOL(CoreFoundation.CFPreferencesAppValueIsForced)
        v = CoreFoundation.CFPreferencesAppValueIsForced(
            "AutoFocus", "com.apple.Terminal"
        )
        self.assertIs(v is True or v, False)

    def testSetting(self):
        prefsFn = os.path.expanduser("~/Library/Preferences/PyObjCTest.plist")
        if os.path.exists(prefsFn):
            os.unlink(prefsFn)

        v = CoreFoundation.CFPreferencesCopyAppValue("PyObjCTestValue", "PyObjCTest")
        self.assertIs(v, None)
        CoreFoundation.CFPreferencesSetAppValue(
            "PyObjCTestValue", "value1", "PyObjCTest"
        )
        v = CoreFoundation.CFPreferencesCopyAppValue("PyObjCTestValue", "PyObjCTest")
        self.assertEqual(v, "value1")
        CoreFoundation.CFPreferencesSetAppValue("PyObjCTestValue", None, "PyObjCTest")
        CoreFoundation.CFPreferencesAddSuitePreferencesToApp(
            "PyObjCTest", CoreFoundation.kCFPreferencesCurrentApplication
        )
        CoreFoundation.CFPreferencesRemoveSuitePreferencesFromApp(
            "PyObjCTest", CoreFoundation.kCFPreferencesCurrentApplication
        )

        ok = CoreFoundation.CFPreferencesAppSynchronize("PyObjCTest")
        self.assertTrue(ok)

        CoreFoundation.CFPreferencesSetValue(
            "PyObjCTestValue2",
            "value2",
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        v = CoreFoundation.CFPreferencesCopyValue(
            "PyObjCTestValue2",
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertEqual(v, "value2")
        CoreFoundation.CFPreferencesSetValue(
            "PyObjCTestValue2",
            None,
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        v = CoreFoundation.CFPreferencesCopyValue(
            "PyObjCTestValue2",
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertIs(v, None)
        v = CoreFoundation.CFPreferencesCopyValue(
            "PyObjCTestValue2",
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        # self.assertIsNot(v, None)
        CoreFoundation.CFPreferencesSetMultiple(
            {"key1": 99, "key2": 42},
            ["PyObjCTestValue"],
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        v = CoreFoundation.CFPreferencesCopyValue(
            "PyObjCTestValue",
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertIs(v, None)
        v = CoreFoundation.CFPreferencesCopyValue(
            "key2",
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertEqual(v, 42)
        if os.path.exists(prefsFn):
            os.unlink(prefsFn)
        ok = CoreFoundation.CFPreferencesSynchronize(
            "PyObjCTest",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )

        self.assertTrue(ok)

        self.assertResultIsCFRetained(CoreFoundation.CFPreferencesCopyApplicationList)
        apps = CoreFoundation.CFPreferencesCopyApplicationList(
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertIsInstance(apps, CoreFoundation.CFArrayRef)
        self.assertIn("com.apple.AddressBook", apps)
        self.assertResultIsCFRetained(CoreFoundation.CFPreferencesCopyKeyList)
        keys = CoreFoundation.CFPreferencesCopyKeyList(
            "com.apple.dock",
            CoreFoundation.kCFPreferencesCurrentUser,
            CoreFoundation.kCFPreferencesAnyHost,
        )
        self.assertIsInstance(keys, CoreFoundation.CFArrayRef)
        self.assertTrue("region" in keys or "version" in keys)

    def testConstants(self):
        self.assertIsInstance(CoreFoundation.kCFPreferencesAnyApplication, str)
        self.assertIsInstance(CoreFoundation.kCFPreferencesCurrentApplication, str)
        self.assertIsInstance(CoreFoundation.kCFPreferencesAnyHost, str)
        self.assertIsInstance(CoreFoundation.kCFPreferencesCurrentHost, str)
        self.assertIsInstance(CoreFoundation.kCFPreferencesAnyUser, str)
        self.assertIsInstance(CoreFoundation.kCFPreferencesCurrentUser, str)
