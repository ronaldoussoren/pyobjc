import unittest
import objc

try:
    import Foundation
except ImportError:
    pass

try:
    import AppKit
except ImportError:
    pass

try:
    import PreferencePanes
except ImportError:
    pass

try:
    import ScreenSaver
except ImportError:
    pass

try:
    import InterfaceBuilder
except ImportError:
    pass

try:
    import WebKit
except ImportError:
    pass

import sys


class SplitSignatureTest (unittest.TestCase):

    def testSplitSignature(self):
    # This is a very expensive test, with 1 goal: Verify that all method
    # signatures, and therefore all signatures changed by PyObjC, are
    # valid.
        for cls in objc.getClassList():
            for selName in dir(cls):
                try:
                    sel = getattr(cls, selName)
                except AttributeError:
                    continue

                if not isinstance(sel, objc.selector): continue
                elems = objc.splitSignature(sel.signature)


    def testSimple(self):
        self.assertEquals(objc.splitSignature("@:@"), ('@',':','@'))
        self.assertEquals(objc.splitSignature("@:10{NSRect=ff}"), ('@',':','{NSRect=ff}'))
        self.assertEquals(objc.splitSignature("@:o^@"), ('@',':','o^@'))

    def testSignatureCount(self):
        EXCEPTIONS=[

            # For some reason this signature doesn't seem to be correct, even
            # though we don't touch it...
            "initWithDocument_URL_windowProperties_locationProperties_interpreterBuiltins_",
            
            # Some unittests...
            "setKey4",
            "get_key2",
            "read_bar",
        ]

        for cls in objc.getClassList():
            for selName in dir(cls):
                if selName in EXCEPTIONS: continue

                try:
                    sel = getattr(cls, selName)
                except AttributeError:
                    continue

                if not isinstance(sel, objc.selector): continue
                elems = objc.splitSignature(sel.signature)

                argcount = len(elems) - 3 # retval, self, _sel
                coloncount = sel.selector.count(':')

                self.assertEquals(argcount, coloncount, 
                        '%s [%d:%d] %r %r'%(sel.selector, argcount, coloncount, elems, cls))


if __name__ == "__main__":
    unittest.main()
