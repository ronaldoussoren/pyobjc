#
# this script needs a version of the 'new' pyobjc
#
# This generates wrappers for 'simple' functions, basically anything that
# has only 'by value' arguments, and return a simple object or an 'id'
#

verbose=0

### We tried to import objc to detect if a name denotes a class. Now that
# this script is started before we have a valid PyObjC installation this
# is less usefull. Just rely on the static class list below.
#
#try:
#    import objc
#except ImportError:
#    objc = None
#
#try:
#    import AppKit
#except ImportError:
#    pass

objc = None


import re
import sys
import types

# Types that are also simple values (mostly enums)
TYPE_ALIASES={}

# Varargs functions to be treated like normal functions
IGNORE_VARARGS = []

# Function mapping
FUNC_MAP = {}
DEFAULT_FUNCMAP=None

# FUNCMAPS can set an argument-type to this value ('is' not '==') to remove
# the argument from the python interface and force it to a specific value.
FORCE_VALUE="ForceValue"

HDR="""\
/*
 * This is a generated file.
 */

/*typedef void* PYOBJC_VOIDPTR;*/

"""

PTR_RE=re.compile('[ \t]+\*')
def simplify_type(typestr):
    typestr = PTR_RE.sub('*', typestr)

    return typestr

PROT_MATCHER=re.compile('<[A-Za-z0-9_ \t,]*>')
def is_id(typestr):
    # Remove protocol 'declarations' (id <NSObject, NSString>)
    typestr = PROT_MATCHER.sub('', typestr).strip()


    if typestr == 'id':
        return 1
    elif typestr[-1] != '*':
        return 0

    if objc != None:
        try:
            objc.lookUpClass(typestr[:-1])
            return 1
        except:
            return 0
    else:
        # These types are used in function definition (OSX 10.2), this
        # list is necessary for people that build without an installed
        # PyObjC.
        if typestr[:-1] in ('NSString', 'NSArray', 'NSWindow', 'NSColor', 'NSPasteboard', 'NSBundle', 'NSDictionary', 'NSResponder', 'NSThread', 'NSMutableDictionary', ):
            return 1
        return 0

# TODO: actually use this, and add more types (when using: always check here
# first, and then special logic (like handling 'id'-like values)
# TODO: Use PyObjC_ObjCToPython/PyObjC_PythonToObjC!
SIMPLE_TYPES={
    # key: ( 'to_python', 'parse_fmt', 'parse_args' )
    #      items in the tuple are either None (not needed), a string or
    #      a function. The string will be %-expanded with a dict containing
    #      the key 'varname', and varname will be the only argument to
    #      the function that must return a string.
    'char': (
        '\tresult = PyString_FromStringAndSize(&(%(varname)s), 1);\n\tif (result == NULL) return NULL;',
        'O&',
        'PyObjC_ConvertChar, &%(varname)s',
    ),
    'Class': (
        '\tresult = PyObjCClass_New(%(varname)s);\n\tif (result == NULL) return NULL;',
        'O&',
        'PyObjCClass_Convert, &%(varname)s',
    ),
    'int': (
        "\tresult = PyInt_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
        'i',
        '&%(varname)s',
        None
    ),
    'PYOBJC_VOIDPTR': (
        "\tresult = PyInt_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
        'i',
        '&%(varname)s',
        None
    ),
    'BOOL': (
        "\tresult = PyBool_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
        'O&',
        'PyObjC_ConvertBOOL, &%(varname)s',
        None
    ),
    'short': (
        "\tresult = PyInt_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
        'h',
        '&%(varname)s',
        None
    ),
    'long': (
        "\tresult = PyInt_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
        'l',
        '&%(varname)s',
        None
    ),
    'float': (
        "\tresult = PyFloat_FromDouble(%(varname)s);\n\tif (result == NULL) return NULL;",
        'f',
        '&%(varname)s',
        None
    ),
    'double': (
        "\tresult = PyFloat_FromDouble(%(varname)s);\n\tif (result == NULL) return NULL;",
        'd',
        '&%(varname)s',
        None
    ),
    'long long': (
        "\t result = PyLong_FromLongLong(%(varname)s);\n\tif (result == NULL) return NULL;",
        'L',
        '&%(varname)s',
        None
    ),
    'char*': (
        "\t result = PyString_FromString(%(varname)s);\n\tif (result == NULL) return NULL;",
        "s",
        '&%(varname)s',
        None
    ),
}

if sys.platform == 'darwin':
    SIMPLE_TYPES['SEL'] = (
        '\tresult = PyString_FromString(SELNAME(%(varname)s));\n\tif (result == NULL) return NULL;',
        'O&',
        'PyObjCSelector_Convert, &%(varname)s',
    )
