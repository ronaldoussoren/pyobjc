import unittest
import objc

from Foundation import *

class TestHelper (NSObject):
    def incFoo_(self, foo):
        foo[0] += 1

class TestNSUndoManager(unittest.TestCase):
    def testUndoManager(self):
        x = TestHelper.new()
        m = NSUndoManager.new()
        l = [ 0 ]

        m.prepareWithInvocationTarget_(x).incFoo_(l)
        m.undo()

        self.assertEquals(l[0], 1)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite( TestNSUndoManager))
    return suite

if __name__ == '__main__':
    unittest.main( )
