"""
A tool to check the contents of a metadata file.

This is mostly meant to look for missing annotation (as far as that can be done
using a tool), but will report on other problems (like bad element/attribute
names) as well.

XXX: How do I recover linenumber information from an ElementTree?
"""
import optparse, sys, objc
from PyObjCMetaData.et import *

gCoreFoundationTypes = [
    # Some commonly used CF-types (to avoid false positives)
    '^{__CFString}',
    'r^{__CFString}',
    '^{__CFData}',
    'r^{__CFData}',
]

default_name_attribute='name'
name_attribute={
    'method': 'selector',
}

mandatory_attributes={
    'struct': ('name',),
    'cftype': ('name',),
    'opaque': ('name',),
    'constant': ('name',),
    'string_constant': ('name', 'value'),
    'enum': ('name',),
    'function': ('name',),
    'function_alias': ('name', 'original'),
    'class': ('name',),
    'informal_protocol': ('name',),
    ('informal_protocol', 'method'): ('selector',),
    ('class', 'method'): ('selector',),
}

valid_attributes={
    'struct': ('name', 'type', 'type64', 'opaque'),
    'cftype': ('name', 'type', 'type64', 'tollfree', 'gettypeid_func'),
    'opaque': ('name', 'type', 'type64'),
    'constant': ('name', 'type', 'type64', 'magic_cookie'),
    'string_constant': ('name', 'value', 'nsstring'),
    'enum': ('name', 'value', 'value64', 'le_value', 'be_value', 'ignore', 'suggestion'),
    'function': ('name', 'variadic', 'inline'),
    'function_alias': ('name', 'original'),
    'class': ('name',),
    'informal_protocol': ('name',),
    ('informal_protocol', 'method'): ('selector', 'type', 'type64', 'class_method'),
    ('class', 'method'): ('selector', 'class_method', 'variadic', 'ignore', 'suggestion', ),
    'arg': ('c_array_length_in_arg', 'c_array_of_fixed_length', 'c_array_delimited_by_null', 'c_array_of_variable_length', 'function_pointer', 'sel_of_type', 'sel_of_type64', 'c_array_length_in_retval', 'type_modifier', 'null_accepted', 'printf_format', 'already_retained', 'type', 'type64', 'index'),
    'retval': ('c_array_length_in_arg', 'c_array_of_fixed_length', 'c_array_delimited_by_null', 'c_array_of_variable_length', 'function_pointer', 'sel_of_type', 'sel_of_type64', 'already_retained', 'type', 'type64'),
}

boolean_attributes={
    'struct': ('opaque',),
    'constant': ('magic_cookie',),
    'string_constant': ('nsstring',),
    'enum': ('ignore',),
    'function': ('variadic', 'inline'),
    ('informal_protocol', 'method'): ('class_method',),
    ('class', 'method'): ('class_method', 'variadic', 'ignore', ),
    'arg': ('c_array_delimitd_by_null', 'c_array_of_variable_length', 'function_pointer', 'c_array_length_in_retval', 'null_accepted', 'printf_format', 'already_retained', ),
    'retval': ('c_array_delimitd_by_null', 'c_array_of_variable_length', 'function_pointer', 'already_retained'),
}

encoding_attributes={
    'struct': ('type', 'type64',),
    'cftype': ('type', 'type64',),
    'opaque': ('type', 'type64',),
    'constant': ('type', 'type64',),
    ('informal_protocol', 'method'): ('type', 'type64'),
    'arg': ('type', 'type64',),
    'retval': ('type', 'type64',),
}

encoding_string_attributes={
    ('informal_protocol', 'method'): ('type', 'type64'),
    'arg': ('sel_of_type', 'sel_of_type64',),
    'retval': ('sel_of_type', 'sel_of_type64',),
}

def name(node):
    return node.get(name_attribute.get(node.tag, default_name_attribute))

