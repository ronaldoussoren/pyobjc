
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStatusItem (TestCase):
    def testMethods(self):
        m = NSStatusItem.setAction_.__metadata__()
        self.failUnlessEqual(m['arguments'][2]['sel_of_type'], 'v@:@')

        m = NSStatusItem.setDoubleAction_.__metadata__()
        self.failUnlessEqual(m['arguments'][2]['sel_of_type'], 'v@:@')

        self.failUnlessResultIsBOOL(NSStatusItem.isEnabled)
        self.failUnlessArgIsBOOL(NSStatusItem.setEnabled_, 0)
        self.failUnlessResultIsBOOL(NSStatusItem.highlightMode)
        self.failUnlessArgIsBOOL(NSStatusItem.setHighlightMode_, 0)
        self.failUnlessArgIsBOOL(NSStatusItem.drawStatusBarBackgroundInRect_withHighlight_, 1)

if __name__ == "__main__":
    main()
