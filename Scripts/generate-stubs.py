#!/usr/bin/env python

#
# This file started out as a module for parsing objective-C signatures,
# and now is a script for generating a number of functions for signatures:
# - Call the super-class implementation from python
# - Call the python method from objective-C (used in method-tables in the
#   objective-C side of a python/objective-C hybrid class)
#
# TODO:
# - Split into two files: The signature library and the actual program.
# - Support pass-by-reference parameters (_C_IN, _C_OUT, _C_INOUT)
# - Support struct-returns, these are handled differently by the Apple
#   objC compiler.

# parse_typestr(typestr) -> typeinfo, reststr
# parse_signature(typestr) -> [typeinfo,...]

# For now this controls wether we generate just the methods or also the registration
# function...
import sys

_SIMPLE_TYPES={}

def new_name():
	i = 0
	while 1:
		yield "pyobjcanonymous%d"%i
		i += 1

name_iter = new_name()

class simple_type:
	__slots__ = ('fmt_char', 'c_str')

	def __init__(self, fmt_char, c_str):
		self.fmt_char = fmt_char
		self.c_str = c_str

		global _SIMPLE_TYPES
		_SIMPLE_TYPES[fmt_char] = self

	def __repr__(self):
		return "<simple '%s' '%s'>"%(self.fmt_char, self.c_str)

	def typestr(self):
		return self.fmt_char

	def c_decl(self, var):
		return '%s %s'%(self.c_str, var)

	def c_pre_decl(self):
		return ''

	def parse(str):
		return _SIMPLE_TYPES[str[0]], str[1:]
	parse = staticmethod(parse)

class TP_ARRAY:
	__slots__ = ('count', 'elem_types')

	def __init__(self, count, elem_types):
		self.count = count
		self.elem_types = elem_types

	def __repr__(self):
		return '<array %d of %s>'%(self.count, self.elem_types)

	def typestr(self):
		return '[%d%s]'%(self.count, self.elem_types.typestr())

	def c_decl(self, var):
		return '%s[%d]'%(self.elem_types.c_decl(var), self.count)

	def c_pre_decl(self):
		return self.elem_types.c_pre_decl()

	def parse(str):
		if not str.startswith('['):
			raise ValueError, 'No array %s'%str

		str = str[1:]
		cnt = ''
		while str[0].isdigit():
			cnt += str[0]
			str = str[1:]
		cnt = int(cnt)
		valuetype, str = parse_typestr(str)
		if str[0] != ']':
			raise ValueError,  'Missing end-of-array marker'

		return TP_ARRAY(cnt, valuetype), str[1:]

	parse = staticmethod(parse)

class TP_BITFIELD:
	__slots__ = ('count', )

	def __init__(self, count):
		self.count = count

	def __repr__(self):
		return '<bitstring %d>'%(self.count,)

	def typestr(self):
		return 'b%d'%(self.count, )

	def c_decl(self, var):
		return 'int %s:%d'%(var, self.count)

	def c_pre_decl(self):
		return ''

	def parse(str):
		if not str.startswith('b'):
			raise ValueError, 'No bitstring %s'%str

		str = str[1:]
		cnt = ''
		while str and str[0].isdigit():
			cnt += str[0]
			str = str[1:]
		cnt = int(cnt)

		return TP_BITFIELD(cnt), str


	parse = staticmethod(parse)

_UNIONS={}
class TP_UNION:
	__slots__ = ('name', 'elem_types', 'did_pre_decl')

	def __init__(self, name, elem_types):
		if name == '?':
			self.name = name_iter.next()
		else:
			self.name = name
		self.elem_types = elem_types
		self.did_pre_decl = False

	def __repr__(self):
		return '<union %s of %s>'%(self.name, self.elem_types)

	def typestr(self):
		result = ['(%s='%self.name]
		for tp in self.elem_types:
			result.append(tp.typestr())
		result.append(')')
		return ''.join(result)

	def c_decl(self, var):
		return 'union %s %s'%(self.name, var)

	def c_pre_decl(self):
		if self.did_pre_decl: return ''

		res = ''
		for e in self.elem_types:
			res += e.c_pre_decl()

		res += 'union %s {'%self.name
		for idx, tp in enumerate(self.elem_types):
			res += "\t%s;"%tp.c_decl('field_%d'%idx)
		res += '};\n'

		self.did_pre_decl = True

		return res

	def parse(str):
		if not str.startswith('('):
			raise ValueError, 'No union %s'%str

		str = str[1:]
		idx = str.index('=')
		name = str[:idx]
		str = str[idx+1:]
	
		valuetypes = []
		while str[0] != ')':
			while str[0].isdigit():
				str = str[1:]
				if str[0] == ')':
					break
			if str[0] == ')': break
			tp, str = parse_typestr(str)
			valuetypes.append(tp)

		if name not in _UNIONS:
			_UNIONS[name] = TP_UNION(name, valuetypes)
		return _UNIONS[name], str[1:]

	parse = staticmethod(parse)

