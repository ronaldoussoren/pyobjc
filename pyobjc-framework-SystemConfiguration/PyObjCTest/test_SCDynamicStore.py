from PyObjCTools.TestSupport import *

from SystemConfiguration import *
import SystemConfiguration
import os

class TestSCDynamicStore (TestCase):
    def testTypes(self):
        self.failUnless(isinstance(SCDynamicStoreRef, objc.objc_class))

    def testStructs(self):
        self.failIf( hasattr(SystemConfiguration, 'SCDynamicStoreContext') )

    def testFunctions(self):
        n = SCDynamicStoreGetTypeID()
        self.failUnless(isinstance(n, (int, long)))


        l = []
        info = object()
        def callback(store, changedKeys, info):
            l.append((store, changedKeys, info))

        st = SCDynamicStoreCreate(None, 
                "pyobjc.test", 
                callback, info)
        self.failUnless(isinstance(st, SCDynamicStoreRef))
        
        st = SCDynamicStoreCreateWithOptions(None,
                "pyobjc.test",
                {},
                callback,
                info)
        self.failUnless(isinstance(st, SCDynamicStoreRef))


        src = SCDynamicStoreCreateRunLoopSource(None, st, 0)
        self.failUnless(isinstance(src, CFRunLoopSourceRef))
        del src

        v = SCDynamicStoreCopyKeyList(st, u'.*')
        self.failUnless(isinstance(v, CFArrayRef))
        self.failUnless(len(v) > 0)
        self.failUnless(isinstance(v[0], unicode))

        r = SCDynamicStoreAddValue(st, "Setup:/PyObjC", { u"key":42 })
        self.failUnless(r is True or r is False)

        r = SCDynamicStoreAddTemporaryValue(st, "Setup:/PyObjC", { u"key":42 })
        self.failUnless(r is True or r is False)

        v = SCDynamicStoreCopyValue(st, "Setup:/")
        self.failUnless(isinstance(v, CFDictionaryRef))

        v = SCDynamicStoreCopyMultiple(st, None, ['.*'])
        self.failUnless(isinstance(v, CFDictionaryRef))

        r = SCDynamicStoreSetValue(st, "Setup:/PyObjC", { u"key":42 })
        self.failUnless(r is True or r is False)

        r = SCDynamicStoreSetMultiple(st, 
                {
                    'Setup:/PyObjC2': { u"key": 42},
                },
                ['Setup:/PyObjC'],
                ['System:/'])
        self.failUnless(r is True or r is False)

        r = SCDynamicStoreRemoveValue(st, "Setup:/PyObjC")
        self.failUnless(r is True or r is False)

        r = SCDynamicStoreNotifyValue(st, "Setup:/")
        self.failUnless(r is True or r is False)

        r = SCDynamicStoreSetNotificationKeys(st, ['Setup:/'], None)
        self.failUnless(r is True)

        r = SCDynamicStoreCopyNotifiedKeys(st)
        self.failUnless(isinstance(r, CFArrayRef))

    def testCallbacks(self):
        if os.getuid() != 0:
            self.fail("WARNING: Need root privileges to test callback mechanism")
            return

        info = object()
        l = []
        def callback(store, changedKeys, info):
            l.append((store, changedKeys, info))

        st = SCDynamicStoreCreate(None, 
                u"pyobjc.test", 
                callback, info)

        SCDynamicStoreSetNotificationKeys(st, None, ['.*'])
        src = SCDynamicStoreCreateRunLoopSource(None, st, 0)
        self.failUnless(isinstance(src, CFRunLoopSourceRef))

        SCDynamicStoreAddTemporaryValue(st, "pyobjc.test.key", "value")

        CFRunLoopAddSource(CFRunLoopGetCurrent(), src, kCFRunLoopCommonModes)
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 2.0, False)

        self.failUnless(len(l) > 1)
        self.failUnless(l[0][0] is st)
        self.failUnlessIsInstance(l[0][1], CFArrayRef)
        self.failUnless(l[0][2] is info)
        








    def testContants(self):
        self.failUnless( isinstance(kSCDynamicStoreUseSessionKeys, unicode) )


if __name__ == "__main__":
    main()
