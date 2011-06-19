"""
Helper script for compiling .brigesupport files into a more compact form

Note: the format of the compiled data is unstable for now, new versions
of PyObjC can and will use different formats.
"""
import getopt
import sys
from xml.etree import ElementTree
import os
import time
import json

import objc

gUsage = "Usage: pyobjc-compile-bridgesupport --input=FILE --output=FILE"

class bstr(str):
    __slots__ = ()

    def __repr__(self):
        result = super(bstr, self).__repr__()
        if result.startswith('b'):
            return result
        return 'b' + result

class funccall (object):
    def __init__(self, name, args=None, kwds=None):
        self._name = name

        self._args = ()
        self._kwds = {}

        if args is not None:
            self._args = args
        if kwds is not None:
            self._kwds = kwds

    def __call__(self, *args, **kwds):
        self._args = args
        self._kwds = kwds

    def __repr__(self):
        result = [self._name, '(']
        for a in self._args:
            if result[-1] != '(':
                result.append(', ')
            result.append(repr(a))

        for k, v in self._kwds.iteritems():
            if result[-1] != '(':
                result.append(', ')
            result.append(k)
            result.append('=')
            result.append(repr(v))
        result.append(')')
        return ''.join(result)

def sel32or64(a, b):
    return funccall('sel32or64', (a, b))

def littleOrBig(a, b):
    return funccall('littleOrBig', (a, b))


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'Vh?i:o:', ['version', 'help', 'input=', 'output='])

    except getopt.error,  msg:
        print >>sys.stderr, msg
        print >>sys.stderr, gUsage
        sys.exit(1)

    input = None
    output = None

    if args:
        print >>sys.stderr, "Additional arguments"
        print >>sys.stderr, gUsage
        sys.exit(1)

    for k, v in opts:
        if k in ('-V', '--version'):
            print "pyobjc %s"%(objc.__version__,)
            sys.exit(0)

        elif k in ('-h', '-?', '--help'):
            print gUsage
            sys.exit(0)

        elif k in ('-i', '--input'):
            input = v

        elif k in ('-o', '--output'):
            output = v 

        else:
            raise RuntimeError("Unhandled command-line option")


    if input is None or output is None:
        print >>sys.stderr, "Specify input and output files"
        print >>sys.stderr, gUsage
        sys.exit(1)

    try:
        input_tree = ElementTree.parse(input)
    except Exception, msg:
        print >>sys.stderr, msg
        sys.exit(1)

    fp = open(output, 'w')
    print >>fp, "# Generated file, don't edit"
    print >>fp, "# Source: %s"%(input,)
    print >>fp, "# Last update: %s"%(time.ctime(),)
    print >>fp, ""
    print >>fp, "import objc, sys"
    print >>fp, ""
    print >>fp, "if sys.maxint > 2 ** 32:"
    print >>fp, "    def sel32or64(a, b): return b"
    print >>fp, "else:"
    print >>fp, "    def sel32or64(a, b): return a"
    print >>fp, "if sys.byteorder == 'little':"
    print >>fp, "    def littleOrBig(a, b): return a"
    print >>fp, "else:"
    print >>fp, "    def littleOrBig(a, b): return b"
    print >>fp, ""

    emit_misc(fp, input_tree)
    emit_constants(fp, input_tree)
    emit_enums(fp, input_tree)
    emit_strconsts(fp, input_tree)
    emit_functions(fp, input_tree)
    emit_cftype(fp, input_tree)
    emit_classes(fp, input_tree)
    emit_informal_protocols(fp, input_tree)

