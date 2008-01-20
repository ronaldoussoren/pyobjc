/*
 * Some utility functions...
 *
 * TODO: Documentation
 */

#include "pyobjc.h"

#import <Foundation/Foundation.h>

PyObject* PyObjCExc_Error;
PyObject* PyObjCExc_NoSuchClassError;
PyObject* PyObjCExc_InternalError;
PyObject* PyObjCExc_UnInitDeallocWarning;
PyObject* PyObjCExc_ObjCRevivalWarning;
PyObject* PyObjCExc_LockError;


int 
PyObjCUtil_Init(PyObject* module)
{
#define NEW_EXC(identifier, name, base_class) \
	identifier = PyErr_NewException("objc."name, base_class, NULL); \
	if (identifier == NULL) return -1; \
	Py_INCREF(identifier); \
	if (PyModule_AddObject(module, name, identifier) < 0) return -1;

	NEW_EXC(PyObjCExc_Error, "error", NULL);
	NEW_EXC(PyObjCExc_NoSuchClassError, "nosuchclass_error", PyObjCExc_Error);
	NEW_EXC(PyObjCExc_InternalError, "internal_error", PyObjCExc_Error);
	NEW_EXC(PyObjCExc_UnInitDeallocWarning, "UninitializedDeallocWarning", PyExc_Warning);
	NEW_EXC(PyObjCExc_ObjCRevivalWarning, "RevivedObjectiveCObjectWarning", PyExc_Warning);
	NEW_EXC(PyObjCExc_LockError, "LockError", PyObjCExc_Error);

	return 0;
}

static PyObject* 
ObjCErr_PyExcForName(const char* value)
{
	/* XXX: This table should be changeable from python */
	if (strcmp(value, "NSRangeException") == 0) {
		return PyExc_IndexError;
	}  else if (strcmp(value, "NSInvalidArgumentException") == 0) {
		return PyExc_ValueError;
	}  else if (strcmp(value, "NSMallocException") == 0) {
		return PyExc_MemoryError;
	}  else if (strcmp(value, "NSUnknownKeyException") == 0) {
		return PyExc_KeyError;
	}

	return PyObjCExc_Error;
}
	

