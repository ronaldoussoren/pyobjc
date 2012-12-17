from PyObjCTools.TestSupport import *

from SystemConfiguration import *
import SystemConfiguration
import os

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestSCDynamicStore (TestCase):
    def testTypes(self):
        self.assertTrue(isinstance(SCDynamicStoreRef, objc.objc_class))

    def testStructs(self):
        self.assertFalse( hasattr(SystemConfiguration, 'SCDynamicStoreContext') )

    def testFunctions(self):
        n = SCDynamicStoreGetTypeID()
        self.assertTrue(isinstance(n, (int, long)))


        l = []
        info = object()
        def callback(store, changedKeys, info):
            l.append((store, changedKeys, info))

        st = SCDynamicStoreCreate(None,
                "pyobjc.test",
                callback, info)
        self.assertTrue(isinstance(st, SCDynamicStoreRef))

        st = SCDynamicStoreCreateWithOptions(None,
                "pyobjc.test",
                {},
                callback,
                info)
        self.assertTrue(isinstance(st, SCDynamicStoreRef))

        src = SCDynamicStoreCreateRunLoopSource(None, st, 0)
        self.assertTrue(isinstance(src, CFRunLoopSourceRef))
        del src

        v = SCDynamicStoreCopyKeyList(st, b'.*'.decode('latin1'))
        self.assertTrue(isinstance(v, CFArrayRef))
        self.assertTrue(len(v) > 0)
        self.assertTrue(isinstance(v[0], unicode))

        r = SCDynamicStoreAddValue(st, "Setup:/PyObjC", { b"key".decode('latin1'):42 })
        self.assertTrue(r is True or r is False)

        r = SCDynamicStoreAddTemporaryValue(st, "Setup:/PyObjC", { b"key".decode('latin1'):42 })
        self.assertTrue(r is True or r is False)

        v = SCDynamicStoreCopyValue(st, "Setup:/")
        self.assertTrue(isinstance(v, CFDictionaryRef))

        v = SCDynamicStoreCopyMultiple(st, None, ['.*'])
        self.assertTrue(isinstance(v, CFDictionaryRef))

        r = SCDynamicStoreSetValue(st, "Setup:/PyObjC", { b"key".decode('latin1'):42 })
        self.assertTrue(r is True or r is False)

        r = SCDynamicStoreSetMultiple(st,
                {
                    'Setup:/PyObjC2': { b"key".decode('latin1'): 42},
                },
                ['Setup:/PyObjC'],
                ['System:/'])
        self.assertTrue(r is True or r is False)

        r = SCDynamicStoreRemoveValue(st, "Setup:/PyObjC")
        self.assertTrue(r is True or r is False)

        r = SCDynamicStoreNotifyValue(st, "Setup:/")
        self.assertTrue(r is True or r is False)

        r = SCDynamicStoreSetNotificationKeys(st, ['Setup:/'], None)
        self.assertTrue(r is True)

        r = SCDynamicStoreCopyNotifiedKeys(st)
        self.assertTrue(isinstance(r, CFArrayRef))

    @expectedFailure
    def testCallbacks(self):
        if os.getuid() != 0:
            self.fail("WARNING: Need root privileges to test callback mechanism")
            return

        info = object()
        l = []
        def callback(store, changedKeys, info):
            l.append((store, changedKeys, info))

        st = SCDynamicStoreCreate(None,
                b"pyobjc.test".decode('latin1'),
                callback, info)

        SCDynamicStoreSetNotificationKeys(st, None, ['.*'])
        src = SCDynamicStoreCreateRunLoopSource(None, st, 0)
        self.assertTrue(isinstance(src, CFRunLoopSourceRef))

        SCDynamicStoreAddTemporaryValue(st, "pyobjc.test.key", "value")

        CFRunLoopAddSource(CFRunLoopGetCurrent(), src, kCFRunLoopCommonModes)
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 2.0, False)

        self.assertTrue(len(l) > 1)
        self.assertTrue(l[0][0] is st)
        self.assertIsInstance(l[0][1], CFArrayRef)
        self.assertTrue(l[0][2] is info)









    def testContants(self):
        self.assertTrue( isinstance(kSCDynamicStoreUseSessionKeys, unicode) )


if __name__ == "__main__":
    main()
