import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import Accounts

    ACAccountStoreSaveCompletionHandler = b'vZ@'
    ACAccountStoreRemoveCompletionHandler = b'vZ@'
    ACAccountStoreRequestAccessCompletionHandler = b'vZ@'
    ACAccountStoreCredentialRenewalHandler = b'v' + objc._C_NSInteger + b'@'

    class TestACAccountStore (TestCase):
        @min_os_level("10.8")
        def testConstants(self):
            self.assertHasAttr(Accounts, "ACAccountStoreDidChangeNotification")
            self.assertIsInstance(Accounts.ACAccountStoreDidChangeNotification, unicode)

        def testMethods(self):
            self.assertArgIsBlock(Accounts.ACAccountStore.saveAccount_withCompletionHandler_, 1, ACAccountStoreSaveCompletionHandler)
            self.assertArgIsBlock(Accounts.ACAccountStore.requestAccessToAccountsWithType_withCompletionHandler_, 1, ACAccountStoreRequestAccessCompletionHandler)
            self.assertArgIsBlock(Accounts.ACAccountStore.requestAccessToAccountsWithType_options_completion_, 2, ACAccountStoreRequestAccessCompletionHandler)
            self.assertArgIsBlock(Accounts.ACAccountStore.renewCredentialsForAccount_completion_, 1, ACAccountStoreCredentialRenewalHandler)
            self.assertArgIsBlock(Accounts.ACAccountStore.removeAccount_withCompletionHandler_, 1, ACAccountStoreRemoveCompletionHandler)

if __name__ == "__main__":
    main()
