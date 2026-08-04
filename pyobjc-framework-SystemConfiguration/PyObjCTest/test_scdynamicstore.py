import os

from PyObjCTools.TestSupport import TestCase, expectedFailureIf, NoObjCClass
import SystemConfiguration
import objc


class TestSCDynamicStore(TestCase):
    def test_constants(self):
        self.assertTrue(
            isinstance(SystemConfiguration.kSCDynamicStoreUseSessionKeys, str)
        )

    def test_types(self):
        self.assertTrue(
            isinstance(SystemConfiguration.SCDynamicStoreRef, objc.objc_class)
        )

    def test_structs(self):
        self.assertFalse(hasattr(SystemConfiguration, "SCDynamicStoreContext"))

    def test_functions(self):
        n = SystemConfiguration.SCDynamicStoreGetTypeID()
        self.assertTrue(isinstance(n, int))

        lst = []
        info = object()

        def callback(store, changedKeys, info):
            lst.append((store, changedKeys, info))

        with self.assertRaisesRegex(TypeError, "Need 4 arguments, got 0"):
            SystemConfiguration.SCDynamicStoreCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            st = SystemConfiguration.SCDynamicStoreCreate(
                NoObjCClass(), "pyobjc.test", callback, info
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            st = SystemConfiguration.SCDynamicStoreCreate(
                None, NoObjCClass(), callback, info
            )

        st = SystemConfiguration.SCDynamicStoreCreate(
            None, "pyobjc.test", callback, info
        )
        self.assertTrue(isinstance(st, SystemConfiguration.SCDynamicStoreRef))

        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            SystemConfiguration.SCDynamicStoreCreateWithOptions()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            st = SystemConfiguration.SCDynamicStoreCreateWithOptions(
                NoObjCClass(), "pyobjc.test", {}, callback, info
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            st = SystemConfiguration.SCDynamicStoreCreateWithOptions(
                None, NoObjCClass(), {}, callback, info
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            st = SystemConfiguration.SCDynamicStoreCreateWithOptions(
                None, "pyobjc.test", NoObjCClass(), callback, info
            )

        st = SystemConfiguration.SCDynamicStoreCreateWithOptions(
            None,
            "pyobjc.test",
            {SystemConfiguration.kSCDynamicStoreUseSessionKeys: 3.5},
            callback,
            info,
        )
        self.assertIs(st, None)

        st = SystemConfiguration.SCDynamicStoreCreateWithOptions(
            None,
            "pyobjc.test",
            {SystemConfiguration.kSCDynamicStoreUseSessionKeys: True},
            callback,
            info,
        )
        self.assertIsInstance(st, SystemConfiguration.SCDynamicStoreRef)

        src = SystemConfiguration.SCDynamicStoreCreateRunLoopSource(None, st, 0)
        self.assertIsInstance(src, SystemConfiguration.CFRunLoopSourceRef)
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

    @expectedFailureIf(os.geteuid() != 0)
    def test_callbacks(self):
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

        SystemConfiguration.CFRunLoopAddSource(
            SystemConfiguration.CFRunLoopGetCurrent(),
            src,
            SystemConfiguration.kCFRunLoopCommonModes,
        )
        SystemConfiguration.SCDynamicStoreAddTemporaryValue(
            st, "pyobjc.test.key.1", "value"
        )
        SystemConfiguration.CFRunLoopRunInMode(
            SystemConfiguration.kCFRunLoopDefaultMode, 2.0, False
        )

        self.assertTrue(len(lst) > 0)
        self.assertTrue(lst[0][0] is st)
        self.assertIsInstance(lst[0][1], SystemConfiguration.CFArrayRef)
        self.assertTrue(lst[0][2] is info)

        self.assertResultIsBOOL(SystemConfiguration.SCDynamicStoreSetDispatchQueue)

    @expectedFailureIf(os.geteuid() != 0)
    def test_callbacks_raises(self):
        if os.getuid() != 0:
            self.fail("WARNING: Need root privileges to test callback mechanism")
            return

        info = object()
        lst = []

        def callback(store, changedKeys, info):
            raise RuntimeError("callback error")

        st = SystemConfiguration.SCDynamicStoreCreate(
            None, b"pyobjc.test.2", callback, info
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
        with self.assertRaisesRegex(RuntimeError, "callback error"):
            SystemConfiguration.CFRunLoopRunInMode(
                SystemConfiguration.kCFRunLoopDefaultMode, 2.0, False
            )

        self.assertEqual(lst, [])
