import Foundation
from PyObjCTools.TestSupport import TestCase


class TestXMLDTDNode(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSXMLDTDNodeKind)

    def testConstants(self):
        self.assertEqual(Foundation.NSXMLEntityGeneralKind, 1)
        self.assertEqual(Foundation.NSXMLEntityParsedKind, 2)
        self.assertEqual(Foundation.NSXMLEntityUnparsedKind, 3)
        self.assertEqual(Foundation.NSXMLEntityParameterKind, 4)
        self.assertEqual(Foundation.NSXMLEntityPredefined, 5)
        self.assertEqual(Foundation.NSXMLAttributeCDATAKind, 6)
        self.assertEqual(Foundation.NSXMLAttributeIDKind, 7)
        self.assertEqual(Foundation.NSXMLAttributeIDRefKind, 8)
        self.assertEqual(Foundation.NSXMLAttributeIDRefsKind, 9)
        self.assertEqual(Foundation.NSXMLAttributeEntityKind, 10)
        self.assertEqual(Foundation.NSXMLAttributeEntitiesKind, 11)
        self.assertEqual(Foundation.NSXMLAttributeNMTokenKind, 12)
        self.assertEqual(Foundation.NSXMLAttributeNMTokensKind, 13)
        self.assertEqual(Foundation.NSXMLAttributeEnumerationKind, 14)
        self.assertEqual(Foundation.NSXMLAttributeNotationKind, 15)
        self.assertEqual(Foundation.NSXMLElementDeclarationUndefinedKind, 16)
        self.assertEqual(Foundation.NSXMLElementDeclarationEmptyKind, 17)
        self.assertEqual(Foundation.NSXMLElementDeclarationAnyKind, 18)
        self.assertEqual(Foundation.NSXMLElementDeclarationMixedKind, 19)
        self.assertEqual(Foundation.NSXMLElementDeclarationElementKind, 20)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSXMLDTDNode.isExternal)
