
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str


class TestImageKitDeprecatedHelper (NSObject):
    def numberOfCellsInImageBrowser_(self, b): return 1
    def imageBrowser_cellAtIndex_(self, b, idx): return None
    def imageBrowser_moveCellsAtIndexes_toIndex_(self, b, st, i): return True



class TestImageKitDeprecated (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertEqual(IKImagePickerAllowsVideoCaptureKey, IKPictureTakerAllowsVideoCaptureKey)
        self.assertEqual(IKImagePickerAllowsFileChoosingKey, IKPictureTakerAllowsFileChoosingKey)
        self.assertEqual(IKImagePickerShowRecentPictureKey, IKPictureTakerShowRecentPictureKey)
        self.assertEqual(IKImagePickerUpdateRecentPictureKey, IKPictureTakerUpdateRecentPictureKey)
        self.assertEqual(IKImagePickerAllowsEditingKey, IKPictureTakerAllowsEditingKey)
        self.assertEqual(IKImagePickerShowEffectsKey, IKPictureTakerShowEffectsKey)
        self.assertEqual(IKImagePickerInformationalTextKey, IKPictureTakerInformationalTextKey)
        self.assertEqual(IKImagePickerImageTransformsKey, IKPictureTakerImageTransformsKey)
        self.assertEqual(IKImagePickerOutputImageMaxSizeKey, IKPictureTakerOutputImageMaxSizeKey)
        self.assertEqual(IKImagePickerCropAreaSizeKey, IKPictureTakerCropAreaSizeKey)

        self.assertIsInstance(IKPictureTakerShowAddressBookPicture, unicode)
        self.assertIsInstance(IKPictureTakerShowEmptyPicture, unicode)

    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsSEL(IKImagePicker.beginImagePickerWithDelegate_didEndSelector_contextInfo_, 1, b'v@:@' + objc._C_NSUInteger + b'^v')
        self.assertArgIsSEL(IKImagePicker.beginImagePickerSheetForWindow_withDelegate_didEndSelector_contextInfo_, 2, b'v@:@' + objc._C_NSUInteger + b'^v')

    @min_os_level('10.5')
    def testProtocols(self):
        self.assertIsInstance(protocols.IKImageBrowserDataSourceDeprecated, objc.informal_protocol)

        self.assertResultHasType(TestImageKitDeprecatedHelper.numberOfCellsInImageBrowser_, objc._C_NSUInteger)
        self.assertArgHasType(TestImageKitDeprecatedHelper.imageBrowser_cellAtIndex_, 1, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestImageKitDeprecatedHelper.imageBrowser_moveCellsAtIndexes_toIndex_)
        self.assertArgHasType(TestImageKitDeprecatedHelper.imageBrowser_moveCellsAtIndexes_toIndex_, 2, objc._C_NSUInteger)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(IKImageBrowserCellLayerTypeBackground, unicode)
        self.assertIsInstance(IKImageBrowserCellLayerTypeForeground, unicode)
        self.assertIsInstance(IKImageBrowserCellLayerTypeSelection, unicode)
        self.assertIsInstance(IKImageBrowserCellLayerTypePlaceHolder, unicode)

if __name__ == "__main__":
    main()
