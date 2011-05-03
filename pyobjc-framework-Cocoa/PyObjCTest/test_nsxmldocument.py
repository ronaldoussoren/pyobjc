from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLDocument (TestCase):
    def testConstants(self):
        self.assertEqual(NSXMLDocumentXMLKind, 0)
        self.assertEqual(NSXMLDocumentXHTMLKind, 1)
        self.assertEqual(NSXMLDocumentHTMLKind, 2)
        self.assertEqual(NSXMLDocumentTextKind, 3)

    def testOutputArgs(self):
        self.assertArgIsOut(NSXMLDocument.initWithXMLString_options_error_, 2)
        self.assertArgIsOut(NSXMLDocument.initWithContentsOfURL_options_error_, 2)
        self.assertArgIsOut(NSXMLDocument.initWithData_options_error_, 2)
        self.assertArgIsOut(NSXMLDocument.objectByApplyingXSLT_arguments_error_, 2)
        self.assertArgIsOut(NSXMLDocument.objectByApplyingXSLTString_arguments_error_, 2)
        self.assertArgIsOut(NSXMLDocument.objectByApplyingXSLTAtURL_arguments_error_, 2)
        self.assertArgIsOut(NSXMLDocument.validateAndReturnError_, 0)

        self.assertResultIsBOOL(NSXMLDocument.isStandalone)
        self.assertArgIsBOOL(NSXMLDocument.setStandalone_, 0)
        self.assertResultIsBOOL(NSXMLDocument.validateAndReturnError_)

if __name__ == "__main__":
    main()
