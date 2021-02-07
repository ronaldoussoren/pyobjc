import os

from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import SystemConfiguration
import objc


class TestSCDynamicStore(TestCase):
    def testTypes(self):
        self.assertTrue(
            isinstance(SystemConfiguration.SCDynamicStoreRef, objc.objc_class)
        )

    def testStructs(self):
        self.assertFalse(hasattr(SystemConfiguration, "SCDynamicStoreContext"))

    def testFunctions(self):
        n = SystemConfiguration.SCDynamicStoreGetTypeID()
        self.assertTrue(isinstance(n, int))

        lst = []
        info = object()

        def callback(store, changedKeys, info):
            lst.append((store, changedKeys, info))

        st = SystemConfiguration.SCDynamicStoreCreate(
            None, "pyobjc.test", callback, info
        )
        self.assertTrue(isinstance(st, SystemConfiguration.SCDynamicStoreRef))

        st = SystemConfiguration.SCDynamicStoreCreateWithOptions(
            None, "pyobjc.test", {}, callback, info
        )
        self.assertTrue(isinstance(st, SystemConfiguration.SCDynamicStoreRef))

        src = SystemConfiguration.SCDynamicStoreCreateRunLoopSource(None, st, 0)
        self.assertTrue(isinstance(src, SystemConfiguration.CFRunLoopSourceRef))
        del src

        v = SystemConfiguration.SCDynamicStoreCopyKeyList(st, ".*")
        self.assertTrue(isinstance(v, SystemConfiguration.CFArrayRef))
        self.assertTrue(len(v) > 0)
        self.assertTrue(isinstance(v[0], str))

        r = SystemConfiguration.SCDynamicStoreAddValue(st, "Setup:/PyObjC", {"key": 42})
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCDynamicStoreAddTemporaryValue(
            st, "Setup:/PyObjC", {"key": 42}
        )
        self.assertTrue(r is True or r is False)

        v = SystemConfiguration.SCDynamicStoreCopyValue(st, "Setup:/")
        self.assertTrue(isinstance(v, SystemConfiguration.CFDictionaryRef))

        v = SystemConfiguration.SCDynamicStoreCopyMultiple(st, None, [".*"])
        self.assertTrue(isinstance(v, SystemConfiguration.CFDictionaryRef))

        r = SystemConfiguration.SCDynamicStoreSetValue(st, "Setup:/PyObjC", {"key": 42})
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCDynamicStoreSetMultiple(
            st, {"Setup:/PyObjC2": {"key": 42}}, ["Setup:/PyObjC"], ["System:/"]
        )
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCDynamicStoreRemoveValue(st, "Setup:/PyObjC")
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCDynamicStoreNotifyValue(st, "Setup:/")
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCDynamicStoreSetNotificationKeys(st, ["Setup:/"], None)
        self.assertTrue(r is True)

        r = SystemConfiguration.SCDynamicStoreCopyNotifiedKeys(st)
        self.assertTrue(isinstance(r, SystemConfiguration.CFArrayRef))

    @expectedFailure
    def testCallbacks(self):
        if os.getuid() != 0:
            self.fail("WARNING: Need root privileges to test callback mechanism")
            return

        info = object()
        lst = []

        def callback(store, changedKeys, info):
            lst.append((store, changedKeys, info))

        st = SystemConfiguration.SCDynamicStoreCreate(
            None, b"pyobjc.test", callback, info
        )

        SystemConfiguration.SCDynamicStoreSetNotificationKeys(st, None, [".*"])
        src = SystemConfiguration.SCDynamicStoreCreateRunLoopSource(None, st, 0)
        self.assertTrue(isinstance(src, SystemConfiguration.CFRunLoopSourceRef))

        SystemConfiguration.SCDynamicStoreAddTemporaryValue(
            st, "pyobjc.test.key", "value"
        )

        SystemConfiguration.CFRunLoopAddSource(
            SystemConfiguration.CFRunLoopGetCurrent(),
            src,
            SystemConfiguration.kCFRunLoopCommonModes,
        )
        SystemConfiguration.CFRunLoopRunInMode(
            SystemConfiguration.kCFRunLoopDefaultMode, 2.0, False
        )

        self.assertTrue(len(lst) > 1)
        self.assertTrue(lst[0][0] is st)
        self.assertIsInstance(lst[0][1], SystemConfiguration.CFArrayRef)
        self.assertTrue(lst[0][2] is info)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        self.assertResultIsBOOL(SystemConfiguration.SCDynamicStoreSetDispatchQueue)

    def testContants(self):
        self.assertTrue(
            isinstance(SystemConfiguration.kSCDynamicStoreUseSessionKeys, str)
        )
