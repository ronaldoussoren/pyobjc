import unittest
import objc

from Foundation import *


class TestNSCoderUsage(unittest.TestCase):
    if not hasattr(unittest.TestCase, 'assertAlmostEquals'):
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

            def initWithCoder_(self, coder):
                # NSObject does not implement NSCoding, no need to
                # call superclass implementation:
                #    self = super(CodeClass1, self).initWithCoder_(coder)
                self = self.init()
                self.intVal = coder.decodeValueOfObjCType_at_(objc._C_INT)
                self.dblVal = coder.decodeValueOfObjCType_at_(objc._C_DBL)
                self.dblArray = coder.decodeArrayOfObjCType_count_at_(objc._C_DBL, 4)
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

if __name__ == '__main__':
    unittest.main( )
