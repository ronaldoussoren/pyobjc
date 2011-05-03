from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestXMLNode (TestCase):
    # NOTE: This doesn't actually test the API

    def testTypes(self):
        self.assertIsCFType(CFXMLNodeRef)


    def testConstants(self):
        self.assertEqual(kCFXMLNodeCurrentVersion , 1 )
        self.assertEqual(kCFXMLNodeTypeDocument , 1 )
        self.assertEqual(kCFXMLNodeTypeElement , 2 )
        self.assertEqual(kCFXMLNodeTypeAttribute , 3 )
        self.assertEqual(kCFXMLNodeTypeProcessingInstruction , 4 )
        self.assertEqual(kCFXMLNodeTypeComment , 5 )
        self.assertEqual(kCFXMLNodeTypeText , 6 )
        self.assertEqual(kCFXMLNodeTypeCDATASection , 7 )
        self.assertEqual(kCFXMLNodeTypeDocumentFragment , 8 )
        self.assertEqual(kCFXMLNodeTypeEntity , 9 )
        self.assertEqual(kCFXMLNodeTypeEntityReference , 10 )
        self.assertEqual(kCFXMLNodeTypeDocumentType , 11 )
        self.assertEqual(kCFXMLNodeTypeWhitespace , 12 )
        self.assertEqual(kCFXMLNodeTypeNotation , 13 )
        self.assertEqual(kCFXMLNodeTypeElementTypeDeclaration , 14 )
        self.assertEqual(kCFXMLNodeTypeAttributeListDeclaration , 15 )
        self.assertEqual(kCFXMLEntityTypeParameter , 0 )
        self.assertEqual(kCFXMLEntityTypeParsedInternal , 1 )
        self.assertEqual(kCFXMLEntityTypeParsedExternal , 2 )
        self.assertEqual(kCFXMLEntityTypeUnparsed , 3 )
        self.assertEqual(kCFXMLEntityTypeCharacter , 4 )
    def testStructs(self):
        return 

        o = CFXMLElementInfo()
        self.assertHasAttr(o, 'attributes')
        self.assertHasAttr(o, 'attributeOrder')
        self.assertHasAttr(o, 'isEmpty')
        self.assertHasAttr(o, '_reserved')
        o = CFXMLProcessingInstructionInfo()
        self.assertHasAttr(o, 'dataString')
        o = CFXMLDocumentInfo()
        self.assertHasAttr(o, 'sourceURL')
        self.assertHasAttr(o, 'encoding')
        o = CFXMLExternalID()
        self.assertHasAttr(o, 'systemID')
        self.assertHasAttr(o, 'publicID')
        o = CFXMLDocumentTypeInfo()
        self.assertHasAttr(o, 'externalID')
        o = CFXMLNotationInfo()
        self.assertHasAttr(o, 'externalID')
        o = CFXMLElementTypeDeclarationInfo()
        self.assertHasAttr(o, 'contentDescription')
        o = CFXMLAttributeDeclarationInfo()
        self.assertHasAttr(o, 'attributeName')
        self.assertHasAttr(o, 'typeString')
        self.assertHasAttr(o, 'defaultString')
        o = CFXMLAttributeListDeclarationInfo()
        self.assertHasAttr(o, 'numberOfAttributes')
        self.assertHasAttr(o, 'attributes')
        o = CFXMLEntityInfo()
        self.assertHasAttr(o, 'entityType')
        self.assertHasAttr(o, 'replacementText')
        self.assertHasAttr(o, 'entityID')
        self.assertHasAttr(o, 'notationName')
        o = CFXMLEntityReferenceInfo()
        self.assertHasAttr(o, 'entityType')
    def testFunctions(self):
        self.assertIsInstance(CFXMLNodeGetTypeID(), (int, long))

        # CFXMLNodeCreate: requires manual binding
        # CFXMLNodeGetInfoPtr: likewise
        # Add tests that create all valid types of nodes with there additional info and
        # try to extract the information.

        self.assertResultIsCFRetained(CFXMLNodeCreateCopy)
        self.assertResultIsCFRetained(CFXMLTreeCreateWithNode)

if __name__ == "__main__":
    main()
