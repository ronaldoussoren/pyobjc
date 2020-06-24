from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level
import SystemConfiguration


class TestSCSchemaDefinitions(TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(SystemConfiguration.kSCEntNetIPSec, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetSMB, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecLocalIdentifier, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetIPSecLocalIdentifierType, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetIPSecAuthenticationMethod, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecSharedSecret, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetIPSecSharedSecretEncryption, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecLocalCertificate, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPSecAuthenticationMethodSharedSecret, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPSecAuthenticationMethodCertificate, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPSecSharedSecretEncryptionKeychain, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPSecLocalIdentifierTypeKeyID, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemAccessPointName, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetModemConnectionPersonality, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemDeviceContextID, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemDeviceModel, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemDeviceVendor, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetPPPAuthPasswordEncryptionToken, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetSMBNetBIOSName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetSMBNetBIOSNodeType, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetSMBNetBIOSScope, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetSMBWINSAddresses, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetSMBWorkgroup, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetSMBNetBIOSNodeTypeBroadcast, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetSMBNetBIOSNodeTypePeer, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetSMBNetBIOSNodeTypeMixed, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetSMBNetBIOSNodeTypeHybrid, str
        )

    @min_os_level("10.6")
    def testConstants10_5_missing(self):
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPSecAuthenticationMethodHybrid, str
        )

    def testConstants(self):
        self.assertIsInstance(SystemConfiguration.kSCResvLink, str)
        self.assertIsInstance(SystemConfiguration.kSCResvInactive, str)
        self.assertIsInstance(SystemConfiguration.kSCPropInterfaceName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropMACAddress, str)
        self.assertIsInstance(SystemConfiguration.kSCPropUserDefinedName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropVersion, str)
        self.assertIsInstance(SystemConfiguration.kSCPrefCurrentSet, str)
        self.assertIsInstance(SystemConfiguration.kSCPrefNetworkServices, str)
        self.assertIsInstance(SystemConfiguration.kSCPrefSets, str)
        self.assertIsInstance(SystemConfiguration.kSCPrefSystem, str)
        self.assertIsInstance(SystemConfiguration.kSCCompNetwork, str)
        self.assertIsInstance(SystemConfiguration.kSCCompService, str)
        self.assertIsInstance(SystemConfiguration.kSCCompGlobal, str)
        self.assertIsInstance(SystemConfiguration.kSCCompHostNames, str)
        self.assertIsInstance(SystemConfiguration.kSCCompInterface, str)
        self.assertIsInstance(SystemConfiguration.kSCCompSystem, str)
        self.assertIsInstance(SystemConfiguration.kSCCompUsers, str)
        self.assertIsInstance(SystemConfiguration.kSCCompAnyRegex, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetAirPort, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetAppleTalk, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetDHCP, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetDNS, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetEthernet, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetFireWire, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetInterface, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetIPv4, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetIPv6, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetL2TP, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetLink, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetModem, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetNetInfo, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetPPP, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetPPPoE, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetPPPSerial, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetPPTP, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNetProxies, str)
        self.assertIsInstance(SystemConfiguration.kSCEntNet6to4, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetOverridePrimary, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetServiceOrder, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPOverridePrimary, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetInterfaces, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetLocalHostName, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetAirPortAllowNetCreation, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetAirPortAuthPassword, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetAirPortAuthPasswordEncryption, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetAirPortJoinMode, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetAirPortPowerEnabled, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetAirPortPreferredNetwork, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetAirPortSavePasswords, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetAirPortJoinModeAutomatic, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetAirPortJoinModePreferred, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetAirPortJoinModeRanked, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetAirPortJoinModeRecent, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetAirPortJoinModeStrongest, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetAirPortAuthPasswordEncryptionKeychain, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSDomainName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSOptions, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSSearchDomains, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSSearchOrder, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSServerAddresses, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSServerPort, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSServerTimeout, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetDNSSortList, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetDNSSupplementalMatchDomains, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetDNSSupplementalMatchOrders, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetEthernetMediaSubType, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetEthernetMediaOptions, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetEthernetMTU, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetInterfaceDeviceName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetInterfaceHardware, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetInterfaceType, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetInterfaceSubType, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetInterfaceSupportsModemOnHold, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceTypeEthernet, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceTypeFireWire, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceTypePPP, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceType6to4, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceSubTypePPPoE, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetInterfaceSubTypePPPSerial, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceSubTypePPTP, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceSubTypeL2TP, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv4Addresses, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv4ConfigMethod, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv4DHCPClientID, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv4Router, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv4SubnetMasks, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv4DestAddresses, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv4BroadcastAddresses, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetIPv4ConfigMethodBOOTP, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetIPv4ConfigMethodDHCP, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetIPv4ConfigMethodINFORM, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPv4ConfigMethodLinkLocal, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetIPv4ConfigMethodManual, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetIPv4ConfigMethodPPP, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv6Addresses, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv6ConfigMethod, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv6DestAddresses, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv6Flags, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv6PrefixLength, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPv6Router, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPv6ConfigMethodAutomatic, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetIPv6ConfigMethodManual, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPv6ConfigMethodRouterAdvertisement, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetIPv6ConfigMethod6to4, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNet6to4Relay, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetLinkActive, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetLinkDetaching, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemConnectionScript, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemConnectSpeed, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemDataCompression, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemDialMode, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemErrorCorrection, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetModemHoldCallWaitingAudibleAlert, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetModemHoldDisconnectOnAnswer, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemHoldEnabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemHoldReminder, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemHoldReminderTime, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemNote, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemPulseDial, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemSpeaker, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetModemSpeed, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetModemDialModeIgnoreDialTone, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetModemDialModeManual, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetModemDialModeWaitForDialTone, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPACSPEnabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPConnectTime, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPDeviceLastCause, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPDialOnDemand, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPDisconnectOnFastUserSwitch, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPDisconnectOnIdle, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPDisconnectOnIdleTimer, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPDisconnectOnLogout, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPDisconnectOnSleep, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPDisconnectTime, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPIdleReminderTimer, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPIdleReminder, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLastCause, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLogfile, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPPlugins, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPRetryConnectTime, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPSessionTimer, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPStatus, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPUseSessionTimer, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPVerboseLogging, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPAuthEAPPlugins, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPAuthName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPAuthPassword, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPAuthPasswordEncryption, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPAuthPrompt, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPAuthProtocol, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetPPPAuthPasswordEncryptionKeychain, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetPPPAuthPromptBefore, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetPPPAuthPromptAfter, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetPPPAuthProtocolCHAP, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetPPPAuthProtocolEAP, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetPPPAuthProtocolMSCHAP1, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetPPPAuthProtocolMSCHAP2, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetPPPAuthProtocolPAP, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPCommAlternateRemoteAddress, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCommConnectDelay, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPCommDisplayTerminalWindow, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCommRedialCount, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCommRedialEnabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCommRedialInterval, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCommRemoteAddress, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCommTerminalScript, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPCommUseTerminalScript, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCCPEnabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCCPMPPE40Enabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPCCPMPPE128Enabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPIPCPCompressionVJ, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPIPCPUsePeerDNS, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLCPEchoEnabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLCPEchoFailure, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLCPEchoInterval, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPLCPCompressionACField, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetPPPLCPCompressionPField, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLCPMRU, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLCPMTU, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLCPReceiveACCM, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetPPPLCPTransmitACCM, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetL2TPIPSecSharedSecret, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetL2TPIPSecSharedSecretEncryption, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetL2TPTransport, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetL2TPIPSecSharedSecretEncryptionKeychain, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetL2TPTransportIP, str)
        self.assertIsInstance(SystemConfiguration.kSCValNetL2TPTransportIPSec, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesExceptionsList, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetProxiesExcludeSimpleHostnames, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesFTPEnable, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesFTPPassive, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesFTPPort, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesFTPProxy, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesGopherEnable, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesGopherPort, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesGopherProxy, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesHTTPEnable, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesHTTPPort, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesHTTPProxy, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesHTTPSEnable, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesHTTPSPort, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesHTTPSProxy, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesRTSPEnable, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesRTSPPort, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesRTSPProxy, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesSOCKSEnable, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesSOCKSPort, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetProxiesSOCKSProxy, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetProxiesProxyAutoConfigEnable, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetProxiesProxyAutoConfigURLString, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetProxiesProxyAutoDiscoveryEnable, str
        )
        self.assertIsInstance(SystemConfiguration.kSCEntUsersConsoleUser, str)
        self.assertIsInstance(SystemConfiguration.kSCPropSystemComputerName, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropSystemComputerNameEncoding, str
        )
        self.assertIsInstance(SystemConfiguration.kSCDynamicStoreDomainFile, str)
        self.assertIsInstance(SystemConfiguration.kSCDynamicStoreDomainPlugin, str)
        self.assertIsInstance(SystemConfiguration.kSCDynamicStoreDomainSetup, str)
        self.assertIsInstance(SystemConfiguration.kSCDynamicStoreDomainState, str)
        self.assertIsInstance(SystemConfiguration.kSCDynamicStoreDomainPrefs, str)
        self.assertIsInstance(
            SystemConfiguration.kSCDynamicStorePropSetupCurrentSet, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCDynamicStorePropSetupLastUpdated, str
        )
        self.assertIsInstance(SystemConfiguration.kSCDynamicStorePropNetInterfaces, str)
        self.assertIsInstance(
            SystemConfiguration.kSCDynamicStorePropNetPrimaryInterface, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCDynamicStorePropNetPrimaryService, str
        )
        self.assertIsInstance(SystemConfiguration.kSCDynamicStorePropNetServiceIDs, str)
        self.assertIsInstance(SystemConfiguration.kSCPropUsersConsoleUserName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropUsersConsoleUserUID, str)
        self.assertIsInstance(SystemConfiguration.kSCPropUsersConsoleUserGID, str)

    @max_os_level("10.11")
    def testConstantsUpto10_12(self):
        self.assertIsInstance(SystemConfiguration.kSCPropNetAppleTalkComputerName, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetAppleTalkComputerNameEncoding, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetAppleTalkConfigMethod, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetAppleTalkDefaultZone, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetAppleTalkNetworkID, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetAppleTalkNetworkRange, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetAppleTalkNodeID, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetAppleTalkSeedNetworkRange, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetAppleTalkSeedZones, str)
        self.assertIsInstance(
            SystemConfiguration.kSCValNetAppleTalkConfigMethodNode, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetAppleTalkConfigMethodRouter, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetAppleTalkConfigMethodSeedRouter, str
        )
        self.assertIsInstance(SystemConfiguration.kSCPropNetNetInfoBindingMethods, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetNetInfoServerAddresses, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetNetInfoServerTags, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetNetInfoBroadcastServerTag, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetNetInfoBindingMethodsBroadcast, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetNetInfoBindingMethodsDHCP, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetNetInfoBindingMethodsManual, str
        )
        self.assertIsInstance(SystemConfiguration.kSCValNetNetInfoDefaultServerTag, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(SystemConfiguration.kSCValNetInterfaceTypeIPSec, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecConnectTime, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecRemoteAddress, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecStatus, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecXAuthEnabled, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecXAuthName, str)
        self.assertIsInstance(SystemConfiguration.kSCPropNetIPSecXAuthPassword, str)
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetIPSecXAuthPasswordEncryption, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPSecXAuthPasswordEncryptionKeychain, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPSecXAuthPasswordEncryptionPrompt, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPv4ConfigMethodAutomatic, str
        )

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(
            SystemConfiguration.kSCValNetIPv6ConfigMethodLinkLocal, str
        )
        self.assertIsInstance(
            SystemConfiguration.kSCPropNetProxiesProxyAutoConfigJavaScript, str
        )
