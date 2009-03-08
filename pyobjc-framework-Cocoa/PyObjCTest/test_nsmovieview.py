
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMovieView (TestCase):
    @onlyOn32Bit
    def testConstants(self):
        self.failUnlessEqual(NSQTMovieNormalPlayback, 0)
        self.failUnlessEqual(NSQTMovieLoopingPlayback, 1)
        self.failUnlessEqual(NSQTMovieLoopingBackAndForthPlayback, 2)

    @onlyOn32Bit
    def testMethods(self):
        self.fail("- (void* /*MovieController*/) movieController;")




if __name__ == "__main__":
    main()
