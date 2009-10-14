
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKImageView (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(IKToolModeNone, unicode)
        self.failUnlessIsInstance(IKToolModeMove, unicode)
        self.failUnlessIsInstance(IKToolModeSelect, unicode)
        self.failUnlessIsInstance(IKToolModeCrop, unicode)
        self.failUnlessIsInstance(IKToolModeRotate, unicode)
        self.failUnlessIsInstance(IKToolModeAnnotate, unicode)
        self.failUnlessIsInstance(IKOverlayTypeBackground, unicode)
        self.failUnlessIsInstance(IKOverlayTypeImage, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(IKToolModeSelectRect, unicode)
        self.failUnlessIsInstance(IKToolModeSelectEllipse, unicode)
        self.failUnlessIsInstance(IKToolModeSelectLasso, unicode)





if __name__ == "__main__":
    main()
