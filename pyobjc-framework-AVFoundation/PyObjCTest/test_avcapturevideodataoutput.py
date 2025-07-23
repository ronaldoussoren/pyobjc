import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestAVCaptureVideoDataOutput(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.setAlwaysDiscardsLateVideoFrames_, 0
        )

    @min_os_level("12.0")
    def testMethodsTundra(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.alwaysDiscardsLateVideoFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.setAlwaysDiscardsLateVideoFrames_,
            0,
        )

    @min_os_level("26.0")
    def testMethods26_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.preparesCellularRadioForNetworkConnection
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.setPreparesCellularRadioForNetworkConnection_,
            0,
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.preservesDynamicHDRMetadata
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.setPreservesDynamicHDRMetadata_, 0
        )

    @min_os_level("26.0")
    def test_methods_tundra26_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.preparesCellularRadioForNetworkConnection
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.setPreparesCellularRadioForNetworkConnection_,
            0,
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.preservesDynamicHDRMetadata
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.setPreservesDynamicHDRMetadata_,
            0,
        )

    @min_sdk_level("10.7")
    def testProtocols(self):
        self.assertProtocolExists("AVCaptureVideoDataOutputSampleBufferDelegate")
