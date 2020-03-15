# Place holder for real tests.
import objc
import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSLocalizedString(TestCase):
    def testBasic(self):
        # This is mostly a regression tests, the function used to crash on
        # this...
        if objc.platform != "MACOSX":
            return

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedString(
            b"hello world".decode("ascii"), b"".decode("ascii")
        )
        del pool
        self.assertEqual(s, b"hello world".decode("ascii"))
        # XXX : Since we get the same object back, it's still str
        # self.assertEqual (s.nsstring().description(), b"hello world".decode('ascii'))

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringFromTable(
            b"hello world".decode("ascii"), b"tab".decode("utf-8"), b"".decode("ascii")
        )
        del pool
        self.assertEqual(s, b"hello world".decode("ascii"))

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringFromTableInBundle(
            b"hello world".decode("ascii"),
            b"tab".decode("utf-8"),
            Foundation.NSBundle.mainBundle(),
            b"".decode("ascii"),
        )
        del pool
        self.assertEqual(s, b"hello world".decode("ascii"))

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringWithDefaultValue(
            b"hello world".decode("ascii"),
            b"tab".decode("utf-8"),
            Foundation.NSBundle.mainBundle(),
            b"default".decode("utf-8"),
            b"".decode("ascii"),
        )
        del pool
        self.assertEqual(s, b"default".decode("ascii"))