void 
PyObjCErr_FromObjC(NSException* localException)
{
	NSDictionary* userInfo;
	PyObject*     dict;
	PyObject*     exception;
	PyObject*     v;
	PyObject*	  buf;
	PyObject*     exc_type;
	PyObject*     exc_value;
	PyObject*     exc_traceback;
	PyObject*     c_localException_name;
	PyObject*     c_localException_reason;
	NSObject* t;

	PyGILState_STATE state;

	state = PyGILState_Ensure();

	exception = ObjCErr_PyExcForName([[localException name] UTF8String]);

	userInfo = [localException userInfo];
	if (userInfo) {
		id val;

		val = [userInfo objectForKey:@"__pyobjc_exc_type__"];
		if (val) {
			exc_type = [val pyObject];
			exc_value = [[userInfo objectForKey:@"__pyobjc_exc_value__"]  pyObject];
			exc_traceback = [[userInfo objectForKey:@"__pyobjc_exc_traceback__"]  pyObject];

			/* -pyObject returns a borrowed reference and 
			 * PyErr_Restore steals one from us.
			 */
			Py_INCREF(exc_type);
			Py_XINCREF(exc_value);
			Py_XINCREF(exc_traceback);

			PyErr_Restore(exc_type, exc_value, exc_traceback);
			PyGILState_Release(state);
			return;
		}
	}

	t = [localException name];
	c_localException_name = pythonify_c_value(@encode(NSObject*), &t);
	if (c_localException_name == NULL) {
		return;
	}

	t = [localException reason];
	c_localException_reason = pythonify_c_value(@encode(NSObject*), &t);
	if (c_localException_reason == NULL) {
		Py_DECREF(c_localException_name);
		return;
	}

	dict = PyDict_New();
	if (dict == NULL) {
		Py_DECREF(c_localException_name);
		Py_DECREF(c_localException_reason);
		return;
	}
	PyDict_SetItemString(dict, "name", c_localException_name);
	Py_DECREF(c_localException_name);

	PyDict_SetItemString(dict, "reason",  c_localException_reason);
	Py_DECREF(c_localException_reason);
	if (userInfo) {
		v = PyObjCObject_New(userInfo, PyObjCObject_kDEFAULT, YES);
		if (v != NULL) {
			PyDict_SetItemString(dict, "userInfo", v);
			Py_DECREF(v);
		} else { 
			PyErr_Clear();
		}
	} else {
		PyDict_SetItemString(dict, "userInfo", Py_None);
	}

#if 0	
	/* build the description as a NSString to maintain the highest 
	 * fidelity.
	 * This code is disabled because the base exception class doesn't
	 * like unicode arguments, that will wreak havoc when converting the
	 * exception to text, which in turn makes it impossible to find out
	 * what the exception actually was without poking in the PyObjC
	 * specific fields.
	 */
	NSString* description = [NSString stringWithFormat:@"%@ - %@",
			[localException name], [localException reason]];
	if (description == nil) {
		PyErr_SetString(exception, "<<<UNKNOWN REASON>>>");
	} else {
		buf = pythonify_c_value(@encode(NSObject*), &description);
		if (buf == NULL) {
			Py_DECREF(dict);
			PyGILState_Release(state);
			return;
		}
	}
#else
	 buf = PyString_FromFormat("%s - %s", 
               [[localException name] UTF8String],
               [[localException reason] UTF8String]);
	PyErr_SetObject(exception, buf);
#endif
	PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
	if (!exc_value || !PyObject_IsInstance(exc_value, exc_type)) {
		PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);
	}

	PyObject_SetAttrString(exc_value, "_pyobjc_info_", dict);
	Py_DECREF(dict); dict = NULL;
	PyObject_SetAttrString(exc_value, "name", c_localException_name);
	PyErr_Restore(exc_type, exc_value, exc_traceback);
	PyGILState_Release(state);
}

void 
PyObjCErr_ToObjC(void)
{
	PyObjCErr_ToObjCWithGILState(NULL);
}


NSException* 
PyObjCErr_AsExc(void)
{
	PyObject* exc_type;
	PyObject* exc_value;
	PyObject* exc_traceback;
	PyObject* args;
	PyObject* repr;
	PyObject* typerepr;
	NSException* val;
	NSMutableDictionary* userInfo;

	PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
	if (exc_type == NULL) {
		return nil;
	}

	PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);

	args = PyObject_GetAttrString(exc_value, "_pyobjc_info_");
	if (args == NULL) {
		PyErr_Clear();
	} else {
		/* This may be an exception that started out in 
		 * Objective-C code.
		 */
		PyObject* v;
		NSString* reason = NULL;
		NSString* name = NULL;

		v = PyDict_GetItemString(args, "reason"); 
		if (v) {
			if (depythonify_c_value(@encode(NSObject*), v, &reason) < 0) {
				PyErr_Clear();
			}
		}

		v = PyDict_GetItemString(args, "name"); 
		if (v) {
			if (depythonify_c_value(@encode(NSObject*), v, &name) < 0) {
				PyErr_Clear();
			}
		}

		v = PyDict_GetItemString(args, "userInfo");
		if (v && PyObjCObject_Check(v)) {
			userInfo = PyObjCObject_GetObject(v);
		} else {
			userInfo = nil;
			PyErr_Clear();
		}

		if (name && reason) {
			val = [NSException exceptionWithName:name
				     reason:reason
				     userInfo:userInfo];
			Py_DECREF(args);
			Py_XDECREF(exc_type);
			Py_XDECREF(exc_value);
			Py_XDECREF(exc_traceback);
			
			return val;
		}
	}

	repr = PyObject_Str(exc_value);
	typerepr = PyObject_Str(exc_type);
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
		reason:[NSString stringWithFormat:@"%s: %s", PyString_AS_STRING(typerepr), PyString_AS_STRING(repr)]
		userInfo:userInfo];

	Py_DECREF(typerepr);
	Py_DECREF(repr);

	if (PyObjC_VerboseLevel) {
		PyErr_Restore(exc_type, exc_value , exc_traceback);
		NSLog(@"PyObjC: Converting exception to Objective-C:");
		PyErr_Print();
	} else {
		Py_DECREF(exc_type);
		Py_XDECREF(exc_value);
		Py_XDECREF(exc_traceback);
	}
	return val;
}

