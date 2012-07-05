import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2**32:
    from PyObjCTools.TestSupport import *
    import Accounts

    class TestACAccountType (TestCase):
        @min_os_level("10.8")
        def testConstants(self):
            self.assertIsInstance(Accounts.ACAccountTypeIdentifierTwitter, unicode)
            self.assertIsInstance(Accounts.ACAccountTypeIdentifierSinaWeibo, unicode)

        @min_os_level("10.8")
        def testMethods(self):
            self.assertResultIsBOOL(Accounts.ACAccountType.accessGranted)

    if __name__ == "__main__":
        main()
