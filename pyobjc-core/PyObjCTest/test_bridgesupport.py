try:
    import ctypes
except ImportError:
    ctypes = None
import os
import re
import subprocess
import sys
import warnings
import xml.etree.ElementTree as ET

import objc
import objc._bridgesupport as bridgesupport
from PyObjCTools.TestSupport import (
    TestCase,
    skipUnless,
)

from importlib import reload


IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

TEST_XML = b"""\
<signatures>
  <unknown><!-- ignore -->
    <enum name='nested1' value='4' /><!-- should be ignored -->
  </unknown>
  <opaque name='opaque1' type='^{opaque1}'/>
  <opaque name='opaque2' type='^{opaque2=f}' type64='^{opaque2=d}' />
  <opaque type='^{opaque2=f}' type64='^{opaque2=d}' /><!-- ignore -->
  <opaque name='opaque3' /><!-- ignore -->
  <opaque name='opaque4' type64='^{opaque4=d}' /><!-- ignore 32-bit -->
  <opaque /><!-- ignore -->
  <constant name='constant1' type='@'/>
  <constant name='constant2' type='I' type64='Q' />
  <constant type='@'/><!-- ignore -->
  <constant name='constant3' /><!-- ignore -->
  <constant name='constant4' type64='Q' /><!-- ignore 32-bit -->
  <constant name='constant5' type='B' /><!-- NSBOOL -->
  <constant name='constant6' type='Z' /><!-- bool -->
  <constant name='constant7' type='@' magic_cookie='false' />
  <constant name='constant8' type='@' magic_cookie='true' />
  <constant /><!-- ignore -->
  <constant name='constant9' type='{foo=i?i}' /><!-- ignore: embedded ? -->
  <constant name='constant10' type='{foo={x=?}}' /><!-- ignore: embedded ? -->
  <string_constant name='strconst1' value='string constant1' />
  <string_constant name='strconst2' value='string constant 2' value64='string constant two' />
  <string_constant name='strconst1u' value='string constant1 unicode' nsstring='true' />
  <string_constant name='strconst2u' value='string constant 2 unicode'
      value64='string constant two unicode' nsstring='true' />
  <string_constant name='strconst3' /><!-- ignore -->
  <string_constant name='strconst4' nsstring='true' /><!-- ignore -->
  <string_constant name='strconst5' value64='string five' /><!-- ignore 32-bit -->
  <string_constant name='strconst6' value64='string five unicode'
     nsstring='true' /><!-- ignore 32-bit -->
  <string_constant name='strconst7' value='zee&#0235;n' nsstring='true' />
  <string_constant /><!-- ignore -->
  <string_constant name='strconstinvalid' value='zee&#5235;n'  nsstring='false' />
  <enum name='enum1' value='1' />
  <enum name='enum2' value='3' value64='4'/>
  <enum name='enum3' le_value='5' be_value='6'/>
  <enum name='enum4' value='7' be_value='8' /><!-- should have value 7 -->
  <enum name='enum5' /><!-- ignore -->
  <enum value='3' value64='4'/><!-- ignore -->
  <enum name='enum6' value64='4'/><!-- ignore 32-bit -->
  <enum name='enum7' be_value='6' /><!-- ignore intel -->
  <enum name='enum8' le_value='5' /><!-- ignore ppc -->
  <enum name='enum9' value='2.5' />
  <enum name='enum10' value='0x1.5p+3' />
  <enum name='enum11' value='11.5f' />
  <enum name='enum12' value='12.5F' />
  <enum name='enum13' value='13l' />
  <enum name='enum14' value='14L' />
  <enum name='enum_posinf' value='+inf' />
  <enum name='enum_posinf2' value='inf' />
  <enum name='enum_neginf' value='-inf' />
  <enum name='enum_nan' value='nan' />
  <enum /><!-- ignore -->
  <enum /><!-- ignore -->
  <null_const name='null1' />
  <null_const /><!-- ignore -->
  <function_pointer name='func1' original='orig_function' />
  <function_pointer name='func2' /><!-- ignore -->
  <function_pointer original='func3' /><!-- ignore -->
  <function_pointer /><!-- ignore -->
  <cftype name='CFProxy1Ref' type='^{CFProxy}' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy2Ref' type='^{CFProxy32}'
    type64='^{CFProxy64}' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy3Ref' type='^{CFProxy3}'
    tollfree='NSProxy' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy4Ref' type='^{CFProxy4}' tollfree='NSProxy2' />
  <cftype name='CFProxy5Ref' type='^{CFProxy}'
    gettypeid_func='NoSuchFunction' /><!-- tollfree to CFTypeRef -->
  <cftype name='CFProxy6Ref' type='^{CFProxy}' />
  <cftype name='CFProxy7Ref' type='^{CFProxy32}' type64='^{CFProxy64}' />
  <cftype type='^{CFProxy}' gettypeid_func='CFArrayGetTypeID' /><!-- ignore -->
  <cftype name='CFProxy8Ref' gettypeid_func='CFArrayGetTypeID' /><!-- ignore -->
  <cftype name='CFProxy9Ref' type64='^{CFProxy64}'
    gettypeid_func='CFArrayGetTypeID' /><!-- ignore 32-bit -->
  <cftype/><!-- ignore -->
  <class name='MyClass1'></class>
  <class /><!-- ignore -->
  <class name='MyClass2'>
    <function name='method.function'></function><!-- ignore, not at toplevel -->
    <method selector='method1' classmethod='true' ></method>
    <method selector='method2' variadic='true' ></method>
    <method selector='method3' variadic='true' c_array_delimited_by_null='true'></method>
    <method selector='method4' variadic='true' c_array_length_in_arg='4'>
    </method>
    <method selector='method5' c_array_delimited_by_null='true'><retval type='d'/>
    </method><!-- c_array... ignored -->
    <method selector='method6' c_array_length_in_arg='4'><retval type='d' /><dummy/>
    </method><!-- c_array... ignored -->
    <method selector='method7' ignore='true'></method>
    <method selector='method8' ignore='true' suggestion='ignore me'>
    </method>
    <method selector='method9' suggestion='ignore me'><retval type='d'/>
    </method><!-- suggestion ignored -->
    <method selector='method10'>
       <retval type='d'/>
    </method>
    <method selector='method11' classmethod='false'>
       <retval type='f' type64='d' />
    </method>
    <method selector='method12' classmethod='true'>
       <retval/><!-- ignore -->
    </method>
    <method selector='method13' class_method='true'>
       <retval type_modifier='n' />
    </method>
    <method selector='method13b' class_method='false'>
       <retval sel_of_type='v@:f' c_array_of_fixed_length='4'/>
    </method>
    <method selector='method14'>
       <retval sel_of_type='v@:f' sel_of_type64='v@:d' />
    </method>
    <method selector='method15'>
       <retval null_accepted='false' already_retained='true'
         c_array_length_in_result='true' />
    </method>
    <method selector='method16'>
       <retval c_array_delimited_by_null='true' already_cfretained='true'
         c_array_of_variable_length='true' printf_format='true' free_result='true' />
    </method>
    <method selector='method17'>
       <retval c_array_length_in_arg='1'/>
    </method>
    <method selector='method18'>
       <retval c_array_length_in_arg='1,2'/>
    </method>
    <method selector='method19'>
       <retval c_array_length_in_arg='4, 5'/>
    </method>
    <method selector='method20'>
       <retval function_pointer_retained='false'/>
          <!-- ignored, no function data -->
    </method>
    <method selector='method21'>
       <retval function_pointer_retained='false' function_pointer='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
          <dummy />
       </retval>
    </method>
    <method selector='method22'>
       <retval function_pointer_retained='false' block='true'>
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
    <method ></method><!-- ignore -->
    <method variadic='true'></method><!-- ignore -->
    <method ignore='true'></method><!-- ignore -->
  </class>
  <class name='MyClass3'>
    <method selector='method7'>
       <retval type='q' />
       <arg index='1' type='f'/>
       <arg index='2' type='d'/>
    </method>
    <method selector='method8'>
       <arg index='1' type='d'/>
       <arg index='2' type='d'/>
    </method>
    <method selector='method9'>
       <arg type='d'/><!-- ignored: no index -->
    </method>
    <method selector='method10'>
       <arg index='1' type='d'/>
    </method>
    <method selector='method11'>
       <arg index='1' type='f' type64='d' />
    </method>
    <method selector='method12'>
       <arg index='1'/><!-- ignore -->
    </method>
    <method selector='method13'>
       <arg index='1' type_modifier='n' />
    </method>
    <method selector='method13b'>
       <arg index='1' sel_of_type='v@:f' c_array_of_fixed_length='4'/>
    </method>
    <method selector='method14'>
       <arg index='1' sel_of_type='v@:f' sel_of_type64='v@:d' />
    </method>
    <method selector='method15'>
       <arg index='1' null_accepted='false' already_retained='true'
          c_array_length_in_result='true' />
    </method>
    <method selector='method16'>
       <arg index='1' c_array_delimited_by_null='true'
          already_cfretained='true' c_array_of_variable_length='true'
          printf_format='true' free_result='true' />
    </method>
    <method selector='method17'>
       <arg index='1' c_array_length_in_arg='1'/>
    </method>
    <method selector='method18'>
       <arg index='1' c_array_length_in_arg='1,2'/>
    </method>
    <method selector='method19'>
       <arg index='1' c_array_length_in_arg='4, 5'/>
    </method>
    <method selector='method20'>
       <arg index='1' function_pointer_retained='false'/>
         <!-- ignored, no function data -->
    </method>
    <method selector='method21'>
       <arg index='1' function_pointer_retained='false' function_pointer='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </arg>
    </method>
    <method selector='method22'>
       <arg index='1' function_pointer_retained='false' block='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </arg>
    </method>
    <method selector='method23'>
       <arg index='1' function_pointer='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </arg>
    </method>
    <method selector='method24' classmethod='true'>
       <arg index='1' block='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </arg>
    </method>
  </class>
  <function /><!-- ignored -->
  <function><!-- ignored -->
    <arg type="f" />
    <retval type="@" />
  </function>
  <function name='function1' ignore='true' ><!-- ignore -->
    <arg type="f" />
    <retval type="@" />
  </function>
  <function name='function2' variadic='true' ></function>
  <function name='function3' variadic='true' c_array_delimited_by_null='true'>
  </function>
  <function name='function4' variadic='true' c_array_length_in_arg='4'>
  </function>
  <function name='function5' c_array_delimited_by_null='true'><retval type='d'/>
  </function><!-- c_array... ignored -->
  <function name='function6' c_array_length_in_arg='4'><retval type='d' />
  </function><!-- c_array... ignored -->
  <function name='function7' ignore='true'></function>
  <function name='function8' ignore='true' suggestion='ignore me'></function>
  <function name='function9' suggestion='ignore me'><retval type='d'/>
  </function><!-- suggestion ignored -->
  <function name='function10'>
    <retval type='d'/>
  </function>
  <function name='function11'>
     <retval type='f' type64='d' />
  </function>
  <function name='function12'>
     <retval/><!-- ignore -->
  </function>
  <function name='function13'>
     <retval type='i' type_modifier='n' />
  </function>
  <function name='function14'>
     <retval type=':' sel_of_type='v@:f' c_array_of_fixed_length='4'/>
  </function>
  <function name='function15'>
     <retval type=':' sel_of_type='v@:f' sel_of_type64='v@:d' />
  </function>
  <function name='function16'>
     <retval type='i' null_accepted='false' already_retained='true'
        c_array_length_in_result='true' />
  </function>
  <function name='function17'>
     <retval type='i' already_cfretained='true' c_array_delimited_by_null='true'
          c_array_of_variable_length='true' printf_format='true'
          free_result='true' />
  </function>
  <function name='function18'>
     <retval type='i' c_array_length_in_arg='1'/>
  </function>
  <function name='function19'>
     <retval type='i' c_array_length_in_arg='1,2'/>
  </function>
  <function name='function20'>
     <retval type='i' c_array_length_in_arg='4, 5'/>
  </function>
  <function name='function21'>
     <retval type='?' function_pointer_retained='false'/>
       <!-- ignored, no function data -->
  </function>
  <function name='function22'>
     <retval type='?' function_pointer_retained='false' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function23'>
     <retval type='@?' function_pointer_retained='false' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function24'>
     <retval type='?' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function25'>
     <retval type='@?' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function26'>
     <retval type='q' />
     <arg index='1' type='f'/>
     <arg index='2' type='d'/>
  </function>
  <function name='function27'>
     <arg index='1' type='d'/>
     <arg index='2' type='d'/>
  </function>
  <function name='function29'>
     <arg type='d'/>
  </function>
  <function name='function30'>
     <arg type='f' type64='d' />
  </function>
  <function name='function32'>
     <arg type='@' type_modifier='n' />
  </function>
  <function name='function33'>
     <arg type=':' sel_of_type='v@:f' c_array_of_fixed_length='4'/>
  </function>
  <function name='function34'>
     <arg type=':' sel_of_type='v@:f' sel_of_type64='v@:d' />
  </function>
  <function name='function35'>
     <arg type='@' null_accepted='false' already_retained='true'
       c_array_length_in_result='true' />
  </function>
  <function name='function36'>
     <arg type='@' c_array_delimited_by_null='true' already_cfretained='true'
        c_array_of_variable_length='true' printf_format='true'
        free_result='true' />
  </function>
  <function name='function37'>
     <arg type='@' c_array_length_in_arg='1'/>
  </function>
  <function name='function38'>
     <arg type='@' c_array_length_in_arg='1,2'/>
  </function>
  <function name='function39'>
     <arg type='@' c_array_length_in_arg='4, 5'/>
  </function>
  <function name='function40'>
     <arg type='?' function_pointer_retained='false'/>
     <!-- ignored, no function data -->
  </function>
  <function name='function41'>
     <arg type='?' function_pointer_retained='false' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function42'>
     <arg type='@?' function_pointer_retained='false' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function43'>
     <arg type='?' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function44'>
     <arg type='@?' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function45'><!-- ignore: arg node without type-->
    <arg type_modifier='n' />
  </function>
  <function name='function46'><!-- ignore: arg node without type-->
    <arg type='@' />
    <arg type_modifier='n' />
  </function>
  <function name='function47'><!-- ignore: retval node without type-->
    <retval type_modifier='n'/>
    <arg type='@' />
    <arg type='@' />
  </function>
  <!-- TODO: type rewriting (_C_BOOL, _C_NSBOOL)-->
  <informal_protocol/><!-- ignore -->
  <informal_protocol name='protocol1' />
  <informal_protocol name='protocol2' >
    <method selector='selector1' type='v@:f' type64='v@:d' />
    <method selector='selector2' type='v@:f' type64='v@:d' classmethod='false' />
    <method selector='selector3' type='v@:f' type64='v@:d' classmethod='true' />
    <method selector='selector4' type='v@:f' type64='v@:d' variadic='true' />
         <!-- 'variadic' is ignored -->
    <method selector='selector5' /><!-- ignore: no type -->
    <method selector='selector6' type64='v@:@' /><!-- ignore 32-bit -->
    <method selector='selector7' type='v@:f' class_method='false' />
       <!-- manpage: class_method, pyobjc 2.3: classmethod -->
    <method selector='selector8' type='v@:f' class_method='true' />
    <method/>
    <method selector='selector9'/>
    <method type='v@:f'/>
  </informal_protocol>
  <struct/><!-- ignore -->
  <struct type='{foo=dd}' /><!--ignore-->
  <struct name='struct1' /><!-- ignore -->
  <struct name='struct2' alias='module.struct3' /><!-- ignore -->
  <struct name='struct3' type='{struct3=@@}' />
  <struct name='struct4' type='{struct3=ff}' type64='{struct4=dd}' />
  <struct name='struct5' type='{struct3=@@}' alias='module2.struct'/>
  <struct name='struct6' type='{struct6=BB}' /><!-- _C_NSBOOL -->
  <struct name='struct7' type='{struct7=Z@}' /><!-- _C_BOOL -->
  <struct name='struct8' type='{struct8=@@}' alias='sys.maxsize'/>
  <struct name='struct9' type='{struct9=ii}' alias='sys.does_not_exist'/>
</signatures>
"""


