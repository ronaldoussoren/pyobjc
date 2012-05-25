from PyObjCTools.TestSupport import *
import AppKit

class TestNSBitmapImageRep (TestCase):

    def test_getTIFFCompressionTypes(self):
        r = AppKit.NSBitmapImageRep.getTIFFCompressionTypes_count_(None, None)

        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)

        lst, ln = r

        self.assertIsInstance(lst, tuple)
        self.assertIsInstance(ln, int)

        self.assertEqual(len(lst), ln)
        self.assertTrue(all(isinstance(x, int) for x in lst))

if __name__ == "__main__":
    main()
