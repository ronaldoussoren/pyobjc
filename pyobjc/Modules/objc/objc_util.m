/*
 * Some utility functions...
 *
 * TODO: Documentation
 */

#include "pyobjc.h"

#import <Foundation/NSString.h>
#import <Foundation/NSDictionary.h>

PyObject* ObjCExc_error;
PyObject* ObjCExc_noclass_error;
PyObject* ObjCExc_internal_error;

int ObjCUtil_Init(PyObject* module)
{
#define NEW_EXC(identifier, name, base_class) \
	identifier = PyErr_NewException("objc."name, base_class, NULL); \
	if (identifier == NULL) return -1; \
	Py_INCREF(identifier); \
	if (PyModule_AddObject(module, name, identifier) < 0) return -1;

	NEW_EXC(ObjCExc_error, "error", NULL);
	NEW_EXC(ObjCExc_noclass_error, "nosuchclass_error", ObjCExc_error);
	NEW_EXC(ObjCExc_internal_error, "internal_error", ObjCExc_error);

	return 0;
}

void ObjCErr_Set(PyObject* exc, char* fmt, ...)
{
	char buf[1024];
	va_list ap;
	
	va_start(ap, fmt);
	vsnprintf(buf, sizeof(buf), fmt, ap);
	va_end(ap);

	PyErr_SetString(exc, buf);
}


static PyObject* 
ObjCErr_PyExcForName(const char* value)
{
	/* TODO: This table should be changeable from python */
	if (strcmp(value, "NSRangeException") == 0) {
		return PyExc_IndexError;
	}  else if (strcmp(value, "NSInvalidArgumentException") == 0) {
		return PyExc_ValueError;
	}  else if (strcmp(value, "NSMallocException") == 0) {
		return PyExc_MemoryError;
	}  else if (strcmp(value, "NSUnknownKeyException") == 0) {
		return PyExc_KeyError;
	}

	return ObjCExc_error;
}
	

void PyObjCErr_FromObjC(NSException* localException)
{
	NSDictionary* userInfo;
	PyObject*     dict;
	PyObject*     exception;
	PyObject*     v;
	char          buf[256];
	PyObject*     exc_type;
	PyObject*     exc_value;
	PyObject*     exc_traceback;

	exception = ObjCErr_PyExcForName([[localException name] cString]);

	userInfo = [localException userInfo];
	if (userInfo) {
		id val;

		val = [userInfo objectForKey:@"__pyobjc_exc_type__"];
		if (val) {
			exc_type = [val  pyObject];
			exc_value = [[userInfo objectForKey:@"__pyobjc_exc_value__"]  pyObject];
			exc_traceback = [[userInfo objectForKey:@"__pyobjc_exc_traceback__"]  pyObject];

			/* -pyObject returns a borrowed reference and 
			 * PyErr_Restore steals one from us.
			 */
			Py_INCREF(exc_type);
			Py_XINCREF(exc_value);
			Py_XINCREF(exc_traceback);

			PyErr_Restore(exc_type, exc_value , exc_traceback);
			return;
		}
	}

	dict = PyDict_New();
	v = PyString_FromString([[localException name] cString]);
	PyDict_SetItemString(dict, "name", v);
	v = PyString_FromString([[localException reason] cString]);
	PyDict_SetItemString(dict, "reason",  v);
	Py_DECREF(v);
	if (userInfo) {
		v = PyObjCObject_New(userInfo);
		if (v != NULL) {
			PyDict_SetItemString(dict, "userInfo", v);
			Py_DECREF(v);
		} else { 
			PyErr_Clear();
		}
	} else {
		PyDict_SetItemString(dict, "userInfo", Py_None);
	}

	snprintf(buf, sizeof(buf), "%s - %s", 
		[[localException name] cString],
		[[localException reason] cString]);

	PyErr_SetObject(exception, PyString_FromString(buf));
	PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
	if (!exc_value || !PyObject_IsInstance(exc_value, exc_type)) {
		PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);
	}
	PyObject_SetAttrString(exc_value, "_pyobjc_info_", dict);
	PyObject_SetAttrString(exc_value, "name", PyString_FromString(
		[[localException name] cString]));
	PyErr_Restore(exc_type, exc_value, exc_traceback);
}

