from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLDTDNode (TestCase):
    def testConstants(self):
        self.assertEquals(NSXMLEntityGeneralKind, 1)
        self.assertEquals(NSXMLEntityParsedKind, 2)
        self.assertEquals(NSXMLEntityUnparsedKind, 3)
        self.assertEquals(NSXMLEntityParameterKind, 4)
        self.assertEquals(NSXMLEntityPredefined, 5)
        self.assertEquals(NSXMLAttributeCDATAKind, 6)
        self.assertEquals(NSXMLAttributeIDKind, 7)
        self.assertEquals(NSXMLAttributeIDRefKind, 8)
        self.assertEquals(NSXMLAttributeIDRefsKind,  9)      
        self.assertEquals(NSXMLAttributeEntityKind, 10)
        self.assertEquals(NSXMLAttributeEntitiesKind, 11)
        self.assertEquals(NSXMLAttributeNMTokenKind, 12)
        self.assertEquals(NSXMLAttributeNMTokensKind, 13)
        self.assertEquals(NSXMLAttributeEnumerationKind, 14)
        self.assertEquals(NSXMLAttributeNotationKind, 15)
        self.assertEquals(NSXMLElementDeclarationUndefinedKind, 16)
        self.assertEquals(NSXMLElementDeclarationEmptyKind, 17)
        self.assertEquals(NSXMLElementDeclarationAnyKind, 18)
        self.assertEquals(NSXMLElementDeclarationMixedKind, 19)
        self.assertEquals(NSXMLElementDeclarationElementKind, 20)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSXMLDTDNode.isExternal)


if __name__ == "__main__":
    main()
