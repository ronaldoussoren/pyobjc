
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVReturn (TestCase):
    def testConstants(self):
        self.assertEqual(kCVReturnSuccess, 0)
        self.assertEqual(kCVReturnError, -6660)
        self.assertEqual(kCVReturnInvalidArgument, -6661)
        self.assertEqual(kCVReturnAllocationFailed, -6662)
        self.assertEqual(kCVReturnInvalidDisplay, -6670)
        self.assertEqual(kCVReturnDisplayLinkAlreadyRunning, -6671)
        self.assertEqual(kCVReturnDisplayLinkNotRunning, -6672)
        self.assertEqual(kCVReturnDisplayLinkCallbacksNotSet, -6673)
        self.assertEqual(kCVReturnInvalidPixelFormat, -6680)
        self.assertEqual(kCVReturnInvalidSize, -6681)
        self.assertEqual(kCVReturnInvalidPixelBufferAttributes, -6682)
        self.assertEqual(kCVReturnPixelBufferNotOpenGLCompatible, -6683)
        self.assertEqual(kCVReturnPoolAllocationFailed, -6690)
        self.assertEqual(kCVReturnInvalidPoolAttributes, -6691)

if __name__ == "__main__":
    main()
