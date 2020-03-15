import Foundation
from PyObjCTools.TestSupport import TestCase


class TestXMLNode(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSXMLInvalidKind, 0)
        self.assertEqual(Foundation.NSXMLDocumentKind, 1)
        self.assertEqual(Foundation.NSXMLElementKind, 2)
        self.assertEqual(Foundation.NSXMLAttributeKind, 3)
        self.assertEqual(Foundation.NSXMLNamespaceKind, 4)
        self.assertEqual(Foundation.NSXMLProcessingInstructionKind, 5)
        self.assertEqual(Foundation.NSXMLCommentKind, 6)
        self.assertEqual(Foundation.NSXMLTextKind, 7)
        self.assertEqual(Foundation.NSXMLDTDKind, 8)
        self.assertEqual(Foundation.NSXMLEntityDeclarationKind, 9)
        self.assertEqual(Foundation.NSXMLAttributeDeclarationKind, 10)
        self.assertEqual(Foundation.NSXMLElementDeclarationKind, 11)
        self.assertEqual(Foundation.NSXMLNotationDeclarationKind, 12)

    def testOutputArgs(self):
        self.assertArgIsOut(Foundation.NSXMLNode.nodesForXPath_error_, 1)
        self.assertArgIsOut(Foundation.NSXMLNode.objectsForXQuery_constants_error_, 2)
        self.assertArgIsOut(Foundation.NSXMLNode.objectsForXQuery_error_, 1)
        self.assertArgIsBOOL(Foundation.NSXMLNode.setStringValue_resolvingEntities_, 1)
        self.assertArgIsBOOL(
            Foundation.NSXMLNode.canonicalXMLStringPreservingComments_, 0
        )
