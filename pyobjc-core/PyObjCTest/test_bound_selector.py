from PyObjCTools.TestSupport import TestCase
import objc
import gc

NSObject = objc.lookUpClass("NSObject")


class TestBoundSelector(TestCase):
    def test_no_creation(self):
        with self.assertRaisesRegex(
            TypeError, "Cannot create instances of objc.bound_selector"
        ):
            objc.bound_selector(b"hello")

    def test_compare(self):
        o = NSObject.alloc().init()
        p = NSObject.alloc().init()

        d1 = o.description
        d2 = p.description
        m1 = o.methodForSelector_

        self.assertFalse(d1 == 42)
        self.assertTrue(d1 != 42)
        self.assertFalse(42 == d1)
        self.assertTrue(42 != d1)

        self.assertTrue(o.description == o.description)
        self.assertTrue(d1 == d1)
        self.assertFalse(d1 != d1)

        self.assertTrue(d1 != d2)
        self.assertFalse(d1 == d2)

        self.assertTrue(d1 != m1)
        self.assertFalse(d1 == m1)

        self.assertTrue(d1 != o)
        self.assertFalse(d1 == o)

        self.assertTrue(o != d1)
        self.assertFalse(o == d1)

        with self.assertRaisesRegex(TypeError, "'<' not supported"):
            d1 < d2  # noqa: B015

    def test_compare_raises(self):
        class C:
            def __call__(self, first):
                return 1

            def __hash__(self):
                return 42

            def __eq__(self, other):
                raise RuntimeError("no comparing here")

            def __ne__(self, other):
                raise RuntimeError("no comparing here")

        with self.assertRaisesRegex(RuntimeError, "no comparing here"):
            C() == C()  # noqa: B015

        s1 = objc.selector(C(), selector=b"method", signature=b"@@:")
        s2 = objc.selector(C(), selector=b"method", signature=b"@@:")
        self.assertIsInstance(s1, objc.python_selector)
        self.assertIsInstance(s2, objc.python_selector)
        with self.assertRaisesRegex(RuntimeError, "no comparing here"):
            s1 == s2  # noqa: B015

        obj = NSObject.alloc().init()
        b1 = s1.__get__(obj, NSObject)
        b2 = s2.__get__(obj, NSObject)
        self.assertIsInstance(b1, objc.bound_selector)
        self.assertIsInstance(b2, objc.bound_selector)

        with self.assertRaisesRegex(RuntimeError, "no comparing here"):
            b1 == b2  # noqa: B015

    def test_clearing(self):
        done = False

        class D:
            def __del__(self):
                nonlocal done
                print("done")
                done = True

        @objc.selector
        def foo(self):
            pass

        o = foo.__get__(foo)
        del foo
        o.__func__.callable.attr = D()
        o.__func__.callable.attr2 = o

        self.assertFalse(done)
        del o
        self.assertFalse(done)
        for _ in range(5):
            gc.collect()

        # XXX: This fails because python_selector
        # and native_selector don't implement the GC
        # protocol.
        # self.assertTrue(done)
