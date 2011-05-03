
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKPictureTaker (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsSEL(IKPictureTaker.beginPictureTakerWithDelegate_didEndSelector_contextInfo_, 1, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgIsSEL(IKPictureTaker.beginPictureTakerSheetForWindow_withDelegate_didEndSelector_contextInfo_, 2, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgIsSEL(IKPictureTaker.popUpRecentsMenuForView_withDelegate_didEndSelector_contextInfo_, 2, b'v@:@' + objc._C_NSInteger + b'^v')

        self.assertResultIsBOOL(IKPictureTaker.mirroring)
        self.assertArgIsBOOL(IKPictureTaker.setMirroring_, 0)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(IKPictureTakerAllowsVideoCaptureKey, unicode)
        self.assertIsInstance(IKPictureTakerAllowsFileChoosingKey, unicode)
        self.assertIsInstance(IKPictureTakerShowRecentPictureKey, unicode)
        self.assertIsInstance(IKPictureTakerUpdateRecentPictureKey, unicode)
        self.assertIsInstance(IKPictureTakerAllowsEditingKey, unicode)
        self.assertIsInstance(IKPictureTakerShowEffectsKey, unicode)
        self.assertIsInstance(IKPictureTakerInformationalTextKey, unicode)
        self.assertIsInstance(IKPictureTakerImageTransformsKey, unicode)
        self.assertIsInstance(IKPictureTakerOutputImageMaxSizeKey, unicode)
        self.assertIsInstance(IKPictureTakerCropAreaSizeKey, unicode)
        self.assertIsInstance(IKPictureTakerShowAddressBookPictureKey, unicode)
        self.assertIsInstance(IKPictureTakerShowEmptyPictureKey, unicode)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(IKPictureTakerRemainOpenAfterValidateKey, unicode)


if __name__ == "__main__":
    main()
