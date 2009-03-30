from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLDocument (TestCase):
    def testConstants(self):
        self.assertEquals(NSXMLDocumentXMLKind, 0)
        self.assertEquals(NSXMLDocumentXHTMLKind, 1)
        self.assertEquals(NSXMLDocumentHTMLKind, 2)
        self.assertEquals(NSXMLDocumentTextKind, 3)

    def testOutputArgs(self):
        self.failUnlessArgIsOut(NSXMLDocument.initWithXMLString_options_error_, 2)
        self.failUnlessArgIsOut(NSXMLDocument.initWithContentsOfURL_options_error_, 2)
        self.failUnlessArgIsOut(NSXMLDocument.initWithData_options_error_, 2)
        self.failUnlessArgIsOut(NSXMLDocument.objectByApplyingXSLT_arguments_error_, 2)
        self.failUnlessArgIsOut(NSXMLDocument.objectByApplyingXSLTString_arguments_error_, 2)
        self.failUnlessArgIsOut(NSXMLDocument.objectByApplyingXSLTAtURL_arguments_error_, 2)
        self.failUnlessArgIsOut(NSXMLDocument.validateAndReturnError_, 0)

        self.failUnlessResultIsBOOL(NSXMLDocument.isStandalone)
        self.failUnlessArgIsBOOL(NSXMLDocument.setStandalone_, 0)
        self.failUnlessResultIsBOOL(NSXMLDocument.validateAndReturnError_)

if __name__ == "__main__":
    main()
