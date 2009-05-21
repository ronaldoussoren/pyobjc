from PyObjCTools.TestSupport import *
import objc



gDict = {}

"""
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
"""

import sys


class SplitSignatureTest (TestCase):

    def testSplitSignature(self):
    # This is a very expensive test, with 1 goal: Verify that all method
    # signatures, and therefore all signatures changed by PyObjC, are
    # valid.
        for cls in objc.getClassList():
            for selName in cls.__dict__.keys():
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

        # struct definition in an struct objc_ivar
        self.assertEquals(objc.splitSignature('{_NSRect="origin"{_NSPoint="x"f"y"f}"size"{_NSSize="width"f"height"f}}'), ('{_NSRect="origin"{_NSPoint="x"f"y"f}"size"{_NSSize="width"f"height"f}}',))

    def testSignatureCount(self):
        EXCEPTIONS=[

            # For some reason this signature doesn't seem to be correct, even
            # though we don't touch it...
            "initWithDocument_URL_windowProperties_locationProperties_interpreterBuiltins_",
            
            # Some unittests...
            "setKey4",
            "get_key2",
            "read_bar",
            "setFoo_",
            "method_with_embedded_underscores",
            "methodWithArg_",
            "myMethod",
            "twoargs",
            "set_helper",

            # dictionary methods
            'get',
        ]

        for cls in objc.getClassList():
            if cls.__name__.startswith('OC_'): continue
            for selName in cls.__dict__.keys():
                if selName in EXCEPTIONS: continue
                if selName.startswith('__') and selName.endswith('__'): continue

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
    main()
