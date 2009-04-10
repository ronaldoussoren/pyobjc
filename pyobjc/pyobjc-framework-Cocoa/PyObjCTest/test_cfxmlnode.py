from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestXMLNode (TestCase):
    # NOTE: This doesn't actually test the API

    def testTypes(self):
        self.failUnlessIsCFType(CFXMLNodeRef)


    def testConstants(self):
        self.failUnless( kCFXMLNodeCurrentVersion == 1 )

        self.failUnless( kCFXMLNodeTypeDocument == 1 )
        self.failUnless( kCFXMLNodeTypeElement == 2 )
        self.failUnless( kCFXMLNodeTypeAttribute == 3 )
        self.failUnless( kCFXMLNodeTypeProcessingInstruction == 4 )
        self.failUnless( kCFXMLNodeTypeComment == 5 )
        self.failUnless( kCFXMLNodeTypeText == 6 )
        self.failUnless( kCFXMLNodeTypeCDATASection == 7 )
        self.failUnless( kCFXMLNodeTypeDocumentFragment == 8 )
        self.failUnless( kCFXMLNodeTypeEntity == 9 )
        self.failUnless( kCFXMLNodeTypeEntityReference == 10 )
        self.failUnless( kCFXMLNodeTypeDocumentType == 11 )
        self.failUnless( kCFXMLNodeTypeWhitespace == 12 )
        self.failUnless( kCFXMLNodeTypeNotation == 13 )
        self.failUnless( kCFXMLNodeTypeElementTypeDeclaration == 14 )
        self.failUnless( kCFXMLNodeTypeAttributeListDeclaration == 15 )

        self.failUnless( kCFXMLEntityTypeParameter == 0 )
        self.failUnless( kCFXMLEntityTypeParsedInternal == 1 )
        self.failUnless( kCFXMLEntityTypeParsedExternal == 2 )
        self.failUnless( kCFXMLEntityTypeUnparsed == 3 )
        self.failUnless( kCFXMLEntityTypeCharacter == 4 )

    def testStructs(self):
        return 

        o = CFXMLElementInfo()
        self.failUnless( hasattr(o, 'attributes') )
        self.failUnless( hasattr(o, 'attributeOrder') )
        self.failUnless( hasattr(o, 'isEmpty') )
        self.failUnless( hasattr(o, '_reserved') )

        o = CFXMLProcessingInstructionInfo()
        self.failUnless( hasattr(o, 'dataString') )

        o = CFXMLDocumentInfo()
        self.failUnless( hasattr(o, 'sourceURL') )
        self.failUnless( hasattr(o, 'encoding') )

        o = CFXMLExternalID()
        self.failUnless( hasattr(o, 'systemID') )
        self.failUnless( hasattr(o, 'publicID') )

        o = CFXMLDocumentTypeInfo()
        self.failUnless( hasattr(o, 'externalID') )

        o = CFXMLNotationInfo()
        self.failUnless( hasattr(o, 'externalID') )

        o = CFXMLElementTypeDeclarationInfo()
        self.failUnless( hasattr(o, 'contentDescription') )

        o = CFXMLAttributeDeclarationInfo()
        self.failUnless( hasattr(o, 'attributeName') )
        self.failUnless( hasattr(o, 'typeString') )
        self.failUnless( hasattr(o, 'defaultString') )

        o = CFXMLAttributeListDeclarationInfo()
        self.failUnless( hasattr(o, 'numberOfAttributes') )
        self.failUnless( hasattr(o, 'attributes') )

        o = CFXMLEntityInfo()
        self.failUnless( hasattr(o, 'entityType') )
        self.failUnless( hasattr(o, 'replacementText') )
        self.failUnless( hasattr(o, 'entityID') )
        self.failUnless( hasattr(o, 'notationName') )

        o = CFXMLEntityReferenceInfo()
        self.failUnless( hasattr(o, 'entityType') )

    def testFunctions(self):
        self.failUnlessIsInstance(CFXMLNodeGetTypeID(), (int, long))

        # CFXMLNodeCreate: requires manual binding
        # CFXMLNodeGetInfoPtr: likewise
        # Add tests that create all valid types of nodes with there additional info and
        # try to extract the information.

        self.failUnlessResultIsCFRetained(CFXMLNodeCreateCopy)
        self.failUnlessResultIsCFRetained(CFXMLTreeCreateWithNode)

if __name__ == "__main__":
    main()
