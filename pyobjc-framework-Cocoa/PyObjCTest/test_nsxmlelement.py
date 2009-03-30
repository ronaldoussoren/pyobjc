from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLElement (TestCase):
    def testOutputArgs(self):
        self.failUnlessArgIsOut(NSXMLElement.initWithXMLString_error_, 1)
        self.failUnlessArgIsBOOL(NSXMLElement.normalizeAdjacentTextNodesPreservingCDATA_, 0)

if __name__ == "__main__":
    main()
