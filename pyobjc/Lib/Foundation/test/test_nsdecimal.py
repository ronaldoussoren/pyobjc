#
# Some tests for NSDecimal (C type) and NSDecimalNumber (Objective-C class)
#
import unittest
from Foundation import *
import operator
import objc

class TestNSDecimal (unittest.TestCase):
    def testCreation(self):
        o = NSDecimal(u"1.25")
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), u"1.25")

        o = NSDecimal(12345, -2, objc.YES)
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), u"-123.45")

        o = NSDecimal()
        self.assert_(isinstance(o, NSDecimal))
        self.assert_(str(o) in (u"0", u"0.0"))

        o = NSDecimal(1234)
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), u"1234")

        o = NSDecimal(-1234)
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), u"-1234")

        o = NSDecimal(long(1234))
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), u"1234")

        o = NSDecimal(long(-1234))
        self.assert_(isinstance(o, NSDecimal))
        self.assertEquals(str(o), u"-1234")

        o = NSDecimal(1L << 64 - 1)

        # This is wrong, explict conversion should be allowed!
        #self.assertRaises(TypeError, NSDecimal, 1.2)
        self.assertRaises(OverflowError, NSDecimal, 1L << 128)
        self.assertRaises(OverflowError, NSDecimal, -1L << 128)

    def testFunction(self):
        # We only test addition, as all function wrappers are generated this
        # should be enough to verify that the machinery is working correctly.
        o = NSDecimal(u"1.5")
        p = NSDecimal(12345, -2, objc.YES)
        r = NSDecimal(u"-121.95")
        q = NSDecimal()

        NSDecimalAdd(q, o, p, NSRoundPlain)

        self.assertEquals(str(q), str(r))

    def testCompare(self):
        small = NSDecimal(u"1")
        small2 = NSDecimal(u"1")
        large = NSDecimal(u"42")

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
        o = NSDecimal(u"1234.44")
        self.assertEquals(o.as_int(), 1234)

        o = NSDecimal(u"1.5")
        self.assertEquals(o.as_float(), 1.5)

        self.assertRaises(TypeError, int, o)
        self.assertRaises(TypeError, float, o)

    def testCreateFromFloat(self):
        o = NSDecimal(1.1)
        self.assertAlmostEquals(o.as_float(), 1.1)

    if not hasattr(unittest.TestCase, 'assertAlmostEquals'):
        def assertAlmostEquals(self, val1, val2, eta=0.000001):
            self.assert_(abs(val1 - val2) < eta)


class TestNSDecimalNumber (unittest.TestCase):
    def testCreation1(self):
        o = NSDecimalNumber.decimalNumberWithString_(u"1.1234")
        self.assertEquals(o.description(), u"1.1234")

        p = o.decimalValue()
        self.assert_(isinstance(p, NSDecimal))
        self.assertEquals(str(p), u"1.1234")

    def testCreation2(self):
        p = NSDecimal(u"1.1234")
        o = NSDecimalNumber.decimalNumberWithDecimal_(p)
        self.assertEquals(o.description(), u"1.1234")

    def testCreation3(self):
        p = NSDecimal(u"1.1234")
        o = NSDecimalNumber.alloc().initWithDecimal_(p)
        self.assertEquals(o.description(), u"1.1234")

