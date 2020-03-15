import Foundation
from PyObjCTools.TestSupport import TestCase


class TestXMLDTD(TestCase):
    def testOutputArgs(self):
        self.assertArgIsOut(Foundation.NSXMLDTD.initWithContentsOfURL_options_error_, 2)
        self.assertArgIsOut(Foundation.NSXMLDTD.initWithData_options_error_, 2)
