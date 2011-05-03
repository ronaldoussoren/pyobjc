
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStatusItem (TestCase):
    def testMethods(self):
        m = NSStatusItem.setAction_.__metadata__()
        self.assertEqual(m['arguments'][2]['sel_of_type'], b'v@:@')

        m = NSStatusItem.setDoubleAction_.__metadata__()
        self.assertEqual(m['arguments'][2]['sel_of_type'], b'v@:@')

        self.assertResultIsBOOL(NSStatusItem.isEnabled)
        self.assertArgIsBOOL(NSStatusItem.setEnabled_, 0)
        self.assertResultIsBOOL(NSStatusItem.highlightMode)
        self.assertArgIsBOOL(NSStatusItem.setHighlightMode_, 0)
        self.assertArgIsBOOL(NSStatusItem.drawStatusBarBackgroundInRect_withHighlight_, 1)

if __name__ == "__main__":
    main()
