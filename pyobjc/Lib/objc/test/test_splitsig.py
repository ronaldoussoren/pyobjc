import unittest
import objc
import Foundation
import AppKit
import PreferencePanes
#import ScreenSaver
import InterfaceBuilder

class SplitSignatureTest (unittest.TestCase):

    # Test is disabled, causes core dump.
    def xxtestSplitSignature(self):
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

if __name__ == "__main__":
    unittest.main()
