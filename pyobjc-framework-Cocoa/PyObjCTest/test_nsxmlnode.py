from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLNode (TestCase):
    def testConstants(self):
        self.assertEqual(NSXMLInvalidKind, 0)
        self.assertEqual(NSXMLDocumentKind, 1)
        self.assertEqual(NSXMLElementKind, 2)
        self.assertEqual(NSXMLAttributeKind, 3)
        self.assertEqual(NSXMLNamespaceKind, 4)
        self.assertEqual(NSXMLProcessingInstructionKind, 5)
        self.assertEqual(NSXMLCommentKind, 6)
        self.assertEqual(NSXMLTextKind, 7)
        self.assertEqual(NSXMLDTDKind, 8)
        self.assertEqual(NSXMLEntityDeclarationKind, 9)
        self.assertEqual(NSXMLAttributeDeclarationKind, 10)
        self.assertEqual(NSXMLElementDeclarationKind, 11)
        self.assertEqual(NSXMLNotationDeclarationKind, 12)

    def testOutputArgs(self):
        self.assertArgIsOut(NSXMLNode.nodesForXPath_error_, 1)
        self.assertArgIsOut(NSXMLNode.objectsForXQuery_constants_error_, 2)
        self.assertArgIsOut(NSXMLNode.objectsForXQuery_error_, 1)
        self.assertArgIsBOOL(NSXMLNode.setStringValue_resolvingEntities_, 1)
        self.assertArgIsBOOL(NSXMLNode.canonicalXMLStringPreservingComments_, 0)


if __name__ == "__main__":
    main()
