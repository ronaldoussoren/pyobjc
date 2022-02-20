import CoreWLAN
import Foundation
from PyObjCTools.TestSupport import TestCase


class TestCoreWLANTypes(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreWLAN.CWChannelBand)
        self.assertIsEnumType(CoreWLAN.CWChannelWidth)
        self.assertIsEnumType(CoreWLAN.CWCipherKeyFlags)
        self.assertIsEnumType(CoreWLAN.CWErr)
        self.assertIsEnumType(CoreWLAN.CWEventType)
        self.assertIsEnumType(CoreWLAN.CWIBSSModeSecurity)
        self.assertIsEnumType(CoreWLAN.CWInterfaceMode)
        self.assertIsEnumType(CoreWLAN.CWKeychainDomain)
        self.assertIsEnumType(CoreWLAN.CWPHYMode)
        self.assertIsEnumType(CoreWLAN.CWSecurity)

    def testConstants(self):
        self.assertEqual(CoreWLAN.kCWNoErr, 0)
        self.assertEqual(CoreWLAN.kCWEAPOLErr, 1)
        self.assertEqual(CoreWLAN.kCWInvalidParameterErr, -3900)
        self.assertEqual(CoreWLAN.kCWNoMemoryErr, -3901)
        self.assertEqual(CoreWLAN.kCWUnknownErr, -3902)
        self.assertEqual(CoreWLAN.kCWNotSupportedErr, -3903)
        self.assertEqual(CoreWLAN.kCWInvalidFormatErr, -3904)
        self.assertEqual(CoreWLAN.kCWTimeoutErr, -3905)
        self.assertEqual(CoreWLAN.kCWUnspecifiedFailureErr, -3906)
        self.assertEqual(CoreWLAN.kCWUnsupportedCapabilitiesErr, -3907)
        self.assertEqual(CoreWLAN.kCWReassociationDeniedErr, -3908)
        self.assertEqual(CoreWLAN.kCWAssociationDeniedErr, -3909)
        self.assertEqual(CoreWLAN.kCWAuthenticationAlgorithmUnsupportedErr, -3910)
        self.assertEqual(CoreWLAN.kCWInvalidAuthenticationSequenceNumberErr, -3911)
        self.assertEqual(CoreWLAN.kCWChallengeFailureErr, -3912)
        self.assertEqual(CoreWLAN.kCWAPFullErr, -3913)
        self.assertEqual(CoreWLAN.kCWUnsupportedRateSetErr, -3914)
        self.assertEqual(CoreWLAN.kCWShortSlotUnsupportedErr, -3915)
        self.assertEqual(CoreWLAN.kCWDSSSOFDMUnsupportedErr, -3916)
        self.assertEqual(CoreWLAN.kCWInvalidInformationElementErr, -3917)
        self.assertEqual(CoreWLAN.kCWInvalidGroupCipherErr, -3918)
        self.assertEqual(CoreWLAN.kCWInvalidPairwiseCipherErr, -3919)
        self.assertEqual(CoreWLAN.kCWInvalidAKMPErr, -3920)
        self.assertEqual(CoreWLAN.kCWUnsupportedRSNVersionErr, -3921)
        self.assertEqual(CoreWLAN.kCWInvalidRSNCapabilitiesErr, -3922)
        self.assertEqual(CoreWLAN.kCWCipherSuiteRejectedErr, -3923)
        self.assertEqual(CoreWLAN.kCWInvalidPMKErr, -3924)
        self.assertEqual(CoreWLAN.kCWSupplicantTimeoutErr, -3925)
        self.assertEqual(CoreWLAN.kCWHTFeaturesNotSupportedErr, -3926)
        self.assertEqual(CoreWLAN.kCWPCOTransitionTimeNotSupportedErr, -3927)
        self.assertEqual(CoreWLAN.kCWReferenceNotBoundErr, -3928)
        self.assertEqual(CoreWLAN.kCWIPCFailureErr, -3929)
        self.assertEqual(CoreWLAN.kCWOperationNotPermittedErr, -3930)
        self.assertEqual(CoreWLAN.kCWErr, -3931)
        self.assertEqual(CoreWLAN.kCWPHYModeNone, 0)
        self.assertEqual(CoreWLAN.kCWPHYMode11a, 1)
        self.assertEqual(CoreWLAN.kCWPHYMode11b, 2)
        self.assertEqual(CoreWLAN.kCWPHYMode11g, 3)
        self.assertEqual(CoreWLAN.kCWPHYMode11n, 4)
        self.assertEqual(CoreWLAN.kCWPHYMode11ac, 5)
        self.assertEqual(CoreWLAN.kCWPHYMode11ax, 6)
        self.assertEqual(CoreWLAN.kCWInterfaceModeNone, 0)
        self.assertEqual(CoreWLAN.kCWInterfaceModeStation, 1)
        self.assertEqual(CoreWLAN.kCWInterfaceModeIBSS, 2)
        self.assertEqual(CoreWLAN.kCWInterfaceModeHostAP, 3)
        self.assertEqual(CoreWLAN.kCWSecurityNone, 0)
        self.assertEqual(CoreWLAN.kCWSecurityWEP, 1)
        self.assertEqual(CoreWLAN.kCWSecurityWPAPersonal, 2)
        self.assertEqual(CoreWLAN.kCWSecurityWPAPersonalMixed, 3)
        self.assertEqual(CoreWLAN.kCWSecurityWPA2Personal, 4)
        self.assertEqual(CoreWLAN.kCWSecurityPersonal, 5)
        self.assertEqual(CoreWLAN.kCWSecurityDynamicWEP, 6)
        self.assertEqual(CoreWLAN.kCWSecurityWPAEnterprise, 7)
        self.assertEqual(CoreWLAN.kCWSecurityWPAEnterpriseMixed, 8)
        self.assertEqual(CoreWLAN.kCWSecurityWPA2Enterprise, 9)
        self.assertEqual(CoreWLAN.kCWSecurityEnterprise, 10)
        self.assertEqual(CoreWLAN.kCWSecurityWPA3Personal, 11)
        self.assertEqual(CoreWLAN.kCWSecurityWPA3Enterprise, 12)
        self.assertEqual(CoreWLAN.kCWSecurityWPA3Transition, 13)
        self.assertEqual(CoreWLAN.kCWSecurityUnknown, Foundation.NSIntegerMax)
        self.assertEqual(CoreWLAN.kCWIBSSModeSecurityNone, 0)
        self.assertEqual(CoreWLAN.kCWIBSSModeSecurityWEP40, 1)
        self.assertEqual(CoreWLAN.kCWIBSSModeSecurityWEP104, 2)
        self.assertEqual(CoreWLAN.kCWChannelWidthUnknown, 0)
        self.assertEqual(CoreWLAN.kCWChannelWidth20MHz, 1)
        self.assertEqual(CoreWLAN.kCWChannelWidth40MHz, 2)
        self.assertEqual(CoreWLAN.kCWChannelWidth80MHz, 3)
        self.assertEqual(CoreWLAN.kCWChannelWidth160MHz, 4)
        self.assertEqual(CoreWLAN.kCWChannelBandUnknown, 0)
        self.assertEqual(CoreWLAN.kCWChannelBand2GHz, 1)
        self.assertEqual(CoreWLAN.kCWChannelBand5GHz, 2)
        self.assertEqual(CoreWLAN.kCWCipherKeyFlagsNone, 0)
        self.assertEqual(CoreWLAN.kCWCipherKeyFlagsUnicast, 1 << 1)
        self.assertEqual(CoreWLAN.kCWCipherKeyFlagsMulticast, 1 << 2)
        self.assertEqual(CoreWLAN.kCWCipherKeyFlagsTx, 1 << 3),
        self.assertEqual(CoreWLAN.kCWCipherKeyFlagsRx, 1 << 4),
        self.assertEqual(CoreWLAN.kCWParamErr, CoreWLAN.kCWInvalidParameterErr)
        self.assertEqual(CoreWLAN.kCWNoMemErr, CoreWLAN.kCWNoMemoryErr)
        self.assertEqual(CoreWLAN.kCWUknownErr, CoreWLAN.kCWUnknownErr)
        self.assertEqual(CoreWLAN.kCWFormatErr, CoreWLAN.kCWInvalidFormatErr)
        self.assertEqual(
            CoreWLAN.kCWAuthAlgUnsupportedErr,
            CoreWLAN.kCWAuthenticationAlgorithmUnsupportedErr,
        )
        self.assertEqual(
            CoreWLAN.kCWInvalidAuthSeqNumErr,
            CoreWLAN.kCWInvalidAuthenticationSequenceNumberErr,
        )
        self.assertEqual(
            CoreWLAN.kCWInvalidInfoElementErr, CoreWLAN.kCWInvalidInformationElementErr
        )
        self.assertEqual(
            CoreWLAN.kCWHTFeaturesNotSupported, CoreWLAN.kCWHTFeaturesNotSupportedErr
        )
        self.assertEqual(
            CoreWLAN.kCWPCOTransitionTimeNotSupported,
            CoreWLAN.kCWPCOTransitionTimeNotSupportedErr,
        )
        self.assertEqual(CoreWLAN.kCWRefNotBoundErr, CoreWLAN.kCWReferenceNotBoundErr)
        self.assertEqual(CoreWLAN.kCWIPCError, CoreWLAN.kCWIPCFailureErr)
        self.assertEqual(
            CoreWLAN.kCWOpNotPermitted, CoreWLAN.kCWOperationNotPermittedErr
        )
        self.assertEqual(CoreWLAN.kCWError, CoreWLAN.kCWErr)
        self.assertEqual(CoreWLAN.kCWPHYMode11A, 0)
        self.assertEqual(CoreWLAN.kCWPHYMode11B, 1)
        self.assertEqual(CoreWLAN.kCWPHYMode11G, 2)
        self.assertEqual(CoreWLAN.kCWPHYMode11N, 3)
        self.assertEqual(CoreWLAN.kCWOpModeStation, 0)
        self.assertEqual(CoreWLAN.kCWOpModeIBSS, 1)
        self.assertEqual(CoreWLAN.kCWOpModeHostAP, 2)
        self.assertEqual(CoreWLAN.kCWOpModeMonitorMode, 3)
        self.assertEqual(CoreWLAN.kCWSecurityModeOpen, 0)
        self.assertEqual(CoreWLAN.kCWSecurityModeWEP, 1)
        self.assertEqual(CoreWLAN.kCWSecurityModeWPA_PSK, 2)
        self.assertEqual(CoreWLAN.kCWSecurityModeWPA2_PSK, 3)
        self.assertEqual(CoreWLAN.kCWSecurityModeDynamicWEP, 4)
        self.assertEqual(CoreWLAN.kCWSecurityModeWPA_Enterprise, 5)
        self.assertEqual(CoreWLAN.kCWSecurityModeWPA2_Enterprise, 6)
        self.assertEqual(CoreWLAN.kCWSecurityModeWPS, 7)
        self.assertEqual(CoreWLAN.kCWInterfaceStateInactive, 0)
        self.assertEqual(CoreWLAN.kCWInterfaceStateScanning, 1)
        self.assertEqual(CoreWLAN.kCWInterfaceStateAuthenticating, 2)
        self.assertEqual(CoreWLAN.kCWInterfaceStateAssociating, 3)
        self.assertEqual(CoreWLAN.kCWInterfaceStateRunning, 4)
        self.assertEqual(CoreWLAN.kCWScanTypeActive, 0)
        self.assertEqual(CoreWLAN.kCWScanTypePassive, 1)
        self.assertEqual(CoreWLAN.kCWScanTypeFast, 2)
        self.assertEqual(CoreWLAN.kCWKeychainDomainNone, 0)
        self.assertEqual(CoreWLAN.kCWKeychainDomainUser, 1)
        self.assertEqual(CoreWLAN.kCWKeychainDomainSystem, 2)
        self.assertEqual(CoreWLAN.CWEventTypeNone, 0)
        self.assertEqual(CoreWLAN.CWEventTypePowerDidChange, 1)
        self.assertEqual(CoreWLAN.CWEventTypeSSIDDidChange, 2)
        self.assertEqual(CoreWLAN.CWEventTypeBSSIDDidChange, 3)
        self.assertEqual(CoreWLAN.CWEventTypeCountryCodeDidChange, 4)
        self.assertEqual(CoreWLAN.CWEventTypeLinkDidChange, 5)
        self.assertEqual(CoreWLAN.CWEventTypeLinkQualityDidChange, 6)
        self.assertEqual(CoreWLAN.CWEventTypeModeDidChange, 7)
        self.assertEqual(CoreWLAN.CWEventTypeScanCacheUpdated, 8)
        self.assertEqual(CoreWLAN.CWEventTypeUnknown, Foundation.NSIntegerMax)

        # Introduced in 10.12
        self.assertEqual(CoreWLAN.CWEventTypeVirtualInterfaceStateChanged, 9)
        self.assertEqual(CoreWLAN.CWEventTypeRangingReportEvent, 10)
