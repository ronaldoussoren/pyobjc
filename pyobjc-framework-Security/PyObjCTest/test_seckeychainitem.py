from PyObjCTools.TestSupport import *

import Security

class TestKeychainitem (TestCase):

    def test_constants(self):
        self.assertEqual(Security.kSecInternetPasswordItemClass, fourcc(b'inet'))
        self.assertEqual(Security.kSecGenericPasswordItemClass, fourcc(b'genp'))
        self.assertEqual(Security.kSecAppleSharePasswordItemClass, fourcc(b'ashp'))
        self.assertEqual(Security.kSecCertificateItemClass, 0x80001000)
        self.assertEqual(Security.kSecPublicKeyItemClass, 0x0000000F)
        self.assertEqual(Security.kSecPrivateKeyItemClass, 0x00000010)
        self.assertEqual(Security.kSecSymmetricKeyItemClass, 0x00000011)

        self.assertEqual(Security.kSecCreationDateItemAttr, fourcc(b'cdat'))
        self.assertEqual(Security.kSecModDateItemAttr, fourcc(b'mdat'))
        self.assertEqual(Security.kSecDescriptionItemAttr, fourcc(b'desc'))
        self.assertEqual(Security.kSecCommentItemAttr, fourcc(b'icmt'))
        self.assertEqual(Security.kSecCreatorItemAttr, fourcc(b'crtr'))
        self.assertEqual(Security.kSecTypeItemAttr, fourcc(b'type'))
        self.assertEqual(Security.kSecScriptCodeItemAttr, fourcc(b'scrp'))
        self.assertEqual(Security.kSecLabelItemAttr, fourcc(b'labl'))
        self.assertEqual(Security.kSecInvisibleItemAttr, fourcc(b'invi'))
        self.assertEqual(Security.kSecNegativeItemAttr, fourcc(b'nega'))
        self.assertEqual(Security.kSecCustomIconItemAttr, fourcc(b'cusi'))
        self.assertEqual(Security.kSecAccountItemAttr, fourcc(b'acct'))
        self.assertEqual(Security.kSecServiceItemAttr, fourcc(b'svce'))
        self.assertEqual(Security.kSecGenericItemAttr, fourcc(b'gena'))
        self.assertEqual(Security.kSecSecurityDomainItemAttr, fourcc(b'sdmn'))
        self.assertEqual(Security.kSecServerItemAttr, fourcc(b'srvr'))
        self.assertEqual(Security.kSecAuthenticationTypeItemAttr, fourcc(b'atyp'))
        self.assertEqual(Security.kSecPortItemAttr, fourcc(b'port'))
        self.assertEqual(Security.kSecPathItemAttr, fourcc(b'path'))
        self.assertEqual(Security.kSecVolumeItemAttr, fourcc(b'vlme'))
        self.assertEqual(Security.kSecAddressItemAttr, fourcc(b'addr'))
        self.assertEqual(Security.kSecSignatureItemAttr, fourcc(b'ssig'))
        self.assertEqual(Security.kSecProtocolItemAttr, fourcc(b'ptcl'))
        self.assertEqual(Security.kSecCertificateType, fourcc(b'ctyp'))
        self.assertEqual(Security.kSecCertificateEncoding, fourcc(b'cenc'))
        self.assertEqual(Security.kSecCrlType, fourcc(b'crtp'))
        self.assertEqual(Security.kSecCrlEncoding, fourcc(b'crnc'))
        self.assertEqual(Security.kSecAlias, fourcc(b'alis'))

    def test_functions(self):
        self.assertIsInstance(Security.SecKeychainItemGetTypeID(), (int, long))

        self.fail("SecKeychainItemModifyAttributesAndData: SecKeychainAttributeList requires manual work")

if __name__ == "__main__":
    main()