class NSDecimalOperators (unittest.TestCase):
    def testAddition(self):
        r = NSDecimal()
        o = NSDecimal(1)
        p = NSDecimal(2)

        NSDecimalAdd(r, o, p, NSRoundPlain)
        self.assertEquals(o+p, r)
        self.assertEquals(o+2, r)
        self.assertEquals(o+2L, r)
        self.assertEquals(1+p, r)
        self.assertEquals(1+p, r)

        self.assertRaises(TypeError, operator.add, o, 1.2)
        self.assertRaises(TypeError, operator.add, 1.2, o)

    def testSubtraction(self):
        r = NSDecimal()
        o = NSDecimal(1)
        p = NSDecimal(2)

        NSDecimalSubtract(r, o, p, NSRoundPlain)
        self.assertEquals(o-p, r)
        self.assertEquals(o-2, r)
        self.assertEquals(o-2L, r)
        self.assertEquals(1-p, r)
        self.assertEquals(1-p, r)

        self.assertRaises(TypeError, operator.sub, o, 1.2)
        self.assertRaises(TypeError, operator.sub, 1.2, o)

    def testMultiplication(self):
        r = NSDecimal()
        o = NSDecimal(2)
        p = NSDecimal(3)

        NSDecimalMultiply(r, o, p, NSRoundPlain)
        self.assertEquals(o*p, r)
        self.assertEquals(o*3, r)
        self.assertEquals(o*3L, r)
        self.assertEquals(2*p, r)
        self.assertEquals(2*p, r)

        self.assertRaises(TypeError, operator.mul, o, 1.2)
        self.assertRaises(TypeError, operator.mul, 1.2, o)

    def testDivision(self):
        r = NSDecimal()
        o = NSDecimal(2)
        p = NSDecimal(3)

        NSDecimalDivide(r, o, p, NSRoundPlain)
        self.assertEquals(o/p, r)
        self.assertEquals(o/3, r)
        self.assertEquals(o/3L, r)
        self.assertEquals(2/p, r)
        self.assertEquals(2/p, r)

        self.assertRaises(TypeError, operator.div, o, 1.2)
        self.assertRaises(TypeError, operator.div, 1.2, o)

    def testPositive(self):
        o = NSDecimal(2)
        p = NSDecimal(-2)

        self.assertEquals(+o, o)
        self.assertEquals(+p, p)

    def testNegative(self):
        o = NSDecimal(2)
        p = NSDecimal(-2)

        self.assertEquals(-o, p)
        self.assertEquals(-p, o)

    def testAbs(self):
        o = NSDecimal(2)
        p = NSDecimal(-2)

        self.assertEquals(abs(o), o)
        self.assertEquals(abs(p), o)

    def testBitwise(self):
        o = NSDecimal(2)
        p = NSDecimal(3)

        self.assertRaises(TypeError, operator.and_, o, p)
        self.assertRaises(TypeError, operator.or_, o, p)
        self.assertRaises(TypeError, operator.not_, o, p)

    def testPow(self):
        o = NSDecimal(2)
        p = NSDecimal(3)

        self.assertRaises(TypeError, pow, o, p)
        self.assertRaises(TypeError, pow, o, 2)
        self.assertRaises(TypeError, pow, 2, o)

    def testDivMod(self):
        o = NSDecimal(2)
        p = NSDecimal(3)

        self.assertRaises(TypeError, divmod, o, p)
        self.assertRaises(TypeError, divmod, o, 2)
        self.assertRaises(TypeError, divmod, 2, o)

    def testInplaceAddition(self):
        r = NSDecimal()
        o = NSDecimal(1)
        p = NSDecimal(2)

        NSDecimalAdd(r, o, p, NSRoundPlain)

        o = NSDecimal(1)
        o += p
        self.assertEquals(o, r)

        o = NSDecimal(1)
        o += 2
        self.assertEquals(o, r)

        o = NSDecimal(1)
        o += 2L
        self.assertEquals(o, r)

        o = 1
        o += p
        self.assertEquals(o, r)

        o = 1L
        o += p
        self.assertEquals(o, r)

        try:
            o = 1.2
            o += p
            self.fail()
        except TypeError:
            pass

        try:
            o = NSDecimal(1)
            o += 1.2
            self.fail()
        except TypeError:
            pass

    def testInplaceSubtraction(self):
        r = NSDecimal()
        o = NSDecimal(1)
        p = NSDecimal(2)

        NSDecimalSubtract(r, o, p, NSRoundPlain)

        o = NSDecimal(1)
        o -= p
        self.assertEquals(o, r)

        o = NSDecimal(1)
        o -= 2
        self.assertEquals(o, r)

        o = NSDecimal(1)
        o -= 2
        self.assertEquals(o, r)

        o = 1
        o -= p
        self.assertEquals(o, r)

        o = 1
        o -= p
        self.assertEquals(o, r)

    def testInplaceMultiplication(self):
        r = NSDecimal()
        o = NSDecimal(2)
        p = NSDecimal(3)

        NSDecimalMultiply(r, o, p, NSRoundPlain)

        o = NSDecimal(2)
        o *= p
        self.assertEquals(o, r)

        o = NSDecimal(2)
        o *= 3
        self.assertEquals(o, r)

        o = NSDecimal(2)
        o *= 3L
        self.assertEquals(o, r)

        o = 2
        o *= p
        self.assertEquals(o, r)

        o = 2L
        o *= p
        self.assertEquals(o, r)

    def testInplaceDivision(self):
        r = NSDecimal()
        o = NSDecimal(2)
        p = NSDecimal(3)

        NSDecimalDivide(r, o, p, NSRoundPlain)

        o = NSDecimal(2)
        o /= p
        self.assertEquals(o, r)

        o = NSDecimal(2)
        o /= 3
        self.assertEquals(o, r)

        o = NSDecimal(2)
        o /= 3L
        self.assertEquals(o, r)

        o = 2
        o /= p
        self.assertEquals(o, r)

        o = 2L
        o /= p
        self.assertEquals(o, r)

