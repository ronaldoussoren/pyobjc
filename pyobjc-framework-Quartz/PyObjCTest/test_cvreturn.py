from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCVReturn(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCVReturnSuccess, 0)
        self.assertEqual(Quartz.kCVReturnError, -6660)
        self.assertEqual(Quartz.kCVReturnInvalidArgument, -6661)
        self.assertEqual(Quartz.kCVReturnAllocationFailed, -6662)
        self.assertEqual(Quartz.kCVReturnUnsupported, -6663)
        self.assertEqual(Quartz.kCVReturnInvalidDisplay, -6670)
        self.assertEqual(Quartz.kCVReturnDisplayLinkAlreadyRunning, -6671)
        self.assertEqual(Quartz.kCVReturnDisplayLinkNotRunning, -6672)
        self.assertEqual(Quartz.kCVReturnDisplayLinkCallbacksNotSet, -6673)
        self.assertEqual(Quartz.kCVReturnInvalidPixelFormat, -6680)
        self.assertEqual(Quartz.kCVReturnInvalidSize, -6681)
        self.assertEqual(Quartz.kCVReturnInvalidPixelBufferAttributes, -6682)
        self.assertEqual(Quartz.kCVReturnPixelBufferNotOpenGLCompatible, -6683)
        self.assertEqual(Quartz.kCVReturnPixelBufferNotMetalCompatible, -6684)
        self.assertEqual(Quartz.kCVReturnWouldExceedAllocationThreshold, -6689)
        self.assertEqual(Quartz.kCVReturnPoolAllocationFailed, -6690)
        self.assertEqual(Quartz.kCVReturnInvalidPoolAttributes, -6691)
        self.assertEqual(Quartz.kCVReturnRetry, -6692)
        self.assertEqual(Quartz.kCVReturnLast, -6699)
