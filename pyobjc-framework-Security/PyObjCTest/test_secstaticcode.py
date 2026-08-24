import Security
from PyObjCTools.TestSupport import TestCase


class TestSecStaticCode(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecCodeAttributeArchitecture, str)
        self.assertIsInstance(Security.kSecCodeAttributeSubarchitecture, str)
        self.assertIsInstance(Security.kSecCodeAttributeUniversalFileOffset, str)
        self.assertIsInstance(Security.kSecCodeAttributeBundleVersion, str)

        self.assertEqual(Security.kSecCSCheckAllArchitectures, 1 << 0)
        self.assertEqual(Security.kSecCSDoNotValidateExecutable, 1 << 1)
        self.assertEqual(Security.kSecCSDoNotValidateResources, 1 << 2)
        self.assertEqual(
            Security.kSecCSBasicValidateOnly,
            Security.kSecCSDoNotValidateExecutable
            | Security.kSecCSDoNotValidateResources,
        )
        self.assertEqual(Security.kSecCSCheckNestedCode, 1 << 3)
        self.assertEqual(Security.kSecCSStrictValidate, 1 << 4)
        self.assertEqual(Security.kSecCSFullReport, 1 << 5)
        self.assertEqual(
            Security.kSecCSCheckGatekeeperArchitectures,
            (1 << 6) | Security.kSecCSCheckAllArchitectures,
        )
        self.assertEqual(Security.kSecCSRestrictSymlinks, 1 << 7)
        self.assertEqual(Security.kSecCSRestrictToAppLike, 1 << 8)
        self.assertEqual(Security.kSecCSRestrictSidebandData, 1 << 9)
        self.assertEqual(Security.kSecCSUseSoftwareSigningCert, 1 << 10)
        self.assertEqual(Security.kSecCSValidatePEH, 1 << 11)
        self.assertEqual(Security.kSecCSSingleThreaded, 1 << 12)
        self.assertEqual(Security.kSecCSAllowNetworkAccess, 1 << 16)
        self.assertEqual(Security.kSecCSFastExecutableValidation, 1 << 17)

    def test_functions(self):
        self.assertIsInstance(Security.SecStaticCodeGetTypeID(), int)

        self.assertArgIsOut(
            Security.SecStaticCodeCreateWithPath,
            2,
        )
        self.assertArgIsCFRetained(Security.SecStaticCodeCreateWithPath, 2)

        self.assertArgIsOut(
            Security.SecStaticCodeCreateWithPathAndAttributes,
            3,
        )
        self.assertArgIsCFRetained(Security.SecStaticCodeCreateWithPathAndAttributes, 3)

        Security.SecStaticCodeCheckValidity

        self.assertArgIsOut(
            Security.SecStaticCodeCheckValidityWithErrors,
            3,
        )
        self.assertArgIsCFRetained(
            Security.SecStaticCodeCheckValidityWithErrors,
            3,
        )
