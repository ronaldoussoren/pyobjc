import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptionConversionValidator(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVCaptionConversionValidatorStatus)

    def test_constants(self):
        self.assertEqual(AVFoundation.AVCaptionConversionValidatorStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVCaptionConversionValidatorStatusValidating, 1)
        self.assertEqual(AVFoundation.AVCaptionConversionValidatorStatusCompleted, 2)
        self.assertEqual(AVFoundation.AVCaptionConversionValidatorStatusStopped, 3)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            AVFoundation.AVCaptionConversionWarningTypeExcessMediaData, str
        )
        self.assertIsInstance(
            AVFoundation.AVCaptionConversionAdjustmentTypeTimeRange, str
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptionConversionValidator.validateCaptionConversionWithWarningHandler_,
            0,
            b"v@",
        )
