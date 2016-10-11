from PyObjCTools.TestSupport import *

from ImageCaptureCore import *


class TestICCameraDeviceHelper (NSObject):
    def didDownloadFile_error_options_contextInfo_(self, a, b, c, d): pass
    def didReceiveDownloadProgressForFile_downloadedBytes_maxBytes_(self, a, b, c): pass

class TestICCameraDevice (TestCase):
    def testConstants(self):
        self.assertIsInstance(ICCameraDeviceCanTakePicture, unicode)
        self.assertIsInstance(ICCameraDeviceCanTakePictureUsingShutterReleaseOnCamera, unicode)
        self.assertIsInstance(ICCameraDeviceCanDeleteOneFile, unicode)
        self.assertIsInstance(ICCameraDeviceCanDeleteAllFiles, unicode)
        self.assertIsInstance(ICCameraDeviceCanSyncClock, unicode)
        self.assertIsInstance(ICCameraDeviceCanReceiveFile, unicode)
        self.assertIsInstance(ICCameraDeviceCanAcceptPTPCommands, unicode)
        self.assertIsInstance(ICDownloadsDirectoryURL, unicode)
        self.assertIsInstance(ICSaveAsFilename, unicode)
        self.assertIsInstance(ICSavedFilename, unicode)
        self.assertIsInstance(ICSavedAncillaryFiles, unicode)
        self.assertIsInstance(ICOverwrite, unicode)
        self.assertIsInstance(ICDeleteAfterSuccessfulDownload, unicode)
        self.assertIsInstance(ICDownloadSidecarFiles, unicode)

    @os_level_between('10.11', '10.11')
    def testConstants10_11(self):
        self.assertIsInstance(ICCameraDeviceSupportsFastPTP, unicode)

    def testProtocolObjects(self):
        objc.protocolNamed('ICCameraDeviceDelegate')

    @min_sdk_level('10.7')
    def testProtocolObjects10_7(self):
        objc.protocolNamed('ICCameraDeviceDownloadDelegate')

    def testProtocolMethods(self):
        self.assertArgHasType(TestICCameraDeviceHelper.didDownloadFile_error_options_contextInfo_, 3, b'^v')
        self.assertArgHasType(TestICCameraDeviceHelper.didReceiveDownloadProgressForFile_downloadedBytes_maxBytes_, 1, b'q')
        self.assertArgHasType(TestICCameraDeviceHelper.didReceiveDownloadProgressForFile_downloadedBytes_maxBytes_, 2, b'q')

    def testMethods(self):
        self.assertResultIsBOOL(ICCameraDevice.batteryLevelAvailable)
        self.assertResultIsBOOL(ICCameraDevice.isAccessRestrictedAppleDevice)
        self.assertResultIsBOOL(ICCameraDevice.tetheredCaptureEnabled)
        self.assertArgIsBOOL(ICCameraDevice.setTetheredCaptureEnabled_, 0)
        self.assertArgIsSEL(ICCameraDevice.requestDownloadFile_options_downloadDelegate_didDownloadSelector_contextInfo_, 3, b'v@:@@@^v')
        self.assertArgIsSEL(ICCameraDevice.requestUploadFile_options_uploadDelegate_didUploadSelector_contextInfo_, 3, b'v@:@@^v')
        self.assertArgIsSEL(ICCameraDevice.requestReadDataFromFile_atOffset_length_readDelegate_didReadDataSelector_contextInfo_, 4, b'v@:@@@^v')
        self.assertArgIsSEL(ICCameraDevice.requestSendPTPCommand_outData_sendCommandDelegate_didSendCommandSelector_contextInfo_, 3, b'v@:@@@@^v')

if __name__ == "__main__":
    main()
