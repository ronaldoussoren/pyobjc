
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFDictionary (TestCase):
    @expectedFailure
    def testIncomplete(self):
        CGPDFDictionaryGetObject
        CGPDFDictionaryGetBoolean
        CGPDFDictionaryGetInteger
        CGPDFDictionaryGetNumber
        CGPDFDictionaryGetName
        CGPDFDictionaryGetString
        CGPDFDictionaryGetArray
        CGPDFDictionaryGetDictionary
        CGPDFDictionaryGetGetStream
        CGPDFDictionaryApplyFunction
        self.fail("Add header tests for <CoreGraphics/CGPDFDictionary.h>")

    def testFunctions(self):
        CGPDFDictionaryGetCount

if __name__ == "__main__":
    main()
