
from PyObjCTools.TestSupport import *
from Collaboration import *

class TestCBIdentity (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(CBIdentity.isHidden)
        self.failUnlessResultIsBOOL(CBIdentity.isMemberOfGroup_)


if __name__ == "__main__":
    main()
