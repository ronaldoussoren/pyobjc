#
# this script needs a version of the 'new' pyobjc
#
# This generates wrappers for 'simple' functions, basically anything that
# has only 'by value' arguments, and return a simple object or an 'id'
#

try:
    import objc
except ImportError:
    objc = None

try:
    import AppKit
except ImportError:
    pass


import re
import sys
import types

# Types that are also int-values (mostly enums)
INT_ALIASES=[]

# Varargs functions to be treated like normal functions
IGNORE_VARARGS = []

# Function mapping
FUNC_MAP = {}

HDR="""\
/*
 * This is a generated file.
 */

typedef void* PYOBJC_VOIDPTR;

static inline int convert_BOOL(PyObject* object, void* pvar)
{
    BOOL* pbool = (BOOL*)pvar;

    if (PyObject_IsTrue(object)) {
        *pbool = YES;
    } else {
        *pbool = NO;
    }

    return 1;
}


static inline int convert_char(PyObject* object, void* pvar)
{
	char* pchar = (char*)pvar;

	if (!PyString_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Expecting string of len 1");
		return 0;
	}

	if (PyString_Size(object) != 1) {
		PyErr_SetString(PyExc_TypeError, "Expecting string of len 1");
		return 0;
	}

	*pchar = *PyString_AsString(object);
	return 1;
}

static inline int convert_id(PyObject* object, void* pvar)
{
	id* pid = (id*)pvar;

	*pid = PyObjC_PythonToId(object);

        if (PyErr_Occurred()) {
            return 0;
        } 
        return 1;
}

static inline int convert_SEL(PyObject* object, void* pvar)
{
        if (object == Py_None) {
            *(SEL*)pvar = NULL;
            return 1;
        }
        if (PyObjCSelector_Check(object)) {
            *(SEL*)pvar = PyObjCSelector_GetSelector(object);
            return 1;
        }
	if (!PyString_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Expected string");
		return 0;
	}

	*(SEL*)pvar = SELUID(PyString_AsString(object));
	return 1;
}

static inline int convert_Class(PyObject* object, void* pvar)
{
	if (!PyObjCClass_Check(object)) {
		PyErr_SetString(PyExc_TypeError, "Expected objective-C class");
		return 0;
	}

	*(Class*)pvar = PyObjCClass_GetClass(object);
	if (*(Class*)pvar == NULL) return 0;
	return 1;
}

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
            return 0

# TODO: actually use this, and add more types (when using: always check here
# first, and then special logic (like handling 'id'-like values)
SIMPLE_TYPES={
	# key: ( 'to_python', 'parse_fmt', 'parse_args' ) 
	#      items in the tuple are either None (not needed), a string or
	#      a function. The string will be %-expanded with a dict containing
	#      the key 'varname', and varname will be the only argument to
	#      the function that must return a string.
	'char': (
		'\tresult = PyString_FromStringAndSize(&(%(varname)s), 1);\n\tif (result == NULL) return NULL;',
		'O&', 		
		'convert_char, &%(varname)s', 
	),
	'SEL': (
		'\tresult = PyString_FromString(SELNAME(%(varname)s));\n\tif (result == NULL) return NULL;',
		'O&', 		
		'convert_SEL, &%(varname)s', 
	),
	'Class': (
		'\tresult = PyObjCClass_New(%(varname)s);\n\tif (result == NULL) return NULL;',
		'O&', 		
		'convert_Class, &%(varname)s', 
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
		"\tresult = PyObjCBool_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
		'O&', 		
		'convert_BOOL, &%(varname)s', 
		None
	),
	'unsigned': (
		"\tresult = PyInt_FromLong(%(varname)s);\n\tif (result == NULL) return NULL;",
		'i',
		'&%(varname)s',
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
}
		
def simple_to_python(varname, typestr):
	if typestr.startswith('const ') or typestr.startswith('const\t'):
		typestr = typestr[6:].strip()

	if is_id(typestr):
		return "\tresult = PyObjC_IdToPython(%(varname)s); if (result == NULL) return NULL;"%{ 'varname': varname }

	if typestr in INT_ALIASES:
		x = SIMPLE_TYPES['int']
	else:
		x = SIMPLE_TYPES[typestr]

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

	if typestr in INT_ALIASES:
		x = SIMPLE_TYPES['int']
	else:
		x = SIMPLE_TYPES[typestr]
	return x[1]

def parsetuple_arguments(typestr, varname):
	if typestr.startswith('const ') or typestr.startswith('const\t'):
		typestr = typestr[6:].strip()

	if is_id(typestr):
		return "convert_id, &%(varname)s"%{ 'varname': varname }

	if typestr in INT_ALIASES:
		x = SIMPLE_TYPES['int']
	else:
		x = SIMPLE_TYPES[typestr]

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
	
	if typestr in INT_ALIASES:
		return 1

	elif typestr in SIMPLE_TYPES:
		return 1

	else:
		return is_id(typestr)


def parse_prototype(protostr):
	protostr = protostr.strip()
	idx = protostr.index('(')

	arguments = [ x.strip() for x in protostr[idx+1:-2].split(',') ]
	before = protostr[:idx].strip()
	idx=len(before)-1
	while before[idx].isalnum() or before[idx] == '_':
		idx -= 1
	
	funcname = before[idx+1:].strip()
	retval = simplify_type(before[:idx+1].strip())

	if not is_simple_type(retval) and retval != 'void':
		raise ValueError, "Complex function (retval)"

	new_arguments = []
	if len(arguments)  != 1 or arguments[0] != 'void':
		for a in arguments:
			if a == '...':
                                if funcname in IGNORE_VARARGS:
                                    continue
				raise ValueError, "Complex function (varargs)"
			idx = len(a)-1
			while a[idx].isalnum() or a[idx] == '_':
				idx -= 1
			new_arguments.append((simplify_type(a[:idx+1].strip()), a[idx+1:].strip()))
	arguments = tuple(new_arguments)

        if FUNC_MAP.has_key(funcname):
            arguments = FUNC_MAP[funcname](funcname, arguments)

	for tp, name in arguments:
		if not is_simple_type(tp):
			raise ValueError, "Complex function (arg of type %s)"%(tp,)

	return retval, funcname, arguments


def process_function(fp, protostr):
	retval, funcname, arguments = parse_prototype(protostr)

	fp.write("/* %s */\n"%protostr)
	fp.write("static PyObject* objc_%s(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)\n"%funcname)
	fp.write("{\n")
	keywords = [ a[1] for a in arguments ]
	keywords = '", "'.join(keywords)
	if keywords:
		keywords = '"%s", '%keywords
	fp.write("static\tchar* keywords[] = { %sNULL };\n"%keywords)
	fp.write("\tPyObject* result;\n")
	if retval != 'void':
		fp.write("\t%s objc_result;\n"%retval)
	
	fmt = ''
	arglist = ''
	for tp, name in arguments:
		fmt += parsetuple_fmt(tp)
		v =parsetuple_arguments(tp, "objc_%s"%name)
		if v:
			arglist += ", %s"%v

		if is_id(tp):
			fp.write("\tid objc_%s;\n"%name)
		else:
			fp.write("\t%s objc_%s;\n"%(tp, name))

	fp.write("\n")

	fp.write('\tif (!PyArg_ParseTupleAndKeywords(args, kwds, "%s:%s", keywords%s)) return NULL;\n'%(fmt, funcname, arglist))

	fp.write("\tNS_DURING\n")
	if retval != 'void':
		fp.write("\t\tobjc_result = %s(\n"%funcname,)
	else:
		fp.write("\t\t%s(\n"%funcname,)
	sep = ""
	for tp, name in arguments:
		fp.write("%sobjc_%s"%(sep, name))
		sep = ", "
	fp.write(");\n")
	fp.write("\tNS_HANDLER\n")
	fp.write("\t\tPyObjCErr_FromObjC(localException);\n")
	fp.write("\t\treturn NULL;\n")
	fp.write("\tNS_ENDHANDLER\n")

	if retval != 'void':
		fp.write("\t%s\n"%simple_to_python("objc_result", retval))
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

	for l in lst:
		l = l.strip()
		if not l: continue
		if l[0] == '#': continue
		total_count += 1
		try:
			sys.stderr.write("Converting '%s' ..."%l.strip())
			sys.stderr.flush()

			funcs.append((process_function(fp, l), l))
			sys.stderr.write("done\n")
			sys.stderr.flush()
			ok_count += 1
		except ValueError, msg:
			sys.stderr.write("failed: %s\n"%msg)
			sys.stderr.flush()


	fp.write("\n")

	if not funcs:
		fp.write("#define METHOD_TABLE_ENTRIES\n")
	else:
		fp.write("#define METHOD_TABLE_ENTRIES \\\n")
		for f in funcs:
			fp.write('\t{ "%(funcname)s", (PyCFunction)objc_%(funcname)s, METH_VARARGS|METH_KEYWORDS, "%(funcproto)s" }, \\\n'%{'funcname':f[0], 'funcproto':f[1]})
		fp.write("\t/* END */\n")


	sys.stderr.write("Converted %d of %d functions\n"%(ok_count, total_count))

if __name__ == "__main__":
	import sys
	INT_ALIASES.append('NSWindowDepth')
	process_list(sys.stdout, file(sys.argv[1]))