_STRUCTS={}
class TP_STRUCT:
	__slots__ = ('name', 'elem_types', 'did_pre_decl')

	def __init__(self, name, elem_types):
		if name == '?':
			self.name = name_iter.next()
		else:
			self.name = name
		self.elem_types = elem_types
		self.did_pre_decl = False

		# Somewhat hackish...
		# Some structs are already defined in the headers we're
		# including in the generated file.
		if self.name in [ 
				'_object', 'timespec', 'stat', 
				'__sbuf', '__sFILE' ]:
			self.did_pre_decl = True

	def __repr__(self):
		return '<struct %s of %s>'%(self.name, self.elem_types)

	def typestr(self):
		result = ['{%s='%self.name]
		for tp in self.elem_types:
			result.append(tp.typestr())
		result.append('}')
		return ''.join(result)

	def c_decl(self, var):
		return 'struct %s %s'%(self.name, var)

	def c_pre_decl(self):
		if self.did_pre_decl: return ''

		if not self.elem_types: return 'struct %s;'%self.name

		res = ''
		for e in self.elem_types:
			res += e.c_pre_decl()

		res += 'struct %s {\n'%self.name
		for idx, tp in enumerate(self.elem_types):
			res += "\t" + tp.c_decl('field_%d'%idx) + ";\n";
		res += '};\n'

		self.did_pre_decl = True

		return res

	def parse(str):
		if not str.startswith('{'):
			raise ValueError, 'No struct ' + str

		str = str[1:]
		idx = str.find('=')
		idx2 = str.find('}')
		if idx == -1 or (idx2 !=-1 and idx2 < idx):
			name = str[:idx2]
			valuetypes = []
			str = str[idx2:]
		else:
			name = str[:idx]
			str = str[idx+1:]
		
			valuetypes = []
			while str[0] != '}':
				while str[0].isdigit():
					str = str[1:]
					if str[0] == ')':
						break
				if str[0] == '}': break
				tp, str = parse_typestr(str)
				valuetypes.append(tp)

		if name not in _STRUCTS:
				_STRUCTS[name] = TP_STRUCT(name, valuetypes)
		return _STRUCTS[name], str[1:]

	parse = staticmethod(parse)

class TP_POINTER:
	__slots__ = ('type')

	def __init__(self, type):
		self.type = type

	def __repr__(self):
		return '<pointer to %s>'%self.type

	def typestr(self):
		return '^%s'%self.type.typestr()

	def c_decl(self, var):
		return '%s *%s'%(self.type.c_decl(''), var)

	def c_pre_decl(self):
		return self.type.c_pre_decl();

	def parse(str):
		if not str.startswith('^'):
			raise ValueError, 'No pointer '+str

		tp, str = parse_typestr(str[1:])

		return TP_POINTER(tp), str

	parse = staticmethod(parse)

TP_CHAR=simple_type('c', 'char')
TP_INT=simple_type('i', 'int')
TP_SHORT=simple_type('s', 'short')
TP_LONG=simple_type('l', 'long')
TP_LONGLONG=simple_type('q', 'long long')
TP_UCHAR=simple_type('C', 'unsigned char')
TP_UINT=simple_type('I', 'unsigned int')
TP_USHORT=simple_type('S', 'unsigned short')
TP_ULONG=simple_type('L', 'unsigned long')
TP_ULONGLONG=simple_type('Q', 'unsigned long long')
TP_FLOAT=simple_type('f', 'float')
TP_DOUBLE=simple_type('d', 'double')
TP_VOID=simple_type('v', 'void')
TP_CSTR=simple_type('*', 'char*')
TP_ID=simple_type('@', 'id')
TP_CLASS=simple_type('#', 'Class')
TP_SEL=simple_type(':', 'SEL')
TP_UNKNOWN=simple_type('?', 'void*')

