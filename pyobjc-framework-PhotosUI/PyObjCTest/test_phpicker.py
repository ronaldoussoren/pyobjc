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

    @min_os_level("13.0")
    def testClasses(self):
        self.assertClassIsFinal(PhotosUI.PHPickerFilter)
        self.assertClassIsFinal(PhotosUI.PHPickerConfiguration)
        self.assertClassIsFinal(PhotosUI.PHPickerResult)
        self.assertClassIsFinal(PhotosUI.PHPickerViewController)

    @min_sdk_level("13.0")
    def testProtocols(self):
        self.assertProtocolExists("PHPickerViewControllerDelegate")
