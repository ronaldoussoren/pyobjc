
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *

class TestIKPictureTaker (TestCase):
    def testMethods(self):
        self.failUnlessArgIsSEL(IKPictureTaker.beginPictureTakerWithDelegate_didEndSelector_contextInfo_, 1, 'v@:@' + objc._C_NSInteger + '^v')
        self.failUnlessArgIsSEL(IKPictureTaker.beginPictureTakerSheetForWindow_withDelegate_didEndSelector_contextInfo_, 2, 'v@:@' + objc._C_NSInteger + '^v')
        self.failUnlessArgIsSEL(IKPictureTaker.popUpRecentsMenuForView_withDelegate_didEndSelector_contextInfo_, 1, 'v@:@' + objc._C_NSInteger + '^v')

        self.failUnlessResultIsBOOL(IKPictureTaker.mirroring)
        self.failUnlessArgIsBOOL(IKPictureTaker.setMirroring_, 0)

    def testConstants(self):
        self.failUnlessIsInstance(IKPictureTakerAllowsVideoCaptureKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerAllowsFileChoosingKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerShowRecentPictureKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerUpdateRecentPictureKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerAllowsEditingKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerShowEffectsKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerInformationalTextKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerImageTransformsKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerOutputImageMaxSizeKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerCropAreaSizeKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerShowAddressBookPictureKey, unicode)
        self.failUnlessIsInstance(IKPictureTakerShowEmptyPictureKey, unicode)



if __name__ == "__main__":
    main()
