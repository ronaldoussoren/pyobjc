import objc
from PyObjCTools.TestSupport import TestCase
from objc import super  # noqa: A004
import objc._new as new_mod

NSObject = objc.lookUpClass("NSObject")


class TestDefaultNewForPythonClass(TestCase):
    def test_nsobject(self):
        v = NSObject()
        self.assertIsInstance(v, NSObject)

        self.assertEqual(new_mod.NEW_MAP["NSObject"], {(): "init"})

        with self.assertRaisesRegex(
            TypeError, r"NSObject\(\) does not support keyword arguments 'y', 'x'"
        ):
            NSObject(y=3, x=4)

    def test_basic(self):
        class OCPyNew1(NSObject):
            def initWithX_y_(self, x_val, y_val):
                self = super().init()
                self.x = x_val
                self.y = y_val
                return self

            def initPoint_(self, p):
                self = super().init()
                self.x, self.y = p
                return self

            def initializeZ_(self, z):
                self.z = 0

        v = OCPyNew1(x=1, y=2)
        self.assertIsInstance(v, OCPyNew1)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

        v = OCPyNew1(point=(3, 4))
        self.assertIsInstance(v, OCPyNew1)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4)

        v = OCPyNew1()
        self.assertIsInstance(v, OCPyNew1)

        with self.assertRaisesRegex(
            TypeError, r"OCPyNew1\(\) does not support keyword arguments 'y', 'x'"
        ):
            OCPyNew1(y=3, x=4)

        with self.assertRaisesRegex(
            TypeError, r"OCPyNew1\(\) does not support keyword arguments 'z'"
        ):
            OCPyNew1(z=4)

    def test_explicit_new(self):
        # Test that an explicit __new__ overrides the default
        # implementation.
        class OCPyNew2(NSObject):
            def __new__(self, *, z):
                return self.alloc().initWithValue_(z)

            def initWithValue_(self, value):
                self = super().init()
                self.value = value
                return self

        v = OCPyNew2(z=4)
        self.assertEqual(v.value, 4)

        with self.assertRaisesRegex(TypeError, "got an unexpected keyword argument"):
            OCPyNew2(value=9)

    def test_dunder_init(self):
        class OCPyNew3(NSObject):
            def initWithValue_(self, v):
                self = super().init()
                self.value = v
                return self

            def __init__(self, **kwds):
                # __init__ is never called automaticly for
                # Cocoa classes.
                self.value += 1

        v = OCPyNew3.alloc().initWithValue_(3)
        self.assertEqual(v.value, 3)

        v = OCPyNew3(value=4)
        self.assertEqual(v.value, 4)

    def test_dunder_init_with_error(self):
        class OCPyNew4(NSObject):
            def initWithValue_error_(self, v, error):
                self = super().init()
                self.value = v
                return self, None

            def __init__(self, **kwds):
                # __init__ is never called automaticly for
                # Cocoa classes.
                self.value += 1

        v, e = OCPyNew4.alloc().initWithValue_error_(3, None)
        self.assertEqual(v.value, 3)
        self.assertIs(e, None)

        v, e = OCPyNew4(value=4, error=None)
        self.assertEqual(v.value, 4)
        self.assertIs(e, None)

    def test_init_is_none(self):
        class OCPyNew5(NSObject):
            init = None

            def initWithValue_(self, new_value):
                self = super().init()
                self.value = new_value
                return self

        with self.assertRaisesRegex(
            TypeError, r"OCPyNew5\(\) requires keyword arguments"
        ):
            OCPyNew5()

        v = OCPyNew5(value=3)
        self.assertIsInstance(v, OCPyNew5)
        self.assertEqual(v.value, 3)


# TODO: TestDefaultNewForObjectiveCClass
# Need the metadata update interface before implementing this.
# Also check interaction with __init__
