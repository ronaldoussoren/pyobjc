
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *

class TestIKImageView (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(IKToolModeNone, unicode)
        self.failUnlessIsInstance(IKToolModeMove, unicode)
        self.failUnlessIsInstance(IKToolModeSelect, unicode)
        self.failUnlessIsInstance(IKToolModeCrop, unicode)
        self.failUnlessIsInstance(IKToolModeRotate, unicode)
        self.failUnlessIsInstance(IKToolModeAnnotate, unicode)
        self.failUnlessIsInstance(IKOverlayTypeBackground, unicode)
        self.failUnlessIsInstance(IKOverlayTypeImage, unicode)


if __name__ == "__main__":
    main()
