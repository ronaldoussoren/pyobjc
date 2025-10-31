from .customcallers import (
    OC_CustomCaller,
    OC_CustomCallerChild1,
    OC_CustomCallerChild2,
    OC_CustomCallerGrandchild,
)
from PyObjCTools.TestSupport import TestCase
import objc

objc.registerMetaDataForSelector(
    b"OC_CustomCaller",
    b"customcaller8:",
    {"arguments": {2 + 0: {"type_modifier": objc._C_IN}}},
)


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

    def test_not_callable(self):
        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8'"):
            OC_CustomCaller.alloc().init().customcallers8()

        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8:'"):
            OC_CustomCaller.alloc().init().customcallers8_(1)

    def test_not_callable_sel_and_imp(self):
        o = OC_CustomCaller.alloc().init()
        m = OC_CustomCaller.pyobjc_instanceMethods.customcallers8

        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8'"):
            m(o)

        m = OC_CustomCaller.pyobjc_instanceMethods.customcallers8_
        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8:'"):
            m(o, 1)

        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8'"):
            OC_CustomCaller.instanceMethodForSelector_(b"customcallers8")

        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8:'"):
            OC_CustomCaller.instanceMethodForSelector_(b"customcallers8:")

        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8'"):
            o.methodForSelector_(b"customcallers8")

        with self.assertRaisesRegex(TypeError, "Cannot call 'customcallers8:'"):
            o.methodForSelector_(b"customcallers8:")
