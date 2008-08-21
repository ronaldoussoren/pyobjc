from Foundation import *
import unittest

class TestArchiver (unittest.TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSInconsistentArchiveException, unicode))


if __name__ == "__main__":
    unittest.main()
