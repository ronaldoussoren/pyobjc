from PyObjCTools.TestSupport import *

from SystemConfiguration import *
import SystemConfiguration
import os

class TestSCDynamicStore (TestCase):
    def testTypes(self):
        self.assertTrue(isinstance(SCDynamicStoreRef, objc.objc_class))

    def testStructs(self):
        self.assertFalse( hasattr(SystemConfiguration, 'SCDynamicStoreContext') )

    def testFunctions(self):
        print 1
        n = SCDynamicStoreGetTypeID()
        print 2
        self.assertTrue(isinstance(n, (int, long)))
        print 3


        l = []
        info = object()
        def callback(store, changedKeys, info):
            print "CALLBACK"
            l.append((store, changedKeys, info))

        print 4
        st = SCDynamicStoreCreate(None, 
                "pyobjc.test", 
                callback, info)
        self.assertTrue(isinstance(st, SCDynamicStoreRef))
        print 5
        
        st = SCDynamicStoreCreateWithOptions(None,
                "pyobjc.test",
                {},
                callback,
                info)
        self.assertTrue(isinstance(st, SCDynamicStoreRef))
        print 6
        print st


        src = SCDynamicStoreCreateRunLoopSource(None, st, 0)
        print 6, 2
        self.assertTrue(isinstance(src, CFRunLoopSourceRef))
        print 6, 3
        del src
        print 7

        v = SCDynamicStoreCopyKeyList(st, u'.*')
        self.assertTrue(isinstance(v, CFArrayRef))
        self.assertTrue(len(v) > 0)
        self.assertTrue(isinstance(v[0], unicode))
        print 8

        r = SCDynamicStoreAddValue(st, "Setup:/PyObjC", { u"key":42 })
        self.assertTrue(r is True or r is False)

        r = SCDynamicStoreAddTemporaryValue(st, "Setup:/PyObjC", { u"key":42 })
        self.assertTrue(r is True or r is False)

        v = SCDynamicStoreCopyValue(st, "Setup:/")
        self.assertTrue(isinstance(v, CFDictionaryRef))

        v = SCDynamicStoreCopyMultiple(st, None, ['.*'])
        self.assertTrue(isinstance(v, CFDictionaryRef))

        r = SCDynamicStoreSetValue(st, "Setup:/PyObjC", { u"key":42 })
        self.assertTrue(r is True or r is False)

        r = SCDynamicStoreSetMultiple(st, 
                {
                    'Setup:/PyObjC2': { u"key": 42},
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
                u"pyobjc.test", 
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