else:
    SIMPLE_TYPES['SEL'] = (
        '\tresult = PyString_FromString(sel_get_name(%(varname)s));\n\tif (result == NULL) return NULL;',
        'O&',
        'PyObjCSelector_Convert, &%(varname)s',
    )

SIMPLE_TYPES['unsigned long long'] =  (
    "\t result = PyLong_FromUnsignedLongLong(%(varname)s);\n\tif (result == NULL) return NULL;",
    'K',
    '&%(varname)s',
    None
)
SIMPLE_TYPES['unsigned'] = (
    "\tresult = PyInt_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
    'I',
    '&%(varname)s',
    None
)
SIMPLE_TYPES['unsigned int'] = SIMPLE_TYPES['unsigned']
SIMPLE_TYPES['unsigned long'] = SIMPLE_TYPES['unsigned']

SIMPLE_TYPES['unsigned short'] = (
    "\tresult = PyInt_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
    'H',
    '&%(varname)s',
    None
)

def hidden_from_python(typestr):
    if typestr is FORCE_VALUE: return 1
    if typestr.startswith('const ') or typestr.startswith('const\t'):
        typestr = typestr[6:].strip()

    if is_id(typestr):
        return 0

    x = SIMPLE_TYPES[TYPE_ALIASES.get(typestr, typestr)]

    if x[2] is '':
        return 1
    return 0


def simple_to_python(varname, typestr):
    if typestr.startswith('const ') or typestr.startswith('const\t'):
        typestr = typestr[6:].strip()

    if is_id(typestr):
        return "\tresult = PyObjC_IdToPython(%(varname)s); if (result == NULL) return NULL;"%{ 'varname': varname }

    x = SIMPLE_TYPES[TYPE_ALIASES.get(typestr, typestr)]
    
    if x[0] is None:
        return
    elif isinstance(x[0], str):
        return x[0]%{'varname': varname }
    elif isinstance(x[0], types.FunctionType):
        return x[0](varname)
    else:
        raise ValueError, "Bad config for %s"%typestr

def parsetuple_fmt(typestr):
    if typestr.startswith('const ') or typestr.startswith('const\t'):
        typestr = typestr[6:].strip()

    if is_id(typestr):
        return 'O&';

    x = SIMPLE_TYPES[TYPE_ALIASES.get(typestr, typestr)]

    return x[1]

def parsetuple_arguments(typestr, varname):
    if typestr.startswith('const ') or typestr.startswith('const\t'):
        typestr = typestr[6:].strip()

    if is_id(typestr):
        return "PyObjCObject_Convert, &%(varname)s"%{ 'varname': varname }

    x = SIMPLE_TYPES[TYPE_ALIASES.get(typestr, typestr)]
    
    if x[2] is None:
        return
    elif isinstance(x[2], str):
        return x[2]%{'varname': varname }
    elif isinstance(x[2], types.FunctionType):
        return x[2](varname)
    else:
        raise ValueError, "Bad config for %s"%typestr

def is_simple_type(typestr):
    if typestr.startswith('const ') or typestr.startswith('const\t'):
        typestr = typestr[6:].strip()

    return (typestr in TYPE_ALIASES) or (typestr in SIMPLE_TYPES) or is_id(typestr)

def parse_prototype(protostr):
    protostr = protostr.strip()
    if protostr[-1] != ')':
        protostr = protostr.strip()[:-1].strip()
    idx = protostr.index('(')

    arguments = [ x.strip() for x in protostr[idx+1:-1].split(',') ]
    before = protostr[:idx].strip()
    idx=len(before)-1
    while before[idx].isalnum() or before[idx] == '_':
        idx -= 1

    funcname = before[idx+1:].strip()
    retval = simplify_type(before[:idx+1].strip())

    if not is_simple_type(retval) and retval != 'void':
        raise ValueError, "Complex function (retval) --%s--"%(retval,)

    new_arguments = []
    if len(arguments)  != 1 or arguments[0] != 'void' and arguments[0] != '':
        for a in arguments:
            if a == '...':
                if funcname in IGNORE_VARARGS:
                    continue
                raise ValueError, "Complex function (varargs)"
            idx = len(a)-1
            while idx > 0 and (a[idx].isalnum() or a[idx] == '_'):
                idx -= 1
            new_arguments.append((simplify_type(a[:idx+1].strip()), a[idx+1:].strip()))
    arguments = tuple(new_arguments)

    if FUNC_MAP.has_key(funcname):
        arguments = FUNC_MAP[funcname](funcname, arguments)
    elif DEFAULT_FUNCMAP is not None:
        arguments = DEFAULT_FUNCMAP(funcname, arguments)


    for tp, name in arguments:
        if tp is FORCE_VALUE: continue
        if not is_simple_type(tp):
            raise ValueError, "Complex function (arg of type %s)"%(tp,)

    return retval, funcname, arguments

