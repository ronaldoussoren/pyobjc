import objc
from PyObjCTest.structpointer1 import OC_TestStructPointer
from PyObjCTest.structpointer2 import FooEncoded
from PyObjCTools.TestSupport import TestCase

TestStructPointerStructPtr = objc.createOpaquePointerType(
    "TestStructPointerStructPtr", FooEncoded
)


class TestOpaqueStructPointer(TestCase):
    def testPointer(self):
        # Check that the TestPointerStructPtr has a signature that is
        # different from the one in the method definition. The latter contains
        # more information.
        retval = objc.splitSignature(
            OC_TestStructPointer.returnPointerToStruct.signature
        )[0]
        self.assertNotEqual(TestStructPointerStructPtr.__typestr__, retval)

        # And then check that the correct pointer wrapper is created
        v = OC_TestStructPointer.returnPointerToStruct()
        self.assertIsInstance(v, TestStructPointerStructPtr)
