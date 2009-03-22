from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPathCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSPathStyleStandard, 0)
        self.failUnlessEqual(NSPathStyleNavigationBar, 1)
        self.failUnlessEqual(NSPathStylePopUp, 2)

    def testMethods(self):
        m = NSPathCell.setDoubleAction_.__metadata__()
        self.failUnlessEqual(m['arguments'][2]['sel_of_type'], 'v@:@')


if __name__ == "__main__":
    main()
