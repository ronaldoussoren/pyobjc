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
            for selName in list(cls.__dict__.keys()):
                try:
                    sel = getattr(cls, selName.decode('latin1'))
                except AttributeError:
                    continue

                if not isinstance(sel, objc.selector): continue
                elems = objc.splitSignature(sel.signature)


    def testSimple(self):
        self.assertEqual(objc.splitSignature(b"@:@"), (b'@',b':',b'@'))
        self.assertEqual(objc.splitSignature(b"@:10{NSRect=ff}"), (b'@',b':',b'{NSRect=ff}'))
        self.assertEqual(objc.splitSignature(b"@:o^@"), (b'@',b':',b'o^@'))

        # Block pointer
        self.assertEqual(objc.splitSignature(b"@:@?"), (b'@',b':',b'@?'))

        # struct definition in an struct objc_ivar
        self.assertEqual(objc.splitSignature(b'{_NSRect="origin"{_NSPoint="x"f"y"f}"size"{_NSSize="width"f"height"f}}'), (b'{_NSRect="origin"{_NSPoint="x"f"y"f}"size"{_NSSize="width"f"height"f}}',))

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
            "get",
            "has_key",
        ]

        for cls in objc.getClassList():
            #if cls.__name__.startswith('OC_'): continue
            if cls.__name__.startswith('OC'): continue
            for selName in cls.__dict__.keys():
                self.assertIsInstance(selName, str)
                if selName in EXCEPTIONS: continue
                if selName.startswith('__') and selName.endswith('__'): continue

                try:
                    sel = getattr(cls, selName)
                except AttributeError:
                    continue

                if not isinstance(sel, objc.selector): continue
                elems = objc.splitSignature(sel.signature)

                argcount = len(elems) - 3 # retval, self, _sel
                coloncount = sel.selector.count(b':')

                self.assertEqual(argcount, coloncount,
                        '%s [%d:%d] %r %r'%(sel.selector.decode('latin1'), argcount, coloncount, elems, cls))

    def testSplitStructSignature(self):
        self.assertRaises(ValueError, objc.splitStructSignature, objc._C_ID)
        self.assertRaises(ValueError, objc.splitStructSignature, b"{NSPoint=dd")
        self.assertRaises(ValueError, objc.splitStructSignature, b"{NSPoint=dd}d")

        self.assertEqual(objc.splitStructSignature(b'{NSPoint=dd}'), ("NSPoint", [(None, b'd'), (None, b'd')]))
        self.assertEqual(objc.splitStructSignature(b'{NSPoint="x"d"y"d}'), ("NSPoint", [("x", b'd'), ("y", b'd')]))

    def testSplitStruct(self):
        self.assertRaises(ValueError, objc.splitStruct, objc._C_ID)
        self.assertRaises(ValueError, objc.splitStruct, b"{NSPoint=dd")
        self.assertRaises(ValueError, objc.splitStruct, b"{NSPoint=dd}d")

        self.assertEqual(objc.splitStruct(b'{NSPoint=dd}'), ("NSPoint", [(None, b'd'), (None, b'd')]))
        self.assertEqual(objc.splitStruct(b'{NSPoint="x"d"y"d}'), ("NSPoint", [("x", b'd'), ("y", b'd')]))

if __name__ == "__main__":
    main()
