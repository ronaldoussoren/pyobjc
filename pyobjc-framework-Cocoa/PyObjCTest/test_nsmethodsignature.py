import Foundation
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSMethodSignature(TestCase):
    def testTypes(self):
        o = Foundation.NSObject.instanceMethodSignatureForSelector_("description")

        m = Foundation.NSMethodSignature.signatureWithObjCTypes_.__metadata__()
        self.assertEqual(m["arguments"][2]["type"], b"n^t")

        m = o.methodReturnType.__metadata__()
        self.assertEqual(m["retval"]["type"], b"^t")
        m = o.getArgumentTypeAtIndex_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"^t")

    def testUsing(self):
        o = Foundation.NSMethodSignature.signatureWithObjCTypes_(b"^v@:@o^i")
        self.assertIsInstance(o, Foundation.NSMethodSignature)
        v = o.methodReturnType()
        self.assertEqual(v, b"^v")
        self.assertIsInstance(v, bytes)
        v = o.getArgumentTypeAtIndex_(0)
        self.assertEqual(v, b"@")
        self.assertIsInstance(v, bytes)
        v = o.getArgumentTypeAtIndex_(3)
        self.assertEqual(v, b"o^i")
        self.assertIsInstance(v, bytes)

    def testMethods(self):
        self.assertResultHasType(
            Foundation.NSMethodSignature.getArgumentTypeAtIndex_,
            b"^" + objc._C_CHAR_AS_TEXT,
        )
        self.assertResultIsNullTerminated(
            Foundation.NSMethodSignature.getArgumentTypeAtIndex_
        )
        self.assertResultHasType(
            Foundation.NSMethodSignature.methodReturnType, b"^" + objc._C_CHAR_AS_TEXT
        )
        self.assertResultIsNullTerminated(Foundation.NSMethodSignature.methodReturnType)
        self.assertResultIsBOOL(Foundation.NSMethodSignature.isOneway)
