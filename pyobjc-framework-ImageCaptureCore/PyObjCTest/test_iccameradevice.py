import ImageCaptureCore
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
    os_level_between,
)


class TestICCameraDeviceHelper(ImageCaptureCore.NSObject):
    def didDownloadFile_error_options_contextInfo_(self, a, b, c, d):
        pass

    def didReceiveDownloadProgressForFile_downloadedBytes_maxBytes_(self, a, b, c):
        pass


class TestICCameraDevice(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(ImageCaptureCore.ICDeleteError, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICDeleteResult, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICUploadOption, str)

    def testConstants(self):
        self.assertIsInstance(ImageCaptureCore.ICCameraDeviceCanTakePicture, str)
        self.assertIsInstance(
            ImageCaptureCore.ICCameraDeviceCanTakePictureUsingShutterReleaseOnCamera,
            str,
        )
        self.assertIsInstance(ImageCaptureCore.ICCameraDeviceCanDeleteOneFile, str)
        self.assertIsInstance(ImageCaptureCore.ICCameraDeviceCanDeleteAllFiles, str)
        self.assertIsInstance(ImageCaptureCore.ICCameraDeviceCanSyncClock, str)
        self.assertIsInstance(ImageCaptureCore.ICCameraDeviceCanReceiveFile, str)
        self.assertIsInstance(ImageCaptureCore.ICCameraDeviceCanAcceptPTPCommands, str)
        self.assertIsInstance(ImageCaptureCore.ICDownloadsDirectoryURL, str)
        self.assertIsInstance(ImageCaptureCore.ICSaveAsFilename, str)
        self.assertIsInstance(ImageCaptureCore.ICSavedFilename, str)
        self.assertIsInstance(ImageCaptureCore.ICSavedAncillaryFiles, str)
        self.assertIsInstance(ImageCaptureCore.ICOverwrite, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteAfterSuccessfulDownload, str)
        self.assertIsInstance(ImageCaptureCore.ICDownloadSidecarFiles, str)

        self.assertEqual(ImageCaptureCore.ICMediaPresentationConvertedAssets, 1)
        self.assertEqual(ImageCaptureCore.ICMediaPresentationOriginalAssets, 2)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(ImageCaptureCore.ICDeleteSuccessful, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteCanceled, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteFailed, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteErrorReadOnly, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteErrorFileMissing, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteErrorDeviceMissing, str)
        self.assertIsInstance(ImageCaptureCore.ICDeleteErrorCanceled, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(ImageCaptureCore.ICTruncateAfterSuccessfulDownload, str)

    @os_level_between("10.11", "10.11")
    def testConstants10_11(self):
        self.assertIsInstance(ImageCaptureCore.ICCameraDeviceSupportsFastPTP, str)

    def testProtocolObjects(self):
        self.assertProtocolExists("ICCameraDeviceDelegate")

    @min_sdk_level("10.7")
    def testProtocolObjects10_7(self):
        self.assertProtocolExists("ICCameraDeviceDownloadDelegate")

    def testProtocolMethods(self):
        self.assertArgHasType(
            TestICCameraDeviceHelper.didDownloadFile_error_options_contextInfo_,
            3,
            b"^v",
        )
        self.assertArgHasType(
            TestICCameraDeviceHelper.didReceiveDownloadProgressForFile_downloadedBytes_maxBytes_,
            1,
            b"q",
        )
        self.assertArgHasType(
            TestICCameraDeviceHelper.didReceiveDownloadProgressForFile_downloadedBytes_maxBytes_,
            2,
            b"q",
        )

    def testMethods(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraDevice.isLocked)
        self.assertResultIsBOOL(
            ImageCaptureCore.ICCameraDevice.isAccessRestrictedAppleDevice
        )
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraDevice.tetheredCaptureEnabled)
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraDevice.batteryLevelAvailable)
        self.assertResultIsBOOL(
            ImageCaptureCore.ICCameraDevice.isAccessRestrictedAppleDevice
        )
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraDevice.tetheredCaptureEnabled)
        self.assertArgIsSEL(
            ImageCaptureCore.ICCameraDevice.requestDownloadFile_options_downloadDelegate_didDownloadSelector_contextInfo_,
            3,
            b"v@:@@@^v",
        )
        self.assertArgIsSEL(
            ImageCaptureCore.ICCameraDevice.requestUploadFile_options_uploadDelegate_didUploadSelector_contextInfo_,
            3,
            b"v@:@@^v",
        )
        self.assertArgIsSEL(
            ImageCaptureCore.ICCameraDevice.requestReadDataFromFile_atOffset_length_readDelegate_didReadDataSelector_contextInfo_,
            4,
            b"v@:@@@^v",
        )
        self.assertArgIsSEL(
            ImageCaptureCore.ICCameraDevice.requestSendPTPCommand_outData_sendCommandDelegate_didSendCommandSelector_contextInfo_,
            3,
            b"v@:@@@@^v",
        )

    @min_os_level("10.12")
    def test_methods10_10(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraDevice.iCloudPhotosEnabled)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICCameraDevice.isEjectable)
        self.assertArgIsBlock(
            ImageCaptureCore.ICCameraDevice.requestDeleteFiles_deleteFailed_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ImageCaptureCore.ICCameraDevice.requestDeleteFiles_deleteFailed_completion_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            ImageCaptureCore.ICCameraDevice.requestSendPTPCommand_outData_completion_,
            2,
            b"v@@@",
        )
