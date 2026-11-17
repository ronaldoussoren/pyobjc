from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import PhotosUI


class TestPHPicker(TestCase):
    def test_enums(self):
        self.assertIsEnumType(PhotosUI.PHPickerConfigurationAssetRepresentationMode)
        self.assertEqual(
            PhotosUI.PHPickerConfigurationAssetRepresentationModeAutomatic, 0
        )
        self.assertEqual(
            PhotosUI.PHPickerConfigurationAssetRepresentationModeCurrent, 1
        )
        self.assertEqual(
            PhotosUI.PHPickerConfigurationAssetRepresentationModeCompatible, 2
        )

        self.assertIsEnumType(PhotosUI.PHPickerConfigurationSelection)
        self.assertEqual(PhotosUI.PHPickerConfigurationSelectionDefault, 0)
        self.assertEqual(PhotosUI.PHPickerConfigurationSelectionOrdered, 1)
        self.assertEqual(PhotosUI.PHPickerConfigurationSelectionContinuous, 2)
        self.assertEqual(PhotosUI.PHPickerConfigurationSelectionContinuousAndOrdered, 3)

        self.assertIsEnumType(PhotosUI.PHPickerMode)
        self.assertEqual(PhotosUI.PHPickerModeDefault, 0)
        self.assertEqual(PhotosUI.PHPickerModeCompact, 1)

        self.assertIsEnumType(PhotosUI.PHPickerCapabilities)
        self.assertEqual(PhotosUI.PHPickerCapabilitiesNone, 0)
        self.assertEqual(PhotosUI.PHPickerCapabilitiesSearch, 1 << 0)
        self.assertEqual(PhotosUI.PHPickerCapabilitiesStagingArea, 1 << 1)
        self.assertEqual(PhotosUI.PHPickerCapabilitiesCollectionNavigation, 1 << 2)
        self.assertEqual(PhotosUI.PHPickerCapabilitiesSelectionActions, 1 << 3)
        self.assertEqual(
            PhotosUI.PHPickerCapabilitiesSensitivityAnalysisIntervention, 1 << 4
        )
        self.assertEqual(
            PhotosUI.PHPickerCapabilitiesAutomaticModalInPresentation, 1 << 5
        )
        self.assertEqual(
            PhotosUI.PHPickerCapabilitiesAutomaticPreferredContentSize, 1 << 6
        )
        self.assertEqual(PhotosUI.PHPickerCapabilitiesSidebar, 1 << 7)

        self.assertIsEnumType(PhotosUI.PHPickerMetadataOptions)
        self.assertEqual(PhotosUI.PHPickerMetadataOptionsNone, 0)
        self.assertEqual(PhotosUI.PHPickerMetadataOptionsRemoveLocation, 1 << 0)
        self.assertEqual(PhotosUI.PHPickerMetadataOptionsRemoveCaptions, 1 << 1)
        self.assertEqual(
            PhotosUI.PHPickerMetadataOptionsRemoveAppleReferenceImage, 1 << 2
        )
        self.assertEqual(PhotosUI.PHPickerMetadataOptionsRemoveKeywords, 1 << 3)

        self.assertIsEnumType(PhotosUI.PHPickerResultThumbnailSize)
        self.assertEqual(PhotosUI.PHPickerResultThumbnailSizeSmall, 1)
        self.assertEqual(PhotosUI.PHPickerResultThumbnailSizeStandard, 2)

        self.assertIsEnumType(PhotosUI.PHPickerSecondaryButtonType)
        self.assertEqual(PhotosUI.PHPickerSecondaryButtonTypeAutomatic, 0)
        self.assertEqual(PhotosUI.PHPickerSecondaryButtonTypeNone, 1)
        self.assertEqual(PhotosUI.PHPickerSecondaryButtonTypeCancel, 2)
        self.assertEqual(PhotosUI.PHPickerSecondaryButtonTypeBack, 3)
        self.assertEqual(PhotosUI.PHPickerSecondaryButtonTypeClose, 4)
        self.assertEqual(PhotosUI.PHPickerSecondaryButtonTypeClear, 5)

    @min_os_level("27.3")
    def test_methods(self):
        self.assertArgIsBlock(
            PhotosUI.PHPickerResult.requestThumbnailImageURLForPreferredSize_resultHandler_,
            1,
            b"v@@",
        )

    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("PHPickerViewControllerDelegate", PhotosUI)