def rewrite_typecode(value):
    result = []

    while value and value[0] in (objc._C_PTR, objc._C_IN, objc._C_INOUT, objc._C_ONEWAY, objc._C_CONST):
        result.append(value[0])
        value = value[1:]

    if value[0] == objc._C_BOOL:
        result.append(objc._C_NSBOOL)
        value = value[1:]

    elif value[0] == objc._C_NSBOOL:
        result.append(objc._C_BOOL)
        value = value[1:]

    elif value[0] == objc._C_STRUCT_B:
        while value[0] != '=' and value[0] != objc._C_STRUCT_E:
            result.append(value[0])
            value = value[1:]

        if value[0] == '=':
            result.append(value[0])
            value = value[1:]

        while value[0] != objc._C_STRUCT_E:
            if value[0] == '"':
                # Embedded field name
                result.append(value[0])
                value = value[1:]
                while value[0] != '"':
                    result.append(value[0])
                    value = value[1:]
                result.append(value[0])
                value = value[1:]

            cur, value = rewrite_typecode(value)
            result.append(cur)

        result.append(objc._C_STRUCT_E)
        value = value[1:]

    elif value[0] == objc._C_UNION_B:
        while value[0] != '=' and value[0] != objc._C_UNION_E:
            result.append(value[0])
            value = value[1:]

        if value[0] == '=':
            result.append(value[0])
            value = value[1:]

        while value[0] != objc._C_UNION_E:
            if value[0] == '"':
                # Embedded field name
                result.append(value[0])
                value = value[1:]
                while value[0] != '"':
                    result.append(value[0])
                    value = value[1:]
                result.append(value[0])
                value = value[1:]

            cur, value = rewrite_typecode(value)
            result.append(cur)

        result.append(objc._C_UNION_E)
        value = value[1:]

    elif value[0] == objc._C_ARY_B:
        result.append(value[0])
        value = value[1:]
        while value[0].isdigit():
            result.append(value[0])
            value = value[1:]

        while value[0] != objc._C_ARY_E:
            cur, value = rewrite_typecode(value)
            result.append(cur)

        result.append(value[0])
        value = value[1:]

    else:
        result.append(value[0])
        value = value[1:]

    return ''.join(result), value

def rewrite_typestr(value):
    if value is None: return value
    result = []

    cur, rest = rewrite_typecode(value)
    result.append(cur)

    while rest:
        cur, rest = rewrite_typecode(rest)
        result.append(cur)
    return ''.join(result)

def emit_misc(fp, tree):
    fp.write("misc = {\n")

    for node in tree.findall('.//opaque'):
        if node.get('ignore', 'false') == 'true':
            continue
        name = node.get('name')
        type = node.get('type')
        type64 = node.get('type64')

        if type64 is None or type == type64:
            fp.write('    "%s": objc.createOpaquePointerType(%r, b%r),\n'%(
                name, name, rewrite_typestr(type)))
        else:
            fp.write('    "%s": objc.createOpaquePointerType(%r, sel32or64(b%r, b%r)),\n'%(
                name, name, rewrite_typestr(type), rewrite_typestr(type64)))

    for node in tree.findall('.//struct'):
        if node.get('ignore', 'false') == 'true':
            continue
        name = node.get('name')
        type = node.get('type')
        type64 = node.get('type64')


        if type64 is None or type == type64:
            fp.write('    "%s": objc.createStructType(%r, b%r, None),\n'%(
                name, name, rewrite_typestr(type)))
        else:
            fp.write('    "%s": objc.createStructType(%r, sel32or64(b%r, b%r), None),\n'%(
                name, name, rewrite_typestr(type), rewrite_typestr(type64)))


    fp.write("}\n")

def emit_constants(fp, tree):

    fp.write("constants = '''$")
    for node in tree.findall('.//constant'):
        if node.get('ignore', 'false') == 'true':
            continue
        name = node.get("name")
        type = rewrite_typestr(node.get("type", "@"))

        if type[0] == '{':
            _, rest = type.split('=', 1)
            if '?' in rest:
                # Skip structs with embedded function pointers and
                # other unhandled types
                continue

        type = rewrite_typestr(type)

        if node.get("magic_cookie", "false") == "true":
            type = "=" + type

        if type == "@":
            fp.write(name)
        else:
            fp.write(name)
            fp.write("@")
            fp.write(type)
        fp.write("$")
    fp.write("'''\n")


def emit_enums(fp, tree):
    others = {}
    fp.write("enums = '''$")
    for node in tree.findall('.//enum'):
        if node.get('ignore', 'false') == 'true':
            continue
        name = node.get("name")
        value = node.get("value")
        value64 = node.get("value64")

        if value is None and value64 is not None:
            value = value64

        if value is None:
            le_value = int(node.get("le_value"))
            be_value = int(node.get("be_value"))
            others[name] = littleOrBig(le_value, be_value)

        elif value64 is None or value64 == value:
            fp.write(name)
            fp.write("@")
            fp.write(value)
            fp.write("$")

        else:
            others[name] = sel32or64(value, value64)

    fp.write("'''\n")

    if others:
        fp.write("misc.update(%r)\n"%(others,))



