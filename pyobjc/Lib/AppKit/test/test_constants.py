import unittest
import AppKit

class ContantTest (unittest.TestCase):

    def testNSFloatingWindowLevel(self):
        # NSFloatingWindowLevel is a define in Objective-C, up-to 1.0rc1 
        # we didn't correctly pick up this define due to a bug in the code.
        self.assert_(hasattr(AppKit, 'NSFloatingWindowLevel'))
        self.assert_(isinstance(AppKit.NSFloatingWindowLevel, int))

if __name__ == "__main__":
    unittest.main()
