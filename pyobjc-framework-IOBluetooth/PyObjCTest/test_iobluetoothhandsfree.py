from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestIOBluetoothHandsFree(TestCase):
    def test_constants(self):
        self.assertIsEnumType(IOBluetooth.IOBluetoothHandsFreeDeviceFeatures)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeDeviceFeatureNone, 0)
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureECAndOrNRFunction, 1 << 0
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureThreeWayCalling, 1 << 1
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureCLIPresentation, 1 << 2
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureVoiceRecognition, 1 << 3
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureRemoteVolumeControl, 1 << 4
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureEnhancedCallStatus, 1 << 5
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureEnhancedCallControl, 1 << 6
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeDeviceFeatureCodecNegotiation, 1 << 7
        )

        self.assertIsEnumType(IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatures)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureNone, 0)
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureThreeWayCalling, 1 << 0
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureECAndOrNRFunction, 1 << 1
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureVoiceRecognition, 1 << 2
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureInBandRingTone, 1 << 3
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureAttachedNumberToVoiceTag,
            1 << 4,
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureRejectCallCapability,
            1 << 5,
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureEnhancedCallStatus,
            1 << 6,
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureEnhancedCallControl,
            1 << 7,
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureExtendedErrorResultCodes,
            1 << 8,
        )
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeAudioGatewayFeatureCodecNegotiation, 1 << 9
        )

        self.assertIsEnumType(IOBluetooth.IOBluetoothHandsFreeCallHoldModes)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCallHoldMode0, 1 << 0)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCallHoldMode1, 1 << 1)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCallHoldMode1idx, 1 << 2)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCallHoldMode2, 1 << 3)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCallHoldMode2idx, 1 << 4)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCallHoldMode3, 1 << 5)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCallHoldMode4, 1 << 6)

        self.assertIsEnumType(IOBluetooth.IOBluetoothHandsFreeCodecID)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCodecIDCVSD, 0x01)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCodecIDmSBC, 0x02)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreeCodecIDAACELD, 0x80)

        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeIndicatorService, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeIndicatorCall, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeIndicatorCallSetup, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeIndicatorCallHeld, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeIndicatorSignal, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeIndicatorRoam, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeIndicatorBattChg, str)

        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallIndex, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallDirection, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallStatus, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallMode, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallMultiparty, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallNumber, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallType, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothHandsFreeCallName, str)

        self.assertIsEnumType(IOBluetooth.IOBluetoothSMSMode)
        self.assertEqual(IOBluetooth.IOBluetoothSMSModePDU, 0)
        self.assertEqual(IOBluetooth.IOBluetoothSMSModeText, 1)

        self.assertIsEnumType(IOBluetooth.IOBluetoothHandsFreeSMSSupport)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreePhase2SMSSupport, 1 << 0)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreePhase2pSMSSupport, 1 << 1)
        self.assertEqual(
            IOBluetooth.IOBluetoothHandsFreeManufactureSpecificSMSSupport, 1 << 2
        )

        self.assertIsEnumType(IOBluetooth.IOBluetoothHandsFreePDUMessageStatus)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreePDUStatusRecUnread, 0)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreePDUStatusRecRead, 1)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreePDUStatusStoUnsent, 2)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreePDUStatusStoSent, 3)
        self.assertEqual(IOBluetooth.IOBluetoothHandsFreePDUStatusAll, 4)

        self.assertIsInstance(IOBluetooth.IOBluetoothPDUServicCenterAddress, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUServiceCenterAddressType, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUType, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUOriginatingAddress, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUOriginatingAddressType, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUProtocolID, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUTimestamp, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUEncoding, str)
        self.assertIsInstance(IOBluetooth.IOBluetoothPDUUserData, str)

    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothHandsFreeDelegate")

    def test_methods(self):
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothHandsFree.isInputMuted)
        self.assertArgIsBOOL(IOBluetooth.IOBluetoothHandsFree.setInputMuted_, 0)

        self.assertResultIsBOOL(IOBluetooth.IOBluetoothHandsFree.isOutputMuted)
        self.assertArgIsBOOL(IOBluetooth.IOBluetoothHandsFree.setOutputMuted_, 0)

        self.assertResultIsBOOL(IOBluetooth.IOBluetoothHandsFree.isSMSEnabled)
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothHandsFree.isConnected)
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothHandsFree.isSCOConnected)

        self.assertResultIsBOOL(IOBluetooth.IOBluetoothDevice.isHandsFreeAudioGateway)
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothDevice.isHandsFreeDevice)
