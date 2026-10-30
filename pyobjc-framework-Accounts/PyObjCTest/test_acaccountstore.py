from PyObjCTools.TestSupport import TestCase
import Accounts
import objc

ACAccountStoreSaveCompletionHandler = b"vZ@"
ACAccountStoreRemoveCompletionHandler = b"vZ@"
ACAccountStoreRequestAccessCompletionHandler = b"vZ@"
ACAccountStoreCredentialRenewalHandler = b"v" + objc._C_NSInteger + b"@"


class TestACAccountStore(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Accounts.ACAccountCredentialRenewResult)
        self.assertEqual(Accounts.ACAccountCredentialRenewResultRenewed, 0)
        self.assertEqual(Accounts.ACAccountCredentialRenewResultRejected, 1)
        self.assertEqual(Accounts.ACAccountCredentialRenewResultFailed, 2)

    def test_constants(self):
        self.assertHasAttr(Accounts, "ACAccountStoreDidChangeNotification")
        self.assertIsInstance(Accounts.ACAccountStoreDidChangeNotification, str)

    def test_methods(self):
        self.assertArgIsBlock(
            Accounts.ACAccountStore.saveAccount_withCompletionHandler_,
            1,
            ACAccountStoreSaveCompletionHandler,
        )
        self.assertArgIsBlock(
            Accounts.ACAccountStore.requestAccessToAccountsWithType_options_completion_,
            2,
            ACAccountStoreRequestAccessCompletionHandler,
        )
        self.assertArgIsBlock(
            Accounts.ACAccountStore.renewCredentialsForAccount_completion_,
            1,
            ACAccountStoreCredentialRenewalHandler,
        )
        self.assertArgIsBlock(
            Accounts.ACAccountStore.removeAccount_withCompletionHandler_,
            1,
            ACAccountStoreRemoveCompletionHandler,
        )