def have_func(fname, funclist):
    for n, l in funclist:
        if fname == n:
            return 1
    return 0

def process_function(fp, protostr, funclist):
    retval, funcname, arguments = parse_prototype(protostr)

    if have_func(funcname, funclist):
        return

    fp.write("/* %s */\n"%protostr)
    fp.write("static PyObject* objc_%s(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)\n"%funcname)
    fp.write("{\n")
    keywords = [ a[1] for a in arguments if not hidden_from_python(a[0])]
    keywords = '", "'.join(keywords)
    if keywords:
        keywords = '"%s", '%keywords
    fp.write("static\tchar* keywords[] = { %sNULL };\n"%keywords)
    fp.write("\tPyObject* result;\n")
    if retval != 'void':
        fp.write("\t%s _objc__result_;\n"%retval)

    fmt = ''
    arglist = ''
    for tp, name in arguments:
        if tp is FORCE_VALUE: continue
        fmt += parsetuple_fmt(tp)
        v =parsetuple_arguments(tp, "objc_%s"%name)
        if v:
            arglist += ", %s"%v

        if is_id(tp):
            fp.write("\tid objc_%s;\n"%name)
        else:
            if hidden_from_python(tp):
                fp.write("\t%s objc_%s = 0;\n"%(tp, name))
            else:
                fp.write("\t%s objc_%s;\n"%(tp, name))

    fp.write("\n")

    fp.write('\tif (!PyArg_ParseTupleAndKeywords(args, kwds, "%s:%s", keywords%s)) return NULL;\n'%(fmt, funcname, arglist))

    fp.write("\tPyObjC_DURING\n")
    if retval != 'void':
        fp.write("\t\t_objc__result_ = %s(\n"%funcname,)
    else:
        fp.write("\t\t%s(\n"%funcname,)
    sep = "\t\t\t\t"
    for tp, name in arguments:
        if tp is FORCE_VALUE:
            fp.write("%s%s"%(sep, name))
        else:
            fp.write("%sobjc_%s"%(sep, name))
        sep = ",\n\t\t\t\t"
    fp.write(");\n")
    fp.write("\tPyObjC_HANDLER\n")
    fp.write("\t\tPyObjCErr_FromObjC(localException);\n")
    fp.write("\tPy_BLOCK_THREADS\n")
    fp.write("\tNS_VALUERETURN(NULL, PyObject*);\n")
    fp.write("\tPyObjC_ENDHANDLER\n")

    if retval != 'void':
        fp.write("\t%s\n"%simple_to_python("_objc__result_", retval))
    else:
        fp.write("\tresult = Py_None;\n\tPy_INCREF(Py_None);\n");

    fp.write("\treturn result;\n")
    fp.write("}\n")
    return funcname


def process_list(fp, lst):
    ok_count = 0
    total_count = 0
    funcs=[]

    fp.write(HDR)

    for i, l in enumerate(lst):
        l = l.strip()
        if not l: continue
        if l[0] == '#': continue
        total_count += 1
        try:
            funcs.append((process_function(fp, l, funcs), l))
            if verbose:
                sys.stderr.write("Converting '%s' ..."%l.strip())
                sys.stderr.write("done\n")
            sys.stderr.flush()
            ok_count += 1

        except ValueError, msg:
            fn = getattr(lst, 'name', None)
            if fn is not None:
                sys.stderr.write('%s:%d\n' % (fn, i+1))
            sys.stderr.write("%s\n"%l.strip())
            sys.stderr.write("Converting failed: %s\n"%msg)
            sys.stderr.flush()

    fp.write("\n")



    if verbose:
        sys.stderr.write("Converted %d of %d functions\n"%(ok_count, total_count))

    return funcs

def gen_method_table_entries(fp, funcs):
    if not funcs:
        fp.write("#define METHOD_TABLE_ENTRIES\n")
    else:
        fp.write("#define METHOD_TABLE_ENTRIES \\\n")
        for f in funcs:
            if f[0] is None: continue
            fp.write('\t{ "%(funcname)s", (PyCFunction)objc_%(funcname)s, METH_VARARGS|METH_KEYWORDS, "%(funcproto)s" }, \\\n'%{'funcname':f[0], 'funcproto':f[1]})
        fp.write("\t/* END */\n")


if __name__ == "__main__":
    import sys
    TYPE_ALIASES['NSWindowDepth'] = 'int'
    process_list(sys.stdout, file(sys.argv[1]))
