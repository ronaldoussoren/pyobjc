from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation

class TestNSInvocation (TestCase):
    def test_dummy(self):
        value = NSMutableArray.arrayWithArray_([1, 2, 3])

        invocation = NSInvocation.invocationWithMethodSignature_(value.methodSignatureForSelector_('count'))
        invocation.setSelector_('count')
        invocation.setTarget_(value)
        invocation.invoke()

        v = invocation.getReturnValue_(None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessEqual(v, 3)

        invocation = NSInvocation.invocationWithMethodSignature_(value.methodSignatureForSelector_('addObject:'))
        invocation.setSelector_('addObject:')
        invocation.setTarget_(value)
        invocation.setArgument_atIndex_(u"hello", 2)
        v = invocation.getArgument_atIndex_(None, 2)
        self.failUnlessEqual(v, u"hello")
        invocation.invoke()

        self.failUnlessEqual(value.count(), 4)



    def testMethods(self):
        self.failUnlessResultIsBOOL(NSInvocation.argumentsRetained)

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