void 
PyObjCErr_ToObjCWithGILState(PyGILState_STATE* state)
{
	NSException* exc = PyObjCErr_AsExc();

	if (state) {
		PyGILState_Release(*state);
	}
	[exc raise];
}


char* 
PyObjCUtil_Strdup(const char* value)
{
	Py_ssize_t len;
	char* result;

	len = strlen(value);
	result = PyMem_Malloc(len+1);
	if (result == NULL) return NULL;

	memcpy(result, value, len);
	result[len] = 0;
	return result;
}


NSMapTableKeyCallBacks PyObjCUtil_PointerKeyCallBacks = {
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
};

NSMapTableValueCallBacks PyObjCUtil_PointerValueCallBacks = {
	NULL,
	NULL,
	NULL,
};

static void
nsmaptable_objc_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	CFRetain((id)datum);
}

static void
nsmaptable_objc_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	CFRelease((id)datum);
}

NSMapTableKeyCallBacks PyObjCUtil_ObjCIdentityKeyCallBacks = {
	NULL,
	NULL,
	&nsmaptable_objc_retain,
	&nsmaptable_objc_release,
	NULL,
	NULL,
};

NSMapTableValueCallBacks PyObjCUtil_ObjCValueCallBacks = {
	&nsmaptable_objc_retain,
	&nsmaptable_objc_release,
	NULL  // generic description
};


#define SHOULD_FREE 1
#define SHOULD_IGNORE 2

void
PyObjC_FreeCArray(int code, void* array)
{
	if (code == SHOULD_FREE) {
		PyMem_Free(array);
	}
}

static PyTypeObject* array_type = NULL;

