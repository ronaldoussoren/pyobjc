import unittest
import objc

from Foundation import *
from objc.test.testbndl import PyObjC_TestClass4

class TestNSCoderUsage(unittest.TestCase):
    if not hasattr(unittest.TestCase, 'assertAlmostEquals'):
        # XXX Move to a PyObjC unittest module?
        def assertAlmostEquals(self, val1, val2):
            self.assert_ (abs(val1 - val2) <  0.000001)

    def testUsage(self):
        class CoderClass1 (NSObject):
            def encodeWithCoder_(self, coder):
                # NSObject does not implement NSCoding, no need to
                # call superclass implementation:
                #    super(CoderClass1, self).encodeWithCoder_(coder)
                coder.encodeValueOfObjCType_at_(objc._C_INT, 2)
                coder.encodeValueOfObjCType_at_(objc._C_DBL, 2.0)
                coder.encodeArrayOfObjCType_count_at_(objc._C_DBL, 4, (1.0, 2.0, 3.0, 4.0))
                coder.encodeBytes_length_("hello world!", 5)

            def initWithCoder_(self, coder):
                # NSObject does not implement NSCoding, no need to
                # call superclass implementation:
                #    self = super(CodeClass1, self).initWithCoder_(coder)
                self = self.init()
                self.intVal = coder.decodeValueOfObjCType_at_(objc._C_INT)
                self.dblVal = coder.decodeValueOfObjCType_at_(objc._C_DBL)
                self.dblArray = coder.decodeArrayOfObjCType_count_at_(objc._C_DBL, 4)
                self.decodedBytes = coder.decodeBytesWithReturnedLength_()
                return self

        origObj = CoderClass1.alloc().init()
        data = NSMutableData.data()
        archiver = NSArchiver.alloc().initForWritingWithMutableData_(data)
        archiver.encodeObject_(origObj)

        archiver = NSUnarchiver.alloc().initForReadingWithData_(data)
        newObj = archiver.decodeObject()

        self.assertEquals(newObj.intVal, 2)
        self.assertAlmostEquals(newObj.dblVal, 2.0)
        self.assertEquals(len(newObj.dblArray), 4)
        self.assertAlmostEquals(newObj.dblArray[0], 1.0)
        self.assertAlmostEquals(newObj.dblArray[1], 2.0)
        self.assertAlmostEquals(newObj.dblArray[2], 3.0)
        self.assertAlmostEquals(newObj.dblArray[3], 4.0)
        self.assertEquals(newObj.decodedBytes[0], "hello")
        self.assertEquals(newObj.decodedBytes[1], 5)


class MyCoder (NSCoder):
    def init(self):
        self = super(MyCoder, self).init()
        if self is None: return None
        self.coded = []
        return self

    def encodeValueOfObjCType_at_(self, tp, value):
        self.coded.append( ("value", tp, value) )

    def encodeArrayOfObjCType_count_at_(self, tp, cnt, value):
        self.coded.append( ("array", tp, cnt, value) )

    def encodeBytes_length_(self, bytes, length):
        self.coded.append( ("bytes", bytes, length) )

    def decodeValueOfObjCType_at_(self, tp):
        if tp == 'i':
            return 42
        elif tp == 'd':
            return 1.5

    def decodeArrayOfObjCType_count_at_(self, tp, cnt):
        return range(cnt)

    def decodeBytesWithReturnedLength_(self):
        return ("ABCDEabcde", 10)

class TestPythonCoder(unittest.TestCase):
    #
    # This test accesses a NSCoder implemented in Python from Objective-C
    #
    # The tests only use those methods that require a custom IMP-stub.
    #
    def testEncoding(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestClass4.alloc().init()
        o.encodeWithCoder_(coder)
        self.assertEquals(coder.coded,
                [
                    ("value", "d", 1.5),
                    ("array", "i", 4, (3,4,5,6)),
                    ("bytes", "hello world", 11),
                ])

    def testDecoding(self):
        coder = MyCoder.alloc().init()
        o = PyObjC_TestClass4

        self.assertEquals(o.fetchInt_(coder), 42)
        self.assertEquals(o.fetchDouble_(coder), 1.5)

        d = o.fetchData_(coder)
        self.assertEquals(d.length(), 10)
        self.assertEquals(str(d.bytes()), "ABCDEabcde")

        d = o.fetchArray_(coder)
        self.assertEquals(tuple(range(10)), tuple(d))

if __name__ == '__main__':
    unittest.main( )
