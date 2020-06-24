from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestIKSlideShowHelper(Quartz.NSObject):
    def numberOfSlideshowItems(self):
        return 1

    def slideshowItemAtIndex_(self, idx):
        return None

    def nameOfSlideshowItemAtIndex_(self, idx):
        return None

    def canExportSlideshowItemAtIndex_toApplication_(self, idx, app):
        return True

    def slideshowDidChangeCurrentIndex_(self, idx):
        pass


class TestIKSlideshow(TestCase):
    @min_os_level("10.5")
    def no_testProtocols(self):
        self.assertIsInstance(
            objc.protocolNamed("IKSlideshowDataSource"), objc.formal_protocol
        )

    @min_os_level("10.5")
    def testProtocolMethods(self):
        self.assertResultHasType(
            TestIKSlideShowHelper.numberOfSlideshowItems, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestIKSlideShowHelper.slideshowItemAtIndex_, 0, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestIKSlideShowHelper.nameOfSlideshowItemAtIndex_, 0, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestIKSlideShowHelper.canExportSlideshowItemAtIndex_toApplication_
        )
        self.assertArgHasType(
            TestIKSlideShowHelper.slideshowDidChangeCurrentIndex_, 0, objc._C_NSUInteger
        )

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.IKSlideshow.canExportToApplication_)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.IKSlideshowModeImages, str)
        self.assertIsInstance(Quartz.IKSlideshowModePDF, str)
        self.assertIsInstance(Quartz.IKSlideshowModeOther, str)
        self.assertIsInstance(Quartz.IKSlideshowWrapAround, str)
        self.assertIsInstance(Quartz.IKSlideshowStartPaused, str)
        self.assertIsInstance(Quartz.IKSlideshowStartIndex, str)
        self.assertIsInstance(Quartz.IKSlideshowPDFDisplayBox, str)
        self.assertIsInstance(Quartz.IKSlideshowPDFDisplayMode, str)
        self.assertIsInstance(Quartz.IKSlideshowPDFDisplaysAsBook, str)
        self.assertIsInstance(Quartz.IK_iPhotoBundleIdentifier, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.IKSlideshowScreen, str)
        self.assertIsInstance(Quartz.IKSlideshowAudioFile, str)
        self.assertIsInstance(Quartz.IKSlideshowPDFDisplayBox, str)
        self.assertIsInstance(Quartz.IKSlideshowPDFDisplayMode, str)
        self.assertIsInstance(Quartz.IKSlideshowPDFDisplaysAsBook, str)
        self.assertIsInstance(Quartz.IK_ApertureBundleIdentifier, str)
        self.assertIsInstance(Quartz.IK_MailBundleIdentifier, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.IK_PhotosBundleIdentifier, str)
