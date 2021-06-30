import CFOpenDirectory
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailure,
    expectedFailureIf,
)


class TestCFOpenDirectoryConstants(TestCase):
    def testConstants(self):
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyAddress, str)
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyPort, str)
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyUsername, str)
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyPassword, str)

        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAttributeTypes, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAFPServer, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAliases, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAugments, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAutomount, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAutomountMap, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAutoServerSetup, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeBootp, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeCertificateAuthorities, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeComputerLists, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeComputerGroups, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeComputers, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeConfiguration, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeEthernets, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeFileMakerServers, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeFTPServer, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeGroups, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeHostServices, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeHosts, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeLDAPServer, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeLocations, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeMounts, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNFS, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNetDomains, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNetGroups, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNetworks, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePeople, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetComputers, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetComputerGroups, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetComputerLists, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetGroups, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetUsers, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePrintService, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePrintServiceUser, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePrinters, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeProtocols, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeQTSServer, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeRecordTypes, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeResources, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeRPC, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeSMBServer, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeServer, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeServices, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeSharePoints, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeUsers, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeWebServer, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAllAttributes, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeStandardOnly, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNativeOnly, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAdminLimits, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAltSecurityIdentities, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAuthenticationHint, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAllTypes, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAuthorityRevocationList, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBirthday, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCACertificate, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCapacity, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeCertificateRevocationList, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeComment, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeContactGUID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeContactPerson, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCreationTimestamp, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCrossCertificatePair, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDataStamp, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFullName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDNSDomain, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDNSNameServer, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeENetAddress, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeExpire, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFirstName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGUID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHardwareUUID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHomeDirectoryQuota, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeHomeDirectorySoftQuota, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHomeLocOwner, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeInternetAlias, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKDCConfigData, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLastName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLDAPSearchBaseSuffix, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLocation, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMapGUID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMCXFlags, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMCXSettings, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMailAttribute, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMetaAutomountMap, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMiddleName, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeModificationTimestamp, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNFSHomeDirectory, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNote, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOperatingSystem, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeOperatingSystemVersion, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOwner, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOwnerGUID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePassword, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePasswordPlus, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePasswordPolicyOptions, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePasswordServerList, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePasswordServerLocation, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePicture, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePort, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePresetUserIsAdmin, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryComputerGUID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryComputerList, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryGroupID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinter1284DeviceID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterLPRHost, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterLPRQueue, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterMakeAndModel, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterType, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterURI, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterXRISupported, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrintServiceInfoText, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrintServiceInfoXML, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrintServiceUserData, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRealUserID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRelativeDNPrefix, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBAcctFlags, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBGroupRID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBHome, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBHomeDrive, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBKickoffTime, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBLogoffTime, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBLogonTime, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBPrimaryGroupSID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBPWDLastSet, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBProfilePath, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBRID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBScriptPath, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBSID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBUserWorkstations, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeServiceType, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSetupAdvertising, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSetupAutoRegister, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSetupLocation, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSetupOccupation, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTimeToLive, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUniqueID, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUserCertificate, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUserPKCS12Data, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUserShell, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUserSMIMECertificate, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSDumpFreq, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSLinkDir, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSPassNo, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSType, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeWeblogURI, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeXMLPlist, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProtocolNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRPCNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNetworkNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAccessControlEntry, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAddressLine1, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAddressLine2, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAddressLine3, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAreaCode, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAuthenticationAuthority, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAutomountInformation, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBootParams, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBuilding, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeServicesLocator, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCity, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCompany, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeComputers, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCountry, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDepartment, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDNSName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeEMailAddress, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeEMailContacts, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFaxNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroup, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroupMembers, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroupMembership, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroupServices, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHomePhoneNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHTML, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHomeDirectory, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeIMHandle, str, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeIPAddress, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeIPAddressAndENetAddress, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeIPv6Address, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeJPEGPhoto, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeJobTitle, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKDCAuthKey, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKeywords, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLDAPReadReplicas, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLDAPWriteReplicas, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMapCoordinates, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMapURI, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMIME, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMobileNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNestedGroups, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNetGroups, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNickName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOrganizationInfo, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOrganizationName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePagerNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePhoneContacts, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePhoneNumber, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePGPPublicKey, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePostalAddress, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePostalAddressContacts, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePostalCode, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNamePrefix, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProtocols, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecordName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRelationships, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeResourceInfo, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeResourceType, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeState, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeStreet, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNameSuffix, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeURL, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSOpts, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAlias, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAuthCredential, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCopyTimestamp, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDateRecordCreated, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKerberosRealm, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeNTDomainComputerAccount, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeOriginalHomeDirectory, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeOriginalNFSHomeDirectory, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOriginalNodeName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryNTDomain, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePwdAgingPolicy, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeReadOnlyNode, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTimePackage, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTotalSize, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAuthMethod, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMetaNodeLocation, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodePath, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePlugInInfo, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecordType, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSchema, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSubNodes, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNetGroupTriplet, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSearchPath, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSearchPolicy, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAutomaticSearchPath, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLocalOnlySearchPath, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCustomSearchPath, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBuildVersion, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeConfigAvailable, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeConfigFile, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCoreFWVersion, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFunctionalState, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFWVersion, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePluginIndex, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNumTableList, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVersion, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePIDValue, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProcessName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTotalRefCount, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDirRefCount, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeRefCount, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecRefCount, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAttrListRefCount, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAttrListValueRefCount, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDirRefs, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeRefs, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecRefs, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAttrListRefs, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAttrListValueRefs, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationType2WayRandom, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationType2WayRandomChangePasswd, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeAPOP, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeCRAM_MD5, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeChangePasswd, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeClearText, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeCrypt, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeDIGEST_MD5, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeDeleteUser, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeGetEffectivePolicy, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeGetGlobalPolicy, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeGetKerberosPrincipal, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeGetPolicy, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeGetUserData, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeGetUserName, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeKerberosTickets, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeMPPEMasterKeys, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeMSCHAP2, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeNTLMv2, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNTLMv2WithSessionKey, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeNewUser, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNewUserWithPolicy, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNodeNativeClearTextOK, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNodeNativeNoClearText, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeReadSecureHash, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMBNTv2UserSessionKey, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMBWorkstationCredentialSessionKey, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSMB_LM_Key, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSMB_NT_Key, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMB_NT_UserSessionKey, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMB_NT_WithUserSessionKey, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetGlobalPolicy, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetLMHash, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetNTHash, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetPassword, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetPasswordAsCurrent, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetPolicy, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetPolicyAsCurrent, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetUserData, str)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetUserName, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetWorkstationPassword, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeWithAuthorizationRef, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeWriteSecureHash, str)

        self.assertEqual(CFOpenDirectory.kODNodeTypeAuthentication, 0x2201)
        self.assertEqual(CFOpenDirectory.kODNodeTypeContacts, 0x2204)
        self.assertEqual(CFOpenDirectory.kODNodeTypeNetwork, 0x2205)
        self.assertEqual(CFOpenDirectory.kODNodeTypeLocalNodes, 0x2200)
        self.assertEqual(CFOpenDirectory.kODNodeTypeConfigure, 0x2202)
        self.assertEqual(CFOpenDirectory.kODMatchAny, 0x0001)
        self.assertEqual(CFOpenDirectory.kODMatchEqualTo, 0x2001)
        self.assertEqual(CFOpenDirectory.kODMatchBeginsWith, 0x2002)
        self.assertEqual(CFOpenDirectory.kODMatchContains, 0x2004)
        self.assertEqual(CFOpenDirectory.kODMatchEndsWith, 0x2003)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveEqualTo, 0x2101)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveBeginsWith, 0x2102)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveContains, 0x2104)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveEndsWith, 0x2103)
        self.assertEqual(CFOpenDirectory.kODMatchGreaterThan, 0x2006)
        self.assertEqual(CFOpenDirectory.kODMatchLessThan, 0x2007)
        self.assertEqual(CFOpenDirectory.kODErrorSuccess, 0)
        self.assertEqual(CFOpenDirectory.kODErrorSessionLocalOnlyDaemonInUse, 1000)
        self.assertEqual(CFOpenDirectory.kODErrorSessionNormalDaemonInUse, 1001)
        self.assertEqual(CFOpenDirectory.kODErrorSessionDaemonNotRunning, 1002)
        self.assertEqual(CFOpenDirectory.kODErrorSessionDaemonRefused, 1003)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyCommunicationError, 1100)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyVersionMismatch, 1101)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyIPUnreachable, 1102)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyUnknownHost, 1103)
        self.assertEqual(CFOpenDirectory.kODErrorNodeUnknownName, 2000)
        self.assertEqual(CFOpenDirectory.kODErrorNodeUnknownType, 2001)
        self.assertEqual(CFOpenDirectory.kODErrorNodeDisabled, 2002)
        self.assertEqual(CFOpenDirectory.kODErrorNodeConnectionFailed, 2100)
        self.assertEqual(CFOpenDirectory.kODErrorNodeUnknownHost, 2200)
        self.assertEqual(CFOpenDirectory.kODErrorQuerySynchronize, 3000)
        self.assertEqual(CFOpenDirectory.kODErrorQueryInvalidMatchType, 3100)
        self.assertEqual(CFOpenDirectory.kODErrorQueryUnsupportedMatchType, 3101)
        self.assertEqual(CFOpenDirectory.kODErrorQueryTimeout, 3102)
        self.assertEqual(CFOpenDirectory.kODErrorRecordReadOnlyNode, 4000)
        self.assertEqual(CFOpenDirectory.kODErrorRecordPermissionError, 4001)
        self.assertEqual(CFOpenDirectory.kODErrorRecordParameterError, 4100)
        self.assertEqual(CFOpenDirectory.kODErrorRecordInvalidType, 4101)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAlreadyExists, 4102)
        self.assertEqual(CFOpenDirectory.kODErrorRecordTypeDisabled, 4103)
        self.assertEqual(CFOpenDirectory.kODErrorRecordNoLongerExists, 4104)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeUnknownType, 4200)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeNotFound, 4201)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeValueSchemaError, 4202)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeValueNotFound, 4203)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsInvalid, 5000)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsMethodNotSupported, 5100)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsNotAuthorized, 5101)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsParameterError, 5102)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsOperationFailed, 5103)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerUnreachable, 5200)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerNotFound, 5201)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerError, 5202)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerTimeout, 5203)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsContactMaster, 5204)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsContactPrimary, 5204)
        self.assertEqual(
            CFOpenDirectory.kODErrorCredentialsServerCommunicationError, 5205
        )
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountNotFound, 5300)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountDisabled, 5301)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountExpired, 5302)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountInactive, 5303)
        self.assertEqual(
            CFOpenDirectory.kODErrorCredentialsAccountTemporarilyLocked, 5304
        )
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountLocked, 5305)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordExpired, 5400)
        self.assertEqual(
            CFOpenDirectory.kODErrorCredentialsPasswordChangeRequired, 5401
        )
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordQualityFailed, 5402)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordTooShort, 5403)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordTooLong, 5404)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordNeedsLetter, 5405)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordNeedsDigit, 5406)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordChangeTooSoon, 5407)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordUnrecoverable, 5408)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsInvalidLogonHours, 5500)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsInvalidComputer, 5501)
        self.assertEqual(CFOpenDirectory.kODErrorPluginOperationNotSupported, 10000)
        self.assertEqual(CFOpenDirectory.kODErrorPluginError, 10001)
        self.assertEqual(CFOpenDirectory.kODErrorDaemonError, 10002)
        self.assertEqual(CFOpenDirectory.kODErrorPluginOperationTimeout, 10003)
        self.assertEqual(CFOpenDirectory.kODErrorPolicyUnsupported, 6000)
        self.assertEqual(CFOpenDirectory.kODErrorPolicyOutOfRange, 6001)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSecureHash, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMetaAmbiguousName, str)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeMetaAugmentedAttributes, str
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMetaRecordName, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKerberosServices, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTrustInformation, str)

        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeOptions, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAdvertisedServices, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLocaleRelay, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLocaleSubnets, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNetworkInterfaces, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeParentLocales, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryLocale, str)

    @expectedFailure
    @min_os_level("10.7")
    def testConstants10_7_missing(self):
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetCertificateHashAsCurrent, str
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(CFOpenDirectory.kODNodeOptionsQuerySkippedSubnode, str)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeQueryInformation, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProfiles, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProfilesTimestamp, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordCannotBeAccountName, str
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyTypePasswordChangeRequired, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyTypePasswordHistory, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordMinimumNumberOfCharacters, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordMaximumNumberOfCharacters, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordMaximumAgeInMinutes, str
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyTypePasswordRequiresAlpha, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordRequiresMixedCase, str
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyTypePasswordRequiresNumeric, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyTypePasswordRequiresSymbol, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordSelfModification, str
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyTypeAccountExpiresOnDate, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMaximumFailedLogins, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMaximumMinutesOfNonUse, str
        )

        self.assertEqual(CFOpenDirectory.kODExpirationTimeExpired, 0)
        self.assertEqual(CFOpenDirectory.kODExpirationTimeNeverExpires, -1)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] in ("10.9", "10.10"))
    @min_os_level("10.9")
    def testConstants10_9_missing(self):
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMaximumMinutesUntilDisabled, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMinutesUntilFailedLoginReset, str
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyIdentifier, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyParameters, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyContent, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyCategoryAuthentication, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyCategoryPasswordContent, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyCategoryPasswordChange, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeRecordName, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeRecordType, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributePassword, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributePasswordHashes, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributePasswordHistory, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributePasswordHistoryDepth, str
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCurrentDate, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCurrentTime, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCurrentTimeOfDay, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCurrentDayOfWeek, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeFailedAuthentications, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeMaximumFailedAuthentications, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeLastFailedAuthenticationTime, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeLastAuthenticationTime, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeLastPasswordChangeTime, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeNewPasswordRequiredTime, str
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCreationTime, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeExpiresEveryNDays, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeEnableOnDate, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeExpiresOnDate, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeEnableOnDayOfWeek, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeExpiresOnDayOfWeek, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeEnableAtTimeOfDay, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeExpiresAtTimeOfDay, str)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeDaysUntilExpiration, str
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyContentDescription, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyEvaluationDetails, str)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyPolicySatisfied, str)

        self.assertIsInstance(CFOpenDirectory.kODModuleConfigOptionQueryTimeout, str)
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionConnectionSetupTimeout, str
        )
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionConnectionIdleDisconnect, str
        )
        self.assertIsInstance(CFOpenDirectory.kODModuleConfigOptionPacketSigning, str)
        self.assertIsInstance(CFOpenDirectory.kODModuleConfigOptionPacketSigning, str)
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionPacketEncryption, str
        )
        self.assertIsInstance(CFOpenDirectory.kODModuleConfigOptionManInTheMiddle, str)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeSASLRealm, str)

    @expectedFailure
    @min_os_level("10.13")
    def testConstants10_13(self):
        # Not actually exported...
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeClearTextReadOnly, str
        )

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(CFOpenDirectory.kODBackOffSeconds, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeMPPEPrimaryKeys, str)
