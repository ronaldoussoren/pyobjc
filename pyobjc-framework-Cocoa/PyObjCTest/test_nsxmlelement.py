import Foundation
from PyObjCTools.TestSupport import TestCase


class TestXMLElement(TestCase):
    def test_output(self):
        self.assertArgIsOut(Foundation.NSXMLElement.initWithXMLString_error_, 1)
        self.assertArgIsBOOL(
            Foundation.NSXMLElement.normalizeAdjacentTextNodesPreservingCDATA_, 0
        )
