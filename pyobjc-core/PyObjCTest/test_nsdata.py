import objc
from objc import super
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.helpernsdata import OC_MutableDataHelper


class TestNSDataSupport(TestCase):
    # XXX: migrate test cases from Cocoa bindings!
    def testyRoBuffer(self):
        cls = objc.lookUpClass("NSData")
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)

        self.assertEqual(buf.bytes(), b"")
        self.assertIsInstance(buf.bytes(), bytes)

        buf = cls.dataWithData_(b"hello")
        self.assertIsInstance(buf, cls)
        self.assertEqual(buf[0:1], b"h")
        self.assertEqual(buf[0:2], b"he")

        self.assertEqual(buf.bytes(), b"hello")
        self.assertIsInstance(buf.bytes(), memoryview)

        with self.assertRaises(TypeError):
            buf.bytes(1)

        view = memoryview(buf)
        self.assertEqual(bytes(view), buf.bytes())
        self.assertTrue(view.readonly)

    def testyRwBuffer(self):
        cls = objc.lookUpClass("NSMutableData")
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)
        self.assertIsInstance(buf.mutableBytes(), memoryview)

        buf = cls.dataWithData_(b"hello")
        self.assertIsInstance(buf, cls)

        self.assertEqual(buf[0], ord("h"))

        buf[0] = ord("H")
        self.assertEqual(buf[0], ord("H"))

        self.assertEqual(buf.bytes(), b"Hello")
        self.assertIsInstance(buf.bytes(), memoryview)

        self.assertEqual(buf[0:2], b"He")
        buf[0:2] = b"hE"
        self.assertEqual(buf[0:2], b"hE")

        with self.assertRaises(TypeError):
            buf.bytes(1)

        with self.assertRaises(TypeError):
            buf.mutableBytes(1)

        vw = buf.mutableBytes()
        self.assertIsInstance(vw, memoryview)
        vw[0:1] = b"Y"
        self.assertEqual(buf.bytes(), b"YEllo")

        view = memoryview(buf)
        self.assertEqual(bytes(view), buf.bytes())
        self.assertFalse(view.readonly)

    def testNullHandling(self):
        nullBuffer = OC_MutableDataHelper.alloc().initWithScenario_(0)
        self.assertEqual(nullBuffer.bytes(), b"")
        self.assertIsInstance(nullBuffer.bytes(), bytes)

        self.assertEqual(nullBuffer.mutableBytes(), b"")
        self.assertIsInstance(nullBuffer.mutableBytes(), memoryview)

    def testExceptions(self):
        raisingBuffer = OC_MutableDataHelper.alloc().initWithScenario_(1)

        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            raisingBuffer.bytes()

        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            raisingBuffer.mutableBytes()


class DataSubClass(objc.lookUpClass("NSData")):
    def init(self):
        self = super().init()
        self._value = b"hello world"
        return self

    def length(self):
        if self._value is None:
            return 0
        return len(self._value)

    def bytes(self):  # noqa: A003
        return self._value


class MutableDataSubClass(objc.lookUpClass("NSMutableData")):
    def init(self):
        self = super().init()
        self._value = bytearray(b"hello world")
        return self

    def length(self):
        if self._value is None:
            return 0
        return len(self._value)

    def bytes(self):  # noqa: A003
        return self._value

    def mutableBytes(self):
        return self._value


class TestSubclassing(TestCase):
    def testNSData(self):
        buf = DataSubClass.alloc().init()

        self.assertEqual(objc.lookUpClass("NSData").dataWithData_(buf), b"hello world")

        buf._value = None
        b = OC_MutableDataHelper.fetchBytesOf_(buf)
        self.assertIs(b, None)

        buf._value = 42
        with self.assertRaises(TypeError):
            OC_MutableDataHelper.fetchBytesOf_(buf)

    def testNSMutableData(self):
        buf = MutableDataSubClass.alloc().init()

        self.assertEqual(objc.lookUpClass("NSData").dataWithData_(buf), b"hello world")

        b = OC_MutableDataHelper.fetchMutableBytesOf_(buf)
        self.assertEqual(b, b"hello world")
        self.assertIsInstance(b, objc.lookUpClass("NSData"))

        buf._value = None
        b = OC_MutableDataHelper.fetchMutableBytesOf_(buf)
        self.assertIs(b, None)

        b = OC_MutableDataHelper.fetchBytesOf_(buf)
        self.assertIs(b, None)

        buf._value = 42
        with self.assertRaises(TypeError):
            OC_MutableDataHelper.fetchBytesOf_(buf)

        with self.assertRaises(TypeError):
            OC_MutableDataHelper.fetchMutableBytesOf_(buf)

    def testCopyRO(self):
        orig = DataSubClass.alloc().init()
        copy = orig.copy()
        self.assertEqual(copy.bytes(), orig.bytes())
        self.assertIsInstance(copy, objc.lookUpClass("NSData"))

    def testCopyRW(self):
        orig = MutableDataSubClass.alloc().init()
        copy = orig.copy()
        self.assertEqual(copy.bytes(), orig.bytes())
        self.assertIsInstance(copy, objc.lookUpClass("NSData"))

        copy = orig.mutableCopy()
        self.assertEqual(copy.bytes(), orig.bytes())
        self.assertIsInstance(copy, objc.lookUpClass("NSMutableData"))
