from PyObjCTools.TestSupport import TestCase, os_release, expectedFailureIf
import Quartz

import objc


class TestCGPDFScanner(TestCase):
    def testTypes(self):
        self.assertIsOpaquePointer(Quartz.CGPDFScannerRef)

    @expectedFailureIf(os_release().startswith("10.5."))
    def testFunctionMissingOn10_5(self):
        Quartz.CGPDFScannerRetain

    def testFunctions(self):
        self.assertResultIsNotCFRetained(Quartz.CGPDFScannerCreate)

        Quartz.CGPDFScannerRelease
        self.assertResultHasType(Quartz.CGPDFScannerScan, objc._C_BOOL)
        Quartz.CGPDFScannerGetContentStream

        self.assertResultHasType(Quartz.CGPDFScannerPopObject, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopObject, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopBoolean, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopBoolean, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopInteger, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopInteger, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopNumber, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopNumber, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopName, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopName, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopString, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopString, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopArray, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopArray, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopDictionary, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopDictionary, 1)

        self.assertResultHasType(Quartz.CGPDFScannerPopStream, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGPDFScannerPopStream, 1)