def iter_framework_dir(framework_dir):
    for dn in os.listdir(framework_dir):
        fn = os.path.join(
            framework_dir,
            dn,
            "Resources",
            "BridgeSupport",
            dn.replace(".framework", ".bridgesupport"),
        )
        if os.path.exists(fn):
            yield fn

        fn = os.path.join(framework_dir, dn, "Frameworks")
        if os.path.exists(fn):
            yield from iter_framework_dir(fn)


def contains_any(name, fragments):
    return any(x in name for x in fragments)


class TestBridgeSupportParser(TestCase):
    def testInvalidToplevel(self):
        with self.assertRaisesRegex(
            objc.error, "invalid root node in bridgesupport file"
        ):
            bridgesupport._BridgeSupportParser(
                b"<signatures2></signatures2>",
                "Cocoa",
            )

        with self.assertRaises(ET.ParseError):
            bridgesupport._BridgeSupportParser(
                b"<signatures2></signatures>",
                "Cocoa",
            )

    def test_xml_structure_variants(self):
        # Run 'verify_xml_structure' for all cpu variant
        # (big/little endian,  32- en 64-bit)
        orig_byteorder = sys.byteorder
        orig_maxsize = sys.maxsize

        try:
            for is32bit in (True, False):
                sys.maxsize = 2**31 - 1 if is32bit else 2**63 - 1

                for endian in ("little", "big"):
                    sys.byteorder = endian

                    reload(bridgesupport)

                    self.verify_xml_structure()

        finally:
            sys.byteorder = orig_byteorder
            sys.maxsize = orig_maxsize

            # See above
            reload(bridgesupport)

    def verify_xml_structure(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            prs = self.assert_valid_bridgesupport("TestXML", TEST_XML)

        all_constants = [
            ("constant1", b"@", False),
            ("constant2", b"I" if sys.maxsize < 2**32 else b"Q", False),
            ("constant5", objc._C_NSBOOL, False),
            ("constant6", objc._C_BOOL, False),
            ("constant7", b"@", False),
            ("constant8", b"@", True),
        ]
        if sys.maxsize > 2**32:
            all_constants.append(("constant4", b"Q", False))

        all_values = {
            "strconst1": b"string constant1",
            "strconst2": (
                b"string constant 2" if sys.maxsize < 2**32 else b"string constant two"
            ),
            "strconst1u": "string constant1 unicode",
            "strconst2u": (
                "string constant 2 unicode"
                if sys.maxsize < 2**32
                else "string constant two unicode"
            ),
            "strconst7": "zee\xebn",
            "enum1": 1,
            "enum2": 3 if sys.maxsize < 2**32 else 4,
            "enum3": 5 if sys.byteorder == "little" else 6,
            "enum4": 7,
            "enum9": 2.5,
            "enum10": 10.5,
            "enum11": 11.5,
            "enum12": 12.5,
            "enum13": 13,
            "enum14": 14,
            "enum_posinf": float("+inf"),
            "enum_neginf": float("-inf"),
            "enum_nan": float("nan"),
            "enum_posinf2": float("+inf"),
            "null1": None,
        }
        if sys.maxsize > 2**32:
            all_values["strconst5"] = b"string five"
            all_values["strconst6"] = "string five unicode"
            all_values["enum6"] = 4

        if sys.byteorder == "little":
            all_values["enum8"] = 5
        else:
            all_values["enum7"] = 6

        all_opaque = [
            ("opaque1", b"^{opaque1}"),
            ("opaque2", b"^{opaque2=f}" if sys.maxsize < 2**32 else b"^{opaque2=d}"),
        ]
        if sys.maxsize > 2**32:
            all_opaque.append(("opaque4", b"^{opaque4=d}"))

        all_func_aliases = [("func1", "orig_function")]

        a = objc.lookUpClass("NSArray").alloc().init()
        CFArrayTypeID = a._cfTypeID()
        all_cftypes = [
            ("CFProxy1Ref", b"^{CFProxy}", CFArrayTypeID),
            (
                "CFProxy2Ref",
                b"^{CFProxy32}" if sys.maxsize < 2**32 else b"^{CFProxy64}",
                CFArrayTypeID,
            ),
            ("CFProxy3Ref", b"^{CFProxy3}", None, "NSProxy"),
            ("CFProxy4Ref", b"^{CFProxy4}", None, "NSProxy2"),
            ("CFProxy5Ref", b"^{CFProxy}", None, "NSCFType"),
            ("CFProxy6Ref", b"^{CFProxy}", None, "NSCFType"),
            (
                "CFProxy7Ref",
                b"^{CFProxy32}" if sys.maxsize < 2**32 else b"^{CFProxy64}",
                None,
                "NSCFType",
            ),
        ]
        if sys.maxsize > 2**32:
            all_cftypes.append(("CFProxy9Ref", b"^{CFProxy64}", CFArrayTypeID))

        all_methods = {
            (b"MyClass2", b"method2", False): {"variadic": True},
            (b"MyClass2", b"method3", False): {
                "variadic": True,
                "c_array_delimited_by_null": True,
            },
            (b"MyClass2", b"method4", False): {
                "variadic": True,
                "c_array_length_in_arg": 4 + 2,
            },
            (b"MyClass2", b"method5", False): {"retval": {"type": b"d"}},
            (b"MyClass2", b"method6", False): {"retval": {"type": b"d"}},
            (b"MyClass2", b"method7", False): {"suggestion": "don't use this method"},
            (b"MyClass2", b"method8", False): {"suggestion": "ignore me"},
            (b"MyClass2", b"method9", False): {"retval": {"type": b"d"}},
            (b"MyClass2", b"method10", False): {"retval": {"type": b"d"}},
            (b"MyClass2", b"method11", False): {
                "retval": {"type": b"f" if sys.maxsize < 2**32 else b"d"}
            },
            (b"MyClass2", b"method13", True): {"retval": {"type_modifier": b"n"}},
            (b"MyClass2", b"method13b", False): {
                "retval": {"sel_of_type": b"v@:f", "c_array_of_fixed_length": 4}
            },
            (b"MyClass2", b"method14", False): {
                "retval": {"sel_of_type": b"v@:f" if sys.maxsize < 2**32 else b"v@:d"}
            },
            (b"MyClass2", b"method15", False): {
                "retval": {"null_accepted": False, "already_retained": True}
            },
            (b"MyClass2", b"method16", False): {
                "retval": {
                    "c_array_delimited_by_null": True,
                    "c_array_of_variable_length": True,
                    "printf_format": True,
                    "free_result": True,
                    "already_cfretained": True,
                }
            },
            (b"MyClass2", b"method17", False): {
                "retval": {"c_array_length_in_arg": 1 + 2}
            },
            (b"MyClass2", b"method18", False): {
                "retval": {"c_array_length_in_arg": (1 + 2, 2 + 2)}
            },
            (b"MyClass2", b"method19", False): {
                "retval": {"c_array_length_in_arg": (4 + 2, 5 + 2)}
            },
            (b"MyClass2", b"method21", False): {
                "retval": {
                    "callable_retained": False,
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                    },
                }
            },
            (b"MyClass2", b"method22", False): {
                "retval": {
                    "callable_retained": False,
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"d"},
                        },
                    },
                }
            },
            (b"MyClass2", b"method23", False): {
                "retval": {
                    "callable_retained": True,
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                    },
                }
            },
            (b"MyClass2", b"method24", False): {
                "retval": {
                    "callable_retained": True,
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"d"},
                        },
                    },
                }
            },
            (b"MyClass3", b"method7", False): {
                "retval": {"type": b"q"},
                "arguments": {2 + 1: {"type": b"f"}, 2 + 2: {"type": b"d"}},
            },
            (b"MyClass3", b"method8", False): {
                "arguments": {2 + 1: {"type": b"d"}, 2 + 2: {"type": b"d"}}
            },
            (b"MyClass3", b"method10", False): {"arguments": {2 + 1: {"type": b"d"}}},
            (b"MyClass3", b"method11", False): {
                "arguments": {2 + 1: {"type": b"f" if sys.maxsize < 2**32 else b"d"}}
            },
            (b"MyClass3", b"method13", False): {
                "arguments": {2 + 1: {"type_modifier": b"n"}}
            },
            (b"MyClass3", b"method13b", False): {
                "arguments": {
                    2 + 1: {"sel_of_type": b"v@:f", "c_array_of_fixed_length": 4}
                }
            },
            (b"MyClass3", b"method14", False): {
                "arguments": {
                    2 + 1: {"sel_of_type": b"v@:f" if sys.maxsize < 2**32 else b"v@:d"}
                }
            },
            (b"MyClass3", b"method15", False): {
                "arguments": {
                    2
                    + 1: {
                        "null_accepted": False,
                        "already_retained": True,
                        "c_array_length_in_result": True,
                    }
                }
            },
            (b"MyClass3", b"method16", False): {
                "arguments": {
                    2
                    + 1: {
                        "c_array_delimited_by_null": True,
                        "c_array_of_variable_length": True,
                        "printf_format": True,
                        "free_result": True,
                        "already_cfretained": True,
                    }
                }
            },
            (b"MyClass3", b"method17", False): {
                "arguments": {2 + 1: {"c_array_length_in_arg": 1 + 2}}
            },
            (b"MyClass3", b"method18", False): {
                "arguments": {2 + 1: {"c_array_length_in_arg": (1 + 2, 2 + 2)}}
            },
            (b"MyClass3", b"method19", False): {
                "arguments": {2 + 1: {"c_array_length_in_arg": (4 + 2, 5 + 2)}}
            },
            (b"MyClass3", b"method21", False): {
                "arguments": {
                    2
                    + 1: {
                        "callable_retained": False,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                        },
                    }
                }
            },
            (b"MyClass3", b"method22", False): {
                "arguments": {
                    2
                    + 1: {
                        "callable_retained": False,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {
                                0: {"type": b"^v"},
                                1: {"type": b"@"},
                                2: {"type": b"d"},
                            },
                        },
                    }
                }
            },
            (b"MyClass3", b"method23", False): {
                "arguments": {
                    2
                    + 1: {
                        "callable_retained": True,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                        },
                    }
                }
            },
            (b"MyClass3", b"method24", True): {
                "arguments": {
                    2
                    + 1: {
                        "callable_retained": True,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {
                                0: {"type": b"^v"},
                                1: {"type": b"@"},
                                2: {"type": b"d"},
                            },
                        },
                    }
                }
            },
        }

        all_functions = [
            ("function2", b"v", "", {"variadic": True}),
            (
                "function3",
                b"v",
                "",
                {"variadic": True, "c_array_delimited_by_null": True},
            ),
            ("function4", b"v", "", {"variadic": True, "c_array_length_in_arg": 4}),
            ("function5", b"d", "", {"retval": {"type": b"d"}}),
            ("function6", b"d", "", {"retval": {"type": b"d"}}),
            ("function9", b"d", "", {"retval": {"type": b"d"}}),
            ("function10", b"d", "", {"retval": {"type": b"d"}}),
            (
                "function11",
                b"f" if sys.maxsize < 2**32 else b"d",
                "",
                {"retval": {"type": b"f" if sys.maxsize < 2**32 else b"d"}},
            ),
            ("function13", b"i", "", {"retval": {"type": b"i", "type_modifier": b"n"}}),
            (
                "function14",
                b":",
                "",
                {
                    "retval": {
                        "type": b":",
                        "sel_of_type": b"v@:f",
                        "c_array_of_fixed_length": 4,
                    }
                },
            ),
            (
                "function15",
                b":",
                "",
                {
                    "retval": {
                        "type": b":",
                        "sel_of_type": b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                    }
                },
            ),
            (
                "function16",
                b"i",
                "",
                {
                    "retval": {
                        "type": b"i",
                        "null_accepted": False,
                        "already_retained": True,
                    }
                },
            ),
            (
                "function17",
                b"i",
                "",
                {
                    "retval": {
                        "type": b"i",
                        "already_cfretained": True,
                        "c_array_delimited_by_null": True,
                        "c_array_of_variable_length": True,
                        "printf_format": True,
                        "free_result": True,
                    }
                },
            ),
            (
                "function18",
                b"i",
                "",
                {"retval": {"type": b"i", "c_array_length_in_arg": 1}},
            ),
            (
                "function19",
                b"i",
                "",
                {"retval": {"type": b"i", "c_array_length_in_arg": (1, 2)}},
            ),
            (
                "function20",
                b"i",
                "",
                {"retval": {"type": b"i", "c_array_length_in_arg": (4, 5)}},
            ),
            ("function21", b"?", "", {"retval": {"type": b"?"}}),
            (
                "function22",
                b"?",
                "",
                {
                    "retval": {
                        "type": b"?",
                        "callable_retained": False,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                        },
                    }
                },
            ),
            (
                "function23",
                b"@?",
                "",
                {
                    "retval": {
                        "type": b"@?",
                        "callable_retained": False,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {
                                0: {"type": b"^v"},
                                1: {"type": b"@"},
                                2: {"type": b"d"},
                            },
                        },
                    }
                },
            ),
            (
                "function24",
                b"?",
                "",
                {
                    "retval": {
                        "type": b"?",
                        "callable_retained": True,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                        },
                    }
                },
            ),
            (
                "function25",
                b"@?",
                "",
                {
                    "retval": {
                        "type": b"@?",
                        "callable_retained": True,
                        "callable": {
                            "retval": {"type": b"v"},
                            "arguments": {
                                0: {"type": b"^v"},
                                1: {"type": b"@"},
                                2: {"type": b"d"},
                            },
                        },
                    }
                },
            ),
            (
                "function26",
                b"qfd",
                "",
                {
                    "retval": {"type": b"q"},
                    "arguments": {0: {"type": b"f"}, 1: {"type": b"d"}},
                },
            ),
            (
                "function27",
                b"vdd",
                "",
                {"arguments": {0: {"type": b"d"}, 1: {"type": b"d"}}},
            ),
            ("function29", b"vd", "", {"arguments": {0: {"type": b"d"}}}),
            (
                "function30",
                b"vf" if sys.maxsize < 2**32 else b"vd",
                "",
                {"arguments": {0: {"type": b"f" if sys.maxsize < 2**32 else b"d"}}},
            ),
            (
                "function32",
                b"v@",
                "",
                {"arguments": {0: {"type": b"@", "type_modifier": b"n"}}},
            ),
            (
                "function33",
                b"v:",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b":",
                            "sel_of_type": b"v@:f",
                            "c_array_of_fixed_length": 4,
                        }
                    }
                },
            ),
            (
                "function34",
                b"v:",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b":",
                            "sel_of_type": b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                        }
                    }
                },
            ),
            (
                "function35",
                b"v@",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b"@",
                            "null_accepted": False,
                            "already_retained": True,
                            "c_array_length_in_result": True,
                        }
                    }
                },
            ),
            (
                "function36",
                b"v@",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b"@",
                            "c_array_delimited_by_null": True,
                            "already_cfretained": True,
                            "c_array_of_variable_length": True,
                            "printf_format": True,
                            "free_result": True,
                        }
                    }
                },
            ),
            (
                "function37",
                b"v@",
                "",
                {"arguments": {0: {"type": b"@", "c_array_length_in_arg": 1}}},
            ),
            (
                "function38",
                b"v@",
                "",
                {"arguments": {0: {"type": b"@", "c_array_length_in_arg": (1, 2)}}},
            ),
            (
                "function39",
                b"v@",
                "",
                {"arguments": {0: {"type": b"@", "c_array_length_in_arg": (4, 5)}}},
            ),
            ("function40", b"v?", "", {"arguments": {0: {"type": b"?"}}}),
            (
                "function41",
                b"v?",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b"?",
                            "callable_retained": False,
                            "callable": {
                                "retval": {"type": b"v"},
                                "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                            },
                        }
                    }
                },
            ),
            (
                "function42",
                b"v@?",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b"@?",
                            "callable_retained": False,
                            "callable": {
                                "retval": {"type": b"v"},
                                "arguments": {
                                    0: {"type": b"^v"},
                                    1: {"type": b"@"},
                                    2: {"type": b"d"},
                                },
                            },
                        }
                    }
                },
            ),
            (
                "function43",
                b"v?",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b"?",
                            "callable_retained": True,
                            "callable": {
                                "retval": {"type": b"v"},
                                "arguments": {0: {"type": b"@"}, 1: {"type": b"d"}},
                            },
                        }
                    }
                },
            ),
            (
                "function44",
                b"v@?",
                "",
                {
                    "arguments": {
                        0: {
                            "type": b"@?",
                            "callable_retained": True,
                            "callable": {
                                "retval": {"type": b"v"},
                                "arguments": {
                                    0: {"type": b"^v"},
                                    1: {"type": b"@"},
                                    2: {"type": b"d"},
                                },
                            },
                        }
                    }
                },
            ),
        ]

        self.maxDiff = None
        if sys.maxsize <= 2**32:
            all_protocols = [
                (
                    "protocol2",
                    [
                        objc.selector(
                            None,
                            b"selector1",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                        ),
                        objc.selector(
                            None,
                            b"selector2",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                        ),
                        objc.selector(
                            None,
                            b"selector3",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                            isClassMethod=True,
                        ),
                        objc.selector(
                            None,
                            b"selector4",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                        ),
                        objc.selector(None, b"selector7", b"v@:f"),
                        objc.selector(None, b"selector8", b"v@:f", isClassMethod=True),
                    ],
                )
            ]
        else:
            all_protocols = [
                (
                    "protocol2",
                    [
                        objc.selector(
                            None,
                            b"selector1",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                        ),
                        objc.selector(
                            None,
                            b"selector2",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                        ),
                        objc.selector(
                            None,
                            b"selector3",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                            isClassMethod=True,
                        ),
                        objc.selector(
                            None,
                            b"selector4",
                            b"v@:f" if sys.maxsize < 2**32 else b"v@:d",
                        ),
                        objc.selector(None, b"selector6", b"v@:@"),
                        objc.selector(None, b"selector7", b"v@:f"),
                        objc.selector(None, b"selector8", b"v@:f", isClassMethod=True),
                    ],
                )
            ]

        all_structs = [
            ("struct3", b"{struct3=@@}", None),
            (
                "struct4",
                b"{struct3=ff}" if sys.maxsize < 2**32 else b"{struct4=dd}",
                None,
            ),
            ("struct5", b"{struct3=@@}", None),
            ("struct6", b"{struct6=ZZ}", None),
            ("struct7", b"{struct7=B@}", None),
            ("struct8", b"{struct8=@@}", sys.maxsize),
            ("struct9", b"{struct9=ii}", None),
        ]

        self.assertNotIn("strconstinvalid", prs.values)

        self.maxDiff = None
        self.assertCountEqual(prs.constants, all_constants)
        self.assertCountEqual(prs.values, all_values)
        self.assertCountEqual(prs.opaque, all_opaque)
        self.assertCountEqual(prs.func_aliases, all_func_aliases)
        self.assertCountEqual(prs.cftypes, all_cftypes)
        self.assertCountEqual(prs.functions, all_functions)
        self.assertEqual(prs.meta, all_methods)
        self.assertCountEqual(prs.informal_protocols, all_protocols)
        self.assertCountEqual(prs.structs, all_structs)

    def assertIsIdentifier(self, value):
        m = IDENTIFIER.match(value)
        if m is None:
            self.fail(f"'{value}' is not an identifier")

    def assert_valid_callable(self, meta, function):
        if function:
            if "arguments" in meta:
                indexes = sorted(meta["arguments"])
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

            key = "c_array_of_fixed_length"
            if key in meta["retval"]:
                self.assertIsInstance(meta["retval"][key], int)

            key = "c_array_length_in_arg"
            if key in meta["retval"]:
                if isinstance(meta["retval"][key], tuple):
                    self.assertEqual(len(meta["retval"][key]), 2)
                    self.assertTrue(
                        all(isinstance(x, int) for x in meta["retval"][key])
                    )
                else:
                    self.assertIsInstance(meta["retval"][key], int)

            for key in (
                "c_array_delimited_by_null",
                "printf_format",
                "c_array_of_variable_length",
                "null_accepted",
            ):
                if key in meta["retval"]:
                    self.assertIsInstance(meta["retval"][key], bool)

            self.assertNotIn("c_array_length_in_result", meta["retval"])
            self.assertEqual(set(meta["retval"]) - valid_keys, set())

        if "arguments" in meta:
            for idx in meta["arguments"]:
                self.assertIsInstance(idx, int)
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
                    self.assertIsInstance(arg["c_array_of_fixed_length"], int)

                if "c_array_length_in_arg" in arg:
                    if isinstance(arg["c_array_length_in_arg"], int):
                        pass

                    else:
                        self.assertIsInstance(arg["c_array_length_in_arg"], tuple)
                        self.assertEqual(len(arg["c_array_length_in_arg"]), 2)
                        for x in arg["c_array_length_in_arg"]:
                            self.assertIsInstance(x, int)

                for key in (
                    "c_array_delimited_by_null",
                    "printf_format",
                    "c_array_of_variable_length",
                    "null_accepted",
                    "c_array_length_in_result",
                ):
                    if key in arg:
                        self.assertIsInstance(arg[key], bool)

                self.assertEqual(set(arg) - valid_keys, set())

        if "suggestion" in meta:
            self.assertIsInstance(meta["suggestion"], str)

        if "variadic" in meta:
            self.assertIsInstance(meta["variadic"], bool)

        if "variadic" in meta and meta["variadic"]:
            self.assertEqual(
                set(meta.keys())
                - {
                    "arguments",
                    "retval",
                    "variadic",
                    "classmethod",
                    "c_array_length_in_arg",
                    "c_array_delimited_by_null",
                    "suggestion",
                },
                set(),
            )

            found = False
            if "c_array_length_in_arg" in meta:
                self.assertIsInstance(meta["c_array_length_in_arg"], int)
                self.assertNotIn("c_array_delimited_by_null", meta)
                found = True

            if "c_array_delimited_by_null" in meta:
                self.assertIsInstance(meta["c_array_delimited_by_null"], bool)
                found = False

            for idx in meta.get("arguments", {}):
                arg = meta["arguments"][idx]
                if "printf_format" in arg and arg["printf_format"]:
                    if found:
                        self.fail(
                            "meta for variadic with two ways to determine size: %s"
                            % (meta,)
                        )
                    found = True

            # NOTE: disabled because having unsupported variadic methods would be fine (e.g.
            #       metadata says the method is variadic, but it doesn't fall into one of the
            #       supported categories)
            # if not found:
            #    self.fail("meta for variadic without method for determining size: %s"%(meta,))

        else:
            self.assertEqual(
                set(meta.keys())
                - {"arguments", "retval", "variadic", "suggestion", "classmethod"},
                set(),
            )

    def assert_valid_bridgesupport(self, framework_name, xmldata):
        try:
            prs = bridgesupport._BridgeSupportParser(xmldata, framework_name)
        except objc.internal_error as exc:
            if "PyObjCRT_SkipTypeSpec: Unhandled type" in str(exc):
                self.fail("Bad type encoding in metadata (bad type)")
            elif "Invalid array definition" in str(exc):
                self.fail("Bad type encoding in metadata (bad array)")
            elif "Invalid union definition in type signature" in str(exc):
                self.fail("Bad type encoding in metadata (bad union)")
            elif "Invalid struct definition in type signature" in str(exc):
                self.fail("Bad type encoding in metadata (bad struct)")
            else:
                raise

        for item in prs.cftypes:
            if len(item) == 3:
                name, encoding, typeId = item
                tollfreeName = None

            elif len(item) == 4:
                name, encoding, typeId, tollfreeName = item
                self.assertIsNot(tollfreeName, None)

            else:
                self.fail(f"Wrong item length in cftypes: {item}")

            self.assertIsInstance(name, str)
            self.assertIsInstance(encoding, bytes)
            self.assertEqual(len(objc.splitSignature(encoding)), 1)
            if tollfreeName is None:
                self.assertIsInstance(typeId, int)

            else:
                self.assertIs(typeId, None)
                self.assertIsInstance(tollfreeName, str)

        for name, typestr, magic in prs.constants:
            self.assertIsInstance(name, str)
            self.assertIsInstance(typestr, bytes)
            self.assertIsInstance(magic, bool)
            self.assertEqual(len(objc.splitSignature(typestr)), 1)

        for name, orig in prs.func_aliases:
            self.assertIsInstance(name, str)
            self.assertIsInstance(orig, str)
            self.assertIsIdentifier(name)

        for name, encoding, doc, meta in prs.functions:
            self.assertIsInstance(name, str)
            self.assertIsInstance(encoding, bytes)

            # check that signature string is well-formed:
            objc.splitSignature(encoding)

            self.assertEqual(doc, "")
            self.assertIsInstance(meta, dict)
            self.assert_valid_callable(meta, function=True)

        for name, method_list in prs.informal_protocols:
            self.assertIsInstance(name, str)
            self.assertIsInstance(method_list, list)
            for sel in method_list:
                self.assertIsInstance(sel, objc.selector)
                self.assertIs(sel.callable, None)

        for clsname, selname, is_class in prs.meta:
            meta = prs.meta[(clsname, selname, is_class)]
            self.assertIsInstance(clsname, bytes)
            self.assertIsInstance(is_class, bool)
            self.assertIsInstance(selname, bytes)
            self.assertIsInstance(meta, dict)
            self.assert_valid_callable(meta, function=False)

        for name, typestr in prs.opaque:
            self.assertIsInstance(name, str)
            self.assertIsInstance(typestr, bytes)

            self.assertEqual(len(objc.splitSignature(typestr)), 1)

        for name, typestr, _alias in prs.structs:
            self.assertIsInstance(name, str)
            self.assertIsInstance(typestr, bytes)
            self.assertEqual(len(objc.splitSignature(typestr)), 1)

        for name in prs.values:
            self.assertIsInstance(
                prs.values[name], (str, int, float, bytes, type(None))
            )

        return prs


