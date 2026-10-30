import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSBitmapImageRep(TestCase):
    def test_gettiffcompressiontypes(self):
        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            AppKit.NSBitmapImageRep.getTIFFCompressionTypes_count_()

        with self.assertRaisesRegex(ValueError, "buffer must be None"):
            AppKit.NSBitmapImageRep.getTIFFCompressionTypes_count_(42, None)

        with self.assertRaisesRegex(ValueError, "length must be None"):
            AppKit.NSBitmapImageRep.getTIFFCompressionTypes_count_(None, 42)

        r = AppKit.NSBitmapImageRep.getTIFFCompressionTypes_count_(None, None)

        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)

        ln, lst = r

        self.assertIsInstance(lst, tuple)
        self.assertIsInstance(ln, int)

        self.assertEqual(len(lst), ln)
        self.assertTrue(all(isinstance(x, int) for x in lst))
