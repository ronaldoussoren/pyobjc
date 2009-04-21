
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *

class TestIKSlideShowHelper (NSObject):
    def slideshowItemAtIndex_(self, idx): return None
    def nameOfSlideshowItemAtIndex_(self, idx): return None
    def canExportSlideshowItemAtIndex_toApplication_(self, idx, app): return True
    def slideshowDidChangeCurrentIndex_(self, idx): pass


class TestIKSlideshow (TestCase):
    def no_testProtocols(self):
        self.failUnlessIsInstance(objc.protocolNamed("IKSlideshowDataSource"), objc.formal_protocol)

    def testProtocolMethods(self):
        self.failUnlessArgHasType(TestIKSlideShowHelper.slideshowItemAtIndex_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIKSlideShowHelper.nameOfSlideshowItemAtIndex_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_, 0, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_)
        self.failUnlessArgHasType(TestIKSlideShowHelper.slideshowDidChangeCurrentIndex_, 0, objc._C_NSUInteger)

    def testMethods(self):
        self.failUnlessResultIsBOOL(IKSlideshow.canExportToApplication_)

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



if __name__ == "__main__":
    main()
