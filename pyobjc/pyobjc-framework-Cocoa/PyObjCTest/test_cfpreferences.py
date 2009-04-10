from PyObjCTools.TestSupport import *
import os
from CoreFoundation import *


class TestPreferences (TestCase):
    def testGetting(self):
        v = CFPreferencesCopyAppValue("WindowCloseAction", "com.apple.Terminal")
        self.failUnless(isinstance(v, unicode))

        self.failUnlessResultIsBOOL(CFPreferencesGetAppBooleanValue)
        self.failUnlessArgHasType(CFPreferencesGetAppBooleanValue, 2, 'o^Z')
        v, valid = CFPreferencesGetAppBooleanValue("AutoFocus", "com.apple.Terminal", None)
        self.failUnless(valid)
        self.failUnless(isinstance(v, bool))

        self.failUnlessArgHasType(CFPreferencesGetAppIntegerValue, 2, 'o^Z')
        v, valid = CFPreferencesGetAppIntegerValue("WindowCloseAction", "com.apple.Terminal", None)
        self.failUnless(valid)
        self.failUnless(isinstance(v, (int, long)))

        v = CFPreferencesCopyValue("WindowCloseAction", "com.apple.Terminal", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(isinstance(v, unicode))


        v = CFPreferencesCopyMultiple(None, "com.apple.Terminal", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(isinstance(v, CFDictionaryRef))

        v = CFPreferencesCopyMultiple([u"AutoFocus", u"WindowCloseAction"], "com.apple.Terminal", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(isinstance(v, CFDictionaryRef))

        self.failUnlessResultIsBOOL(CFPreferencesAppValueIsForced)
        v = CFPreferencesAppValueIsForced("AutoFocus", "com.apple.Terminal")
        self.failUnless(v is True or v is False)

    def testSetting(self):
        prefsFn = os.path.expanduser('~/Library/Preferences/PyObjCTest.plist')
        if os.path.exists(prefsFn):
            os.unlink(prefsFn)

        v = CFPreferencesCopyAppValue("PyObjCTestValue", "PyObjCTest")
        self.failUnless(v is None)

        CFPreferencesSetAppValue("PyObjCTestValue", "value1", "PyObjCTest")
        v = CFPreferencesCopyAppValue("PyObjCTestValue", "PyObjCTest")
        self.failUnless(v == "value1")

        CFPreferencesAddSuitePreferencesToApp("PyObjCTest", kCFPreferencesCurrentApplication)
        CFPreferencesRemoveSuitePreferencesFromApp("PyObjCTest", kCFPreferencesCurrentApplication)

        ok = CFPreferencesAppSynchronize("PyObjCTest")
        self.failUnless(ok)
        self.failUnless(os.path.exists(prefsFn))
        os.unlink(prefsFn)

        CFPreferencesSetValue("PyObjCTestValue2", "value2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        v = CFPreferencesCopyValue("PyObjCTestValue2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(v == "value2")

        CFPreferencesSetValue("PyObjCTestValue2", None, "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        v = CFPreferencesCopyValue("PyObjCTestValue2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(v is None)

        v = CFPreferencesCopyValue("PyObjCTestValue", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(v is not None)
        CFPreferencesSetMultiple({
            'key1': 99,
            'key2': 42,
        }, ["PyObjCTestValue"], "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        v = CFPreferencesCopyValue("PyObjCTestValue", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(v is None)
        v = CFPreferencesCopyValue("key2", "PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(v == 42)

        if os.path.exists(prefsFn):
            os.unlink(prefsFn)
        ok = CFPreferencesSynchronize("PyObjCTest", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(ok)
        self.failUnless(os.path.exists(prefsFn))
        os.unlink(prefsFn)

        self.failUnlessResultIsCFRetained(CFPreferencesCopyApplicationList)
        apps = CFPreferencesCopyApplicationList(kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(isinstance(apps, CFArrayRef))
        self.failUnless(u"com.apple.AddressBook" in apps)

        self.failUnlessResultIsCFRetained(CFPreferencesCopyKeyList)
        keys = CFPreferencesCopyKeyList(u"com.apple.AddressBook", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
        self.failUnless(isinstance(keys, CFArrayRef))
        self.failUnless(u"ABNameSorting" in keys)

    def testConstants(self):
        self.failUnless(isinstance(kCFPreferencesAnyApplication, unicode))
        self.failUnless(isinstance(kCFPreferencesCurrentApplication, unicode))
        self.failUnless(isinstance(kCFPreferencesAnyHost, unicode))
        self.failUnless(isinstance(kCFPreferencesCurrentHost, unicode))
        self.failUnless(isinstance(kCFPreferencesAnyUser, unicode))
        self.failUnless(isinstance(kCFPreferencesCurrentUser, unicode))


if __name__ == "__main__":
    main()
