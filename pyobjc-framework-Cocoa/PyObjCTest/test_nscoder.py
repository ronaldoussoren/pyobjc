import Foundation
from PyObjCTest.testhelper import PyObjC_TestClass4
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSCoderUsage(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSDecodingFailurePolicy)

    def testUsage(self):
        class CoderClass1(Foundation.NSObject):
            def encodeWithCoder_(self, coder):
                # Foundation.NSObject does not implement Foundation.NSCoding, no need to
                # call superclass implementation:
                #    super(CoderClass1, self).encodeWithCoder_(coder)
                coder.encodeValueOfObjCType_at_(objc._C_INT, 2)
                coder.encodeValueOfObjCType_at_(objc._C_DBL, 2.0)
                coder.encodeArrayOfObjCType_count_at_(
                    objc._C_DBL, 4, (1.0, 2.0, 3.0, 4.0)
                )
                coder.encodeBytes_length_(b"hello world!", 5)

            def initWithCoder_(self, coder):
                # Foundation.NSObject does not implement Foundation.NSCoding, no need to
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
        data = Foundation.NSMutableData.data()
        archiver = Foundation.NSArchiver.alloc().initForWritingWithMutableData_(data)
        archiver.encodeObject_(origObj)

        archiver = Foundation.NSUnarchiver.alloc().initForReadingWithData_(data)
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


class MyCoder(Foundation.NSCoder):
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

    def decodeValueOfObjCType_at_(self, tp, value):
        if tp == b"i":
            return 42
        elif tp == b"d":
            return 1.5

    def decodeArrayOfObjCType_count_at_(self, tp, cnt, value):
        return range(cnt)

    def decodeBytesWithReturnedLength_(self, length):
        return (b"ABCDEabcde", 10)


class TestPythonCoder(TestCase):
    #
    # This test accesses a Foundation.NSCoder implemented in Python from Objective-C
    #
    # The tests only use those methods that require a custom IMP-stub.
    #
    def testEncoding(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestClass4.alloc().init()
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
        o = PyObjC_TestClass4

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

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSCoder.allowsKeyedCoding)
        self.assertArgIsBOOL(Foundation.NSCoder.encodeBool_forKey_, 0)
        self.assertResultIsBOOL(Foundation.NSCoder.containsValueForKey_)
        self.assertResultIsBOOL(Foundation.NSCoder.decodeBoolForKey_)

        self.assertResultHasType(
            Foundation.NSCoder.decodeBytesForKey_returnedLength_, b"^v"
        )
        self.assertResultSizeInArg(
            Foundation.NSCoder.decodeBytesForKey_returnedLength_, 1
        )
        self.assertArgIsOut(Foundation.NSCoder.decodeBytesForKey_returnedLength_, 1)

        self.assertTrue(hasattr(Foundation, "NXReadNSObjectFromCoder"))

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(Foundation.NSCoder.requiresSecureCoding)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsOut(Foundation.NSCoder.decodeTopLevelObjectAndReturnError_, 0)
        self.assertArgIsOut(
            Foundation.NSCoder.decodeTopLevelObjectOfClass_forKey_error_, 2
        )

    @min_os_level("15.4")
    def testMethods15_4(self):
        self.assertResultSizeInArg(Foundation.NSCoder.decodeBytesWithMinimumLength_, 0)
        self.assertResultSizeInArg(
            Foundation.NSCoder.decodeBytesForKey_minimumLength_, 1
        )

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(Foundation.NSDecodingFailurePolicyRaiseException, 0)
        self.assertEqual(Foundation.NSDecodingFailurePolicySetErrorAndReturn, 1)
