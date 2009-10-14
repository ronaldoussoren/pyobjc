
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKSlideShowHelper (NSObject):
    def slideshowItemAtIndex_(self, idx): return None
    def nameOfSlideshowItemAtIndex_(self, idx): return None
    def canExportSlideshowItemAtIndex_toApplication_(self, idx, app): return True
    def slideshowDidChangeCurrentIndex_(self, idx): pass


class TestIKSlideshow (TestCase):
    @min_os_level('10.5')
    def no_testProtocols(self):
        self.failUnlessIsInstance(objc.protocolNamed("IKSlideshowDataSource"), objc.formal_protocol)

    @min_os_level('10.5')
    def testProtocolMethods(self):
        self.failUnlessArgHasType(TestIKSlideShowHelper.slideshowItemAtIndex_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIKSlideShowHelper.nameOfSlideshowItemAtIndex_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_, 0, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_)
        self.failUnlessArgHasType(TestIKSlideShowHelper.slideshowDidChangeCurrentIndex_, 0, objc._C_NSUInteger)

    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(IKSlideshow.canExportToApplication_)

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(IKSlideshowModeImages, unicode)
        self.failUnlessIsInstance(IKSlideshowModePDF, unicode)
        self.failUnlessIsInstance(IKSlideshowModeOther, unicode)
        self.failUnlessIsInstance(IKSlideshowWrapAround, unicode)
        self.failUnlessIsInstance(IKSlideshowStartPaused, unicode)
        self.failUnlessIsInstance(IKSlideshowStartIndex, unicode)
        self.failUnlessIsInstance(IKSlideshowPDFDisplayBox, unicode)
        self.failUnlessIsInstance(IKSlideshowPDFDisplayMode, unicode)
        self.failUnlessIsInstance(IKSlideshowPDFDisplaysAsBook, unicode)
        self.failUnlessIsInstance(IK_iPhotoBundleIdentifier, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(IKSlideshowScreen, unicode)
        self.failUnlessIsInstance(IKSlideshowAudioFile, unicode)
        self.failUnlessIsInstance(IKSlideshowPDFDisplayBox, unicode)
        self.failUnlessIsInstance(IKSlideshowPDFDisplayMode, unicode)
        self.failUnlessIsInstance(IKSlideshowPDFDisplaysAsBook, unicode)
        self.failUnlessIsInstance(IK_ApertureBundleIdentifier, unicode)
        self.failUnlessIsInstance(IK_MailBundleIdentifier, unicode)


if __name__ == "__main__":
    main()
