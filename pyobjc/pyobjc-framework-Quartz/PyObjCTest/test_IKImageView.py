
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKImageView (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(IKToolModeNone, unicode)
        self.assertIsInstance(IKToolModeMove, unicode)
        self.assertIsInstance(IKToolModeSelect, unicode)
        self.assertIsInstance(IKToolModeCrop, unicode)
        self.assertIsInstance(IKToolModeRotate, unicode)
        self.assertIsInstance(IKToolModeAnnotate, unicode)
        self.assertIsInstance(IKOverlayTypeBackground, unicode)
        self.assertIsInstance(IKOverlayTypeImage, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(IKToolModeSelectRect, unicode)
        self.assertIsInstance(IKToolModeSelectEllipse, unicode)
        self.assertIsInstance(IKToolModeSelectLasso, unicode)





if __name__ == "__main__":
    main()
