import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureAncillaryDataEncoder(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AVFoundation.AVCaptureAncillaryDataUserKey, str)

    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsInstance(
            AVFoundation.AVCaptureAncillaryDataUserKeyRDD18InstanceUID, str
        )
        self.assertIsInstance(
            AVFoundation.AVCaptureAncillaryDataUserKeyRDD18UDAMSetVersion, str
        )
        self.assertIsInstance(
            AVFoundation.AVCaptureAncillaryDataUserKeyRDD18UserItems, str
        )

    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureAncillaryDataEncoder.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureAncillaryDataEncoder.setEnabled_, 0)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureAncillaryDataEncoder.setRDD18AncillaryData_forTag_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVCaptureAncillaryDataEncoder.setRDD18AncillaryData_forTag_error_,
            2,
        )
