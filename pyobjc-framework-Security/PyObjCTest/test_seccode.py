import Security
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import objc


class TestCode(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecCodeRef)

    def test_constants(self):
        self.assertEqual(Security.kSecCSUseAllArchitectures, 1 << 0)

        self.assertIsInstance(Security.kSecGuestAttributeCanonical, str)
        self.assertIsInstance(Security.kSecGuestAttributeHash, str)
        self.assertIsInstance(Security.kSecGuestAttributeMachPort, str)
        self.assertIsInstance(Security.kSecGuestAttributePid, str)
        self.assertIsInstance(Security.kSecGuestAttributeDynamicCode, str)
        self.assertIsInstance(Security.kSecGuestAttributeDynamicCodeInfoPlist, str)

        self.assertEqual(Security.kSecCSInternalInformation, 1 << 0)
        self.assertEqual(Security.kSecCSSigningInformation, 1 << 1)
        self.assertEqual(Security.kSecCSRequirementInformation, 1 << 2)
        self.assertEqual(Security.kSecCSDynamicInformation, 1 << 3)
        self.assertEqual(Security.kSecCSContentInformation, 1 << 4)
        self.assertEqual(Security.kSecCSSkipResourceDirectory, 1 << 5)
        self.assertEqual(Security.kSecCSCalculateCMSDigest, 1 << 6)

        self.assertIsInstance(Security.kSecCodeInfoCertificates, str)
        self.assertIsInstance(Security.kSecCodeInfoChangedFiles, str)
        self.assertIsInstance(Security.kSecCodeInfoCMS, str)
        self.assertIsInstance(Security.kSecCodeInfoDesignatedRequirement, str)
        self.assertIsInstance(Security.kSecCodeInfoEntitlements, str)
        self.assertIsInstance(Security.kSecCodeInfoEntitlementsDict, str)
        self.assertIsInstance(Security.kSecCodeInfoFlags, str)
        self.assertIsInstance(Security.kSecCodeInfoFormat, str)
        self.assertIsInstance(Security.kSecCodeInfoDigestAlgorithm, str)
        self.assertIsInstance(Security.kSecCodeInfoIdentifier, str)
        self.assertIsInstance(Security.kSecCodeInfoImplicitDesignatedRequirement, str)
        self.assertIsInstance(Security.kSecCodeInfoMainExecutable, str)
        self.assertIsInstance(Security.kSecCodeInfoPList, str)
        self.assertIsInstance(Security.kSecCodeInfoRequirements, str)
        self.assertIsInstance(Security.kSecCodeInfoRequirementData, str)
        self.assertIsInstance(Security.kSecCodeInfoSource, str)
        self.assertIsInstance(Security.kSecCodeInfoStatus, str)
        self.assertIsInstance(Security.kSecCodeInfoTeamIdentifier, str)
        self.assertIsInstance(Security.kSecCodeInfoTime, str)
        self.assertIsInstance(Security.kSecCodeInfoTimestamp, str)
        self.assertIsInstance(Security.kSecCodeInfoTrust, str)
        self.assertIsInstance(Security.kSecCodeInfoUnique, str)

    @expectedFailure
    def test_constants_missing(self):
        self.assertIsInstance(Security.kSecGuestAttributeArchitecture, str)
        self.assertIsInstance(Security.kSecGuestAttributeSubarchitecture, str)
        self.assertIsInstance(Security.kSecCodeInfoPlatformIdentifier, str)

    @min_os_level("10.11.4")
    def test_constants_10_11_4(self):
        self.assertIsInstance(Security.kSecCodeInfoDigestAlgorithms, str)
        self.assertIsInstance(Security.kSecCodeInfoCdHashes, str)

    @min_os_level("10.12")
    def test_constants_10_12(self):
        self.assertIsInstance(Security.kSecGuestAttributeAudit, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecCodeGetTypeID(), int)

        self.assertResultHasType(Security.SecCodeCopySelf, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopySelf, 0, objc._C_UINT)
        self.assertArgHasType(
            Security.SecCodeCopySelf, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecCodeCopySelf, 1)

        self.assertResultHasType(Security.SecCodeCopyStaticCode, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyStaticCode, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyStaticCode, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecCodeCopyStaticCode, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyStaticCode, 2)

        self.assertResultHasType(Security.SecCodeCopyHost, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyHost, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyHost, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecCodeCopyHost, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyHost, 2)

        self.assertResultHasType(Security.SecCodeCopyGuestWithAttributes, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyGuestWithAttributes, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyGuestWithAttributes, 1, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyGuestWithAttributes, 2, objc._C_UINT)
        self.assertArgHasType(
            Security.SecCodeCopyGuestWithAttributes,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyGuestWithAttributes, 3)

        self.assertResultHasType(Security.SecCodeCheckValidity, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCheckValidity, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCheckValidity, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCheckValidity, 2, objc._C_ID)

        self.assertResultHasType(Security.SecCodeCheckValidityWithErrors, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCheckValidityWithErrors, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCheckValidityWithErrors, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecCodeCheckValidityWithErrors, 2, objc._C_ID)
        self.assertArgHasType(
            Security.SecCodeCheckValidityWithErrors,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertResultHasType(Security.SecCodeCopyPath, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyPath, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopyPath, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecCodeCopyPath, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyPath, 2)

        self.assertResultHasType(Security.SecCodeCopyDesignatedRequirement, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopyDesignatedRequirement, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecCodeCopyDesignatedRequirement, 1, objc._C_UINT
        )
        self.assertArgHasType(
            Security.SecCodeCopyDesignatedRequirement,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyDesignatedRequirement, 2)

        self.assertResultHasType(Security.SecCodeCopySigningInformation, objc._C_INT)
        self.assertArgHasType(Security.SecCodeCopySigningInformation, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeCopySigningInformation, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecCodeCopySigningInformation,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecCodeCopySigningInformation, 2)

        self.assertResultHasType(Security.SecCodeMapMemory, objc._C_INT)
        self.assertArgHasType(Security.SecCodeMapMemory, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCodeMapMemory, 1, objc._C_UINT)

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertArgIsOut(Security.SecCodeCreateWithXPCMessage, 2)
        self.assertArgIsCFRetained(Security.SecCodeCreateWithXPCMessage, 2)
