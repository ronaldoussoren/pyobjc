import objc
from .unavailable import OC_NSUnavailable, OC_NSUnavailableChild
from PyObjCTools.TestSupport import TestCase

objc.registerUnavailableMethod("OC_NSUnavailable", b"instmeth1")
objc.registerUnavailableMethod("OC_NSUnavailable", b"clsmeth1")


class OC_PyUnavailable(OC_NSUnavailable):
    def instmeth1(self):
        return "py-inst"

    @classmethod
    def clsmeth1(self):
        return "py-cls"


class TestUnavailable(TestCase):
    def test_method_unavailable(self):
        v = OC_NSUnavailable.alloc().init()
        with self.assertRaisesRegex(TypeError, "'instmeth1' is NS_UNAVAILABLE"):
            v.instmeth1()

        with self.assertRaisesRegex(TypeError, "'clsmeth1' is NS_UNAVAILABLE"):
            OC_NSUnavailable.clsmeth1()

        with self.assertRaisesRegex(AttributeError, "has no attribute 'clsmeth1'"):
            v.clsmeth1()

    def test_method_unavailable_in_subclass(self):
        # Same as test_method_unavailable but with
        # OC_NSUnavailbleChild.
        v = OC_NSUnavailableChild.alloc().init()
        with self.assertRaisesRegex(TypeError, "'instmeth1' is NS_UNAVAILABLE"):
            v.instmeth1()

        with self.assertRaisesRegex(TypeError, "'clsmeth1' is NS_UNAVAILABLE"):
            OC_NSUnavailableChild.clsmeth1()

        with self.assertRaisesRegex(AttributeError, "has no attribute 'clsmeth1'"):
            v.clsmeth1()

    # XXX: Add this (and corresponding implementation) when
    #      there are instances where a Cocoa class uses
    #      NS_UNAVAILABLE and a Cocoa subclass makes it available
    #      again ('Cocoa subclass' being 'in Apple's system headers')
    #
    # def test_method_availble_in_subclass(self):
    #    self.fail()
    #

    def test_instance_method_defined_in_python(self):
        # Subclass class from `test_instance_method_unavailable` and
        # define the unavailable method. Check that method then works
        # on the subclass (and still doesn't work on parent class)

        v = OC_PyUnavailable.alloc().init()
        self.assertEqual(v.instmeth1(), "py-inst")
        self.assertEqual(OC_PyUnavailable.clsmeth1(), "py-cls")

        # Also test by invoking the selector through ObjC
        self.assertEqual(OC_PyUnavailable.invokeInst_(v), "py-inst")
        self.assertEqual(OC_PyUnavailable.invokeCls(), "py-cls")
