import unittest

from AppKit import *
import objc

class ObjCTestNSView_KnowPageRange (NSView):
    def knowsPageRange_(self):
        return  objc.YES, (1, 10)

class TestNSView (unittest.TestCase):

    def test_knowsPageRange(self):
        method = ObjCTestNSView_KnowPageRange.knowsPageRange_
        self.assertEquals(method.signature, "C@:o^{_NSRange=II}")

if __name__ == "__main__":
    unittest.main()
