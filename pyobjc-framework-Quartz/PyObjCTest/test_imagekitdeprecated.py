from PyObjCTools.TestSupport import TestCase, max_os_level
import Quartz
import objc


class TestImageKitDeprecatedHelper(Quartz.NSObject):
    def numberOfCellsInImageBrowser_(self, b):
        return 1

    def imageBrowser_cellAtIndex_(self, b, idx):
        return None

    def imageBrowser_moveCellsAtIndexes_toIndex_(self, b, st, i):
        return True


class TestImageKitDeprecated(TestCase):
    def test_constants(self):
        self.assertEqual(
            Quartz.IKImagePickerAllowsVideoCaptureKey,
            Quartz.IKPictureTakerAllowsVideoCaptureKey,
        )
        self.assertEqual(
            Quartz.IKImagePickerAllowsFileChoosingKey,
            Quartz.IKPictureTakerAllowsFileChoosingKey,
        )
        self.assertEqual(
            Quartz.IKImagePickerShowRecentPictureKey,
            Quartz.IKPictureTakerShowRecentPictureKey,
        )
        self.assertEqual(
            Quartz.IKImagePickerUpdateRecentPictureKey,
            Quartz.IKPictureTakerUpdateRecentPictureKey,
        )
        self.assertEqual(
            Quartz.IKImagePickerAllowsEditingKey, Quartz.IKPictureTakerAllowsEditingKey
        )
        self.assertEqual(
            Quartz.IKImagePickerShowEffectsKey, Quartz.IKPictureTakerShowEffectsKey
        )
        self.assertEqual(
            Quartz.IKImagePickerInformationalTextKey,
            Quartz.IKPictureTakerInformationalTextKey,
        )
        self.assertEqual(
            Quartz.IKImagePickerImageTransformsKey,
            Quartz.IKPictureTakerImageTransformsKey,
        )
        self.assertEqual(
            Quartz.IKImagePickerOutputImageMaxSizeKey,
            Quartz.IKPictureTakerOutputImageMaxSizeKey,
        )
        self.assertEqual(
            Quartz.IKImagePickerCropAreaSizeKey, Quartz.IKPictureTakerCropAreaSizeKey
        )

        self.assertIsInstance(Quartz.IKPictureTakerShowAddressBookPicture, str)
        self.assertIsInstance(Quartz.IKPictureTakerShowEmptyPicture, str)
        self.assertIsInstance(Quartz.IKPictureTakerCropAreaSizeKey, str)

    @max_os_level("10.13")
    def test_constants_removed_10_13(self):
        self.assertIsInstance(Quartz.IKImageBrowserCellLayerTypeBackground, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellLayerTypeForeground, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellLayerTypeSelection, str)
        self.assertIsInstance(Quartz.IKImageBrowserCellLayerTypePlaceHolder, str)

    def test_methods(self):
        self.assertArgIsSEL(
            Quartz.IKImagePicker.beginImagePickerWithDelegate_didEndSelector_contextInfo_,
            1,
            b"v@:@" + objc._C_NSUInteger + b"^v",
        )
        self.assertArgIsSEL(
            Quartz.IKImagePicker.beginImagePickerSheetForWindow_withDelegate_didEndSelector_contextInfo_,
            2,
            b"v@:@" + objc._C_NSUInteger + b"^v",
        )

    def test_protocol_methods(self):
        # self.assertIsInstance(protocols.IKImageBrowserDataSourceDeprecated, objc.informal_protocol)

        self.assertResultHasType(
            TestImageKitDeprecatedHelper.numberOfCellsInImageBrowser_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestImageKitDeprecatedHelper.imageBrowser_cellAtIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestImageKitDeprecatedHelper.imageBrowser_moveCellsAtIndexes_toIndex_
        )
        self.assertArgHasType(
            TestImageKitDeprecatedHelper.imageBrowser_moveCellsAtIndexes_toIndex_,
            2,
            objc._C_NSUInteger,
        )
