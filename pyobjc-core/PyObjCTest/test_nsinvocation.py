from PyObjCTools.TestSupport import TestCase
import objc

NSInvocation = objc.lookUpClass("NSInvocation")
NSMutableArray = objc.lookUpClass("NSMutableArray")


class TestNSInvocation(TestCase):
    def test_dummy(self):
        value = NSMutableArray.arrayWithArray_([1, 2, 3])

        invocation = NSInvocation.invocationWithMethodSignature_(
            value.methodSignatureForSelector_("count")
        )
        invocation.setSelector_("count")
        invocation.setTarget_(value)
        invocation.invoke()

        v = invocation.getReturnValue_(None)
        self.assertIsInstance(v, int)
        self.assertEqual(v, 3)

        invocation = NSInvocation.invocationWithMethodSignature_(
            value.methodSignatureForSelector_("addObject:")
        )
        invocation.setSelector_("addObject:")
        invocation.setTarget_(value)
        invocation.setArgument_atIndex_("hello", 2)
        v = invocation.getArgument_atIndex_(None, 2)
        self.assertEqual(v, "hello")
        invocation.invoke()

        self.assertEqual(value.count(), 4)
