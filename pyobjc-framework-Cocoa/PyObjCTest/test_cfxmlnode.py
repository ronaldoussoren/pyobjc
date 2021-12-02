import CoreFoundation
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestXMLNode(TestCase):
    # NOTE: This doesn't actually test the API

    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFXMLNodeRef)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFXMLNodeCurrentVersion, 1)

        self.assertEqual(CoreFoundation.kCFXMLNodeTypeDocument, 1)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeElement, 2)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeAttribute, 3)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeProcessingInstruction, 4)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeComment, 5)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeText, 6)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeCDATASection, 7)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeDocumentFragment, 8)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeEntity, 9)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeEntityReference, 10)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeDocumentType, 11)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeWhitespace, 12)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeNotation, 13)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeElementTypeDeclaration, 14)
        self.assertEqual(CoreFoundation.kCFXMLNodeTypeAttributeListDeclaration, 15)

        self.assertEqual(CoreFoundation.kCFXMLEntityTypeParameter, 0)
        self.assertEqual(CoreFoundation.kCFXMLEntityTypeParsedInternal, 1)
        self.assertEqual(CoreFoundation.kCFXMLEntityTypeParsedExternal, 2)
        self.assertEqual(CoreFoundation.kCFXMLEntityTypeUnparsed, 3)
        self.assertEqual(CoreFoundation.kCFXMLEntityTypeCharacter, 4)

    def testStructs(self):
        # self.fail()

        o = CoreFoundation.CFXMLElementInfo()
        self.assertHasAttr(o, "attributes")
        self.assertHasAttr(o, "attributeOrder")
        self.assertHasAttr(o, "isEmpty")
        self.assertHasAttr(o, "_reserved")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLProcessingInstructionInfo()
        self.assertHasAttr(o, "dataString")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLDocumentInfo()
        self.assertHasAttr(o, "sourceURL")
        self.assertHasAttr(o, "encoding")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLExternalID()
        self.assertHasAttr(o, "systemID")
        self.assertHasAttr(o, "publicID")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLDocumentTypeInfo()
        self.assertHasAttr(o, "externalID")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLNotationInfo()
        self.assertHasAttr(o, "externalID")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLElementTypeDeclarationInfo()
        self.assertHasAttr(o, "contentDescription")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLAttributeDeclarationInfo()
        self.assertHasAttr(o, "attributeName")
        self.assertHasAttr(o, "typeString")
        self.assertHasAttr(o, "defaultString")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLAttributeListDeclarationInfo()
        self.assertHasAttr(o, "numberOfAttributes")
        self.assertHasAttr(o, "attributes")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLEntityInfo()
        self.assertHasAttr(o, "entityType")
        self.assertHasAttr(o, "replacementText")
        self.assertHasAttr(o, "entityID")
        self.assertHasAttr(o, "notationName")
        self.assertPickleRoundTrips(o)

        o = CoreFoundation.CFXMLEntityReferenceInfo()
        self.assertHasAttr(o, "entityType")

    def testFunctions(self):
        self.assertIsInstance(CoreFoundation.CFXMLNodeGetTypeID(), int)

        # CoreFoundation.CFXMLNodeCreate: requires manual binding
        # CoreFoundation.CFXMLNodeGetInfoPtr: likewise
        # Add tests that create all valid types of nodes with there additional info and
        # try to extract the information.

        self.assertResultIsCFRetained(CoreFoundation.CFXMLNodeCreateCopy)
        self.assertResultIsCFRetained(CoreFoundation.CFXMLTreeCreateWithNode)
        CoreFoundation.CFXMLNodeGetTypeCode
        CoreFoundation.CFXMLNodeGetString
        CoreFoundation.CFXMLNodeGetVersion
        CoreFoundation.CFXMLTreeGetNode

    @expectedFailure
    def testMissingWrappers(self):
        self.fail("CFXML requires manual wrappers (low prio)")
