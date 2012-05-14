from PyObjCTools.TestSupport import *
import Accounts

class TestACAccountStore (TestCase):
    @min_os_level("10.8")
    def testConstants(self):
        self.assertHasAttr(Accounts, "ACAccountStoreDidChangeNotification")
        self.assertIsInstance(Accounts.ACAccountStoreDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
