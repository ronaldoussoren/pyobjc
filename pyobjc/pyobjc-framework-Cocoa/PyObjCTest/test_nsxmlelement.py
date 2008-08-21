from Foundation import *
import unittest

class TestXMLElement (unittest.TestCase):
    def testOutputArgs(self):
        n =  NSXMLElement.alloc().init()
        self.assertEquals(
            n.initWithXMLString_error_.__metadata__()['arguments'][3]['type'],
            'o^@')

if __name__ == "__main__":
    unittest.main()
