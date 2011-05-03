
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMovie (TestCase):

    @onlyOn32Bit
    def testMethods(self):
        self.assertArgIsBOOL(NSMovie.initWithURL_byReference_, 1)
        self.assertResultIsBOOL(NSMovie.canInitWithPasteboard_)

if __name__ == "__main__":
    main()
