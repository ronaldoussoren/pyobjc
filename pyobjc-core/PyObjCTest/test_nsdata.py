from PyObjCTools.TestSupport import *
import objc
import sys

class TestNSDataSupport (TestCase):
    # XXX: migrate test cases from Cocoa bindings!
    def testEmptyRoBuffer(self):
        cls = objc.lookUpClass('NSData')
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)

        if sys.version_info[0] == 3:
            self.assertEqual(buf.bytes(), b"")
        elif sys.version_info[:2] == (2, 7):
            self.assertEqual(buf.bytes(), memoryview(b""))
        else:
            self.assertEqual(buf.bytes(), bytes(b""))

        if sys.version_info[0] == 2:
            buf = cls.dataWithData_(buffer(b"hello"))
        else:
            buf = cls.dataWithData_(b"hello")
        self.assertIsInstance(buf, cls)
        self.assertEqual(buf[0:1], b"h")
        self.assertEqual(buf[0:2], b"he")




    def testEmptyRwBuffer(self):
        cls = objc.lookUpClass('NSMutableData')
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)

        if sys.version_info[0] == 2:
            buf = cls.dataWithData_(buffer(b"hello"))
        else:
            buf = cls.dataWithData_(b"hello")
        self.assertIsInstance(buf, cls)

        if sys.version_info[0] == 2:
            self.assertEqual(buf[0], "h")
        else:
            self.assertEqual(buf[0], ord("h"))

        if sys.version_info[0] == 2:
            buf[0] = "H"
        else:
            buf[0] = ord("H")
        if sys.version_info[0] == 2:
            self.assertEqual(buf[0], "H")
        else:
            self.assertEqual(buf[0], ord("H"))

        if sys.version_info[0] == 3:
            self.assertEqual(buf.bytes(), b"Hello")
        elif sys.version_info[:2] == (2, 7):
            self.assertEqual(buf.bytes(), memoryview(b"Hello"))
        else:
            self.assertEqual(buf.bytes(), bytes(b"Hello"))

        self.assertEqual(buf[0:2], b"He")
        buf[0:2] = b"hE"
        self.assertEqual(buf[0:2], b"hE")


if __name__ == "__main__":
    main()
