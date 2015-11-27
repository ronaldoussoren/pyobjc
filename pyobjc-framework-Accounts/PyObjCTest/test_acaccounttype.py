import sys

if sys.maxsize > 2**32:
    from PyObjCTools.TestSupport import *
    import Accounts

    class TestACAccountType (TestCase):
        @min_os_level("10.9")
        def testConstants10_9(self):
            self.assertIsInstance(Accounts.ACAccountTypeIdentifierLinkedIn, unicode)
            self.assertIsInstance(Accounts.ACAccountTypeIdentifierTencentWeibo, unicode)
            self.assertIsInstance(Accounts.ACLinkedInAppIdKey, unicode)
            self.assertIsInstance(Accounts.ACLinkedInPermissionsKey, unicode)
            self.assertIsInstance(Accounts.ACTencentWeiboAppIdKey, unicode)

        @min_os_level("10.8")
        def testConstants(self):
            self.assertIsInstance(Accounts.ACAccountTypeIdentifierTwitter, unicode)
            self.assertIsInstance(Accounts.ACAccountTypeIdentifierSinaWeibo, unicode)
            self.assertIsInstance(Accounts.ACFacebookAppIdKey, unicode)
            self.assertIsInstance(Accounts.ACFacebookPermissionsKey, unicode)
            self.assertIsInstance(Accounts.ACFacebookAudienceKey, unicode)
            self.assertIsInstance(Accounts.ACFacebookAudienceEveryone, unicode)
            self.assertIsInstance(Accounts.ACFacebookAudienceFriends, unicode)
            self.assertIsInstance(Accounts.ACFacebookAudienceOnlyMe, unicode)

        @min_os_level("10.8")
        def testMethods(self):
            self.assertResultIsBOOL(Accounts.ACAccountType.accessGranted)

    if __name__ == "__main__":
        main()
