from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLDTDNode (TestCase):
    def testConstants(self):
        self.assertEqual(NSXMLEntityGeneralKind, 1)
        self.assertEqual(NSXMLEntityParsedKind, 2)
        self.assertEqual(NSXMLEntityUnparsedKind, 3)
        self.assertEqual(NSXMLEntityParameterKind, 4)
        self.assertEqual(NSXMLEntityPredefined, 5)
        self.assertEqual(NSXMLAttributeCDATAKind, 6)
        self.assertEqual(NSXMLAttributeIDKind, 7)
        self.assertEqual(NSXMLAttributeIDRefKind, 8)
        self.assertEqual(NSXMLAttributeIDRefsKind,  9)      
        self.assertEqual(NSXMLAttributeEntityKind, 10)
        self.assertEqual(NSXMLAttributeEntitiesKind, 11)
        self.assertEqual(NSXMLAttributeNMTokenKind, 12)
        self.assertEqual(NSXMLAttributeNMTokensKind, 13)
        self.assertEqual(NSXMLAttributeEnumerationKind, 14)
        self.assertEqual(NSXMLAttributeNotationKind, 15)
        self.assertEqual(NSXMLElementDeclarationUndefinedKind, 16)
        self.assertEqual(NSXMLElementDeclarationEmptyKind, 17)
        self.assertEqual(NSXMLElementDeclarationAnyKind, 18)
        self.assertEqual(NSXMLElementDeclarationMixedKind, 19)
        self.assertEqual(NSXMLElementDeclarationElementKind, 20)

    def testMethods(self):
        self.assertResultIsBOOL(NSXMLDTDNode.isExternal)


if __name__ == "__main__":
    main()
