
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGPDFDictionary (TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFDictionary.h>")

if __name__ == "__main__":
    main()
