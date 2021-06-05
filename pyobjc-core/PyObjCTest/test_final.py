import objc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")


class TestFinal(TestCase):
    def test_default_nonfinal(self):
        self.assertFalse(NSObject.__objc_final__)

    def test_final_subclass(self):
        class FinalClass(NSObject, final=True):
            pass

        self.assertTrue(FinalClass.__objc_final__)

        # with self.assertRaises(TypeError):
        #    class SubclaasOfFinal (FinalClass):
        #        pass

    def test_make_final(self):
        class NonFinalClass(NSObject):
            pass

        self.assertFalse(NonFinalClass.__objc_final__)

        NonFinalClass.__objc_final__ = True

        self.assertTrue(NonFinalClass.__objc_final__)