def extract_struct_fields(typestr):
    """ Return (structTag, fieldNames) """
    assert typestr[0] == '{'

    # XXX: this is harder than it looks at first, really need a recursive parser here.

    nameend=typestr.find('=')

    if nameend != -1:
        name = typestr[1:nameend]

        return name, () # XXX: this is wrong, as is the code below
        rest = typestr[nameend+1:-1]
        fields = []
        while rest:
            if rest.startswith('"'):
                end = rest.find('"', 1)
            fields.append(rest[1:end])
            rest = rest[end+1:]
            end = rest.find('"')
            if end == -1:
                assert validate_encoding(rest)
                rest = ''

            else:
                assert validate_encoding(rest[:end])
                rest = rest[end:]

        return name, fields

    else:
        name = typestr[1:-1]
        return name, ()

def validate_encoding(typestr):
    """ Return True iff 'typestr' is a valid encoded type """
    if not typestr:
        return False

    # Strip qualifiers
    while typestr and typestr[0] in (objc._C_IN, objc._C_OUT, objc._C_INOUT, objc._C_CONST, objc._C_ONEWAY):
        typestr = typestr[1:]

    if not typestr:
        return False

    if typestr[0] in (objc._C_BOOL, objc._C_CHARPTR, objc._C_CHR, 
            objc._C_CLASS, objc._C_DBL, objc._C_FLT, objc._C_ID, objc._C_INT, 
            objc._C_LNG, objc._C_LNG_LNG, objc._C_NSBOOL, objc._C_SEL, objc._C_SHT, 
            objc._C_UCHR, objc._C_UINT, objc._C_ULNG, objc._C_ULNG_LNG, objc._C_UNDEF, 
            objc._C_USHT):

        return len(typestr) == 1

    elif typestr[0] == objc._C_ARY_B:
        if typestr[-1] != objc._C_ARY_E:
            return False

        typestr = typestr[1:-1]
        if len(typestr) == 0:
            return False

        while typestr and typestr[0].isdigit():
            typestr = typestr[1:]

        if len(typestr) == 0:
            return False

        return validate_encoding(typestr)

    elif typestr[0] == objc._C_STRUCT_B:
        return True
        if typestr[-1] != objc._C_STRUCT_E:
            return False

        typestr = typestr[1:-1]
        if '=' in typestr:
            name = typestr[:typestr.find('=')]
            rest = typestr[typestr.find('=')+1:]
            if rest:
                if rest[0] != '"':
                    fields = objc.splitSignature(rest)
                    for fld in fields:
                        if not validate_signature(fld):
                            return False

                else:
                    while rest:
                        if rest.startswith('"'):
                            end = rest.find('"', 1)
                            fn = rest[1:end]
                            for ch in fn:
                                if fn != '_' and not fn.isalpha() and not fn.isdigit():
                                    return False
                            rest = rest[end+1:]
                            end = rest.find('"')
                            if end == -1:
                                if not validate_encoding(rest):
                                    return False
                                rest = ''

                            else:
                                if not validate_encoding(rest[:end]):
                                    return False
                                rest = rest[end:]
                
            
        else:
            name = typestr

        if name != '?':
            for ch in name:
                if ch != '_' and not ch.isalpha() and not ch.isdigit():
                    return False

        return True

    elif typestr[0] == objc._C_BFLD:
        typestr = typestr[1:]
        if len(typestr) == 0:
            return False
        while typestr and typestr[0].isdigit():
            typestr = typestr[1:]
        return typestr == ''

    return True

def validate_encoding_string(typestr):
    result = True
    try:
        parts = objc.splitSignature(typestr)
    except:
        return False

    for el in parts:
        result = result and validate_encoding(el)
    return result

