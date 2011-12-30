from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSCachedImageRep (TestCase):
    def testMethods(self):
        self.asertArgIsBOOL(NSCachedImageRep.initWithSize_depth_separate_alpha_, 2)
        self.asertArgIsBOOL(NSCachedImageRep.initWithSize_depth_separate_alpha_, 3)


if __name__ == "__main__":
    main()
