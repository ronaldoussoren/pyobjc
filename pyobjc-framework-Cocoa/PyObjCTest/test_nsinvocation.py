from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation

try:
    long
except NameError:
    long = int


class TestNSInvocation (TestCase):
    def test_dummy(self):
        value = NSMutableArray.arrayWithArray_([1, 2, 3])

        invocation = NSInvocation.invocationWithMethodSignature_(value.methodSignatureForSelector_('count'))
        invocation.setSelector_('count')
        invocation.setTarget_(value)
        invocation.invoke()

        v = invocation.getReturnValue_(None)
        self.assertIsInstance(v, (int, long))
        self.assertEqual(v, 3)

        invocation = NSInvocation.invocationWithMethodSignature_(value.methodSignatureForSelector_('addObject:'))
        invocation.setSelector_('addObject:')
        invocation.setTarget_(value)
        invocation.setArgument_atIndex_(b"hello".decode('ascii'), 2)
        v = invocation.getArgument_atIndex_(None, 2)
        self.assertEqual(v, b"hello".decode('ascii'))
        invocation.invoke()

        self.assertEqual(value.count(), 4)



    def testMethods(self):
        self.assertResultIsBOOL(NSInvocation.argumentsRetained)

    def testNoUnsupported(self):
        self.assertNotHasAttr(Foundation, 'NSObjCValue')
        self.assertNotHasAttr(Foundation, 'NSObjCNoType')
        self.assertNotHasAttr(Foundation, 'NSObjCVoidType')
        self.assertNotHasAttr(Foundation, 'NSObjCCharType')
        self.assertNotHasAttr(Foundation, 'NSObjCShortType')
        self.assertNotHasAttr(Foundation, 'NSObjCLongType')
        self.assertNotHasAttr(Foundation, 'NSObjCLonglongType')
        self.assertNotHasAttr(Foundation, 'NSObjCFloatType')
        self.assertNotHasAttr(Foundation, 'NSObjCDoubleType')
        self.assertNotHasAttr(Foundation, 'NSObjCBoolType')
        self.assertNotHasAttr(Foundation, 'NSObjCSelectorType')
        self.assertNotHasAttr(Foundation, 'NSObjCObjectType')
        self.assertNotHasAttr(Foundation, 'NSObjCStructType')
        self.assertNotHasAttr(Foundation, 'NSObjCPointerType')
        self.assertNotHasAttr(Foundation, 'NSObjCStringType')
        self.assertNotHasAttr(Foundation, 'NSObjCArrayType')
        self.assertNotHasAttr(Foundation, 'NSObjCUnionType')
        self.assertNotHasAttr(Foundation, 'NSObjCBitfield')
if __name__ == "__main__":
    main()
