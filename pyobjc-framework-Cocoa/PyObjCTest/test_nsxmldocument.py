import Foundation
from PyObjCTools.TestSupport import TestCase


class TestXMLDocument(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSXMLDocumentXMLKind, 0)
        self.assertEqual(Foundation.NSXMLDocumentXHTMLKind, 1)
        self.assertEqual(Foundation.NSXMLDocumentHTMLKind, 2)
        self.assertEqual(Foundation.NSXMLDocumentTextKind, 3)

    def testOutputArgs(self):
        self.assertArgIsOut(
            Foundation.NSXMLDocument.initWithXMLString_options_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSXMLDocument.initWithContentsOfURL_options_error_, 2
        )
        self.assertArgIsOut(Foundation.NSXMLDocument.initWithData_options_error_, 2)
        self.assertArgIsOut(
            Foundation.NSXMLDocument.objectByApplyingXSLT_arguments_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSXMLDocument.objectByApplyingXSLTString_arguments_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSXMLDocument.objectByApplyingXSLTAtURL_arguments_error_, 2
        )
        self.assertArgIsOut(Foundation.NSXMLDocument.validateAndReturnError_, 0)

        self.assertResultIsBOOL(Foundation.NSXMLDocument.isStandalone)
        self.assertArgIsBOOL(Foundation.NSXMLDocument.setStandalone_, 0)
        self.assertResultIsBOOL(Foundation.NSXMLDocument.validateAndReturnError_)
