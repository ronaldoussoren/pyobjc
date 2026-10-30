import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestSecCode(TestCase):
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

    @min_os_level("10.13")
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

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(
            Security.kSecCodeInfoDefaultDesignatedLightweightCodeRequirement, str
        )

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(Security.kSecCodeInfoStapledNotarizationTicket, str)

    @min_os_level("27.0")
    def test_constants27_0(self):
        self.assertIsInstance(Security.kSecCodeInfoTotalSignatures, str)
        self.assertIsInstance(Security.kSecCodeInfoChosenSignature, str)
        self.assertIsInstance(Security.kSecCodeInfoSignerInfoSKID, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecCodeGetTypeID(), int)

        self.assertArgIsOut(Security.SecCodeCopySelf, 1)
        self.assertArgIsCFRetained(Security.SecCodeCopySelf, 1)

        self.assertArgIsOut(Security.SecCodeCopyStaticCode, 2)
        self.assertArgIsCFRetained(Security.SecCodeCopyStaticCode, 2)

        self.assertArgIsOut(Security.SecCodeCopyHost, 2)
        self.assertArgIsCFRetained(Security.SecCodeCopyHost, 2)

        self.assertArgIsOut(
            Security.SecCodeCopyGuestWithAttributes,
            3,
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyGuestWithAttributes, 3)

        Security.SecCodeCheckValidity

        Security.SecCodeCheckValidityWithErrors
        self.assertArgIsOut(
            Security.SecCodeCheckValidityWithErrors,
            3,
        )

        self.assertArgIsOut(
            Security.SecCodeCopyPath, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyPath, 2)

        self.assertArgIsOut(
            Security.SecCodeCopyDesignatedRequirement,
            2,
        )
        self.assertArgIsCFRetained(Security.SecCodeCopyDesignatedRequirement, 2)

        self.assertArgIsOut(
            Security.SecCodeCopySigningInformation,
            2,
        )
        self.assertArgIsCFRetained(Security.SecCodeCopySigningInformation, 2)

        Security.SecCodeMapMemory

    @min_os_level("10.13")
    def test_functions10_13(self):
        Security.SecCodeValidateFileResource

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertArgIsOut(Security.SecCodeCreateWithXPCMessage, 2)
        self.assertArgIsCFRetained(Security.SecCodeCreateWithXPCMessage, 2)
