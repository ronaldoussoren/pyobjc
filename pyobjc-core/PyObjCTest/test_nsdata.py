import objc
from PyObjCTools.TestSupport import TestCase


class TestNSDataSupport(TestCase):
    # XXX: migrate test cases from Cocoa bindings!
    def testEmptyRoBuffer(self):
        cls = objc.lookUpClass("NSData")
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)

        self.assertEqual(buf.bytes(), b"")

        buf = cls.dataWithData_(b"hello")
        self.assertIsInstance(buf, cls)
        self.assertEqual(buf[0:1], b"h")
        self.assertEqual(buf[0:2], b"he")

    def testEmptyRwBuffer(self):
        cls = objc.lookUpClass("NSMutableData")
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)

        buf = cls.dataWithData_(b"hello")
        self.assertIsInstance(buf, cls)

        self.assertEqual(buf[0], ord("h"))

        buf[0] = ord("H")
        self.assertEqual(buf[0], ord("H"))

        self.assertEqual(buf.bytes(), b"Hello")

        self.assertEqual(buf[0:2], b"He")
        buf[0:2] = b"hE"
        self.assertEqual(buf[0:2], b"hE")
