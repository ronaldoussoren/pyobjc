import unittest

import objc

class TestRegressions(unittest.TestCase):
    def testQualifiersInSignature(self):
        import Foundation
        import AppKit
        AppKit.NSColor.redColor().getRed_green_blue_alpha_()

if __name__ == '__main__':
    unittest.main()
