import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase


class TestICCameraDevice(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ImageCaptureCore.ICEXIFOrientationType)

    def testConstants(self):
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation1, 1)
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation2, 2)
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation3, 3)
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation4, 4)
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation5, 5)
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation6, 6)
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation7, 7)
        self.assertEqual(ImageCaptureCore.ICEXIFOrientation8, 8)

        self.assertEqual(ImageCaptureCore.ICReturnSuccess, 0)
        self.assertEqual(ImageCaptureCore.ICReturnInvalidParam, -9922)
        self.assertEqual(ImageCaptureCore.ICReturnCommunicationTimedOut, -9923)
        self.assertEqual(ImageCaptureCore.ICReturnScanOperationCanceled, -9924)
        self.assertEqual(ImageCaptureCore.ICReturnScannerInUseByLocalUser, -9925)
        self.assertEqual(ImageCaptureCore.ICReturnScannerInUseByRemoteUser, -9926)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToOpenSession, -9927)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToCloseSession, -9928)
        self.assertEqual(
            ImageCaptureCore.ICReturnScannerFailedToSelectFunctionalUnit, -9929
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnScannerFailedToCompleteOverviewScan, -9930
        )
        self.assertEqual(ImageCaptureCore.ICReturnScannerFailedToCompleteScan, -9931)
        self.assertEqual(
            ImageCaptureCore.ICReturnReceivedUnsolicitedScannerStatusInfo, -9932
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnReceivedUnsolicitedScannerErrorInfo, -9933
        )
        self.assertEqual(ImageCaptureCore.ICReturnDownloadFailed, -9934)
        self.assertEqual(ImageCaptureCore.ICReturnUploadFailed, -9935)
        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToCompletePassThroughCommand, -9936
        )
        self.assertEqual(ImageCaptureCore.ICReturnDownloadCanceled, -9937)
        self.assertEqual(ImageCaptureCore.ICReturnFailedToEnabeTethering, -9938)
        self.assertEqual(ImageCaptureCore.ICReturnFailedToDisabeTethering, -9939)
        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToCompleteSendMessageRequest, -9940
        )
        self.assertEqual(ImageCaptureCore.ICReturnDeleteFilesFailed, -9941)
        self.assertEqual(ImageCaptureCore.ICReturnDeleteFilesCanceled, -9942)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceIsPasscodeLocked, -9943)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToTakePicture, -9944)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareNotInstalled, -9945)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareIsBeingInstalled, -9946)
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationCompleted, -9947
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationCanceled, -9948
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationFailed, -9949
        )
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareNotAvailable, -9950)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCouldNotPair, -9951)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCouldNotUnpair, -9952)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceNeedsCredentials, -9953)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceIsBusyEnumerating, -9954)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCommandGeneralFailure, -9955)

        self.assertEqual(ImageCaptureCore.ICReturnCodeThumbnailOffset, -21000)
        self.assertEqual(ImageCaptureCore.ICReturnCodeMetadataOffset, -21050)
        self.assertEqual(ImageCaptureCore.ICReturnCodeDownloadOffset, -21100)
        self.assertEqual(ImageCaptureCore.ICReturnCodeDeleteOffset, -21150)
        self.assertEqual(ImageCaptureCore.ICReturnCodeExFATOffset, -21200)
        self.assertEqual(ImageCaptureCore.ICReturnCodePTPOffset, -21250)
        self.assertEqual(ImageCaptureCore.ICReturnCodeSystemOffset, -21300)
        self.assertEqual(ImageCaptureCore.ICReturnCodeDeviceOffset, -21350)
        self.assertEqual(ImageCaptureCore.ICReturnCodeDeviceConnection, -21400)
        self.assertEqual(ImageCaptureCore.ICReturnCodeObjectOffset, -21450)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToCompleteTransfer, -9956)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToSendData, -9957)
        self.assertEqual(ImageCaptureCore.ICReturnSessionNotOpened, -9958)
        self.assertEqual(
            ImageCaptureCore.ICReturnThumbnailNotAvailable,
            ImageCaptureCore.ICReturnCodeThumbnailOffset,
        )

        self.assertEqual(
            ImageCaptureCore.ICReturnErrorDeviceEjected,
            ImageCaptureCore.ICReturnCodeSystemOffset,
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnConnectionDriverExited,
            ImageCaptureCore.ICReturnCodeDeviceOffset,
        )
        self.assertEqual(ImageCaptureCore.ICReturnMultiErrorDictionary, -30000)

        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeCommunicationErr, -9900)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceNotFoundErr, -9901)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceNotOpenErr, -9902)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeFileCorruptedErr, -9903)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeIOPendingErr, -9904)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeInvalidObjectErr, -9905)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeInvalidPropertyErr, -9906)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeIndexOutOfRangeErr, -9907)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodePropertyTypeNotFoundErr, -9908
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeCannotYieldDevice, -9909)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDataTypeNotFoundErr, -9910)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceMemoryAllocationErr, -9911
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceInternalErr, -9912)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceInvalidParamErr, -9913
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceAlreadyOpenErr, -9914)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceLocationIDNotFoundErr, -9915
        )
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceGUIDNotFoundErr, -9916
        )
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceIOServicePathNotFoundErr, -9917
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceUnsupportedErr, -9918)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeFrameworkInternalErr, -9919)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeExtensionInternalErr, -9920)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeInvalidSessionErr, -9921)

        self.assertEqual(ImageCaptureCore.ICReturnSuccess, 0)
        self.assertEqual(ImageCaptureCore.ICReturnInvalidParam, -9922)
        self.assertEqual(ImageCaptureCore.ICReturnCommunicationTimedOut, -9923)
        self.assertEqual(ImageCaptureCore.ICReturnScanOperationCanceled, -9924)
        self.assertEqual(ImageCaptureCore.ICReturnScannerInUseByLocalUser, -9925)
        self.assertEqual(ImageCaptureCore.ICReturnScannerInUseByRemoteUser, -9926)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToOpenSession, -9927)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToCloseSession, -9928)
        self.assertEqual(
            ImageCaptureCore.ICReturnScannerFailedToSelectFunctionalUnit, -9929
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnScannerFailedToCompleteOverviewScan, -9930
        )
        self.assertEqual(ImageCaptureCore.ICReturnScannerFailedToCompleteScan, -9931)
        self.assertEqual(
            ImageCaptureCore.ICReturnReceivedUnsolicitedScannerStatusInfo, -9932
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnReceivedUnsolicitedScannerErrorInfo, -9933
        )
        self.assertEqual(ImageCaptureCore.ICReturnDownloadFailed, -9934)
        self.assertEqual(ImageCaptureCore.ICReturnUploadFailed, -9935)
        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToCompletePassThroughCommand, -9936
        )
        self.assertEqual(ImageCaptureCore.ICReturnDownloadCanceled, -9937)
        self.assertEqual(ImageCaptureCore.ICReturnFailedToEnabeTethering, -9938)
        self.assertEqual(ImageCaptureCore.ICReturnFailedToDisabeTethering, -9939)
        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToCompleteSendMessageRequest, -9940
        )
        self.assertEqual(ImageCaptureCore.ICReturnDeleteFilesFailed, -9941)
        self.assertEqual(ImageCaptureCore.ICReturnDeleteFilesCanceled, -9942)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToTakePicture, -9944)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareNotInstalled, -9945)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareIsBeingInstalled, -9946)
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationCompleted, -9947
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationCanceled, -9948
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationFailed, -9949
        )
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareNotAvailable, -9950)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCouldNotPair, -9951)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCouldNotUnpair, -9952)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceNeedsCredentials, -9953)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceIsBusyEnumerating, -9954)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCommandGeneralFailure, -9955)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToCompleteTransfer, -9956)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToSendData, -9957)
        self.assertEqual(ImageCaptureCore.ICReturnSessionNotOpened, -9958)
        self.assertEqual(ImageCaptureCore.ICReturnExFATVolumeInvalid, 21200)
        self.assertEqual(ImageCaptureCore.ICReturnMultiErrorDictionary, -30000)
        self.assertEqual(
            ImageCaptureCore.ICReturnDownloadPathInvalid,
            ImageCaptureCore.ICReturnCodeDownloadOffset,
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnCodeObjectDoesNotExist,
            ImageCaptureCore.ICReturnCodeObjectOffset,
        )

        self.assertEqual(ImageCaptureCore.ICReturnThumbnailNotAvailable, -21000)
        self.assertEqual(ImageCaptureCore.ICReturnThumbnailAlreadyFetching, -20999)
        self.assertEqual(ImageCaptureCore.ICReturnThumbnailCanceled, -20098)
        self.assertEqual(ImageCaptureCore.ICReturnThumbnailInvalid, -20097)

        self.assertEqual(ImageCaptureCore.ICReturnMetadataNotAvailable, -20150)
        self.assertEqual(ImageCaptureCore.ICReturnMetadataAlreadyFetching, -20149)
        self.assertEqual(ImageCaptureCore.ICReturnMetadataCanceled, -20148)
        self.assertEqual(ImageCaptureCore.ICReturnMetadataInvalid, -20147)

        self.assertEqual(ImageCaptureCore.ICReturnConnectionDriverExited, -21350)
        self.assertEqual(
            ImageCaptureCore.ICReturnConnectionClosedSessionSuddenly, -21349
        )
        self.assertEqual(ImageCaptureCore.ICReturnConnectionEjectedSuddenly, -21348)
        self.assertEqual(ImageCaptureCore.ICReturnConnectionSessionAlreadyOpen, -21347)
        self.assertEqual(ImageCaptureCore.ICReturnConnectionEjectFailed, -21346)
        self.assertEqual(ImageCaptureCore.ICReturnConnectionFailedToOpen, -21345)
        self.assertEqual(ImageCaptureCore.ICReturnConnectionFailedToOpenDevice, -21344)
        self.assertEqual(
            ImageCaptureCore.ICReturnConnectionNotAuthorizedToOpenDevice, -21343
        )
        self.assertEqual(ImageCaptureCore.ICReturnPTPFailedToSendCommand, -21250)
        self.assertEqual(ImageCaptureCore.ICReturnPTPNotAuthorizedToSendCommand, -21249)

        self.assertEqual(ImageCaptureCore.ICReturnDownloadPathInvalid, -21100)
        self.assertEqual(ImageCaptureCore.ICReturnDownloadFileWritable, -21099)

        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeCommunicationErr, -9900)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceNotFoundErr, -9901)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceNotOpenErr, -9902)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeFileCorruptedErr, -9903)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeIOPendingErr, -9904)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeInvalidObjectErr, -9905)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeInvalidPropertyErr, -9906)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeIndexOutOfRangeErr, -9907)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodePropertyTypeNotFoundErr, -9908
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeCannotYieldDevice, -9909)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDataTypeNotFoundErr, -9910)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceMemoryAllocationErr, -9911
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceInternalErr, -9912)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceInvalidParamErr, -9913
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceAlreadyOpenErr, -9914)
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceLocationIDNotFoundErr, -9915
        )
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceGUIDNotFoundErr, -9916
        )
        self.assertEqual(
            ImageCaptureCore.ICLegacyReturnCodeDeviceIOServicePathNotFoundErr, -9917
        )
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeDeviceUnsupportedErr, -9918)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeFrameworkInternalErr, -9919)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeExtensionInternalErr, -9920)
        self.assertEqual(ImageCaptureCore.ICLegacyReturnCodeInvalidSessionErr, -9921)

        self.assertEqual(ImageCaptureCore.ICReturnSuccess, 0)
        self.assertEqual(ImageCaptureCore.ICReturnInvalidParam, -9922)
        self.assertEqual(ImageCaptureCore.ICReturnCommunicationTimedOut, -9923)
        self.assertEqual(ImageCaptureCore.ICReturnScanOperationCanceled, -9924)
        self.assertEqual(ImageCaptureCore.ICReturnScannerInUseByLocalUser, -9925)
        self.assertEqual(ImageCaptureCore.ICReturnScannerInUseByRemoteUser, -9926)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToOpenSession, -9927)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToCloseSession, -9928)
        self.assertEqual(
            ImageCaptureCore.ICReturnScannerFailedToSelectFunctionalUnit, -9929
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnScannerFailedToCompleteOverviewScan, -9930
        )
        self.assertEqual(ImageCaptureCore.ICReturnScannerFailedToCompleteScan, -9931)
        self.assertEqual(
            ImageCaptureCore.ICReturnReceivedUnsolicitedScannerStatusInfo, -9932
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnReceivedUnsolicitedScannerErrorInfo, -9933
        )
        self.assertEqual(ImageCaptureCore.ICReturnDownloadFailed, -9934)
        self.assertEqual(ImageCaptureCore.ICReturnUploadFailed, -9935)
        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToCompletePassThroughCommand, -9936
        )
        self.assertEqual(ImageCaptureCore.ICReturnDownloadCanceled, -9937)
        self.assertEqual(ImageCaptureCore.ICReturnFailedToEnabeTethering, -9938)
        self.assertEqual(ImageCaptureCore.ICReturnFailedToDisabeTethering, -9939)
        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToCompleteSendMessageRequest, -9940
        )
        self.assertEqual(ImageCaptureCore.ICReturnDeleteFilesFailed, -9941)
        self.assertEqual(ImageCaptureCore.ICReturnDeleteFilesCanceled, -9942)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceIsPasscodeLocked, -9943)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToTakePicture, -9944)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareNotInstalled, -9945)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareIsBeingInstalled, -9946)
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationCompleted, -9947
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationCanceled, -9948
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnDeviceSoftwareInstallationFailed, -9949
        )
        self.assertEqual(ImageCaptureCore.ICReturnDeviceSoftwareNotAvailable, -9950)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCouldNotPair, -9951)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCouldNotUnpair, -9952)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceNeedsCredentials, -9953)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceIsBusyEnumerating, -9954)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceCommandGeneralFailure, -9955)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToCompleteTransfer, -9956)
        self.assertEqual(ImageCaptureCore.ICReturnDeviceFailedToSendData, -9957)
        self.assertEqual(ImageCaptureCore.ICReturnSessionNotOpened, -9958)
        self.assertEqual(ImageCaptureCore.ICReturnExFATVolumeInvalid, 21200)
        self.assertEqual(ImageCaptureCore.ICReturnMultiErrorDictionary, -30000)

        self.assertEqual(ImageCaptureCore.ICReturnCodeObjectDoesNotExist, -21450)
        self.assertEqual(ImageCaptureCore.ICReturnCodeObjectDataOffsetInvalid, -21449)
        self.assertEqual(ImageCaptureCore.ICReturnCodeObjectCouldNotBeRead, -21448)
        self.assertEqual(ImageCaptureCore.ICReturnCodeObjectDataEmpty, -21447)
        self.assertEqual(ImageCaptureCore.ICReturnCodeObjectDataRequestTooLarge, -21446)

        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToEnableTethering,
            ImageCaptureCore.ICReturnFailedToEnabeTethering,
        )
        self.assertEqual(
            ImageCaptureCore.ICReturnFailedToDisableTethering,
            ImageCaptureCore.ICReturnFailedToDisabeTethering,
        )
