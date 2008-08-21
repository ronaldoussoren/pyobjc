from Foundation import *
import unittest

class TestValueTrans (unittest.TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSNegateBooleanTransformerName, unicode))
        self.failUnless(isinstance(NSIsNilTransformerName, unicode))
        self.failUnless(isinstance(NSIsNotNilTransformerName, unicode))
        self.failUnless(isinstance(NSUnarchiveFromDataTransformerName, unicode))
        self.failUnless(isinstance(NSKeyedUnarchiveFromDataTransformerName, unicode))

if __name__ == "__main__":
    unittest.main()
