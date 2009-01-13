from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSDecimalNumber (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSDecimalNumberExactnessException, unicode))
        self.failUnless(isinstance(NSDecimalNumberOverflowException, unicode))
        self.failUnless(isinstance(NSDecimalNumberUnderflowException, unicode))
        self.failUnless(isinstance(NSDecimalNumberDivideByZeroException, unicode))

    def testNSDecimal(self):
        self.fail("initWithDecimal:")
        self.fail("decimalValue")
        self.fail("decimalNumberWithDecimal:")

    def testNSNumberAsNSDecimal(self):
        self.fail('NSNumber.decimalValue')

    def testNSScannerWithDecimal(self):
        self.fail('NSScanner.scanDecimal')

if __name__ == "__main__":
    main()
