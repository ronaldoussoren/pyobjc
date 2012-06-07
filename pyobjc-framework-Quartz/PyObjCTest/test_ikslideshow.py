
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str

class TestIKSlideShowHelper (NSObject):
    def slideshowItemAtIndex_(self, idx): return None
    def nameOfSlideshowItemAtIndex_(self, idx): return None
    def canExportSlideshowItemAtIndex_toApplication_(self, idx, app): return True
    def slideshowDidChangeCurrentIndex_(self, idx): pass


class TestIKSlideshow (TestCase):
    @min_os_level('10.5')
    def no_testProtocols(self):
        self.assertIsInstance(objc.protocolNamed("IKSlideshowDataSource"), objc.formal_protocol)

    @min_os_level('10.5')
    def testProtocolMethods(self):
        self.assertArgHasType(TestIKSlideShowHelper.slideshowItemAtIndex_, 0, objc._C_NSUInteger)
        self.assertArgHasType(TestIKSlideShowHelper.nameOfSlideshowItemAtIndex_, 0, objc._C_NSUInteger)
        self.assertArgHasType(TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_, 0, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_)
        self.assertArgHasType(TestIKSlideShowHelper.slideshowDidChangeCurrentIndex_, 0, objc._C_NSUInteger)

    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(IKSlideshow.canExportToApplication_)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(IKSlideshowModeImages, unicode)
        self.assertIsInstance(IKSlideshowModePDF, unicode)
        self.assertIsInstance(IKSlideshowModeOther, unicode)
        self.assertIsInstance(IKSlideshowWrapAround, unicode)
        self.assertIsInstance(IKSlideshowStartPaused, unicode)
        self.assertIsInstance(IKSlideshowStartIndex, unicode)
        self.assertIsInstance(IKSlideshowPDFDisplayBox, unicode)
        self.assertIsInstance(IKSlideshowPDFDisplayMode, unicode)
        self.assertIsInstance(IKSlideshowPDFDisplaysAsBook, unicode)
        self.assertIsInstance(IK_iPhotoBundleIdentifier, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(IKSlideshowScreen, unicode)
        self.assertIsInstance(IKSlideshowAudioFile, unicode)
        self.assertIsInstance(IKSlideshowPDFDisplayBox, unicode)
        self.assertIsInstance(IKSlideshowPDFDisplayMode, unicode)
        self.assertIsInstance(IKSlideshowPDFDisplaysAsBook, unicode)
        self.assertIsInstance(IK_ApertureBundleIdentifier, unicode)
        self.assertIsInstance(IK_MailBundleIdentifier, unicode)


if __name__ == "__main__":
    main()
