from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLElement (TestCase):
    def testOutputArgs(self):
        self.assertArgIsOut(NSXMLElement.initWithXMLString_error_, 1)
        self.assertArgIsBOOL(NSXMLElement.normalizeAdjacentTextNodesPreservingCDATA_, 0)

if __name__ == "__main__":
    main()
