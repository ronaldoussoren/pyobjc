import unittest
from Foundation import *

class TestNSDecimal (unittest.TestCase):
    def testCreation(self):
        o = NSDecimal("1.25")
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), "1.25")

        o = NSDecimal(12345, -2, True)
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), "-123.45")

        o = NSDecimal()
        self.assert_(isinstance(o, NSDecimal))
        self.assert_(str(o) in ("0", "0.0"))

        o = NSDecimal(1234)
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), "1234")

        o = NSDecimal(-1234)
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), "-1234")

        o = NSDecimal(long(1234))
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), "1234")

        o = NSDecimal(long(-1234))
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), "-1234")

        o = NSDecimal(1L << 64 - 1)

        self.assertRaises(TypeError, NSDecimal, 1.2)
        self.assertRaises(OverflowError, NSDecimal, 1L << 128)
        self.assertRaises(OverflowError, NSDecimal, -1L << 128)

    def testFunction(self):
        # We only test addition, as all function wrappers are generated this 
        # should be enough to verify that the machinery is working correctly.
        o = NSDecimal("1.5")
        p = NSDecimal(12345, -2, True)
        r = NSDecimal("-121.95")
        q = NSDecimal()

        NSDecimalAdd(q, o, p, NSRoundPlain)

        self.assertEquals(str(q), str(r))

    def testCompare(self):
        small = NSDecimal("1")
        small2 = NSDecimal("1")
        large = NSDecimal("42")

        self.assert_(small == small2)
        self.assert_(not (small == large))
        self.assert_(not (small != small2))
        self.assert_(small < large)
        self.assert_(not(large < small))
        self.assert_(not(small < small))
        self.assert_(small <= large)
        self.assert_(small <= small)
        self.assert_(not(large <= small))
        self.assert_(large > small)
        self.assert_(not(small > large))
        self.assert_(not(large > large))
        self.assert_(large >= small)
        self.assert_(large >= large)
        self.assert_(not(small >= large))

    def testConversion(self):
        o = NSDecimal("1234.44")
        self.assertEquals(o.as_int(), 1234)

        o = NSDecimal("1.5")
        self.assertEquals(o.as_float(), 1.5)

        self.assertRaises(TypeError, int, o)
        self.assertRaises(TypeError, float, o)

class TestNSDecimalNumber (unittest.TestCase):
    def testCreation1(self):
        o = NSDecimalNumber.decimalNumberWithString_("1.1234")
        self.assertEquals(o.description(), "1.1234")

        p = o.decimalValue()
        self.assert_(isinstance(p, NSDecimal))
        self.assertEquals(str(p), "1.1234")

    def testCreation2(self):
        p = NSDecimal("1.1234")
        o = NSDecimalNumber.decimalNumberWithDecimal_(p)
        self.assertEquals(o.description(), "1.1234")

    def testCreation3(self):
        p = NSDecimal("1.1234")
        o = NSDecimalNumber.alloc().initWithDecimal_(p)
        self.assertEquals(o.description(), "1.1234")

if __name__ == "__main__":
    unittest.main()
