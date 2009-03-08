
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStatusItem (TestCase):
    def testMethods(self):
        m = NSStatusItem.setAction_.__metadata__()
        self.failUnlessEqual(m['arguments'][2]['sel_of_type'], 'v@:@')

        m = NSStatusItem.setDoubleAction_.__metadata__()
        self.failUnlessEqual(m['arguments'][2]['sel_of_type'], 'v@:@')

if __name__ == "__main__":
    main()
