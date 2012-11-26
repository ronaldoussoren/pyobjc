from PyObjCTools.TestSupport import *

import objc._bridgesupport as bridgesupport
import os
import re
import sys
import imp
import ctypes

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

TEST_XML="""\
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
  <string_constant name='strconst1' value='string constant1' />
  <string_constant name='strconst2' value='string constant 2' value64='string constant two' />
  <string_constant name='strconst1u' value='string constant1 unicode' nsstring='true' />
  <string_constant name='strconst2u' value='string constant 2 unicode' value64='string constant two unicode' nsstring='true' />
  <string_constant name='strconst3' /><!-- ignore -->
  <string_constant name='strconst4' nsstring='true' /><!-- ignore -->
  <string_constant name='strconst5' value64='string five' /><!-- ignore 32-bit -->
  <string_constant name='strconst6' value64='string five unicode' nsstring='true' /><!-- ignore 32-bit -->
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
  <enum name='enum9' value='2.5' />
  <enum name='enum10' value='0x1.5p+3' />
  <enum /><!-- ignore -->
  <null_const name='null1' />
  <null_const /><!-- ignore -->
  <function_pointer name='func1' original='orig_function' />
  <function_pointer name='func2' /><!-- ignore -->
  <function_pointer original='func3' /><!-- ignore -->
  <function_pointer /><!-- ignore -->
  <cftype name='CFProxy1Ref' type='^{CFProxy}' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy2Ref' type='^{CFProxy32}' type64='^{CFProxy64}' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy3Ref' type='^{CFProxy3}' tollfree='NSProxy' gettypeid_func='CFArrayGetTypeID' />
  <cftype name='CFProxy4Ref' type='^{CFProxy4}' tollfree='NSProxy2' />
  <cftype name='CFProxy5Ref' type='^{CFProxy}' gettypeid_func='NoSuchFunction' /><!-- tollfree to CFTypeRef -->
  <cftype name='CFProxy6Ref' type='^{CFProxy}' />
  <cftype name='CFProxy7Ref' type='^{CFProxy32}' type64='^{CFProxy64}' />
  <cftype type='^{CFProxy}' gettypeid_func='CFArrayGetTypeID' /><!-- ignore -->
  <cftype name='CFProxy8Ref' gettypeid_func='CFArrayGetTypeID' /><!-- ignore -->
  <cftype name='CFProxy9Ref' type64='^{CFProxy64}' gettypeid_func='CFArrayGetTypeID' /><!-- ignore 32-bit -->
  <cftype/><!-- ignore -->
  <class name='MyClass1'></class>
  <class /><!-- ignore -->
  <class name='MyClass2'>
    <method selector='method1' classmethod='true' ></method>
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
       <retval null_accepted='false' already_retained='true' c_array_length_in_result='true' />
    </method>
    <method selector='method16'>
       <retval c_array_delimited_by_null='true' already_cfretained='true' c_array_of_variable_length='true' printf_format='true' free_result='true' />
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
       <arg index='1' null_accepted='false' already_retained='true' c_array_length_in_result='true' />
    </method>
    <method selector='method16'>
       <arg index='1' c_array_delimited_by_null='true' already_cfretained='true' c_array_of_variable_length='true' printf_format='true' free_result='true' />
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
       <arg index='1' function_pointer_retained='true'/><!-- ignored, no function data -->
    </method>
    <method selector='method21'>
       <arg index='1' function_pointer_retained='true' function_pointer='true'>
          <retval type='v' />
          <arg type='@' />
          <arg type='d' />
       </arg>
    </method>
    <method selector='method22'>
       <arg index='1' function_pointer_retained='true' block='true'>
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
    <method selector='method24'>
       <arg index='1' block='true' classmethod='true'>
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
  <function name='function3' variadic='true' c_array_delimited_by_null='true'></function>
  <function name='function4' variadic='true' c_array_length_in_arg='4'></function>
  <function name='function5' c_array_delimited_by_null='true'><retval type='d'/></function><!-- c_array... ignored -->
  <function name='function6' c_array_length_in_arg='4'><retval type='d' /></function><!-- c_array... ignored -->
  <function name='function7' ignore='true'></function>
  <function name='function8' ignore='true' suggestion='ignore me'></function>
  <function name='function9' suggestion='ignore me'><retval type='d'/></function><!-- suggestion ignored -->
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
     <retval type_modifier='n' />
  </function>
  <function name='function14'>
     <retval sel_of_type='v@:f' c_array_of_fixed_length='4'/>
  </function>
  <function name='function15'>
     <retval sel_of_type='v@:f' sel_of_type64='v@:d' />
  </function>
  <function name='function16'>
     <retval null_accepted='false' already_retained='true' already_cfretained='true' c_array_length_in_result='true' />
  </function>
  <function name='function17'>
     <retval c_array_delimited_by_null='true' c_array_of_variable_length='true' printf_format='true' free_result='true' />
  </function>
  <function name='function18'>
     <retval c_array_length_in_arg='1'/>
  </function>
  <function name='function19'>
     <retval c_array_length_in_arg='1,2'/>
  </function>
  <function name='function20'>
     <retval c_array_length_in_arg='4, 5'/>
  </function>
  <function name='function21'>
     <retval function_pointer_retained='true'/><!-- ignored, no function data -->
  </function>
  <function name='function22'>
     <retval function_pointer_retained='true' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function23'>
     <retval function_pointer_retained='true' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function24'>
     <retval function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function25'>
     <retval block='true'>
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
  <function name='function28'>
     <arg type='d'/><!-- ignored: no index -->
  </function>
  <function name='function29'>
     <arg index='1' type='d'/>
  </function>
  <function name='function30'>
     <arg index='1' type='f' type64='d' />
  </function>
  <function name='function31'>
     <arg index='1'/><!-- ignore -->
  </function>
  <function name='function32'>
     <arg index='1' type_modifier='n' />
  </function>
  <function name='function33'>
     <arg index='1' sel_of_type='v@:f' c_array_of_fixed_length='4'/>
  </function>
  <function name='function34'>
     <arg index='1' sel_of_type='v@:f' sel_of_type64='v@:d' />
  </function>
  <function name='function35'>
     <arg index='1' null_accepted='false' already_retained='true' already_cfretained='true' c_array_length_in_result='true' />
  </function>
  <function name='function36'>
     <arg index='1' c_array_delimited_by_null='true' c_array_of_variable_length='true' printf_format='true' free_result='true' />
  </function>
  <function name='function37'>
     <arg index='1' c_array_length_in_arg='1'/>
  </function>
  <function name='function38'>
     <arg index='1' c_array_length_in_arg='1,2'/>
  </function>
  <function name='function39'>
     <arg index='1' c_array_length_in_arg='4, 5'/>
  </function>
  <function name='function40'>
     <arg index='1' function_pointer_retained='true'/><!-- ignored, no function data -->
  </function>
  <function name='function41'>
     <arg index='1' function_pointer_retained='true' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function42'>
     <arg index='1' function_pointer_retained='true' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function43'>
     <arg index='1' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function44'>
     <arg index='1' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <!-- TODO: type rewriting (_C_BOOL, _C_NSBOOL)-->
  <informal_protocol/><!-- ignore -->
  <informal_protocol name='protocol1' />
  <informal_protocol name='protocol1' >
    <method selector='selector1' type='v@:f' type64='v@:d' />
    <method selector='selector2' type='v@:f' type64='v@:d' classmethod='false' />
    <method selector='selector3' type='v@:f' type64='v@:d' classmethod='true' />
    <method selector='selector4' type='v@:f' type64='v@:d' variadic='true' /><!-- 'variadic' is ignored -->
    <method selector='selector5' /><!-- ignore: no type -->
    <method selector='selector6' type64='v@:@' /><!-- ignore 32-bit -->
    <method selector='selector7' type='v@:f' type64='v@:d' class_method='false' /><!-- manpage: class_method, pyobjc 2.3: classmethod -->
    <method selector='selector8' type='v@:f' type64='v@:d' class_method='true' />
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
</signatures>
"""

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

    def _test_xml_structure_variants(self):
        # Run 'verify_xml_structure' for all cpu variant 
        # (big/little endian,  32- en 64-bit)
        orig_byteorder = sys.byteorder
        orig_maxsize = sys.maxsize

        try:
            for is32bit in (True, False):
                for endian in ('little', 'big'):
                    sys.maxsize = 2**63-1 if endian == 'big' else 2**32-1
                    sys.byteorder = endian

                    # Reload the bridgesupport module because
                    # it contains conditional definitions
                    imp.reload(bridgesupport)

                    self.verify_xml_structure()

        finally:
            sys.byteorder = orig_byteorder 
            sys.maxsize = orig_maxsize

            # See above
            imp.reload(bridgesupport)

    def test_verify_xml_structure(self):
        prs = self.assert_valid_bridgesupport('TestXML', TEST_XML)

        all_constants = [
            ('constant1', b'@', False,),
            ('constant2', b'I' if sys.maxsize < 2**32 else 'Q' , False,),
            ('constant5', objc._C_NSBOOL, False,),
            ('constant6', objc._C_BOOL, False,),
            ('constant7', b'@', False,),
            ('constant8', b'@', True,),
        ]
        if sys.maxsize > 2**32:
            all_constants.append(
                ('constant4', b'Q', False)
            )

        all_values = {
            'strconst1': b'string constant1',
            'strconst2': b'string constant 2' if sys.maxsize < 2**32 else b'string constant two',
            'strconst1u': b'string constant1 unicode'.decode('ascii'),
            'strconst2u': b'string constant 2 unicode'.decode('ascii') if sys.maxsize < 2**32 else b'string constant two unicode'.decode('ascii'),
            'enum1': 1,
            'enum2': 3 if sys.maxsize < 2**32 else 4,
            'enum3': 5 if sys.byteorder == 'little' else 6,
            'enum4': 7,
            'enum9': 2.5,
            'enum10': 10.5,
            'null1': None,
        }
        if sys.maxsize > 2**32:
            all_values['strconst5'] = b'string five'
            all_values['strconst6'] = b'string five unicode'.decode('ascii')
            all_values['enum6'] = 4

        if sys.byteorder == 'little':
            all_values['enum8'] = 5
        else:
            all_values['enum7'] = 6

        all_opaque = [
            ('opaque1', b'^{opaque1}'),
            ('opaque2', b'^{opaque2=f}' if sys.maxsize < 2**32 else b'^{opaque2=d}'),
        ]
        if sys.maxsize > 2**32:
          all_opaque.append(
              ('opaque4', b'^{opaque4=d}'),
          )

        all_func_aliases = [
            ('func1', 'orig_function'),
        ]

        a = objc.lookUpClass('NSArray').alloc().init()
        CFArrayTypeID = a._cfTypeID()
        all_cftypes = [
            ( 'CFProxy1Ref', b'^{CFProxy}', CFArrayTypeID),
            ( 'CFProxy2Ref', b'^{CFProxy32}' if sys.maxint < 2**32 else b'^{CFProxy64}', CFArrayTypeID),
            ( 'CFProxy3Ref', b'^{CFProxy3}', None, 'NSProxy'),
            ( 'CFProxy4Ref', b'^{CFProxy4}', None, 'NSProxy2'),
            ( 'CFProxy5Ref', b'^{CFProxy}', None, 'NSCFType'),
            ( 'CFProxy6Ref', b'^{CFProxy}', None, 'NSCFType'),
            ( 'CFProxy7Ref',  b'^{CFProxy32}' if sys.maxint < 2**32 else b'^{CFProxy64}', None, 'NSCFType' ),
        ]
        if sys.maxsize > 2**32:
            all_cftypes.append(
                ( 'CFProxy9Ref',  b'^{CFProxy64}', CFArrayTypeID),
            )


        all_methods = {
            (b'MyClass2', b'method2', False): { 'variadic': True },
            (b'MyClass2', b'method3', False): { 'variadic': True,  'c_array_delimited_by_null': True },
            (b'MyClass2', b'method4', False): { 'variadic': True,  'c_array_length_in_arg': 4+2 },
            (b'MyClass2', b'method5', False): { 'retval': { 'type': b'd' } },
            (b'MyClass2', b'method6', False): { 'retval': { 'type': b'd' } },
            (b'MyClass2', b'method7', False): { 'suggestion': "don't use this method" },
            (b'MyClass2', b'method8', False): { 'suggestion': 'ignore me' },
            (b'MyClass2', b'method9', False): { 'suggestion': 'ignore me' },
            (b'MyClass2', b'method10', False ): { 'retval': { 'type': b'd' } },
            (b'MyClass2', b'method11', False ): {
                'retval': { 
                    'type': b'f' if sys.maxsize < 2**32 else b'd'
                }
            },
            (b'MyClass2', b'method13', True): { 'retval': { 'type_modifier': b'n' } },
            (b'MyClass2', b'method13b', False): {
                'retval': { 'sel_of_type': b'v@:f', 'c_array_of_fixed_length': 4 },
            },
            (b'MyClass2', b'method14', False): {
                'retval': { 'sel_of_type': b'v@:f' if sys.maxsize < 2**32 else b'v@:d' }
            },
            (b'MyClass2', b'method15', False): {
                'retval': { 'null_accepted': False, 'already_retained': True,  }
            },
            (b'MyClass2', b'method16', False): {
                'retval': { 'c_array_delimited_by_null': True, 'c_array_of_variable_length': True, 'printf_format': True,  
                            'free_result': True, 'already_cfretained': True }
            },
            (b'MyClass2', b'method17', False): {
                'retval': { 'c_array_length_in_arg': 1+2 }
            },
            (b'MyClass2', b'method18', False): {
                'retval': { 'c_array_length_in_arg': (1+2, 2+2) }
            },
            (b'MyClass2', b'method19', False): {
                'retval': { 'c_array_length_in_arg': (4+2, 5+2) }
            },
            (b'MyClass2', b'method21', False): {
                'retval': { 'function_pointer_retained': True, 'callable': {
                    'retval': { 'type': b'v' },
                    'arguments': { 
                        0: b'@',
                        1: b'd',
                    }
                }}
            },
            (b'MyClass2', b'method22', False): {
                'retval': { 'function_pointer_retained': True, 'callable': {
                    'retval': { 'type': b'v' },
                    'arguments': { 
                        0: { 'type': b'@' },
                        1: { 'type': b'd' },
                    }
                }}
            },
            (b'MyClass2', b'method23', False): {
                'retval': { 'callable': {
                    'retval': { 'type': b'v' },
                    'arguments': {
                        0: { 'type': b'@' },
                        1: { 'type': b'd' },
                    }
                }}
            },
            (b'MyClass2', b'method24', False): {
                'retval': { 'callable': {
                    'retval': { 'type': b'v' },
                    'arguments': {
                        0: { 'type': b'@' },
                        1: { 'type': b'd' },
                    }
                }}
            },
            (b'MyClass3', b'method7', False): {
                'retval': { 'type': b'q' },
                'arguments': {
                    2+1: { 'type': b'f' },
                    2+2: { 'type': b'd' },
                }
            },
            (b'MyClass3', b'method8', False): {
                'arguments': {
                    2+1: { 'type': b'd' },
                    2+2: { 'type': b'd' },
                }
            },
            (b'MyClass3', b'method10', False): {
                'arguments': {
                    2+1: { 'type': b'd' }
                }
            },
            (b'MyClass3', b'method11', False): {
                'arguments': {
                    2+1: { 'type': b'f' if sys.maxsize < 2**32 else b'd' }
                }
            },
            (b'MyClass3', b'method13', False): {
                'arguments': {
                    2+1: { 'type_modifier': b'n' },
                }
            },
            (b'MyClass3', b'method13b', False): {
                'arguments': {
                    2+1: { 'sel_of_type': b'v@:f', 'c_array_of_fixed_lengt': 4 }
                }
            },
            (b'MyClass3', b'method14', False): {
                'arguments': {
                    2+1: { 'sel_of_type': b'v@:f' if sys.maxsize < 2**32 else b'v@:d' }
                }
            },
            (b'MyClass3', b'method15', False): {
                'arguments': {
                    2+1: { 'null_accepted': False, 'already_retained': True, 
                           'c_array_length_in_result': True }
                }
            },
            (b'MyClass3', b'method16', False): {
                'arguments': {
                    2+1: { 'c_array_delimited_by_null': True, 'c_array_of_variable_length': True, 
                           'printf_format': True, 'free_result': True, 'already_cfretained': True }
                }
            },
            (b'MyClass3', b'method17', False): {
                'arguments': {
                    2+1:  { 'c_array_length_in_arg': 1+2 },
                }
            },
            (b'MyClass3', b'method18', False): {
                'arguments': {
                    2+1:  { 'c_array_length_in_arg': (1+2, 2+2) }
                }
            },
            (b'MyClass3', b'method19', False): {
                'arguments': {
                    2+1:  { 'c_array_length_in_arg': (4+2, 5+2) }
                }
            },
            (b'MyClass3', b'method21', False): {
                'arguments': {
                    2+1: { 'callable_retained': True, 'callable': {
                        'retval': { 'type': b'v' },
                        'arguments': {
                            0:  { 'type': b'@' },
                            1:  { 'type': b'd' },
                        }
                    }}
                }
            },
            (b'MyClass3', b'method22', False): {
                'arguments': {
                    2+1: { 'callable_retained': True, 'callable': {
                        'retval': { 'type': b'v' },
                        'arguments': {
                            0:  { 'type': b'@' },
                            1:  { 'type': b'd' },
                        }
                    }}
                }
            },
            (b'MyClass3', b'method23', False): {
                'arguments': {
                    2+1: { 'callable': {
                        'retval': { 'type': b'v' },
                        'arguments': {
                            0:  { 'type': b'@' },
                            1:  { 'type': b'd' },
                        }
                    }}
                }
            },
            (b'MyClass3', b'method23', False): {
                'arguments': {
                    2+1: { 'callable': {
                        'retval': { 'type': b'v' },
                        'arguments': {
                            0:  { 'type': b'@' },
                            1:  { 'type': b'd' },
                        }
                    }}
                }
            },
        }      

        self.assertItemsEqual(prs.constants,    all_constants)
        self.assertEqual(prs.values,            all_values)
        self.assertItemsEqual(prs.opaque,       all_opaque)
        self.assertItemsEqual(prs.func_aliases, all_func_aliases)
        self.assertItemsEqual(prs.cftypes,      all_cftypes)

        self.maxDiff = None
        self.assertEqual(prs.meta,              all_methods)
        self.fail("validate the metadata from TEST_XML")

        '''
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
  <function name='function3' variadic='true' c_array_delimited_by_null='true'></function>
  <function name='function4' variadic='true' c_array_length_in_arg='4'></function>
  <function name='function5' c_array_delimited_by_null='true'><retval type='d'/></function><!-- c_array... ignored -->
  <function name='function6' c_array_length_in_arg='4'><retval type='d' /></function><!-- c_array... ignored -->
  <function name='function7' ignore='true'></function>
  <function name='function8' ignore='true' suggestion='ignore me'></function>
  <function name='function9' suggestion='ignore me'><retval type='d'/></function><!-- suggestion ignored -->
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
     <retval type_modifier='n' />
  </function>
  <function name='function14'>
     <retval sel_of_type='v@:f' c_array_of_fixed_length='4'/>
  </function>
  <function name='function15'>
     <retval sel_of_type='v@:f' sel_of_type64='v@:d' />
  </function>
  <function name='function16'>
     <retval null_accepted='false' already_retained='true' already_cfretained='true' c_array_length_in_result='true' />
  </function>
  <function name='function17'>
     <retval c_array_delimited_by_null='true' c_array_of_variable_length='true' printf_format='true' free_result='true' />
  </function>
  <function name='function18'>
     <retval c_array_length_in_arg='1'/>
  </function>
  <function name='function19'>
     <retval c_array_length_in_arg='1,2'/>
  </function>
  <function name='function20'>
     <retval c_array_length_in_arg='4, 5'/>
  </function>
  <function name='function21'>
     <retval function_pointer_retained='true'/><!-- ignored, no function data -->
  </function>
  <function name='function22'>
     <retval function_pointer_retained='true' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function23'>
     <retval function_pointer_retained='true' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function24'>
     <retval function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </retval>
  </function>
  <function name='function25'>
     <retval block='true'>
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
  <function name='function28'>
     <arg type='d'/><!-- ignored: no index -->
  </function>
  <function name='function29'>
     <arg index='1' type='d'/>
  </function>
  <function name='function30'>
     <arg index='1' type='f' type64='d' />
  </function>
  <function name='function31'>
     <arg index='1'/><!-- ignore -->
  </function>
  <function name='function32'>
     <arg index='1' type_modifier='n' />
  </function>
  <function name='function33'>
     <arg index='1' sel_of_type='v@:f' c_array_of_fixed_length='4'/>
  </function>
  <function name='function34'>
     <arg index='1' sel_of_type='v@:f' sel_of_type64='v@:d' />
  </function>
  <function name='function35'>
     <arg index='1' null_accepted='false' already_retained='true' already_cfretained='true' c_array_length_in_result='true' />
  </function>
  <function name='function36'>
     <arg index='1' c_array_delimited_by_null='true' c_array_of_variable_length='true' printf_format='true' free_result='true' />
  </function>
  <function name='function37'>
     <arg index='1' c_array_length_in_arg='1'/>
  </function>
  <function name='function38'>
     <arg index='1' c_array_length_in_arg='1,2'/>
  </function>
  <function name='function39'>
     <arg index='1' c_array_length_in_arg='4, 5'/>
  </function>
  <function name='function40'>
     <arg index='1' function_pointer_retained='true'/><!-- ignored, no function data -->
  </function>
  <function name='function41'>
     <arg index='1' function_pointer_retained='true' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function42'>
     <arg index='1' function_pointer_retained='true' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function43'>
     <arg index='1' function_pointer='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <function name='function44'>
     <arg index='1' block='true'>
        <retval type='v' />
        <arg type='@' />
        <arg type='d' />
     </arg>
  </function>
  <!-- TODO: type rewriting (_C_BOOL, _C_NSBOOL)-->
  <informal_protocol/><!-- ignore -->
  <informal_protocol name='protocol1' />
  <informal_protocol name='protocol1' >
    <method selector='selector1' type='v@:f' type64='v@:d' />
    <method selector='selector2' type='v@:f' type64='v@:d' classmethod='false' />
    <method selector='selector3' type='v@:f' type64='v@:d' classmethod='true' />
    <method selector='selector4' type='v@:f' type64='v@:d' variadic='true' /><!-- 'variadic' is ignored -->
    <method selector='selector5' /><!-- ignore: no type -->
    <method selector='selector6' type64='v@:@' /><!-- ignore 32-bit -->
    <method selector='selector7' type='v@:f' type64='v@:d' class_method='false' /><!-- manpage: class_method, pyobjc 2.3: classmethod -->
    <method selector='selector8' type='v@:f' type64='v@:d' class_method='true' />
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
</signatures>
'''

    def assertIsIdentifier(self, value):
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

            key = "c_array_of_fixed_length"
            if key in meta["retval"]:
                self.assertIsInstance(meta["retval"][key], (int, long))

            key = "c_array_length_in_arg"
            if key in meta["retval"]:
                if isinstance(meta["retval"][key], tuple):
                    self.assertEqual(len(meta["retval"][key]), 2)
                    self.assertTrue(all(isinstance(x, (int, long)) for x in meta["retval"][key]))
                else:
                    self.assertIsInstance(meta["retval"][key], (int, long))

            for key in ("c_array_delimited_by_null", "printf_format", "c_array_of_variable_length", "null_accepted"):
                if key in meta["retval"]:
                    self.assertIsInstance(meta["retval"][key], bool)


            self.assertNotIn("c_array_length_in_result", meta["retval"])
            self.assertEqual(set(meta["retval"]) - valid_keys, set())

        if 'arguments' in meta:
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
            self.assertEqual(set(meta.keys()) - {"arguments", "retval", "variadic", "classmethod",
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
            self.assertEqual(set(meta.keys()) - {"arguments", "retval", "variadic", "suggestion", "classmethod" }, set())

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

        for clsname, selname, is_class in prs.meta:
            meta = prs.meta[(clsname, selname, is_class)]
            self.assertIsInstance(clsname, bytes)
            self.assertIsInstance(is_class, bool)
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
            self.assertIsInstance(prs.values[name], (basestring, long, int, float, bytes, type(None)))

        return prs


if __name__ == "__main__":
    main()
