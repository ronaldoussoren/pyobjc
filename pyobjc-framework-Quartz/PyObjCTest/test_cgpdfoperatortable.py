
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFOperatorTable (TestCase):

    def testTypes(self):
        self.assertIsOpaquePointer(CGPDFOperatorTableRef)

    def testFunctions(self):
        CGPDFOperatorCallback = b'v^{CGPDFScanner=}^v'

        self.assertArgIsFunction(CGPDFOperatorTableSetCallback, 2, CGPDFOperatorCallback, True)

        CGPDFOperatorTableRetain
        CGPDFOperatorTableRelease

if __name__ == "__main__":
    main()
