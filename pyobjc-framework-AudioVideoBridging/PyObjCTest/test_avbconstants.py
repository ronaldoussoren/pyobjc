from PyObjCTools.TestSupport import TestCase
import AudioVideoBridging


class TestAVBConstants(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AudioVideoBridging.AVB17221ACMPFlags)
        self.assertIsEnumType(AudioVideoBridging.AVB17221ACMPMessageType)
        self.assertIsEnumType(AudioVideoBridging.AVB17221ACMPStatusCode)
        self.assertIsEnumType(AudioVideoBridging.AVB17221ADPControllerCapabilities)
        self.assertIsEnumType(AudioVideoBridging.AVB17221ADPEntityCapabilities)
        self.assertIsEnumType(AudioVideoBridging.AVB17221ADPListenerCapabilities)
        self.assertIsEnumType(AudioVideoBridging.AVB17221ADPTalkerCapabilities)
        self.assertIsEnumType(AudioVideoBridging.AVB17221AECPAddressAccessTLVMode)
        self.assertIsEnumType(AudioVideoBridging.AVB17221AECPMessageType)
        self.assertIsEnumType(AudioVideoBridging.AVB17221AECPStatusCode)
        self.assertIsEnumType(AudioVideoBridging.AVB17221AEMCommandType)

    def test_constants(self):
        self.assertIsInstance(AudioVideoBridging.AVBErrorDomain, str)

        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesDFUMode, 0x00000001
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesEFUMode, 0x00000001
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAddressAccessSupported,
            0x00000002,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesGatewayEntity, 0x00000004
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAEMSupported, 0x00000008
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesLegacyAVC, 0x00000010
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAssociationIDSupported,
            0x00000020,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAssociationIDValid,
            0x00000040,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesVendorUniqueSupported,
            0x00000080,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesClassASupported, 0x00000100
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesClassBSupported, 0x00000200
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesASSupported, 0x00000400
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesGPTPSupported, 0x00000400
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAEMAuthenticationSupported,
            0x00000800,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAEMAuthenticationRequired,
            0x00001000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAEMPersistentAcquireSupported,
            0x00002000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAEMIdenitifyControlIndexValid,
            0x00004000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesAEMInterfaceIndexValid,
            0x00008000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesGeneralControllerIgnore,
            0x00010000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesEntityNotReady, 0x00020000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesACMPAcquireWithAEM,
            0x00040000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesACMPAuthenticateWithAEM,
            0x00080000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesSupportsUDPv4ATDECC,
            0x00100000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesSupportsUDPv4Streaming,
            0x00200000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesSupportsUDPv6ATDECC,
            0x00400000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesSupportsUDPv6Streaming,
            0x00800000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPEntityCapabilitiesMultiplePTPInstances,
            0x01000000,
        )

        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesImplemented, 0x0001
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesHasOtherSource, 0x0200
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesHasControlSource, 0x0400
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesHasMediaClockSource, 0x0800
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesHasSMPTESource, 0x1000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesHasMIDISource, 0x2000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesHasAudioSource, 0x4000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPTalkerCapabilitiesHasVideoSource, 0x8000
        )

        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesImplemented, 0x0001
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesHasOtherSink, 0x0200
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesHasControlSink, 0x0400
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesHasMediaClockSink, 0x0800
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesHasSMPTESink, 0x1000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesHasMIDISink, 0x2000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesHasAudioSink, 0x4000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPListenerCapabilitiesHasVideoSink, 0x8000
        )

        self.assertEqual(
            AudioVideoBridging.AVB17221ADPControllerCapabilitiesImplemented, 0x00000001
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ADPControllerCapabilitiesHasLayer3Proxy,
            0x00000002,
        )

        self.assertEqual(AudioVideoBridging.AVB17221AECPMessageTypeAEMCommand, 0x0)
        self.assertEqual(AudioVideoBridging.AVB17221AECPMessageTypeAEMResponse, 0x1)
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPMessageTypeAddressAccessCommand, 0x2
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPMessageTypeAddressAccessResponse, 0x3
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPMessageTypeLegacyAVCCommand, 0x4
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPMessageTypeLegacyAVCResponse, 0x5
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPMessageTypeVendorUniqueCommand, 0x6
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPMessageTypeVendorUniqueResponse, 0x7
        )

        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusSuccess, 0x00)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusNotImplemented, 0x01)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusNoSuchDescriptor, 0x02)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusEntityLocked, 0x03)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusEntityAcquired, 0x04)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusNotAuthorized, 0x05)
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPStatusInsufficientPrivileges, 0x06
        )
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusBadArguments, 0x07)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusNoResources, 0x08)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusInProgress, 0x09)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusEntityMisbehaving, 0x0A)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusNotSupported, 0x0B)
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusStreamIsRunning, 0x0C)
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPStatusAddressAccessAddressTooLow, 0x02
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPStatusAddressAccessAddressTooHigh, 0x03
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPStatusAddressAccessAddressInvalid, 0x04
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPStatusAddressAccessTLVInvalid, 0x05
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPStatusAddressAccessDataInvalid, 0x06
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPStatusAddressAccessUnsupported, 0x07
        )
        self.assertEqual(AudioVideoBridging.AVB17221AECPStatusAVCFailure, 0x02)

        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeConnectTXCommand, 0x0
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeConnectTXResponse, 0x1
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeDisconnectTXCommand, 0x2
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeDisconnectTXResponse, 0x3
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeGetTXStateCommand, 0x4
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeGetTXStateResponse, 0x5
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeConnectRXCommand, 0x6
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeConnectRXResponse, 0x7
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeDisconnectRXCommand, 0x8
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeDisconnectRXResponse, 0x9
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeGetRXStateCommand, 0xA
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeGetRXStateResponse, 0xB
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeGetTXConnectionCommand, 0xC
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPMessageTypeGetTXConnectionResponse, 0xD
        )

        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusSuccess, 0x00)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusListenerUnknownID, 0x01)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusTalkerUnknownID, 0x02)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusTalkerDestMACFail, 0x03)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusTalkerNoStreamIndex, 0x04)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusTalkerNoBandwidth, 0x05)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusTalkerExclusive, 0x06)
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPStatusListenerTalkerTimeout, 0x07
        )
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusListenerExclusive, 0x08)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusStateUnavailable, 0x09)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusNotConnected, 0x0A)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusNoSuchConnection, 0x0B)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusUnableToSendMessage, 0x0C)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusTalkerMisbehaving, 0x0D)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusListenerMisbehaving, 0x0E)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusSRPFace, 0x0F)
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPStatusControllerNotAuthorized, 0x10
        )
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusIncompatibleRequest, 0x11)
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPStatusListenerInvalidConnection, 0x12
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPStatusListenerCanOnlyListenOnce, 0x13
        )
        self.assertEqual(AudioVideoBridging.AVB17221ACMPStatusNotSupported, 0x1F)

        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsNone, 0x0000)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsClassB, 0x0001)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsFastConnect, 0x0002)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsSavedState, 0x0004)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsStreamingWait, 0x0008)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsSupportsEncrypted, 0x0010)
        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsEncryptedPDU, 0x0020)
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPFlagsStreamingTalkerFailed, 0x0040
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPFlagsStreamingConnectedListenersValid, 0x0080
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221ACMPFlagsStreamingNoStreamReservationProtocol,
            0x0100,
        )
        self.assertEqual(AudioVideoBridging.AVB17221ACMPFlagsStreamingUsingUDP, 0x0200)

        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeAcquireEntity, 0x0000)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeLockEntity, 0x0001)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeEntityAvailable, 0x0002
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeControllerAvailable, 0x0003
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeReadDescriptor, 0x0004
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeWriteDescriptor, 0x0005
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetConfiguration, 0x0006
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetConfiguration, 0x0007
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetStreamFormat, 0x0008
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetStreamFormat, 0x0009
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetVideoFormat, 0x000A
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetVideoFormat, 0x000B
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetSensorFormat, 0x000C
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetSensorFormat, 0x000D
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeSetStreamInfo, 0x000E)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetStreamInfo, 0x000F)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeSetName, 0x0010)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetName, 0x0011)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetAssociationID, 0x0012
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetAssociationID, 0x0013
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetSamplingRate, 0x0014
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetSamplingRate, 0x0015
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetClockSource, 0x0016
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetClockSource, 0x0017
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeSetControl, 0x0018)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetControl, 0x0019)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeIncrementControl, 0x001A
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeDecrementControl, 0x001B
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetSignalSelector, 0x001C
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetSignalSelector, 0x001D
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeSetMixer, 0x001E)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetMixer, 0x001F)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeSetMatrix, 0x0020)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetMatrix, 0x0021)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeStartStreaming, 0x0022
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeStopStreaming, 0x0023)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeRegisterUnsolicitedNotification,
            0x0024,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeDeregisterUnsolicitedNotification,
            0x0025,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeIdentifyNotification, 0x0026
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetAVBInfo, 0x0027)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetASPath, 0x0028)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetCounters, 0x0029)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeReboot, 0x002A)
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetAudioMap, 0x002B)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAddAudioMapping, 0x002C
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeRemoveAudioMapping, 0x002D
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetVideoMap, 0x002E)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAddVideoMapping, 0x002F
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeRemoveVideoMapping, 0x0030
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeGetSensorMap, 0x0031)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAddSensorMapping, 0x0032
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeRemoveSensorMapping, 0x0033
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeStartOperation, 0x0034
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAbortOperation, 0x0035
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeOperationStatus, 0x0036
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateAddKey, 0x0037
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateDeleteKey, 0x0038
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateGetKeyList, 0x0039
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateGetKey, 0x003A
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateAddKeyToChain, 0x003B
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateDeleteKeyFromChain,
            0x003C,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateGetKeychainList, 0x003D
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateGetIdentity, 0x003E
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateAddToken, 0x003F
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeAuthenticateDeleteToken, 0x0040
        )
        self.assertEqual(AudioVideoBridging.AVB17221AEMCommandTypeAuthenticate, 0x0041)
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeDeauthenticate, 0x0042
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeEnableTransportSecurity, 0x0043
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeDisableTransportSecurity, 0x0044
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeEnableStreamEncryption, 0x0045
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeDisableStreamEncryption, 0x0046
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetMemoryObjectLength, 0x0047
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetMemoryObjectLength, 0x0048
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetStreamBackup, 0x0049
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetStreamBackup, 0x004A
        )

        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetDynamicInfo, 0x004B
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetMaxTransitTime, 0x004C
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetMaxTransitTime, 0x004D
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetSampingRateRange, 0x004E
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetSamplingRateRange, 0x004F
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetPTPInstanceInfo, 0x0050
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPInstanceInfo, 0x0051
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPInstanceExtendedInfo, 0x0052
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPInstanceGrandmasterInfo,
            0x0053,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPInstancePathCount, 0x0054
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPInstancePathTrace, 0x0055
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPInstancePerformanceMonitoringCount,
            0x0056,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPInstancePerformanceMonitoringRecord,
            0x0057,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetPTPPortInitialIntervals, 0x0058
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortInitialIntervals, 0x0059
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortCurrentIntervals, 0x005B
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetPTPPortRemoteIntervals, 0x005C
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortRemoteIntervals, 0x005D
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetPTPPortInfo, 0x005E
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortInfo, 0x005F
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeSetPTPPortOverrides, 0x0060
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortOverrides, 0x0061
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortPDelayMonitoringCount,
            0x0062,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortPDelayMonitoringRecord,
            0x0063,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortPerformanceMonitoringCount,
            0x0064,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPTPPortPerformanceMonitoringRecord,
            0x0065,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221AEMCommandTypeGetPathLatency, 0x0066
        )

        self.assertEqual(AudioVideoBridging.AVB17221AECPAddressAccessTLVModeRead, 0x00)
        self.assertEqual(AudioVideoBridging.AVB17221AECPAddressAccessTLVModeWrite, 0x01)
        self.assertEqual(
            AudioVideoBridging.AVB17221AECPAddressAccessTLVModeExecute, 0x02
        )
