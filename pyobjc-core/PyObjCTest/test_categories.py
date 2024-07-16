"""
Tests for handling Objective-C categories that are loaded
in Objective-C.

These tests are primarily here to check that caching
of attribute lookups works correctly, even when
there are categories or other dynamic behaviours that
add to the set of methods on a class (directly or
indirectly).

     *** GENERATED FILE ***

These tests are generated from Tools/generate-category-tests.py
"""

from PyObjCTools.TestSupport import TestCase
from . import categories_base as mod


class TestCategories(TestCase):
    def test_base_methods_grandparent_parent_child(self):

        with self.subTest("parent"):
            o = mod.OC_Category_P0.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP0 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP0 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP0 - method3 - P")
            self.assertEqual(o.gpMethod4(), "GP0 - method4 - GP")

            self.assertEqual(o.pMethod1(), "P0 - method1 - P")
            self.assertEqual(o.pMethod2(), "P0 - method2 - P")

        with self.subTest("grandparent"):
            o = mod.OC_Category_GP0.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP0 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP0 - method2 - GP")
            self.assertEqual(o.gpMethod3(), "GP0 - method3 - GP")
            self.assertEqual(o.gpMethod4(), "GP0 - method4 - GP")

        with self.subTest("child"):
            o = mod.OC_Category_C0.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP0 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP0 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP0 - method3 - C")
            self.assertEqual(o.gpMethod4(), "GP0 - method4 - C")

            self.assertEqual(o.pMethod1(), "P0 - method1 - P")
            self.assertEqual(o.pMethod2(), "P0 - method2 - C")

            self.assertEqual(o.method1(), "C0 - method1 - C")

    def test_base_methods_grandparent_child_parent(self):

        with self.subTest("child"):
            o = mod.OC_Category_C1.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP1 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP1 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP1 - method3 - C")
            self.assertEqual(o.gpMethod4(), "GP1 - method4 - C")

            self.assertEqual(o.pMethod1(), "P1 - method1 - P")
            self.assertEqual(o.pMethod2(), "P1 - method2 - C")

            self.assertEqual(o.method1(), "C1 - method1 - C")

        with self.subTest("parent"):
            o = mod.OC_Category_P1.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP1 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP1 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP1 - method3 - P")
            self.assertEqual(o.gpMethod4(), "GP1 - method4 - GP")

            self.assertEqual(o.pMethod1(), "P1 - method1 - P")
            self.assertEqual(o.pMethod2(), "P1 - method2 - P")

        with self.subTest("grandparent"):
            o = mod.OC_Category_GP1.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP1 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP1 - method2 - GP")
            self.assertEqual(o.gpMethod3(), "GP1 - method3 - GP")
            self.assertEqual(o.gpMethod4(), "GP1 - method4 - GP")

    def test_base_methods_parent_grandparent_child(self):

        with self.subTest("parent"):
            o = mod.OC_Category_P2.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP2 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP2 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP2 - method3 - P")
            self.assertEqual(o.gpMethod4(), "GP2 - method4 - GP")

            self.assertEqual(o.pMethod1(), "P2 - method1 - P")
            self.assertEqual(o.pMethod2(), "P2 - method2 - P")

        with self.subTest("grandparent"):
            o = mod.OC_Category_GP2.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP2 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP2 - method2 - GP")
            self.assertEqual(o.gpMethod3(), "GP2 - method3 - GP")
            self.assertEqual(o.gpMethod4(), "GP2 - method4 - GP")

        with self.subTest("child"):
            o = mod.OC_Category_C2.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP2 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP2 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP2 - method3 - C")
            self.assertEqual(o.gpMethod4(), "GP2 - method4 - C")

            self.assertEqual(o.pMethod1(), "P2 - method1 - P")
            self.assertEqual(o.pMethod2(), "P2 - method2 - C")

            self.assertEqual(o.method1(), "C2 - method1 - C")

    def test_base_methods_parent_child_grandparent(self):

        with self.subTest("parent"):
            o = mod.OC_Category_P3.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP3 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP3 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP3 - method3 - P")
            self.assertEqual(o.gpMethod4(), "GP3 - method4 - GP")

            self.assertEqual(o.pMethod1(), "P3 - method1 - P")
            self.assertEqual(o.pMethod2(), "P3 - method2 - P")

        with self.subTest("grandparent"):
            o = mod.OC_Category_GP3.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP3 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP3 - method2 - GP")
            self.assertEqual(o.gpMethod3(), "GP3 - method3 - GP")
            self.assertEqual(o.gpMethod4(), "GP3 - method4 - GP")

        with self.subTest("child"):
            o = mod.OC_Category_C3.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP3 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP3 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP3 - method3 - C")
            self.assertEqual(o.gpMethod4(), "GP3 - method4 - C")

            self.assertEqual(o.pMethod1(), "P3 - method1 - P")
            self.assertEqual(o.pMethod2(), "P3 - method2 - C")

            self.assertEqual(o.method1(), "C3 - method1 - C")

    def test_base_methods_child_grandparent_parent(self):
        with self.subTest("child"):
            o = mod.OC_Category_C4.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP4 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP4 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP4 - method3 - C")
            self.assertEqual(o.gpMethod4(), "GP4 - method4 - C")

            self.assertEqual(o.pMethod1(), "P4 - method1 - P")
            self.assertEqual(o.pMethod2(), "P4 - method2 - C")

            self.assertEqual(o.method1(), "C4 - method1 - C")

        with self.subTest("parent"):
            o = mod.OC_Category_P4.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP4 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP4 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP4 - method3 - P")
            self.assertEqual(o.gpMethod4(), "GP4 - method4 - GP")

            self.assertEqual(o.pMethod1(), "P4 - method1 - P")
            self.assertEqual(o.pMethod2(), "P4 - method2 - P")

        with self.subTest("grandparent"):
            o = mod.OC_Category_GP4.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP4 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP4 - method2 - GP")
            self.assertEqual(o.gpMethod3(), "GP4 - method3 - GP")
            self.assertEqual(o.gpMethod4(), "GP4 - method4 - GP")

    def test_base_methods_child_parent_grandparent(self):
        with self.subTest("child"):
            o = mod.OC_Category_C5.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP5 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP5 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP5 - method3 - C")
            self.assertEqual(o.gpMethod4(), "GP5 - method4 - C")

            self.assertEqual(o.pMethod1(), "P5 - method1 - P")
            self.assertEqual(o.pMethod2(), "P5 - method2 - C")

            self.assertEqual(o.method1(), "C5 - method1 - C")

        with self.subTest("parent"):
            o = mod.OC_Category_P5.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP5 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP5 - method2 - P")
            self.assertEqual(o.gpMethod3(), "GP5 - method3 - P")
            self.assertEqual(o.gpMethod4(), "GP5 - method4 - GP")

            self.assertEqual(o.pMethod1(), "P5 - method1 - P")
            self.assertEqual(o.pMethod2(), "P5 - method2 - P")

        with self.subTest("grandparent"):
            o = mod.OC_Category_GP5.alloc().init()
            self.assertEqual(o.gpMethod1(), "GP5 - method1 - GP")
            self.assertEqual(o.gpMethod2(), "GP5 - method2 - GP")
            self.assertEqual(o.gpMethod3(), "GP5 - method3 - GP")
            self.assertEqual(o.gpMethod4(), "GP5 - method4 - GP")

    def test_category_on_grandparent_before_inst_grandparent_parent_child(self):
        from . import category_gp6  # noqa: F401

        c = mod.OC_Category_C6.alloc().init()
        p = mod.OC_Category_P6.alloc().init()
        gp = mod.OC_Category_GP6.alloc().init()

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP6 - gpMethod1 - GP6(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP6 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP6 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP6 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP6 - gpMethod5 - GP6(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP6 - gpMethod1 - GP6(Cat)")
            self.assertEqual(p.gpMethod2(), "GP6 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP6 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP6 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP6 - gpMethod5 - GP6(Cat)")

            self.assertEqual(p.pMethod1(), "P6 - method1 - P")
            self.assertEqual(p.pMethod2(), "P6 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP6 - pMethod3 - GP6(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP6 - gpMethod1 - GP6(Cat)")
            self.assertEqual(c.gpMethod2(), "GP6 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP6 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP6 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP6 - gpMethod5 - GP6(Cat)")

            self.assertEqual(c.pMethod1(), "P6 - method1 - P")
            self.assertEqual(c.pMethod2(), "P6 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP6 - pMethod3 - GP6(Cat)")

            self.assertEqual(c.method1(), "C6 - method1 - C")
            self.assertEqual(c.method2(), "GP6 - method2 - GP6(Cat)")

    def test_category_on_grandparent_after_inst_grandparent_parent_child(self):
        c = mod.OC_Category_C7.alloc().init()
        p = mod.OC_Category_P7.alloc().init()
        gp = mod.OC_Category_GP7.alloc().init()

        from . import category_gp7  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP7 - gpMethod1 - GP7(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP7 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP7 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP7 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP7 - gpMethod5 - GP7(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP7 - gpMethod1 - GP7(Cat)")
            self.assertEqual(p.gpMethod2(), "GP7 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP7 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP7 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP7 - gpMethod5 - GP7(Cat)")

            self.assertEqual(p.pMethod1(), "P7 - method1 - P")
            self.assertEqual(p.pMethod2(), "P7 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP7 - pMethod3 - GP7(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP7 - gpMethod1 - GP7(Cat)")
            self.assertEqual(c.gpMethod2(), "GP7 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP7 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP7 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP7 - gpMethod5 - GP7(Cat)")

            self.assertEqual(c.pMethod1(), "P7 - method1 - P")
            self.assertEqual(c.pMethod2(), "P7 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP7 - pMethod3 - GP7(Cat)")

            self.assertEqual(c.method1(), "C7 - method1 - C")
            self.assertEqual(c.method2(), "GP7 - method2 - GP7(Cat)")

    def test_category_on_grandparent_after_calls_grandparent_parent_child(self):
        c = mod.OC_Category_C8.alloc().init()
        p = mod.OC_Category_P8.alloc().init()
        gp = mod.OC_Category_GP8.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_gp8  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP8 - gpMethod1 - GP8(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP8 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP8 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP8 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP8 - gpMethod5 - GP8(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP8 - gpMethod1 - GP8(Cat)")
            self.assertEqual(p.gpMethod2(), "GP8 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP8 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP8 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP8 - gpMethod5 - GP8(Cat)")

            self.assertEqual(p.pMethod1(), "P8 - method1 - P")
            self.assertEqual(p.pMethod2(), "P8 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP8 - pMethod3 - GP8(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP8 - gpMethod1 - GP8(Cat)")
            self.assertEqual(c.gpMethod2(), "GP8 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP8 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP8 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP8 - gpMethod5 - GP8(Cat)")

            self.assertEqual(c.pMethod1(), "P8 - method1 - P")
            self.assertEqual(c.pMethod2(), "P8 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP8 - pMethod3 - GP8(Cat)")

            self.assertEqual(c.method1(), "C8 - method1 - C")
            self.assertEqual(c.method2(), "GP8 - method2 - GP8(Cat)")

    def test_category_on_grandparent_before_inst_grandparent_child_parent(self):
        from . import category_gp9  # noqa: F401

        c = mod.OC_Category_C9.alloc().init()
        p = mod.OC_Category_P9.alloc().init()
        gp = mod.OC_Category_GP9.alloc().init()

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP9 - gpMethod1 - GP9(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP9 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP9 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP9 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP9 - gpMethod5 - GP9(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP9 - gpMethod1 - GP9(Cat)")
            self.assertEqual(c.gpMethod2(), "GP9 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP9 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP9 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP9 - gpMethod5 - GP9(Cat)")

            self.assertEqual(c.pMethod1(), "P9 - method1 - P")
            self.assertEqual(c.pMethod2(), "P9 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP9 - pMethod3 - GP9(Cat)")

            self.assertEqual(c.method1(), "C9 - method1 - C")
            self.assertEqual(c.method2(), "GP9 - method2 - GP9(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP9 - gpMethod1 - GP9(Cat)")
            self.assertEqual(p.gpMethod2(), "GP9 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP9 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP9 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP9 - gpMethod5 - GP9(Cat)")

            self.assertEqual(p.pMethod1(), "P9 - method1 - P")
            self.assertEqual(p.pMethod2(), "P9 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP9 - pMethod3 - GP9(Cat)")

    def test_category_on_grandparent_after_inst_grandparent_child_parent(self):
        c = mod.OC_Category_C10.alloc().init()
        p = mod.OC_Category_P10.alloc().init()
        gp = mod.OC_Category_GP10.alloc().init()

        from . import category_gp10  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP10 - gpMethod1 - GP10(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP10 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP10 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP10 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP10 - gpMethod5 - GP10(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP10 - gpMethod1 - GP10(Cat)")
            self.assertEqual(c.gpMethod2(), "GP10 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP10 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP10 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP10 - gpMethod5 - GP10(Cat)")

            self.assertEqual(c.pMethod1(), "P10 - method1 - P")
            self.assertEqual(c.pMethod2(), "P10 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP10 - pMethod3 - GP10(Cat)")

            self.assertEqual(c.method1(), "C10 - method1 - C")
            self.assertEqual(c.method2(), "GP10 - method2 - GP10(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP10 - gpMethod1 - GP10(Cat)")
            self.assertEqual(p.gpMethod2(), "GP10 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP10 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP10 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP10 - gpMethod5 - GP10(Cat)")

            self.assertEqual(p.pMethod1(), "P10 - method1 - P")
            self.assertEqual(p.pMethod2(), "P10 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP10 - pMethod3 - GP10(Cat)")

    def test_category_on_grandparent_after_calls_grandparent_child_parent(self):
        c = mod.OC_Category_C11.alloc().init()
        p = mod.OC_Category_P11.alloc().init()
        gp = mod.OC_Category_GP11.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_gp11  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP11 - gpMethod1 - GP11(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP11 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP11 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP11 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP11 - gpMethod5 - GP11(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP11 - gpMethod1 - GP11(Cat)")
            self.assertEqual(c.gpMethod2(), "GP11 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP11 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP11 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP11 - gpMethod5 - GP11(Cat)")

            self.assertEqual(c.pMethod1(), "P11 - method1 - P")
            self.assertEqual(c.pMethod2(), "P11 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP11 - pMethod3 - GP11(Cat)")

            self.assertEqual(c.method1(), "C11 - method1 - C")
            self.assertEqual(c.method2(), "GP11 - method2 - GP11(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP11 - gpMethod1 - GP11(Cat)")
            self.assertEqual(p.gpMethod2(), "GP11 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP11 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP11 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP11 - gpMethod5 - GP11(Cat)")

            self.assertEqual(p.pMethod1(), "P11 - method1 - P")
            self.assertEqual(p.pMethod2(), "P11 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP11 - pMethod3 - GP11(Cat)")

    def test_category_on_grandparent_before_inst_parent_grandparent_child(self):
        from . import category_gp12  # noqa: F401

        c = mod.OC_Category_C12.alloc().init()
        p = mod.OC_Category_P12.alloc().init()
        gp = mod.OC_Category_GP12.alloc().init()

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP12 - gpMethod1 - GP12(Cat)")
            self.assertEqual(p.gpMethod2(), "GP12 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP12 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP12 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP12 - gpMethod5 - GP12(Cat)")

            self.assertEqual(p.pMethod1(), "P12 - method1 - P")
            self.assertEqual(p.pMethod2(), "P12 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP12 - pMethod3 - GP12(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP12 - gpMethod1 - GP12(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP12 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP12 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP12 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP12 - gpMethod5 - GP12(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP12 - gpMethod1 - GP12(Cat)")
            self.assertEqual(c.gpMethod2(), "GP12 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP12 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP12 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP12 - gpMethod5 - GP12(Cat)")

            self.assertEqual(c.pMethod1(), "P12 - method1 - P")
            self.assertEqual(c.pMethod2(), "P12 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP12 - pMethod3 - GP12(Cat)")

            self.assertEqual(c.method1(), "C12 - method1 - C")
            self.assertEqual(c.method2(), "GP12 - method2 - GP12(Cat)")

    def test_category_on_grandparent_after_inst_parent_grandparent_child(self):
        c = mod.OC_Category_C13.alloc().init()
        p = mod.OC_Category_P13.alloc().init()
        gp = mod.OC_Category_GP13.alloc().init()

        from . import category_gp13  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP13 - gpMethod1 - GP13(Cat)")
            self.assertEqual(p.gpMethod2(), "GP13 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP13 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP13 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP13 - gpMethod5 - GP13(Cat)")

            self.assertEqual(p.pMethod1(), "P13 - method1 - P")
            self.assertEqual(p.pMethod2(), "P13 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP13 - pMethod3 - GP13(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP13 - gpMethod1 - GP13(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP13 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP13 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP13 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP13 - gpMethod5 - GP13(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP13 - gpMethod1 - GP13(Cat)")
            self.assertEqual(c.gpMethod2(), "GP13 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP13 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP13 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP13 - gpMethod5 - GP13(Cat)")

            self.assertEqual(c.pMethod1(), "P13 - method1 - P")
            self.assertEqual(c.pMethod2(), "P13 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP13 - pMethod3 - GP13(Cat)")

            self.assertEqual(c.method1(), "C13 - method1 - C")
            self.assertEqual(c.method2(), "GP13 - method2 - GP13(Cat)")

    def test_category_on_grandparent_after_calls_parent_grandparent_child(self):
        c = mod.OC_Category_C14.alloc().init()
        p = mod.OC_Category_P14.alloc().init()
        gp = mod.OC_Category_GP14.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_gp14  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP14 - gpMethod1 - GP14(Cat)")
            self.assertEqual(p.gpMethod2(), "GP14 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP14 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP14 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP14 - gpMethod5 - GP14(Cat)")

            self.assertEqual(p.pMethod1(), "P14 - method1 - P")
            self.assertEqual(p.pMethod2(), "P14 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP14 - pMethod3 - GP14(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP14 - gpMethod1 - GP14(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP14 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP14 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP14 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP14 - gpMethod5 - GP14(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP14 - gpMethod1 - GP14(Cat)")
            self.assertEqual(c.gpMethod2(), "GP14 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP14 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP14 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP14 - gpMethod5 - GP14(Cat)")

            self.assertEqual(c.pMethod1(), "P14 - method1 - P")
            self.assertEqual(c.pMethod2(), "P14 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP14 - pMethod3 - GP14(Cat)")

            self.assertEqual(c.method1(), "C14 - method1 - C")
            self.assertEqual(c.method2(), "GP14 - method2 - GP14(Cat)")

    def test_category_on_grandparent_before_inst_parent_child_grandparent(self):
        from . import category_gp15  # noqa: F401

        c = mod.OC_Category_C15.alloc().init()
        p = mod.OC_Category_P15.alloc().init()
        gp = mod.OC_Category_GP15.alloc().init()

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP15 - gpMethod1 - GP15(Cat)")
            self.assertEqual(p.gpMethod2(), "GP15 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP15 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP15 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP15 - gpMethod5 - GP15(Cat)")

            self.assertEqual(p.pMethod1(), "P15 - method1 - P")
            self.assertEqual(p.pMethod2(), "P15 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP15 - pMethod3 - GP15(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP15 - gpMethod1 - GP15(Cat)")
            self.assertEqual(c.gpMethod2(), "GP15 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP15 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP15 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP15 - gpMethod5 - GP15(Cat)")

            self.assertEqual(c.pMethod1(), "P15 - method1 - P")
            self.assertEqual(c.pMethod2(), "P15 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP15 - pMethod3 - GP15(Cat)")

            self.assertEqual(c.method1(), "C15 - method1 - C")
            self.assertEqual(c.method2(), "GP15 - method2 - GP15(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP15 - gpMethod1 - GP15(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP15 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP15 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP15 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP15 - gpMethod5 - GP15(Cat)")

    def test_category_on_grandparent_after_inst_parent_child_grandparent(self):
        c = mod.OC_Category_C16.alloc().init()
        p = mod.OC_Category_P16.alloc().init()
        gp = mod.OC_Category_GP16.alloc().init()

        from . import category_gp16  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP16 - gpMethod1 - GP16(Cat)")
            self.assertEqual(p.gpMethod2(), "GP16 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP16 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP16 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP16 - gpMethod5 - GP16(Cat)")

            self.assertEqual(p.pMethod1(), "P16 - method1 - P")
            self.assertEqual(p.pMethod2(), "P16 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP16 - pMethod3 - GP16(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP16 - gpMethod1 - GP16(Cat)")
            self.assertEqual(c.gpMethod2(), "GP16 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP16 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP16 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP16 - gpMethod5 - GP16(Cat)")

            self.assertEqual(c.pMethod1(), "P16 - method1 - P")
            self.assertEqual(c.pMethod2(), "P16 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP16 - pMethod3 - GP16(Cat)")

            self.assertEqual(c.method1(), "C16 - method1 - C")
            self.assertEqual(c.method2(), "GP16 - method2 - GP16(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP16 - gpMethod1 - GP16(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP16 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP16 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP16 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP16 - gpMethod5 - GP16(Cat)")

    def test_category_on_grandparent_after_calls_parent_child_grandparent(self):
        c = mod.OC_Category_C17.alloc().init()
        p = mod.OC_Category_P17.alloc().init()
        gp = mod.OC_Category_GP17.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_gp17  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP17 - gpMethod1 - GP17(Cat)")
            self.assertEqual(p.gpMethod2(), "GP17 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP17 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP17 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP17 - gpMethod5 - GP17(Cat)")

            self.assertEqual(p.pMethod1(), "P17 - method1 - P")
            self.assertEqual(p.pMethod2(), "P17 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP17 - pMethod3 - GP17(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP17 - gpMethod1 - GP17(Cat)")
            self.assertEqual(c.gpMethod2(), "GP17 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP17 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP17 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP17 - gpMethod5 - GP17(Cat)")

            self.assertEqual(c.pMethod1(), "P17 - method1 - P")
            self.assertEqual(c.pMethod2(), "P17 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP17 - pMethod3 - GP17(Cat)")

            self.assertEqual(c.method1(), "C17 - method1 - C")
            self.assertEqual(c.method2(), "GP17 - method2 - GP17(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP17 - gpMethod1 - GP17(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP17 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP17 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP17 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP17 - gpMethod5 - GP17(Cat)")

    def test_category_on_grandparent_before_inst_child_grandparent_parent(self):
        from . import category_gp18  # noqa: F401

        c = mod.OC_Category_C18.alloc().init()
        p = mod.OC_Category_P18.alloc().init()
        gp = mod.OC_Category_GP18.alloc().init()

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP18 - gpMethod1 - GP18(Cat)")
            self.assertEqual(c.gpMethod2(), "GP18 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP18 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP18 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP18 - gpMethod5 - GP18(Cat)")

            self.assertEqual(c.pMethod1(), "P18 - method1 - P")
            self.assertEqual(c.pMethod2(), "P18 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP18 - pMethod3 - GP18(Cat)")

            self.assertEqual(c.method1(), "C18 - method1 - C")
            self.assertEqual(c.method2(), "GP18 - method2 - GP18(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP18 - gpMethod1 - GP18(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP18 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP18 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP18 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP18 - gpMethod5 - GP18(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP18 - gpMethod1 - GP18(Cat)")
            self.assertEqual(p.gpMethod2(), "GP18 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP18 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP18 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP18 - gpMethod5 - GP18(Cat)")

            self.assertEqual(p.pMethod1(), "P18 - method1 - P")
            self.assertEqual(p.pMethod2(), "P18 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP18 - pMethod3 - GP18(Cat)")

    def test_category_on_grandparent_after_inst_child_grandparent_parent(self):
        c = mod.OC_Category_C19.alloc().init()
        p = mod.OC_Category_P19.alloc().init()
        gp = mod.OC_Category_GP19.alloc().init()

        from . import category_gp19  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP19 - gpMethod1 - GP19(Cat)")
            self.assertEqual(c.gpMethod2(), "GP19 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP19 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP19 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP19 - gpMethod5 - GP19(Cat)")

            self.assertEqual(c.pMethod1(), "P19 - method1 - P")
            self.assertEqual(c.pMethod2(), "P19 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP19 - pMethod3 - GP19(Cat)")

            self.assertEqual(c.method1(), "C19 - method1 - C")
            self.assertEqual(c.method2(), "GP19 - method2 - GP19(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP19 - gpMethod1 - GP19(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP19 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP19 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP19 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP19 - gpMethod5 - GP19(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP19 - gpMethod1 - GP19(Cat)")
            self.assertEqual(p.gpMethod2(), "GP19 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP19 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP19 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP19 - gpMethod5 - GP19(Cat)")

            self.assertEqual(p.pMethod1(), "P19 - method1 - P")
            self.assertEqual(p.pMethod2(), "P19 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP19 - pMethod3 - GP19(Cat)")

    def test_category_on_grandparent_after_calls_child_grandparent_parent(self):
        c = mod.OC_Category_C20.alloc().init()
        p = mod.OC_Category_P20.alloc().init()
        gp = mod.OC_Category_GP20.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_gp20  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP20 - gpMethod1 - GP20(Cat)")
            self.assertEqual(c.gpMethod2(), "GP20 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP20 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP20 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP20 - gpMethod5 - GP20(Cat)")

            self.assertEqual(c.pMethod1(), "P20 - method1 - P")
            self.assertEqual(c.pMethod2(), "P20 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP20 - pMethod3 - GP20(Cat)")

            self.assertEqual(c.method1(), "C20 - method1 - C")
            self.assertEqual(c.method2(), "GP20 - method2 - GP20(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP20 - gpMethod1 - GP20(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP20 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP20 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP20 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP20 - gpMethod5 - GP20(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP20 - gpMethod1 - GP20(Cat)")
            self.assertEqual(p.gpMethod2(), "GP20 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP20 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP20 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP20 - gpMethod5 - GP20(Cat)")

            self.assertEqual(p.pMethod1(), "P20 - method1 - P")
            self.assertEqual(p.pMethod2(), "P20 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP20 - pMethod3 - GP20(Cat)")

    def test_category_on_grandparent_before_inst_child_parent_grandparent(self):
        from . import category_gp21  # noqa: F401

        c = mod.OC_Category_C21.alloc().init()
        p = mod.OC_Category_P21.alloc().init()
        gp = mod.OC_Category_GP21.alloc().init()

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP21 - gpMethod1 - GP21(Cat)")
            self.assertEqual(c.gpMethod2(), "GP21 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP21 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP21 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP21 - gpMethod5 - GP21(Cat)")

            self.assertEqual(c.pMethod1(), "P21 - method1 - P")
            self.assertEqual(c.pMethod2(), "P21 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP21 - pMethod3 - GP21(Cat)")

            self.assertEqual(c.method1(), "C21 - method1 - C")
            self.assertEqual(c.method2(), "GP21 - method2 - GP21(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP21 - gpMethod1 - GP21(Cat)")
            self.assertEqual(p.gpMethod2(), "GP21 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP21 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP21 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP21 - gpMethod5 - GP21(Cat)")

            self.assertEqual(p.pMethod1(), "P21 - method1 - P")
            self.assertEqual(p.pMethod2(), "P21 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP21 - pMethod3 - GP21(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP21 - gpMethod1 - GP21(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP21 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP21 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP21 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP21 - gpMethod5 - GP21(Cat)")

    def test_category_on_grandparent_after_inst_child_parent_grandparent(self):
        c = mod.OC_Category_C22.alloc().init()
        p = mod.OC_Category_P22.alloc().init()
        gp = mod.OC_Category_GP22.alloc().init()

        from . import category_gp22  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP22 - gpMethod1 - GP22(Cat)")
            self.assertEqual(c.gpMethod2(), "GP22 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP22 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP22 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP22 - gpMethod5 - GP22(Cat)")

            self.assertEqual(c.pMethod1(), "P22 - method1 - P")
            self.assertEqual(c.pMethod2(), "P22 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP22 - pMethod3 - GP22(Cat)")

            self.assertEqual(c.method1(), "C22 - method1 - C")
            self.assertEqual(c.method2(), "GP22 - method2 - GP22(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP22 - gpMethod1 - GP22(Cat)")
            self.assertEqual(p.gpMethod2(), "GP22 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP22 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP22 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP22 - gpMethod5 - GP22(Cat)")

            self.assertEqual(p.pMethod1(), "P22 - method1 - P")
            self.assertEqual(p.pMethod2(), "P22 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP22 - pMethod3 - GP22(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP22 - gpMethod1 - GP22(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP22 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP22 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP22 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP22 - gpMethod5 - GP22(Cat)")

    def test_category_on_grandparent_after_calls_child_parent_grandparent(self):
        c = mod.OC_Category_C23.alloc().init()
        p = mod.OC_Category_P23.alloc().init()
        gp = mod.OC_Category_GP23.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_gp23  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "GP23 - gpMethod1 - GP23(Cat)")
            self.assertEqual(c.gpMethod2(), "GP23 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP23 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP23 - method4 - C")
            self.assertEqual(c.gpMethod5(), "GP23 - gpMethod5 - GP23(Cat)")

            self.assertEqual(c.pMethod1(), "P23 - method1 - P")
            self.assertEqual(c.pMethod2(), "P23 - method2 - C")
            self.assertEqual(c.pMethod3(), "GP23 - pMethod3 - GP23(Cat)")

            self.assertEqual(c.method1(), "C23 - method1 - C")
            self.assertEqual(c.method2(), "GP23 - method2 - GP23(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP23 - gpMethod1 - GP23(Cat)")
            self.assertEqual(p.gpMethod2(), "GP23 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP23 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP23 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "GP23 - gpMethod5 - GP23(Cat)")

            self.assertEqual(p.pMethod1(), "P23 - method1 - P")
            self.assertEqual(p.pMethod2(), "P23 - method2 - P")
            self.assertEqual(p.pMethod3(), "GP23 - pMethod3 - GP23(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP23 - gpMethod1 - GP23(Cat)")
            self.assertEqual(gp.gpMethod2(), "GP23 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP23 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP23 - method4 - GP")
            self.assertEqual(gp.gpMethod5(), "GP23 - gpMethod5 - GP23(Cat)")

    def test_category_on_parent_before_inst_grandparent_parent_child(self):
        from . import category_p24  # noqa: F401

        c = mod.OC_Category_C24.alloc().init()
        p = mod.OC_Category_P24.alloc().init()
        gp = mod.OC_Category_GP24.alloc().init()

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP24 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP24 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP24 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP24 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP24 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P24 - gpMethod1 - P24(Cat)")
            self.assertEqual(p.gpMethod2(), "GP24 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP24 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP24 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P24 - gpMethod5 - P24(Cat)")

            self.assertEqual(p.pMethod1(), "P24 - pMethod1 - P24(Cat)")
            self.assertEqual(p.pMethod2(), "P24 - method2 - P")
            self.assertEqual(p.pMethod3(), "P24 - pMethod3 - P24(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P24 - gpMethod1 - P24(Cat)")
            self.assertEqual(c.gpMethod2(), "GP24 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP24 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP24 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P24 - gpMethod5 - P24(Cat)")

            self.assertEqual(c.pMethod1(), "P24 - pMethod1 - P24(Cat)")
            self.assertEqual(c.pMethod2(), "P24 - method2 - C")
            self.assertEqual(c.pMethod3(), "P24 - pMethod3 - P24(Cat)")

            self.assertEqual(c.method1(), "C24 - method1 - C")
            self.assertEqual(c.method2(), "P24 - method2 - P24(Cat)")

    def test_category_on_parent_after_inst_grandparent_parent_child(self):
        c = mod.OC_Category_C25.alloc().init()
        p = mod.OC_Category_P25.alloc().init()
        gp = mod.OC_Category_GP25.alloc().init()

        from . import category_p25  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP25 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP25 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP25 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP25 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP25 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P25 - gpMethod1 - P25(Cat)")
            self.assertEqual(p.gpMethod2(), "GP25 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP25 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP25 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P25 - gpMethod5 - P25(Cat)")

            self.assertEqual(p.pMethod1(), "P25 - pMethod1 - P25(Cat)")
            self.assertEqual(p.pMethod2(), "P25 - method2 - P")
            self.assertEqual(p.pMethod3(), "P25 - pMethod3 - P25(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P25 - gpMethod1 - P25(Cat)")
            self.assertEqual(c.gpMethod2(), "GP25 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP25 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP25 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P25 - gpMethod5 - P25(Cat)")

            self.assertEqual(c.pMethod1(), "P25 - pMethod1 - P25(Cat)")
            self.assertEqual(c.pMethod2(), "P25 - method2 - C")
            self.assertEqual(c.pMethod3(), "P25 - pMethod3 - P25(Cat)")

            self.assertEqual(c.method1(), "C25 - method1 - C")
            self.assertEqual(c.method2(), "P25 - method2 - P25(Cat)")

    def test_category_on_parent_after_calls_grandparent_parent_child(self):
        c = mod.OC_Category_C26.alloc().init()
        p = mod.OC_Category_P26.alloc().init()
        gp = mod.OC_Category_GP26.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_p26  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP26 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP26 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP26 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP26 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP26 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P26 - gpMethod1 - P26(Cat)")
            self.assertEqual(p.gpMethod2(), "GP26 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP26 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP26 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P26 - gpMethod5 - P26(Cat)")

            self.assertEqual(p.pMethod1(), "P26 - pMethod1 - P26(Cat)")
            self.assertEqual(p.pMethod2(), "P26 - method2 - P")
            self.assertEqual(p.pMethod3(), "P26 - pMethod3 - P26(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P26 - gpMethod1 - P26(Cat)")
            self.assertEqual(c.gpMethod2(), "GP26 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP26 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP26 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P26 - gpMethod5 - P26(Cat)")

            self.assertEqual(c.pMethod1(), "P26 - pMethod1 - P26(Cat)")
            self.assertEqual(c.pMethod2(), "P26 - method2 - C")
            self.assertEqual(c.pMethod3(), "P26 - pMethod3 - P26(Cat)")

            self.assertEqual(c.method1(), "C26 - method1 - C")
            self.assertEqual(c.method2(), "P26 - method2 - P26(Cat)")

    def test_category_on_parent_before_inst_grandparent_child_parent(self):
        from . import category_p27  # noqa: F401

        c = mod.OC_Category_C27.alloc().init()
        p = mod.OC_Category_P27.alloc().init()
        gp = mod.OC_Category_GP27.alloc().init()

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP27 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP27 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP27 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP27 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP27 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P27 - gpMethod1 - P27(Cat)")
            self.assertEqual(c.gpMethod2(), "GP27 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP27 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP27 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P27 - gpMethod5 - P27(Cat)")

            self.assertEqual(c.pMethod1(), "P27 - pMethod1 - P27(Cat)")
            self.assertEqual(c.pMethod2(), "P27 - method2 - C")
            self.assertEqual(c.pMethod3(), "P27 - pMethod3 - P27(Cat)")

            self.assertEqual(c.method1(), "C27 - method1 - C")
            self.assertEqual(c.method2(), "P27 - method2 - P27(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P27 - gpMethod1 - P27(Cat)")
            self.assertEqual(p.gpMethod2(), "GP27 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP27 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP27 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P27 - gpMethod5 - P27(Cat)")

            self.assertEqual(p.pMethod1(), "P27 - pMethod1 - P27(Cat)")
            self.assertEqual(p.pMethod2(), "P27 - method2 - P")
            self.assertEqual(p.pMethod3(), "P27 - pMethod3 - P27(Cat)")

    def test_category_on_parent_after_inst_grandparent_child_parent(self):
        c = mod.OC_Category_C28.alloc().init()
        p = mod.OC_Category_P28.alloc().init()
        gp = mod.OC_Category_GP28.alloc().init()

        from . import category_p28  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP28 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP28 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP28 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP28 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP28 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P28 - gpMethod1 - P28(Cat)")
            self.assertEqual(c.gpMethod2(), "GP28 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP28 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP28 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P28 - gpMethod5 - P28(Cat)")

            self.assertEqual(c.pMethod1(), "P28 - pMethod1 - P28(Cat)")
            self.assertEqual(c.pMethod2(), "P28 - method2 - C")
            self.assertEqual(c.pMethod3(), "P28 - pMethod3 - P28(Cat)")

            self.assertEqual(c.method1(), "C28 - method1 - C")
            self.assertEqual(c.method2(), "P28 - method2 - P28(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P28 - gpMethod1 - P28(Cat)")
            self.assertEqual(p.gpMethod2(), "GP28 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP28 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP28 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P28 - gpMethod5 - P28(Cat)")

            self.assertEqual(p.pMethod1(), "P28 - pMethod1 - P28(Cat)")
            self.assertEqual(p.pMethod2(), "P28 - method2 - P")
            self.assertEqual(p.pMethod3(), "P28 - pMethod3 - P28(Cat)")

    def test_category_on_parent_after_calls_grandparent_child_parent(self):
        c = mod.OC_Category_C29.alloc().init()
        p = mod.OC_Category_P29.alloc().init()
        gp = mod.OC_Category_GP29.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_p29  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP29 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP29 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP29 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP29 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP29 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P29 - gpMethod1 - P29(Cat)")
            self.assertEqual(c.gpMethod2(), "GP29 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP29 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP29 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P29 - gpMethod5 - P29(Cat)")

            self.assertEqual(c.pMethod1(), "P29 - pMethod1 - P29(Cat)")
            self.assertEqual(c.pMethod2(), "P29 - method2 - C")
            self.assertEqual(c.pMethod3(), "P29 - pMethod3 - P29(Cat)")

            self.assertEqual(c.method1(), "C29 - method1 - C")
            self.assertEqual(c.method2(), "P29 - method2 - P29(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P29 - gpMethod1 - P29(Cat)")
            self.assertEqual(p.gpMethod2(), "GP29 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP29 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP29 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P29 - gpMethod5 - P29(Cat)")

            self.assertEqual(p.pMethod1(), "P29 - pMethod1 - P29(Cat)")
            self.assertEqual(p.pMethod2(), "P29 - method2 - P")
            self.assertEqual(p.pMethod3(), "P29 - pMethod3 - P29(Cat)")

    def test_category_on_parent_before_inst_parent_grandparent_child(self):
        from . import category_p30  # noqa: F401

        c = mod.OC_Category_C30.alloc().init()
        p = mod.OC_Category_P30.alloc().init()
        gp = mod.OC_Category_GP30.alloc().init()

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P30 - gpMethod1 - P30(Cat)")
            self.assertEqual(p.gpMethod2(), "GP30 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP30 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP30 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P30 - gpMethod5 - P30(Cat)")

            self.assertEqual(p.pMethod1(), "P30 - pMethod1 - P30(Cat)")
            self.assertEqual(p.pMethod2(), "P30 - method2 - P")
            self.assertEqual(p.pMethod3(), "P30 - pMethod3 - P30(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP30 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP30 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP30 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP30 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP30 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P30 - gpMethod1 - P30(Cat)")
            self.assertEqual(c.gpMethod2(), "GP30 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP30 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP30 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P30 - gpMethod5 - P30(Cat)")

            self.assertEqual(c.pMethod1(), "P30 - pMethod1 - P30(Cat)")
            self.assertEqual(c.pMethod2(), "P30 - method2 - C")
            self.assertEqual(c.pMethod3(), "P30 - pMethod3 - P30(Cat)")

            self.assertEqual(c.method1(), "C30 - method1 - C")
            self.assertEqual(c.method2(), "P30 - method2 - P30(Cat)")

    def test_category_on_parent_after_inst_parent_grandparent_child(self):
        c = mod.OC_Category_C31.alloc().init()
        p = mod.OC_Category_P31.alloc().init()
        gp = mod.OC_Category_GP31.alloc().init()

        from . import category_p31  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P31 - gpMethod1 - P31(Cat)")
            self.assertEqual(p.gpMethod2(), "GP31 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP31 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP31 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P31 - gpMethod5 - P31(Cat)")

            self.assertEqual(p.pMethod1(), "P31 - pMethod1 - P31(Cat)")
            self.assertEqual(p.pMethod2(), "P31 - method2 - P")
            self.assertEqual(p.pMethod3(), "P31 - pMethod3 - P31(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP31 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP31 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP31 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP31 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP31 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P31 - gpMethod1 - P31(Cat)")
            self.assertEqual(c.gpMethod2(), "GP31 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP31 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP31 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P31 - gpMethod5 - P31(Cat)")

            self.assertEqual(c.pMethod1(), "P31 - pMethod1 - P31(Cat)")
            self.assertEqual(c.pMethod2(), "P31 - method2 - C")
            self.assertEqual(c.pMethod3(), "P31 - pMethod3 - P31(Cat)")

            self.assertEqual(c.method1(), "C31 - method1 - C")
            self.assertEqual(c.method2(), "P31 - method2 - P31(Cat)")

    def test_category_on_parent_after_calls_parent_grandparent_child(self):
        c = mod.OC_Category_C32.alloc().init()
        p = mod.OC_Category_P32.alloc().init()
        gp = mod.OC_Category_GP32.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_p32  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P32 - gpMethod1 - P32(Cat)")
            self.assertEqual(p.gpMethod2(), "GP32 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP32 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP32 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P32 - gpMethod5 - P32(Cat)")

            self.assertEqual(p.pMethod1(), "P32 - pMethod1 - P32(Cat)")
            self.assertEqual(p.pMethod2(), "P32 - method2 - P")
            self.assertEqual(p.pMethod3(), "P32 - pMethod3 - P32(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP32 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP32 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP32 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP32 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP32 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P32 - gpMethod1 - P32(Cat)")
            self.assertEqual(c.gpMethod2(), "GP32 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP32 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP32 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P32 - gpMethod5 - P32(Cat)")

            self.assertEqual(c.pMethod1(), "P32 - pMethod1 - P32(Cat)")
            self.assertEqual(c.pMethod2(), "P32 - method2 - C")
            self.assertEqual(c.pMethod3(), "P32 - pMethod3 - P32(Cat)")

            self.assertEqual(c.method1(), "C32 - method1 - C")
            self.assertEqual(c.method2(), "P32 - method2 - P32(Cat)")

    def test_category_on_parent_before_inst_parent_child_grandparent(self):
        from . import category_p33  # noqa: F401

        c = mod.OC_Category_C33.alloc().init()
        p = mod.OC_Category_P33.alloc().init()
        gp = mod.OC_Category_GP33.alloc().init()

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P33 - gpMethod1 - P33(Cat)")
            self.assertEqual(p.gpMethod2(), "GP33 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP33 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP33 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P33 - gpMethod5 - P33(Cat)")

            self.assertEqual(p.pMethod1(), "P33 - pMethod1 - P33(Cat)")
            self.assertEqual(p.pMethod2(), "P33 - method2 - P")
            self.assertEqual(p.pMethod3(), "P33 - pMethod3 - P33(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P33 - gpMethod1 - P33(Cat)")
            self.assertEqual(c.gpMethod2(), "GP33 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP33 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP33 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P33 - gpMethod5 - P33(Cat)")

            self.assertEqual(c.pMethod1(), "P33 - pMethod1 - P33(Cat)")
            self.assertEqual(c.pMethod2(), "P33 - method2 - C")
            self.assertEqual(c.pMethod3(), "P33 - pMethod3 - P33(Cat)")

            self.assertEqual(c.method1(), "C33 - method1 - C")
            self.assertEqual(c.method2(), "P33 - method2 - P33(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP33 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP33 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP33 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP33 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP33 - method5 - GP")

    def test_category_on_parent_after_inst_parent_child_grandparent(self):
        c = mod.OC_Category_C34.alloc().init()
        p = mod.OC_Category_P34.alloc().init()
        gp = mod.OC_Category_GP34.alloc().init()

        from . import category_p34  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P34 - gpMethod1 - P34(Cat)")
            self.assertEqual(p.gpMethod2(), "GP34 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP34 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP34 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P34 - gpMethod5 - P34(Cat)")

            self.assertEqual(p.pMethod1(), "P34 - pMethod1 - P34(Cat)")
            self.assertEqual(p.pMethod2(), "P34 - method2 - P")
            self.assertEqual(p.pMethod3(), "P34 - pMethod3 - P34(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P34 - gpMethod1 - P34(Cat)")
            self.assertEqual(c.gpMethod2(), "GP34 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP34 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP34 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P34 - gpMethod5 - P34(Cat)")

            self.assertEqual(c.pMethod1(), "P34 - pMethod1 - P34(Cat)")
            self.assertEqual(c.pMethod2(), "P34 - method2 - C")
            self.assertEqual(c.pMethod3(), "P34 - pMethod3 - P34(Cat)")

            self.assertEqual(c.method1(), "C34 - method1 - C")
            self.assertEqual(c.method2(), "P34 - method2 - P34(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP34 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP34 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP34 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP34 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP34 - method5 - GP")

    def test_category_on_parent_after_calls_parent_child_grandparent(self):
        c = mod.OC_Category_C35.alloc().init()
        p = mod.OC_Category_P35.alloc().init()
        gp = mod.OC_Category_GP35.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_p35  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P35 - gpMethod1 - P35(Cat)")
            self.assertEqual(p.gpMethod2(), "GP35 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP35 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP35 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P35 - gpMethod5 - P35(Cat)")

            self.assertEqual(p.pMethod1(), "P35 - pMethod1 - P35(Cat)")
            self.assertEqual(p.pMethod2(), "P35 - method2 - P")
            self.assertEqual(p.pMethod3(), "P35 - pMethod3 - P35(Cat)")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P35 - gpMethod1 - P35(Cat)")
            self.assertEqual(c.gpMethod2(), "GP35 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP35 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP35 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P35 - gpMethod5 - P35(Cat)")

            self.assertEqual(c.pMethod1(), "P35 - pMethod1 - P35(Cat)")
            self.assertEqual(c.pMethod2(), "P35 - method2 - C")
            self.assertEqual(c.pMethod3(), "P35 - pMethod3 - P35(Cat)")

            self.assertEqual(c.method1(), "C35 - method1 - C")
            self.assertEqual(c.method2(), "P35 - method2 - P35(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP35 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP35 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP35 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP35 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP35 - method5 - GP")

    def test_category_on_parent_before_inst_child_grandparent_parent(self):
        from . import category_p36  # noqa: F401

        c = mod.OC_Category_C36.alloc().init()
        p = mod.OC_Category_P36.alloc().init()
        gp = mod.OC_Category_GP36.alloc().init()

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P36 - gpMethod1 - P36(Cat)")
            self.assertEqual(c.gpMethod2(), "GP36 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP36 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP36 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P36 - gpMethod5 - P36(Cat)")

            self.assertEqual(c.pMethod1(), "P36 - pMethod1 - P36(Cat)")
            self.assertEqual(c.pMethod2(), "P36 - method2 - C")
            self.assertEqual(c.pMethod3(), "P36 - pMethod3 - P36(Cat)")

            self.assertEqual(c.method1(), "C36 - method1 - C")
            self.assertEqual(c.method2(), "P36 - method2 - P36(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP36 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP36 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP36 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP36 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP36 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P36 - gpMethod1 - P36(Cat)")
            self.assertEqual(p.gpMethod2(), "GP36 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP36 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP36 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P36 - gpMethod5 - P36(Cat)")

            self.assertEqual(p.pMethod1(), "P36 - pMethod1 - P36(Cat)")
            self.assertEqual(p.pMethod2(), "P36 - method2 - P")
            self.assertEqual(p.pMethod3(), "P36 - pMethod3 - P36(Cat)")

    def test_category_on_parent_after_inst_child_grandparent_parent(self):
        c = mod.OC_Category_C37.alloc().init()
        p = mod.OC_Category_P37.alloc().init()
        gp = mod.OC_Category_GP37.alloc().init()

        from . import category_p37  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P37 - gpMethod1 - P37(Cat)")
            self.assertEqual(c.gpMethod2(), "GP37 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP37 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP37 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P37 - gpMethod5 - P37(Cat)")

            self.assertEqual(c.pMethod1(), "P37 - pMethod1 - P37(Cat)")
            self.assertEqual(c.pMethod2(), "P37 - method2 - C")
            self.assertEqual(c.pMethod3(), "P37 - pMethod3 - P37(Cat)")

            self.assertEqual(c.method1(), "C37 - method1 - C")
            self.assertEqual(c.method2(), "P37 - method2 - P37(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP37 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP37 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP37 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP37 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP37 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P37 - gpMethod1 - P37(Cat)")
            self.assertEqual(p.gpMethod2(), "GP37 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP37 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP37 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P37 - gpMethod5 - P37(Cat)")

            self.assertEqual(p.pMethod1(), "P37 - pMethod1 - P37(Cat)")
            self.assertEqual(p.pMethod2(), "P37 - method2 - P")
            self.assertEqual(p.pMethod3(), "P37 - pMethod3 - P37(Cat)")

    def test_category_on_parent_after_calls_child_grandparent_parent(self):
        c = mod.OC_Category_C38.alloc().init()
        p = mod.OC_Category_P38.alloc().init()
        gp = mod.OC_Category_GP38.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_p38  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P38 - gpMethod1 - P38(Cat)")
            self.assertEqual(c.gpMethod2(), "GP38 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP38 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP38 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P38 - gpMethod5 - P38(Cat)")

            self.assertEqual(c.pMethod1(), "P38 - pMethod1 - P38(Cat)")
            self.assertEqual(c.pMethod2(), "P38 - method2 - C")
            self.assertEqual(c.pMethod3(), "P38 - pMethod3 - P38(Cat)")

            self.assertEqual(c.method1(), "C38 - method1 - C")
            self.assertEqual(c.method2(), "P38 - method2 - P38(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP38 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP38 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP38 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP38 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP38 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P38 - gpMethod1 - P38(Cat)")
            self.assertEqual(p.gpMethod2(), "GP38 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP38 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP38 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P38 - gpMethod5 - P38(Cat)")

            self.assertEqual(p.pMethod1(), "P38 - pMethod1 - P38(Cat)")
            self.assertEqual(p.pMethod2(), "P38 - method2 - P")
            self.assertEqual(p.pMethod3(), "P38 - pMethod3 - P38(Cat)")

    def test_category_on_parent_before_inst_child_parent_grandparent(self):
        from . import category_p39  # noqa: F401

        c = mod.OC_Category_C39.alloc().init()
        p = mod.OC_Category_P39.alloc().init()
        gp = mod.OC_Category_GP39.alloc().init()

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P39 - gpMethod1 - P39(Cat)")
            self.assertEqual(c.gpMethod2(), "GP39 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP39 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP39 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P39 - gpMethod5 - P39(Cat)")

            self.assertEqual(c.pMethod1(), "P39 - pMethod1 - P39(Cat)")
            self.assertEqual(c.pMethod2(), "P39 - method2 - C")
            self.assertEqual(c.pMethod3(), "P39 - pMethod3 - P39(Cat)")

            self.assertEqual(c.method1(), "C39 - method1 - C")
            self.assertEqual(c.method2(), "P39 - method2 - P39(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P39 - gpMethod1 - P39(Cat)")
            self.assertEqual(p.gpMethod2(), "GP39 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP39 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP39 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P39 - gpMethod5 - P39(Cat)")

            self.assertEqual(p.pMethod1(), "P39 - pMethod1 - P39(Cat)")
            self.assertEqual(p.pMethod2(), "P39 - method2 - P")
            self.assertEqual(p.pMethod3(), "P39 - pMethod3 - P39(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP39 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP39 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP39 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP39 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP39 - method5 - GP")

    def test_category_on_parent_after_inst_child_parent_grandparent(self):
        c = mod.OC_Category_C40.alloc().init()
        p = mod.OC_Category_P40.alloc().init()
        gp = mod.OC_Category_GP40.alloc().init()

        from . import category_p40  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P40 - gpMethod1 - P40(Cat)")
            self.assertEqual(c.gpMethod2(), "GP40 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP40 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP40 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P40 - gpMethod5 - P40(Cat)")

            self.assertEqual(c.pMethod1(), "P40 - pMethod1 - P40(Cat)")
            self.assertEqual(c.pMethod2(), "P40 - method2 - C")
            self.assertEqual(c.pMethod3(), "P40 - pMethod3 - P40(Cat)")

            self.assertEqual(c.method1(), "C40 - method1 - C")
            self.assertEqual(c.method2(), "P40 - method2 - P40(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P40 - gpMethod1 - P40(Cat)")
            self.assertEqual(p.gpMethod2(), "GP40 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP40 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP40 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P40 - gpMethod5 - P40(Cat)")

            self.assertEqual(p.pMethod1(), "P40 - pMethod1 - P40(Cat)")
            self.assertEqual(p.pMethod2(), "P40 - method2 - P")
            self.assertEqual(p.pMethod3(), "P40 - pMethod3 - P40(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP40 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP40 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP40 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP40 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP40 - method5 - GP")

    def test_category_on_parent_after_calls_child_parent_grandparent(self):
        c = mod.OC_Category_C41.alloc().init()
        p = mod.OC_Category_P41.alloc().init()
        gp = mod.OC_Category_GP41.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_p41  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "P41 - gpMethod1 - P41(Cat)")
            self.assertEqual(c.gpMethod2(), "GP41 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP41 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP41 - method4 - C")
            self.assertEqual(c.gpMethod5(), "P41 - gpMethod5 - P41(Cat)")

            self.assertEqual(c.pMethod1(), "P41 - pMethod1 - P41(Cat)")
            self.assertEqual(c.pMethod2(), "P41 - method2 - C")
            self.assertEqual(c.pMethod3(), "P41 - pMethod3 - P41(Cat)")

            self.assertEqual(c.method1(), "C41 - method1 - C")
            self.assertEqual(c.method2(), "P41 - method2 - P41(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "P41 - gpMethod1 - P41(Cat)")
            self.assertEqual(p.gpMethod2(), "GP41 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP41 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP41 - method4 - GP")
            self.assertEqual(p.gpMethod5(), "P41 - gpMethod5 - P41(Cat)")

            self.assertEqual(p.pMethod1(), "P41 - pMethod1 - P41(Cat)")
            self.assertEqual(p.pMethod2(), "P41 - method2 - P")
            self.assertEqual(p.pMethod3(), "P41 - pMethod3 - P41(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP41 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP41 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP41 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP41 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP41 - method5 - GP")

    def test_category_on_child_before_inst_grandparent_parent_child(self):
        from . import category_c42  # noqa: F401

        c = mod.OC_Category_C42.alloc().init()
        p = mod.OC_Category_P42.alloc().init()
        gp = mod.OC_Category_GP42.alloc().init()

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP42 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP42 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP42 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP42 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP42 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP42 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP42 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP42 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP42 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP42 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P42 - method1 - P")
            self.assertEqual(p.pMethod2(), "P42 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P42 - method3 - P")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C42 - gpMethod1 - C42(Cat)")
            self.assertEqual(c.gpMethod2(), "GP42 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP42 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP42 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C42 - gpMethod5 - C42(Cat)")

            self.assertEqual(c.pMethod1(), "C42 - pMethod1 - C42(Cat)")
            self.assertEqual(c.pMethod2(), "P42 - method2 - C")
            self.assertEqual(c.pMethod3(), "C42 - pMethod3 - C42(Cat)")

            self.assertEqual(c.method1(), "C42 - method1 - C42(Cat)")
            self.assertEqual(c.method2(), "C42 - method2 - C42(Cat)")

    def test_category_on_child_after_inst_grandparent_parent_child(self):
        c = mod.OC_Category_C43.alloc().init()
        p = mod.OC_Category_P43.alloc().init()
        gp = mod.OC_Category_GP43.alloc().init()

        from . import category_c43  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP43 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP43 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP43 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP43 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP43 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP43 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP43 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP43 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP43 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP43 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P43 - method1 - P")
            self.assertEqual(p.pMethod2(), "P43 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P43 - method3 - P")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C43 - gpMethod1 - C43(Cat)")
            self.assertEqual(c.gpMethod2(), "GP43 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP43 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP43 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C43 - gpMethod5 - C43(Cat)")

            self.assertEqual(c.pMethod1(), "C43 - pMethod1 - C43(Cat)")
            self.assertEqual(c.pMethod2(), "P43 - method2 - C")
            self.assertEqual(c.pMethod3(), "C43 - pMethod3 - C43(Cat)")

            self.assertEqual(c.method1(), "C43 - method1 - C43(Cat)")
            self.assertEqual(c.method2(), "C43 - method2 - C43(Cat)")

    def test_category_on_child_after_calls_grandparent_parent_child(self):
        c = mod.OC_Category_C44.alloc().init()
        p = mod.OC_Category_P44.alloc().init()
        gp = mod.OC_Category_GP44.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_c44  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP44 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP44 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP44 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP44 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP44 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP44 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP44 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP44 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP44 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP44 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P44 - method1 - P")
            self.assertEqual(p.pMethod2(), "P44 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P44 - method3 - P")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C44 - gpMethod1 - C44(Cat)")
            self.assertEqual(c.gpMethod2(), "GP44 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP44 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP44 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C44 - gpMethod5 - C44(Cat)")

            self.assertEqual(c.pMethod1(), "C44 - pMethod1 - C44(Cat)")
            self.assertEqual(c.pMethod2(), "P44 - method2 - C")
            self.assertEqual(c.pMethod3(), "C44 - pMethod3 - C44(Cat)")

            self.assertEqual(c.method1(), "C44 - method1 - C44(Cat)")
            self.assertEqual(c.method2(), "C44 - method2 - C44(Cat)")

    def test_category_on_child_before_inst_grandparent_child_parent(self):
        from . import category_c45  # noqa: F401

        c = mod.OC_Category_C45.alloc().init()
        p = mod.OC_Category_P45.alloc().init()
        gp = mod.OC_Category_GP45.alloc().init()

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP45 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP45 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP45 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP45 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP45 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C45 - gpMethod1 - C45(Cat)")
            self.assertEqual(c.gpMethod2(), "GP45 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP45 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP45 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C45 - gpMethod5 - C45(Cat)")

            self.assertEqual(c.pMethod1(), "C45 - pMethod1 - C45(Cat)")
            self.assertEqual(c.pMethod2(), "P45 - method2 - C")
            self.assertEqual(c.pMethod3(), "C45 - pMethod3 - C45(Cat)")

            self.assertEqual(c.method1(), "C45 - method1 - C45(Cat)")
            self.assertEqual(c.method2(), "C45 - method2 - C45(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP45 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP45 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP45 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP45 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP45 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P45 - method1 - P")
            self.assertEqual(p.pMethod2(), "P45 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P45 - method3 - P")

    def test_category_on_child_after_inst_grandparent_child_parent(self):
        c = mod.OC_Category_C46.alloc().init()
        p = mod.OC_Category_P46.alloc().init()
        gp = mod.OC_Category_GP46.alloc().init()

        from . import category_c46  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP46 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP46 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP46 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP46 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP46 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C46 - gpMethod1 - C46(Cat)")
            self.assertEqual(c.gpMethod2(), "GP46 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP46 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP46 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C46 - gpMethod5 - C46(Cat)")

            self.assertEqual(c.pMethod1(), "C46 - pMethod1 - C46(Cat)")
            self.assertEqual(c.pMethod2(), "P46 - method2 - C")
            self.assertEqual(c.pMethod3(), "C46 - pMethod3 - C46(Cat)")

            self.assertEqual(c.method1(), "C46 - method1 - C46(Cat)")
            self.assertEqual(c.method2(), "C46 - method2 - C46(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP46 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP46 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP46 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP46 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP46 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P46 - method1 - P")
            self.assertEqual(p.pMethod2(), "P46 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P46 - method3 - P")

    def test_category_on_child_after_calls_grandparent_child_parent(self):
        c = mod.OC_Category_C47.alloc().init()
        p = mod.OC_Category_P47.alloc().init()
        gp = mod.OC_Category_GP47.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_c47  # noqa: F401

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP47 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP47 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP47 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP47 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP47 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C47 - gpMethod1 - C47(Cat)")
            self.assertEqual(c.gpMethod2(), "GP47 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP47 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP47 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C47 - gpMethod5 - C47(Cat)")

            self.assertEqual(c.pMethod1(), "C47 - pMethod1 - C47(Cat)")
            self.assertEqual(c.pMethod2(), "P47 - method2 - C")
            self.assertEqual(c.pMethod3(), "C47 - pMethod3 - C47(Cat)")

            self.assertEqual(c.method1(), "C47 - method1 - C47(Cat)")
            self.assertEqual(c.method2(), "C47 - method2 - C47(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP47 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP47 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP47 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP47 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP47 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P47 - method1 - P")
            self.assertEqual(p.pMethod2(), "P47 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P47 - method3 - P")

    def test_category_on_child_before_inst_parent_grandparent_child(self):
        from . import category_c48  # noqa: F401

        c = mod.OC_Category_C48.alloc().init()
        p = mod.OC_Category_P48.alloc().init()
        gp = mod.OC_Category_GP48.alloc().init()

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP48 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP48 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP48 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP48 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP48 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P48 - method1 - P")
            self.assertEqual(p.pMethod2(), "P48 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P48 - method3 - P")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP48 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP48 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP48 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP48 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP48 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C48 - gpMethod1 - C48(Cat)")
            self.assertEqual(c.gpMethod2(), "GP48 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP48 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP48 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C48 - gpMethod5 - C48(Cat)")

            self.assertEqual(c.pMethod1(), "C48 - pMethod1 - C48(Cat)")
            self.assertEqual(c.pMethod2(), "P48 - method2 - C")
            self.assertEqual(c.pMethod3(), "C48 - pMethod3 - C48(Cat)")

            self.assertEqual(c.method1(), "C48 - method1 - C48(Cat)")
            self.assertEqual(c.method2(), "C48 - method2 - C48(Cat)")

    def test_category_on_child_after_inst_parent_grandparent_child(self):
        c = mod.OC_Category_C49.alloc().init()
        p = mod.OC_Category_P49.alloc().init()
        gp = mod.OC_Category_GP49.alloc().init()

        from . import category_c49  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP49 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP49 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP49 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP49 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP49 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P49 - method1 - P")
            self.assertEqual(p.pMethod2(), "P49 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P49 - method3 - P")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP49 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP49 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP49 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP49 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP49 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C49 - gpMethod1 - C49(Cat)")
            self.assertEqual(c.gpMethod2(), "GP49 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP49 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP49 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C49 - gpMethod5 - C49(Cat)")

            self.assertEqual(c.pMethod1(), "C49 - pMethod1 - C49(Cat)")
            self.assertEqual(c.pMethod2(), "P49 - method2 - C")
            self.assertEqual(c.pMethod3(), "C49 - pMethod3 - C49(Cat)")

            self.assertEqual(c.method1(), "C49 - method1 - C49(Cat)")
            self.assertEqual(c.method2(), "C49 - method2 - C49(Cat)")

    def test_category_on_child_after_calls_parent_grandparent_child(self):
        c = mod.OC_Category_C50.alloc().init()
        p = mod.OC_Category_P50.alloc().init()
        gp = mod.OC_Category_GP50.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_c50  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP50 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP50 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP50 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP50 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP50 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P50 - method1 - P")
            self.assertEqual(p.pMethod2(), "P50 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P50 - method3 - P")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP50 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP50 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP50 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP50 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP50 - method5 - GP")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C50 - gpMethod1 - C50(Cat)")
            self.assertEqual(c.gpMethod2(), "GP50 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP50 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP50 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C50 - gpMethod5 - C50(Cat)")

            self.assertEqual(c.pMethod1(), "C50 - pMethod1 - C50(Cat)")
            self.assertEqual(c.pMethod2(), "P50 - method2 - C")
            self.assertEqual(c.pMethod3(), "C50 - pMethod3 - C50(Cat)")

            self.assertEqual(c.method1(), "C50 - method1 - C50(Cat)")
            self.assertEqual(c.method2(), "C50 - method2 - C50(Cat)")

    def test_category_on_child_before_inst_parent_child_grandparent(self):
        from . import category_c51  # noqa: F401

        c = mod.OC_Category_C51.alloc().init()
        p = mod.OC_Category_P51.alloc().init()
        gp = mod.OC_Category_GP51.alloc().init()

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP51 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP51 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP51 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP51 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP51 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P51 - method1 - P")
            self.assertEqual(p.pMethod2(), "P51 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P51 - method3 - P")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C51 - gpMethod1 - C51(Cat)")
            self.assertEqual(c.gpMethod2(), "GP51 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP51 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP51 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C51 - gpMethod5 - C51(Cat)")

            self.assertEqual(c.pMethod1(), "C51 - pMethod1 - C51(Cat)")
            self.assertEqual(c.pMethod2(), "P51 - method2 - C")
            self.assertEqual(c.pMethod3(), "C51 - pMethod3 - C51(Cat)")

            self.assertEqual(c.method1(), "C51 - method1 - C51(Cat)")
            self.assertEqual(c.method2(), "C51 - method2 - C51(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP51 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP51 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP51 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP51 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP51 - method5 - GP")

    def test_category_on_child_after_inst_parent_child_grandparent(self):
        c = mod.OC_Category_C52.alloc().init()
        p = mod.OC_Category_P52.alloc().init()
        gp = mod.OC_Category_GP52.alloc().init()

        from . import category_c52  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP52 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP52 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP52 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP52 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP52 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P52 - method1 - P")
            self.assertEqual(p.pMethod2(), "P52 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P52 - method3 - P")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C52 - gpMethod1 - C52(Cat)")
            self.assertEqual(c.gpMethod2(), "GP52 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP52 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP52 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C52 - gpMethod5 - C52(Cat)")

            self.assertEqual(c.pMethod1(), "C52 - pMethod1 - C52(Cat)")
            self.assertEqual(c.pMethod2(), "P52 - method2 - C")
            self.assertEqual(c.pMethod3(), "C52 - pMethod3 - C52(Cat)")

            self.assertEqual(c.method1(), "C52 - method1 - C52(Cat)")
            self.assertEqual(c.method2(), "C52 - method2 - C52(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP52 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP52 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP52 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP52 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP52 - method5 - GP")

    def test_category_on_child_after_calls_parent_child_grandparent(self):
        c = mod.OC_Category_C53.alloc().init()
        p = mod.OC_Category_P53.alloc().init()
        gp = mod.OC_Category_GP53.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_c53  # noqa: F401

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP53 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP53 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP53 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP53 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP53 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P53 - method1 - P")
            self.assertEqual(p.pMethod2(), "P53 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P53 - method3 - P")

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C53 - gpMethod1 - C53(Cat)")
            self.assertEqual(c.gpMethod2(), "GP53 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP53 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP53 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C53 - gpMethod5 - C53(Cat)")

            self.assertEqual(c.pMethod1(), "C53 - pMethod1 - C53(Cat)")
            self.assertEqual(c.pMethod2(), "P53 - method2 - C")
            self.assertEqual(c.pMethod3(), "C53 - pMethod3 - C53(Cat)")

            self.assertEqual(c.method1(), "C53 - method1 - C53(Cat)")
            self.assertEqual(c.method2(), "C53 - method2 - C53(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP53 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP53 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP53 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP53 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP53 - method5 - GP")

    def test_category_on_child_before_inst_child_grandparent_parent(self):
        from . import category_c54  # noqa: F401

        c = mod.OC_Category_C54.alloc().init()
        p = mod.OC_Category_P54.alloc().init()
        gp = mod.OC_Category_GP54.alloc().init()

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C54 - gpMethod1 - C54(Cat)")
            self.assertEqual(c.gpMethod2(), "GP54 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP54 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP54 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C54 - gpMethod5 - C54(Cat)")

            self.assertEqual(c.pMethod1(), "C54 - pMethod1 - C54(Cat)")
            self.assertEqual(c.pMethod2(), "P54 - method2 - C")
            self.assertEqual(c.pMethod3(), "C54 - pMethod3 - C54(Cat)")

            self.assertEqual(c.method1(), "C54 - method1 - C54(Cat)")
            self.assertEqual(c.method2(), "C54 - method2 - C54(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP54 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP54 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP54 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP54 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP54 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP54 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP54 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP54 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP54 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP54 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P54 - method1 - P")
            self.assertEqual(p.pMethod2(), "P54 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P54 - method3 - P")

    def test_category_on_child_after_inst_child_grandparent_parent(self):
        c = mod.OC_Category_C55.alloc().init()
        p = mod.OC_Category_P55.alloc().init()
        gp = mod.OC_Category_GP55.alloc().init()

        from . import category_c55  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C55 - gpMethod1 - C55(Cat)")
            self.assertEqual(c.gpMethod2(), "GP55 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP55 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP55 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C55 - gpMethod5 - C55(Cat)")

            self.assertEqual(c.pMethod1(), "C55 - pMethod1 - C55(Cat)")
            self.assertEqual(c.pMethod2(), "P55 - method2 - C")
            self.assertEqual(c.pMethod3(), "C55 - pMethod3 - C55(Cat)")

            self.assertEqual(c.method1(), "C55 - method1 - C55(Cat)")
            self.assertEqual(c.method2(), "C55 - method2 - C55(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP55 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP55 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP55 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP55 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP55 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP55 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP55 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP55 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP55 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP55 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P55 - method1 - P")
            self.assertEqual(p.pMethod2(), "P55 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P55 - method3 - P")

    def test_category_on_child_after_calls_child_grandparent_parent(self):
        c = mod.OC_Category_C56.alloc().init()
        p = mod.OC_Category_P56.alloc().init()
        gp = mod.OC_Category_GP56.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_c56  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C56 - gpMethod1 - C56(Cat)")
            self.assertEqual(c.gpMethod2(), "GP56 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP56 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP56 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C56 - gpMethod5 - C56(Cat)")

            self.assertEqual(c.pMethod1(), "C56 - pMethod1 - C56(Cat)")
            self.assertEqual(c.pMethod2(), "P56 - method2 - C")
            self.assertEqual(c.pMethod3(), "C56 - pMethod3 - C56(Cat)")

            self.assertEqual(c.method1(), "C56 - method1 - C56(Cat)")
            self.assertEqual(c.method2(), "C56 - method2 - C56(Cat)")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP56 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP56 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP56 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP56 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP56 - method5 - GP")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP56 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP56 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP56 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP56 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP56 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P56 - method1 - P")
            self.assertEqual(p.pMethod2(), "P56 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P56 - method3 - P")

    def test_category_on_child_before_inst_child_parent_grandparent(self):
        from . import category_c57  # noqa: F401

        c = mod.OC_Category_C57.alloc().init()
        p = mod.OC_Category_P57.alloc().init()
        gp = mod.OC_Category_GP57.alloc().init()

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C57 - gpMethod1 - C57(Cat)")
            self.assertEqual(c.gpMethod2(), "GP57 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP57 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP57 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C57 - gpMethod5 - C57(Cat)")

            self.assertEqual(c.pMethod1(), "C57 - pMethod1 - C57(Cat)")
            self.assertEqual(c.pMethod2(), "P57 - method2 - C")
            self.assertEqual(c.pMethod3(), "C57 - pMethod3 - C57(Cat)")

            self.assertEqual(c.method1(), "C57 - method1 - C57(Cat)")
            self.assertEqual(c.method2(), "C57 - method2 - C57(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP57 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP57 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP57 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP57 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP57 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P57 - method1 - P")
            self.assertEqual(p.pMethod2(), "P57 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P57 - method3 - P")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP57 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP57 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP57 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP57 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP57 - method5 - GP")

    def test_category_on_child_after_inst_child_parent_grandparent(self):
        c = mod.OC_Category_C58.alloc().init()
        p = mod.OC_Category_P58.alloc().init()
        gp = mod.OC_Category_GP58.alloc().init()

        from . import category_c58  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C58 - gpMethod1 - C58(Cat)")
            self.assertEqual(c.gpMethod2(), "GP58 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP58 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP58 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C58 - gpMethod5 - C58(Cat)")

            self.assertEqual(c.pMethod1(), "C58 - pMethod1 - C58(Cat)")
            self.assertEqual(c.pMethod2(), "P58 - method2 - C")
            self.assertEqual(c.pMethod3(), "C58 - pMethod3 - C58(Cat)")

            self.assertEqual(c.method1(), "C58 - method1 - C58(Cat)")
            self.assertEqual(c.method2(), "C58 - method2 - C58(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP58 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP58 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP58 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP58 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP58 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P58 - method1 - P")
            self.assertEqual(p.pMethod2(), "P58 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P58 - method3 - P")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP58 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP58 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP58 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP58 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP58 - method5 - GP")

    def test_category_on_child_after_calls_child_parent_grandparent(self):
        c = mod.OC_Category_C59.alloc().init()
        p = mod.OC_Category_P59.alloc().init()
        gp = mod.OC_Category_GP59.alloc().init()

        c.gpMethod1()
        c.gpMethod2()
        c.gpMethod3()
        c.gpMethod4()
        p.gpMethod1()
        p.gpMethod2()
        p.gpMethod3()
        p.gpMethod4()
        gp.gpMethod1()
        gp.gpMethod2()
        gp.gpMethod3()
        gp.gpMethod4()
        c.pMethod1()
        c.pMethod2()
        p.pMethod1()
        p.pMethod2()
        c.method1()
        from . import category_c59  # noqa: F401

        with self.subTest("child"):
            self.assertEqual(c.gpMethod1(), "C59 - gpMethod1 - C59(Cat)")
            self.assertEqual(c.gpMethod2(), "GP59 - method2 - P")
            self.assertEqual(c.gpMethod3(), "GP59 - method3 - C")
            self.assertEqual(c.gpMethod4(), "GP59 - method4 - C")
            self.assertEqual(c.gpMethod5(), "C59 - gpMethod5 - C59(Cat)")

            self.assertEqual(c.pMethod1(), "C59 - pMethod1 - C59(Cat)")
            self.assertEqual(c.pMethod2(), "P59 - method2 - C")
            self.assertEqual(c.pMethod3(), "C59 - pMethod3 - C59(Cat)")

            self.assertEqual(c.method1(), "C59 - method1 - C59(Cat)")
            self.assertEqual(c.method2(), "C59 - method2 - C59(Cat)")

        with self.subTest("parent"):
            self.assertEqual(p.gpMethod1(), "GP59 - method1 - GP")
            self.assertEqual(p.gpMethod2(), "GP59 - method2 - P")
            self.assertEqual(p.gpMethod3(), "GP59 - method3 - P")
            self.assertEqual(p.gpMethod4(), "GP59 - method4 - GP")
            # self.assertEqual(p.gpMethod5(), "GP59 - method5 - GP")

            self.assertEqual(p.pMethod1(), "P59 - method1 - P")
            self.assertEqual(p.pMethod2(), "P59 - method2 - P")
            # self.assertEqual(p.pMethod3(), "P59 - method3 - P")

        with self.subTest("grandparent"):
            self.assertEqual(gp.gpMethod1(), "GP59 - method1 - GP")
            self.assertEqual(gp.gpMethod2(), "GP59 - method2 - GP")
            self.assertEqual(gp.gpMethod3(), "GP59 - method3 - GP")
            self.assertEqual(gp.gpMethod4(), "GP59 - method4 - GP")
            # self.assertEqual(gp.gpMethod5(), "GP59 - method5 - GP")