class NSDecimalNumberOperators (unittest.TestCase):
    def testAddition(self):
        r = NSDecimal()
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(1))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))

        NSDecimalAdd(r, o.decimalValue(), p.decimalValue(), NSRoundPlain)
        self.assertEquals((o+p), r)
        self.assertEquals((o+2), r)
        self.assertEquals((o+2L), r)
        self.assertEquals((1+p), r)
        self.assertEquals((1+p), r)

        self.assertRaises(TypeError, operator.add, o, 1.2)
        self.assertRaises(TypeError, operator.add, 1.2, o)

        o = NSDecimalNumber.zero()
        self.assertRaises(TypeError, operator.add, o, 1.2)

    def testSubtraction(self):
        r = NSDecimal()
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(1))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))

        NSDecimalSubtract(r, o.decimalValue(), p.decimalValue(), NSRoundPlain)
        self.assertEquals((o-p), r)
        self.assertEquals((o-2), r)
        self.assertEquals((o-2L), r)
        self.assertEquals((1-p), r)
        self.assertEquals((1-p), r)

        self.assertRaises(TypeError, operator.sub, o, 1.2)
        self.assertRaises(TypeError, operator.sub, 1.2, o)

    def testMultiplication(self):
        r = NSDecimal()
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(3))

        NSDecimalMultiply(r, o.decimalValue(), p.decimalValue(), NSRoundPlain)
        self.assertEquals((o*p), r)
        self.assertEquals((o*3), r)
        self.assertEquals((o*3L), r)
        self.assertEquals((2*p), r)
        self.assertEquals((2*p), r)

        self.assertRaises(TypeError, operator.mul, o, 1.2)
        self.assertRaises(TypeError, operator.mul, 1.2, o)

    def testDivision(self):
        r = NSDecimal()
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(3))

        NSDecimalDivide(r, o.decimalValue(), p.decimalValue(), NSRoundPlain)
        self.assertEquals((o/p), r)
        self.assertEquals((o/3), r)
        self.assertEquals((o/3L), r)
        self.assertEquals((2/p), r)
        self.assertEquals((2/p), r)

        self.assertRaises(TypeError, operator.div, o, 1.2)
        self.assertRaises(TypeError, operator.div, 1.2, o)

    def testPositive(self):
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(-2))

        self.assertEquals((+o), o.decimalValue())
        self.assertEquals((+p), p.decimalValue())

    def testNegative(self):
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(-2))

        self.assertEquals((-o), p.decimalValue())
        self.assertEquals((-p), o.decimalValue())

    def testAbs(self):
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(-2))

        self.assertEquals(abs(o), o.decimalValue())
        self.assertEquals(abs(p), o.decimalValue())

    def testBitwise(self):
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(-2))

        self.assertRaises(TypeError, operator.and_, o, p)
        self.assertRaises(TypeError, operator.or_, o, p)
        self.assertRaises(TypeError, operator.not_, o, p)

    def testPow(self):
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(-2))

        self.assertRaises(TypeError, pow, o, p)
        self.assertRaises(TypeError, pow, o, 2)
        self.assertRaises(TypeError, pow, 2, o)

    def testDivMod(self):
        o = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(2))
        p = NSDecimalNumber.decimalNumberWithDecimal_(NSDecimal(-2))

        self.assertRaises(TypeError, divmod, o, p)
        self.assertRaises(TypeError, divmod, o, 2)
        self.assertRaises(TypeError, divmod, 2, o)

if __name__ == "__main__":
    unittest.main()
