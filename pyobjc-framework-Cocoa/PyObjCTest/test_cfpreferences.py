from PyObjCTools.TestSupport import *
import os
from CoreFoundation import *


class TestPreferences (TestCase):
    def testGetting(self):
        v = CFPreferencesCopyAppValue("WindowCloseAction", "com.apple.Terminal")
        self.assertIsInstance(v, unicode)
        self.assertResultIsBOOL(CFPreferencesGetAppBooleanValue)
        self.assertArgHasType(CFPreferencesGetAppBooleanValue, 2, b'o^Z')
        v, valid = CFPreferencesGetAppBooleanValue("AutoFocus", "com.apple.Terminal", None)
        self.assertTrue(valid)
        self.assertIsInstance(v, bool)
        self.assertArgHasType(CFPreferencesGetAppIntegerValue, 2, b'o^Z')
        v, valid = CFPreferencesGetAppIntegerValue("WindowCloseAction", "com.apple.Terminal", None)
        self.assertTrue(valid)
        self.assertIsInstance(v, (int, long))
        v = CFPreferencesCopyValue("WindowCloseAction", "com.apple.Terminal", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIsInstance(v, unicode)
        v = CFPreferencesCopyMultiple(None, "com.apple.Terminal", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIsInstance(v, CFDictionaryRef)
        v = CFPreferencesCopyMultiple([u"AutoFocus", u"WindowCloseAction"], "com.apple.Terminal", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertResultIsBOOL(CFPreferencesAppValueIsForced)
        v = CFPreferencesAppValueIsForced("AutoFocus", "com.apple.Terminal")
        self.assertIs(v is True or v, False)
    def testSetting(self):
        prefsFn = os.path.expanduser('~/Library/Preferences/PyObjCTest.plist')
        if os.path.exists(prefsFn):
            os.unlink(prefsFn)

        v = CFPreferencesCopyAppValue("PyObjCTestValue", "PyObjCTest")
        self.assertIs(v, None)
        CFPreferencesSetAppValue("PyObjCTestValue", "value1", "PyObjCTest")
        v = CFPreferencesCopyAppValue("PyObjCTestValue", "PyObjCTest")
        self.assertEqual(v , "value1")
        CFPreferencesAddSuitePreferencesToApp("PyObjCTest", kCFPreferencesCurrentApplication)
        CFPreferencesRemoveSuitePreferencesFromApp("PyObjCTest", kCFPreferencesCurrentApplication)

        ok = CFPreferencesAppSynchronize("PyObjCTest")
        self.assertTrue(ok)
        self.assertTrue(os.path.exists(prefsFn))
        os.unlink(prefsFn)

        CFPreferencesSetValue("PyObjCTestValue2", "value2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        v = CFPreferencesCopyValue("PyObjCTestValue2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertEqual(v , "value2")
        CFPreferencesSetValue("PyObjCTestValue2", None, "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        v = CFPreferencesCopyValue("PyObjCTestValue2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIs(v, None)
        v = CFPreferencesCopyValue("PyObjCTestValue", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIsNot(v, None)
        CFPreferencesSetMultiple({
            'key1': 99,
            'key2': 42,
        }, ["PyObjCTestValue"], "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        v = CFPreferencesCopyValue("PyObjCTestValue", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIs(v, None)
        v = CFPreferencesCopyValue("key2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertEqual(v , 42)
        if os.path.exists(prefsFn):
            os.unlink(prefsFn)
        ok = CFPreferencesSynchronize("PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertTrue(ok)
        self.assertTrue(os.path.exists(prefsFn))
        os.unlink(prefsFn)

        self.assertResultIsCFRetained(CFPreferencesCopyApplicationList)
        apps = CFPreferencesCopyApplicationList(kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIsInstance(apps, CFArrayRef)
        self.assertIsIn(u"com.apple.AddressBook", apps)
        self.assertResultIsCFRetained(CFPreferencesCopyKeyList)
        keys = CFPreferencesCopyKeyList(u"com.apple.AddressBook", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.assertIsInstance(keys, CFArrayRef)
        self.assertIsIn(u"ABNameSorting", keys)
    def testConstants(self):
        self.assertIsInstance(kCFPreferencesAnyApplication, unicode)
        self.assertIsInstance(kCFPreferencesCurrentApplication, unicode)
        self.assertIsInstance(kCFPreferencesAnyHost, unicode)
        self.assertIsInstance(kCFPreferencesCurrentHost, unicode)
        self.assertIsInstance(kCFPreferencesAnyUser, unicode)
        self.assertIsInstance(kCFPreferencesCurrentUser, unicode)
if __name__ == "__main__":
    main()
