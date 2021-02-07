from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestIKPictureTaker(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgIsSEL(
            Quartz.IKPictureTaker.beginPictureTakerWithDelegate_didEndSelector_contextInfo_,
            1,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgIsSEL(
            Quartz.IKPictureTaker.beginPictureTakerSheetForWindow_withDelegate_didEndSelector_contextInfo_,
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgIsSEL(
            Quartz.IKPictureTaker.popUpRecentsMenuForView_withDelegate_didEndSelector_contextInfo_,
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )

        self.assertResultIsBOOL(Quartz.IKPictureTaker.mirroring)
        self.assertArgIsBOOL(Quartz.IKPictureTaker.setMirroring_, 0)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.IKPictureTakerAllowsVideoCaptureKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerAllowsFileChoosingKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerShowRecentPictureKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerUpdateRecentPictureKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerAllowsEditingKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerShowEffectsKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerInformationalTextKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerImageTransformsKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerOutputImageMaxSizeKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerCropAreaSizeKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerShowAddressBookPictureKey, str)
        self.assertIsInstance(Quartz.IKPictureTakerShowEmptyPictureKey, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.IKPictureTakerRemainOpenAfterValidateKey, str)