# Bitfields should never be toplevel, and we don't use c_pre_decl, so this
# should be fine
# FIX ME: Make seperate class ('bnum A bit field of num bits')
#TP_BITFIELD=simple_type('b', '<BITSTRING>')

def parse_typestr(str):
	while str and str[0].isdigit():
		str = str[1:]
	if not str:
		return None, ''

	try:
		return simple_type.parse(str)
	except:
		pass

	try:
		return TP_POINTER.parse(str)
	except ValueError, msg:
		pass

	try:
		return TP_ARRAY.parse(str)
	except ValueError, msg:
		pass

	try:
		return TP_STRUCT.parse(str)
	except ValueError, msg:
		pass

	try:
		return TP_UNION.parse(str)
	except:
		pass

	try:
		return TP_BITFIELD.parse(str)
	except ValueError, msg:
		pass

	if str[0] in 'r':
		# Ignore RPC related specifiers
		return parse_typestr(str[1:])

	raise ValueError, "No match for "+str

def parse_signature(typestr):
	types = []
	while typestr:
		tp, typestr = parse_typestr(typestr)
		if tp == None:
			continue
		types.append(tp)
	return types



###############################################################################

def make_imp(idx, types):
	hdr = 'static %s\nmeth_imp_%d(id self, SEL sel'%(
		types[0].c_decl(''), idx)

	for i in range(3, len(types)):
		hdr += ", " + types[i].c_decl('arg_%d'%(i-1))

	hdr += ')'
	print hdr
	print '{'
	print '\tPyObject* arglist;'
	print '\tPyObject* retval;'
	print '\tPyObject* tmp;'

	if types[0] != TP_VOID:
		print '\tconst char* errstr;'
		print '\t%s;'%(types[0].c_decl('objc_retval'))

	print '\n\targlist = PyTuple_New(%d);'%(len(types)-2)
	print '\tif (arglist == NULL) ObjCErr_ToObjC();'
	print ''

	print '\ttmp = ObjC_ObjCToPython("@", &self);'
	print '\tif (tmp == NULL) ObjCErr_ToObjC();'
	print '\tPyTuple_SetItem(arglist, 0, tmp);'

	for i in range(3, len(types)):
		val = types[i]
		print '\ttmp = ObjC_ObjCToPython("%s", &arg_%d);'%(
			val.typestr(), i-1)

		print '\tif (tmp == NULL) ObjCErr_ToObjC();'
		print '\tPyTuple_SetItem(arglist, %d, tmp);'%(i-2)

	print ""

	print '\tretval = ObjC_CallPython(self, sel, arglist);'
	print '\tPy_DECREF(arglist);'
	print '\tif (retval == NULL) ObjCErr_ToObjC();'

	if types[0] != TP_VOID:
		print '\terrstr = ObjC_PythonToObjC("%s", retval, &objc_retval);'%(types[0].typestr())
		print '\tPy_DECREF(retval);'

		print '\tif (errstr != NULL) {'
		#print '\t\tObjCErr_Set(objc_error, "cannot convert result %s", errstr);'
		print '\t\tPyErr_SetString(PyExc_ValueError, "Cannot convert to ObjC");'
		print '\t\tObjCErr_ToObjC();'
		print '\t}'
		print '\treturn objc_retval;'

	print '}'


