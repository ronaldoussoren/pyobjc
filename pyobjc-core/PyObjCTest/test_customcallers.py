from .customcallers import (
    OC_CustomCaller,
    OC_CustomCallerChild1,
    OC_CustomCallerChild2,
    OC_CustomCallerGrandchild,
)
from PyObjCTools.TestSupport import TestCase


class TestRegistrationOrder(TestCase):
    def test_default_caller(self):
        with self.subTest("no customcallers for selector"):
            self.assertEqual(OC_CustomCaller.alloc().init().customcallers1(), 1)

        with self.subTest("no match for selector"):
            self.assertEqual(OC_CustomCallerChild1.alloc().init().customcallers6(), 16)

    def test_none_before_class(self):
        self.assertEqual(OC_CustomCallerChild1.alloc().init().customcallers2(), -2)
        self.assertEqual(OC_CustomCallerGrandchild.alloc().init().customcallers2(), -2)
        self.assertEqual(OC_CustomCallerChild2.alloc().init().customcallers2(), -20)

    def test_none_after_class(self):
        self.assertEqual(OC_CustomCallerChild1.alloc().init().customcallers3(), -3)
        self.assertEqual(OC_CustomCallerGrandchild.alloc().init().customcallers3(), -3)
        self.assertEqual(OC_CustomCallerChild2.alloc().init().customcallers3(), -30)

    def test_subclass_before_superclass(self):
        self.assertEqual(OC_CustomCallerChild1.alloc().init().customcallers4(), -4)
        self.assertEqual(OC_CustomCallerGrandchild.alloc().init().customcallers4(), -4)
        self.assertEqual(OC_CustomCallerChild2.alloc().init().customcallers4(), -40)

    def test_subclass_after_superclass(self):
        self.assertEqual(OC_CustomCallerChild1.alloc().init().customcallers5(), -5)
        self.assertEqual(OC_CustomCallerGrandchild.alloc().init().customcallers5(), -5)
        self.assertEqual(OC_CustomCallerChild2.alloc().init().customcallers5(), -50)

    def test_double_registration(self):
        self.assertEqual(OC_CustomCallerChild1.alloc().init().customcallers7(), 17)
        self.assertEqual(OC_CustomCallerGrandchild.alloc().init().customcallers7(), 117)
        self.assertEqual(OC_CustomCallerChild2.alloc().init().customcallers7(), -70)
