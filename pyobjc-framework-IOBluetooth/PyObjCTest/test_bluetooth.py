from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestBluetooth(TestCase):
    def test_constants(self):
        self.assertEqual(IOBluetooth.kBluetoothConnectionHandleNone, 0xFFFF)

        self.assertIsEnumType(IOBluetooth.BluetoothEncryptionEnable)
        self.assertEqual(IOBluetooth.kBluetoothEncryptionEnableOff, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothEncryptionEnableOn, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothEncryptionEnableBREDRE0, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothEncryptionEnableLEAESCCM, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothEncryptionEnableBREDRAESCCM, 0x02)

        self.assertIsEnumType(IOBluetooth.BluetoothKeyFlag)
        self.assertEqual(IOBluetooth.kBluetoothKeyFlagSemiPermanent, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothKeyFlagTemporary, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothKeyType)
        self.assertEqual(IOBluetooth.kBluetoothKeyTypeCombination, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothKeyTypeLocalUnit, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothKeyTypeRemoteUnit, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothKeyTypeDebugCombination, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothKeyTypeUnauthenticatedCombination, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothKeyTypeAuthenticatedCombination, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothKeyTypeChangedCombination, 0x06)
        self.assertEqual(
            IOBluetooth.kBluetoothKeyTypeUnauthenticatedCombinationP256, 0x07
        )
        self.assertEqual(
            IOBluetooth.kBluetoothKeyTypeAuthenticatedCombinationP256, 0x08
        )

        self.assertIsEnumType(IOBluetooth.BluetoothPacketType)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeReserved1, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothPacketType2DH1Omit, 0x0002)
        self.assertEqual(IOBluetooth.kBluetoothPacketType3DH1Omit, 0x0004)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeDM1, 0x0008)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeDH1, 0x0010)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeHV1, 0x0020)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeHV2, 0x0040)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeHV3, 0x0080)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeDV, 0x0100)
        self.assertEqual(IOBluetooth.kBluetoothPacketType2DH3Omit, 0x0100)
        self.assertEqual(IOBluetooth.kBluetoothPacketType3DH3Omit, 0x0200)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeAUX, 0x0200)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeDM3, 0x0400)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeDH3, 0x0800)
        self.assertEqual(IOBluetooth.kBluetoothPacketType2DH5Omit, 0x1000)
        self.assertEqual(IOBluetooth.kBluetoothPacketType3DM5Omit, 0x2000)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeDM5, 0x4000)
        self.assertEqual(IOBluetooth.kBluetoothPacketTypeDH5, 0x8000)
        self.assertNotHasAttr(IOBluetooth, "kBluetoothPacketTypeEnd")

        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeNone, 0x0000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeHV1, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeHV2, 0x0002
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeHV3, 0x0004
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeEV3, 0x0008
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeEV4, 0x0010
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeEV5, 0x0020
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketType2EV3Omit, 0x0040
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketType3EV3Omit, 0x0080
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketType2EV5Omit, 0x0100
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketType3EV5Omit, 0x0200
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeFutureUse, 0xFC00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSynchronousConnectionPacketTypeAll, 0xFFFF
        )
        self.assertNotHasAttr(
            IOBluetooth, "kBluetoothSynchronousConnectionPacketTypeEnd"
        )

        self.assertIsEnumType(IOBluetooth.BluetoothLAP)
        self.assertEqual(IOBluetooth.kBluetoothGeneralInquiryAccessCodeIndex, 0)
        self.assertEqual(
            IOBluetooth.kBluetoothGeneralInquiryAccessCodeLAPValue, 0x9E8B33
        )
        self.assertEqual(IOBluetooth.kBluetoothLimitedInquiryAccessCodeIndex, 1)
        self.assertEqual(
            IOBluetooth.kBluetoothLimitedInquiryAccessCodeLAPValue, 0x9E8B00
        )
        self.assertNotHasAttr(IOBluetooth, "kBluetoothLimitedInquiryAccessCodeEnd")

        self.assertIsEnumType(IOBluetooth.BluetoothPageScanRepetitionMode)
        self.assertEqual(IOBluetooth.kBluetoothPageScanRepetitionModeR0, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothPageScanRepetitionModeR1, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothPageScanRepetitionModeR2, 0x02)

        self.assertIsEnumType(IOBluetooth.BluetoothPageScanPeriodMode)
        self.assertEqual(IOBluetooth.kBluetoothPageScanPeriodModeP0, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothPageScanPeriodModeP1, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothPageScanPeriodModeP2, 0x02)

        self.assertIsEnumType(IOBluetooth.BluetoothPageScanMode)
        self.assertEqual(IOBluetooth.kBluetoothPageScanModeMandatory, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothPageScanModeOptional1, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothPageScanModeOptional2, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothPageScanModeOptional3, 0x03)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIPageScanType)
        self.assertEqual(IOBluetooth.kBluetoothHCIPageScanTypeStandard, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIPageScanTypeInterlaced, 0x01)

        self.assertEqual(IOBluetooth.kBluetoothHCIPageScanTypeReservedStart, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothHCIPageScanTypeReservedEnd, 0xFF)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIErroneousDataReporting)
        self.assertEqual(IOBluetooth.kBluetoothHCIErroneousDataReportingDisabled, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIErroneousDataReportingEnabled, 0x01)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErroneousDataReportingReservedStart, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErroneousDataReportingReservedEnd, 0xFF
        )

        self.assertEqual(IOBluetooth.kBluetoothDeviceNameMaxLength, 248)

        self.assertIsEnumType(IOBluetooth.BluetoothRole)
        self.assertIsEnumType(IOBluetooth.BluetoothAllowRoleSwitch)
        self.assertEqual(IOBluetooth.kBluetoothDontAllowRoleSwitch, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothAllowRoleSwitch, 0x01)

        self.assertEqual(IOBluetooth.kBluetoothRoleBecomeCentral, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothRoleRemainPeripheral, 0x01)
        self.assertEqual(
            IOBluetooth.kBluetoothRoleBecomeMaster,
            IOBluetooth.kBluetoothRoleBecomeCentral,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothRoleRemainSlave,
            IOBluetooth.kBluetoothRoleRemainPeripheral,
        )

        self.assertEqual(IOBluetooth.kBluetoothL2CAPMaxPacketSize, 65535)
        self.assertEqual(IOBluetooth.kBluetoothACLLogicalChannelReserved, 0)
        self.assertEqual(IOBluetooth.kBluetoothACLLogicalChannelL2CAPContinue, 1)
        self.assertEqual(IOBluetooth.kBluetoothACLLogicalChannelL2CAPStart, 2)
        self.assertEqual(IOBluetooth.kBluetoothACLLogicalChannelLMP, 3)

        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPChannelID)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelNull, 0x0000)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelSignalling, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelConnectionLessData, 0x0002)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelAMPManagerProtocol, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelAttributeProtocol, 0x0004)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelLESignalling, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelSecurityManager, 0x0006)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelBREDRSecurityManager, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelReservedStart, 0x0008)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelLEAP, 0x002A)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelLEAS, 0x002B)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelMagicPairing, 0x0030)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelMagnet, 0x003A)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelReservedEnd, 0x003E)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelAMPTestManager, 0x003F)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelDynamicStart, 0x0040)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelDynamicEnd, 0xFFFF)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPChannelEnd, 0xFFFF)

        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPCommandCode)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeReserved, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeCommandReject, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeConnectionRequest, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeConnectionResponse, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeConfigureRequest, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeConfigureResponse, 0x05)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeDisconnectionRequest, 0x06
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeDisconnectionResponse, 0x07
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeEchoRequest, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeEchoResponse, 0x09)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeInformationRequest, 0x0A)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeInformationResponse, 0x0B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeCreateChannelRequest, 0x0C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeCreateChannelResponse, 0x0D
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPCommandCodeMoveChannelRequest, 0x0E)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeMoveChannelResponse, 0x0F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeMoveChannelConfirmation, 0x10
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeMoveChannelConfirmationResponse, 0x11
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeConnectionParameterUpdateRequest, 0x12
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeConnectionParameterUpdateResponse,
            0x13,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeLECreditBasedConnectionRequest, 0x14
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeLECreditBasedConnectionResponse, 0x15
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandCodeLEFlowControlCredit, 0x16
        )

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandRejectReasonCommandNotUnderstood, 0x0000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandRejectReasonSignallingMTUExceeded, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPCommandRejectReasonInvalidCIDInRequest, 0x0002
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPCommandRejectReason)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPFlushTimeoutUseExisting, 0x0000)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPFlushTimeoutImmediate, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPFlushTimeoutForever, 0xFFFF)

        self.assertNotHasAttr(IOBluetooth, "kBluetoothL2CAPFlushTimeoutEnd")

        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPSegmentationAndReassembly)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPSegmentationAndReassemblyUnsegmentedSDU, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPSegmentationAndReassemblyStartOfSDU, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPSegmentationAndReassemblyEndOfSDU, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPSegmentationAndReassemblyContinuationOfSDU, 0x03
        )

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInfoTypeMaxConnectionlessMTUSize, 0x0001
        )

        self.assertEqual(IOBluetooth.kBluetoothL2CAPPacketHeaderSize, 4)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPConnectionResultSuccessful, 0x0000)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPConnectionResultPending, 0x0001)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionResultRefusedPSMNotSupported, 0x0002
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionResultRefusedSecurityBlock, 0x0003
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionResultRefusedNoResources, 0x0004
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionResultRefusedReserved, 0x0005
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionResultRefusedInvalidSourceCID, 0x0006
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionResultRefusedSourceCIDAlreadyAllocated,
            0x0007,
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPConnectionResult)

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionStatusNoInfoAvailable, 0x0000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionStatusAuthenticationPending, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConnectionStatusAuthorizationPending, 0x0002
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPConnectionStatus)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPConfigurationResultSuccess, 0x0000)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationResultUnacceptableParams, 0x0001
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPConfigurationResultRejected, 0x0002)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationResultUnknownOptions, 0x0003
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPConfigurationResult)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPConfigurationOptionMTU, 0x01)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationOptionFlushTimeout, 0x02
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPConfigurationOptionQoS, 0x03)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationOptionRetransmissionAndFlowControl,
            0x04,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationOptionFrameCheckSequence, 0x05
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationOptionExtendedFlowSpecification,
            0x06,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationOptionExtendedWindowSize, 0x07
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPConfigurationOption)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPConfigurationOptionMTULength, 2)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationOptionFlushTimeoutLength, 2
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPConfigurationOptionQoSLength, 22)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationOptionRetransmissionAndFlowControlLength,
            9,
        )

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationBasicL2CAPModeFlag, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationRetransmissionModeFlag, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationFlowControlModeFlag, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPConfigurationEnhancedRetransmissionMode, 0x03
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPConfigurationStreamingMode, 0x04)
        self.assertIsEnumType(
            IOBluetooth.BluetoothL2CAPConfigurationRetransmissionAndFlowControlFlags
        )

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationTypeConnectionlessMTU, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationTypeExtendedFeatures, 0x0002
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationTypeFixedChannelsSupported, 0x0003
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPInformationType)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPInformationResultSuccess, 0x0000)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationResultNotSupported, 0x0001
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPInformationResult)

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationNoExtendedFeatures, 0x00000000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationFlowControlMode, 0x00000001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationRetransmissionMode, 0x00000002
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationBidirectionalQoS, 0x00000004
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationEnhancedRetransmissionMode, 0x00000008
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationStreamingMode, 0x00000010
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPInformationFCSOption, 0x00000020)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationExtendedFlowSpecification, 0x00000040
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationFixedChannels, 0x00000080
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPInformationExtendedWindowSize, 0x00000100
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPUnicastConnectionlessDataReception, 0x00000200
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPInformationExtendedFeaturesMask)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPQoSTypeNoTraffic, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPQoSTypeBestEffort, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPQoSTypeGuaranteed, 0x02)
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPQoSType)

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPSupervisoryFuctionTypeReceiverReady, 0x0
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPSupervisoryFuctionTypeReject, 0x1)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPSupervisoryFuctionTypeReceiverNotReady, 0x2
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPSupervisoryFuctionTypeSelectiveReject, 0x3
        )
        self.assertIsEnumType(IOBluetooth.BluetoothL2CAPSupervisoryFuctionType)

        self.assertEqual(IOBluetooth.kBluetoothLETXTimeMin, 0x0148)
        self.assertEqual(IOBluetooth.kBluetoothLETXTimeDefault, 0x0148)
        self.assertEqual(IOBluetooth.kBluetoothLETXTimeMax, 0x0848)
        self.assertEqual(IOBluetooth.kBluetoothLETXOctetsMin, 0x001B)
        self.assertEqual(IOBluetooth.kBluetoothLETXOctetsDefault, 0x001B)
        self.assertEqual(IOBluetooth.kBluetoothLETXOctetsMax, 0x00FB)

        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPMTULowEnergyDefault,
            IOBluetooth.kBluetoothLETXOctetsMin,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPMTULowEnergyMax,
            IOBluetooth.kBluetoothLETXOctetsMax,
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPMTUMinimum, 0x0030)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPMTUDefault, 0x03F9)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPMTUMaximum, 0xFFFF)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPMTUStart, 0x7FFF)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPMTUSIG, 0x0030)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPFlushTimeoutDefault,
            IOBluetooth.kBluetoothL2CAPFlushTimeoutForever,
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPQoSFlagsDefault, 0)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPQoSTypeDefault,
            IOBluetooth.kBluetoothL2CAPQoSTypeBestEffort,
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPQoSTokenRateDefault, 0x00000000)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPQoSTokenBucketSizeDefault, 0x00000000
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPQoSPeakBandwidthDefault, 0x00000000)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPQoSLatencyDefault, 0xFFFFFFFF)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPQoSDelayVariationDefault, 0xFFFFFFFF
        )

        self.assertEqual(IOBluetooth.kBluetoothLEMaxTXTimeMin, 0x0148)
        self.assertEqual(
            IOBluetooth.kBluetoothLEMaxTXTimeDefault,
            IOBluetooth.kBluetoothL2CAPMTULowEnergyDefault,
        )
        self.assertEqual(IOBluetooth.kBluetoothLEMaxTXTimeMax, 0x0848)
        self.assertEqual(IOBluetooth.kBluetoothLEMaxTXOctetsMin, 0x001B)
        self.assertEqual(IOBluetooth.kBluetoothLEMaxTXOctetsDefault, 0x0080)
        self.assertEqual(IOBluetooth.kBluetoothLEMaxTXOctetsMax, 0x00FB)

        self.assertEqual(IOBluetooth.kBluetoothLESMPTimeout, 30)

        self.assertEqual(IOBluetooth.kBluetoothLESMPMinEncryptionKeySize, 7)
        self.assertEqual(IOBluetooth.kBluetoothLESMPMaxEncryptionKeySize, 16)

        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerEncryptionKey, 1 << 0)
        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerIDKey, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerSignKey, 1 << 2)
        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerLinkKey, 1 << 3)

        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeReserved, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingRequest, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingResponse, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingConfirm, 0x03
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingRandom, 0x04
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingFailed, 0x05
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeEncryptionInfo, 0x06
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeMasterIdentification, 0x07
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeIdentityInfo, 0x08
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeIdentityAddressInfo, 0x09
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeSigningInfo, 0x0A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeSecurityRequest, 0x0B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingPublicKey, 0x0C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingDHKeyCheck, 0x0D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodePairingKeypressNotification,
            0x0E,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeReservedStart, 0x0F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerCommandCodeReservedEnd, 0xFF
        )
        self.assertIsEnumType(IOBluetooth.BluetoothLESecurityManagerCommandCode)

        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerUserInputCapabilityNoInput, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerUserInputCapabilityYesNo, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerUserInputCapabilityKeyboard, 0x03
        )
        self.assertIsEnumType(IOBluetooth.BluetoothLESecurityManagerUserInputCapability)

        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerUserOutputCapabilityNoOutput, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerUserOutputCapabilityNumericOutput,
            0x02,
        )
        self.assertIsEnumType(
            IOBluetooth.BluetoothLESecurityManagerUserOutputCapability
        )

        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerIOCapabilityDisplayOnly, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerIOCapabilityDisplayYesNo, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerIOCapabilityKeyboardOnly, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerIOCapabilityNoInputNoOutput, 0x03
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerIOCapabilityKeyboardDisplay, 0x04
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerIOCapabilityReservedStart, 0x05
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerIOCapabilityReservedEnd, 0xFF
        )
        self.assertIsEnumType(IOBluetooth.BluetoothLESecurityManagerIOCapability)

        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerOOBAuthenticationDataNotPresent, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerOOBAuthenticationDataPresent, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerOOBDataReservedStart, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerOOBDataReservedEnd, 0xFF
        )
        self.assertIsEnumType(IOBluetooth.BluetoothLESecurityManagerOOBData)

        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerNoBonding, 0)
        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerBonding, 1)
        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerReservedStart, 2)
        self.assertEqual(IOBluetooth.kBluetoothLESecurityManagerReservedEnd, 3)

        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeReserved, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodePasskeyEntryFailed, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeOOBNotAvailbale, 0x02
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeAuthenticationRequirements,
            0x03,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeConfirmValueFailed, 0x04
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodePairingNotSupported, 0x05
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeEncryptionKeySize, 0x06
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeCommandNotSupported, 0x07
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeUnspecifiedReason, 0x08
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeRepeatedAttempts, 0x09
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeInvalidParameters, 0x0A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeDHKeyCheckFailed, 0x0B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeNumericComparisonFailed,
            0x0C,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeBREDRPairingInProgress,
            0x0D,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeCrossTransportKeyDerivationGenerationNotAllowed,
            0x0E,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeReservedStart, 0x0F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerReasonCodeReservedEnd, 0xFF
        )
        self.assertIsEnumType(
            IOBluetooth.BluetoothLESecurityManagerPairingFailedReasonCode
        )

        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerNotificationTypePasskeyEntryStarted,
            0,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerNotificationTypePasskeyDigitEntered,
            1,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerNotificationTypePasskeyDigitErased, 2
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerNotificationTypePasskeyCleared, 3
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerNotificationTypePasskeyEntryCompleted,
            4,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerNotificationTypeReservedStart, 5
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLESecurityManagerNotificationTypeReservedEnd, 255
        )
        self.assertIsEnumType(
            IOBluetooth.BluetoothLESecurityManagerKeypressNotificationType
        )

        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeReserved, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPCommandReject, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPDiscoverRequest, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPDiscoverResponse, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPChangeNotify, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPChangeResponse, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPGetInfoRequest, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPGetInfoResponse, 0x07)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPGetAssocRequest, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothAMPManagerCodeAMPGetAssocResponse, 0x09)
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCodeAMPCreatePhysicalLinkRequest, 0x0A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCodeAMPCreatePhysicalLinkResponse, 0x0B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCodeAMPDisconnectPhysicalLinkRequest, 0x0C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCodeAMPDisconnectPhysicalLinkResponse, 0x0D
        )
        self.assertIsEnumType(IOBluetooth.BluetoothAMPManagerCode)

        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCommandRejectReasonCommandNotRecognized,
            0x0000,
        )
        self.assertIsEnumType(IOBluetooth.BluetoothAMPCommandRejectReason)

        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDiscoverResponseControllerStatusPoweredDown,
            0x00,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDiscoverResponseControllerStatusBluetoothOnly,
            0x01,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDiscoverResponseControllerStatusNoCapacity,
            0x02,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDiscoverResponseControllerStatusLowCapacity,
            0x03,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDiscoverResponseControllerStatusMediumCapacity,
            0x04,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDiscoverResponseControllerStatusHighCapacity,
            0x05,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDiscoverResponseControllerStatusFullCapacity,
            0x06,
        )
        self.assertIsEnumType(IOBluetooth.BluetoothAMPDiscoverResponseControllerStatus)

        self.assertEqual(IOBluetooth.kBluetoothAMPManagerGetInfoResponseSuccess, 0x00)
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerGetInfoResponseInvalidControllerID, 0x01
        )
        self.assertIsEnumType(IOBluetooth.BluetoothAMPGetInfoResponseStatus)

        self.assertEqual(IOBluetooth.kBluetoothAMPManagerGetAssocResponseSuccess, 0x00)
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerGetAssocResponseInvalidControllerID, 0x01
        )
        self.assertIsEnumType(IOBluetooth.BluetoothAMPGetAssocResponseStatus)

        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCreatePhysicalLinkResponseSuccess, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCreatePhysicalLinkResponseInvalidControllerID,
            0x01,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCreatePhysicalLinkResponseUnableToStartLinkCreation,
            0x02,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCreatePhysicalLinkResponseCollisionOccurred,
            0x03,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCreatePhysicalLinkResponseAMPDisconnectedPhysicalLinkRequestReceived,
            0x04,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCreatePhysicalLinkResponsePhysicalLinkAlreadyExists,
            0x05,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerCreatePhysicalLinkResponseSecurityViolation,
            0x06,
        )
        self.assertIsEnumType(IOBluetooth.BluetoothAMPCreatePhysicalLinkResponseStatus)

        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDisconnectPhysicalLinkResponseSuccess, 0x00
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDisconnectPhysicalLinkResponseInvalidControllerID,
            0x01,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAMPManagerDisconnectPhysicalLinkResponseNoPhysicalLink,
            0x02,
        )
        self.assertIsEnumType(
            IOBluetooth.BluetoothAMPDisconnectPhysicalLinkResponseStatus
        )

        self.assertIsEnumType(IOBluetooth.BluetoothHCICommandOpCodeGroup)
        self.assertIsEnumType(IOBluetooth.BluetoothHCICommandOpCodeCommand)
        self.assertIsEnumType(IOBluetooth.BluetoothHCICommandOpCode)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIVendorCommandSelector)

        self.assertEqual(IOBluetooth.kBluetoothHCIOpCodeNoOp, 0)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupNoOp, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandNoOp, 0x0000)

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupLinkControl, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandInquiry, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandInquiryCancel, 0x0002)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandPeriodicInquiryMode, 0x0003)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandExitPeriodicInquiryMode, 0x0004
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandCreateConnection, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandDisconnect, 0x0006)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandAddSCOConnection, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandCreateConnectionCancel, 0x0008)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandAcceptConnectionRequest, 0x0009
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandRejectConnectionRequest, 0x000A
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLinkKeyRequestReply, 0x000B)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLinkKeyRequestNegativeReply, 0x000C
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandPINCodeRequestReply, 0x000D)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandPINCodeRequestNegativeReply, 0x000E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandChangeConnectionPacketType, 0x000F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandAuthenticationRequested, 0x0011
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetConnectionEncryption, 0x0013
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandChangeConnectionLinkKey, 0x0015
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandMasterLinkKey, 0x0017)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandRemoteNameRequest, 0x0019)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadRemoteSupportedFeatures, 0x001B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadRemoteExtendedFeatures, 0x001C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadRemoteVersionInformation, 0x001D
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadClockOffset, 0x001F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandRemoteNameRequestCancel, 0x001A
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLMPHandle, 0x0020)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetupSynchronousConnection, 0x0028
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandAcceptSynchronousConnectionRequest, 0x0029
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandRejectSynchronousConnectionRequest, 0x002A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandIOCapabilityRequestReply, 0x002B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandUserConfirmationRequestReply, 0x002C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandUserConfirmationRequestNegativeReply, 0x002D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandUserPasskeyRequestReply, 0x002E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandUserPasskeyRequestNegativeReply, 0x002F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandRemoteOOBDataRequestReply, 0x0030
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandRemoteOOBDataRequestNegativeReply, 0x0033
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandIOCapabilityRequestNegativeReply, 0x0034
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandEnhancedSetupSynchronousConnection, 0x003D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandEnhancedAcceptSynchronousConnectionRequest,
            0x003E,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandTruncatedPage, 0x003F)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandTruncatedPageCancel, 0x0040)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetConnectionlessPeripheralBroadcast, 0x0041
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetConnectionlessPeripheralBroadcastReceive,
            0x0042,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandStartSynchronizationTrain, 0x0043
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReceiveSynchronizationTrain, 0x0044
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandRemoteOOBExtendedDataRequestReply, 0x0045
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetConnectionlessSlaveBroadcast,
            IOBluetooth.kBluetoothHCICommandSetConnectionlessPeripheralBroadcast,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetConnectionlessSlaveBroadcastReceive,
            IOBluetooth.kBluetoothHCICommandSetConnectionlessPeripheralBroadcastReceive,
        )

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupLinkPolicy, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandHoldMode, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSniffMode, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandExitSniffMode, 0x0004)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandParkMode, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandExitParkMode, 0x0006)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandQoSSetup, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandRoleDiscovery, 0x0009)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSwitchRole, 0x000B)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLinkPolicySettings, 0x000C)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteLinkPolicySettings, 0x000D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadDefaultLinkPolicySettings, 0x000E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteDefaultLinkPolicySettings, 0x000F
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandFlowSpecification, 0x0010)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSniffSubrating, 0x0011)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandAcceptSniffRequest, 0x0031)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandRejectSniffRequest, 0x0032)

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupHostController, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSetEventMask, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReset, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSetEventFilter, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandFlush, 0x0008)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadPINType, 0x0009)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWritePINType, 0x000A)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandCreateNewUnitKey, 0x000B)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadStoredLinkKey, 0x000D)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteStoredLinkKey, 0x0011)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandDeleteStoredLinkKey, 0x0012)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandChangeLocalName, 0x0013)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLocalName, 0x0014)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadConnectionAcceptTimeout, 0x0015
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteConnectionAcceptTimeout, 0x0016
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadPageTimeout, 0x0017)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWritePageTimeout, 0x0018)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadScanEnable, 0x0019)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteScanEnable, 0x001A)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadPageScanActivity, 0x001B)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWritePageScanActivity, 0x001C)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadInquiryScanActivity, 0x001D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteInquiryScanActivity, 0x001E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadAuthenticationEnable, 0x001F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteAuthenticationEnable, 0x0020
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadEncryptionMode, 0x0021)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteEncryptionMode, 0x0022)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadClassOfDevice, 0x0023)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteClassOfDevice, 0x0024)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadVoiceSetting, 0x0025)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteVoiceSetting, 0x0026)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadAutomaticFlushTimeout, 0x0027
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteAutomaticFlushTimeout, 0x0028
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadNumberOfBroadcastRetransmissions, 0x0029
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteNumberOfBroadcastRetransmissions,
            0x002A,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadHoldModeActivity, 0x002B)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteHoldModeActivity, 0x002C)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadTransmitPowerLevel, 0x002D)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadSCOFlowControlEnable, 0x002E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteSCOFlowControlEnable, 0x002F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetHostControllerToHostFlowControl, 0x0031
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandHostBufferSize, 0x0033)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandHostNumberOfCompletedPackets, 0x0035
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLinkSupervisionTimeout, 0x0036
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteLinkSupervisionTimeout, 0x0037
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadNumberOfSupportedIAC, 0x0038
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadCurrentIACLAP, 0x0039)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteCurrentIACLAP, 0x003A)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadPageScanPeriodMode, 0x003B)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWritePageScanPeriodMode, 0x003C
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadPageScanMode, 0x003D)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWritePageScanMode, 0x003E)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSetAFHClassification, 0x003F)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadInquiryScanType, 0x0042)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteInquiryScanType, 0x0043)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadInquiryMode, 0x0044)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteInquiryMode, 0x0045)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadPageScanType, 0x0046)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWritePageScanType, 0x0047)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadAFHChannelAssessmentMode, 0x0048
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteAFHChannelAssessmentMode, 0x0049
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadExtendedInquiryResponse, 0x0051
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteExtendedInquiryResponse, 0x0052
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandRefreshEncryptionKey, 0x0053)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadSimplePairingMode, 0x0055)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteSimplePairingMode, 0x0056)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLocalOOBData, 0x0057)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadInquiryResponseTransmitPower, 0x0058
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteInquiryResponseTransmitPower, 0x0059
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSendKeypressNotification, 0x0060
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadDefaultErroneousDataReporting, 0x005A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteDefaultErroneousDataReporting, 0x005B
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandEnhancedFlush, 0x005F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLogicalLinkAcceptTimeout, 0x0061
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteLogicalLinkAcceptTimeout, 0x0062
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSetEventMaskPageTwo, 0x0063)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLocationData, 0x0064)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteLocationData, 0x0065)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadFlowControlMode, 0x0066)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteFlowControlMode, 0x0067)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadEnhancedTransmitPowerLevel, 0x0068
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadBestEffortFlushTimeout, 0x0069
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteBestEffortFlushTimeout, 0x006A
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandShortRangeMode, 0x006B)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLEHostSupported, 0x006C)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteLEHostSupported, 0x006D)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetMWSChannelParameters, 0x006E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetExternalFrameConfiguration, 0x006F
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSetMWSSignaling, 0x0070)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSetMWSTransportLayer, 0x0071)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetMWSScanFrequencyTable, 0x0072
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetMWSPATTERNConfiguration, 0x0073
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandSetReservedLTADDR, 0x0074)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandDeleteReservedLTADDR, 0x0075)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetConnectionlessPeripheralBroadcastData,
            0x0076,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadSynchronizationTrainParameters, 0x0077
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteSynchronizationTrainParameters, 0x0078
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadSecureConnectionsHostSupport, 0x0079
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteSecureConnectionsHostSupport, 0x007A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadAuthenticatedPayloadTimeout, 0x007B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteAuthenticatedPayloadTimeout, 0x007C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLocalOOBExtendedData, 0x007D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadExtendedPageTimeout, 0x007E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteExtendedPageTimeout, 0x007F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadExtendedInquiryLength, 0x0080
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteExtendedInquiryLength, 0x0081
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetConnectionlessSlaveBroadcastData,
            IOBluetooth.kBluetoothHCICommandSetConnectionlessPeripheralBroadcastData,
        )

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupInformational, 0x04)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLocalVersionInformation, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLocalSupportedCommands, 0x0002
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLocalSupportedFeatures, 0x0003
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLocalExtendedFeatures, 0x0004
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadBufferSize, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadCountryCode, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadDeviceAddress, 0x0009)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadDataBlockSize, 0x000A)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadLocalSupportedCodecs, 0x000B
        )

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupStatus, 0x05)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandReadFailedContactCounter, 0x0001
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandResetFailedContactCounter, 0x0002
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandGetLinkQuality, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadRSSI, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadAFHMappings, 0x0006)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadClock, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadEncryptionKeySize, 0x0008)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLocalAMPInfo, 0x0009)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLocalAMPASSOC, 0x000A)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteRemoteAMPASSOC, 0x000B)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandGetMWSTransportLayerConfiguration, 0x000C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandSetTriggeredClockCapture, 0x000D
        )

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupTesting, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandReadLoopbackMode, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandWriteLoopbackMode, 0x0002)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandEnableDeviceUnderTestMode, 0x0003
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandWriteSimplePairingDebugMode, 0x0004
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandEnableAMPReceiverReports, 0x0007
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandAMPTestEnd, 0x0008)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandAMPTest, 0x0009)

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupLowEnergy, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetEventMask, 0x0001)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEReadBufferSize, 0x0002)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadLocalSupportedFeatures, 0x0003
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetRandomAddress, 0x0005)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetAdvertisingParameters, 0x0006
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadAdvertisingChannelTxPower, 0x0007
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetAdvertisingData, 0x0008)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetScanResponseData, 0x0009)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetAdvertiseEnable, 0x000A)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetScanParameters, 0x000B)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetScanEnable, 0x000C)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLECreateConnection, 0x000D)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLECreateConnectionCancel, 0x000E
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEReadWhiteListSize, 0x000F)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEClearWhiteList, 0x0010)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEAddDeviceToWhiteList, 0x0011)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLERemoveDeviceFromWhiteList, 0x0012
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEConnectionUpdate, 0x0013)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetHostChannelClassification, 0x0014
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEReadChannelMap, 0x0015)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadRemoteUsedFeatures, 0x0016
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEEncrypt, 0x0017)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLERand, 0x0018)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEStartEncryption, 0x0019)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLELongTermKeyRequestReply, 0x001A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLELongTermKeyRequestNegativeReply, 0x001B
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEReadSupportedStates, 0x001C)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEReceiverTest, 0x001D)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLETransmitterTest, 0x001E)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLETestEnd, 0x001F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLERemoteConnectionParameterRequestReply,
            0x0020,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLERemoteConnectionParameterRequestNegativeReply,
            0x0021,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetDataLength, 0x0022)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadSuggestedDefaultDataLength, 0x0023
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEWriteSuggestedDefaultDataLength, 0x0024
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadLocalP256PublicKey, 0x0025
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEGenerateDHKey, 0x0026)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEAddDeviceToResolvingList, 0x0027
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLERemoveDeviceFromResolvingList, 0x0028
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEClearResolvingList, 0x0029)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadResolvingListSize, 0x002A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadPeerResolvableAddress, 0x002B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadLocalResolvableAddress, 0x002C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetAddressResolutionEnable, 0x002D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetResolvablePrivateAddressTimeout, 0x002E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadMaximumDataLength, 0x002F
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEReadPhy, 0x0030)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetDefaultPhy, 0x0031)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetPhy, 0x0032)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEEnhancedReceiverTest, 0x0033)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEEnhancedTransmitterTest, 0x0034
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetAdvertisingSetRandomAddress, 0x0035
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetExtendedAdvertisingParameters, 0x0036
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetExtendedAdvertisingData, 0x0037
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetExtendedScanResponseData, 0x0038
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetExtendedAdvertisingEnableCommand,
            0x0039,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadMaximumAdvertisingDataLength, 0x003A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadNumberofSupportedAdvertisingSets,
            0x003B,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLERemoveAdvertisingSet, 0x003C)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEClearAdvertisingSets, 0x003D)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetPeriodicAdvertisingParameters, 0x003E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetPeriodicAdvertisingData, 0x003F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetPeriodicAdvertisingEnable, 0x0040
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetExtendedScanParameters, 0x0041
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLESetExtendedScanEnable, 0x0042
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEExtendedCreateConnection, 0x0043
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEPeriodicAdvertisingCreateSync, 0x0044
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEPeriodicAdvertisingCreateSyncCancel,
            0x0045,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEPeriodicAdvertisingTerminateSync, 0x0046
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEAddDeviceToPeriodicAdvertiserList, 0x0047
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLERemoveDeviceFromPeriodicAdvertiserList,
            0x0048,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEClearPeriodicAdvertiserList, 0x0049
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadPeriodicAdvertiserListSize, 0x004A
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLEReadTransmitPower, 0x004B)
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEReadRFPathCompensation, 0x004C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCICommandLEWriteRFPathCompensation, 0x004D
        )
        self.assertEqual(IOBluetooth.kBluetoothHCICommandLESetPrivacyMode, 0x004E)

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupLogoTesting, 0x3E)

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupVendorSpecific, 0x3F)

        self.assertEqual(IOBluetooth.kBluetoothHCICommandGroupMax, 0x40)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandMax, 0x03FF)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIConnectionModes)
        self.assertEqual(IOBluetooth.kConnectionActiveMode, 0)
        self.assertEqual(IOBluetooth.kConnectionHoldMode, 1)
        self.assertEqual(IOBluetooth.kConnectionSniffMode, 2)
        self.assertEqual(IOBluetooth.kConnectionParkMode, 3)
        self.assertEqual(IOBluetooth.kConnectionModeReservedForFutureUse, 4)

        self.assertIsEnumType(IOBluetooth.BluetoothLEFeatureBits)
        self.assertEqual(IOBluetooth.kBluetoothLEFeatureLEEncryption, 1 << 0)
        self.assertEqual(
            IOBluetooth.kBluetoothLEFeatureConnectionParamsRequestProcedure, 1 << 1
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLEFeatureExtendedRejectIndication, 1 << 2
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLEFeaturePeripheralInitiatedFeaturesExchange, 1 << 3
        )
        self.assertEqual(IOBluetooth.kBluetoothLEFeatureLEPing, 1 << 4)
        self.assertEqual(
            IOBluetooth.kBluetoothLEFeatureLEDataPacketLengthExtension, 1 << 5
        )
        self.assertEqual(IOBluetooth.kBluetoothLEFeatureLLPrivacy, 1 << 6)
        self.assertEqual(
            IOBluetooth.kBluetoothLEFeatureExtendedScannerFilterPolicies, 1 << 7
        )
        self.assertEqual(
            IOBluetooth.kBluetoothLEFeatureSlaveInitiatedFeaturesExchange,
            IOBluetooth.kBluetoothLEFeaturePeripheralInitiatedFeaturesExchange,
        )

        self.assertIsEnumType(IOBluetooth.BluetoothFeatureBits)
        self.assertEqual(IOBluetooth.kBluetoothFeatureThreeSlotPackets, 1 << 0)
        self.assertEqual(IOBluetooth.kBluetoothFeatureFiveSlotPackets, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothFeatureEncryption, 1 << 2)
        self.assertEqual(IOBluetooth.kBluetoothFeatureSlotOffset, 1 << 3)
        self.assertEqual(IOBluetooth.kBluetoothFeatureTimingAccuracy, 1 << 4)
        self.assertEqual(IOBluetooth.kBluetoothFeatureSwitchRoles, 1 << 5)
        self.assertEqual(IOBluetooth.kBluetoothFeatureHoldMode, 1 << 6)
        self.assertEqual(IOBluetooth.kBluetoothFeatureSniffMode, 1 << 7)
        self.assertEqual(IOBluetooth.kBluetoothFeatureParkMode, 1 << 0)
        self.assertEqual(IOBluetooth.kBluetoothFeatureRSSI, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothFeaturePowerControlRequests, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothFeatureChannelQuality, 1 << 2)
        self.assertEqual(IOBluetooth.kBluetoothFeatureSCOLink, 1 << 3)
        self.assertEqual(IOBluetooth.kBluetoothFeatureHV2Packets, 1 << 4)
        self.assertEqual(IOBluetooth.kBluetoothFeatureHV3Packets, 1 << 5)
        self.assertEqual(IOBluetooth.kBluetoothFeatureULawLog, 1 << 6)
        self.assertEqual(IOBluetooth.kBluetoothFeatureALawLog, 1 << 7)
        self.assertEqual(IOBluetooth.kBluetoothFeatureCVSD, 1 << 0)
        self.assertEqual(IOBluetooth.kBluetoothFeaturePagingScheme, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothFeaturePowerControl, 1 << 2)
        self.assertEqual(IOBluetooth.kBluetoothFeatureTransparentSCOData, 1 << 3)
        self.assertEqual(IOBluetooth.kBluetoothFeatureFlowControlLagBit0, 1 << 4)
        self.assertEqual(IOBluetooth.kBluetoothFeatureFlowControlLagBit1, 1 << 5)
        self.assertEqual(IOBluetooth.kBluetoothFeatureFlowControlLagBit2, 1 << 6)
        self.assertEqual(IOBluetooth.kBluetoothFeatureBroadcastEncryption, 1 << 7)
        self.assertEqual(IOBluetooth.kBluetoothFeatureScatterMode, 1 << 0)
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureEnhancedDataRateACL2MbpsMode, 1 << 1
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureEnhancedDataRateACL3MbpsMode, 1 << 2
        )
        self.assertEqual(IOBluetooth.kBluetoothFeatureEnhancedInquiryScan, 1 << 3)
        self.assertEqual(IOBluetooth.kBluetoothFeatureInterlacedInquiryScan, 1 << 4)
        self.assertEqual(IOBluetooth.kBluetoothFeatureInterlacedPageScan, 1 << 5)
        self.assertEqual(IOBluetooth.kBluetoothFeatureRSSIWithInquiryResult, 1 << 6)
        self.assertEqual(IOBluetooth.kBluetoothFeatureExtendedSCOLink, 1 << 7)
        self.assertEqual(IOBluetooth.kBluetoothFeatureEV4Packets, 1 << 0)
        self.assertEqual(IOBluetooth.kBluetoothFeatureEV5Packets, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothFeatureAbsenceMasks, 1 << 2)
        self.assertEqual(IOBluetooth.kBluetoothFeatureAFHCapablePeripheral, 1 << 3)
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureAFHClassificationPeripheral, 1 << 4
        )
        self.assertEqual(IOBluetooth.kBluetoothFeatureAliasAuhentication, 1 << 5)
        self.assertEqual(IOBluetooth.kBluetoothFeatureLESupportedController, 1 << 6)
        self.assertEqual(
            IOBluetooth.kBluetoothFeature3SlotEnhancedDataRateACLPackets, 1 << 7
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureAFHCapableSlave,
            IOBluetooth.kBluetoothFeatureAFHCapablePeripheral,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureAFHClassificationSlave,
            IOBluetooth.kBluetoothFeatureAFHClassificationPeripheral,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeature5SlotEnhancedDataRateACLPackets, 1 << 0
        )
        self.assertEqual(IOBluetooth.kBluetoothFeatureSniffSubrating, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothFeaturePauseEncryption, 1 << 2)
        self.assertEqual(IOBluetooth.kBluetoothFeatureAFHCapableMaster, 1 << 3)
        self.assertEqual(IOBluetooth.kBluetoothFeatureAFHClassificationMaster, 1 << 4)
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureEnhancedDataRateeSCO2MbpsMode, 1 << 5
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureEnhancedDataRateeSCO3MbpsMode, 1 << 6
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeature3SlotEnhancedDataRateeSCOPackets, 1 << 7
        )
        self.assertEqual(IOBluetooth.kBluetoothFeatureExtendedInquiryResponse, 1 << 0)
        self.assertEqual(IOBluetooth.kBluetoothFeatureSecureSimplePairing, 1 << 3)
        self.assertEqual(IOBluetooth.kBluetoothFeatureEncapsulatedPDU, 1 << 4)
        self.assertEqual(IOBluetooth.kBluetoothFeatureErroneousDataReporting, 1 << 5)
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureNonFlushablePacketBoundaryFlag, 1 << 6
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureLinkSupervisionTimeoutChangedEvent, 1 << 0
        )
        self.assertEqual(
            IOBluetooth.kBluetoothFeatureInquiryTransmissionPowerLevel, 1 << 1
        )
        self.assertEqual(IOBluetooth.kBluetoothFeatureExtendedFeatures, 1 << 7)
        self.assertEqual(
            IOBluetooth.kBluetoothExtendedFeatureSimpleSecurePairingHostMode, 1 << 0
        )
        self.assertEqual(
            IOBluetooth.kBluetoothExtendedFeatureLESupportedHostMode, 1 << 1
        )
        self.assertEqual(
            IOBluetooth.kBluetoothExtendedFeatureLEAndBREDRToSameDeviceHostMode, 1 << 2
        )
        self.assertEqual(
            IOBluetooth.KBluetoothExtendedFeatureSecureConnectionsHostMode, 1 << 3
        )
        self.assertEqual(
            IOBluetooth.kBluetoothExtendedFeatureSecureConnectionsControllerSupport,
            1 << 0,
        )
        self.assertEqual(IOBluetooth.kBluetoothExtendedFeaturePing, 1 << 1)
        self.assertEqual(IOBluetooth.kBluetoothExtendedFeatureReserved, 1 << 2)
        self.assertEqual(IOBluetooth.kBluetoothExtendedFeatureTrainNudging, 1 << 3)
        self.assertEqual(
            IOBluetooth.kBluetoothExtendedFeatureSlotAvailabilityMask, 1 << 4
        )

        self.assertIsEnumType(IOBluetooth.BluetoothHCIRoles)
        self.assertEqual(IOBluetooth.kBluetoothHCICentralRole, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIPeripheralRole, 0x01)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIMasterRole, IOBluetooth.kBluetoothHCICentralRole
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCISlaveRole, IOBluetooth.kBluetoothHCIPeripheralRole
        )

        self.assertIsEnumType(IOBluetooth.BluetoothHCILinkPolicySettingsValues)
        self.assertEqual(IOBluetooth.kDisableAllLMModes, 0x0000)
        self.assertEqual(IOBluetooth.kEnableCentralPeripheralSwitch, 0x0001)
        self.assertEqual(IOBluetooth.kEnableHoldMode, 0x0002)
        self.assertEqual(IOBluetooth.kEnableSniffMode, 0x0004)
        self.assertEqual(IOBluetooth.kEnableParkMode, 0x0008)
        self.assertEqual(IOBluetooth.kReservedForFutureUse, 0x0010)
        self.assertEqual(
            IOBluetooth.kEnableMasterSlaveSwitch,
            IOBluetooth.kEnableCentralPeripheralSwitch,
        )

        self.assertIsEnumType(IOBluetooth.BluetoothHCILoopbackMode)
        self.assertEqual(IOBluetooth.kBluetoothHCILoopbackModeOff, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCILoopbackModeLocal, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCILoopbackModeRemote, 0x02)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIPageScanMode)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIPageScanModes)
        self.assertEqual(IOBluetooth.kMandatoryPageScanMode, 0x00)
        self.assertEqual(IOBluetooth.kOptionalPageScanMode1, 0x01)
        self.assertEqual(IOBluetooth.kOptionalPageScanMode2, 0x02)
        self.assertEqual(IOBluetooth.kOptionalPageScanMode3, 0x03)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIPageScanPeriodMode)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIPageScanPeriodModes)
        self.assertEqual(IOBluetooth.kP0Mode, 0x00)
        self.assertEqual(IOBluetooth.kP1Mode, 0x01)
        self.assertEqual(IOBluetooth.kP2Mode, 0x02)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIPageScanEnableState)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIPageScanEnableStates)
        self.assertEqual(IOBluetooth.kNoScansEnabled, 0x00)
        self.assertEqual(IOBluetooth.kInquiryScanEnabledPageScanDisabled, 0x01)
        self.assertEqual(IOBluetooth.kInquiryScanDisabledPageScanEnabled, 0x02)
        self.assertEqual(IOBluetooth.kInquiryScanEnabledPageScanEnabled, 0x03)

        self.assertIsEnumType(IOBluetooth.BluetoothHCITimeoutValues)
        self.assertEqual(IOBluetooth.kDefaultPageTimeout, 0x2710)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIDeleteStoredLinkKeyFlags)
        self.assertEqual(IOBluetooth.kDeleteKeyForSpecifiedDeviceOnly, 0x00)
        self.assertEqual(IOBluetooth.kDeleteAllStoredLinkKeys, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIReadStoredLinkKeysFlags)
        self.assertEqual(IOBluetooth.kReturnLinkKeyForSpecifiedDeviceOnly, 0x00)
        self.assertEqual(IOBluetooth.kReadAllStoredLinkKeys, 0x01)

        self.assertEqual(IOBluetooth.kMaximumNumberOfInquiryAccessCodes, 0x40)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIFlowControlState)
        self.assertIsEnumType(IOBluetooth.BluetoothHCISCOFlowControlStates)
        self.assertEqual(IOBluetooth.kSCOFlowControlDisabled, 0x00)
        self.assertEqual(IOBluetooth.kSCOFlowControlEnabled, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIGeneralFlowControlStates)
        self.assertEqual(IOBluetooth.kHostControllerToHostFlowControlOff, 0x00)
        self.assertEqual(IOBluetooth.kHCIACLDataPacketsOnHCISCODataPacketsOff, 0x01)
        self.assertEqual(IOBluetooth.kHCIACLDataPacketsOffHCISCODataPacketsOn, 0x02)
        self.assertEqual(IOBluetooth.kHCIACLDataPacketsOnHCISCODataPacketsOn, 0x03)

        self.assertIsEnumType(IOBluetooth.BluetoothHCITransmitPowerLevelType)
        self.assertIsEnumType(IOBluetooth.BluetoothHCITransmitReadPowerLevelTypes)
        self.assertEqual(IOBluetooth.kReadCurrentTransmitPowerLevel, 0x00)
        self.assertEqual(IOBluetooth.kReadMaximumTransmitPowerLevel, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIAFHChannelAssessmentMode)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIAFHChannelAssessmentModes)
        self.assertEqual(IOBluetooth.kAFHChannelAssessmentModeDisabled, 0x00)
        self.assertEqual(IOBluetooth.kAFHChannelAssessmentModeEnabled, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIHoldModeActivity)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIHoldModeActivityStates)
        self.assertEqual(IOBluetooth.kMaintainCurrentPowerState, 0x00)
        self.assertEqual(IOBluetooth.kSuspendPageScan, 0x01)
        self.assertEqual(IOBluetooth.kSuspendInquiryScan, 0x02)
        self.assertEqual(IOBluetooth.kSuspendPeriodicInquiries, 0x03)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIAuthenticationEnable)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIAuthentionEnableModes)
        self.assertEqual(IOBluetooth.kAuthenticationDisabled, 0x00)
        self.assertEqual(IOBluetooth.kAuthenticationEnabled, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIEncryptionMode)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIEncryptionModes)
        self.assertEqual(IOBluetooth.kEncryptionDisabled, 0x00)
        self.assertEqual(IOBluetooth.kEncryptionOnlyForPointToPointPackets, 0x01)
        self.assertEqual(
            IOBluetooth.kEncryptionForBothPointToPointAndBroadcastPackets, 0x02
        )

        self.assertIsEnumType(IOBluetooth.BluetoothTransportTypes)
        self.assertEqual(IOBluetooth.kBluetoothTransportTypeUSB, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothTransportTypePCCard, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothTransportTypePCICard, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothTransportTypeUART, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothTransportTypePCIe, 0x05)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIFECRequiredValues)
        self.assertEqual(IOBluetooth.kBluetoothHCIFECRequired, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIFECNotRequired, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothHCIInquiryMode)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIInquiryModes)
        self.assertEqual(IOBluetooth.kBluetoothHCIInquiryModeResultFormatStandard, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIInquiryModeResultFormatWithRSSI, 0x01)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIInquiryModeResultFormatWithRSSIOrExtendedInquiryResultFormat,
            0x02,
        )

        self.assertIsEnumType(IOBluetooth.BluetoothHCIInquiryScanType)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIInquiryScanTypes)
        self.assertEqual(IOBluetooth.kBluetoothHCIInquiryScanTypeStandard, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIInquiryScanTypeInterlaced, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCIInquiryScanTypeReservedStart, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothHCIInquiryScanTypeReservedEnd, 0xFF)

        self.assertIsEnumType(IOBluetooth.BluetoothHCISimplePairingModes)
        self.assertEqual(IOBluetooth.kBluetoothHCISimplePairingModeNotSet, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCISimplePairingModeEnabled, 0x01)

        self.assertIsEnumType(IOBluetooth.BluetoothSimplePairingDebugModes)
        self.assertEqual(IOBluetooth.kBluetoothHCISimplePairingDebugModeDisabled, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCISimplePairingDebugModeEnabled, 0x01)
        self.assertIsEnumType(IOBluetooth.BluetoothIOCapability)
        self.assertIsEnumType(IOBluetooth.BluetoothIOCapabilities)
        self.assertEqual(IOBluetooth.kBluetoothCapabilityTypeDisplayOnly, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothCapabilityTypeDisplayYesNo, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothCapabilityTypeKeyboardOnly, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothCapabilityTypeNoInputNoOutput, 0x03)

        self.assertIsEnumType(IOBluetooth.BluetoothOOBDataPresence)
        self.assertIsEnumType(IOBluetooth.BluetoothOOBDataPresenceValues)
        self.assertEqual(IOBluetooth.kBluetoothOOBAuthenticationDataNotPresent, 0x00)
        self.assertEqual(
            IOBluetooth.kBluetoothOOBAuthenticationDataFromRemoteDevicePresent, 0x01
        )

        self.assertIsEnumType(IOBluetooth.BluetoothAuthenticationRequirements)
        self.assertIsEnumType(IOBluetooth.BluetoothAuthenticationRequirementsValues)
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionNotRequired,
            0x00,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionRequired, 0x01
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionNotRequiredNoBonding,
            0x00,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionRequiredNoBonding,
            0x01,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionNotRequiredDedicatedBonding,
            0x02,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionRequiredDedicatedBonding,
            0x03,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionNotRequiredGeneralBonding,
            0x04,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothAuthenticationRequirementsMITMProtectionRequiredGeneralBonding,
            0x05,
        )

        self.assertIsEnumType(IOBluetooth.BluetoothKeypressNotificationTypes)
        self.assertEqual(
            IOBluetooth.kBluetoothKeypressNotificationTypePasskeyEntryStarted, 0
        )
        self.assertEqual(
            IOBluetooth.kBluetoothKeypressNotificationTypePasskeyDigitEntered, 1
        )
        self.assertEqual(
            IOBluetooth.kBluetoothKeypressNotificationTypePasskeyDigitErased, 2
        )
        self.assertEqual(
            IOBluetooth.kBluetoothKeypressNotificationTypePasskeyCleared, 3
        )
        self.assertEqual(
            IOBluetooth.kBluetoothKeypressNotificationTypePasskeyEntryCompleted, 4
        )

        self.assertEqual(IOBluetooth.kBluetoothHCICommandPacketHeaderSize, 3)
        self.assertEqual(IOBluetooth.kBluetoothHCICommandPacketMaxDataSize, 255)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIMaxCommandPacketSize,
            IOBluetooth.kBluetoothHCICommandPacketHeaderSize
            + IOBluetooth.kBluetoothHCICommandPacketMaxDataSize,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventPacketHeaderSize, 2)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventPacketMaxDataSize, 255)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIMaxEventPacketSize,
            IOBluetooth.kBluetoothHCIEventPacketHeaderSize
            + IOBluetooth.kBluetoothHCIEventPacketMaxDataSize,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIDataPacketHeaderSize, 4)
        self.assertEqual(IOBluetooth.kBluetoothHCIDataPacketMaxDataSize, 65535)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIMaxDataPacketSize,
            IOBluetooth.kBluetoothHCIDataPacketHeaderSize
            + IOBluetooth.kBluetoothHCIDataPacketMaxDataSize,
        )

        self.assertIsEnumType(IOBluetooth.BluetoothLinkType)
        self.assertIsEnumType(IOBluetooth.BluetoothLinkTypes)
        self.assertEqual(IOBluetooth.kBluetoothSCOConnection, 0)
        self.assertEqual(IOBluetooth.kBluetoothACLConnection, 1)
        self.assertEqual(IOBluetooth.kBluetoothESCOConnection, 2)
        self.assertEqual(IOBluetooth.kBluetoothLinkTypeNone, 0xFF)

        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingInputCodingMask, 0x300)
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingInputCodingLinearInputCoding, 0x000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingInputCodingULawInputCoding, 0x100
        )
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingInputCodingALawInputCoding, 0x200
        )

        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingInputDataFormatMask, 0x0C0)
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingInputDataFormat1sComplement, 0x000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingInputDataFormat2sComplement, 0x040
        )
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingInputDataFormatSignMagnitude, 0x080
        )
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingInputDataFormatUnsigned, 0x0C0
        )

        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingInputSampleSizeMask, 0x020)
        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingInputSampleSize8Bit, 0x000)
        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingInputSampleSize16Bit, 0x020)

        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingPCMBitPositionMask, 0x01C)

        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingAirCodingFormatMask, 0x003)
        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingAirCodingFormatCVSD, 0x000)
        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingAirCodingFormatULaw, 0x001)
        self.assertEqual(IOBluetooth.kBluetoothVoiceSettingAirCodingFormatALaw, 0x002)
        self.assertEqual(
            IOBluetooth.kBluetoothVoiceSettingAirCodingFormatTransparentData, 0x003
        )

        self.assertIsEnumType(IOBluetooth.BluetoothHCIRetransmissionEffortTypes)
        self.assertEqual(IOBluetooth.kHCIRetransmissionEffortTypeNone, 0x00)
        self.assertEqual(
            IOBluetooth.kHCIRetransmissionEffortTypeAtLeastOneAndOptimizeForPower, 0x01
        )
        self.assertEqual(
            IOBluetooth.kHCIRetransmissionEffortTypeAtLeastOneAndOptimizeLinkQuality,
            0x02,
        )
        self.assertEqual(IOBluetooth.kHCIRetransmissionEffortTypeDontCare, 0xFF)

        self.assertIsEnumType(IOBluetooth.BluetoothAirMode)
        self.assertEqual(IOBluetooth.kBluetoothAirModeULawLog, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothAirModeALawLog, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothAirModeCVSD, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothAirModeTransparentData, 0x03)

        self.assertEqual(IOBluetooth.kBluetoothHCIEventInquiryComplete, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventInquiryResult, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventConnectionComplete, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventConnectionRequest, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventDisconnectionComplete, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventAuthenticationComplete, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventRemoteNameRequestComplete, 0x07)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventEncryptionChange, 0x08)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventChangeConnectionLinkKeyComplete, 0x09
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMasterLinkKeyComplete, 0x0A)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventReadRemoteSupportedFeaturesComplete, 0x0B
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventReadRemoteVersionInformationComplete, 0x0C
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventQoSSetupComplete, 0x0D)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventCommandComplete, 0x0E)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventCommandStatus, 0x0F)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventHardwareError, 0x10)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventFlushOccurred, 0x11)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventRoleChange, 0x12)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventNumberOfCompletedPackets, 0x13)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventModeChange, 0x14)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventReturnLinkKeys, 0x15)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventPINCodeRequest, 0x16)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventLinkKeyRequest, 0x17)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventLinkKeyNotification, 0x18)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventLoopbackCommand, 0x19)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventDataBufferOverflow, 0x1A)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaxSlotsChange, 0x1B)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventReadClockOffsetComplete, 0x1C)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventConnectionPacketType, 0x1D)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventQoSViolation, 0x1E)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventPageScanModeChange, 0x1F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventPageScanRepetitionModeChange, 0x20
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventFlowSpecificationComplete, 0x21)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventInquiryResultWithRSSI, 0x22)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventReadRemoteExtendedFeaturesComplete, 0x23
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventSynchronousConnectionComplete, 0x2C
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventSynchronousConnectionChanged, 0x2D
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventSniffSubrating, 0x2E)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventExtendedInquiryResult, 0x2F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventEncryptionKeyRefreshComplete, 0x30
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventIOCapabilityRequest, 0x31)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventIOCapabilityResponse, 0x32)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventUserConfirmationRequest, 0x33)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventUserPasskeyRequest, 0x34)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventRemoteOOBDataRequest, 0x35)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventSimplePairingComplete, 0x36)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventLinkSupervisionTimeoutChanged, 0x38
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventEnhancedFlushComplete, 0x39)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventUserPasskeyNotification, 0x3B)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventKeypressNotification, 0x3C)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventRemoteHostSupportedFeaturesNotification, 0x3D
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventLEMetaEvent, 0x3E)
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEConnectionComplete, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEAdvertisingReport, 0x02)
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEConnectionUpdateComplete, 0x03
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEReadRemoteUsedFeaturesComplete, 0x04
        )
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLELongTermKeyRequest, 0x05)
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLERemoteConnectionParameterRequest, 0x06
        )
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEDataLengthChange, 0x07)
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEReadLocalP256PublicKeyComplete, 0x08
        )
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEGenerateDHKeyComplete, 0x09)
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEEnhancedConnectionComplete, 0x0A
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEDirectAdvertisingReport, 0x0B
        )
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEPhyUpdateComplete, 0x0C)
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEExtendedAdvertising, 0x0D)
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEPeriodicAdvertisingSyncEstablished, 0x0E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEPeriodicAdvertisingReport, 0x0F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEPeriodicAdvertisingSyncLost, 0x10
        )
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEScanTimeout, 0x11)
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEAdvertisingSetTerminated, 0x12
        )
        self.assertEqual(IOBluetooth.kBluetoothHCISubEventLEScanRequestReceived, 0x13)
        self.assertEqual(
            IOBluetooth.kBluetoothHCISubEventLEChannelSelectionAlgorithm, 0x14
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventPhysicalLinkComplete, 0x40)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventChannelSelected, 0x41)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventDisconnectionPhysicalLinkComplete, 0x42
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventPhysicalLinkLossEarlyWarning, 0x43
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventPhysicalLinkRecovery, 0x44)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventLogicalLinkComplete, 0x45)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventDisconnectionLogicalLinkComplete, 0x46
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventFlowSpecModifyComplete, 0x47)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventNumberOfCompletedDataBlocks, 0x48
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventShortRangeModeChangeComplete, 0x4C
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventAMPStatusChange, 0x4D)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventAMPStartTest, 0x49)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventAMPTestEnd, 0x4A)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventAMPReceiverReport, 0x4B)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventLogoTesting, 0xFE)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventVendorSpecific, 0xFF)

        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskLEDefault64Bit, 0x000000000000001F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskDefault64Bit, 0x00001FFFFFFFFFFF
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskAll64Bit, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskFlowSpecificationCompleteEvent,
            0x0000000100000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskInquiryResultWithRSSIEvent,
            0x0000000200000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskReadRemoteExtendedFeaturesCompleteEvent,
            0x0000000400000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskSynchronousConnectionCompleteEvent,
            0x0000080000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskSynchronousConnectionChangedEvent,
            0x0000100000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskSniffSubratingEvent, 0x0000200000000000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskExtendedInquiryResultEvent,
            0x0000400000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskEncryptionChangeEvent, 0x0000000000000080
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskEncryptionKeyRefreshCompleteEvent,
            0x0000800000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskLinkSupervisionTimeoutChangedEvent,
            0x0080000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskEnhancedFlushCompleteEvent,
            0x0100000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskIOCapabilityRequestEvent,
            0x0001000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskIOCapabilityRequestReplyEvent,
            0x0002000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskUserConfirmationRequestEvent,
            0x0004000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskUserPasskeyRequestEvent,
            0x0008000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskRemoteOOBDataRequestEvent,
            0x0010000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskSimplePairingCompleteEvent,
            0x0020000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEvnetMaskLinkSupervisionTimeoutChangedEvent,
            0x0080000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEvnetMaskEnhancedFlushCompleteEvent,
            0x0100000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskUserPasskeyNotificationEvent,
            0x0400000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskKeypressNotificationEvent,
            0x0800000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskRemoteHostSupportedFeaturesNotificationEvent,
            0x1000000000000000,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskLEMetaEvent, 0x2000000000000000
        )

        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskNone, 0x00000000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskInquiryComplete, 0x00000001)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskInquiryResult, 0x00000002)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskConnectionComplete, 0x00000004
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskConnectionRequest, 0x00000008
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskDisconnectionComplete, 0x00000010
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskAuthenticationComplete, 0x00000020
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskRemoteNameRequestComplete, 0x00000040
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskEncryptionChange, 0x00000080)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskChangeConnectionLinkKeyComplete,
            0x00000100,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskMasterLinkKeyComplete, 0x00000200
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskReadRemoteSupportedFeaturesComplete,
            0x00000400,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskReadRemoteVersionInformationComplete,
            0x00000800,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskQoSSetupComplete, 0x00001000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskCommandComplete, 0x00002000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskCommandStatus, 0x00004000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskHardwareError, 0x00008000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskFlushOccurred, 0x00010000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskRoleChange, 0x00020000)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskNumberOfCompletedPackets, 0x00040000
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskModeChange, 0x00080000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskReturnLinkKeys, 0x00100000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskPINCodeRequest, 0x00200000)
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskLinkKeyRequest, 0x00400000)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskLinkKeyNotification, 0x00800000
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskLoopbackCommand, 0x01000000)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskDataBufferOverflow, 0x02000000
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskMaxSlotsChange, 0x04000000)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskReadClockOffsetComplete, 0x08000000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskConnectionPacketTypeChanged, 0x10000000
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskQoSViolation, 0x20000000)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskPageScanModeChange, 0x40000000
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskPageScanRepetitionModeChange, 0x80000000
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIEventMaskAll, 0xFFFFFFFF)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIEventMaskDefault,
            IOBluetooth.kBluetoothHCIEventMaskAll,
        )

        self.assertEqual(IOBluetooth.kBluetoothHCIErrorSuccess, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorUnknownHCICommand, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorNoConnection, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorHardwareFailure, 0x03)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorPageTimeout, 0x04)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorAuthenticationFailure, 0x05)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorKeyMissing, 0x06)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorMemoryFull, 0x07)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorConnectionTimeout, 0x08)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorMaxNumberOfConnections, 0x09)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorMaxNumberOfSCOConnectionsToADevice, 0x0A
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorACLConnectionAlreadyExists, 0x0B)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorCommandDisallowed, 0x0C)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorHostRejectedLimitedResources, 0x0D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorHostRejectedSecurityReasons, 0x0E
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorHostRejectedRemoteDeviceIsPersonal, 0x0F
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorHostTimeout, 0x10)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorUnsupportedFeatureOrParameterValue, 0x11
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorInvalidHCICommandParameters, 0x12
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorOtherEndTerminatedConnectionUserEnded, 0x13
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorOtherEndTerminatedConnectionLowResources, 0x14
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorOtherEndTerminatedConnectionAboutToPowerOff,
            0x15,
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorConnectionTerminatedByLocalHost, 0x16
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorRepeatedAttempts, 0x17)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorPairingNotAllowed, 0x18)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorUnknownLMPPDU, 0x19)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorUnsupportedRemoteFeature, 0x1A)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorSCOOffsetRejected, 0x1B)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorSCOIntervalRejected, 0x1C)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorSCOAirModeRejected, 0x1D)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorInvalidLMPParameters, 0x1E)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorUnspecifiedError, 0x1F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorUnsupportedLMPParameterValue, 0x20
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorRoleChangeNotAllowed, 0x21)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorLMPResponseTimeout, 0x22)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorLMPErrorTransactionCollision, 0x23
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorLMPPDUNotAllowed, 0x24)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorEncryptionModeNotAcceptable, 0x25
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorUnitKeyUsed, 0x26)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorQoSNotSupported, 0x27)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorInstantPassed, 0x28)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorPairingWithUnitKeyNotSupported, 0x29
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorHostRejectedUnacceptableDeviceAddress, 0x0F
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorDifferentTransactionCollision, 0x2A
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorQoSUnacceptableParameter, 0x2C)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorQoSRejected, 0x2D)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorChannelClassificationNotSupported, 0x2E
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorInsufficientSecurity, 0x2F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorParameterOutOfMandatoryRange, 0x30
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorRoleSwitchPending, 0x31)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorReservedSlotViolation, 0x34)
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorRoleSwitchFailed, 0x35)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorExtendedInquiryResponseTooLarge, 0x36
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorSecureSimplePairingNotSupportedByHost, 0x37
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorHostBusyPairing, 0x38)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorConnectionRejectedDueToNoSuitableChannelFound,
            0x39,
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorControllerBusy, 0x3A)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorUnacceptableConnectionInterval, 0x3B
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorDirectedAdvertisingTimeout, 0x3C)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorConnectionTerminatedDueToMICFailure, 0x3D
        )
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorConnectionFailedToBeEstablished, 0x3E
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorMACConnectionFailed, 0x3F)
        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorCoarseClockAdjustmentRejected, 0x40
        )
        self.assertEqual(IOBluetooth.kBluetoothHCIErrorMax, 0x40)

        self.assertEqual(IOBluetooth.kBluetoothHCIPowerStateON, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCIPowerStateOFF, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothHCIPowerStateUnintialized, 0xFF)
        self.assertIsEnumType(IOBluetooth.BluetoothHCIPowerState)

        self.assertEqual(
            IOBluetooth.kBluetoothHCIErrorPowerIsOFF,
            IOBluetooth.kBluetoothHCIErrorMax + 1,
        )

        self.assertEqual(IOBluetooth.kBluetoothHCITransportUSBClassCode, 0xE0)
        self.assertEqual(IOBluetooth.kBluetoothHCITransportUSBSubClassCode, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothHCITransportUSBProtocolCode, 0x01)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCIEventIDReserved, 0x00)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCIEventIDL2CA_ConnectInd, 0x01)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCIEventIDL2CA_ConfigInd, 0x02)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCIEventIDL2CA_DisconnectInd, 0x03)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPTCIEventIDL2CA_QoSViolationInd, 0x04
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCIEventIDL2CA_TimeOutInd, 0x05)

        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandReserved, 0x0000)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_ConnectReq, 0x0001)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPTCICommandL2CA_DisconnectReq, 0x0002
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_ConfigReq, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_DisableCLT, 0x0004)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_EnableCLT, 0x0005)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_GroupCreate, 0x0006)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_GroupClose, 0x0007)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPTCICommandL2CA_GroupAddMember, 0x0008
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPTCICommandL2CA_GroupRemoveMember, 0x0009
        )
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPTCICommandL2CA_GroupMembership, 0x000A
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_WriteData, 0x000B)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_ReadData, 0x000C)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_Ping, 0x000D)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_GetInfo, 0x000E)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_Reserved1, 0x000F)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_Reserved2, 0x0010)
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_ConnectResp, 0x0011)
        self.assertEqual(
            IOBluetooth.kBluetoothL2CAPTCICommandL2CA_DisconnectResp, 0x0012
        )
        self.assertEqual(IOBluetooth.kBluetoothL2CAPTCICommandL2CA_ConfigResp, 0x0013)

        self.assertEqual(IOBluetooth.kMaxChannelIDPerSide, 31)

        self.assertIsEnumType(IOBluetooth.BluetoothRFCOMMParityType)
        self.assertEqual(IOBluetooth.kBluetoothRFCOMMParityTypeNoParity, 0)
        self.assertEqual(IOBluetooth.kBluetoothRFCOMMParityTypeOddParity, 1)
        self.assertEqual(IOBluetooth.kBluetoothRFCOMMParityTypeEvenParity, 2)
        self.assertEqual(IOBluetooth.kBluetoothRFCOMMParityTypeMaxParity, 3)
        self.assertIsEnumType(IOBluetooth.BluetoothRFCOMMParityType)

        self.assertIsEnumType(IOBluetooth.BluetoothRFCOMMLineStatus)
        self.assertEqual(IOBluetooth.BluetoothRFCOMMLineStatusNoError, 0)
        self.assertEqual(IOBluetooth.BluetoothRFCOMMLineStatusOverrunError, 1)
        self.assertEqual(IOBluetooth.BluetoothRFCOMMLineStatusParityError, 2)
        self.assertEqual(IOBluetooth.BluetoothRFCOMMLineStatusFramingError, 3)

        self.assertIsEnumType(IOBluetooth.BluetoothSDPPDUID)
        self.assertEqual(IOBluetooth.kBluetoothSDPPDUIDReserved, 0)
        self.assertEqual(IOBluetooth.kBluetoothSDPPDUIDErrorResponse, 1)
        self.assertEqual(IOBluetooth.kBluetoothSDPPDUIDServiceSearchRequest, 2)
        self.assertEqual(IOBluetooth.kBluetoothSDPPDUIDServiceSearchResponse, 3)
        self.assertEqual(IOBluetooth.kBluetoothSDPPDUIDServiceAttributeRequest, 4)
        self.assertEqual(IOBluetooth.kBluetoothSDPPDUIDServiceAttributeResponse, 5)
        self.assertEqual(IOBluetooth.kBluetoothSDPPDUIDServiceSearchAttributeRequest, 6)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPPDUIDServiceSearchAttributeResponse, 7
        )

        self.assertIsEnumType(IOBluetooth.BluetoothSDPErrorCode)
        self.assertEqual(IOBluetooth.kBluetoothSDPErrorCodeSuccess, 0x0000)
        self.assertEqual(IOBluetooth.kBluetoothSDPErrorCodeReserved, 0x0000)
        self.assertEqual(IOBluetooth.kBluetoothSDPErrorCodeInvalidSDPVersion, 0x0001)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPErrorCodeInvalidServiceRecordHandle, 0x0002
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPErrorCodeInvalidRequestSyntax, 0x0003)
        self.assertEqual(IOBluetooth.kBluetoothSDPErrorCodeInvalidPDUSize, 0x0004)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPErrorCodeInvalidContinuationState, 0x0005
        )
        self.assertEqual(
            IOBluetooth.kBluetoothSDPErrorCodeInsufficientResources, 0x0006
        )

        self.assertEqual(IOBluetooth.kBluetoothSDPErrorCodeReservedStart, 0x0007)
        self.assertEqual(IOBluetooth.kBluetoothSDPErrorCodeReservedEnd, 0xFFFF)

        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeNil, 0)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeUnsignedInt, 1)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeSignedInt, 2)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeUUID, 3)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeString, 4)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeBoolean, 5)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeDataElementSequence, 6)
        self.assertEqual(
            IOBluetooth.kBluetoothSDPDataElementTypeDataElementAlternative, 7
        )
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeURL, 8)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeReservedStart, 9)
        self.assertEqual(IOBluetooth.kBluetoothSDPDataElementTypeReservedEnd, 31)

        self.assertEqual(IOBluetooth.BluetoothLEScanTypePassive, 0x00)
        self.assertEqual(IOBluetooth.BluetoothLEScanTypeActive, 0x01)
        self.assertIsEnumType(IOBluetooth.BluetoothLEScanType)

        self.assertEqual(IOBluetooth.BluetoothLEAddressTypePublic, 0x00)
        self.assertEqual(IOBluetooth.BluetoothLEAddressTypeRandom, 0x01)
        self.assertIsEnumType(IOBluetooth.BluetoothLEAddressType)

        self.assertEqual(IOBluetooth.BluetoothLEScanFilterNone, 0x00)
        self.assertEqual(IOBluetooth.BluetoothLEScanFilterSafelist, 0x01)
        self.assertEqual(
            IOBluetooth.BluetoothLEScanFilterWhitelist,
            IOBluetooth.BluetoothLEScanFilterSafelist,
        )
        self.assertIsEnumType(IOBluetooth.BluetoothLEScanFilter)

        self.assertEqual(IOBluetooth.BluetoothLEScanDisable, 0x00)
        self.assertEqual(IOBluetooth.BluetoothLEScanEnable, 0x01)
        self.assertIsEnumType(IOBluetooth.BluetoothLEScan)

        self.assertEqual(IOBluetooth.BluetoothLEConnectionIntervalMin, 0x06)
        self.assertEqual(IOBluetooth.BluetoothLEConnectionIntervalMax, 0x0C80)
        self.assertIsEnumType(IOBluetooth.BluetoothLEConnectionInterval)

        self.assertEqual(IOBluetooth.BluetoothLEScanDuplicateFilterDisable, 0x00)
        self.assertEqual(IOBluetooth.BluetoothLEScanDuplicateFilterEnable, 0x01)
        self.assertIsEnumType(IOBluetooth.BluetoothLEScanDuplicateFilter)

        self.assertEqual(
            IOBluetooth.BluetoothLEAdvertisingTypeConnectableUndirected, 0x00
        )
        self.assertEqual(
            IOBluetooth.BluetoothLEAdvertisingTypeConnectableDirected, 0x01
        )
        self.assertEqual(
            IOBluetooth.BluetoothLEAdvertisingTypeDiscoverableUndirected, 0x02
        )
        self.assertEqual(
            IOBluetooth.BluetoothLEAdvertisingTypeNonConnectableUndirected, 0x03
        )
        self.assertEqual(IOBluetooth.BluetoothLEAdvertisingTypeScanResponse, 0x04)
        self.assertIsEnumType(IOBluetooth.BluetoothLEAdvertisingType)

        self.assertEqual(IOBluetooth.kInfoStringMaxLength, 35)
        self.assertEqual(IOBluetooth.kBluetoothHCIInquiryResultsMaxResults, 50)

    def test_struct_tyeps(self):
        v = IOBluetooth.BluetoothDeviceAddress()
        self.assertIs(v.data, None)

        v = IOBluetooth.BluetoothKey()
        self.assertIs(v.data, None)

        v = IOBluetooth.BluetoothIRK()
        self.assertIs(v.data, None)

        v = IOBluetooth.BluetoothPINCode()
        self.assertIs(v.data, None)

        v = IOBluetooth.BluetoothSetEventMask()
        self.assertIs(v.data, None)

        v = IOBluetooth.BluetoothL2CAPQualityOfServiceOptions()
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.serviceType, 0)
        self.assertEqual(v.tokenRate, 0)
        self.assertEqual(v.tokenBucketSize, 0)
        self.assertEqual(v.peakBandwidth, 0)
        self.assertEqual(v.latency, 0)
        self.assertEqual(v.delayVariation, 0)

        v = IOBluetooth.BluetoothL2CAPRetransmissionAndFlowControlOptions()
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.txWindowSize, 0)
        self.assertEqual(v.maxTransmit, 0)
        self.assertEqual(v.retransmissionTimeout, 0)
        self.assertEqual(v.monitorTimeout, 0)
        self.assertEqual(v.maxPDUPayloadSize, 0)

        v = IOBluetooth.BluetoothHCISupportedCommands()
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothHCISupportedFeatures()
        self.assertEqual(v.data, None)

        self.assertIs(
            IOBluetooth.BluetoothHCILESupportedFeatures,
            IOBluetooth.BluetoothHCISupportedFeatures,
        )
        self.assertIs(
            IOBluetooth.BluetoothHCILEUsedFeatures,
            IOBluetooth.BluetoothHCISupportedFeatures,
        )

        v = IOBluetooth.BluetoothHCIExtendedFeaturesInfo()
        self.assertEqual(v.page, 0)
        self.assertEqual(v.maxPage, 0)
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothEventFilterCondition()
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothHCIFailedContactInfo()
        self.assertEqual(v.count, 0)
        self.assertEqual(v.handle, 0)

        v = IOBluetooth.BluetoothHCIRSSIInfo()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.RSSIValue, 0)

        v = IOBluetooth.BluetoothHCILinkQualityInfo()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.qualityValue, 0)

        v = IOBluetooth.BluetoothHCIEncryptionKeySizeInfo()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.keySize, 0)

        v = IOBluetooth.BluetoothHCIRoleInfo()
        self.assertEqual(v.role, 0)
        self.assertEqual(v.handle, 0)

        v = IOBluetooth.BluetoothHCILinkPolicySettingsInfo()
        self.assertEqual(v.settings, 0)
        self.assertEqual(v.handle, 0)

        v = IOBluetooth.BluetoothHCIQualityOfServiceSetupParams()
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.serviceType, 0)
        self.assertEqual(v.tokenRate, 0)
        self.assertEqual(v.peakBandwidth, 0)
        self.assertEqual(v.latency, 0)
        self.assertEqual(v.delayVariation, 0)

        v = IOBluetooth.BluetoothHCISetupSynchronousConnectionParams()
        self.assertEqual(v.transmitBandwidth, 0)
        self.assertEqual(v.receiveBandwidth, 0)
        self.assertEqual(v.maxLatency, 0)
        self.assertEqual(v.voiceSetting, 0)
        self.assertEqual(v.retransmissionEffort, 0)
        self.assertEqual(v.packetType, 0)

        v = IOBluetooth.BluetoothHCIAcceptSynchronousConnectionRequestParams()
        self.assertEqual(v.transmitBandwidth, 0)
        self.assertEqual(v.receiveBandwidth, 0)
        self.assertEqual(v.maxLatency, 0)
        self.assertEqual(v.contentFormat, 0)
        self.assertEqual(v.retransmissionEffort, 0)
        self.assertEqual(v.packetType, 0)

        v = IOBluetooth.BluetoothHCIEnhancedSetupSynchronousConnectionParams()
        self.assertEqual(v.transmitBandwidth, 0)
        self.assertEqual(v.receiveBandwidth, 0)
        self.assertEqual(v.transmitCodingFormat, 0)
        self.assertEqual(v.receiveCodingFormat, 0)
        self.assertEqual(v.transmitCodecFrameSize, 0)
        self.assertEqual(v.receiveCodecFrameSize, 0)
        self.assertEqual(v.inputBandwidth, 0)
        self.assertEqual(v.outputBandwidth, 0)
        self.assertEqual(v.inputCodingFormat, 0)
        self.assertEqual(v.outputCodingFormat, 0)
        self.assertEqual(v.inputCodedDataSize, 0)
        self.assertEqual(v.outputCodedDataSize, 0)
        self.assertEqual(v.inputPCMDataFormat, 0)
        self.assertEqual(v.outputPCMDataFormat, 0)
        self.assertEqual(v.inputPCMSamplePayloadMSBPosition, 0)
        self.assertEqual(v.outputPCMSamplePayloadMSBPosition, 0)
        self.assertEqual(v.inputDataPath, 0)
        self.assertEqual(v.outputDataPath, 0)
        self.assertEqual(v.inputTransportUnitSize, 0)
        self.assertEqual(v.outputTransportUnitSize, 0)
        self.assertEqual(v.maxLatency, 0)
        self.assertEqual(v.packetType, 0)
        self.assertEqual(v.retransmissionEffort, 0)

        v = IOBluetooth.BluetoothHCIEnhancedAcceptSynchronousConnectionRequestParams()
        self.assertEqual(v.transmitBandwidth, 0)
        self.assertEqual(v.receiveBandwidth, 0)
        self.assertEqual(v.transmitCodingFormat, 0)
        self.assertEqual(v.receiveCodingFormat, 0)
        self.assertEqual(v.transmitCodecFrameSize, 0)
        self.assertEqual(v.receiveCodecFrameSize, 0)
        self.assertEqual(v.inputBandwidth, 0)
        self.assertEqual(v.outputBandwidth, 0)
        self.assertEqual(v.inputCodingFormat, 0)
        self.assertEqual(v.outputCodingFormat, 0)
        self.assertEqual(v.inputCodedDataSize, 0)
        self.assertEqual(v.outputCodedDataSize, 0)
        self.assertEqual(v.inputPCMDataFormat, 0)
        self.assertEqual(v.outputPCMDataFormat, 0)
        self.assertEqual(v.inputPCMSamplePayloadMSBPosition, 0)
        self.assertEqual(v.outputPCMSamplePayloadMSBPosition, 0)
        self.assertEqual(v.inputDataPath, 0)
        self.assertEqual(v.outputDataPath, 0)
        self.assertEqual(v.inputTransportUnitSize, 0)
        self.assertEqual(v.outputTransportUnitSize, 0)
        self.assertEqual(v.maxLatency, 0)
        self.assertEqual(v.packetType, 0)
        self.assertEqual(v.retransmissionEffort, 0)

        v = IOBluetooth.BluetoothReadClockInfo()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.clock, 0)
        self.assertEqual(v.accuracy, 0)

        v = IOBluetooth.BluetoothHCIEventFlowSpecificationData()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.flowDirection, 0)
        self.assertEqual(v.serviceType, 0)
        self.assertEqual(v.tokenRate, 0)
        self.assertEqual(v.tokenBucketSize, 0)
        self.assertEqual(v.peakBandwidth, 0)
        self.assertEqual(v.accessLatency, 0)

        v = IOBluetooth.BluetoothHCIVersionInfo()
        self.assertEqual(v.manufacturerName, 0)
        self.assertEqual(v.lmpVersion, 0)
        self.assertEqual(v.lmpSubVersion, 0)
        self.assertEqual(v.hciVersion, 0)
        self.assertEqual(v.hciRevision, 0)

        v = IOBluetooth.BluetoothHCIBufferSize()
        self.assertEqual(v.ACLDataPacketLength, 0)
        self.assertEqual(v.SCODataPacketLength, 0)
        self.assertEqual(v.totalNumACLDataPackets, 0)
        self.assertEqual(v.totalNumSCODataPackets, 0)

        v = IOBluetooth.BluetoothHCILEBufferSize()
        self.assertEqual(v.ACLDataPacketLength, 0)
        self.assertEqual(v.totalNumACLDataPackets, 0)

        v = IOBluetooth.BluetoothHCIStoredLinkKeysInfo()
        self.assertEqual(v.numLinkKeysRead, 0)
        self.assertEqual(v.maxNumLinkKeysAllowedInDevice, 0)

        v = IOBluetooth.BluetoothHCIScanActivity()
        self.assertEqual(v.scanInterval, 0)
        self.assertEqual(v.scanWindow, 0)

        v = IOBluetooth.BluetoothHCIInquiryAccessCode()
        self.assertEqual(v.data, None)

        # XXX: Needs manual helpers
        v = IOBluetooth.BluetoothHCICurrentInquiryAccessCodes()
        self.assertEqual(v.count, 0)
        self.assertEqual(v.codes, None)

        v = IOBluetooth.BluetoothHCICurrentInquiryAccessCodesForWrite()
        self.assertEqual(v.count, 0)
        self.assertEqual(v.codes, None)

        v = IOBluetooth.BluetoothHCILinkSupervisionTimeout()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.timeout, 0)

        v = IOBluetooth.BluetoothHCITransmitPowerLevelInfo()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.level, 0)

        v = IOBluetooth.BluetoothHCIAutomaticFlushTimeoutInfo()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.timeout, 0)

        v = IOBluetooth.BluetoothTransportInfo()
        self.assertEqual(v.productID, 0)
        self.assertEqual(v.vendorID, 0)
        self.assertEqual(v.type, 0)
        self.assertEqual(v.productName, None)
        self.assertEqual(v.vendorName, None)
        self.assertEqual(v.totalDataBytesSent, 0)
        self.assertEqual(v.totalSCOBytesSent, 0)
        self.assertEqual(v.totalDataBytesReceived, 0)
        self.assertEqual(v.totalSCOBytesReceived, 0)

        v = IOBluetooth.BluetoothHCIInquiryResult()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.pageScanRepetitionMode, 0)
        self.assertEqual(v.pageScanPeriodMode, 0)
        self.assertEqual(v.pageScanMode, 0)
        self.assertEqual(v.classOfDevice, 0)
        self.assertEqual(v.clockOffset, 0)

        v = IOBluetooth.BluetoothHCIInquiryResults()
        self.assertEqual(v.results, None)
        self.assertEqual(v.count, 0)

        v = IOBluetooth.BluetoothHCIInquiryWithRSSIResult()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.pageScanRepetitionMode, 0)
        self.assertEqual(v.reserved, 0)
        self.assertEqual(v.classOfDevice, 0)
        self.assertEqual(v.clockOffset, 0)
        self.assertEqual(v.RSSIValue, 0)

        v = IOBluetooth.BluetoothHCIInquiryWithRSSIResults()
        self.assertEqual(v.results, None)
        self.assertEqual(v.count, 0)

        v = IOBluetooth.BluetoothHCIExtendedInquiryResponse()
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothHCIReadExtendedInquiryResponseResults()
        self.assertEqual(v.outFECRequired, 0)
        self.assertEqual(
            v.extendedInquiryResponse, IOBluetooth.BluetoothHCIExtendedInquiryResponse()
        )

        v = IOBluetooth.BluetoothHCIExtendedInquiryResult()
        self.assertEqual(v.numberOfReponses, 0)
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.pageScanRepetitionMode, 0)
        self.assertEqual(v.reserved, 0)
        self.assertEqual(v.classOfDevice, 0)
        self.assertEqual(v.clockOffset, 0)
        self.assertEqual(v.RSSIValue, 0)
        self.assertEqual(
            v.extendedInquiryResponse, IOBluetooth.BluetoothHCIExtendedInquiryResponse()
        )

        v = IOBluetooth.BluetoothHCIReadLMPHandleResults()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.lmp_handle, 0)
        self.assertEqual(v.reserved, 0)

        v = IOBluetooth.BluetoothHCISimplePairingOOBData()
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothHCIReadLocalOOBDataResults()
        self.assertEqual(v.hash, IOBluetooth.BluetoothHCISimplePairingOOBData())
        self.assertEqual(v.randomizer, IOBluetooth.BluetoothHCISimplePairingOOBData())

        v = IOBluetooth.BluetoothIOCapabilityResponse()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.ioCapability, 0)
        self.assertEqual(v.OOBDataPresence, 0)
        self.assertEqual(v.authenticationRequirements, 0)

        v = IOBluetooth.BluetoothUserPasskeyNotification()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.passkey, 0)

        v = IOBluetooth.BluetoothKeypressNotification()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.notificationType, 0)

        v = IOBluetooth.BluetoothRemoteHostSupportedFeaturesNotification()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(
            v.hostSupportedFeatures, IOBluetooth.BluetoothHCISupportedFeatures()
        )

        v = IOBluetooth.BluetoothAFHHostChannelClassification()
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothAFHResults()
        self.assertEqual(v.handle, 0)
        self.assertEqual(v.mode, 0)
        self.assertEqual(v.afhMap, None)

        v = IOBluetooth.BluetoothUserConfirmationRequest()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.numericValue, 0)

        v = IOBluetooth.BluetoothHCIEventSimplePairingCompleteResults()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())

        v = IOBluetooth.BluetoothSynchronousConnectionInfo()
        self.assertEqual(v.transmitBandWidth, 0)
        self.assertEqual(v.receiveBandWidth, 0)
        self.assertEqual(v.maxLatency, 0)
        self.assertEqual(v.voiceSetting, 0)
        self.assertEqual(v.retransmissionEffort, 0)
        self.assertEqual(v.packetType, 0)

        v = IOBluetooth.BluetoothEnhancedSynchronousConnectionInfo()
        self.assertEqual(v.transmitBandWidth, 0)
        self.assertEqual(v.receiveBandWidth, 0)
        self.assertEqual(v.transmitCodingFormat, 0)
        self.assertEqual(v.receiveCodingFormat, 0)
        self.assertEqual(v.transmitCodecFrameSize, 0)
        self.assertEqual(v.receiveCodecFrameSize, 0)
        self.assertEqual(v.inputBandwidth, 0)
        self.assertEqual(v.outputBandwidth, 0)
        self.assertEqual(v.inputCodingFormat, 0)
        self.assertEqual(v.outputCodingFormat, 0)
        self.assertEqual(v.inputCodedDataSize, 0)
        self.assertEqual(v.outputCodedDataSize, 0)
        self.assertEqual(v.inputPCMDataFormat, 0)
        self.assertEqual(v.outputPCMDataFormat, 0)
        self.assertEqual(v.inputPCMSampelPayloadMSBPosition, 0)
        self.assertEqual(v.outputPCMSampelPayloadMSBPosition, 0)
        self.assertEqual(v.inputDataPath, 0)
        self.assertEqual(v.outputDataPath, 0)
        self.assertEqual(v.inputTransportUnitSize, 0)
        self.assertEqual(v.outputTransportUnitSize, 0)
        self.assertEqual(v.maxLatency, 0)
        self.assertEqual(v.voiceSetting, 0)
        self.assertEqual(v.retransmissionEffort, 0)
        self.assertEqual(v.packetType, 0)

        v = IOBluetooth.BluetoothHCIEventSynchronousConnectionCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.linkType, 0)
        self.assertEqual(v.transmissionInterval, 0)
        self.assertEqual(v.retransmissionWindow, 0)
        self.assertEqual(v.receivePacketLength, 0)
        self.assertEqual(v.transmitPacketLength, 0)
        self.assertEqual(v.airMode, 0)

        v = IOBluetooth.BluetoothHCIEventSynchronousConnectionChangedResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.transmissionInterval, 0)
        self.assertEqual(v.retransmissionWindow, 0)
        self.assertEqual(v.receivePacketLength, 0)
        self.assertEqual(v.transmitPacketLength, 0)

        v = IOBluetooth.BluetoothHCIEventConnectionCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.linkType, 0)
        self.assertEqual(v.encryptionMode, 0)

        v = IOBluetooth.BluetoothHCIEventLEConnectionCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.role, 0)
        self.assertEqual(v.peerAddressType, 0)
        self.assertEqual(v.peerAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.connInterval, 0)
        self.assertEqual(v.connLatency, 0)
        self.assertEqual(v.supervisionTimeout, 0)
        self.assertEqual(v.masterClockAccuracy, 0)

        v = IOBluetooth.BluetoothHCIEventLEEnhancedConnectionCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.role, 0)
        self.assertEqual(v.peerAddressType, 0)
        self.assertEqual(v.peerAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(
            v.localResolvablePrivateAddress, IOBluetooth.BluetoothDeviceAddress()
        )
        self.assertEqual(
            v.peerResolvablePrivateAddress, IOBluetooth.BluetoothDeviceAddress()
        )
        self.assertEqual(v.connInterval, 0)
        self.assertEqual(v.connLatency, 0)
        self.assertEqual(v.supervisionTimeout, 0)
        self.assertEqual(v.masterClockAccuracy, 0)

        v = IOBluetooth.BluetoothHCIEventLEConnectionUpdateCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.connInterval, 0)
        self.assertEqual(v.connLatency, 0)
        self.assertEqual(v.supervisionTimeout, 0)

        v = IOBluetooth.BluetoothHCIEventLEReadRemoteUsedFeaturesCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.usedFeatures, IOBluetooth.BluetoothHCISupportedFeatures())

        v = IOBluetooth.BluetoothHCIEventDisconnectionCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.reason, 0)

        v = IOBluetooth.BluetoothHCIEventReadSupportedFeaturesResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(
            v.supportedFeatures, IOBluetooth.BluetoothHCISupportedFeatures()
        )

        v = IOBluetooth.BluetoothHCIEventReadExtendedFeaturesResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(
            v.supportedFeaturesInfo, IOBluetooth.BluetoothHCIExtendedFeaturesInfo()
        )

        v = IOBluetooth.BluetoothHCIEventReadRemoteVersionInfoResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.lmpVersion, 0)
        self.assertEqual(v.manufacturerName, 0)
        self.assertEqual(v.lmpSubversion, 0)

        v = IOBluetooth.BluetoothHCIEventRemoteNameRequestResults()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.deviceName, None)

        v = IOBluetooth.BluetoothHCIEventReadClockOffsetResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.clockOffset, 0)

        v = IOBluetooth.BluetoothHCIEventConnectionRequestResults()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.classOfDevice, 0)
        self.assertEqual(v.linkType, 0)

        v = IOBluetooth.BluetoothHCIEventLinkKeyNotificationResults()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.linkKey, IOBluetooth.BluetoothKey())
        self.assertEqual(v.keyType, 0)

        v = IOBluetooth.BluetoothHCIEventMaxSlotsChangeResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.maxSlots, 0)

        v = IOBluetooth.BluetoothHCIEventModeChangeResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.mode, 0)
        self.assertEqual(v.modeInterval, 0)

        # XXX: This needs manual helpers!
        if 1:
            self.assertNotHasAttr(IOBluetooth, "BluetoothHCIEventReturnLinkKeysResults")
        else:
            v = IOBluetooth.BluetoothHCIEventReturnLinkKeysResults()
            self.assertEqual(v.numLinkKeys, 0)
            self.assertEqual(v.linkKeys, None)

        v = IOBluetooth.BluetoothHCIEventAuthenticationCompleteResults()
        self.assertEqual(v.connectionHandle, 0)

        v = IOBluetooth.BluetoothHCIEventEncryptionChangeResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.enable, 0)

        v = IOBluetooth.BluetoothHCIEventChangeConnectionLinkKeyCompleteResults()
        self.assertEqual(v.connectionHandle, 0)

        v = IOBluetooth.BluetoothHCIEventMasterLinkKeyCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.keyFlag, 0)

        v = IOBluetooth.BluetoothHCIEventQoSSetupCompleteResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(
            v.setupParams, IOBluetooth.BluetoothHCIQualityOfServiceSetupParams()
        )

        v = IOBluetooth.BluetoothHCIEventHardwareErrorResults()
        self.assertEqual(v.error, 0)

        v = IOBluetooth.BluetoothHCIEventFlushOccurredResults()
        self.assertEqual(v.connectionHandle, 0)

        v = IOBluetooth.BluetoothHCIEventRoleChangeResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.role, 0)

        v = IOBluetooth.BluetoothHCIEventDataBufferOverflowResults()
        self.assertEqual(v.linkType, 0)

        v = IOBluetooth.BluetoothHCIEventConnectionPacketTypeResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.packetType, 0)

        v = IOBluetooth.BluetoothHCIEventReadRemoteSupportedFeaturesResults()
        self.assertEqual(v.error, 0)
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.lmpFeatures, IOBluetooth.BluetoothHCISupportedFeatures())

        v = IOBluetooth.BluetoothHCIEventReadRemoteExtendedFeaturesResults()
        self.assertEqual(v.error, 0)
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.page, 0)
        self.assertEqual(v.maxPage, 0)
        self.assertEqual(v.lmpFeatures, IOBluetooth.BluetoothHCISupportedFeatures())

        v = IOBluetooth.BluetoothHCIEventQoSViolationResults()
        self.assertEqual(v.connectionHandle, 0)

        v = IOBluetooth.BluetoothHCIEventPageScanModeChangeResults()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.pageScanMode, 0)

        v = IOBluetooth.BluetoothHCIEventPageScanRepetitionModeChangeResults()
        self.assertEqual(v.deviceAddress, IOBluetooth.BluetoothDeviceAddress())
        self.assertEqual(v.pageScanRepetitionMode, 0)

        v = IOBluetooth.BluetoothHCIEventVendorSpecificResults()
        self.assertEqual(v.length, 0)
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothHCIEventEncryptionKeyRefreshCompleteResults()
        self.assertEqual(v.connectionHandle, 0)

        v = IOBluetooth.BluetoothHCIEventSniffSubratingResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.maxTransmitLatency, 0)
        self.assertEqual(v.maxReceiveLatency, 0)
        self.assertEqual(v.minRemoteTimeout, 0)
        self.assertEqual(v.minLocalTimeout, 0)

        v = IOBluetooth.BluetoothHCIEventLEMetaResults()
        self.assertEqual(v.length, 0)
        self.assertEqual(v.data, None)

        v = IOBluetooth.BluetoothHCIEventLELongTermKeyRequestResults()
        self.assertEqual(v.connectionHandle, 0)
        self.assertEqual(v.randomNumber, None)
        self.assertEqual(v.ediv, 0)

        v = IOBluetooth.BluetoothHCIRequestCallbackInfo()
        self.assertEqual(v.userCallback, 0)
        self.assertEqual(v.userRefCon, 0)
        self.assertEqual(v.internalRefCon, 0)
        self.assertEqual(v.asyncIDRefCon, 0)
        self.assertEqual(v.reserved, 0)

    def test_inline_functions(self):
        inCOD = 42

        self.assertEqual(
            IOBluetooth.BluetoothGetDeviceClassMajor(inCOD), ((inCOD) & 0x00001F00) >> 8
        )
        self.assertEqual(
            IOBluetooth.BluetoothGetDeviceClassMinor(inCOD), ((inCOD) & 0x000000FC) >> 2
        )
        self.assertEqual(
            IOBluetooth.BluetoothGetServiceClassMajor(inCOD),
            ((inCOD) & 0x00FFE000) >> 13,
        )

        inServiceClassMajor = 42
        inDeviceClassMajor = 43
        inDeviceClassMinor = 44
        self.assertEqual(
            IOBluetooth.BluetoothMakeClassOfDevice(
                inServiceClassMajor, inDeviceClassMajor, inDeviceClassMinor
            ),
            (((inServiceClassMajor) << 13) & 0x00FFE000)
            | (((inDeviceClassMajor) << 8) & 0x00001F00)
            | (((inDeviceClassMinor) << 2) & 0x000000FC),
        )

        inSeconds = 99.5
        self.assertEqual(
            IOBluetooth.BluetoothGetSlotsFromSeconds(inSeconds), (inSeconds / 0.000625)
        )

        inSlots = 102.25
        self.assertEqual(
            IOBluetooth.BluetoothGetSecondsFromSlots(inSlots), (inSlots * 0.000625)
        )

        GROUP = 1
        CMD = 2
        OPCODE = 3

        self.assertEqual(
            IOBluetooth.BluetoothHCIMakeCommandOpCode(GROUP, CMD),
            (((GROUP) & 0x003F) << 10) | ((CMD) & 0x03FF),
        )
        self.assertEqual(
            IOBluetooth.BluetoothHCIMakeCommandOpCodeEndianSwap(GROUP, CMD),
            IOBluetooth.CFSwapInt16HostToLittle(
                IOBluetooth.BluetoothHCIMakeCommandOpCode(GROUP, CMD)
            ),
        )
        self.assertEqual(
            IOBluetooth.BluetoothHCIExtractCommandOpCodeGroup(OPCODE),
            ((OPCODE) >> 10) & 0x003F,
        )
        self.assertEqual(
            IOBluetooth.BluetoothHCIExtractCommandOpCodeCommand(OPCODE),
            (OPCODE) & 0x03FF,
        )

        self.assertEqual(
            IOBluetooth.BluetoothHCIMakeCommandOpCodeHostOrder(GROUP, CMD),
            IOBluetooth.CFSwapInt16LittleToHost(
                (((GROUP) & 0x003F) << 10) | ((CMD) & 0x03FF)
            ),
        )

        self.assertTrue(
            IOBluetooth.IS_REQUEST_PDU(
                IOBluetooth.kBluetoothSDPPDUIDServiceSearchRequest
            )
        )
        self.assertTrue(
            IOBluetooth.IS_RESPONSE_PDU(
                IOBluetooth.kBluetoothSDPPDUIDServiceAttributeResponse
            )
        )
        self.assertTrue(IOBluetooth.RFCOMM_CHANNEL_ID_IS_VALID(25))
