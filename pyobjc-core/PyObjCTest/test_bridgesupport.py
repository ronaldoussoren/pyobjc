from PyObjCTools.TestSupport import *

import objc._bridgesupport as bridgesupport
import os
import re

import xml.etree.ElementTree as ET 


try:
    basestring
except NameError:
    basestring = str

try:
    long
except NameError:
    long = int

IDENTIFIER=re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

# XXX: add all supported metadata to TEST_XML, validate in test_xml_structure
TEST_XML="""\
<signatures>
  <unknown><!-- ignore -->
    <enum name='nested1' value='4' /><!-- should be ignored -->
  </unknown>
  <opaque name='opaque1' type='^{opaque1}'/>
  <opaque name='opaque2' type='^{opaque2=f}' type64='^{opaque2=d}' />
  <opaque type='^{opaque2=f}' type64='^{opaque2=d}' /><!-- ignore -->
  <opaque name='opaque3' /><!-- ignore -->
  <opaque name='opaque4' type64='^{opaque2=d}' /><!-- ignore 32-bit -->
  <opaque /><!-- ignore -->
  <constant name='constant1' type='@'/>
  <constant name='constant2' type='I' type64='Q' />
  <constant type='@'/><!-- ignore -->
  <constant name='constant3' /><!-- ignore -->
  <constant name='constant2' type64='Q' /><!-- ignore 32-bit -->
  <constant /><!-- ignore -->
  <string_constant name='strconst1' value='string constant1' />
  <string_constant name='strconst2' value='string constant 2' value64='string constant two' />
  <string_constant name='strconst1u' value='string constant1 unicode' nsstring='true' />
  <string_constant name='strconst2u' value='string constant 2 unicode' value64='string constant two unicode' nsstring='true' />
  <string_constant name='strconst3' /><!-- ignore -->
  <string_constant name='strconst4' nsstring='true' /><!-- ignore -->
  <string_constant name='strconst5' value64='string five' /><!-- ignore 32-bit -->
  <string_constant name='strconst5' value64='string five unicode' nsstring='true' /><!-- ignore 32-bit -->
  <string_constant /><!-- ignore -->
  <enum name='enum1' value='1' />
  <enum name='enum2' value='3' value64='4'/>
  <enum name='enum3' le_value='5' be_value64='6'/>
  <enum name='enum4' value='7' be_value='8' /><!-- should have value 7 -->
  <enum name='enum5' /><!-- ignore -->
  <enum value='3' value64='4'/><!-- ignore -->
  <enum name='enum6' value64='4'/><!-- ignore 32-bit -->
  <enum name='enum7' be_value64='6' /><!-- ignore intel -->
  <enum name='enum8' le_value='5' /><!-- ignore ppc -->
  <enum /><!-- ignore -->
  <null_constant name='null1' />
  <null_constant /><!-- ignore -->
  <function_pointer name='func1' orginal='orig_function' />
  <function_pointer name='func2' /><!-- ignore -->
  <function_pointer original='func3' /><!-- ignore -->
  <function_pointer /><!-- ignore -->
  <cftype name='CFProxy1Ref' type='^{CFProxy}' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy2Ref' type='^{CFProxy32}' type64='^{CFProxy64}' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy3Ref' type='^{CFProxy3}' tollfree='NSProxy' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy4Ref' type='^{CFProxy4}' tollfree='NSProxy2' />
  <cftype name='CFProxy5Ref' type='^{CFProxy}' gettypeid_func='NoSuchFunction' /><!-- tollfree to CFTypeRef -->
  <cftype name='CFProxy6Ref' type='^{CFProxy}' /><!-- ignore: no typeid -->
  <cftype name='CFProxy7Ref' type='^{CFProxy32}' type64='^{CFProxy64}' /><!-- ignore: no typeid -->
  <cftype type='^{CFProxy}' gettypeid_func='CFArrayGetTypeID' /><!-- ignore -->
  <cftype name='CFProxy8Ref' gettypeid_func='CFArrayGetTypeID' /><!-- ignore -->
  <cftype name='CFProxy9Ref' type64='^{CFProxy64}' gettypeid_func='CFArrayGetTypeID' /><!-- ignore 32-bit -->
  <cftype/><!-- ignore -->
  <class name='MyClass1'></class>
  <class /><!-- ignore -->
  <class name='MyClass2'>
    <method selector='method1'></method>
    <method selector='method2' variadic='true' ></method>
    <method selector='method3' variadic='true' c_array_delimited_by_null='true'></method>
    <method selector='method4' variadic='true' c_array_length_in_arg='4'></method>
    <method selector='method5' c_array_delimited_by_null='true'><retval type='d'/></method><!-- c_array... ignored -->
    <method selector='method6' c_array_length_in_arg='4'><retval type='d' /></method><!-- c_array... ignored -->
    <method selector='method7' ignore='true'></method>
    <method selector='method8' ignore='true' suggestion='ignore me'></method>
    <method selector='method9' suggestion='ignore me'><retval type='d'/></method><!-- suggestion ignored -->
    <method selector='method10'>
       <retval type='d'/>
    </method>
    <method selector='method11'>
       <retval type='f' type64='d' />
    </method>
    <method selector='method12'>
       <retval/><!-- ignore -->
    </method>
    <method selector='method13'>
       <retval type_modifier='n' />
    </method>
    <method selector='method13'>
       <retval sel_of_type='v@:f' c_array_of_fixed_length='4'/>
    </method>
    <method selector='method14'>
       <retval sel_of_type='v@:f' sel_of_type64='v@:d' />
    </method>
    <method selector='method15'>
       <retval null_accepted='false' already_retained='true' already_cfretained='false' c_array_length_in_result='true' />
    </method>
    <method selector='method16'>
       <retval c_array_delimited_by_null='true' c_array_of_variable_length='false' printf_format='true' free_result='true' />
    </method>
    <method selector='method17'>
       <retval c_array_lenght_in_arg='1'/>
    </method>
    <method selector='method18'>
       <retval c_array_lenght_in_arg='1,2'/>
    </method>
    <method selector='method19'>
       <retval c_array_lenght_in_arg='4, 5'/>
    </method>
    <method selector='method20'>
       <retval function_pointer_retained='true'/><!-- ignored, no function data -->
    </method>
    <method selector='method21'>
       <retval function_pointer_retained='true' function_pointer='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </retval>
    </method>
    <method selector='method22'>
       <retval function_pointer_retained='true' block='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </retval>
    </method>
    <method selector='method23'>
       <retval function_pointer='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </retval>
    </method>
    <method selector='method24'>
       <retval block='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </retval>
    </method>
    <!-- TODO: 'argument' and 'retval' nodes -->
    <method ></method><!-- ignore -->
    <method variadic='true'></method><!-- ignore -->
    <method ignore='true'></method><!-- ignore -->
  </class>
  <function/><!-- TODO -->
  <informal_protocol/><!-- TODO: no name, empty, methods -->
  <struct/><!-- TODO -->
  <!-- TODO: type rewriting (_C_BOOL, _C_NSBOOL)-->
</signatures>
"""

