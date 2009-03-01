
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGShading (TestCase):
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGShading.h>")

    def testTypes(self):
        self.failUnlessIsCFType(CGShadingRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CGShadingGetTypeID(), (int, long))


if __name__ == "__main__":
    main()
