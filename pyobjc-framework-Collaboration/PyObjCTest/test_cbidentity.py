
from PyObjCTools.TestSupport import *
from Collaboration import *

class TestCBIdentity (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CBIdentity.isHidden)
        self.assertResultIsBOOL(CBIdentity.isMemberOfGroup_)


if __name__ == "__main__":
    main()