static inline PyTypeObject* 
fetch_array_type(void)
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

	array_type = (PyTypeObject*)PyObject_GetAttrString(mod, "ArrayType");
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
buffer_get(BOOL writable, PyObject* obj, void** bufptr, Py_ssize_t* sizeptr)
{
	if (writable) {
		return PyObject_AsWriteBuffer(obj, bufptr,  sizeptr);
	} else {
		return PyObject_AsReadBuffer(obj, (const void**)bufptr,  sizeptr);
	}
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
int	
PyObjC_PythonToCArray(
	BOOL        writable, BOOL exactSize,
	const char* elementType,
	PyObject*   pythonList,
	void** array,
	Py_ssize_t*   size,
	PyObject**    bufobj)
{
	Py_ssize_t eltsize = PyObjCRT_SizeOfType(elementType);
	Py_ssize_t i;
	int r;


	if (eltsize == -1) {
		return -1;
	}

	if (eltsize == 1 || eltsize == 0) {
		/* A simple byte-array */
		char* buf;
		Py_ssize_t bufsize;

		if (buffer_get(writable, pythonList, (void**)&buf, &bufsize) == -1) {
			if (writable) {
				/* Ensure that the expected semantics still work
				 * when the passed in buffer is read-only
				 */
				if (buffer_get(NO, pythonList, (void**)&buf, &bufsize) == -1) {
					return -1;
				}

				if (size == NULL || *size == -1) {
					*array = PyMem_Malloc(bufsize);
					if (*array == NULL) {
						return -1;
					}
					memcpy(*array, buf, bufsize);
				} else {
					if ((exactSize && *size != bufsize) || (!exactSize && *size > bufsize)) {
						PyErr_Format(PyExc_ValueError,
							"Requesting buffer of %"PY_FORMAT_SIZE_T"d, have buffer "
							"of %"PY_FORMAT_SIZE_T"d", *size, bufsize);
						return -1;
					}
					*array = PyMem_Malloc(*size);
					if (*array == NULL) {
						return -1;
					}
					memcpy(*array, buf, *size);
				}
				return SHOULD_FREE;
			}
			return -1;
		}
		if (size == NULL) {
			*array = buf;

		} else if (*size == -1) {
			*array = buf;
			*size = bufsize;

		} else {
			if ((exactSize && *size != bufsize) || (!exactSize && *size > bufsize)) {
				PyErr_Format(PyExc_ValueError,
					"Requesting buffer of %"PY_FORMAT_SIZE_T"d, have buffer "
					"of %"PY_FORMAT_SIZE_T"d", *size, bufsize);
				return -1;
			}
			*array = buf;
			*bufobj = pythonList;
			Py_INCREF(pythonList);
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
		Py_ssize_t bufsize;
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

		if (buffer_get(writable, pythonList, (void**)&buf, &bufsize) == -1) {
			return -1;
		}
		if ((bufsize % eltsize) != 0) {
			PyErr_SetString(PyExc_ValueError, 
					"Badly shaped array.array");
			return -1;
		}

		*array = buf;

		if (size == NULL) {
			/* pass */

		} else if (*size == -1) {
			*size = bufsize / eltsize;

		} else {
			bufsize /= eltsize;

			if ((exactSize && *size != bufsize) || (!exactSize && *size > bufsize)) {
				PyErr_Format(PyExc_ValueError,
					"Requesting buffer of %"PY_FORMAT_SIZE_T"d, have buffer "
					"of %"PY_FORMAT_SIZE_T"d", *size, bufsize);
				return -1;
			}
			*array = buf;
			*bufobj = pythonList;
			Py_INCREF(pythonList);
		}
		return SHOULD_IGNORE;

#ifdef PyObjC_ENABLE_NUMARRAY

# error "Please implement Numarray/Numeric support"

	} else if (...){
		/* TODO: Convert the numeric array (or return a pointer to it's
		 * data), but only if it is the right type:
		 * - If typestr is a basic type, the array must be a 1D array
		 *   of that type
		 * - If typestr is a structured type, the array must be a 2D
		 *   array where rows match the structured type
		 *
		 * XXX: I have no idea if this is feasable, not having used
		 * numarray/numeric myself.
		 */
#endif /* PyObjC_ENABLE_NUMARRAY */
	} else {
		Py_ssize_t seqlen;
		Py_ssize_t pycount;
		PyObject* seq = PySequence_Fast(pythonList, 
					"converting to a C array");
		if (seq == NULL) {
			return -1;
		}

		seqlen = PySequence_Fast_GET_SIZE(seq);
		if (size == NULL || *size == -1) {
			pycount = seqlen;
		} else {
			pycount = *size;
		}

		if ((exactSize && seqlen != pycount) || (!exactSize && seqlen < pycount)) {
			Py_DECREF(seq);
			PyErr_Format(PyExc_ValueError,
					"too few values (%"PY_FORMAT_SIZE_T"d) expecting at "
					"least %"PY_FORMAT_SIZE_T"d", seqlen, pycount);
			return -1;
		}
		*array = PyMem_Malloc(eltsize * pycount);
		if (*array == NULL) {
			Py_DECREF(seq);
			PyErr_NoMemory();
			return -1;
		}
		if (size) {
			*size = pycount;
		}
		*bufobj = NULL;

		for (i = 0; i < pycount; i++) {
			PyObject* item = PySequence_Fast_GET_ITEM(seq, i);

			r = depythonify_c_value(elementType, item,
					((char*)*array)+(i*eltsize));
			if (r == -1) {
				Py_DECREF(seq);
				PyMem_Free(*array); *array = NULL;
				return -1;
			}
		}
		return SHOULD_FREE;
	}
	
}


PyObject* 
PyObjC_CArrayToPython(
	const char* elementType,
	void* array,
	Py_ssize_t size)
{
	PyObject* result;
	Py_ssize_t i;
	Py_ssize_t eltsize;

	eltsize = PyObjCRT_SizeOfType(elementType);
	if (eltsize == -1) {
		return NULL;
	}

	if (eltsize == 1 || eltsize == 0) {
		/* Special case for buffer-like objects */
		return PyString_FromStringAndSize(array, size);
	}

	result = PyTuple_New(size);
	if (result == NULL) {
		return NULL;
	}


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

int
PyObjC_IsPythonKeyword(const char* word)
{
	/*
	 * We cheat a little: this list only contains those keywords that
	 * are actually used in Cocoa.
	 *
	 * XXX: If we ever add the complete list here we should optimize
	 * this function.
	 */
	static const char* keywords[] = {
		"class",
		"raise",
		NULL
	};
	const char** cur;

	for (cur = keywords; *cur != NULL; cur++) {
		if (strcmp(word, *cur) == 0) {
			return 1;
		}
	}
	return 0;
}

int
PyObjCRT_SimplifySignature(char* signature, char* buf, size_t buflen)
{
	char* cur;
	char* end;
	char* next;

	cur = signature;
	*buf = '\0';

	while (*cur != '\0') {
		next = end = (char*)PyObjCRT_SkipTypeSpec(cur);
		end -= 1;
		while (end != cur && isdigit(*end)) {
			end --;
		}
		end++;

		if ((size_t)(end - cur) > buflen) {
			return -1;
		}

		memcpy(buf, cur, end-cur);
		buflen -= (end-cur);
		buf += (end-cur);
		*buf = '\0';
		cur = next;
	}
	return 0;
}

int
PyObjCObject_Convert(PyObject* object, void* pvar)
{
	int r;
	r = depythonify_c_value(@encode(id), object, (id*)pvar);
	if (r == -1) {
		return 0;
	} else {
		return 1;
	}
}

int 
PyObjC_ConvertBOOL(PyObject* object, void* pvar)
{
    BOOL* pbool = (BOOL*)pvar;

    if (PyObject_IsTrue(object)) {
        *pbool = YES;
    } else {
        *pbool = NO;
    }

    return 1;
}

int 
PyObjC_ConvertChar(PyObject* object, void* pvar)
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

int 
PyObjCSelector_Convert(PyObject* object, void* pvar)
{ 
    int r;

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

    r = depythonify_c_value(@encode(SEL), object, pvar);
    if (r == -1) {
           return 0;
    }   
    return 1;
}

int 
PyObjCClass_Convert(PyObject* object, void* pvar)
{
    if (!PyObjCClass_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expected objective-C class");
        return 0;
    }

    *(Class*)pvar = PyObjCClass_GetClass(object);
    if (*(Class*)pvar == NULL) return 0;
    return 1;
}


PyObject* 
PyObjC_CArrayToPython2(
	const char* elementType,
	void* array,
	Py_ssize_t size,
	bool alreadyRetained,
	bool alreadyCFRetained)
{
	PyObject* result;
	Py_ssize_t i;
	Py_ssize_t eltsize;

	eltsize = PyObjCRT_SizeOfType(elementType);
	if (eltsize == -1) {
		return NULL;
	}

	if (eltsize == 1 || eltsize == 0) {
		/* Special case for buffer-like objects */
		return PyString_FromStringAndSize(array, size);
	}

	result = PyTuple_New(size);
	if (result == NULL) {
		return NULL;
	}


	for (i = 0; i < size; i++) {
		PyObject* elt = pythonify_c_value(elementType, array);
		if (elt == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		if (alreadyRetained) {
			[*(id*)array release];
		} else if (alreadyCFRetained) {
			CFRelease(*(id*)array);
		}

		PyTuple_SET_ITEM(result, i, elt);
		array = ((char*)array) + eltsize;
	}

	return result;
}
