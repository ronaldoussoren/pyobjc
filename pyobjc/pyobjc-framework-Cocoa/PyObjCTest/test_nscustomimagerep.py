from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCustomImageRep (TestCase):
    def testMethods(self):
        self.assertArgIsSEL(NSCustomImageRep.initWithDrawSelector_delegate_, 0,
                'v@:@')

if __name__ == "__main__":
    main()