def basicValidation(tag, element, parent=None):
    valids = valid_attributes.get(element.tag, ())
    if parent is not None:
        valids = valids + valid_attributes.get((parent.tag, element.tag), ())
    for k in element.attrib.keys():
        if k not in valids:
            print "ERROR: %s: illegal attribute: %r"%(
                    tag, k)

    for k in boolean_attributes.get(element.tag, ()):
        v = element.get(k)
        if v is not None:
            if v not in ('true', 'false'):
                print "ERROR: %s: invalid value for attribute %r: %r"%(
                        tag, k, v)

    for k in encoding_attributes.get(element.tag, ()):
        v = element.get(k)
        if v is not None:
            if not validate_encoding(v):
                print "ERROR: %s: invalid type encoding for attribute %r: %r"%(
                        tag, k, v)

    for k in encoding_string_attributes.get(element.tag, ()):
        v = element.get(k)
        if v is not None:
            if not validate_encoding_string(v):
                print "ERROR: %s: invalid parameter encoding for attribute %r: %r"%(
                        tag, k, v)

    if parent is not None:
        for k in boolean_attributes.get((parent.tag, element.tag), ()):
            v = element.get(k)
            if v is not None:
                if v not in ('true', 'false'):
                    print "ERROR: %s: invalid value for attribute %r: %r"%(
                            tag, k, v)

        for k in encoding_attributes.get((parent.tag, element.tag), ()):
            v = element.get(k)
            if v is not None:
                if not validate_encoding(v):
                    print "ERROR: %s: invalid type encoding for attribute %r: %r"%(
                            tag, k, v)

        for k in encoding_string_attributes.get((parent.tag, element.tag), ()):
            v = element.get(k)
            if v is not None:
                if not validate_encoding_string(v):
                    print "ERROR: %s: invalid parameter encoding for attribute %r: %r"%(
                            tag, k, v)


def validateArgRetval(tag, element, numArg):
    length_in_arg = element.get('c_array_length_in_arg')
    fixed_length = element.get('c_array_of_fixed_length')
    null_delimited = element.get('c_array_delimited_by_null')
    variable_length = element.get('c_array_of_variable_length')
    length_in_retval = element.get('c_array_length_in_retval')


    if element.get('null_accepted') is not None:
        tp = element.get('type')
        if tp is not None:
            if tp != '*' and not tp.startswith('^') and not tp.startswith('r^'):
                print "WARNING: %s: null_accepted but no pointer type"%(
                        tag,)


    if length_in_arg is not None:
        if null_delimited is not None:
            print "ERROR: %s: both c_array_length_in_arg and c_array_delimited_by_null"%(tag,)

        if variable_length is not None:
            print "ERROR: %s: both c_array_length_in_arg and c_array_of_variable_length"%(tag,)

        if ',' in length_in_arg:
            v = [ v.strip() for v in length_in_arg.split(',') ]
            if len(v) != 2:
                print "ERROR: %s: Invalid value for c_array_length_in_arg: %r"(
                        tag, length_in_arg)
            try:
                before, after = [ int(v, 10) for v in v ]
            except ValueError:
                print "ERROR: %s: Invalid value for c_array_length_in_arg: %r"(
                        tag, length_in_arg)

            if numArg is not None:
                if not (0 <= before < numArg):
                    print "ERROR: %s: c_array_length_in_arg out of range: %r"(
                        tag, length_in_arg)
                if not (0 <= after < numArg):
                    print "ERROR: %s: c_array_length_in_arg out of range: %r"(
                        tag, length_in_arg)

            if length_in_retval is not None:
                print "ERROR: %s: 2 element c_array_length_in_arg and c_array_length_in_retval present"%(tag,)
        else:
            try:
                v = int(length_in_arg, 10)
            except ValueError:
                print "ERROR: %s: Invalid value for c_array_length_in_arg: %r" % (
                        tag, length_in_arg)

            if numArg is not None:
                if not (0 <= v < numArg):
                    print "ERROR: %s: c_array_length_in_arg out of range: %r" % (
                        tag, length_in_arg)

    if fixed_length is not None:
        if null_delimited is not None:
            print "ERROR: %s: both c_array_of_fixed_length and c_array_delimited_by_null"%(tag,)
        if variable_length is not None:
            print "ERROR: %s: both c_array_of_fixed_length and c_array_of_variable_length"%(tag,)
        try:
            v = int(fixed_length, 10)
        except ValueError:
            print "ERROR: %s: Invalid value for c_array_of_fixed_length: %r"(
                    tag, fixed_length)

    if element.get('type'):
        tp = element.get('type')
        if tp == '*' or tp.startswith('^') or tp.startswith('r^'):
            pass

        else:
            if length_in_arg is not None or fixed_length is not None \
                or null_delimited is not None or variable_length is not None \
                or length_in_retval is not None:


                    print "WARNING: %s: non-pointer and c_array_* annotation"%(
                            tag,)

        if tp != ':':
            if element.get('sel_of_type') is not None \
                    or element.get('sel_of_type64') is not None:

                print "WARNING: %s: non-selector (%s) and sel_of_type annotation"%(
                        tag, element.get('type'))

        if tp.startswith('^') or tp.startswith('r^'):
            if element.tag == 'arg' and element.get('type_modifier') is None:
                if tp not in gCoreFoundationTypes and tp != '^?':
                    print "WARNING: %s: pointer-type (%s) without 'type_modifier'"%(
                        tag, tp)

        if tp == '^?':
            if element.get('function_pointer') != 'true':
                print "WARNING: %s: type '^?', but not a function_pointer"%(
                        tag,)




    modifier = element.get('type_modifier')
    if modifier is not None:
        if modifier not in ('n', 'N', 'o'):
            print "ERROR: %s: Invalid value for 'type_modifier'"%(
                    tag,)

    if element.get('print_format', 'false') == 'true':
        tp = element.get('type')
        if tp is not None:
            if type not in ('*', '@'):
                print "WARNING: %s: print_format but type not string or object"%(
                        tag,)
