from PyObjCTools.TestSupport import TestCase

import objc
from objc import super  # noqa: A004
from .objectint import OC_ObjectInt

NSProxy = objc.lookUpClass("NSProxy")
NSProtocolChecker = objc.lookUpClass("NSProtocolChecker")
NSArray = objc.lookUpClass("NSArray")

NSProxy.__useKVO__ = False

deallocated = False


class OC_Proxy(NSProxy):
    __slots__ = ("v",)

    def init(self):
        self.v = 9

    def initWithValue_(self, v):
        self.v = v
        return self

    def add_(self, a):
        return a + self.v

    def dealloc(self):
        global deallocated
        deallocated = True
        super().dealloc()


class TestNSProxyHandling(TestCase):
    def test_protocol_checker(self):
        array = NSArray.arrayWithArray_([1, 2, 3])
        self.assertEqual(array.count(), 3)

        with objc.autorelease_pool():
            checker = NSProtocolChecker.protocolCheckerWithTarget_protocol_(
                array, objc.protocolNamed("NSObject")
            )
            self.assertIsInstance(checker, NSProxy)

            with self.assertRaises(AttributeError):
                checker.count()

        self.assertEqual(checker.retainCount(), 1)

    def test_proxy_subclass(self):
        global deallocated
        with objc.autorelease_pool():
            # XXX: 'init' won't work
            o = OC_Proxy.alloc().initWithValue_(2)

        self.assertEqual(o.retainCount(), 1)

        self.assertEqual(o.add_(4), 6)
        self.assertFalse(deallocated)
        del o
        self.assertTrue(deallocated)

        with objc.autorelease_pool():
            deallocated = False
            # XXX: 'init' won't work
            o = OC_Proxy.alloc().initWithValue_(2)
            v = OC_ObjectInt.invokeSelector_of_withArg_(b"add:", o, 9)
            self.assertEqual(v, 11)
            del o
            self.assertTrue(deallocated)

    def test_proxy_class_in_array(self):
        arr = NSArray.arrayWithObject_(NSProxy)
        self.assertIs(arr[0], NSProxy)
