import objc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")


class NotBool:
    def __bool__(self):
        raise RuntimeError("not bool")


class TestFinal(TestCase):
    def test_default_nonfinal(self):
        self.assertFalse(NSObject.__objc_final__)

    def test_final_subclass(self):
        class FinalClass(NSObject, final=True):
            pass

        self.assertTrue(FinalClass.__objc_final__)

        with self.assertRaisesRegex(TypeError, "super class FinalClass is final"):

            class SubclaasOfFinal(FinalClass):
                pass

    def test_make_final(self):
        class NonFinalClass(NSObject):
            pass

        self.assertFalse(NonFinalClass.__objc_final__)

        NonFinalClass.__objc_final__ = True

        self.assertTrue(NonFinalClass.__objc_final__)

        class NoCompare:
            def __bool__(self):
                raise RuntimeError("no compare")

        with self.assertRaises(RuntimeError):
            NonFinalClass.__objc_final__ = NoCompare()

        with self.assertRaisesRegex(
            TypeError, "Cannot delete __objc_final__ attribute"
        ):
            del NonFinalClass.__objc_final__

        with self.assertRaisesRegex(RuntimeError, "not bool"):
            NonFinalClass.__objc_final__ = NotBool()
