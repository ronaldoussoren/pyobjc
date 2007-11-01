import unittest
from CoreFoundation import *

class TestCFNumber (unittest.TestCase):
    def testCFNumberGetValue(self):
        number = 42

        ok, v = CFNumberGetValue(number, kCFNumberSInt8Type);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt16Type);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt32Type);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt64Type);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberCharType);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberShortType);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberIntType);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberLongType);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberLongLongType);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberCFIndexType);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberFloat32Type)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberFloat64Type)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberFloatType)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberDoubleType)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberMaxType+2)
        self.assert_(not ok)

if __name__ == "__main__":
    unittest.main()
