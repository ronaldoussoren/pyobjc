
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSNib (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSNibOwner, unicode)
        self.failUnlessIsInstance(NSNibTopLevelObjects, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSNib.instantiateNibWithOwner_topLevelObjects_)
        self.failUnlessArgIsOut(NSNib.instantiateNibWithOwner_topLevelObjects_, 1)


if __name__ == "__main__":
    main()
