# Place holder for real tests.
from PyObjCTools.TestSupport import *
import objc

from Foundation import NSLocalizedString, NSAutoreleasePool, NSLocalizedStringFromTable, NSLocalizedStringFromTableInBundle, NSLocalizedStringWithDefaultValue, NSBundle

class TestNSLocalizedString(TestCase):
    def testBasic(self):
        # This is mostly a regression tests, the function used to crash on
        # this...
        if objc.platform != 'MACOSX':
            return

        pool = NSAutoreleasePool.alloc().init()
        s = NSLocalizedString(b"hello world".decode('ascii'), b"".decode('ascii'))
        del pool
        self.assertEqual (s, b"hello world".decode('ascii'))
        # XXX : Since we get the same object back, it's still unicode
        #self.assertEqual (s.nsstring().description(), b"hello world".decode('ascii'))


        pool = NSAutoreleasePool.alloc().init()
        s = NSLocalizedStringFromTable(b"hello world".decode('ascii'), b"tab".decode('utf-8'), b"".decode('ascii'))
        del pool
        self.assertEqual (s, b"hello world".decode('ascii'))

        pool = NSAutoreleasePool.alloc().init()
        s = NSLocalizedStringFromTableInBundle(b"hello world".decode('ascii'), b"tab".decode('utf-8'), NSBundle.mainBundle(), b"".decode('ascii'))
        del pool
        self.assertEqual (s, b"hello world".decode('ascii'))

        pool = NSAutoreleasePool.alloc().init()
        s = NSLocalizedStringWithDefaultValue(b"hello world".decode('ascii'), b"tab".decode('utf-8'), NSBundle.mainBundle(), b"default".decode('utf-8'), b"".decode('ascii'))
        del pool
        self.assertEqual (s, b"default".decode('ascii'))

if __name__ == '__main__':
    main( )
