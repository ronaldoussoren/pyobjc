from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.structpointer2 import *
from PyObjCTest.structpointer1 import *

class TestOpaqueStructPointer (TestCase):
    def testPointer(self):

        # Check that the TestPointerStructPtr has a signature that is 
        # different from the one in the method definition. The latter contains
        # more information.
        retval = objc.splitSignature(
                OC_TestStructPointer.returnPointerToStruct.signature)[0]
        self.assertNotEquals(TestStructPointerStructPtr.__typestr__, retval)

        # And then check that the correct pointer wrapper is created
        v = OC_TestStructPointer.returnPointerToStruct()
        self.assert_(isinstance(v, TestStructPointerStructPtr))

if __name__ == "__main__":
    main()
