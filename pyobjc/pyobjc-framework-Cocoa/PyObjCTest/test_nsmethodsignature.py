from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSMethodSignature (TestCase):

    def testTypes(self):
        o = NSObject.instanceMethodSignatureForSelector_('description')

        m = NSMethodSignature.signatureWithObjCTypes_.__metadata__()
        self.assertEquals(m['arguments'][2]['type'], 'n^t')

        m = o.methodReturnType.__metadata__()
        self.assertEquals(m['retval']['type'], '^t')
        m = o.getArgumentTypeAtIndex_.__metadata__()
        self.assertEquals(m['retval']['type'], '^t')

    def testUsing(self):
        o = NSMethodSignature.signatureWithObjCTypes_('^v@:@o^i')
        self.failUnless(isinstance(o, NSMethodSignature))

        v = o.methodReturnType()
        self.assertEquals(v, '^v')
        self.failUnless(isinstance(v, str))

        v = o.getArgumentTypeAtIndex_(0)
        self.assertEquals(v, '@')
        self.failUnless(isinstance(v, str))

        v = o.getArgumentTypeAtIndex_(3)
        self.assertEquals(v, 'o^i')
        self.failUnless(isinstance(v, str))

    def testMethods(self):
        self.failUnlessResultHasType(NSMethodSignature.getArgumentTypeAtIndex_, '^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessResultIsNullTerminated(NSMethodSignature.getArgumentTypeAtIndex_)
        self.failUnlessResultHasType(NSMethodSignature.methodReturnType, '^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessResultIsNullTerminated(NSMethodSignature.methodReturnType)
        self.failUnlessResultIsBOOL(NSMethodSignature.isOneway)

            
if __name__ == "__main__":
    main()
