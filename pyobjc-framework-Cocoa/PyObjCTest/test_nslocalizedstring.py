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
        s = Foundation.NSLocalizedString("hello world", "")
        del pool
        self.assertEqual(s, "hello world")
        # XXX : Since we get the same object back, it's still str
        # self.assertEqual (s.nsstring().description(), b"hello world".decode('ascii'))

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringFromTable(
            "hello world", "tab".decode("utf-8"), ""
        )
        del pool
        self.assertEqual(s, "hello world")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringFromTableInBundle(
            "hello world", "tab".decode("utf-8"), Foundation.NSBundle.mainBundle(), ""
        )
        del pool
        self.assertEqual(s, "hello world")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringWithDefaultValue(
            "hello world",
            "tab".decode("utf-8"),
            Foundation.NSBundle.mainBundle(),
            "default".decode("utf-8"),
            "",
        )
        del pool
        self.assertEqual(s, "default")
