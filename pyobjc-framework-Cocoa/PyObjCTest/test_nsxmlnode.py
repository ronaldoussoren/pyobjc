from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLNode (TestCase):
    def testConstants(self):
        self.assertEquals(NSXMLInvalidKind, 0)
        self.assertEquals(NSXMLDocumentKind, 1)
        self.assertEquals(NSXMLElementKind, 2)
        self.assertEquals(NSXMLAttributeKind, 3)
        self.assertEquals(NSXMLNamespaceKind, 4)
        self.assertEquals(NSXMLProcessingInstructionKind, 5)
        self.assertEquals(NSXMLCommentKind, 6)
        self.assertEquals(NSXMLTextKind, 7)
        self.assertEquals(NSXMLDTDKind, 8)
        self.assertEquals(NSXMLEntityDeclarationKind, 9)
        self.assertEquals(NSXMLAttributeDeclarationKind, 10)
        self.assertEquals(NSXMLElementDeclarationKind, 11)
        self.assertEquals(NSXMLNotationDeclarationKind, 12)

    def testOutputArgs(self):
        n =  NSXMLNode.alloc().init()
        self.assertEquals(
            n.nodesForXPath_error_.__metadata__()['arguments'][3]['type'],
            'o^@')

        print n.objectsForXQuery_constants_error_.__metadata__()
        self.assertEquals(
            n.objectsForXQuery_constants_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.objectsForXQuery_error_.__metadata__()['arguments'][3]['type'],
            'o^@')


if __name__ == "__main__":
    main()
