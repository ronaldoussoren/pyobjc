import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSCache(TestCase):
    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSCache.evictsObjectsWithDiscardedContent)
        self.assertArgIsBOOL(Foundation.NSCache.setEvictsObjectsWithDiscardedContent_, 0)

    @min_sdk_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("NSCacheDelegate")

    def testConvenience(self):
        key = "key"
        value = Foundation.NSObject.alloc().init()
        c = Foundation.NSCache.alloc().init()
        c.setCountLimit_(1000)
        c.setObject_forKey_(value, key)
        self.assertEqual(c.objectForKey_(key), value)
        self.assertEqual(c.objectForKey_(key), value)

        self.assertEqual(c["key"], value)
        c["key"] = 21
        self.assertEqual(c["key"], 21)
        self.assertEqual(c.objectForKey_("key"), 21)

        self.assertEqual(c.get("key"), 21)
        self.assertEqual(c.get("key2"), None)

        c.clear()
        self.assertEqual(c.get("key"), None)

        with self.assertRaises(KeyError):
            c["key"]

        c["key"] = 1
        c["key2"] = 2

        self.assertEqual(c["key"], 1)
        self.assertEqual(c["key2"], 2)

        del c["key"]
        with self.assertRaises(KeyError):
            c["key"]
        self.assertEqual(c["key2"], 2)

        c["key"] = None
        self.assertEqual(c["key"], None)
        self.assertEqual(c.get("key"), None)
