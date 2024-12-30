import objc
from PyObjCTools.TestSupport import TestCase

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

IGNORED_CLASSES = {"UINSServiceViewController"}


class SplitSignatureTest(TestCase):
    def testSplitSignature(self):
        # This is a very expensive test, with 1 goal: Verify that all method
        # signatures, and therefore all signatures changed by PyObjC, are
        # valid.
        for cls in objc.getClassList():
            with self.subTest(cls.__name__):
                if cls.__name__ in IGNORED_CLASSES:
                    continue

                for selName in list(cls.__dict__.keys()):
                    try:
                        sel = getattr(cls, selName.decode("latin1"))
                    except (AttributeError, TypeError):
                        continue

                    if not isinstance(sel, objc.selector):
                        continue

                    # Check is that the call is successfull
                    objc.splitSignature(sel.signature)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            objc.splitSignature()

        with self.assertRaisesRegex(ValueError, "type signature"):
            objc.splitSignature(b"{ab")

    def testSimple(self):
        self.assertEqual(objc.splitSignature(b"@:@"), (b"@", b":", b"@"))
        self.assertEqual(
            objc.splitSignature(b"@:10{NSRect=ff}"), (b"@", b":", b"{NSRect=ff}")
        )
        self.assertEqual(objc.splitSignature(b"@:o^@"), (b"@", b":", b"o^@"))

        # Block pointer
        self.assertEqual(objc.splitSignature(b"@:@?"), (b"@", b":", b"@?"))

        # struct definition in an struct objc_ivar
        self.assertEqual(
            objc.splitSignature(
                b'{_NSRect="origin"{_NSPoint="x"f"y"f}"size"{_NSSize="width"f"height"f}}'
            ),
            (
                b'{_NSRect="origin"{_NSPoint="x"f"y"f}"size"{_NSSize="width"f"height"f}}',
            ),
        )

    def testSignatureCount(self):
        EXCEPTIONS = [
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
            "callback",
            # dictionary methods
            "get",
            "has_key",
            # Unclear why this signature isn't correct, possibly due to the 'queue'.
            # method is private anyway...
            "SCN_setupDisplayLinkWithQueue_screen_policy_",
            "isNSURL__",
        ]

        for cls in objc.getClassList():
            if cls.__name__ in IGNORED_CLASSES:
                continue
            if cls.__name__.startswith("OC"):
                continue
            for selName in cls.__dict__.keys():
                self.assertIsInstance(selName, str)
                if selName in EXCEPTIONS:
                    continue
                if selName.startswith("__") and selName.endswith("__"):
                    continue

                try:
                    sel = getattr(cls, selName)
                except (AttributeError, TypeError):
                    continue

                if not isinstance(sel, objc.selector):
                    continue

                if sel.selector.split(b":", 1)[0] in (
                    b"fm",
                    b"_fm",
                    b"_ns",
                    b"_ax",
                    b"_scr",
                    b"CA_interpolateValues",
                    b"__NS_swiftOverlay",
                    b"__im",
                    b"__msv",
                    b"_compatibility",
                    b"_fides",
                    b"_intents",
                    b"_ql",
                    b"ck",
                    b"cl",
                    b"cksqlcs",
                    b"ef",
                    b"if",
                    b"pep",
                    b"ams",
                    b"safari",
                    b"vs",
                    b"swiftui",
                    b"_swiftui",
                ) or sel.selector in (
                    b"isNSArray::",
                    b"isNSCFConstantString::",
                    b"isNSData::",
                    b"isNSDate::",
                    b"isNSDictionary::",
                    b"isNSNumber::",
                    b"isNSObject::",
                    b"isNSOrderedSet::",
                    b"isNSSet::",
                    b"isNSString::",
                    b"isNSTimeZone::",
                    b"isNSValue::",
                    b"QTKeyValueProxyTarget:keyPathsForValuesAffectingValueForKey:",
                ):
                    # These keep turning up on test runs on macOS 13.1. Ignore as these
                    # are private APIs.
                    continue

                elems = objc.splitSignature(sel.signature)

                argcount = len(elems) - 3  # retval, self, _sel
                coloncount = sel.selector.count(b":")

                with self.subTest(cls=cls.__name__, sel=sel.selector):
                    self.assertEqual(
                        argcount,
                        coloncount,
                        "%s [%d:%d] %r %r"
                        % (
                            sel.selector.decode("latin1"),
                            argcount,
                            coloncount,
                            elems,
                            cls,
                        ),
                    )

    def testSplitStructSignature(self):
        with self.assertRaises(TypeError):
            objc.splitStructSignature()

        self.assertEqual(objc.splitStructSignature(b"{a}"), (None, []))

        with self.assertRaisesRegex(ValueError, "not a struct encoding"):
            objc.splitStructSignature(objc._C_ID)

        with self.assertRaisesRegex(
            ValueError, "value is not a complete struct signature"
        ):
            objc.splitStructSignature(b"{}")

        with self.assertRaisesRegex(
            ValueError, "value is not a complete struct signature"
        ):
            objc.splitStructSignature(b"{NSPoint=dd")
        with self.assertRaisesRegex(ValueError, "additional text at end of signature"):
            objc.splitStructSignature(b"{NSPoint=dd}d")

        with self.assertRaisesRegex(objc.error, "Unhandled type"):
            objc.splitStructSignature(b"{NSPoint=XX}")

        self.assertEqual(
            objc.splitStructSignature(b"{NSPoint=dd}"),
            ("NSPoint", [(None, b"d"), (None, b"d")]),
        )
        self.assertEqual(
            objc.splitStructSignature(b'{NSPoint="x"d"y"d}'),
            ("NSPoint", [("x", b"d"), ("y", b"d")]),
        )

        self.assertEqual(
            objc.splitStructSignature(b"{=d10d}"),
            (None, [(None, b"d"), (None, b"d")]),
        )

        self.assertEqual(
            objc.splitStructSignature(b"{=dd}"),
            (None, [(None, b"d"), (None, b"d")]),
        )

        self.assertEqual(
            objc.splitStructSignature(b"{NSPoint=}"),
            ("NSPoint", []),
        )

        self.assertEqual(
            objc.splitStructSignature(b"{NSPoint}"),
            ("NSPoint", []),
        )