void PyObjCErr_ToObjC(void)
{
	PyObjCErr_ToObjCWithGILState(NULL);
}

void PyObjCErr_ToObjCWithGILState(PyGILState_STATE* state)
{
	PyObject* exc_type;
	PyObject* exc_value;
	PyObject* exc_traceback;
	PyObject* args;
	PyObject* repr;
	NSException* val;
	NSMutableDictionary* userInfo;

	PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
	if (!exc_type)
		return;

	PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);

	args = PyObject_GetAttrString(exc_value, "_pyobjc_info_");
	if (args == NULL) {
		PyErr_Clear();
	} else {
		/* This may be an exception that started out in 
		 * Objective-C code.
		 */
		PyObject* v;
		char*     reason = NULL;
		char*     name = NULL;

		v = PyDict_GetItemString(args, "reason"); 
		if (v && PyString_Check(v)) {
			reason = PyString_AsString(v);
		} else {
			PyErr_Clear();
		}

		v = PyDict_GetItemString(args, "name"); 
		if (v && PyString_Check(v)) {
			name = PyString_AsString(v);
		} else {
			PyErr_Clear();
		}

		v = PyDict_GetItemString(args, "userInfo");
		if (v && PyObjCObject_Check(v)) {
			userInfo = PyObjCObject_GetObject(v);
		} else {
			userInfo = nil;
			PyErr_Clear();
		}

		if (name && reason) {
			id oc_name;
			id oc_reason;

			oc_name = [NSString stringWithCString:name];
			oc_reason = [NSString stringWithCString:reason];
			val = [NSException exceptionWithName:oc_name
				     reason:oc_reason
				     userInfo:userInfo];
			Py_DECREF(args);
			Py_XDECREF(exc_type);
			Py_XDECREF(exc_value);
			Py_XDECREF(exc_traceback);
			
			if (state) {
				PyGILState_Release(*state);
			}
			[val raise];
		}
	}
	Py_XDECREF(args);

	repr = PyObject_Str(exc_value);
	userInfo = [NSMutableDictionary dictionaryWithCapacity: 3];
	[userInfo setObject:
		[OC_PythonObject newWithObject:exc_type]
		forKey:@"__pyobjc_exc_type__"];
	if (exc_value != NULL)
		[userInfo setObject:
			[OC_PythonObject newWithObject:exc_value]
			forKey:@"__pyobjc_exc_value__"];
	if (exc_traceback != NULL)
		[userInfo setObject:
			[OC_PythonObject newWithObject:exc_traceback]
			forKey:@"__pyobjc_exc_traceback__"];

	val = [NSException 
		exceptionWithName:@"OC_PythonException"
		reason:[NSString stringWithCString:PyString_AS_STRING(repr)]
		userInfo:userInfo];

	Py_DECREF(repr);

	if (ObjC_VerboseLevel) {
		PyErr_Restore(exc_type, exc_value , exc_traceback);
		NSLog(@"PyObjC: Converting exception to Objective-C:");
		PyErr_Print();
	} else {
		Py_DECREF(exc_type);
		Py_XDECREF(exc_value);
		Py_XDECREF(exc_traceback);
	}
	if (state) {
		PyGILState_Release(*state);
	}
	[val raise];
}

PyObject* ObjC_class_extender = NULL;

