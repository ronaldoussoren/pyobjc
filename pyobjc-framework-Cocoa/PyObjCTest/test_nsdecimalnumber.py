from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

try:
    bytes
except NameError:
    bytes = str

class Behaviour (NSObject):
    def exceptionDuringOperation_error_leftOperand_rightOperand_(self, exc, err, l, r):
        pass


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
        self.assertEqual(v.description(), '55')

        v = NSDecimalNumber.decimalNumberWithDecimal_(dec)
        self.assertIsInstance(v, NSDecimalNumber)
        self.assertEqual(v.description(), '55')

        o = v.decimalValue()
        self.assertIsInstance(o, NSDecimal)

        o = v.objCType()
        self.assertIsInstance(o, bytes)

    def testNSNumberAsNSDecimal(self):
        v = NSNumber.numberWithFloat_(33.5)
        o = v.decimalValue()
        self.assertIsInstance(o, NSDecimal)

    def testNSScannerWithDecimal(self):
        v = NSScanner.alloc().initWithString_("55.23")

        dec = NSDecimal()
        o = v.scanDecimal_(dec)
        self.assertIs(o, True)
        self.assertEqual(dec.description(), '55.23')

    def testMethods(self):
        self.assertArgIsBOOL(NSDecimalNumber.initWithMantissa_exponent_isNegative_, 2)
        self.assertArgIsBOOL(NSDecimalNumber.decimalNumberWithMantissa_exponent_isNegative_, 2)

        self.assertArgIsBOOL(NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 2)
        self.assertArgIsBOOL(NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 3)
        self.assertArgIsBOOL(NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 4)
        self.assertArgIsBOOL(NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 5)

        self.assertArgIsBOOL(NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 2)
        self.assertArgIsBOOL(NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 3)
        self.assertArgIsBOOL(NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 4)
        self.assertArgIsBOOL(NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_, 5)


    def testProtocols(self):
        self.assertArgHasType(Behaviour.exceptionDuringOperation_error_leftOperand_rightOperand_, 0, objc._C_SEL)
        self.assertArgHasType(Behaviour.exceptionDuringOperation_error_leftOperand_rightOperand_, 1, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