def emit_strconsts(fp, tree):
    items = {}
    for node in tree.findall('.//string_constant'):
        if node.get('ignore', 'false') == 'true':
            continue
        nm = node.get('name')
        value = node.get('value')
        isstr = node.get('nsstring', 'false') == 'true'
        if not isstr:
            value = value.encode('ascii')
        items[nm] = value

    print >>fp, "string_constants = %s"%(items)

def emit_functions(fp, tree):
    items = {}
    for node in tree.findall('.//function'):
        if node.get('ignore', 'false') == 'true':
            continue

        name = node.get('name')
        types = [b'v']
        types64 = [b'v']
        retval = None
        arguments = []
        meta = {}

        if node.get('variadic', 'false') == 'true':
            meta['variadic'] = 'true'
            if node.get('c_array_delimited_by_null', 'false') == 'true':
                meta['c_array_delimited_by_null'] = True

            if node.get('c_array_delimited_by_null') is not None:
                meta['c_array_length_in_arg'] =  \
                        int(node.get('c_array_length_in_arg'))

        for child in node:
            if child.tag == 'retval':
                retval = {}
                convert_argnode(False, child, retval)

                if child.get('type64') is not None:
                    types64[0] = rewrite_typestr(child.get('type64'))
                else:
                    types64[0] = rewrite_typestr(child.get('type'))

                types[0] = rewrite_typestr(child.get('type'))

            elif child.tag == 'arg':
                info = {}
                convert_argnode(False, child, info)
                arguments.append(info)
                
                if child.get('type64') is not None:
                    types64.append(rewrite_typestr(child.get('type64')))
                else:
                    types64.append(rewrite_typestr(child.get('type')))

                types.append(rewrite_typestr(child.get('type')))

            else:
                raise ValueError("Child node %s of function node"%(child.tag,))

        if retval is not None:
            k = list(retval.keys())
            k.sort()
            if k in (['type'], ['type', 'type64']):
                # No additional information, no need to store meta information
                pass

            else:
                meta['retval'] = retval

        if arguments:
            have_meta = False
            for a in arguments:
                k = list(a.keys())
                k.sort()
                if k in (['type'], ['type', 'type64']):
                    # No additional information, no need to store meta 
                    # information
                    pass
                else:
                    have_meta = True

            if have_meta:
                meta['arguments'] = dict(zip(range(len(arguments)), arguments))

        if meta == {}:
            meta = None

        if types[0] is None:
            types[0] = 'v'

        if types64[0] is None:
            types64[0] = 'v'


        types = ''.join(types)
        types64 = ''.join(types64)

        if types != types64:
            if meta is None:
                items[name] = (sel32or64(types, types64),)
            else:
                items[name] = (sel32or64(types, types64), "", meta)
        else:
            if meta is None:
                items[name] = (types,)
            else:
                items[name] = (types, "", meta)


    fp.write("functions = %r\n"%(items,))


BOOLEAN_ATTRIBUTES=[
    ("already_retained", False),
    ("already_cfretained", False),
    ("c_array_length_in_result", False),
    ("c_array_delimited_by_null", False),
    ("c_array_of_variable_length", False),
    ("printf_format", False),
    ("free_result", False),
    ("null_accepted", True),
]

def parse_callable(isfunction, node, dct):
    if node.get('function_pointer_retained', 'true') == 'false':
        dct['callable_retained'] = False

    meta = dct['callable'] = {}
    meta['arguments'] = arguments = {}
    idx = 0

    if not isfunction:
        # Blocks have an implicit first argument
        arguments[idx] = {
                'type': '^v',
        }
        idx += 1

    for child in node:
        if child.tag == 'retval':
            retval = meta['retval'] = {}
            convert_argnode(False, child, retval)

        elif child.tag == 'arg':
            info = {}
            convert_argnode(False, child, info)
            arguments[idx] = info
            idx += 1

        else:
            raise ValueError("Child node %s of function node"%(child.tag,))

    if meta.get('retval') is None:
        meta['retval'] = {
            'type': 'v',
        }

        

