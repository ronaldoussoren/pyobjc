/*
 * Special wrappers for pointer values
 *
 * Pointer arguments to methods can be split into 3 classes:
 * - Pass-by-reference arguments (in, out, inout). 
 *   This is supported by using the modifiers _C_IN, _C_OUT and _C_INOUT
 * - Pointers to buffers
 *   This requires special support, you can't detect the size of the buffer
 *   from the signature
 * - Opaque values
 *   Types like FSRef are for all intents and purposes opaque values,
 *   that happen to be represented using pointers (to structs). The functions
 *   in this file allow extension modules to register functions to convert these
 *   values to and from their Python representation.
 *
 * NOTE:
 * - The pythonify and depythonify functions have the same interface as
 *   the *_New and *_Convert functions in MacPython (pymactoolbox.h), this
 *   makes it easier to interface with that packages.
 */
#include "pyobjc.h"


#import <CoreFoundation/CoreFoundation.h>

struct wrapper {
	const char* signature;
	int offset;
	PyObject* (*pythonify)(void*);
	int (*depythonify)(PyObject*, void*);
};

/* Using an array is pretty lame, this needs to be replaced by a more
 * efficient datastructure. However: As long as their is only a limited
 * number of custom wrappers this should not be a problem.
 */
static struct wrapper* items = 0;
static Py_ssize_t item_count = 0;

/*
 * If signature is a pointer to a structure return the index of the character
 * just beyond the end of the struct name. This information is needed because
 * @encode(struct foo*) can return two different strings:
 * 1) ^{foo} if the compiler has not yet seen a full definition of struct foo
 * 2) ^{foo=...} if the compiler has not yet seen a full definition of 
 *    the struct
 * We want to treat those two pointer as the same type, therefore we need to
 * ignore everything beyond the end of the struct name.
 */
static int find_end_of_structname(const char* signature) {
	if (signature[1] == _C_CONST && signature[2] == _C_STRUCT_B) {
		char* end1;
		char* end2;

		end1 = strchr(signature, _C_STRUCT_E);
		end2 = strchr(signature, '=');

		if (end2 == NULL) {
			return end1 - signature;
		} else {
			return end2 - signature;
		}

	} else if (signature[1] == _C_STRUCT_B) {
		char* end1;
		char* end2;

		end1 = strchr(signature, _C_STRUCT_E);
		end2 = strchr(signature, '=');

		if (end2 == NULL) {
			return end1 - signature;
		} else {
			return end2 - signature;
		}
	}
	return strlen(signature);
}

static struct wrapper*
FindWrapper(const char* signature)
{
	Py_ssize_t i;

	for (i = 0; i < item_count; i++) {
		if (strncmp(signature, items[i].signature, items[i].offset) == 0) {
			/* See comment just above find_end_of_structname */
			if (signature[1] == _C_CONST && signature[2] == _C_STRUCT_B) {
				char ch = signature[items[i].offset];
				if (ch == '=' || ch == _C_STRUCT_E) {
					return items + i;
				}

			} else if (signature[1] == _C_STRUCT_B) {
				char ch = signature[items[i].offset];
				if (ch == '=' || ch == _C_STRUCT_E) {
					return items + i;
				}

			} else {
				if (signature[items[i].offset] == '\0') {
					return items + i;
				}
			}
		}
	}
	return NULL;
}

static PyObject*
ID_to_py(void* idValue)
{
	return pythonify_c_value(@encode(id), &idValue);
}

static int
py_to_ID(PyObject* obj, void* output)
{
	return depythonify_c_value(@encode(id), obj, output);
}

int PyObjCPointerWrapper_RegisterID(const char *signature) {
	return PyObjCPointerWrapper_Register(signature, 
		(PyObjCPointerWrapper_ToPythonFunc)&ID_to_py, 
		(PyObjCPointerWrapper_FromPythonFunc)&py_to_ID);
}

int 
PyObjCPointerWrapper_Register(
	const char* signature,
	PyObjCPointerWrapper_ToPythonFunc pythonify,
	PyObjCPointerWrapper_FromPythonFunc depythonify

	) 
{
	struct wrapper* value;

	/*
	 * Check if we already have a wrapper, if so replace that.
	 * This makes it possible to replace a default wrapper by something
	 * better.
	 */
	if (signature == NULL) {
		return -1;
	}
	value = FindWrapper(signature);
	if (value != NULL) {
		value->pythonify = pythonify;
		value->depythonify = depythonify;
		return 0;
	}

	if (items == NULL) {
		items = PyMem_Malloc(sizeof(struct wrapper));
		if (items == NULL) {
			PyErr_NoMemory();
			return -1;
		}
		item_count = 1;
	} else {
		struct wrapper* tmp;

		tmp = PyMem_Realloc(
			items, sizeof(struct wrapper) *  (item_count+1));
		if (tmp == NULL) {
			PyErr_NoMemory();
			return -1;
		}
		items = tmp;
		item_count ++;
	}

	value = items + (item_count-1);

	value->signature = PyObjCUtil_Strdup(signature);
	if (value->signature == NULL) {
		PyErr_NoMemory();
		item_count --;
		return -1;
	}

	value->offset = find_end_of_structname(value->signature);

	value->pythonify = pythonify;
	value->depythonify = depythonify;

	return 0;
}