class Patcher:
    def __init__(self):
        self._changes = {}

    def patch(self, path, value):
        if path not in self._changes:
            self._changes[path] = self.get(path)
        self.set(path, value)

    def get(self, path):
        module, name = path.rsplit(".", 1)
        m = __import__(module)
        for p in module.split(".")[1:]:
            m = getattr(m, p)

        return getattr(m, name)

    def set(self, path, value):  # noqa: A003
        module, name = path.rsplit(".", 1)
        m = __import__(module)
        for p in module.split(".")[1:]:
            m = getattr(m, p)

        setattr(m, name, value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, tp):
        for k in self._changes:
            self.set(k, self._changes[k])


class TestParseBridgeSupport(TestCase):
    @skipUnless(ctypes is not None, "requires ctypes")
    def test_calls(self):
        # - Minimal XML with all types of metadata
        # - Mock the APIs used by parseBridgeSupport
        #   (with strict verification of arguments, based on C code)
        # - Verify changes to globals where possible
        # - Verify 'updatingmetadata' state

        class InlineTab:
            pass

        def loadConstant(name, typestr, magic):
            self.assertIsInstance(name, str)
            self.assertIsInstance(typestr, str)
            self.assertEqual(len(objc.splitSignature(typestr.encode("ascii"))), 1)
            self.assertIsInstance(magic, bool)

            if "raise" in name:
                raise AttributeError(name)

            return f"<constant {name!r}>"

        SENTINEL = object()

        def registerCFSignature(name, encoding, typeId, tollfreeName=SENTINEL):
            self.assertIsInstance(name, str)
            self.assertIsInstance(encoding, bytes)
            self.assertIsInstance(typeId, (int, type(None)))
            if tollfreeName is not SENTINEL:
                self.assertIsInstance(tollfreeName, str)

            if typeId is None:
                if tollfreeName is SENTINEL:
                    raise ValueError("Must specify a typeid when not toll-free")

            return f"<cftype {name!r}>"

        metadata_registry = {}

        def registerMetaDataForSelector(class_, selector, metadata):
            self.assertIsInstance(class_, bytes)
            self.assertIsInstance(selector, bytes)
            self.assertIsInstance(metadata, dict)

            # XXX: It might be nice to validate the contents of
            # metadata, but that can be added later.

            metadata_registry[(class_, selector)] = metadata

        def createOpaquePointerType(name, typestr, doc=None):
            self.assertIsInstance(name, str)
            self.assertIsInstance(typestr, bytes)
            self.assertIsInstance(doc, (str, type(None)))
            self.assertEqual(len(objc.splitSignature(typestr)), 1)
            self.assertStartswith(typestr, objc._C_PTR)
            return f"<pointer {name!r}>"

        def createStructType(name, typestr, fieldnames, doc=None, pack=-1):
            self.assertIsInstance(name, str)
            self.assertIsInstance(typestr, bytes)
            self.assertIsInstance(fieldnames, (list, tuple, type(None)))
            self.assertIsInstance(doc, (str, type(None)))
            self.assertIsInstance(pack, int)
            self.assertTrue(-1 <= pack <= 32)
            if fieldnames is not None:
                for nm in fieldnames:
                    self.assertIsInstance(nm, (str, bytes))
            return f"<struct {name!r}>"

        def createStructAlias(name, typestr, structType):
            self.assertIsInstance(name, str)
            self.assertIsInstance(typestr, bytes)

        def informal_protocol(name, method_list):
            self.assertIsInstance(name, str)
            for item in method_list:
                self.assertIsInstance(item, objc.selector)
                self.assertIs(item.callable, None)

            return f"<informal_protocol {name!r}>"

        def loadBundleFunctions(
            bundle, module_globals, functionInfo, skip_undefined=True
        ):
            self.assertIs(bundle, None)
            self.assertIsInstance(module_globals, dict)
            self.assertIsInstance(functionInfo, (list, tuple))
            self.assertIsInstance(skip_undefined, bool)
            for item in functionInfo:
                self.assertIsInstance(item, (tuple, list))
                self.assertTrue(2 <= len(item) <= 4)
                self.assertIsInstance(item[0], str)
                self.assertIsInstance(item[1], bytes)
                if len(item) > 2:
                    self.assertIsInstance(item[2], (str, type(None)))
                if len(item) > 3:
                    self.assertIsInstance(item[3], dict)

                if "inline" in item[0]:
                    continue

                module_globals[item[0]] = f"<function {item[0]!r}>"

        def loadFunctionList(
            function_list, module_globals, functionInfo, skip_undefined=True
        ):
            self.assertIsInstance(function_list, InlineTab)
            self.assertIsInstance(module_globals, dict)
            self.assertIsInstance(functionInfo, (list, tuple))
            self.assertIsInstance(skip_undefined, bool)
            for item in functionInfo:
                self.assertIsInstance(item, (tuple, list))
                self.assertTrue(2 <= len(item) <= 4)
                self.assertIsInstance(item[0], str)
                self.assertIsInstance(item[1], bytes)
                if len(item) > 2:
                    self.assertIsInstance(item[2], (str, type(None)))
                if len(item) > 3:
                    self.assertIsInstance(item[3], dict)
                if item[0] not in module_globals:
                    module_globals[item[0]] = f"<inline_function {item[0]!r}>"

        _meta_updates = []

        def _updatingMetadata(flag):
            self.assertIsInstance(flag, bool)
            _meta_updates.append(flag)

        with Patcher() as p:
            p.patch("objc._updatingMetadata", _updatingMetadata)
            p.patch("objc._loadConstant", loadConstant)
            p.patch("objc.registerCFSignature", registerCFSignature)
            p.patch("objc.registerMetaDataForSelector", registerMetaDataForSelector)
            p.patch("objc.createOpaquePointerType", createOpaquePointerType)
            p.patch("objc.createStructType", createStructType)
            p.patch("objc.createStructAlias", createStructAlias)
            p.patch("objc.informal_protocol", informal_protocol)
            p.patch("objc.loadBundleFunctions", loadBundleFunctions)
            p.patch("objc.loadFunctionList", loadFunctionList)
            p.patch("sys.modules", sys.modules.copy())

            # 1. Empty metadata
            _meta_updates = []
            metadata_registry = {}
            module_globals = {}

            with self.assertWarns(DeprecationWarning):
                objc.parseBridgeSupport(
                    b"""\
                <signatures>
                </signatures>
                """,
                    module_globals,
                    "TestFramework",
                )

            self.assertEqual(_meta_updates, [True, False])
            self.assertEqual(metadata_registry, {})
            self.assertEqual(module_globals, {})

            # 2. Various metadata
            _meta_updates = []
            metadata_registry = {}
            module_globals = {}
            orig_libraries = list(bridgesupport._libraries)

            xml = b"""\
            <signatures>
              <opaque name='opaque_type' type='^{opaque}'/>
              <struct name='OCPoint' type='{OCPoint=dd}' />
              <struct name='OCPoint2' type='{OCPoint2=dd}'
                alias='distutils.sysconfig.get_config_var'/>
              <enum name='enum_value' value='42' />
              <constant name='const_value' type='@' />
              <constant name='const_raise' type='@' />
              <cftype name='cftype_value' type='^{cftype}' />
              <class name='class1'>
                <method selector='sel1:' class_method='false'>
                  <arg index='0' null_accepted='false' type_modifier='o' />
                </method>
              </class>
              <function name='function1'>
                 <retval type='f' />
                 <arg type='@' />
                 <arg type='d' />
                 <dummy />
              </function>
              <function name='function2'>
                 <retval type='d' />
                 <arg type='d' />
              </function>
              <function name='inline_function'>
                <retval type='i' />
              </function>
              <function_pointer name='function3' original='function2'/>
              <function_pointer name='function4' original='no_such_function'/>
              <informal_protocol name='protocol1'>
                <method selector='sel1:' type='v@:@' />
              </informal_protocol>
              <informal_protocol name='protocol2'>
                <method selector='sel2:' type='v@:@' />
              </informal_protocol>
            </signatures>
            """
            with self.assertWarns(DeprecationWarning):
                objc.parseBridgeSupport(xml, module_globals, "TestFramework")

            self.assertEqual(_meta_updates, [True, False])
            self.assertEqual(
                metadata_registry,
                {
                    (b"class1", b"sel1:"): {
                        "arguments": {
                            2: {"null_accepted": False, "type_modifier": b"o"}
                        }
                    }
                },
            )

            from distutils.sysconfig import get_config_var

            self.assertNotIn("protocols", module_globals)
            self.assertEqual(
                module_globals,
                {
                    "enum_value": 42,
                    "const_value": "<constant 'const_value'>",
                    "cftype_value": "<cftype 'cftype_value'>",
                    "function1": "<function 'function1'>",
                    "function2": "<function 'function2'>",
                    "function3": "<function 'function2'>",
                    "OCPoint": "<struct 'OCPoint'>",
                    "OCPoint2": get_config_var,
                    "opaque_type": "<pointer 'opaque_type'>",
                },
            )
            self.assertEqual(orig_libraries, bridgesupport._libraries)

            # 3. inlineTab
            _meta_updates = []
            metadata_registry = {}
            module_globals = {}
            orig_libraries = list(bridgesupport._libraries)

            xml = b"""\
            <signatures>
              <function name='function1'>
                 <retval type='f' />
                 <arg type='@' />
                 <arg type='d' />
              </function>
              <function name='function2'>
                 <retval type='d' />
                 <arg type='d' />
              </function>
              <function name='inline_function_name'>
                <retval type='i' />
              </function>
            </signatures>
            """
            with self.assertWarns(DeprecationWarning):
                objc.parseBridgeSupport(
                    xml, module_globals, "TestFramework2", inlineTab=InlineTab()
                )

            self.assertEqual(_meta_updates, [True, False])
            self.assertEqual(metadata_registry, {})
            self.assertNotIn("protocols", module_globals)
            self.assertNotIn("TestFramework2.protocols", sys.modules)
            self.assertEqual(
                module_globals,
                {
                    "function1": "<function 'function1'>",
                    "function2": "<function 'function2'>",
                    "inline_function_name": "<inline_function 'inline_function_name'>",
                },
            )
            self.assertEqual(orig_libraries, bridgesupport._libraries)

            # 4. dylib usage
            _meta_updates = []
            metadata_registry = {}
            module_globals = {}
            orig_libraries = list(bridgesupport._libraries)

            xml = b"""\
            <signatures>
              <function name='function1'>
                 <retval type='f' />
                 <arg type='@' />
                 <arg type='d' />
              </function>
              <function name='function2'>
                 <retval type='d' />
                 <arg type='d' />
              </function>
              <function name='inline_function_name'>
                <retval type='i' />
              </function>
            </signatures>
            """
            with self.assertWarns(DeprecationWarning):
                objc.parseBridgeSupport(
                    xml,
                    module_globals,
                    "TestFramework2",
                    dylib_path="/usr/lib/libxml2.dylib",
                )

            self.assertEqual(_meta_updates, [True, False])
            self.assertEqual(metadata_registry, {})
            self.assertNotIn("protocols", module_globals)
            self.assertNotIn("TestFramework2.protocols", sys.modules)
            self.assertEqual(
                module_globals,
                {
                    "function1": "<function 'function1'>",
                    "function2": "<function 'function2'>",
                },
            )
            self.assertEqual(len(orig_libraries) + 1, len(bridgesupport._libraries))
            self.assertIsInstance(bridgesupport._libraries[-1], ctypes.CDLL)
            self.assertEqual(
                bridgesupport._libraries[-1]._name, "/usr/lib/libxml2.dylib"
            )