def main():
    parser = optparse.OptionParser(version="%prog 0.1")
    parser.add_option("-f", "--file", dest="filename", metavar="FILE",
       help="check the given file")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
        default=False, help="Be more verbose")


    options, args = parser.parse_args()
    if args:
        parser.error("incorrect number of arguments")

    if options.filename is None:
        parser.error("You must specify the filename to check")


    try:
        doc = ET.parse(options.filename).getroot()
    except Exception, e:
        print 'ERROR: Parsing the metadata file failed: %s'%(e,)
        sys.exit(1)

    if doc.tag != 'signatures':
        print 'ERROR: Document tag is not "signatures"'
        sys.exit(1)

    version = doc.get('version')
    if version is not None:
        if version not in ('0.9', '1.0'):
            print "WARNING: Unexpected metadata version: %s"%(version,)

    for k in doc.attrib.keys():
        if k != 'version':
            print "ERROR: %r: illegal attribute %r"%(doc.tag, k)

    for element in doc.getchildren():
        nametag = name_attribute.get(element.tag, default_name_attribute)
        if element.get(nametag) is None:
            print "ERROR: %r without a %r"%(element.tag, nametag)
            continue

        basicValidation("%s %r"%(element.tag, name(element)), element)


        if element.tag == 'enum':
            # TODO: 
            # - check if we have at least one of the value attributes
            # - check that the values are decimal numbers (either integer or 
            #   float)
            value = element.get('value')
            value64 = element.get('value64')
            le_value = element.get('le_value')
            be_value = element.get('be_value')

            if len(list(element.getchildren())) != 0:
                print "ERROR: %s %r: Subelements present"%(
                        element.tag, name(element))

            if le_value is not None or be_value is not None:
                if le_value is None or be_value is None:
                    print "WARNING: %s %r: both be_value and le_value should be present" %(
                            element.tag, name(element))
                if value is not None:
                    print "WARNING: %s %r: both 'value' and byte-order specific data"%(element.tag, name(element))
                if value64 is not None:
                    print "WARNING: %s %r: both 'value64' and byte-order specific data"%(element.tag, name(element))

            if value is not None and value != '':
                if '.' in value:
                    try:
                        v = float(value)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'value'"%(element.tag, name(element))
                else:
                    try:
                        v = int(value, 10)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'value'"%(element.tag, name(element))
            if value64 is not None and value64 != '':
                if '.' in value64:
                    try:
                        v = float(value64)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'value64'"%(element.tag, name(element))
                else:
                    try:
                        v = int(value64, 10)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'value64'"%(element.tag, name(element))
            if le_value is not None and le_value != '':
                if '.' in le_value:
                    try:
                        v = float(le_value)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'le_value'"%(element.tag, name(element))
                else:
                    try:
                        v = int(le_value, 10)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'le_value'"%(element.tag, name(element))
            if be_value is not None and be_value != '':
                if '.' in be_value:
                    try:
                        v = float(be_value)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'be_value'"%(element.tag, name(element))
                else:
                    try:
                        v = int(be_value, 10)
                    except ValueError:
                        print "WARNING: %s %r: invalid value for 'be_value'"%(element.tag, name(element))

            if not value and not value64 and not le_value and not be_value:
                print "ERROR: %s %r: no value specified"%(element.tag, name(element))

        elif element.tag == 'struct':
            type = element.get('type')
            type64 = element.get('type64')
            if len(list(element.getchildren())) != 0:
                print "ERROR: %s %r: Subelements present"%(
                        element.tag, name(element))

            if not type and not type64:
                print "ERROR: %s %r: no type specified"%(element.tag, name(element))


            if type is None:
                tag, fields = None, None

            elif not type.startswith('{'):
                print "ERROR: %s %r: Encoded 'type' is not for a struct"%(
                    element.tag, name(element))
                tag, fields = None, None
            else:
                try:
                    tag, fields = extract_struct_fields(type)

                except ValueError:
                    print "ERROR: %s %r: invalid type encoding for %r"%(
                        element.tag, name(element), 'type')
                    tag, fields = None, None

            if type64 is None:
                tag64, fields64 = None, None

            elif not type64.startswith('{'):
                print "ERROR: %s %r: Encoded 'type64' is not for a struct"%(
                    element.tag, name(element))
                tag64, fields64 = None, None
            else:
                try:
                    tag64, fields64 = extract_struct_fields(type64)

                except ValueError:
                    print "ERROR: %s %r: invalid type encoding for %r"%(
                            element.tag, name(element), 'type64')
                    tag64, fields64 = None, None

            if fields is not None and fields64 is not None:
                if fields != fields64:
                    print "WARNING: %s %r: Inconsistent field names between 'type' and 'type64'"%(element.tag, name(element))

            if tag == '?':
                print "WARNING %s %r: Empty struct tag in attribute 'type'"%(element.tag, name(element))

            if tag64 == '?':
                print "WARNING %s %r: Empty struct tag in attribute 'type64'"%(element.tag, name(element))


        elif element.tag == 'cftype':
            type = element.get('type')
            type64 = element.get('type64')
            if len(list(element.getchildren())) != 0:
                print "ERROR: %s %r: Subelements present"%(
                        element.tag, name(element))

            if not type and not type64:
                print "ERROR: %s %r: no type information"%(element.tag, name(element))
            tollfree = element.get('tollfree')
            if tollfree is not None:
                if not tollfree:
                    print "WARNING: %s %r: empty value for 'tollfree'"%(
                            element.tag, name(element))
            else:
                if not element.get('gettypeid_func'):
                    # This will trigger false positives because Apple APIs are
                    # incomplete (on purpose).
                    print "WARNING: %s %r: not 'tollfree', but no 'gettypeid_func' either'"%(element.tag, name(element))

            if type is not None:
                gCoreFoundationTypes.append(type)

        elif element.tag == 'constant':
            type = element.get('type')
            type64 = element.get('type64')
            if len(list(element.getchildren())) != 0:
                print "ERROR: %s %r: Subelements present"%(
                        element.tag, name(element))

            if not type and not type64:
                print "ERROR: %s %r: no type information"%(element.tag, name(element))

        elif element.tag == 'function':
            arglist =  list(element.getchildren())
            if len(arglist) == 0:
                print "WARNING: %s %r:no argument/retval type information"%(
                        element.tag, name(element))

            seen_retval = False
            argIdx = 0
            argCount = len([a for a in arglist if a.tag == 'arg' ])
            for a in arglist:
                if a.tag not in ('arg', 'retval'):
                    print "ERROR: %s %r: Illegal subelement: %r"%(
                            element.tag, name(element), a.tag)
                    continue

                elif a.tag == 'retval':
                    if seen_retval:
                        print "ERROR: %s %r: Multiple 'retval' subelements"%(
                                element.tag, name(element))
                    seen_retval = True
                    basicValidation('%s %r (retval)'%(
                        element.tag, name(element)), a)
                    validateArgRetval('%s %r (retval)'%(
                        element.tag, name(element)), a, argCount)

                elif a.tag == 'arg':
                    if a.get('index') is not None:
                        print "ERROR: %s %r: Index attribute on argument %d"%(
                                element.tag, name(element), argIdx)
                    basicValidation('%s %r (arg %d)'%(
                        element.tag, name(element), argIdx), a)
                    validateArgRetval('%s %r (arg %d)'%(
                        element.tag, name(element), argIdx), a, argCount)

                    argIdx += 1


        elif element.tag == 'informal_protocol':
            for method in element.getchildren():
                if method.tag != 'method':
                    print "ERROR: %s %r: Illegal subtag: %r"%(
                            element.tag, name(element), method.tag)
                    continue

                if method.get('selector') is None:
                    print "ERROR: %s %r: method without 'selector'"%(
                            element.tag, name(element))

                basicValidation('%s %r: %s %r'%(
                    element.tag, name(element), method.tag, name(method)),
                    method, element)

                arglist = list(method.getchildren())
                if len(arglist) != 0:
                        print "ERROR: %s %r: %s %r: Subelements present"%(
                                element.tag, name(element), method.tag, name(method))

        elif element.tag == 'class':
            for method in element.getchildren():
                if method.tag != 'method':
                    print "ERROR: %s %r: Illegal subtag: %r"%(
                            element.tag, name(element), method.tag)
                    continue

                if method.get('selector') is None:
                    print "ERROR: %s %r: method without 'selector'"%(
                            element.tag, name(element))

                basicValidation('%s %r: %s %r'%(
                    element.tag, name(element), method.tag, name(method)),
                    method, element)

                seen_retval = False
                arglist = method.getchildren()
                for a in arglist:
                    if a.tag not in ('arg', 'retval'):
                        print "ERROR: %s %r: %s %r: Illegal subelement: %r"%(
                                element.tag, name(element), method.tag, name(method), a.tag)
                        continue

                    elif a.tag == 'retval':
                        if seen_retval:
                            print "ERROR: %s %r: %s %r: Multiple 'retval' subelements"%(
                                    element.tag, name(element), method.tag, name(method))
                        seen_retval = True
                        basicValidation('%s %r: %s %r (retval)'%(
                            element.tag, name(element), method.tag, name(method)), a)
                        validateArgRetval('%s %r: %s %r (retval)'%(
                            element.tag, name(element), method.tag, name(method)), a, None)

                    elif a.tag == 'arg':
                        if a.get('index') is None:
                            print "ERROR: %s %r: %s %r: Missing index attribute on argument"%(
                                    element.tag, name(element), method.tag, name(method))
                        else:
                            v = a.get('index')
                            try:
                                v = int(v, 10)
                            except ValueError:
                                print "ERROR: %s %r: %s %r: Invalid index argument: %s"(
                                        element.tag, name(element), method.tag, name(method),
                                        v)

                        basicValidation('%s %r: %s %r (arg %s)'%(
                            element.tag, name(element), method.tag, name(method), a.get('index')), a)
                        validateArgRetval('%s %r: %s %r (arg %s)'%(
                            element.tag, name(element), method.tag, name(method), a.get('index')), a, None)

        else:
            if element.tag not in valid_attributes:
                print "ERROR: illegal tag: %r"%(element.tag,)
            elif len(list(element.getchildren())) != 0:
                print "ERROR: %s %r:Subelements present"%(
                        element.tag, name(element))

    
if __name__ == "__main__":
    main()