PyObject* 
PyObjCPointerWrapper_ToPython(const char* type, void* datum)
{
	struct wrapper* item;
	PyObject* result;

	item = FindWrapper(type);
	if (item == NULL) {
		return NULL;
	}

	if (item->pythonify == ID_to_py) {
		result = PyObjC_FindPythonProxy(*(id*)datum);
		if (result != NULL) {
			return result;

		} else if (*(void**)datum == kCFAllocatorUseContext) {
			/* kCFAllocatorUseContext is a bit too magic for its
			 * own good. 
			 *
			 * Note that this is a crude hack, but as long as this
			 * is the only such object I don't think its worthwhile
			 * to add generic support for this.
			 */
			result = PyObjCCF_NewSpecial2(
				CFAllocatorGetTypeID(), *(void**)datum);

			PyObjC_RegisterPythonProxy(*(id*)datum, result);
			return result;
		} 
	}

	result = item->pythonify(*(void**)datum);
	return result;
}


int 
PyObjCPointerWrapper_FromPython(
	const char* type, PyObject* value, void* datum)
{
	struct wrapper* item;
	int r;

	if (value == PyObjC_NULL) {
		*(void**)datum = NULL;
		return 0;
	}

	item = FindWrapper(type);
	if (item == NULL) {
		return -1;
	}

	r = item->depythonify(value, datum);
	if (r == 0) {
		return 0;
	} else {
		return -1;
	}
}

int PyObjCPointerWrapper_HaveWrapper(const char* type)
{
	return (FindWrapper(type) != NULL);
}


static PyObject*
PyObjectPtr_New(void *obj)
{
	return (PyObject*)obj;
}

static int
PyObjectPtr_Convert(PyObject* obj, void* pObj)
{
	*(void**)pObj = (void *)obj;
	return 0;
}

static PyObject*
class_new(void *obj)
{
	return pythonify_c_value("#", obj);
}

static int
class_convert(PyObject* obj, void* pObj)
{
	return depythonify_c_value("#", obj, pObj);
}


#if PY_MAJOR_VERSION == 2

static int dontClose(FILE* fp __attribute__((__unused__)))
{
	return 0;
}
static PyObject*
FILE_New(void *obj)
{
	FILE* fp = (FILE*)obj;
	char* mode = "r";

#if defined(__SRW) 
	/* This is a hack, but allows us to pass the right file mode into
	 * Python.
	 */
	if (fp->_flags & __SWR) {
		mode = "w";
	} else if (fp->_flags & __SRW) {
		mode = "w+";
	}

#endif
	return PyFile_FromFile(fp, "<objc-file>", mode, dontClose);
}

static int
FILE_Convert(PyObject* obj, void* pObj)
{
	*(FILE**)pObj = PyFile_AsFile(obj);
	if (*(FILE**)pObj == NULL) {
		return 1;
	}

	return 0;
}

#endif

/*
 * Generic CF type support 
 */
static PyObject*
CF_to_py(void* cfValue)
{
	return PyObjC_IDToCFType((id)cfValue);
}

static int
py_to_CF(PyObject* obj, void* output)
{
	id tmp = PyObjC_CFTypeToID(obj);
	if (tmp == NULL && PyErr_Occurred()) {
		return -1;
	}
	*(void**)output = tmp;
	return 0;
}

int PyObjCPointerWrapper_RegisterCF(const char *signature) {
	return PyObjCPointerWrapper_Register(signature, 
		(PyObjCPointerWrapper_ToPythonFunc)&CF_to_py, 
		(PyObjCPointerWrapper_FromPythonFunc)&py_to_CF);
}


int 
PyObjCPointerWrapper_Init(void)
{
	int r = 0;

	r = PyObjCPointerWrapper_RegisterCF(@encode(CFURLRef)); 
	if (r == -1) return -1;

	r = PyObjCPointerWrapper_RegisterCF(@encode(CFSetRef)); 
	if (r == -1) return -1;

#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_2
	r = PyObjCPointerWrapper_RegisterCF(@encode(CFNetServiceRef)); 
	if (r == -1) return -1;
#endif

	r = PyObjCPointerWrapper_RegisterCF(@encode(CFReadStreamRef)); 
	if (r == -1) return -1;

	r = PyObjCPointerWrapper_RegisterCF(@encode(CFRunLoopRef)); 
	if (r == -1) return -1;

	r = PyObjCPointerWrapper_Register(@encode(PyObject*),
		PyObjectPtr_New, PyObjectPtr_Convert);
	if (r == -1) return -1;

	r = PyObjCPointerWrapper_Register("^{objc_class=}",
		class_new, class_convert);
	if (r == -1) return -1;


#if PY_MAJOR_VERSION == 2
	r = PyObjCPointerWrapper_Register(@encode(FILE*),
		FILE_New, FILE_Convert);
	if (r == -1) return -1;
#endif

	return 0;
}
