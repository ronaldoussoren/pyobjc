
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFScanner (TestCase):

    def testTypes(self):
        self.assertIsOpaquePointer(CGPDFScannerRef)

    @expectedFailureIf(os_release().startswith('10.5.'))
    def testFunctionMissingOn10_5(self):
        CGPDFScannerRetain

    def testFunctions(self):
        self.assertResultIsNotCFRetained(CGPDFScannerCreate)

        CGPDFScannerRelease
        self.assertResultHasType(CGPDFScannerScan, objc._C_BOOL)
        CGPDFScannerGetContentStream

        self.assertResultHasType(CGPDFScannerPopObject, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopObject, 1)

        self.assertResultHasType(CGPDFScannerPopBoolean, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopBoolean, 1)

        self.assertResultHasType(CGPDFScannerPopInteger, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopInteger, 1)

        self.assertResultHasType(CGPDFScannerPopNumber, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopNumber, 1)

        self.assertResultHasType(CGPDFScannerPopName, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopName, 1)

        self.assertResultHasType(CGPDFScannerPopString, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopString, 1)

        self.assertResultHasType(CGPDFScannerPopArray, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopArray, 1)

        self.assertResultHasType(CGPDFScannerPopDictionary, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopDictionary, 1)

        self.assertResultHasType(CGPDFScannerPopStream, objc._C_BOOL)
        self.assertArgIsOut(CGPDFScannerPopStream, 1)

if __name__ == "__main__":
    main()