int ObjC_AddConvenienceMethods(Class cls, PyObject* type_dict)
{
	PyObject* super_class;
	PyObject* name;
	PyObject* res;
	PyObject* args;

	if (ObjC_class_extender == NULL || cls == nil) return 0;

	if (cls->super_class == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(cls->super_class);
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(cls->name);
	if (name == NULL) {
		Py_DECREF(super_class);
		return -1;
	}

	args = PyTuple_New(3);
	if (args == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		return -1;
	}

	PyTuple_SET_ITEM(args, 0, super_class);
	PyTuple_SET_ITEM(args, 1, name);
	PyTuple_SET_ITEM(args, 2, type_dict);
	Py_INCREF(type_dict);

	res = PyObject_CallObject(ObjC_class_extender, args);
	Py_DECREF(args);
	if (res == NULL) {
		return -1;
	}
	Py_DECREF(res);

	return 0;
}

/* 
 * Update the convenience methods. We can't just change the type dict here,
 * because the type doesn't pick up new '__' methods  (like __getitem__) 
 * that way.
 */
int ObjC_UpdateConvenienceMethods(PyObject* cls)
{
	PyObject* super_class;
	PyObject* name;
	PyObject* res;
	PyObject* args;
	Class     objc_cls;
	PyObject* dict;
	PyObject* keys;
	PyObject* v;
	int       i, len;

	if (!PyObjCClass_Check(cls)) {
		PyErr_SetString(PyExc_TypeError, "not a class");
		return -1;
	}
	

	if (ObjC_class_extender == NULL || cls == NULL) return 0;

	objc_cls = PyObjCClass_GetClass(cls);

	if (objc_cls->super_class == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(objc_cls->super_class);
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(objc_cls->name);
	if (name == NULL) {
		Py_DECREF(super_class);
		return -1;
	}

	dict = /*PyDict_Copy*/(((PyTypeObject*)cls)->tp_dict);
	Py_INCREF(dict);
	if (dict == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		return -1;
	}

	args = PyTuple_New(3);
	if (args == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		Py_DECREF(dict);
		return -1;
	}

	PyTuple_SET_ITEM(args, 0, super_class);
	PyTuple_SET_ITEM(args, 1, name);
	PyTuple_SET_ITEM(args, 2, dict);

	res = PyObject_CallObject(ObjC_class_extender, args);
	if (res == NULL) {
		Py_DECREF(args);
		return -1;
	}
	Py_DECREF(res);
	keys = PyDict_Keys(dict);
	if (keys == NULL) {
		Py_DECREF(args);
		return -1;
	}

	v = PySequence_Fast(keys, "PyDict_Keys didn't return a sequence");
	Py_DECREF(keys);
	if (v == NULL) {
		return -1;
	}
	keys = v;

	len = PySequence_Fast_GET_SIZE(keys);
	for (i = 0; i < len; i++) {
		PyObject* k = PySequence_Fast_GET_ITEM(keys, i);
		char*     n;
		
		if (k == NULL) {
			PyErr_Clear();
			continue;
		}

		if (!PyString_Check(k)) {
			continue;
		}
		n = PyString_AS_STRING(k);
		if (n[0] != '_' || n[1] != '_') {
			continue;
		}
		if (	   strcmp(n, "__dict__") == 0 
			|| strcmp(n, "__bases__") == 0
			|| strcmp(n, "__slots__") == 0
			|| strcmp(n, "__mro__") == 0
		   ) {

			continue;
		}

		v = PyDict_GetItem(dict, k);
		if (v == NULL) {
			continue;
		}
		if (PyObject_SetAttr(cls, k, v) == -1) {
			continue;
		}
	}

	Py_DECREF(keys);
	Py_DECREF(args);

	return 0;
}

char* ObjC_strdup(const char* value)
{
	int len;
	char* result;

	len = strlen(value);
	result = PyMem_Malloc(len+1);
	if (result == NULL) return NULL;

	memcpy(result, value, len);
	result[len] = 0;
	return result;
}


NSMapTableKeyCallBacks ObjC_PointerKeyCallBacks = {
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
};

NSMapTableValueCallBacks ObjC_PointerValueCallBacks = {
	NULL,
	NULL,
	NULL,
};

#define SHOULD_FREE 0
#define SHOULD_IGNORE 1

void    PyObjC_FreeCArray(int code, void* array)
{
	if (code == SHOULD_FREE) {
		free(array);
	}
}

static PyTypeObject* array_type = NULL;

static inline PyTypeObject* fetch_array_type(void)
{
	PyObject* mod;
	PyObject* name;

	if (array_type != NULL) return array_type;

	name = PyString_FromString("array");
	if (name == NULL) {
		return NULL;
	}

	mod = PyImport_Import(name);
	Py_DECREF(name);
	if (mod == NULL) {
		return NULL;
	}

	array_type = (PyTypeObject*)PyObject_GetAttrString(mod, "array");
	Py_DECREF(mod);
	if (array_type == NULL) {
		return NULL;
	}

	/* XXX: check if array_type is realy a type! */

	return array_type;
}

#define array_check(obj) PyObject_TypeCheck(obj, fetch_array_type())

static char 
array_typestr(PyObject* array)
{
	PyObject* typecode;
	char res;

	typecode = PyObject_GetAttrString(array, "typecode");
	if (typecode == NULL) {
		return '\0';
	}

	if (!PyString_Check(typecode)) {
		PyErr_SetString(PyExc_TypeError, "typecode not a string");
		return '\0';
	}

	switch (*PyString_AS_STRING(typecode)) {
	case 'c': res = _C_CHR; break;
	case 'b': res = _C_CHR; break;
	case 'B': res = _C_UCHR; break;
	case 'u': res = _C_SHT; break;
	case 'h': res = _C_SHT; break;
	case 'H': res = _C_USHT; break;
	case 'i': res = _C_INT; break;
	case 'I': res = _C_UINT; break;
	case 'l': res = _C_LNG; break;
	case 'L': res = _C_ULNG; break;
	case 'f': res = _C_FLT; break;
	case 'd': res = _C_DBL; break;
	default: 
		PyErr_SetString(PyExc_TypeError, "unsupported typecode");
		res = '\0';
	}
	Py_DECREF(typecode);
	
	return res;
}

static int 
buffer_get(PyObject* obj, void** bufptr, int* sizeptr)
{
	int r;

	r = PyArg_Parse(obj, "s#", bufptr, sizeptr);
	if (!r) {
		return -1;
	}
	return 0;

#if 0
	PyBufferProcs* pb = obj->ob_type->tp_as_buffer;
	if (!PyType_HasFeature(obj->ob_type,
				Py_TPFLAGS_HAVE_GETCHARBUFFER) ||
				pb == NULL || 
				pb->bf_getcharbuffer == NULL ||
				pb->bf_getsegcount == NULL) {
		PyErr_SetString(PyExc_TypeError, "cannot access buffer");
		return -1;
	}

	if (pb->bf_getsegcount(obj, NULL) != 1) {
		PyErr_SetString(PyExc_TypeError, 
				"cannot access multi-segment buffer");
		return -1;
	}
	
	*sizeptr = pb->bf_getcharbuffer(obj, 0, (const char**)bufptr);
	if (*sizeptr < 0) {
		PyErr_SetString(PyExc_TypeError,
				"error accessing buffer object");
		return -1;
	}
	return 0;
#endif
}

static char struct_elem_code(const char* typestr);

static char
array_elem_code(const char* typestr)
{
	char res = '\0';
	char tmp;

	if (*typestr++ != _C_ARY_B) {
		return '\0';
	}
	while (isdigit(*typestr)) typestr++;

	if (*typestr == _C_ARY_E) {
		return '\0';
	}

	while (typestr && *typestr != _C_ARY_E) {
		switch(*typestr) {
		case _C_ARY_B:
			tmp = array_elem_code(typestr);
			if (tmp == '\0') return '\0';
			if (res == '\0') {
				res = tmp;
			} else if (tmp != res) {
				return '\0';
			}
			break;
		case _C_STRUCT_B:
			tmp = struct_elem_code(typestr);
			if (tmp == '\0') return '\0';
			if (res == '\0') {
				res = tmp;
			} else if (tmp != res) {
				return '\0';
			}
			break;
		default:
			if (res != '\0' && *typestr != res) return '\0';
			res = *typestr;
		}

		typestr = PyObjCRT_SkipTypeSpec(typestr);
	}
	return res;
}

static char
struct_elem_code(const char* typestr)
{
	char res = '\0';
	char tmp;

	if (*typestr++ != _C_STRUCT_B) {
		return '\0';
	}

	while (*typestr != '=' && *typestr != _C_STRUCT_E) {
		typestr++;
	}

	if (*typestr == _C_STRUCT_E) {
		return '\0';
	}
	typestr++;

	while (typestr && *typestr != _C_STRUCT_E) {
		switch(*typestr) {
		case _C_ARY_B:
			tmp = array_elem_code(typestr);
			if (tmp == '\0') return '\0';
			if (res == '\0') {
				res = tmp;
			} else if (tmp != res) {
				return '\0';
			}
			break;
		case _C_STRUCT_B:
			tmp = struct_elem_code(typestr);
			if (tmp == '\0') return '\0';
			if (res == '\0') {
				res = tmp;
			} else if (tmp != res) {
				return '\0';
			}
			break;
		default:
			if (res != '\0' && *typestr != res) return '\0';
			res = *typestr;
		}

		typestr = PyObjCRT_SkipTypeSpec(typestr);
	}
	return res;
}
		


	

/*
 * Convert a Python object to an array of 'elementType'. The array should
 * contain 'pythonCount' elements, Py_None or NULL is accepted and will result
 * in converting the entire Python sequence.
 *
 * The pythonList should either be a python sequence with appropriate entries,
 * an array.array whose element-types match the element-types of the 
 * 'elementType' or an appropriatly typed and shaped numeric array.
 * 
 * XXX: Numeric arrays are not yet supported.
 */
int	PyObjC_PythonToCArray(
		const char* elementType,
		PyObject* pythonList,
		PyObject* pythonCount,
		void** array,
		int*   size)
{
	int eltsize = PyObjCRT_SizeOfType(elementType);
	int eltcount;
	int i, r;

	if (eltsize == -1) {
		return -1;
	}

	if (eltsize == 1) {
		/* A simple byte-array */
		char* buf;
		int bufsize;

		if (buffer_get(pythonList, (void**)&buf, &bufsize) == -1) {
			return -1;
		}
		if (pythonCount == Py_None || pythonCount == NULL) {
			*array = buf;
			*size = bufsize;
		} else {
			r = depythonify_c_value(@encode(int), pythonCount, &eltcount);
			if (r == -1) {
				return -1;
			}
			if (eltcount > bufsize) {
				PyErr_Format(PyExc_ValueError,
					"Requesting buffer of %d, have buffer "
					"of %d", eltcount, bufsize);
				return -1;
			}
			*array = buf;
			*size = eltcount;
		}
		return SHOULD_IGNORE;
	} 

	/* A more complex array */

	if (array_check(pythonList)) {
		/* An array.array. Only convert if the typestr describes an
		 * simple type of the same type as the array, or a struct/array
		 * containing only elements of the type of the array.
		 */
		char* buf;
		int bufsize;
		char code = array_typestr(pythonList);
		if (code == *elementType) {
			/* Simple array, ok */
		} else if (*elementType == _C_ARY_B) {
			/* Array of arrays, 'code' must be the same as the
			 * element-type of the array.
			 */
			if (code != array_elem_code(elementType)) {
				PyErr_Format(PyExc_ValueError, 
					"type mismatch between array.array "
					"of %c and and C array of %s",
					code, elementType);
				return -1;
			}

		} else if (*elementType == _C_STRUCT_B) {
			/* Array of structs, 'code' must be the same as the
			 * the field-types of the structs (that is, the struct
			 * must contain one or more fields of type 'code').
			 */
			if (code != struct_elem_code(elementType)) {
				PyErr_Format(PyExc_ValueError, 
					"type mismatch between array.array "
					"of %c and and C array of %s",
					code, elementType);
				return -1;
			}
		} else {
			PyErr_Format(PyExc_ValueError, 
				"type mismatch between array.array "
				"of %c and and C array of %s",
				code, elementType);
			return -1;
		}

		if (buffer_get(pythonList, (void**)&buf, &bufsize) == -1) {
			return -1;
		}
		if ((bufsize % eltsize) != 0) {
			PyErr_SetString(PyExc_ValueError, 
					"Badly shaped array.array");
			return -1;
		}

		*array = buf;

		if (pythonCount == Py_None || pythonCount == NULL) {
			*size = bufsize / eltsize;
		} else {

			r = depythonify_c_value(@encode(int), pythonCount, &eltcount);
			if (r == -1) {
				return -1;
			}
			bufsize /= eltsize;

			if (eltcount > bufsize) {
				PyErr_Format(PyExc_ValueError,
					"Requesting buffer of %d, have buffer "
					"of %d", eltcount, bufsize);
				return -1;
			}
			*array = buf;
			*size = eltcount;
		}
		return SHOULD_IGNORE;

#ifdef PyObjC_ENABLE_NUMARRAY

# error "Please implement Numarray/Numeric support"

	} else if (...){
		/* TODO: Convert the numeric array (or return a pointer to it's
		 * data), but only if it is the right type:
		 * - If typestr is a basic type, the array must be a 1D array
		 *   of that type
		 * - If typestr is a structred type, the array must be a 2D
		 *   array where rows match the structured type
		 *
		 * XXX: I have no idea if this is feasable, not having used
		 * numarray/numeric myself.
		 */
#endif /* PyObjC_ENABLE_NUMARRAY */
	} else {
		int seqlen;
		int pycount;
		PyObject* seq = PySequence_Fast(pythonList, 
					"converting to a C array");
		if (seq == NULL) {
			return -1;
		}

		seqlen = PySequence_Fast_GET_SIZE(seq);
		if (pythonCount == Py_None || pythonCount == NULL) {
			pycount = seqlen;
		} else {
			r = depythonify_c_value(
					@encode(int), pythonCount, &pycount);
			if (r == -1) {
				Py_DECREF(seq);
				return -1;
			}
		}

		if (seqlen < pycount) {
			Py_DECREF(seq);
			PyErr_Format(PyExc_ValueError,
					"too few values (%d) expecting at "
					"least %d", seqlen, pycount);
			return -1;
		}
		*array = malloc(eltsize * pycount);
		if (*array == NULL) {
			Py_DECREF(seq);
			PyErr_NoMemory();
			return -1;
		}
		*size = pycount;

		for (i = 0; i < pycount; i++) {
			PyObject* item = PySequence_Fast_GET_ITEM(seq, i);

			r = depythonify_c_value(elementType, item,
					((char*)*array)+(i*eltsize));
			if (r == -1) {
				Py_DECREF(seq);
				free(*array); *array = NULL;
				return -1;
			}
		}
		return SHOULD_FREE;
	}
	
}

PyObject* PyObjC_CArrayToPython(
		const char* elementType,
		void* array,
		int   size)
{
	PyObject* result;
	int i;
	int eltsize;

	result = PyTuple_New(size);
	if (result == NULL) {
		return NULL;
	}

	eltsize = PyObjCRT_SizeOfType(elementType);

	for (i = 0; i < size; i++) {
		PyObject* elt = pythonify_c_value(elementType, array);
		if (elt == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		PyTuple_SET_ITEM(result, i, elt);
		array = ((char*)array) + eltsize;
	}

	return result;
}
