from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz

import objc


class TestCGPDFArray(TestCase):
    def testTypes(self):
        self.assertIsOpaquePointer(Quartz.CGPDFArrayRef)

    def testFunctions(self):
        self.assertResultHasType(Quartz.CGPDFArrayGetArray, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetArray, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetBoolean, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetBoolean, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetDictionary, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetDictionary, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetInteger, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetInteger, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetName, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetName, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetNull, objc._C_BOOL)

        self.assertResultHasType(Quartz.CGPDFArrayGetNumber, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetNumber, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetObject, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetObject, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetStream, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetStream, 2)

        self.assertResultHasType(Quartz.CGPDFArrayGetString, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFArrayGetString, 2)

        Quartz.CGPDFArrayGetCount

    @min_os_level("10.14")
    def testFunctions10_14(self):
        self.assertArgIsBlock(Quartz.CGPDFArrayApplyBlock, 1, b"Bl^{CGPDFObject=}^v")
