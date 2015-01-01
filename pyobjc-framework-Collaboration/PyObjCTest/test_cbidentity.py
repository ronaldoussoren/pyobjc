
from PyObjCTools.TestSupport import *
from Collaboration import *

class TestCBIdentity (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CBIdentity.isHidden)
        self.assertResultIsBOOL(CBIdentity.isMemberOfGroup_)
        self.assertResultIsBOOL(CBUserIdentity.isEnabled)
        self.assertResultIsBOOL(CBUserIdentity.authenticateWithPassword_)


if __name__ == "__main__":
    main()
