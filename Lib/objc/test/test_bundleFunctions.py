import objc
import Foundation
import unittest

def S(*args):
    return ''.join(args)

FUNCTIONS=[
    ( 'NSIsFreedObject', S(objc._C_NSBOOL, objc._C_ID) ),
    ( 'NSCountFrames', S(objc._C_UINT) ),
]

class TestBundleFunctions (unittest.TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testSimple(self):
        self.assert_(0, "Not implemented yet")

if __name__ == "__main__":
    unittest.main()