class TestInitFrameworkWrapper(TestCase):
    def test_calls_parse_helper(self):
        # Test functionality of initFrameworkWrapper and _parseBridgeSupport
        # by mocking 'parseBridgeSupport' (and the location of the caller)
        with Patcher() as p:
            calls = []
            raise_exception = None
            update_globals = None

            def parseBridgeSupport(
                xmldata,
                globals,  # noqa: A002
                frameworkName,
                dylib_path=None,
                inlineTab=None,
            ):
                calls.append((xmldata, globals, frameworkName, dylib_path, inlineTab))
                if update_globals is not None:
                    globals.update(update_globals)

                if raise_exception is not None:
                    raise raise_exception()

            class MockModule:
                pass

            p.patch("objc.parseBridgeSupport", parseBridgeSupport)

            # 1. Verify that failures to load bridgesupport emit a warning
            calls = []
            raise_exception = objc.internal_error
            update_globals = None

            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                bridgesupport._parseBridgeSupport("", {}, "TestFramework")
            self.assertTrue(len(w) == 1)
            self.assertEqual(w[0].category, RuntimeWarning)
            calls = []

            with warnings.catch_warnings(record=True):
                warnings.simplefilter("always")
                g = {}
                update_globals = {"foo": 42, "bar": 33, "protocols": MockModule()}
                bridgesupport._parseBridgeSupport("", g, "TestFramework")
                self.assertEqual(g, update_globals)
                self.assertEqual(calls, [("", g, "TestFramework", None, None)])

                self.assertEqual(len(g["protocols"].__dict__), 0)

            # 2. Run without problems, without 'protocols' in dictionary
            raise_exception = None
            update_globals = {"foo": 42, "bar": 33}

            calls = []
            g = {}
            bridgesupport._parseBridgeSupport("", g, "TestFramework", "a", "b")
            self.assertEqual(g, update_globals)
            self.assertEqual(calls, [("", g, "TestFramework", "a", "b")])
            self.assertNotIn("protocols", g)

            calls = []
            g = {}
            bridgesupport._parseBridgeSupport("", g, "TestFramework", inlineTab="a")
            self.assertEqual(g, update_globals)
            self.assertEqual(calls, [("", g, "TestFramework", None, "a")])
            self.assertNotIn("protocols", g)

            # 3. Run witout problems, with 'protocols' in dictionary
            calls = []
            raise_exception = None
            update_globals = {"foo": 42, "bar": 33, "protocols": MockModule()}

            g = {}
            bridgesupport._parseBridgeSupport("", g, "TestFramework", "a", "b")
            self.assertEqual(g, update_globals)
            self.assertEqual(calls, [("", g, "TestFramework", "a", "b")])
            self.assertEqual(len(g["protocols"].__dict__), 0)

            calls = []
            g = {}
            bridgesupport._parseBridgeSupport("", g, "TestFramework", inlineTab="a")
            self.assertEqual(g, update_globals)
            self.assertEqual(calls, [("", g, "TestFramework", None, "a")])
            self.assertEqual(len(g["protocols"].__dict__), 0)

    def test_calls_initwrappper(self):
        with Patcher() as p:
            SENTINEL = object()

            class InlineTab:
                pass

            bundle_resources = {}

            class Bundle:
                def __init__(self, calls=None):
                    if calls is None:
                        calls = []
                    self.calls = calls

                def pathForResource_ofType_inDirectory_(
                    self, name, resource_type, directory
                ):
                    self.calls.append((name, resource_type, directory))
                    return bundle_resources.get((name, resource_type), None)

                def __eq__(self, other):
                    if type(self) is not type(other):
                        return False

                    return self.calls == other.calls

                def __repr__(self):
                    return f"<Bundle calls={self.calls!r}>"

            load_calls = []
            bundle_exception = None

            def loadBundle(
                module_name,
                module_globals,
                bundle_path=SENTINEL,
                bundle_identifier=SENTINEL,
                scan_classes=True,
            ):
                if bundle_exception is not None:
                    bundle_exception(module_name, bundle_path, bundle_identifier)
                self.assertIsInstance(module_name, str)
                self.assertIsInstance(module_globals, dict)
                if bundle_path is not SENTINEL:
                    self.assertIsInstance(bundle_path, str)
                if bundle_identifier is not SENTINEL:
                    self.assertIsInstance(bundle_identifier, str)
                bool(scan_classes)
                bundle = Bundle()
                load_calls.append(
                    (
                        bundle,
                        module_name,
                        module_globals,
                        bundle_path,
                        bundle_identifier,
                        scan_classes,
                    )
                )
                return bundle

            resources = {}

            def resource_exists(package, name):
                return (package, name) in resources

            def resource_string(package, name):
                try:
                    return resources[(package, name)]
                except KeyError:
                    raise OSError(name)

            parse_calls = []

            def parseBridgeSupport(
                xml, globals, framework, dylib_path=None, inlineTab=None  # noqa: A002
            ):
                parse_calls.append((xml, globals, framework, dylib_path, inlineTab))

            TEST_BRIDGESUPPORT_DIRECTORIES = []

            p.patch("objc.loadBundle", loadBundle)
            p.patch("objc._bridgesupport.resource_exists", resource_exists)
            p.patch("objc._bridgesupport.resource_string", resource_string)
            p.patch("objc._bridgesupport._parseBridgeSupport", parseBridgeSupport)
            p.patch(
                "objc._bridgesupport.BRIDGESUPPORT_DIRECTORIES",
                TEST_BRIDGESUPPORT_DIRECTORIES,
            )

            helper_dir = os.path.join(os.path.dirname(__file__), "data_bridgesupport")

            # 1. No resource files, no bundle files, no library files
            resources = {}
            bundle_resources = {}
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [os.path.join(helper_dir, "empty")]

            def basic_verify(g):
                self.assertIs(g["objc"], objc)
                self.assertIs(g["super"], objc.super)

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "TestFramework",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        True,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "TestFramework",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    frameworkResourceName="TestResources",
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        True,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "TestFramework", "/Library/Framework/Test.framework", None, g
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        "/Library/Framework/Test.framework",
                        SENTINEL,
                        True,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "TestFramework",
                    "/Library/Framework/Test.framework",
                    None,
                    g,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        "/Library/Framework/Test.framework",
                        SENTINEL,
                        False,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper("TestFramework", None, "com.apple.Test", g)
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        True,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "TestFramework", None, "com.apple.Test", g, scan_classes=False
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "TestFramework",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=InlineTab(),
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        True,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "TestFramework",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=InlineTab(),
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("TestFramework", "bridgesupport", "BridgeSupport")]),
                        "TestFramework",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            # 2. Have resource files, bundle files and library files (only first is used)
            resources = {
                (
                    "Test",
                    "PyObjC.bridgesupport",
                ): b"<signatures><constant name='test resource' type='@' /></signatures>"
            }
            bundle_resources = {
                "Test": os.path.join(helper_dir, "bundle_data", "Test.bridgesupport")
            }
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [os.path.join(helper_dir, "with_data")]

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls, [(Bundle([]), "Test", g, SENTINEL, "com.apple.Test", False)]
            )
            self.assertEqual(
                parse_calls,
                [
                    (
                        b"<signatures><constant name='test resource' type='@' /></signatures>",
                        g,
                        "Test",
                        None,
                        inlineTab,
                    )
                ],
            )

            # 3. No resource files, have bundle files and library files
            # (only bundle one is used)
            resources = {}
            bundle_resources = {
                ("Test", "bridgesupport"): os.path.join(
                    helper_dir, "bundle_data", "Test.bridgesupport"
                )
            }
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [os.path.join(helper_dir, "with_data")]

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle(
                            [
                                ("Test", "bridgesupport", "BridgeSupport"),
                                ("Test", "dylib", "BridgeSupport"),
                            ]
                        ),
                        "Test",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(
                parse_calls,
                [
                    (
                        b"<signatures><constant name='bundle.test' type='@'/></signatures>\n",
                        g,
                        "Test",
                        None,
                        None,
                    )
                ],
            )

            # 4. No resource files, have bundle files (with override)
            # and library files (only bundle one is used)
            resources = {
                (
                    "Test",
                    "PyObjCOverrides.bridgesupport",
                ): b"<signatures><constant name='test override' type='@' /></signatures>"
            }
            bundle_resources = {
                ("Test", "bridgesupport"): os.path.join(
                    helper_dir, "bundle_data", "Test.bridgesupport"
                )
            }
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [os.path.join(helper_dir, "with_data")]

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle(
                            [
                                ("Test", "bridgesupport", "BridgeSupport"),
                                ("Test", "dylib", "BridgeSupport"),
                            ]
                        ),
                        "Test",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(
                parse_calls,
                [
                    (
                        b"<signatures><constant name='bundle.test' type='@'/></signatures>\n",
                        g,
                        "Test",
                        None,
                        None,
                    ),
                    (
                        b"<signatures><constant name='test override' type='@' /></signatures>",
                        g,
                        "Test",
                        None,
                        inlineTab,
                    ),
                ],
            )

            resources = {
                (
                    "Test",
                    "PyObjCOverrides.bridgesupport",
                ): b"<signatures><constant name='test override' type='@' /></signatures>"
            }
            bundle_resources = {
                ("Test", "bridgesupport"): os.path.join(
                    helper_dir, "bundle_data", "Test.bridgesupport"
                ),
                ("Test", "dylib"): os.path.join(
                    helper_dir, "bundle_data", "Test.dylib"
                ),
            }
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [os.path.join(helper_dir, "with_data")]

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle(
                            [
                                ("Test", "bridgesupport", "BridgeSupport"),
                                ("Test", "dylib", "BridgeSupport"),
                            ]
                        ),
                        "Test",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(
                parse_calls,
                [
                    (
                        b"<signatures><constant name='bundle.test' type='@'/></signatures>\n",
                        g,
                        "Test",
                        os.path.join(helper_dir, "bundle_data", "Test.dylib"),
                        None,
                    ),
                    (
                        b"<signatures><constant name='test override' type='@' /></signatures>",
                        g,
                        "Test",
                        None,
                        inlineTab,
                    ),
                ],
            )

            # 5. No resource file, no bundle file, have library file
            resources = {}
            bundle_resources = {}
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [os.path.join(helper_dir, "with_data")]

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("Test", "bridgesupport", "BridgeSupport")]),
                        "Test",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(
                parse_calls,
                [
                    (
                        b'<signatures version=\'1\'><string_constant name="info" value="system test.bridgesupport" /></signatures>\n',  # noqa: B950
                        g,
                        "Test",
                        None,
                        None,
                    )
                ],
            )

            resources = {}
            bundle_resources = {}
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [
                os.path.join(helper_dir, "with_data_dylib")
            ]

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("Test", "bridgesupport", "BridgeSupport")]),
                        "Test",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(
                parse_calls,
                [
                    (
                        b'<signatures version=\'1\'><string_constant name="info" value="system test.bridgesupport 2" /></signatures>\n',  # noqa: B950
                        g,
                        "Test",
                        os.path.join(helper_dir, "with_data_dylib", "Test.dylib"),
                        None,
                    )
                ],
            )

            # 6. No resource file, no bundle file, have library file (with override)
            resources = {
                (
                    "Test",
                    "PyObjCOverrides.bridgesupport",
                ): b'<signatures><contant name="override" type="@"></signatures>'
            }
            bundle_resources = {}
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = [os.path.join(helper_dir, "with_data")]

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()
            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )
            basic_verify(g)
            self.assertEqual(len(g), 2)
            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle([("Test", "bridgesupport", "BridgeSupport")]),
                        "Test",
                        g,
                        SENTINEL,
                        "com.apple.Test",
                        False,
                    )
                ],
            )
            self.assertEqual(
                parse_calls,
                [
                    (
                        b'<signatures version=\'1\'><string_constant name="info" value="system test.bridgesupport" /></signatures>\n',  # noqa: B950
                        g,
                        "Test",
                        None,
                        None,
                    ),
                    (
                        b'<signatures><contant name="override" type="@"></signatures>',
                        g,
                        "Test",
                        None,
                        inlineTab,
                    ),
                ],
            )

            # 7. Cannot load bundle (should not look for bridgesupport)
            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()

            def bundle_exception(name, path, identifier):  # noqa: F811
                raise ImportError(name)

            with self.assertWarns(DeprecationWarning):
                with self.assertRaisesRegex(ImportError, "^Test$"):
                    objc.initFrameworkWrapper(
                        "Test",
                        "/Library/Framework/Test.framework",
                        "com.apple.Test",
                        g,
                        inlineTab=inlineTab,
                        scan_classes=False,
                    )

            self.assertEqual(load_calls, [])
            self.assertEqual(parse_calls, [])
            self.assertEqual(g, {})

            # 8. framework_identifier is not None, cannot find through identifier
            resources = {}
            bundle_resources = {}
            TEST_BRIDGESUPPORT_DIRECTORIES[:] = []

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()

            def bundle_exception(name, path, identifier):  # noqa: F811
                if identifier is not SENTINEL:
                    raise ImportError(name)

            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                    scan_classes=False,
                )

            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle(calls=[("Test", "bridgesupport", "BridgeSupport")]),
                        "Test",
                        g,
                        "/Library/Framework/Test.framework",
                        SENTINEL,
                        False,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            load_calls = []
            parse_calls = []
            g = {}
            inlineTab = InlineTab()

            def bundle_exception(name, path, identifier):  # noqa: F811
                if identifier is not SENTINEL:
                    raise ImportError(name)

            with self.assertWarns(DeprecationWarning):
                objc.initFrameworkWrapper(
                    "Test",
                    "/Library/Framework/Test.framework",
                    "com.apple.Test",
                    g,
                    inlineTab=inlineTab,
                )

            self.assertEqual(
                load_calls,
                [
                    (
                        Bundle(calls=[("Test", "bridgesupport", "BridgeSupport")]),
                        "Test",
                        g,
                        "/Library/Framework/Test.framework",
                        SENTINEL,
                        True,
                    )
                ],
            )
            self.assertEqual(parse_calls, [])

            # XXX: The following path's aren't properly tested at the moment:
            # 8. Use the 'frameworkResourceName' parameter

    def test_real_loader(self):
        script = os.path.join(os.path.dirname(__file__), "helper_bridgesupport.py")
        path_elem = os.path.dirname(objc.__file__)

        if sys.byteorder == "big":
            if sys.maxsize < 2**32:
                arch = "-ppc"
            else:
                arch = "-ppc64"

        else:
            if sys.maxsize < 2**32:
                arch = "-i386"
            else:
                arch = "-x86_64"

        return  # XXX
        p = subprocess.Popen(
            ["/usr/bin/arch", arch, sys.executable, script, path_elem],
            stdout=subprocess.PIPE,
        )
        stdout, _ = p.communicate()
        if p.returncode != 0:
            self.fail("Selftest failed: %r" % stdout)


