from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSDecimalNumber (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSDecimalNumberExactnessException, unicode)
        self.assertIsInstance(NSDecimalNumberOverflowException, unicode)
        self.assertIsInstance(NSDecimalNumberUnderflowException, unicode)
        self.assertIsInstance(NSDecimalNumberDivideByZeroException, unicode)
    def testNSDecimal(self):
        dec = NSDecimal('55.0')

        v = NSDecimalNumber.alloc().initWithDecimal_(dec)
        self.assertIsInstance(v, NSDecimalNumber)
        self.assertEqual(str(v), '55')

        v = NSDecimalNumber.decimalNumberWithDecimal_(dec)
        self.assertIsInstance(v, NSDecimalNumber)
        self.assertEqual(str(v), '55')

        o = v.decimalValue()
        self.assertIsInstance(o, NSDecimal)

    def testNSNumberAsNSDecimal(self):
        v = NSNumber.numberWithFloat_(33.5)
        o = v.decimalValue()
        self.assertIsInstance(o, NSDecimal)

    def testNSScannerWithDecimal(self):
        v = NSScanner.alloc().initWithString_("55.23")
        
        dec = NSDecimal()
        o = v.scanDecimal_(dec)
        self.assertIsObject(o, True)
        self.assertEqual(str(dec), '55.23')

if __name__ == "__main__":
    main()
