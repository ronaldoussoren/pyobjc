
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFArray (TestCase):
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFArray.h>")

    def testTypes(self):
        self.failUnlessIsOpaquePointer(CGPDFArrayRef)

    def testFunctions(self):
        self.failUnlessResultHasType(CGPDFArrayGetArray, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetArray, 2)

        self.failUnlessResultHasType(CGPDFArrayGetBoolean, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetBoolean, 2)

        self.failUnlessResultHasType(CGPDFArrayGetDictionary, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetDictionary, 2)

        self.failUnlessResultHasType(CGPDFArrayGetInteger, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetInteger, 2)

        self.failUnlessResultHasType(CGPDFArrayGetName, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetName, 2)

        self.failUnlessResultHasType(CGPDFArrayGetNull, objc._C_BOOL)

        self.failUnlessResultHasType(CGPDFArrayGetNumber, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetNumber, 2)

        self.failUnlessResultHasType(CGPDFArrayGetObject, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetObject, 2)

        self.failUnlessResultHasType(CGPDFArrayGetStream, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetStream, 2)

        self.failUnlessResultHasType(CGPDFArrayGetString, objc._C_BOOL)
        self.failUnlessArgIsOut(CGPDFArrayGetString, 2)

        CGPDFArrayGetCount

if __name__ == "__main__":
    main()
