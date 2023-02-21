import objc
from PyObjCTest.testclassandinst import (
    PyObjC_TestClassAndInstance,
    PyObjC_TestUnallocatable,
)
from PyObjCTools.TestSupport import TestCase


class PyObjC_TestClassAndInstanceSubclass(PyObjC_TestClassAndInstance):
    """Simple subclass, just make sure it still works"""

    pass


class PyObjC_TestClassAndInstanceClassOverride(PyObjC_TestClassAndInstance):
    """return YES for both"""

    @classmethod
    def isInstance(klass):
        return objc.YES


class PyObjC_TestClassAndInstanceInstanceOverride(PyObjC_TestClassAndInstance):
    """return NO for both"""

    def isInstance(self):
        return objc.NO


# XXX
# class PyObjC_TestClassAndInstanceBothOverride(PyObjC_TestClassAndInstance):
#     """flipped"""
#     def isInstance__class__(self):
#         return objc.YES
#
#     def isInstance__inst__(self):
#         return objc.NO


class TestClassAndInstance(TestCase):
    def testClassAndInstanceInstanceOverrideWorkaround(self):
        self.assertFalse(
            PyObjC_TestClassAndInstanceInstanceOverride.pyobjc_classMethods.isInstance()
        )
        self.assertFalse(
            PyObjC_TestClassAndInstanceInstanceOverride.alloc()
            .init()
            .pyobjc_instanceMethods.isInstance()
        )

    def testClassAndInstanceClassOverrideWorkaround(self):
        self.assertTrue(
            PyObjC_TestClassAndInstanceClassOverride.pyobjc_classMethods.isInstance()
        )

    def testClassAndInstanceSubclassWorkaround(self):
        self.assertFalse(
            PyObjC_TestClassAndInstanceSubclass.pyobjc_classMethods.isInstance()
        )
        self.assertTrue(
            PyObjC_TestClassAndInstanceSubclass.alloc()
            .init()
            .pyobjc_instanceMethods.isInstance()
        )

    def testClassAndInstanceWorkaround(self):
        if PyObjC_TestClassAndInstance.pyobjc_classMethods.isInstance():
            self.fail()

        self.assertFalse(PyObjC_TestClassAndInstance.pyobjc_classMethods.isInstance())
        self.assertTrue(
            PyObjC_TestClassAndInstance.alloc()
            .init()
            .pyobjc_instanceMethods.isInstance()
        )

    def testClassAndInstanceClassOverride(self):
        self.assertTrue(PyObjC_TestClassAndInstanceClassOverride.isInstance())
        self.assertTrue(
            PyObjC_TestClassAndInstanceClassOverride.alloc().init().isInstance()
        )

    def testClassAndInstanceInstanceOverride(self):
        # Having the next line true would be nice:
        # self.assertFalse(PyObjC_TestClassAndInstanceInstanceOverride.isInstance())
        # But we'll have to settle for this one instead:
        self.assertFalse(
            PyObjC_TestClassAndInstanceInstanceOverride.pyobjc_classMethods.isInstance()
        )
        self.assertFalse(
            PyObjC_TestClassAndInstanceInstanceOverride.alloc().init().isInstance()
        )

    def testClassAndInstanceSubclass(self):
        # Having the next line true would be nice:
        # self.assertFalse(PyObjC_TestClassAndInstanceSubclass.isInstance())
        # But we'll have to settle for this one instead:
        self.assertFalse(
            PyObjC_TestClassAndInstanceSubclass.pyobjc_classMethods.isInstance()
        )
        self.assertTrue(PyObjC_TestClassAndInstanceSubclass.alloc().init().isInstance())

    def testClassAndInstance(self):
        # Having the next line true would be nice:
        # self.assertEqual(PyObjC_TestClassAndInstance.isInstance(), objc.NO)
        # But we'll have to settle for this one instead:
        self.assertFalse(PyObjC_TestClassAndInstance.pyobjc_classMethods.isInstance())
        self.assertTrue(PyObjC_TestClassAndInstance.alloc().init().isInstance())

    def testUnallocatable(self):
        # FIXME: This crashes on Tiger, haven't had time to debug yet
        self.assertEqual(PyObjC_TestUnallocatable.alloc(), None)
