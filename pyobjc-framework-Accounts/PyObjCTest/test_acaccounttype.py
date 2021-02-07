from PyObjCTools.TestSupport import TestCase, min_os_level
import Accounts


class TestACAccountType(TestCase):
    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Accounts.ACAccountTypeIdentifierLinkedIn, str)
        self.assertIsInstance(Accounts.ACAccountTypeIdentifierTencentWeibo, str)
        self.assertIsInstance(Accounts.ACLinkedInAppIdKey, str)
        self.assertIsInstance(Accounts.ACLinkedInPermissionsKey, str)
        self.assertIsInstance(Accounts.ACTencentWeiboAppIdKey, str)

    @min_os_level("10.8")
    def testConstants(self):
        self.assertIsInstance(Accounts.ACAccountTypeIdentifierTwitter, str)
        self.assertIsInstance(Accounts.ACAccountTypeIdentifierSinaWeibo, str)
        self.assertIsInstance(Accounts.ACFacebookAppIdKey, str)
        self.assertIsInstance(Accounts.ACFacebookPermissionsKey, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceKey, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceEveryone, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceFriends, str)
        self.assertIsInstance(Accounts.ACFacebookAudienceOnlyMe, str)

    @min_os_level("10.8")
    def testMethods(self):
        self.assertResultIsBOOL(Accounts.ACAccountType.accessGranted)
