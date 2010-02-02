
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSNib (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSNibOwner, unicode)
        self.assertIsInstance(NSNibTopLevelObjects, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSNib.instantiateNibWithOwner_topLevelObjects_)
        self.assertArgIsOut(NSNib.instantiateNibWithOwner_topLevelObjects_, 1)


if __name__ == "__main__":
    main()
