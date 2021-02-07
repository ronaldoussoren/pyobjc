import Security
from PyObjCTools.TestSupport import TestCase


class Testoidscrl(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "INTEL_X509V2_CRL_R08"))
        self.assertFalse(hasattr(Security, "INTEL_X509V2_CRL_R08_LENGTH"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLSignedCrlStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLSignedCrlCStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLTbsCertListStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLTbsCertListCStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLVersion"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLIssuerStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLIssuerNameCStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLIssuerNameLDAP"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLThisUpdate"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLNextUpdate"))
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V1CRLRevokedCertificatesStruct")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V1CRLRevokedCertificatesCStruct")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V1CRLNumberOfRevokedCertEntries")
        )
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLRevokedEntryStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLRevokedEntryCStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V1CRLRevokedEntrySerialNumber"))
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V1CRLRevokedEntryRevocationDate")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntryAllExtensionsStruct")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntryAllExtensionsCStruct")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntryNumberOfExtensions")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntrySingleExtensionStruct")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntrySingleExtensionCStruct")
        )
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLRevokedEntryExtensionId"))
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntryExtensionCritical")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntryExtensionType")
        )
        self.assertFalse(
            hasattr(Security, "CSSMOID_X509V2CRLRevokedEntryExtensionValue")
        )
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLAllExtensionsStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLAllExtensionsCStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLNumberOfExtensions"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLSingleExtensionStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLSingleExtensionCStruct"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLExtensionId"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLExtensionCritical"))
        self.assertFalse(hasattr(Security, "CSSMOID_X509V2CRLExtensionType"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP_BASIC"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP_NONCE"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP_CRL"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP_RESPONSE"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP_NOCHECK"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP_ARCHIVE_CUTOFF"))
        self.assertFalse(hasattr(Security, "CSSMOID_PKIX_OCSP_SERVICE_LOCATOR"))
