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


#ifdef MACOSX
#include <pymactoolbox.h>
#import <CoreFoundation/CoreFoundation.h>
#endif

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
static int item_count = 0;

int 
PyObjCPointerWrapper_Register(
	const char* signature,
	PyObjCPointerWrapper_ToPythonFunc pythonify,
	PyObjCPointerWrapper_FromPythonFunc depythonify

	) 
{
	struct wrapper* value;

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

	value->signature = signature;
	if (signature[1] == _C_STRUCT_B) {
		int o1, o2;

		o1 = strchr(signature, _C_STRUCT_E) - signature;
		o2 = strchr(signature, '=') - signature;

		if (o1 < o2) {
			value->offset = o1;
		} else {
			value->offset = o2;
		}
	} else {
		value->offset = strlen(signature);
	}

	value->pythonify = pythonify;
	value->depythonify = depythonify;

	return 0;
}

static struct wrapper*
FindWrapper(const char* signature)
{
	int i;
	int len;

	len = strlen(signature);

	for (i = 0; i < item_count; i++) {
		if (strncmp(signature, items[i].signature, items[i].offset) == 0) {
			if (signature[1] != _C_STRUCT_B || signature[items[i].offset] == '=' || signature[items[i].offset] == _C_STRUCT_E) {
				return items + i;
			}
		}
	}
	return NULL;
}


PyObject* 
PyObjCPointerWrapper_ToPython(const char* type, void* datum)
{
	struct wrapper* item;

	item = FindWrapper(type);
	if (item == NULL) {
		return NULL;
	}

	return item->pythonify(*(void**)datum);
}


int 
PyObjCPointerWrapper_FromPython(
	const char* type, PyObject* value, void* datum)
{
	struct wrapper* item;
	int r;

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

#ifdef MACOSX
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


#endif



int 
PyObjCPointerWrapper_Init(void)
{
	int r = 0;

#ifdef MACOSX
	r = PyObjCPointerWrapper_Register(@encode(CFURLRef), 
		(PyObjCPointerWrapper_ToPythonFunc)CF_to_py, 
		(PyObjCPointerWrapper_FromPythonFunc)py_to_CF);
	if (r == -1) return -1;

	r = PyObjCPointerWrapper_Register(@encode(CFSetRef), 
		(PyObjCPointerWrapper_ToPythonFunc)CF_to_py, 
		(PyObjCPointerWrapper_FromPythonFunc)py_to_CF);
	if (r == -1) return -1;

#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_2
	r = PyObjCPointerWrapper_Register(@encode(CFNetServiceRef), 
		(PyObjCPointerWrapper_ToPythonFunc)CF_to_py, 
		(PyObjCPointerWrapper_FromPythonFunc)py_to_CF);
	if (r == -1) return -1;
#endif

	r = PyObjCPointerWrapper_Register(@encode(CFReadStreamRef), 
		(PyObjCPointerWrapper_ToPythonFunc)CF_to_py, 
		(PyObjCPointerWrapper_FromPythonFunc)py_to_CF);
	if (r == -1) return -1;

	r = PyObjCPointerWrapper_Register(@encode(CFRunLoopRef), 
		(PyObjCPointerWrapper_ToPythonFunc)CF_to_py, 
		(PyObjCPointerWrapper_FromPythonFunc)py_to_CF);
	if (r == -1) return -1;

#endif

	r = PyObjCPointerWrapper_Register(@encode(PyObject*),
		PyObjectPtr_New, PyObjectPtr_Convert);
	if (r == -1) return -1;

	return 0;
}
