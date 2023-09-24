from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import PhotosUI


class TestPHPicker(TestCase):
    def test_constants(self):
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

    @min_os_level("13.0")
    def testClasses(self):
        self.assertClassIsFinal(PhotosUI.PHPickerFilter)
        self.assertClassIsFinal(PhotosUI.PHPickerConfiguration)
        self.assertClassIsFinal(PhotosUI.PHPickerResult)
        self.assertClassIsFinal(PhotosUI.PHPickerViewController)

    @min_sdk_level("13.0")
    def testProtocols(self):
        self.assertProtocolExists("PHPickerViewControllerDelegate")
