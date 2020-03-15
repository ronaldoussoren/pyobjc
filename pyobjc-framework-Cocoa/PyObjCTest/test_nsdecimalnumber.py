import Foundation
from PyObjCTools.TestSupport import TestCase
import objc


class Behaviour(Foundation.NSObject):
    def scale(self):
        return 1

    def roundingMode(self):
        return 1

    def exceptionDuringOperation_error_leftOperand_rightOperand_(self, exc, err, l, r):
        pass


class TestNSDecimalNumber(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSDecimalNumberExactnessException, str)
        self.assertIsInstance(Foundation.NSDecimalNumberOverflowException, str)
        self.assertIsInstance(Foundation.NSDecimalNumberUnderflowException, str)
        self.assertIsInstance(Foundation.NSDecimalNumberDivideByZeroException, str)

    def testNSDecimal(self):
        dec = Foundation.NSDecimal("55.0")

        v = Foundation.NSDecimalNumber.alloc().initWithDecimal_(dec)
        self.assertIsInstance(v, Foundation.NSDecimalNumber)
        self.assertEqual(v.description(), "55")

        v = Foundation.NSDecimalNumber.decimalNumberWithDecimal_(dec)
        self.assertIsInstance(v, Foundation.NSDecimalNumber)
        self.assertEqual(v.description(), "55")

        o = v.decimalValue()
        self.assertIsInstance(o, Foundation.NSDecimal)

        o = v.objCType()
        self.assertIsInstance(o, bytes)

    def testNSNumberAsNSDecimal(self):
        v = Foundation.NSNumber.numberWithFloat_(33.5)
        o = v.decimalValue()
        self.assertIsInstance(o, Foundation.NSDecimal)

    def testNSScannerWithDecimal(self):
        v = Foundation.NSScanner.alloc().initWithString_("55.23")

        o, dec = v.scanDecimal_(None)
        self.assertIsInstance(dec, Foundation.NSDecimal)
        self.assertIs(o, True)
        self.assertEqual(str(dec), "55.23")

    def testMethods(self):
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumber.initWithMantissa_exponent_isNegative_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumber.decimalNumberWithMantissa_exponent_isNegative_, 2
        )

        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.initWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            5,
        )

        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            Foundation.NSDecimalNumberHandler.decimalNumberHandlerWithRoundingMode_scale_raiseOnExactness_raiseOnOverflow_raiseOnUnderflow_raiseOnDivideByZero_,  # noqa: B950
            5,
        )

    def testProtocols(self):
        objc.protocolNamed("NSDecimalNumberBehaviors")
        self.assertArgHasType(
            Behaviour.exceptionDuringOperation_error_leftOperand_rightOperand_,
            0,
            objc._C_SEL,
        )
        self.assertArgHasType(
            Behaviour.exceptionDuringOperation_error_leftOperand_rightOperand_,
            1,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            Behaviour.scale, objc._C_SHT
        )  # XXX: should this happen without a protocol definition, a bit too generic!
        self.assertResultHasType(Behaviour.roundingMode, objc._C_NSUInteger)
