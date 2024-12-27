from PyObjCTools.TestSupport import TestCase
import objc

NSInvocation = objc.lookUpClass("NSInvocation")
NSMutableArray = objc.lookUpClass("NSMutableArray")


class NoObjCClass:
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


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

        invocation.setReturnValue_(8)
        v = invocation.getReturnValue_(None)
        self.assertIsInstance(v, int)
        self.assertEqual(v, 8)

        with self.assertRaisesRegex(ValueError, "depythonifying.*got.*"):
            invocation.setReturnValue_(None)

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

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            invocation.setArgument_atIndex_(NoObjCClass(), 2)

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            invocation.getReturnValue_()

        with self.assertRaisesRegex(ValueError, "buffer must be None"):
            invocation.getReturnValue_("42")

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            invocation.setReturnValue_()

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            invocation.getArgument_atIndex_()

        with self.assertRaisesRegex(ValueError, "buffer must be None"):
            invocation.getArgument_atIndex_("hello", 2)

        with self.assertRaisesRegex(ValueError, "depythonifying.*got.*"):
            invocation.getArgument_atIndex_(None, "two")

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            invocation.setArgument_atIndex_()

        with self.assertRaisesRegex(ValueError, "depythonifying.*got.*"):
            invocation.setArgument_atIndex_("hello", "two")

    def test_dummy_with_imps(self):
        value = NSMutableArray.arrayWithArray_([1, 2, 3])

        invocation = NSInvocation.invocationWithMethodSignature_(
            value.methodSignatureForSelector_("count")
        )
        invocation.setSelector_("count")
        invocation.setTarget_(value)
        invocation.invoke()

        imp = invocation.methodForSelector_(b"getReturnValue:")
        v = imp(invocation, None)
        self.assertIsInstance(v, int)
        self.assertEqual(v, 3)

        imp = invocation.methodForSelector_(b"setReturnValue:")
        imp(invocation, 8)

        invocation = NSInvocation.invocationWithMethodSignature_(
            value.methodSignatureForSelector_("addObject:")
        )
        invocation.setSelector_("addObject:")
        invocation.setTarget_(value)
        imp = invocation.methodForSelector_(b"setArgument:atIndex:")
        imp(invocation, "hello", 2)

        imp = invocation.methodForSelector_(b"getArgument:atIndex:")
        v = imp(invocation, None, 2)
        self.assertEqual(v, "hello")
        invocation.invoke()

        self.assertEqual(value.count(), 4)