class TestMisc(TestCase):
    def test_struct_alias(self):
        tp1 = objc.createStructType("TestStruct1", b'{TestStruct1="f1"d"f2"d}', None)

        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            objc.registerStructAlias(b"{TestStruct2=dd}", tp1)

        # XXX: Disabled for now because this function is used in
        # framework bindings...
        # self.assertTrue(len(w) == 1)
        # self.assertEqual(w[0].category, DeprecationWarning)

        with warnings.catch_warnings(record=True):
            warnings.simplefilter("ignore")
            tp2 = objc.registerStructAlias(b"{TestStruct2=dd}", tp1)
            self.assertIs(tp1, tp2)

        self.assertHasAttr(objc.ivar, "TestStruct1")
        self.assertNotHasAttr(objc.ivar, "TestStruct2")

        tp3 = objc.createStructAlias("TestStruct3", b"{TestStruct3=dd}", tp1)
        self.assertIs(tp1, tp3)
        self.assertHasAttr(objc.ivar, "TestStruct3")

        o = objc.ivar.TestStruct1()
        self.assertEqual(o.__typestr__, b"{TestStruct1=dd}")
        o = objc.ivar.TestStruct3()
        self.assertEqual(o.__typestr__, b"{TestStruct1=dd}")

    def test_ivar_slots(self):
        # XXX: This test is disabled for Python 3.7 because it crashes
        #      the interpreter fairly consistently. See #423
        for name, encoding in [
            ("bool", objc._C_BOOL),
            ("char", objc._C_CHR),
            ("int", objc._C_INT),
            ("short", objc._C_SHT),
            ("long", objc._C_LNG),
            ("long_long", objc._C_LNG_LNG),
            ("unsigned_int", objc._C_UINT),
            ("unsigned_short", objc._C_USHT),
            ("unsigned_long", objc._C_ULNG),
            ("unsigned_long_long", objc._C_ULNG_LNG),
            ("float", objc._C_FLT),
            ("double", objc._C_DBL),
            ("BOOL", objc._C_NSBOOL),
            ("UniChar", objc._C_UNICHAR),
            ("char_text", objc._C_CHAR_AS_TEXT),
            ("char_int", objc._C_CHAR_AS_INT),
        ]:
            with self.subTest(name):
                o = getattr(objc.ivar, name)()
                self.assertIsInstance(o, objc.ivar)
                self.assertEqual(o.__typestr__, encoding)

    def test_resource_stubs(self):
        self.assertTrue(bridgesupport.resource_exists("objc", "__init__.py"))
        self.assertFalse(bridgesupport.resource_exists("objc", "no-such-file"))
        self.assertFalse(
            bridgesupport.resource_exists("no-such-package", "no-such-file")
        )

        data = bridgesupport.resource_string("objc", "__init__.py")
        self.assertIsInstance(data, str)
