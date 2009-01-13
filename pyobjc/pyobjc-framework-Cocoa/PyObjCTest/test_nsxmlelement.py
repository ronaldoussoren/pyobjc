from Foundation import *
from PyObjCTools.TestSupport import *

class TestXMLElement (TestCase):
    def testOutputArgs(self):
        n =  NSXMLElement.alloc().init()
        self.assertEquals(
            n.initWithXMLString_error_.__metadata__()['arguments'][3]['type'],
            'o^@')

if __name__ == "__main__":
    main()
