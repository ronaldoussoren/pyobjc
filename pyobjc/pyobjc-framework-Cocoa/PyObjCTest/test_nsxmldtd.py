from Foundation import *
import unittest

class TestXMLDTD (unittest.TestCase):

    def testOutputArgs(self):
        n =  NSXMLDTD.alloc().init()
        self.assertEquals(
            n.initWithContentsOfURL_options_error_.__metadata__()['arguments'][4]['type'],
            'o^@')
        self.assertEquals(
            n.initWithData_options_error_.__metadata__()['arguments'][4]['type'],
            'o^@')



if __name__ == "__main__":
    unittest.main()
