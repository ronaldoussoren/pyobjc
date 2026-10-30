import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSLocalizedString(TestCase):
    def test_basic(self):
        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedString("hello world", "")
        del pool
        self.assertEqual(s, "hello world")
        # XXX : Since we get the same object back, it's still str
        # self.assertEqual (s.nsstring().description(), "hello world")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringFromTable("hello world", "tab", "")
        del pool
        self.assertEqual(s, "hello world")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringFromTableInBundle(
            "hello world", "tab", Foundation.NSBundle.mainBundle(), ""
        )
        del pool
        self.assertEqual(s, "hello world")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedStringWithDefaultValue(
            "hello world", "tab", Foundation.NSBundle.mainBundle(), "default", ""
        )
        del pool
        self.assertEqual(s, "default")

    @min_os_level("12.0")
    def test_basic_attributed(self):
        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedAttributedString("hello world", "value")
        del pool
        self.assertIsInstance(s, Foundation.NSAttributedString)
        self.assertEqual(s.string(), "hello world")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedAttributedStringFromTable(
            "hello world", "value", "tab"
        )
        del pool
        self.assertIsInstance(s, Foundation.NSAttributedString)
        self.assertEqual(s.string(), "hello world")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedAttributedStringWithDefaultValue(
            "hello world", "tab", Foundation.NSBundle.mainBundle(), "value", "comment"
        )
        del pool
        self.assertIsInstance(s, Foundation.NSAttributedString)
        self.assertEqual(s.string(), "value")

        pool = Foundation.NSAutoreleasePool.alloc().init()
        s = Foundation.NSLocalizedAttributedStringFromTableInBundle(
            "hello world", "value", Foundation.NSBundle.mainBundle(), "tab"
        )
        del pool
        self.assertIsInstance(s, Foundation.NSAttributedString)
        self.assertEqual(s.string(), "hello world")
