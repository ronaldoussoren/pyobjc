import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSXMLNodeOptions(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSXMLNodeOptionsNone, 0)

        self.assertEqual(Foundation.NSXMLNodeIsCDATA, 1 << 0)
        self.assertEqual(Foundation.NSXMLNodeExpandEmptyElement, 1 << 1)
        self.assertEqual(Foundation.NSXMLNodeCompactEmptyElement, 1 << 2)
        self.assertEqual(Foundation.NSXMLNodeUseSingleQuotes, 1 << 3)
        self.assertEqual(Foundation.NSXMLNodeUseDoubleQuotes, 1 << 4)
        self.assertEqual(Foundation.NSXMLNodeNeverEscapeContents, 1 << 5)

        self.assertEqual(Foundation.NSXMLDocumentTidyHTML, 1 << 9)
        self.assertEqual(Foundation.NSXMLDocumentTidyXML, 1 << 10)

        self.assertEqual(Foundation.NSXMLDocumentValidate, 1 << 13)

        self.assertEqual(Foundation.NSXMLNodeLoadExternalEntitiesAlways, 1 << 14)
        self.assertEqual(
            Foundation.NSXMLNodeLoadExternalEntitiesSameOriginOnly, 1 << 15
        )
        self.assertEqual(Foundation.NSXMLNodeLoadExternalEntitiesNever, 1 << 19)

        self.assertEqual(Foundation.NSXMLDocumentXInclude, 1 << 16)

        self.assertEqual(Foundation.NSXMLNodePrettyPrint, 1 << 17)
        self.assertEqual(Foundation.NSXMLDocumentIncludeContentTypeDeclaration, 1 << 18)

        self.assertEqual(Foundation.NSXMLNodePreserveNamespaceOrder, 1 << 20)
        self.assertEqual(Foundation.NSXMLNodePreserveAttributeOrder, 1 << 21)
        self.assertEqual(Foundation.NSXMLNodePreserveEntities, 1 << 22)
        self.assertEqual(Foundation.NSXMLNodePreservePrefixes, 1 << 23)
        self.assertEqual(Foundation.NSXMLNodePreserveCDATA, 1 << 24)
        self.assertEqual(Foundation.NSXMLNodePreserveWhitespace, 1 << 25)
        self.assertEqual(Foundation.NSXMLNodePreserveDTD, 1 << 26)
        self.assertEqual(Foundation.NSXMLNodePreserveCharacterReferences, 1 << 27)
        self.assertEqual(Foundation.NSXMLNodePromoteSignificantWhitespace, 1 << 28)

        self.assertEqual(
            Foundation.NSXMLNodePreserveEmptyElements,
            (
                Foundation.NSXMLNodeExpandEmptyElement
                | Foundation.NSXMLNodeCompactEmptyElement
            ),
        )
        self.assertEqual(
            Foundation.NSXMLNodePreserveQuotes,
            (Foundation.NSXMLNodeUseSingleQuotes | Foundation.NSXMLNodeUseDoubleQuotes),
        )
        self.assertEqual(
            Foundation.NSXMLNodePreserveAll & 0xFFFFFFFF,
            0xFFFFFFFF
            & (
                Foundation.NSXMLNodePreserveNamespaceOrder
                | Foundation.NSXMLNodePreserveAttributeOrder
                | Foundation.NSXMLNodePreserveEntities
                | Foundation.NSXMLNodePreservePrefixes
                | Foundation.NSXMLNodePreserveCDATA
                | Foundation.NSXMLNodePreserveEmptyElements
                | Foundation.NSXMLNodePreserveQuotes
                | Foundation.NSXMLNodePreserveWhitespace
                | Foundation.NSXMLNodePreserveDTD
                | Foundation.NSXMLNodePreserveCharacterReferences
                | 0xFFF00000
            ),
        )
