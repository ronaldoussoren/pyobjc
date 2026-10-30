from PyObjCTools.TestSupport import TestCase
import objc

from .methcat import OC_MethodCategories

# Import for test_bufsizeinarg is needed for the definion of CFArray
from . import test_bufsizeinarg  # noqa: F401

objc.registerMetaDataForSelector(
    b"OC_MethodCategories", b"newAsCF", {"retval": {"already_cfretained": True}}
)
objc.registerMetaDataForSelector(
    b"OC_MethodCategories", b"newNotRetained", {"retval": {"already_retained": False}}
)

objc.registerMetaDataForSelector(
    b"OC_MethodCategories", b"newAsOC", {"retval": {"already_retained": True}}
)
objc.registerMetaDataForSelector(
    b"OC_MethodCategories",
    b"newCFNotRetained",
    {"retval": {"already_cfretained": False}},
)

objc.registerMetaDataForSelector(
    b"OC_MethodCategories", b"copyAsCF", {"retval": {"already_cfretained": True}}
)
objc.registerMetaDataForSelector(
    b"OC_MethodCategories", b"copyNotRetained", {"retval": {"already_retained": False}}
)

objc.registerMetaDataForSelector(
    b"OC_MethodCategories", b"copyAsOC", {"retval": {"already_retained": True}}
)
objc.registerMetaDataForSelector(
    b"OC_MethodCategories",
    b"copyCFNotRetained",
    {"retval": {"already_cfretained": False}},
)


class TestCategoryNewOC(TestCase):
    def test_instance_new(self):
        o = OC_MethodCategories.alloc().init()

        v = o.newWithInt_(2)
        self.assertEqual(len(v), 2)
        self.assertEqual(v.retainCount(), 1)

        self.assertResultIsRetained(o.newWithInt_)
        self.assertResultIsNotCFRetained(o.newWithInt_)

    def test_class_new(self):
        v = OC_MethodCategories.newWithFloat_(2.5)
        self.assertEqual(v, [2.5])

        self.assertResultIsRetained(OC_MethodCategories.newWithFloat_)
        self.assertResultIsNotCFRetained(OC_MethodCategories.newWithFloat_)

    def test_instance_not_new(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.newerValue)
        self.assertResultIsNotCFRetained(o.newerValue)

    def test_class_not_new(self):
        self.assertResultIsNotRetained(OC_MethodCategories.newerValue)
        self.assertResultIsNotCFRetained(OC_MethodCategories.newerValue)

    def test_instance_cfretainedid(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsCFRetained(o.newAsCF)
        self.assertResultIsNotRetained(o.newAsCF)

    def test_instance_new_not_retained(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.newNotRetained)
        self.assertResultIsNotCFRetained(o.newNotRetained)


class TestCategoryNewCF(TestCase):
    def test_instance_new(self):
        o = OC_MethodCategories.alloc().init()

        v = o.newCFWithInt_(2)
        self.assertEqual(len(v), 2)
        self.assertEqual(v.retainCount(), 1)

        self.assertResultIsCFRetained(o.newCFWithInt_)
        self.assertResultIsNotRetained(o.newCFWithInt_)

    def test_class_new(self):
        v = OC_MethodCategories.newCFWithFloat_(2.5)
        self.assertEqual(v, [2.5])

        self.assertResultIsNotRetained(OC_MethodCategories.newCFWithFloat_)
        self.assertResultIsCFRetained(OC_MethodCategories.newCFWithFloat_)

    def test_instance_not_new(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.newerCFValue)
        self.assertResultIsNotCFRetained(o.newerCFValue)

    def test_class_not_new(self):
        self.assertResultIsNotRetained(OC_MethodCategories.newerCFValue)
        self.assertResultIsNotCFRetained(OC_MethodCategories.newerCFValue)

    def test_instance_cfretainedid(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotCFRetained(o.newAsOC)
        self.assertResultIsRetained(o.newAsOC)

    def test_instance_new_not_retained(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.newCFNotRetained)
        self.assertResultIsNotCFRetained(o.newCFNotRetained)


class TestCategoryCopCopy(TestCase):
    def test_instance_copy(self):
        o = OC_MethodCategories.alloc().init()

        v = o.copyWithInt_(2)
        self.assertEqual(len(v), 2)
        self.assertEqual(v.retainCount(), 1)

        self.assertResultIsRetained(o.copyWithInt_)
        self.assertResultIsNotCFRetained(o.copyWithInt_)

    def test_class_copy(self):
        v = OC_MethodCategories.copyWithFloat_(2.5)
        self.assertEqual(v, [2.5])

        self.assertResultIsRetained(OC_MethodCategories.copyWithFloat_)
        self.assertResultIsNotCFRetained(OC_MethodCategories.copyWithFloat_)

    def test_instance_not_copy(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.copyingValue)
        self.assertResultIsNotCFRetained(o.copyingValue)

    def test_class_not_copy(self):
        self.assertResultIsNotRetained(OC_MethodCategories.copyingValue)
        self.assertResultIsNotCFRetained(OC_MethodCategories.copyingValue)

    def test_instance_cfretainedid(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsCFRetained(o.copyAsCF)
        self.assertResultIsNotRetained(o.copyAsCF)

    def test_instance_copy_not_retained(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.copyNotRetained)
        self.assertResultIsNotCFRetained(o.copyNotRetained)


class TestCategoryCopyCF(TestCase):
    def test_instance_copy(self):
        o = OC_MethodCategories.alloc().init()

        v = o.copyCFWithInt_(2)
        self.assertEqual(len(v), 2)
        self.assertEqual(v.retainCount(), 1)

        self.assertResultIsCFRetained(o.copyCFWithInt_)
        self.assertResultIsNotRetained(o.copyCFWithInt_)

    def test_class_copy(self):
        v = OC_MethodCategories.copyCFWithFloat_(2.5)
        self.assertEqual(v, [2.5])

        self.assertResultIsNotRetained(OC_MethodCategories.copyCFWithFloat_)
        self.assertResultIsCFRetained(OC_MethodCategories.copyCFWithFloat_)

    def test_instance_not_copy(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.copyingCFValue)
        self.assertResultIsNotCFRetained(o.copyingCFValue)

    def test_class_not_copy(self):
        self.assertResultIsNotRetained(OC_MethodCategories.copyingCFValue)
        self.assertResultIsNotCFRetained(OC_MethodCategories.copyingCFValue)

    def test_instance_cfretainedid(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotCFRetained(o.copyAsOC)
        self.assertResultIsRetained(o.copyAsOC)

    def test_instance_copy_not_retained(self):
        o = OC_MethodCategories.alloc().init()
        self.assertResultIsNotRetained(o.copyCFNotRetained)
        self.assertResultIsNotCFRetained(o.copyCFNotRetained)