def  make_super_forwarder(idx, types):

	print 'static PyObject* super_%d(PyObject* meth, PyObject* self, PyObject* args)'%idx
	print '{'

	print '\tid objc_self;'
	print '\tconst char* errstr;'

	if len(types) > 3 or types[0] != TP_VOID:
		print '\tPyObject* v;'

	if types[0] != TP_VOID:
		print "\t%s;"%(types[0].c_decl('objc_retval'))

	for i in range(3, len(types)):
		print "\t%s;"%(types[i].c_decl('objc_arg%d'%(i-1)))

	print '\tstruct objc_super super;'
	print ''

	print '\tif (PyTuple_Size(args) != %d) {'%(len(types) - 3)
	#print '\t\tObjCErr_Set(PyExc_TypeError, ' + \
	      #'"Need %d arguments, got %%d\\n", PyTuple_Size(args));'%(
	      	#len(types)-3) 
	print "\t\tPyErr_SetString(PyExc_TypeError, \"Wrong argcount\");"
	print '\t\treturn NULL;'
	print '\t}'

	print '\terrstr = ObjC_PythonToObjC("@", self, &objc_self);'
	print '\tif (errstr != NULL) {'
	#print '\t\tObjCErr_Set(PyExc_TypeError, "depythonify_c_value failed: %s", errstr);'
	print '\t\tPyErr_SetString(PyExc_TypeError, "Cannot convert self");'
	print '\t\treturn NULL;'
	print '\t} ' + \
		'\tsuper.receiver = objc_self;' # same as c version
	print '\tsuper.class = ObjCSelector_GetClass(meth);'

	for i in range(3, len(types)):
		print '\tv = PyTuple_GetItem(args, %d);'%(i-3)
		print '\terrstr = ObjC_PythonToObjC("%s", v, &objc_arg%d);'%(types[i].typestr(), i-1)
		print '\tif (errstr) {'
		#print '\t\tObjCErr_Set(PyExc_TypeError, "depythonify_c_value failed for %s: %%s", errstr);'%types[i].typestr()
		print '\t\tPyErr_SetString(PyExc_TypeError, "Cannot convert argument");'
		print '\treturn NULL;'
		print '\t}'

	print '\tNS_DURING'
	if types[0] != TP_VOID:
		# The extra cast is needed to silence the compiler... 
		hdr = '\t\tobjc_retval = (%s)(long)'%(types[0].c_decl('').strip())
	else:
		hdr = '\t\t(void)'

	hdr += 'objc_msgSendSuper(&super, ObjCSelector_GetSelector(meth)'
	for i in range(3, len(types)):
		hdr += ', objc_arg%d'%(i-1)

	hdr += ');'
	print hdr
	print '\tNS_HANDLER'
	print '\t\tObjCErr_FromObjC(localException);'
	print '\tNS_ENDHANDLER'
	print '\tif (PyErr_Occurred()) return NULL;'

	if types[0] == TP_VOID:
		print '\tPy_INCREF(Py_None);'
		print '\treturn Py_None;'
	else:
		print '\tv = ObjC_ObjCToPython("%s", &objc_retval);'%types[0].typestr()
		print '\treturn v;'

	print '}'


def main():
	import sys
	fp = sys.stdin

	if len(sys.argv) != 2:
		sys.stderr.write("Need function name\n");
		sys.exit(1);
	func_name = sys.argv[1]

	regbuf = []

	print "/*"
 	print " * WARNING: This is a generated file, do not change"
	print " */"
	print ""
	print "#include <Python.h>"
	print "#include <objc/objc.h>"
	print "#include <objc/objc-runtime.h>"
	print "#include <Foundation/NSException.h>"
	print "#define PYOBJC_METHOD_STUB_IMPL"
	print "#include \"pyobjc-api.h\""
	print "static struct pyobjc_api* ObjC_API;"
	print "typedef int (*superfunc)();"

	nr =  0
	for ln in fp:
		ln = ln.strip()
		print "/* signature: %s */"%ln
		types = parse_signature(ln)

		for t in types:
			s = t.c_pre_decl()
			if s:
				print s
		make_imp(nr, types);
		make_super_forwarder(nr, types);
		print ""
		print ""
		regbuf.append( '\t{ "%s", (superfunc)super_%d, (IMP)meth_imp_%d },'%(ln, nr, nr))
		nr += 1

	print "static struct method_table {"
	print "\tchar* signature;"
	print "\tsuperfunc call_super;"
	print "\tIMP implementation;"
	print "} method_table[] = {"
	print "\n".join(regbuf)
	print "\t{0, 0}"
	print "};"
	print ""
	print "int %s(struct pyobjc_api* api)"%func_name
	print "{"
	print "\tstruct method_table* cur = method_table;"
	print ""
	print "\tObjC_API = api;\n"
	print ""
	print "\twhile (cur->signature) {"
	print "\t\tif (ObjC_RegisterSignatureMapping("
	print "\t\t\t\tcur->signature,"
	print "\t\t\t\tcur->call_super,"
	print "\t\t\t\tcur->implementation) < 0) {"
	print "\t\t\treturn -1;"
	print "\t\t}"
	print "\t\tcur ++;"
	print "\t}"
	print "\treturn 0;"
	print "}"

main()
