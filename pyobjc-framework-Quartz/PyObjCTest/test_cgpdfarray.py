
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFArray (TestCase):

    @expectedFailure
    def testIncomplete(self):
        self.fail("Tests are too minimal")

    def testTypes(self):
        self.assertIsOpaquePointer(CGPDFArrayRef)

    def testFunctions(self):
        self.assertResultHasType(CGPDFArrayGetArray, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetArray, 2)

        self.assertResultHasType(CGPDFArrayGetBoolean, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetBoolean, 2)

        self.assertResultHasType(CGPDFArrayGetDictionary, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetDictionary, 2)

        self.assertResultHasType(CGPDFArrayGetInteger, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetInteger, 2)

        self.assertResultHasType(CGPDFArrayGetName, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetName, 2)

        self.assertResultHasType(CGPDFArrayGetNull, objc._C_BOOL)

        self.assertResultHasType(CGPDFArrayGetNumber, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetNumber, 2)

        self.assertResultHasType(CGPDFArrayGetObject, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetObject, 2)

        self.assertResultHasType(CGPDFArrayGetStream, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetStream, 2)

        self.assertResultHasType(CGPDFArrayGetString, objc._C_BOOL)
        self.assertArgIsOut(CGPDFArrayGetString, 2)

        CGPDFArrayGetCount

if __name__ == "__main__":
    main()
