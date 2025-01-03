import os
import struct
import sys
import copy
import warnings

import objc
import objc._lazyimport as lazyimport
from PyObjCTest import metadatafunction
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.test_deprecations import deprecation_warnings


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

        # Uses an invalid identifier on purpuse to force fallback to path.
        o = lazyimport._loadBundle(
            "PreferencePanes",
            "com.apple.frameworks.xxpreferencepanes",
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

        with self.assertRaisesRegex(AttributeError, "Foo"):
            mod.Foo
        with self.assertRaisesRegex(AttributeError, "Foo"):
            mod.Foo
        with self.assertRaisesRegex(AttributeError, "42"):
            getattr(mod, "42")

        if dunder_all:
            # Force precalculation of all attributes by accessing the __all__
            # attribute
            self.assertEqual(set(dir(mod)), set(mod.__all__))

        self.assertEqual(mod.__doc__, initial_dict["__doc__"])
        self.assertEqual(mod.doc_string, initial_dict["__doc__"])
        with self.assertRaisesRegex(AttributeError, "invalid_alias"):
            mod.invalid_alias
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
        with self.assertRaisesRegex(AttributeError, "FunctionThatDoesNotExist"):
            mod.FunctionThatDoesNotExist
        self.assertEqual(mod.mysum, mod.NSAWTEventType + mod.NSAboveBottom + 3)
        with self.assertRaisesRegex(AttributeError, "invalid_expression1"):
            mod.invalid_expression1
        with self.assertRaisesRegex(AttributeError, "invalid_expression2"):
            mod.invalid_expression2
        self.assertIs(mod.NSURL, objc.lookUpClass("NSURL"))
        with self.assertRaisesRegex(AttributeError, "NSNonExistingClass"):
            mod.NSNonExistingClass

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

    def test_nameless_enum_label(self):
        # XXX: This tests a workaround for a bug in libdispatch, to
        #      be removed later.
        initial_dict = {
            "__doc__": "rootless test module",
            "__spec__": object(),
            "__loader__": object(),
        }
        metadict = {
            "enums": "$$NSAWTEventType@16$$@4@",
            "constants": "$$",
        }

        mod = objc.ObjCLazyModule(
            "RootLess", None, None, metadict, None, initial_dict, ()
        )

        self.assertIn("NSAWTEventType", mod.__all__)
        self.assertNotIn("", mod.__all__)

    def test_without_framework(self):
        initial_dict = {
            "__doc__": "rootless test module",
            "__spec__": object(),
            "__loader__": object(),
        }
        metadict = {
            "constants": "$AEAssessmentErrorDomain$",
            "constants_dict": {"ITLibMediaEntityPropertyPersistentID": "@"},
            "enums": "$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$",
            "functions": {
                "ABPersonSetImageData": (
                    objc._C_BOOL + objc._C_ID + objc._C_ID,
                    "",
                    {},
                ),
                "MTLTextureSwizzleChannelsMake": (
                    b"{_MTLTextureSwizzleChannels=CCCC}CCCC",
                ),
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
        with self.assertRaisesRegex(AttributeError, "MTLTextureSwizzleChannelsMake"):
            mod.MTLTextureSwizzleChannelsMake
        with self.assertRaisesRegex(AttributeError, "AEAssessmentErrorDomain"):
            mod.AEAssessmentErrorDomain
        with self.assertRaisesRegex(
            AttributeError, "ITLibMediaEntityPropertyPersistentID"
        ):
            mod.ITLibMediaEntityPropertyPersistentID

    def test_function_wont_override_existing(self):
        metadict = {
            "functions": {
                "CFAllocatorGetTypeID": (objc._C_NSUInteger, ""),
                "CFArrayGetTypeID": (objc._C_NSUInteger, ""),
            },
        }
        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/CoreFoundation.framework",
            metadict,
            None,
            {"CFAllocatorGetTypeID": 42},
            (),
        )

        self.assertEqual(mod.CFAllocatorGetTypeID, 42)
        self.assertIn("CFAllocatorGetTypeID", mod.__all__)
        self.assertIn("CFArrayGetTypeID", mod.__all__)
        self.assertEqual(mod.CFAllocatorGetTypeID, 42)

    def test_inline_function_wont_override_existing(self):
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
            }
        }

        inline_list = metadatafunction.function_list
        mod = objc.ObjCLazyModule(
            "MyFramework",
            None,
            None,
            metadict,
            inline_list,
            {
                "makeArrayWithFormat_": 42,
            },
            (),
        )

        self.assertEqual(mod.makeArrayWithFormat_, 42)
        self.assertIn("makeArrayWithFormat_", mod.__all__)
        self.assertIn("makeArrayWithCFormat_", mod.__all__)
        self.assertEqual(mod.makeArrayWithFormat_, 42)

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
            "aliases": {
                "umax": "ULONG_MAX",
                "max": "LONG_MAX",
                "min": "LONG_MIN",
                "dblmx": "DBL_MAX",
                "dblmn": "DBL_MIN",
                "dbleps": "DBL_EPSILON",
                "fltmx": "FLT_MAX",
                "fltmn": "FLT_MIN",
                "null": "objc.NULL",
                "umx": "UINT32_MAX",
            }
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

        self.assertEqual(mod.umax, 2**64 - 1)
        self.assertEqual(mod.max, sys.maxsize)
        self.assertEqual(mod.min, -sys.maxsize - 1)
        self.assertEqual(mod.dblmx, sys.float_info.max)
        self.assertEqual(mod.dblmn, sys.float_info.min)
        self.assertEqual(mod.dbleps, sys.float_info.epsilon)
        self.assertEqual(mod.fltmx, objc._FLT_MAX)
        self.assertEqual(mod.fltmn, objc._FLT_MIN)
        self.assertEqual(mod.null, objc.NULL)
        self.assertEqual(mod.umx, 2**32 - 1)

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
            with self.assertRaisesRegex(KeyError, "submodule3"):
                mod.__dict__["submodule3"]
            with self.assertRaisesRegex(KeyError, "x"):
                mod.__dict__["submodule.x"]
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
        with self.assertRaisesRegex(AttributeError, "NoSuchFunction"):
            mod.NoSuchFunction

        mod.make4Tuple_ = 42
        self.assertIn("makeArrayWithFormat_", mod.__all__)
        self.assertIn("makeArrayWithCFormat_", mod.__all__)
        self.assertEqual(mod.make4Tuple_, 42)

    def test_inline_list__all__(self):
        # Check __all__ handling for inline functions
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
        mod.__dict__["makeArrayWithFormat_"] = 42
        mod.__dict__["make4Tuple_"] = 43

        self.assertIn("makeArrayWithFormat_", mod.__all__)
        self.assertIn("makeArrayWithCFormat_", mod.__all__)
        self.assertIn("make4Tuple_", mod.__all__)

        self.assertEqual(mod.makeArrayWithFormat_, 42)
        self.assertEqual(mod.make4Tuple_, 43)
        self.assertIsInstance(mod.makeArrayWithCFormat_, objc.function)

    def test_cftype(self):
        # XXX: Need test for a magic cookie constant for a type that is unknown to the bridge
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
            "constants": "$kCFAllocatorDefault@=^{__CFAllocator=}$"
            "kCFAllocatorMalloc@=^{__CFAllocator=}$kCFAllocatorMissing@=^{__CFAllocator=}$",  # noqa: B950
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
        self.assertIsInstance(repr(mod.kCFAllocatorDefault), str)
        self.assertIn("magic instance", repr(mod.kCFAllocatorDefault))

        # XXX: These need to be in a different test file
        self.assertTrue(mod.kCFAllocatorDefault.__pyobjc_magic_coookie__)
        self.assertTrue(mod.kCFAllocatorDefault == mod.kCFAllocatorDefault)
        self.assertFalse(mod.kCFAllocatorDefault != mod.kCFAllocatorDefault)
        self.assertTrue(mod.kCFAllocatorDefault != mod.CFBagRef)
        self.assertFalse(mod.kCFAllocatorDefault == mod.CFBagRef)
        with self.assertRaisesRegex(
            TypeError,
            "'<' not supported between instances of 'CFAllocatorRef' and 'CFAllocatorRef'",
        ):
            mod.kCFAllocatorDefault < mod.kCFAllocatorDefault  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'<=' not supported between instances of 'CFAllocatorRef' and 'CFAllocatorRef'",
        ):
            mod.kCFAllocatorDefault <= mod.kCFAllocatorDefault  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'>' not supported between instances of 'CFAllocatorRef' and 'CFAllocatorRef'",
        ):
            mod.kCFAllocatorDefault > mod.kCFAllocatorDefault  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'>=' not supported between instances of 'CFAllocatorRef' and 'CFAllocatorRef'",
        ):
            mod.kCFAllocatorDefault >= mod.kCFAllocatorDefault  # noqa: B015

        self.assertIsInstance(mod.kCFAllocatorSystemDefault, objc.objc_object)
        self.assertTrue((mod.kCFAllocatorSystemDefault.__flags__ & 0x10) == 0x10)
        self.assertIsInstance(mod.kCFAllocatorSystemDefault, mod.CFAllocatorRef)

        with self.assertRaisesRegex(AttributeError, "kCFAllocatorMissing"):
            mod.kCFAllocatorMissing
        with self.assertRaisesRegex(AttributeError, "kCFAllocatorMissingZone"):
            mod.kCFAllocatorMissingZone

        self.assertIn("kCFAllocatorDefault", mod.__all__)
        self.assertIn("kCFAllocatorSystemDefault", mod.__all__)
        self.assertIn("kCFAllocatorMallocZone", mod.__all__)
        self.assertIn("kCFAllocatorMalloc", mod.__all__)
        with self.assertRaisesRegex(AttributeError, "kCFAllocatorOtherMissingZone"):
            mod.kCFAllocatorOtherMissingZone

        self.assertIsInstance(mod.kCFAllocatorMalloc, objc.objc_object)
        self.assertTrue((mod.kCFAllocatorMalloc.__flags__ & 0x10) == 0x10)
        self.assertIsInstance(mod.kCFAllocatorMalloc, mod.CFAllocatorRef)

        self.assertIsInstance(mod.kCFAllocatorMallocZone, objc.objc_object)
        self.assertTrue((mod.kCFAllocatorMallocZone.__flags__ & 0x10) == 0x10)
        self.assertIsInstance(mod.kCFAllocatorMallocZone, mod.CFAllocatorRef)

    def test_magic_objc_does_not_work(self):
        metadict = {
            "constants_dict": {
                "kCFURLUbiquitousItemDownloadingStatusDownloaded": "=@",
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

        with self.assertRaisesRegex(
            ValueError,
            "Don't know CF type for typestr '@', cannot create special wrapper",
        ):
            mod.kCFURLUbiquitousItemDownloadingStatusDownloaded

    def assertDeprecationWarning(self, func):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            func()

        self.assertEqual(len(w), 1)
        self.assertTrue(issubclass(w[-1].category, objc.ApiDeprecationWarning))

    def assertNoDeprecationWarning(self, func):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            func()

        self.assertEqual(len(w), 0)

    def test_deprecations(self):
        metadict = {
            "constants": "$NSWorkspaceMoveOperation$NSWorkspaceCopyOperation@@$",
            "constants_dict": {
                "NSWorkspaceLinkOperation": "@",
                "NSWindowWillCloseNotification": "@",
                "NSUnderlineByWordMask": objc._C_NSUInteger.decode(),
            },
            "enums": "$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$",
            "aliases": {"min": "LONG_MIN", "max": "LONG_MAX"},
            "deprecated_aliases": {
                "min": 1004,
                "max": 1008,
            },
            "deprecated_constants": {
                "NSWorkspaceLinkOperation": 1004,
                "NSWorkspaceMoveOperation": 1008,
            },
            "deprecated_enums": {
                "NSAWTEventType": 1004,
                "NSAboveBottom": 1008,
            },
        }

        def make_mod():
            initial_dict = {"__doc__": "AppKit test module"}

            return objc.ObjCLazyModule(
                "AppKit",
                None,
                "/System/Library/Frameworks/AppKit.framework",
                copy.deepcopy(metadict),
                None,
                initial_dict,
                (),
            )

        with deprecation_warnings("10.3"):
            mod = make_mod()
            self.assertIsInstance(mod, objc.ObjCLazyModule)
            self.assertNoDeprecationWarning(lambda: mod.NSWorkspaceLinkOperation)
            self.assertNoDeprecationWarning(lambda: mod.NSWorkspaceMoveOperation)
            self.assertNoDeprecationWarning(lambda: mod.NSAWTEventType)
            self.assertNoDeprecationWarning(lambda: mod.NSAboveBottom)
            self.assertNoDeprecationWarning(lambda: mod.min)
            self.assertNoDeprecationWarning(lambda: mod.max)

        with deprecation_warnings("10.5"):
            mod = make_mod()
            self.assertIsInstance(mod, objc.ObjCLazyModule)
            self.assertDeprecationWarning(lambda: mod.NSWorkspaceLinkOperation)
            self.assertNoDeprecationWarning(lambda: mod.NSWorkspaceMoveOperation)
            self.assertDeprecationWarning(lambda: mod.NSAWTEventType)
            self.assertNoDeprecationWarning(lambda: mod.NSAboveBottom)
            self.assertDeprecationWarning(lambda: mod.min)
            self.assertNoDeprecationWarning(lambda: mod.max)

        with deprecation_warnings("12"):
            mod = make_mod()
            self.assertIsInstance(mod, objc.ObjCLazyModule)
            self.assertDeprecationWarning(lambda: mod.NSWorkspaceLinkOperation)
            self.assertDeprecationWarning(lambda: mod.NSWorkspaceMoveOperation)
            self.assertDeprecationWarning(lambda: mod.NSAWTEventType)
            self.assertDeprecationWarning(lambda: mod.NSAboveBottom)
            self.assertDeprecationWarning(lambda: mod.min)
            self.assertDeprecationWarning(lambda: mod.max)

    def test_functions_all(self):
        for override in (False, True):
            metadict = {
                "functions": {
                    "LSSharedFileListItemGetTypeID": (b"Q",),
                },
            }
            initial_dict = {"__doc__": "AppKit test module"}

            mod = objc.ObjCLazyModule(
                "AppKit",
                None,
                "/System/Library/Frameworks/AppKit.framework",
                copy.deepcopy(metadict),
                None,
                initial_dict,
                (),
            )

            if override:
                mod.LSSharedFileListItemGetTypeID = 42
                mod.__all__
                self.assertEqual(mod.LSSharedFileListItemGetTypeID, 42)
            else:
                self.assertIsInstance(mod.LSSharedFileListItemGetTypeID, objc.function)

    def do_indirect_magic(self, fetchall):
        metadict = {
            "cftypes": [
                (
                    "LSSharedFileListItemRef",
                    b"^{OpaqueLSSharedFileListItemRef=}",
                    "LSSharedFileListItemGetTypeID",
                    None,
                ),
            ],
            "functions": {
                "LSSharedFileListItemGetTypeID": (b"Q",),
            },
            "constants": "$kLSSharedFileListItemBeforeFirst@==^{OpaqueLSSharedFileListItemRef=}$",
        }
        initial_dict = {"__doc__": "AppKit test module"}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            copy.deepcopy(metadict),
            None,
            initial_dict,
            (),
        )
        if fetchall:
            mod.__all__

        self.assertIsInstance(
            mod.kLSSharedFileListItemBeforeFirst, mod.LSSharedFileListItemRef
        )

    def test_indirect_magic(self):
        self.do_indirect_magic(False)
        self.do_indirect_magic(True)

    def do_indirect_magic_dict(self, fetchall):
        metadict = {
            "cftypes": [
                (
                    "LSSharedFileListItemRef",
                    b"^{OpaqueLSSharedFileListItemRef=}",
                    "LSSharedFileListItemGetTypeID",
                    None,
                ),
            ],
            "functions": {
                "LSSharedFileListItemGetTypeID": (b"Q",),
            },
            "constants_dict": {
                "kLSSharedFileListItemBeforeFirst": "==^{OpaqueLSSharedFileListItemRef=}",
                "kLSSharedFileListItemLaatste": "==^{OpaqueLSSharedFileListItemRef=}",
            },
        }
        initial_dict = {"__doc__": "AppKit test module"}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            copy.deepcopy(metadict),
            None,
            initial_dict,
            (),
        )

        if fetchall:
            mod.__all__

        self.assertIsInstance(
            mod.kLSSharedFileListItemBeforeFirst, mod.LSSharedFileListItemRef
        )
        self.assertNotHasAttr(mod, "kLSSharedFileListItemLaatste")

    def test_indirect_magic_dict(self):
        self.do_indirect_magic_dict(False)
        self.do_indirect_magic_dict(True)

    def test_default_cftype(self):
        metadict = {
            "cftypes": [
                (
                    "LSSharedFileListItemRef",
                    b"^{OpaqueLSSharedFileListItemRef=}",
                    None,
                    None,
                ),
            ],
        }
        initial_dict = {"__doc__": "AppKit test module"}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            copy.deepcopy(metadict),
            None,
            initial_dict,
            (),
        )

        self.assertIn("CFType", mod.LSSharedFileListItemRef.__name__)

    def test_cfstr(self):
        metadict = {"expressions": {"foo": "CFSTR(b'foo')"}}
        initial_dict = {}

        mod = objc.ObjCLazyModule(
            "AppKit",
            None,
            "/System/Library/Frameworks/AppKit.framework",
            copy.deepcopy(metadict),
            None,
            initial_dict,
            (),
        )

        self.assertEqual(mod.foo, "foo")
