from PyObjCTools.TestSupport import *
import AppKit

class TestNSBitmapImageRep (TestCase):

    def test_getTIFFCompressionTypes(self):
        r = AppKit.NSBitmapImageRep.getTIFFCompressionTypes_count_(None, None)

        self.assert_(isinstance(r, tuple))
        self.assertEqual(len(r), 2)

        lst, ln = r

        self.assert_(isinstance(lst, tuple))
        self.assert_(isinstance(ln, int))

        self.assertEqual(len(lst), ln)
        self.assert_(reduce(lambda x, y: x and isinstance(x, int), lst, True))

if __name__ == "__main__":
    main()
