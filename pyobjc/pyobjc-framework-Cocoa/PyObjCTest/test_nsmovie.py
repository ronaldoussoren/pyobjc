
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMovie (TestCase):

    @onlyOn32Bit
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSMovie.initWithURL_byReference_, 1)
        self.failUnlessResultIsBOOL(NSMovie.canInitWithPasteboard_)

if __name__ == "__main__":
    main()
