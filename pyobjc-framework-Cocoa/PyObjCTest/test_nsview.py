import unittest

from AppKit import *
import objc

class ObjCTestNSView_KnowPageRange (NSView):
    def knowsPageRange_(self, range):
        return  objc.YES, (1, 10)

    def rectForPage_(self, page):
        return ((1,1),(2,2))

class TestNSView (unittest.TestCase):

    def test_knowsPageRange(self):
        method = ObjCTestNSView_KnowPageRange.knowsPageRange_
        self.assertEquals(method.__metadata__()['arguments'][2]['type'], 'o^{_NSRange=II}')

    def test_rectForPage(self):
        method = ObjCTestNSView_KnowPageRange.rectForPage_
        self.assertEquals(objc.splitSignature(method.signature), objc.splitSignature("{_NSRect={_NSPoint=ff}{_NSSize=ff}}12@0:4i8"))

if __name__ == "__main__":
    unittest.main()
