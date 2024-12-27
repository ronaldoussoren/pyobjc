from PyObjCTest.coding import PyObjC_TestCodingClass
from PyObjCTools.TestSupport import TestCase
import objc

NSObject = objc.lookUpClass("NSObject")
NSMutableData = objc.lookUpClass("NSMutableData")
NSArchiver = objc.lookUpClass("NSArchiver")
NSUnarchiver = objc.lookUpClass("NSUnarchiver")
NSCoder = objc.lookUpClass("NSCoder")


class TestNSCoderUsage(TestCase):
    def testUsage(self):
        class CoderClass1(NSObject):
            def encodeWithCoder_(self, coder):
                # NSObject does not implement NSCoding, no need to
                # call superclass implementation:
                #    super(CoderClass1, self).encodeWithCoder_(coder)
                coder.encodeValueOfObjCType_at_(objc._C_INT, 2)
                coder.encodeValueOfObjCType_at_(objc._C_DBL, 2.0)
                coder.encodeArrayOfObjCType_count_at_(
                    objc._C_DBL, 4, (1.0, 2.0, 3.0, 4.0)
                )
                coder.encodeBytes_length_(b"hello world!", 5)

                try:
                    coder.encodeValueOfObjCType_at_(objc._C_INT, "foo")
                except ValueError as exc:
                    if "depythonify" not in str(exc):
                        raise
                else:
                    raise AssertionError("Invalid argument type didn't raise")

                try:
                    coder.encodeValueOfObjCType_at_(objc._C_INT, 2, 3)
                except TypeError as exc:
                    if "expected 2 arguments, got 3" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too many arguments didn't raise")

                try:
                    coder.encodeValueOfObjCType_at_(objc._C_INT)
                except TypeError as exc:
                    if "expected 2 arguments, got 1" not in str(exc):
                        raise
                else:
                    raise AssertionError("Too few arguments didn't raise")

                try:
                    coder.encodeValueOfObjCType_at_("i", 2)
                except TypeError as exc:
                    if "a bytes-like object is required, not 'str'" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

                try:
                    coder.encodeValueOfObjCType_at_(b"X", 2)
                except objc.error as exc:
                    if "type encoding is not valid" not in str(exc):
                        raise
                else:
                    raise AssertionError("Bad encoding type")

            def initWithCoder_(self, coder):
                # NSObject does not implement NSCoding, no need to
                # call superclass implementation:
                #    self = super(CodeClass1, self).initWithCoder_(coder)
                self = self.init()
                self.intVal = coder.decodeValueOfObjCType_at_(objc._C_INT, None)
                self.dblVal = coder.decodeValueOfObjCType_at_(objc._C_DBL, None)
                self.dblArray = coder.decodeArrayOfObjCType_count_at_(
                    objc._C_DBL, 4, None
                )
                self.decodedBytes = coder.decodeBytesWithReturnedLength_(None)
                return self

        origObj = CoderClass1.alloc().init()
        data = NSMutableData.data()
        archiver = NSArchiver.alloc().initForWritingWithMutableData_(data)
        archiver.encodeObject_(origObj)

        archiver = NSUnarchiver.alloc().initForReadingWithData_(data)
        newObj = archiver.decodeObject()

        self.assertEqual(newObj.intVal, 2)
        self.assertAlmostEqual(newObj.dblVal, 2.0)
        self.assertEqual(len(newObj.dblArray), 4)
        self.assertAlmostEqual(newObj.dblArray[0], 1.0)
        self.assertAlmostEqual(newObj.dblArray[1], 2.0)
        self.assertAlmostEqual(newObj.dblArray[2], 3.0)
        self.assertAlmostEqual(newObj.dblArray[3], 4.0)
        self.assertEqual(newObj.decodedBytes[0], b"hello")
        self.assertEqual(newObj.decodedBytes[1], 5)


class MyCoder(NSCoder):
    def init(self):
        self = objc.super(MyCoder, self).init()
        if self is None:
            return None
        self.coded = []
        return self

    def encodeValueOfObjCType_at_(self, tp, value):
        self.coded.append(("value", tp, value))

    def encodeArrayOfObjCType_count_at_(self, tp, cnt, value):
        self.coded.append(("array", tp, cnt, value))

    def encodeBytes_length_(self, value, length):
        self.coded.append(("bytes", value, length))

    def decodeValueOfObjCType_at_(self, tp, at):
        if tp == b"i":
            return 42
        elif tp == b"d":
            return 1.5

    def decodeArrayOfObjCType_count_at_(self, tp, cnt, at):
        return range(cnt)

    def decodeBytesWithReturnedLength_(self, value):
        return (b"ABCDEabcde", 10)


class TestPythonCoder(TestCase):
    #
    # This test accesses a NSCoder implemented in Python from Objective-C
    #
    # The tests only use those methods that require a custom IMP-stub.
    #
    def testEncoding(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestCodingClass.alloc().init()
        o.encodeWithCoder_(coder)
        self.assertEqual(
            coder.coded,
            [
                ("value", b"d", 1.5),
                ("array", b"i", 4, (3, 4, 5, 6)),
                ("bytes", b"hello world", 11),
            ],
        )

    def testDecoding(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestCodingClass

        self.assertEqual(o.fetchInt_(coder), 42)
        self.assertEqual(o.fetchDouble_(coder), 1.5)

        d = o.fetchData_(coder)
        self.assertEqual(d.length(), 10)

        b = d.bytes()
        if isinstance(b, memoryview):
            self.assertEqual(b.tobytes(), b"ABCDEabcde")
        else:
            self.assertEqual(bytes(b), b"ABCDEabcde")

        d = o.fetchArray_(coder)
        self.assertEqual(tuple(range(10)), tuple(d))
