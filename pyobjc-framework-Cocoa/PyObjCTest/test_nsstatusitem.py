
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStatusItem (TestCase):
    def testConstants(self):
        self.assertEqual(NSStatusItemBehaviorRemovalAllowed, 1 << 1)
        self.assertEqual(NSStatusItemBehaviorTerminationOnRemoval, 1 << 2)

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

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSStatusItem.isVisible)
        self.assertArgIsBOOL(NSStatusItem.setVisible_, 0)

if __name__ == "__main__":
    main()