def convert_argnode(ismethod, node, dct):
    if ismethod:
        argoffset = 2
    else:
        argoffset = 0

    v = node.get('type_modifier')
    if v is not None:
        dct['type_modifier'] = bstr(v)

    type = node.get('type')
    type64 = node.get('type64')
    if type is not None:
        if type64 is None or type == type64:
            dct['type'] = bstr(rewrite_typestr(type))
        else:
            dct['type'] = sel32or64(
                    bstr(rewrite_typestr(type)),
                    bstr(rewrite_typestr(type64)))

    sel_of_type = node.get('sel_of_type')
    sel_of_type64 = node.get('sel_of_type64')
    if sel_of_type is not None:
        if sel_of_type64 is None or sel_of_type == sel_of_type64:
            dct['sel_of_type'] = bstr(rewrite_typestr(sel_of_type))
        else:
            dct['sel_of_type'] = sel32or64(
                    bstr(rewrite_typestr(sel_of_type)),
                    bstr(rewrite_typestr(sel_of_type64)))

    v = node.get('c_array_of_fixed_length')
    if v is not None:
        dct['c_array_of_fixed_length'] = int(v)


    v = node.get('c_array_length_in_arg')
    if v is not None:
        if ',' in v:
            a, b = v.split(',')
            a = a.strip()
            b = b.strip()

            dct['c_array_length_in_arg'] = int(a)+argoffset, int(b)+argoffset
        else:
            dct['c_array_length_in_arg'] = int(v)+argoffset


    v = node.get('function_pointer')
    if v == 'true':
        parse_callable(True, node, dct)

    v = node.get('block')
    if v == 'true':
        parse_callable(False, node, dct)


    for attr, default in BOOLEAN_ATTRIBUTES:
        v = node.get(attr)
        if v is not None:
            if v == 'true':
                v = True
            else:
                v = False

            if v != default:
                dct[attr] = v


def emit_classes(fp, tree):
    print >>fp, "r = objc.registerMetaDataForSelector"
    print >>fp, "objc._updatingMetadata(True)"
    print >>fp, "try:"
    print >>fp, "    pass"
    for node in tree.findall('.//class'):
        if node.get('ignore', 'false') == 'true':
            continue
        clsname = node.get('name')
        for method in node:
            if method.tag != 'method': continue

            if method.get('ignore', 'false') == 'true':
                continue
            sel = bstr(method.get('selector'))
            meta = {}
            for info in method:
                if info.tag == 'retval':
                    n = meta['retval'] = {}
                elif info.tag == 'arg':
                    if 'arguments' not in meta:
                        meta['arguments'] = {}

                    n = meta['arguments'][int(info.get('index'))+2] = {}

                convert_argnode(True, info, n)

            print >>fp, '    r(%r, %r, %r)'%(clsname, sel, meta)

    print >>fp, "finally:"
    print >>fp, "    objc._updatingMetadata(False)"

def emit_cftype(fp, tree):
    print >>fp, "cftypes = []"
    for node in tree.findall('.//cftype'):
        name = node.get('name')
        type = node.get('type')
        type64= node.get('type64')
        if type64 is not None and type64 != type:
            type = sel32or64(type, type64)

        gettypeid_func = node.get('gettypeid_func')
        tollfree= node.get('tollfree')

        print >>fp, "cftypes.append((%r, %r, %r, %r))"%(name, type, gettypeid_func, tollfree)




def prot(name, methods):
    return funccall('objc.informal_protocol', (name, methods))

def sel(selector, type):
    return funccall('objc.selector', (None, selector, type), {'isRequired': False})

def emit_informal_protocols(fp, tree):
    protocols = {
    }
    for node in tree.findall('.//informal_protocol'):
        name = node.get('name')

        methods = []

        for method in node:
            selector = method.get('selector')
            type = rewrite_typestr(method.get('type'))
            type64 = rewrite_typestr(method.get('type64'))

            if type64 is not None and type != type64:
                type = sel32or64(type, type64)

            methods.append(sel(selector, type))

        protocols[name] = prot(name, methods)

    if protocols:
        fp.write('protocols=%s\n'%(protocols))
