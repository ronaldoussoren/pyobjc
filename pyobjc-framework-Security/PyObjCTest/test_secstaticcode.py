from PyObjCTools.TestSupport import *

import Security

class TestSecStaticCode (TestCase):

    def test_constants(self):
        self.assertIsInstance(Security.kSecCodeAttributeArchitecture, unicode)
        self.assertIsInstance(Security.kSecCodeAttributeSubarchitecture, unicode)
        self.assertIsInstance(Security.kSecCodeAttributeUniversalFileOffset, unicode)
        self.assertIsInstance(Security.kSecCodeAttributeBundleVersion, unicode)

        self.assertEqual(Security.kSecCSCheckAllArchitectures, 1 << 0)
        self.assertEqual(Security.kSecCSDoNotValidateExecutable, 1 << 1)
        self.assertEqual(Security.kSecCSDoNotValidateResources, 1 << 2)
        self.assertEqual(Security.kSecCSBasicValidateOnly, Security.kSecCSDoNotValidateExecutable | Security.kSecCSDoNotValidateResources)
        self.assertEqual(Security.kSecCSCheckNestedCode, 1 << 3)
        self.assertEqual(Security.kSecCSStrictValidate, 1 << 4)
        self.assertEqual(Security.kSecCSFullReport, 1 << 5)
        self.assertEqual(Security.kSecCSCheckGatekeeperArchitectures, (1 << 6) | Security.kSecCSCheckAllArchitectures)
        self.assertEqual(Security.kSecCSRestrictSymlinks, 1 << 7)
        self.assertEqual(Security.kSecCSRestrictToAppLike, 1 << 8)
        self.assertEqual(Security.kSecCSRestrictSidebandData, 1 << 9)
        self.assertEqual(Security.kSecCSUseSoftwareSigningCert, 1 << 10)
        self.assertEqual(Security.kSecCSValidatePEH, 1 << 11)


    def test_functions(self):
        self.assertIsInstance(Security.SecStaticCodeGetTypeID(), (int, long))

        self.assertResultHasType(Security.SecStaticCodeCreateWithPath, objc._C_INT)
        self.assertArgHasType(Security.SecStaticCodeCreateWithPath, 0, objc._C_ID)
        self.assertArgHasType(Security.SecStaticCodeCreateWithPath, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecStaticCodeCreateWithPath, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecStaticCodeCreateWithPath, 2)

        self.assertResultHasType(Security.SecStaticCodeCreateWithPathAndAttributes, objc._C_INT)
        self.assertArgHasType(Security.SecStaticCodeCreateWithPathAndAttributes, 0, objc._C_ID)
        self.assertArgHasType(Security.SecStaticCodeCreateWithPathAndAttributes, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecStaticCodeCreateWithPathAndAttributes, 2, objc._C_ID)
        self.assertArgHasType(Security.SecStaticCodeCreateWithPathAndAttributes, 3, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecStaticCodeCreateWithPathAndAttributes, 3)


        self.assertResultHasType(Security.SecStaticCodeCheckValidity, objc._C_INT)
        self.assertArgHasType(Security.SecStaticCodeCheckValidity, 0, objc._C_ID)
        self.assertArgHasType(Security.SecStaticCodeCheckValidity, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecStaticCodeCheckValidity, 2, objc._C_ID)

        self.assertResultHasType(Security.SecStaticCodeCheckValidityWithErrors, objc._C_INT)
        self.assertArgHasType(Security.SecStaticCodeCheckValidityWithErrors, 0, objc._C_ID)
        self.assertArgHasType(Security.SecStaticCodeCheckValidityWithErrors, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecStaticCodeCheckValidityWithErrors, 2, objc._C_ID)
        self.assertArgHasType(Security.SecStaticCodeCheckValidityWithErrors, 3, objc._C_OUT + objc._C_PTR + objc._C_ID)


if __name__ == "__main__":
    main()
