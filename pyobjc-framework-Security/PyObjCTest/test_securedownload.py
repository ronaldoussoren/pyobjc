from PyObjCTools.TestSupport import *

import Security

SecureDownloadTrustSetupCallback = b'i@^v'
SecureDownloadTrustEvaluateCallback = b'i@i^v'

class TestSecureDownload (TestCase):

    def test_constants(self):
        self.assertEqual(Security.errSecureDownloadInvalidTicket, -20052)
        self.assertEqual(Security.errSecureDownloadInvalidDownload, -20053)

        self.assertEqual(Security.kSecureDownloadDoNotEvaluateSigner, 0)
        self.assertEqual(Security.kSecureDownloadEvaluateSigner, 1)
        self.assertEqual(Security.kSecureDownloadFailEvaluation, 2)

    def test_types(self):
        self.assertIsOpaquePointer(Security.SecureDownloadRef)

    def test_functions(self):
        self.assertResultHasType(Security.SecureDownloadCreateWithTicket, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadCreateWithTicket, 0, objc._C_ID)
        self.assertArgIsFunction(Security.SecureDownloadCreateWithTicket, 1, SecureDownloadTrustSetupCallback, 1)
        self.assertArgHasType(Security.SecureDownloadCreateWithTicket, 2, objc._C_PTR + objc._C_VOID)
        self.assertArgIsFunction(Security.SecureDownloadCreateWithTicket, 3, SecureDownloadTrustEvaluateCallback, 1)
        self.assertArgHasType(Security.SecureDownloadCreateWithTicket, 4, objc._C_PTR + objc._C_VOID)
        self.assertArgHasType(Security.SecureDownloadCreateWithTicket, 5, objc._C_OUT + objc._C_PTR + Security.SecureDownloadRef.__typestr__)

        self.assertResultHasType(Security.SecureDownloadCopyURLs, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadCopyURLs, 0, Security.SecureDownloadRef.__typestr__)
        self.assertArgHasType(Security.SecureDownloadCopyURLs, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecureDownloadCopyURLs, 1)

        self.assertResultHasType(Security.SecureDownloadCopyName, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadCopyName, 0, Security.SecureDownloadRef.__typestr__)
        self.assertArgHasType(Security.SecureDownloadCopyName, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecureDownloadCopyName, 1)

        self.assertResultHasType(Security.SecureDownloadCopyCreationDate, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadCopyCreationDate, 0, Security.SecureDownloadRef.__typestr__)
        self.assertArgHasType(Security.SecureDownloadCopyCreationDate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecureDownloadCopyCreationDate, 1)

        self.assertResultHasType(Security.SecureDownloadGetDownloadSize, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadGetDownloadSize, 0, Security.SecureDownloadRef.__typestr__)
        self.assertArgHasType(Security.SecureDownloadGetDownloadSize, 1, objc._C_OUT + objc._C_PTR + objc._C_LNGLNG)

        self.assertResultHasType(Security.SecureDownloadUpdateWithData, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadUpdateWithData, 0, Security.SecureDownloadRef.__typestr__)
        self.assertArgHasType(Security.SecureDownloadUpdateWithData, 1, objc._C_ID)

        self.assertResultHasType(Security.SecureDownloadFinished, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadFinished, 0, Security.SecureDownloadRef.__typestr__)

        self.assertResultHasType(Security.SecureDownloadRelease, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadRelease, 0, Security.SecureDownloadRef.__typestr__)

        self.assertResultHasType(Security.SecureDownloadCopyTicketLocation, objc._C_INT)
        self.assertArgHasType(Security.SecureDownloadCopyTicketLocation, 0, Security.SecureDownloadRef.__typestr__)
        self.assertArgHasType(Security.SecureDownloadCopyTicketLocation, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecureDownloadCopyTicketLocation, 1)



if __name__ == "__main__":
    main()
