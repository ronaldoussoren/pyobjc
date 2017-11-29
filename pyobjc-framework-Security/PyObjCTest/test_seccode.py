from PyObjCTools.TestSupport import *

import Security

class TestCode (TestCase):

    def test_types(self):
        self.assertIsCFType(Security.SecCodeRef)

    def test_constants(self):
        self.assertEqual(Security.kSecCSUseAllArchitectures, 1 << 0)

        self.assertIsInstance(Security.kSecGuestAttributeCanonical, unicode)
        self.assertIsInstance(Security.kSecGuestAttributeHash, unicode)
        self.assertIsInstance(Security.kSecGuestAttributeMachPort, unicode)
        self.assertIsInstance(Security.kSecGuestAttributePid, unicode)
        self.assertIsInstance(Security.kSecGuestAttributeDynamicCode, unicode)
        self.assertIsInstance(Security.kSecGuestAttributeDynamicCodeInfoPlist, unicode)

        self.assertEqual(Security.kSecCSInternalInformation, 1 << 0)
        self.assertEqual(Security.kSecCSSigningInformation, 1 << 1)
        self.assertEqual(Security.kSecCSRequirementInformation, 1 << 2)
        self.assertEqual(Security.kSecCSDynamicInformation, 1 << 3)
        self.assertEqual(Security.kSecCSContentInformation, 1 << 4)
        self.assertEqual(Security.kSecCSSkipResourceDirectory, 1 << 5)

        self.assertIsInstance(Security.kSecCodeInfoCertificates, unicode)
        self.assertIsInstance(Security.kSecCodeInfoChangedFiles, unicode)
        self.assertIsInstance(Security.kSecCodeInfoCMS, unicode)
        self.assertIsInstance(Security.kSecCodeInfoDesignatedRequirement, unicode)
        self.assertIsInstance(Security.kSecCodeInfoEntitlements, unicode)
        self.assertIsInstance(Security.kSecCodeInfoEntitlementsDict, unicode)
        self.assertIsInstance(Security.kSecCodeInfoFlags, unicode)
        self.assertIsInstance(Security.kSecCodeInfoFormat, unicode)
        self.assertIsInstance(Security.kSecCodeInfoDigestAlgorithm, unicode)
        self.assertIsInstance(Security.kSecCodeInfoIdentifier, unicode)
        self.assertIsInstance(Security.kSecCodeInfoImplicitDesignatedRequirement, unicode)
        self.assertIsInstance(Security.kSecCodeInfoMainExecutable, unicode)
        self.assertIsInstance(Security.kSecCodeInfoPList, unicode)
        self.assertIsInstance(Security.kSecCodeInfoRequirements, unicode)
        self.assertIsInstance(Security.kSecCodeInfoRequirementData, unicode)
        self.assertIsInstance(Security.kSecCodeInfoSource, unicode)
        self.assertIsInstance(Security.kSecCodeInfoStatus, unicode)
        self.assertIsInstance(Security.kSecCodeInfoTeamIdentifier, unicode)
        self.assertIsInstance(Security.kSecCodeInfoTime, unicode)
        self.assertIsInstance(Security.kSecCodeInfoTimestamp, unicode)
        self.assertIsInstance(Security.kSecCodeInfoTrust, unicode)
        self.assertIsInstance(Security.kSecCodeInfoUnique, unicode)

    @expectedFailure
    def test_constants_missing(self):
        self.assertIsInstance(Security.kSecGuestAttributeArchitecture, unicode)
        self.assertIsInstance(Security.kSecGuestAttributeSubarchitecture, unicode)
        self.assertIsInstance(Security.kSecCodeInfoPlatformIdentifier, unicode)

    @min_os_level('10.11.4')
    def test_constants_10_11_4(self):
        self.assertIsInstance(Security.kSecCodeInfoDigestAlgorithms, unicode)
        self.assertIsInstance(Security.kSecCodeInfoCdHashes, unicode)

    @min_os_level('10.12')
    def test_constants_10_12(self):
        self.assertIsInstance(Security.kSecGuestAttributeAudit, unicode)

    def test_functions(self):
        self.assertIsInstance(Security.SecCodeGetTypeID(), (int, long))

        self.assertResultHasType(Security.SecCodeCopySelf, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopySelf, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCopySelf, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCodeCopySelf, 1)

        self.assertResultHasType(Security.SecCodeCopyStaticCode, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyStaticCode, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyStaticCode, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCopyStaticCode, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCodeCopyStaticCode, 2)

        self.assertResultHasType(Security.SecCodeCopyHost, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyHost, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyHost, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCopyHost, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCodeCopyHost, 2)

        self.assertResultHasType(Security.SecCodeCopyGuestWithAttributes, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyGuestWithAttributes, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyGuestWithAttributes, 1, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyGuestWithAttributes, 2, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCopyGuestWithAttributes, 3, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCodeCopyGuestWithAttributes, 3)

        self.assertResultHasType(Security.SecCodeCheckValidity, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCheckValidity, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCheckValidity, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCheckValidity, 2, objc._C_ID)

        self.assertResultHasType(Security.SecCodeCheckValidityWithErrors, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCheckValidityWithErrors, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCheckValidityWithErrors, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCheckValidityWithErrors, 2, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCheckValidityWithErrors, 3, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecCodeCopyPath, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyPath, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyPath, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCopyPath, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCodeCopyPath, 2)

        self.assertResultHasType(Security.SecCodeCopyDesignatedRequirement, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyDesignatedRequirement, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyDesignatedRequirement, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCopyDesignatedRequirement, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCodeCopyDesignatedRequirement, 2)

        self.assertResultHasType(Security.SecCodeCopySigningInformation, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopySigningInformation, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopySigningInformation, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCopySigningInformation, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCodeCopySigningInformation, 2)

        self.assertResultHasType(Security.SecCodeMapMemory, objc._C_INT)
        self.assertArgHasType(Security.SecCodeMapMemory, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeMapMemory, 1, objc._C_UINT)

if __name__ == "__main__":
    main()
