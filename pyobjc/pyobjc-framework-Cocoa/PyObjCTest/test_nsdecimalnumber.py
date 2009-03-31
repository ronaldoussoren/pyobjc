from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSDecimalNumber (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSDecimalNumberExactnessException, unicode))
        self.failUnless(isinstance(NSDecimalNumberOverflowException, unicode))
        self.failUnless(isinstance(NSDecimalNumberUnderflowException, unicode))
        self.failUnless(isinstance(NSDecimalNumberDivideByZeroException, unicode))

    def testNSDecimal(self):
        dec = NSDecimal('55.0')

        v = NSDecimalNumber.alloc().initWithDecimal_(dec)
        self.failUnlessIsInstance(v, NSDecimalNumber)
        self.failUnlessEqual(str(v), '55')

        v = NSDecimalNumber.decimalNumberWithDecimal_(dec)
        self.failUnlessIsInstance(v, NSDecimalNumber)
        self.failUnlessEqual(str(v), '55')

        o = v.decimalValue()
        self.failUnlessIsInstance(o, NSDecimal)

    def testNSNumberAsNSDecimal(self):
        v = NSNumber.numberWithFloat_(33.5)
        o = v.decimalValue()
        self.failUnlessIsInstance(o, NSDecimal)

    def testNSScannerWithDecimal(self):
        v = NSScanner.alloc().initWithString_("55.23")
        
        dec = NSDecimal()
        o = v.scanDecimal_(dec)
        self.failUnless(o is True)

        self.failUnlessEqual(str(dec), '55.23')

if __name__ == "__main__":
    main()
