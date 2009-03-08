
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSNib (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSNibOwner, unicode)
        self.failUnlessIsInstance(NSNibTopLevelObjects, unicode)

    def testMethods(self):
        m = NSNib.instantiateNibWithOwner_topLevelObjects_.__metadata__()
        self.failUnlessEqual(m['arguments'][3]['type'], 'o^@')


if __name__ == "__main__":
    main()
