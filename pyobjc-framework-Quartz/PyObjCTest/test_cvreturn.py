
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVReturn (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCVReturnSuccess, 0)
        self.failUnlessEqual(kCVReturnError, -6660)
        self.failUnlessEqual(kCVReturnInvalidArgument, -6661)
        self.failUnlessEqual(kCVReturnAllocationFailed, -6662)
        self.failUnlessEqual(kCVReturnInvalidDisplay, -6670)
        self.failUnlessEqual(kCVReturnDisplayLinkAlreadyRunning, -6671)
        self.failUnlessEqual(kCVReturnDisplayLinkNotRunning, -6672)
        self.failUnlessEqual(kCVReturnDisplayLinkCallbacksNotSet, -6673)
        self.failUnlessEqual(kCVReturnInvalidPixelFormat, -6680)
        self.failUnlessEqual(kCVReturnInvalidSize, -6681)
        self.failUnlessEqual(kCVReturnInvalidPixelBufferAttributes, -6682)
        self.failUnlessEqual(kCVReturnPixelBufferNotOpenGLCompatible, -6683)
        self.failUnlessEqual(kCVReturnPoolAllocationFailed, -6690)
        self.failUnlessEqual(kCVReturnInvalidPoolAttributes, -6691)

if __name__ == "__main__":
    main()
