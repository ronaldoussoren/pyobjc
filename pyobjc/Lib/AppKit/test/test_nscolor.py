import unittest
import AppKit

class TestRegressions (unittest.TestCase):
    def testQualifiersInSignature(self):
        AppKit.NSColor.redColor().getRed_green_blue_alpha_()

if __name__ == "__main__":
    unittest.main()
