from PyObjCTools.TestSupport import TestCase
import Accounts


class TestACAccountType(TestCase):
    def test_constants(self):
        self.assertIsInstance(Accounts.ACAccountTypeIdentifierLinkedIn, str)
        self.assertIsInstance(Accounts.ACAccountTypeIdentifierTencentWeibo, str)
        self.assertIsInstance(Accounts.ACLinkedInAppIdKey, str)
        self.assertIsInstance(Accounts.ACLinkedInPermissionsKey, str)
        self.assertIsInstance(Accounts.ACTencentWeiboAppIdKey, str)

        self.assertIsInstance(Accounts.ACAccountTypeIdentifierTwitter, str)
        self.assertIsInstance(Accounts.ACAccountTypeIdentifierSinaWeibo, str)
        self.assertIsInstance(Accounts.ACFacebookAppIdKey, str)
        self.assertIsInstance(Accounts.ACFacebookPermissionsKey, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceKey, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceEveryone, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceFriends, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceOnlyMe, str)

    def test_methods(self):
        self.assertResultIsBOOL(Accounts.ACAccountType.accessGranted)
