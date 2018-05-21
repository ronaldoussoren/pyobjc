from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSCache (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(NSCache.evictsObjectsWithDiscardedContent)
        self.assertArgIsBOOL(NSCache.setEvictsObjectsWithDiscardedContent_,0)

    @min_sdk_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('NSCacheDelegate')

    def testConvenience(self):
        c = NSCache.alloc().init()
        c.setObject_forKey_(42, 'key')
        self.assertEqual(c.objectForKey_('key'), 42)
        self.assertEqual(c.objectForKey_('key'), 42)

        self.assertEqual(c['key'], 42)
        c['key'] = 21
        self.assertEqual(c['key'], 21)
        self.assertEqual(c.objectForKey_('key'), 21)

        self.assertEqual(c.get('key'), 21)
        self.assertEqual(c.get('key2'), None)

        c.clear()
        self.assertEqual(c.get('key'), None)

        with self.assertRaises(KeyError):
            c['key']

        c['key'] = 1
        c['key2'] = 2

        self.assertEqual(c['key'], 1)
        self.assertEqual(c['key2'], 2)

        del c['key']
        with self.assertRaises(KeyError):
            c['key']
        self.assertEqual(c['key2'], 2)

        c['key'] = None
        self.assertEqual(c['key'], None)
        self.assertEqual(c.get('key'), None)

if __name__ == "__main__":
    main()
