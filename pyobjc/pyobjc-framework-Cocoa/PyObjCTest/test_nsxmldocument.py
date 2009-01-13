from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLDocument (TestCase):
    def testConstants(self):
        self.assertEquals(NSXMLDocumentXMLKind, 0)
        self.assertEquals(NSXMLDocumentXHTMLKind, 1)
        self.assertEquals(NSXMLDocumentHTMLKind, 2)
        self.assertEquals(NSXMLDocumentTextKind, 3)

    def testOutputArgs(self):
        n =  NSXMLDocument.alloc().init()
        self.assertEquals(
            n.initWithXMLString_options_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.initWithContentsOfURL_options_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.initWithData_options_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.objectByApplyingXSLT_arguments_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.objectByApplyingXSLTString_arguments_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.objectByApplyingXSLTAtURL_arguments_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.validateAndReturnError_.__metadata__()['arguments'][2]['type'],
            'o^@')

if __name__ == "__main__":
    main()
