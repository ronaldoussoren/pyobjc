import unittest
from Foundation import NSNull

class TestNSNull (unittest.TestCase):
    def testBool(self):
        v = NSNull.null()
        self.assert_(not v)

if __name__ == "__main__":
    unittest.main()
