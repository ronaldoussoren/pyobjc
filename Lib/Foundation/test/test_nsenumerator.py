import unittest
import objc

from Foundation import *

class TestNSEnumeratorInteraction(unittest.TestCase):
    def setUp(self):
        self.arrayContainer = NSArray.arrayWithArray_(range(100))

    def testInOperator(self):
        y = []
        for x in self.arrayContainer.objectEnumerator():
            y.append(x)

        self.assertEquals(len(y), len(self.arrayContainer))
        for i in range(len(y)):
            self.assertEquals(y[i], self.arrayContainer[i])

if __name__ == '__main__':
    unittest.main( )