# XXX: add unsupported variants

class TestBridgeSupport (TestCase):
    def testInvalidToplevel(self):
        self.assertRaises(objc.error, bridgesupport._BridgeSupportParser, '<signatures2></signatures2>', 'Cocoa')
        self.assertRaises(ET.ParseError, bridgesupport._BridgeSupportParser, '<signatures2></signatures>', 'Cocoa')

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

    def test_xml_structure(self):
        prs = self.assert_valid_bridgesupport('TestXML', TEST_XML)

        self.fail("validate the metadata from TEST_XML")

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
            "c_array_length_in_result",
            "c_array_delimited_by_null",
            "printf_format",
            "null_accepted",
            "c_array_of_variable_length",
            "c_array_length_in_arg",
            "c_array_of_fixed_length",
            "sel_of_type",
            "callable",
            "callable_retained",
            "free_result",
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

            if "free_result" in meta["retval"]:
                self.assertIsInstance(meta["retval"]["free_result"], bool)

            for key in ("c_array_length_in_arg", "c_array_of_fixed_length"):
                if key in meta["retval"]:
                    self.assertIsInstance(meta["retval"][key], (int, long))

            for key in ("c_array_delimited_by_null", "printf_format", "c_array_of_variable_length", "null_accepted"):
                if key in meta["retval"]:
                    self.assertIsInstance(meta["retval"][key], bool)


            self.assertNotIn("c_array_length_in_result", meta["retval"])
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

            if "free_result" in arg:
                self.assertIsInstance(arg["free_result"], bool)

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
                        "null_accepted", "c_array_length_in_result"):
                if key in arg:
                    self.assertIsInstance(arg[key], bool)

            self.assertEqual(set(arg) - valid_keys, set())

        if "suggestion" in meta:
            self.assertIsInstance(meta["suggestion"], basestring)

        if "variadic" in meta:
            self.assertIsInstance(meta["variadic"], bool)

        if "variadic" in meta and meta["variadic"]:
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
                arg = meta["arguments"][idx]
                if "printf_format" in arg and arg["printf_format"]:
                    if found:
                        self.fail("meta for variadic with two ways to determine size: %s"%(meta,))
                    found = True

            # NOTE: disabled because having unsupported variadic methods would be fine (e.g.
            #       metadata says the method is variadic, but it doesn't fall into one of the
            #       supported categories)
            #if not found:
            #    self.fail("meta for variadic without method for determining size: %s"%(meta,))

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

        return prs


if __name__ == "__main__":
    main()
