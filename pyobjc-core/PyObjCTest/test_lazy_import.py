import operator
import os
import struct
import sys

import objc
import objc._lazyimport as lazyimport
from PyObjCTest import metadatafunction
from PyObjCTools.TestSupport import TestCase


def lookupClasses(*names):
    result = []
    for nm in names:
        try:
            result.append(objc.lookUpClass(nm))
        except objc.nosuchclass_error:
            pass
    return tuple(result)


class TestLazyImport(TestCase):
    def test_exports(self):
        self.assertIs(objc.ObjCLazyModule, lazyimport.ObjCLazyModule)
        self.assertTrue(issubclass(objc.ObjCLazyModule, type(objc)))

    def test_getattr_map(self):
        o = lazyimport.GetAttrMap(sys)
        self.assertEqual(o["path"], sys.path)
        self.assertEqual(o["version"], sys.version)
        self.assertRaises(KeyError, o.__getitem__, "nosuchkey")

    def test_load_bundle(self):
        NSBundle = objc.lookUpClass("NSBundle")

        # _objc is linked with Foundation, hence should be able to load without
        # providing a valid path
        o = lazyimport._loadBundle("Foundation", "com.apple.Foundation", "/dev/null")
        self.assertIsInstance(o, NSBundle)
        self.assertEqual(o.bundleIdentifier(), "com.apple.Foundation")
        self.assertTrue(o.isLoaded())

        # Load using path
        o = lazyimport._loadBundle(
            "AppKit", None, "/System/Library/Frameworks/AppKit.framework"
        )
        o.load()
        self.assertEqual(o.bundleIdentifier(), "com.apple.AppKit")
        self.assertTrue(o.isLoaded())

        # Should not be loaded yet, hence fallback from identifier to path
        o = lazyimport._loadBundle(
            "PreferencePanes",
            "com.apple.frameworks.preferencepanes",
            "/System/Library/Frameworks/PreferencePanes.framework",
        )
        o.load()
        self.assertEqual(o.bundleIdentifier(), "com.apple.frameworks.preferencepanes")
        self.assertTrue(o.isLoaded())

    def test_all_types_without_all(self):
        self.do_test_all_types(dunder_all=False)

    def test_all_types_with_all(self):
        self.do_test_all_types(dunder_all=True)

    def do_test_all_types(self, dunder_all):
        metadict = {
            "nometadata": 42,  # Ignored...
            "protocols": {
                "NSMachPortDelegateMethods": objc.informal_protocol(
                    "NSMachPortDelegateMethods",
                    [
                        objc.selector(
                            None, b"handleMachMessage:", b"v@:^v", isRequired=False
                        )
                    ],
                )
            },
            "constants": "$NSWorkspaceMoveOperation$NSWorkspaceCopyOperation@@$",
            "constants_dict": {
                "NSWorkspaceLinkOperation": "@",
                "NSWindowWillCloseNotification": "@",
                "NSUnderlineByWordMask": objc._C_NSUInteger.decode("ascii"),
            },
            "enums": "$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$",
            "functions": {
                "NSRectClipList": (
                    b"v^{CGRect={CGPoint=dd}{CGSize=dd}}q",
                    "",
                    {
                        "arguments": {
                            0: {"c_array_length_in_arg": 1, "type_modifier": b"n"}
                        }
                    },
                ),
                "FunctionThatDoesNotExist": (
                    b"v^{CGRect={CGPoint=dd}{CGSize=dd}}q",
                    "",
                    {},
                ),
                "NSAccessibilityActionDescription": (b"@@", "", {}),
            },
            "aliases": {"doc_string": "__doc__", "invalid_alias": "does_not_exist"},
            "expressions": {
                "mysum": "NSAWTEventType + NSAboveBottom + 3",
                "invalid_expression1": "no_such_name + 1",
                "invalid_expression2": 'NSAboveBottom + "b"',
            },
        }

        initial_dict = {"__doc__": "AppKit test module"}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            metadict,
            None,
            initial_dict,
            (),
        )
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        self.assertRaises(AttributeError, getattr, mod, "Foo(")
        self.assertRaises(AttributeError, getattr, mod, "Foo)")
        self.assertRaises(AttributeError, getattr, mod, "42")

        if dunder_all:
            # Force precalculation of all attributes by accessing the __all__
            # attribute
            self.assertEqual(set(dir(mod)), set(mod.__all__))

        self.assertEqual(mod.__doc__, initial_dict["__doc__"])
        self.assertEqual(mod.doc_string, initial_dict["__doc__"])
        self.assertRaises(AttributeError, getattr, mod, "invalid_alias")
        self.assertIsInstance(mod.NSWorkspaceMoveOperation, objc.pyobjc_unicode)
        self.assertTrue(
            (mod.NSWorkspaceMoveOperation.nsstring().__flags__ & 0x10) == 0x00
        )
        self.assertIsInstance(mod.NSWorkspaceCopyOperation, objc.pyobjc_unicode)
        self.assertIsInstance(mod.NSWorkspaceLinkOperation, objc.pyobjc_unicode)

        self.assertIsInstance(mod.NSUnderlineByWordMask, int)
        self.assertEqual(mod.NSAWTEventType, 16)
        self.assertEqual(mod.NSAboveBottom, 4)
        self.assertEqual(mod.NSAboveTop, 1)
        self.assertIsInstance(mod.NSRectClipList, objc.function)
        self.assertEqual(mod.NSRectClipList.__name__, "NSRectClipList")
        self.assertArgSizeInArg(mod.NSRectClipList, 0, 1)
        self.assertRaises(AttributeError, getattr, mod, "FunctionThatDoesNotExist")
        self.assertEqual(mod.mysum, mod.NSAWTEventType + mod.NSAboveBottom + 3)
        self.assertRaises(AttributeError, getattr, mod, "invalid_expression1")
        self.assertRaises(AttributeError, getattr, mod, "invalid_expression2")
        self.assertIs(mod.NSURL, objc.lookUpClass("NSURL"))
        self.assertRaises(AttributeError, getattr, mod, "NSNonExistingClass")

        mod.NSAccessibilityActionDescription = 99
        mod.NSWindowWillCloseNotification = 100
        self.assertEqual(set(dir(mod)), set(mod.__all__))
        self.assertIn("NSRectClipList", mod.__dict__)
        self.assertIn("NSRectClipList", mod.__all__)
        self.assertIn("NSAccessibilityActionDescription", mod.__all__)
        self.assertEqual(mod.NSAccessibilityActionDescription, 99)
        self.assertIn("mysum", mod.__all__)
        self.assertIn("NSWorkspaceMoveOperation", mod.__all__)
        self.assertIn("NSWindowWillCloseNotification", mod.__all__)
        self.assertEqual(mod.NSWindowWillCloseNotification, 100)
        self.assertNotIn("__doc__", mod.__all__)

        self.assertIn(
            "NSMachPortDelegateMethods", mod._ObjCLazyModule__informal_protocols
        )

    def test_without_framework(self):
        initial_dict = {
            "__doc__": "rootless test module",
            "__spec__": object(),
            "__loader__": object(),
        }
        metadict = {
            "constants": "$ABAddressBookErrorDomain$",
            "constants_dict": {"ABMultiValueIdentifiersErrorKey": "@"},
            "enums": "$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$",
            "functions": {
                "ABPersonSetImageData": (objc._C_BOOL + objc._C_ID + objc._C_ID, "", {})
            },
            "aliases": {"doc_string": "__doc__"},
            "expressions": {"mysum": "NSAWTEventType + NSAboveBottom + 3"},
        }

        mod = objc.ObjCLazyModule(
            "RootLess", None, None, metadict, None, initial_dict, ()
        )

        self.assertEqual(mod.__doc__, "rootless test module")
        self.assertEqual(mod.__doc__, mod.doc_string)
        self.assertIs(mod.__spec__, initial_dict["__spec__"])
        self.assertIs(mod.__loader__, initial_dict["__loader__"])
        self.assertEqual(mod.NSAboveBottom, 4)
        self.assertEqual(mod.mysum, mod.NSAWTEventType + mod.NSAboveBottom + 3)
        self.assertRaises(AttributeError, getattr, mod, "ABPersonSetImageData")
        self.assertRaises(AttributeError, getattr, mod, "ABAddressBookErrorDomain")
        self.assertRaises(
            AttributeError, getattr, mod, "ABMultiValueIdentifiersErrorKey"
        )

    def test_with_parents(self):
        mod = objc.ObjCLazyModule("RootLess", None, None, None, None, None, (sys, os))

        self.assertEqual(mod.path, sys.path)
        self.assertIn("path", mod.__dict__)
        self.assertEqual(mod.unlink, os.unlink)
        self.assertIn("unlink", mod.__dict__)

        mod.__dict__["version_info"] = 42
        self.assertEqual(mod.version_info, 42)

        self.assertIn("walk", mod.__all__)
        self.assertIn("version", mod.__all__)
        self.assertNotIn("__doc__", mod.__all__)

    def test_all_clearing(self):
        metadict = {"enums": "$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$"}

        initial_dict = {"__doc__": "AppKit test module"}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            metadict,
            None,
            initial_dict,
            (sys,),
        )
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        mod.__all__ = 42
        self.assertIs(mod.path, sys.path)
        self.assertNotIn("__all__", mod.__dict__)

        mod.__all__ = 42
        self.assertEqual(mod.NSAWTEventType, 16)
        self.assertNotIn("__all__", mod.__dict__)

        mod.__all__ = 42
        self.assertIs(mod.NSObject, objc.lookUpClass("NSObject"))
        self.assertNotIn("__all__", mod.__dict__)

        self.assertTrue("NSAWTEventType" in mod.__all__)
        self.assertTrue("NSAboveBottom" in mod.__all__)

    def test_enum_formats(self):
        metadict = {"enums": "$intval@16$floatval@4.5$charval@'1234'$floatval2@1e3$"}

        initial_dict = {"__doc__": "AppKit test module"}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            metadict,
            None,
            initial_dict,
            (),
        )
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        self.assertEqual(mod.intval, 16)
        self.assertEqual(mod.floatval, 4.5)
        self.assertEqual(mod.charval, struct.unpack(">l", b"1234")[0])
        self.assertEqual(mod.floatval2, 1.0e3)

    def test_magic_aliases(self):
        metadict = {
            "aliases": {"umax": "ULONG_MAX", "max": "LONG_MAX", "min": "LONG_MIN"}
        }

        initial_dict = {"__doc__": "AppKit test module"}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            metadict,
            None,
            initial_dict,
            (),
        )
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        self.assertEqual(mod.umax, 2 ** 64 - 1)
        self.assertEqual(mod.max, sys.maxsize)
        self.assertEqual(mod.min, -sys.maxsize - 1)

    def test_existing_submodules(self):
        try:
            sys.modules["MyFramework.submodule"] = 42
            sys.modules["MyFramework.submodule.x"] = 99
            sys.modules["MyFramework.submodule2"] = 1
            sys.modules["MyFramework.submodule3"] = None
            mod = objc.ObjCLazyModule("MyFramework", None, None, {}, None, {}, ())
            self.assertIsInstance(mod, objc.ObjCLazyModule)
            self.assertEqual(mod.submodule, 42)
            self.assertEqual(mod.submodule2, 1)
            self.assertRaises(KeyError, operator.getitem, mod.__dict__, "submodule3")
            self.assertRaises(KeyError, operator.getitem, mod.__dict__, "submodule.x")
        finally:
            for nm in (
                "MyFramework.submodule",
                "MyFramework.submodule.x",
                "MyFramework.submodule2",
            ):
                if nm in sys.modules:
                    del sys.modules[nm]

    def test_inline_list(self):
        # Use inlinetab from PyObjCTest.metadatafunction extension
        # -> Also check that '__all__' processing loads inline functions!
        metadict = {
            "functions": {
                "makeArrayWithFormat_": (
                    b"@@",
                    "",
                    {"variadic": True, "arguments": {0: {"printf_format": True}}},
                ),
                "makeArrayWithCFormat_": (
                    b"@*",
                    "",
                    {"variadic": True, "arguments": {0: {"printf_format": True}}},
                ),
                "make4Tuple_": (
                    b"@^d",
                    "",
                    {
                        "arguments": {
                            0: {
                                "type_modifier": objc._C_IN,
                                "c_array_of_fixed_length": 4,
                                "null_accepted": False,
                            }
                        }
                    },
                ),
                "NoSuchFunction": (b"@d", "", {}),
            }
        }

        inline_list = metadatafunction.function_list
        mod = objc.ObjCLazyModule(
            "MyFramework", None, None, metadict, inline_list, {}, ()
        )
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        self.assertIsInstance(mod.makeArrayWithFormat_, objc.function)
        v = mod.makeArrayWithFormat_("%3d", 10)
        self.assertEqual(list(v), ["%3d", " 10"])
        self.assertRaises(AttributeError, getattr, mod, "NoSuchFunction")

        mod.make4Tuple_ = 42
        self.assertIn("makeArrayWithFormat_", mod.__all__)
        self.assertIn("makeArrayWithCFormat_", mod.__all__)
        self.assertEqual(mod.make4Tuple_, 42)

    def test_cftype(self):
        metadict = {
            "cftypes": [
                ("CFAllocatorRef", b"^{__CFAllocator=}", "CFAllocatorGetTypeID", None),
                (
                    "CFArrayRef",
                    b"^{__CFArray=}",
                    "CFArrayGetTypeID",
                    "DoesNotExist,NSArray",
                ),
                (
                    "CFAttributedStringRef",
                    b"^{__CFAttributedString=}",
                    "CFAttributedStringGetTypeID",
                    "__NSCFAttributedString,NSCFAttributedString",
                ),
                ("CFBagRef", b"^{__CFBag=}", "xCFBagGetTypeID", None),
                ("CFNoType", b"^{__CFNoType", "CFNoTypeGetTypeID", "DoesNotExist"),
            ],
            "functions": {
                "CFAllocatorGetTypeID": (objc._C_NSUInteger, ""),
                "CFArrayGetTypeID": (objc._C_NSUInteger, ""),
            },
            "constants": "$kCFAllocatorDefault@=^{__CFAllocator=}$kCFAllocatorMalloc@=^{__CFAllocator=}$kCFAllocatorMissing@=^{__CFAllocator=}$",  # noqa: B950
            "constants_dict": {
                "kCFAllocatorSystemDefault": "=^{__CFAllocator=}",
                "kCFAllocatorMallocZone": "=^{__CFAllocator=}",
                "kCFAllocatorMissingZone": "=^{__CFAllocator=}",
                "kCFAllocatorMissingOtherZone": "=^{__CFAllocator=}",
            },
        }
        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/CoreFoundation.framework",
            metadict,
            None,
            {},
            (),
        )

        # Ensure that all types are loaded:
        self.assertIn("CFAllocatorRef", mod.__dict__)
        self.assertIn("CFArrayRef", mod.__dict__)
        self.assertIn("CFAttributedStringRef", mod.__dict__)
        self.assertIn("CFBagRef", mod.__dict__)
        self.assertNotIn("CFNoType", mod.__dict__)

        # Type validation:
        self.assertIn("NSCFType", mod.CFAllocatorRef.__bases__[0].__name__)
        self.assertIs(mod.CFArrayRef, objc.lookUpClass("NSArray"))
        self.assertIn(
            mod.CFAttributedStringRef,
            lookupClasses("NSCFAttributedString", "__NSCFAttributedString"),
        )
        self.assertIn("NSCFType", mod.CFBagRef.__name__)
        self.assertIsNot(mod.CFBagRef, mod.CFAllocatorRef)

        # Tests for 'magic cookie' constants:
        self.assertIsInstance(mod.kCFAllocatorDefault, objc.objc_object)
        self.assertTrue((mod.kCFAllocatorDefault.__flags__ & 0x10) == 0x10)
        self.assertIsInstance(mod.kCFAllocatorDefault, mod.CFAllocatorRef)

        self.assertIsInstance(mod.kCFAllocatorSystemDefault, objc.objc_object)
        self.assertTrue((mod.kCFAllocatorSystemDefault.__flags__ & 0x10) == 0x10)
        self.assertIsInstance(mod.kCFAllocatorSystemDefault, mod.CFAllocatorRef)

        self.assertRaises(AttributeError, getattr, mod, "kCFAllocatorMissing")
        self.assertRaises(AttributeError, getattr, mod, "kCFAllocatorMissingZone")

        self.assertIn("kCFAllocatorDefault", mod.__all__)
        self.assertIn("kCFAllocatorSystemDefault", mod.__all__)
        self.assertIn("kCFAllocatorMallocZone", mod.__all__)
        self.assertIn("kCFAllocatorMalloc", mod.__all__)
        self.assertRaises(AttributeError, getattr, mod, "kCFAllocatorOtherMissingZone")

        self.assertIsInstance(mod.kCFAllocatorMalloc, objc.objc_object)
        self.assertTrue((mod.kCFAllocatorMalloc.__flags__ & 0x10) == 0x10)
        self.assertIsInstance(mod.kCFAllocatorMalloc, mod.CFAllocatorRef)

        self.assertIsInstance(mod.kCFAllocatorMallocZone, objc.objc_object)
        self.assertTrue((mod.kCFAllocatorMallocZone.__flags__ & 0x10) == 0x10)
        self.assertIsInstance(mod.kCFAllocatorMallocZone, mod.CFAllocatorRef)
