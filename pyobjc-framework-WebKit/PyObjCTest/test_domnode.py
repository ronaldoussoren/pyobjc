from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMNode(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_ELEMENT_NODE, 1)
        self.assertEqual(WebKit.DOM_ATTRIBUTE_NODE, 2)
        self.assertEqual(WebKit.DOM_TEXT_NODE, 3)
        self.assertEqual(WebKit.DOM_CDATA_SECTION_NODE, 4)
        self.assertEqual(WebKit.DOM_ENTITY_REFERENCE_NODE, 5)
        self.assertEqual(WebKit.DOM_ENTITY_NODE, 6)
        self.assertEqual(WebKit.DOM_PROCESSING_INSTRUCTION_NODE, 7)
        self.assertEqual(WebKit.DOM_COMMENT_NODE, 8)
        self.assertEqual(WebKit.DOM_DOCUMENT_NODE, 9)
        self.assertEqual(WebKit.DOM_DOCUMENT_TYPE_NODE, 10)
        self.assertEqual(WebKit.DOM_DOCUMENT_FRAGMENT_NODE, 11)
        self.assertEqual(WebKit.DOM_NOTATION_NODE, 12)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(WebKit.DOM_DOCUMENT_POSITION_DISCONNECTED, 1)
        self.assertEqual(WebKit.DOM_DOCUMENT_POSITION_PRECEDING, 2)
        self.assertEqual(WebKit.DOM_DOCUMENT_POSITION_FOLLOWING, 4)
        self.assertEqual(WebKit.DOM_DOCUMENT_POSITION_CONTAINS, 8)
        self.assertEqual(WebKit.DOM_DOCUMENT_POSITION_CONTAINED_BY, 16)
        self.assertEqual(WebKit.DOM_DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC, 32)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMNode.hasChildNodes)
        self.assertArgIsBOOL(WebKit.DOMNode.cloneNode_, 0)
        self.assertResultIsBOOL(WebKit.DOMNode.isSupported_version_)
        self.assertResultIsBOOL(WebKit.DOMNode.isSupported__)
        self.assertResultIsBOOL(WebKit.DOMNode.hasAttributes)
        self.assertResultIsBOOL(WebKit.DOMNode.isSameNode_)
        self.assertResultIsBOOL(WebKit.DOMNode.isEqualNode_)

        self.assertResultIsBOOL(WebKit.DOMNode.isContentEditable)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(WebKit.DOMNode.isDefaultNamespace_)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(WebKit.DOMNode.contains_)
