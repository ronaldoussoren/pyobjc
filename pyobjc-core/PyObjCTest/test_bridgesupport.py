from PyObjCTools.TestSupport import *

import objc._bridgesupport as bridgesupport
import os
import re

try:
    basestring
except NameError:
    basestring = str

try:
    long
except NameError:
    long = int

IDENTIFIER=re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

class TestSystemBridgeSupport (TestCase):

    def iter_framework_dir(self, framework_dir):
        for dn in os.listdir(framework_dir):
            fn = os.path.join(framework_dir, dn, 'Resources', 'BridgeSupport', dn.replace('.framework', '.bridgesupport'))
            if os.path.exists(fn):
                yield fn

            fn = os.path.join(framework_dir, dn, 'Frameworks')
            if os.path.exists(fn):
                for item in self.iter_framework_dir(fn):
                    yield item

    def iter_system_bridgesupport_files(self):
        for item in self.iter_framework_dir('/System/Library/Frameworks'):
            yield item

    def test_system_bridgesupport(self):
        with filterWarnings("ignore", RuntimeWarning):
            # Check that all system bridgesupport files can be processed correctly
            for fn in self.iter_system_bridgesupport_files():
                with open(fn, 'r') as fp:
                    xmldata = fp.read()

                self.assert_valid_bridgesupport(os.path.basename(fn).split('.')[0], xmldata)



    def assertIsIdenfier(self, value):
        m = IDENTIFIER.match(value)
        if m is None:
            self.fail("'%s' is not an identifier"%(value,))


    def assert_valid_callable(self, meta, function):
        if function:
            self.assertIn("arguments", meta)
            indexes = list(sorted(meta["arguments"]))
            self.assertEqual(indexes, list(range(len(indexes))))

        valid_keys = { 
            "type",
            "type_modifier",
            "already_retained",
            "already_cfretained",
            "c_array_length_in_retval",
            "c_array_delimited_by_null",
            "printf_format",
            "null_accepted",
            "c_array_of_variable_length",
            "c_array_length_in_arg",
            "c_array_of_fixed_length",
            "sel_of_type",
            "callable",
            "callable_retained",
        }

        if "retval" in meta:
            if "type" in meta["retval"]:
                self.assertIsInstance(meta["retval"]["type"], bytes)
                self.assertEqual(len(objc.splitSignature(meta["retval"]["type"])), 1)

            if "type_modifier" in meta["retval"]:
                self.assertIsInstance(meta["retval"]["type_modifier"], bytes)
                self.assertIn(meta["retval"]["type_modifier"], [b"o", b"n", b"N"])

            if "callable" in meta["retval"]:
                self.assert_valid_callable(meta["retval"]["callable"], True)
                if "callable_retained" in meta["retval"]:
                    self.assertIsInstance(meta["retval"]["callable_retained"], bool)
            else:
                self.assertNotIn("callable_retained", meta["retval"])

            if "sel_of_type" in meta["retval"]:
                split = objc.splitSignature(meta["retval"]["sel_of_type"])
                self.assertEqual(split[1], objc._C_ID)
                self.assertEqual(split[2], objc._C_SEL)

            if "already_retained" in meta["retval"]:
                self.assertIsInstance(meta["retval"]["already_retained"], bool)
                self.assertNotIn("already_cfretained", meta["retval"])

            if "already_cfretained" in meta["retval"]:
                self.assertIsInstance(meta["retval"]["already_cfretained"], bool)

            for key in ("c_array_length_in_arg", "c_array_of_fixed_length"):
                if key in meta["retval"]:
                    self.assertIsInstance(meta["retval"][key], (int, long))

            for key in ("c_array_delimited_by_null", "printf_format", "c_array_of_variable_length", "null_accepted"):
                if key in meta["retval"]:
                    self.assertIsInstance(meta["retval"][key], bool)


            self.assertNotIn("c_array_length_in_retval", meta["retval"])
            self.assertEqual(set(meta["retval"]) - valid_keys, set())

        for idx in meta["arguments"]:
            self.assertIsInstance(idx, (int, long))
            arg = meta["arguments"][idx]

            if "type" in arg:
                self.assertIsInstance(arg["type"], bytes)
                self.assertEqual(len(objc.splitSignature(arg["type"])), 1)

            if "type_modifier" in arg:
                self.assertIsInstance(arg["type_modifier"], bytes)
                self.assertIn(arg["type_modifier"], [b"o", b"n", b"N"])

            if "callable" in arg:
                self.assert_valid_callable(arg["callable"], True)
                if "callable_retained" in arg:
                    self.assertIsInstance(arg["callable_retained"], bool)
            else:
                self.assertNotIn("callable_retained", arg)

            if "sel_of_type" in arg:
                split = objc.splitSignature(arg["sel_of_type"])
                self.assertEqual(split[1], objc._C_ID)
                self.assertEqual(split[2], objc._C_SEL)

            if "already_retained" in arg:
                self.assertIsInstance(arg["already_retained"], bool)
                self.assertNotIn("already_cfretained", arg)

            if "already_cfretained" in arg:
                self.assertIsInstance(arg["already_cfretained"], bool)

            if "c_array_of_fixed_length" in arg:
                self.assertIsInstance(arg["c_array_of_fixed_length"], (int, long))

            if "c_array_length_in_arg" in arg:
                if isinstance(arg["c_array_length_in_arg"], (int, long)):
                    pass

                else:
                    self.assertIsInstance(arg["c_array_length_in_arg"], tuple)
                    self.assertEqual(len(arg["c_array_length_in_arg"]), 2)
                    for x in arg["c_array_length_in_arg"]:
                        self.assertIsInstance(x, (int, long))


            for key in ("c_array_delimited_by_null", "printf_format", "c_array_of_variable_length", 
                        "null_accepted", "c_array_length_in_retval"):
                if key in arg:
                    self.assertIsInstance(arg[key], bool)

            self.assertEqual(set(arg) - valid_keys, set())

        if "suggestion" in meta:
            self.assertIsInstance(meta["suggestion"], basestring)

        if "variadic" in meta:
            self.assertIsInstance(meta["variadic"], bool)

        if "varidic" in meta and meta["variadic"]:
            self.assertEqual(set(meta.keys()) - {"arguments", "retval", "variadic", 
                    "c_array_length_in_arg", "c_array_delimited_by_null", "suggestion"}, set())

            found = False
            if "c_array_length_in_arg" in meta:
                self.assertIsInstance(meta["c_array_length_in_arg"], (int, long))
                self.assertNotIn("c_array_delimited_by_null", meta)
                found = True

            if "c_array_delimited_by_null" in meta:
                self.assertIsInstance(meta["c_array_delimited_by_null"], bool)
                found = False

            for idx in meta.get("arguments", {}):
                arg = meta["arguments"]["idx"]
                if "printf_format" in arg and arg["print_format"]:
                    if found:
                        self.fail("meta for variadic with two ways to determine size: %s"%(meta,))
                    found = True

            if not found:
                self.fail("meta for variadic without method for deteriming size: %s"(meta,))

        else:
            self.assertEqual(set(meta.keys()) - {"arguments", "retval", "variadic", "suggestion" }, set())

    def assert_valid_bridgesupport(self, framework_name, xmldata):
        prs = bridgesupport._BridgeSupportParser(xmldata, framework_name)

        for item in prs.cftypes:
            if len(item) == 3:
                name, encoding, typeId = item
                tollfreeName = None

            elif len(item) == 4:
                name, encoding, typeId, tollfreeName = item
                self.assertIsNot(tollfreeName, None)


            else:
                self.fail("Wrong item length in cftypes: %s"%(item,))

            self.assertIsInstance(name, basestring)
            self.assertIsInstance(encoding, bytes)
            self.assertEqual(len(objc.splitSignature(encoding)), 1)
            if tollfreeName is None:
                self.assertIsInstance(typeId, (int, long))

            else:
                self.assertIs(typeId, None)
                self.assertIsInstance(tollfreeName, basestring)

        for name, typestr, magic in prs.constants:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(typestr, bytes)
            self.assertIsInstance(magic, bool)
            self.assertEqual(len(objc.splitSignature(typestr)), 1)

        for name, orig in prs.func_aliases:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(orig, basestring)
            self.assertIsIdentifier(name)

        for name, encoding, doc, meta in prs.functions:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(encoding, bytes)

            # check that signature string is well-formed:
            objc.splitSignature(encoding)

            self.assertEqual(doc, "")
            self.assertIsInstance(meta, dict)
            self.assert_valid_callable(meta, function=True)

        for name, method_list in prs.informal_protocols:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(method_list, list)
            for sel in method_list:
                self.assertIsInstance(sel, objc.selector)
                self.assertIs(sel.callable, None)

        for clsname, selname in prs.meta:
            meta = prs.meta[(clsname, selname)]
            self.assertIsInstance(clsname, bytes)
            self.assertIsInstance(selname, bytes)
            self.assertIsInstance(meta, dict)
            self.assert_valid_callable(meta, function=False)

        for name, typestr in prs.opaque:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(typestr, bytes)

            self.assertEqual(len(objc.splitSignature(typestr)), 1)

        for name, typestr in prs.structs:
            self.assertIsInstance(name, basestring)
            self.assertIsInstance(typestr, bytes)

            self.assertEqual(len(objc.splitSignature(typestr)), 1)

        for name in prs.values:
            self.assertIsInstance(prs.values[name], (basestring, long, int, float, bytes))


if __name__ == "__main__":
    main()
