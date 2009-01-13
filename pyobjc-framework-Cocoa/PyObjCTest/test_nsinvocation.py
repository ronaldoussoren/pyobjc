from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation

class TestNSInvocation (TestCase):
    def test_dummy(self):
        self.fail("NSInvocation tests")
        self.fail("getArgument:atIndex:")
        self.fail("setArgument:atIndex:")
        self.fail("getReturnValue:")
        self.fail("setReturnValue:")

    def testNoUnsupported(self):
        self.failIf(hasattr(Foundation, 'NSObjCValue'))
        self.failIf(hasattr(Foundation, 'NSObjCNoType'))
        self.failIf(hasattr(Foundation, 'NSObjCVoidType'))
        self.failIf(hasattr(Foundation, 'NSObjCCharType'))
        self.failIf(hasattr(Foundation, 'NSObjCShortType'))
        self.failIf(hasattr(Foundation, 'NSObjCLongType'))
        self.failIf(hasattr(Foundation, 'NSObjCLonglongType'))
        self.failIf(hasattr(Foundation, 'NSObjCFloatType'))
        self.failIf(hasattr(Foundation, 'NSObjCDoubleType'))
        self.failIf(hasattr(Foundation, 'NSObjCBoolType'))
        self.failIf(hasattr(Foundation, 'NSObjCSelectorType'))
        self.failIf(hasattr(Foundation, 'NSObjCObjectType'))
        self.failIf(hasattr(Foundation, 'NSObjCStructType'))
        self.failIf(hasattr(Foundation, 'NSObjCPointerType'))
        self.failIf(hasattr(Foundation, 'NSObjCStringType'))
        self.failIf(hasattr(Foundation, 'NSObjCArrayType'))
        self.failIf(hasattr(Foundation, 'NSObjCUnionType'))
        self.failIf(hasattr(Foundation, 'NSObjCBitfield'))


if __name__ == "__main__":
    main()
