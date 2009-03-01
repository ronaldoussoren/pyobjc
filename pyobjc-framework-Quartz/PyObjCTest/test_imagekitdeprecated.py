
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *


class TestImageKitDeprecatedHelper (NSObject):
    def numberOfCellsInImageBrowser_(self, b): return 1
    def imageBrowser_cellAtIndex_(self, b, idx): return None
    def imageBrowser_moveCellsAtIndexes_toIndex_(self, b, st, i): return True



class TestImageKitDeprecated (TestCase):
    def testConstants(self):
        self.failUnlessEqual(IKImagePickerAllowsVideoCaptureKey, IKPictureTakerAllowsVideoCaptureKey)
        self.failUnlessEqual(IKImagePickerAllowsFileChoosingKey, IKPictureTakerAllowsFileChoosingKey)
        self.failUnlessEqual(IKImagePickerShowRecentPictureKey, IKPictureTakerShowRecentPictureKey)
        self.failUnlessEqual(IKImagePickerUpdateRecentPictureKey, IKPictureTakerUpdateRecentPictureKey)
        self.failUnlessEqual(IKImagePickerAllowsEditingKey, IKPictureTakerAllowsEditingKey)
        self.failUnlessEqual(IKImagePickerShowEffectsKey, IKPictureTakerShowEffectsKey)
        self.failUnlessEqual(IKImagePickerInformationalTextKey, IKPictureTakerInformationalTextKey)
        self.failUnlessEqual(IKImagePickerImageTransformsKey, IKPictureTakerImageTransformsKey)
        self.failUnlessEqual(IKImagePickerOutputImageMaxSizeKey, IKPictureTakerOutputImageMaxSizeKey)
        self.failUnlessEqual(IKImagePickerCropAreaSizeKey, IKPictureTakerCropAreaSizeKey)

        self.failUnlessIsInstance(IKPictureTakerShowAddressBookPicture, unicode)
        self.failUnlessIsInstance(IKPictureTakerShowEmptyPicture, unicode)

    def testMethods(self):
        self.failUnlessArgIsSEL(IKImagePicker.beginImagePickerWithDelegate_didEndSelector_contextInfo_, 1, 'v@:@' + objc._C_NSUInteger + '^v')
        self.failUnlessArgIsSEL(IKImagePicker.beginImagePickerSheetForWindow_withDelegate_didEndSelector_contextInfo_, 2, 'v@:@' + objc._C_NSUInteger + '^v')

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.IKImageBrowserDataSourceDeprecated, objc.informal_protocol)

        self.failUnlessResultHasType(TestImageKitDeprecatedHelper.numberOfCellsInImageBrowser_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestImageKitDeprecatedHelper.imageBrowser_cellAtIndex_, 1, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestImageKitDeprecatedHelper.imageBrowser_moveCellsAtIndexes_toIndex_)
        self.failUnlessArgHasType(TestImageKitDeprecatedHelper.imageBrowser_moveCellsAtIndexes_toIndex_, 2, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
