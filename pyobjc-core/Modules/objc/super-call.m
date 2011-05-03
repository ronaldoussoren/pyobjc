/*
 * super-call.m -- Finding the right dispatch function for a method-call
 *
 * This file defines a registry that is used to find the right function to
 * call when a method is called. There are 3 variants:
 * - Call the method from python
 * - Call the superclass implementation from python
 * - Call the python implementation of a method from Objective-C
 *
 * The first will almost always be 'execute_and_pythonify_method', the other
 * two classes contain lots of functions because the normal runtime doesn't
 * allow for dynamicly creating these types of calls (see also: register.m)
 */
#include "pyobjc.h"

Py_ssize_t PyObjC_MappingCount = 0;

struct registry
{
	PyObjC_CallFunc 	call_to_objc;
	PyObjCFFI_ClosureFunc	call_to_python;
};
	
/* Dict mapping from signature-string to a 'struct registry' */
static PyObject* signature_registry = NULL;

/* List of 3-tuples: (Class, "selector", 'struct registry' */
static PyObject* special_registry  = NULL;

/*
 * Initialize the data structures
 */
static int
init_registry(void)
{
	if (signature_registry == NULL) {
		signature_registry = PyDict_New();
		if (signature_registry == NULL) return -1;
	}

	if (special_registry == NULL) {
		special_registry = PyList_New(0);
		if (special_registry == NULL) return -1;
	}

	return 0;
}

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 7

static void memblock_capsule_cleanup(void* ptr)
{
	PyMem_Free(ptr);
}
#else
static void memblock_capsule_cleanup(PyObject* ptr)
{
	PyMem_Free(PyCapsule_GetPointer(ptr, "objc.__memblock__"));
}
#endif


/*
 * Add a custom mapping for a method in a class
 */
int 
PyObjC_RegisterMethodMapping(Class class, SEL sel, 
	PyObjC_CallFunc call_to_objc,
	PyObjCFFI_ClosureFunc call_to_python)
{
	struct registry* v;
	const char* selname = sel_getName(sel);
	PyObject* pyclass;
	PyObject* entry;

	if (signature_registry == NULL) {
		if (init_registry() < 0) return -1;
	}

	if (!call_to_python) {
		PyErr_SetString(PyObjCExc_Error, 
			"PyObjC_RegisterMethodMapping: all functions required");
		return -1;
	}

	if (!call_to_objc) {
		call_to_objc = PyObjCFFI_Caller;
	}

	if (class == nil) {
		pyclass = Py_None; Py_INCREF(Py_None);
	} else {	
		pyclass = PyObjCClass_New(class);
		if (pyclass == NULL) return -1;
	}

	v = PyMem_Malloc(sizeof(*v));
	if (v == NULL) {
		PyErr_NoMemory();
		return -1;
	}
	v->call_to_objc  = call_to_objc;
	v->call_to_python = call_to_python;

	entry = PyTuple_New(3);
	if (entry == NULL) return -1;

	PyTuple_SET_ITEM(entry, 0, pyclass);
	PyTuple_SET_ITEM(entry, 1, PyBytes_InternFromString((char*)selname));
	PyTuple_SET_ITEM(entry, 2, PyCapsule_New(v, "objc.__memblock__", memblock_capsule_cleanup));

	if (PyErr_Occurred()) {
		Py_DECREF(entry);
		return -1;
	}

	if (PyList_Append(special_registry, entry) < 0) {
		Py_DECREF(entry);
		return -1;
	}

	PyObjC_MappingCount += 1;

	return 0;
}

int PyObjC_RegisterSignatureMapping(
	char* signature,
	PyObjC_CallFunc call_to_objc,
	PyObjCFFI_ClosureFunc call_to_python)
{
	struct registry* v;
	PyObject*  entry;
	char signature_buf[1024];
	int r;

	if (special_registry == NULL) {
		if (init_registry() < 0) return -1;
	}

	r = PyObjCRT_SimplifySignature(
			signature, 
			signature_buf, 
			sizeof(signature_buf));
	if (r == -1) {
		PyErr_SetString(PyObjCExc_Error, "cannot simplify signature");
		return -1;
	}	

	if (!call_to_objc || !call_to_python) {
		PyErr_SetString(PyObjCExc_Error, 
		   "PyObjC_RegisterSignatureMapping: all functions required");
		return -1;
	}

	v = PyMem_Malloc(sizeof(*v));
	if (v == NULL) {
		PyErr_NoMemory();
		return -1;
	}
	v->call_to_objc  = call_to_objc;
	v->call_to_python = call_to_python;

	entry = PyCapsule_New(v, "objc.__memblock__", memblock_capsule_cleanup);
	if (entry == NULL) {
		PyMem_Free(v);
		return -1;
	}

	PyObject* key = PyBytes_FromString(signature_buf);
	if (key == NULL) {
		return -1;
	}

	if (PyDict_SetItem(signature_registry, key, entry) < 0){
		Py_DECREF(key);
		Py_DECREF(entry);
		return -1;
	}
	Py_DECREF(key);
	Py_DECREF(entry); 
	PyObjC_MappingCount += 1;

	return 0;
}


static struct registry*
search_special(Class class, SEL sel)
{
	PyObject* result = NULL;
	PyObject* special_class = NULL;
	Py_ssize_t special_len;
	Py_ssize_t i;

	if (special_registry == NULL) goto error;

	if (class) {
		special_class = PyObjCClass_New(class);
		if (special_class == NULL) goto error;

	}

	special_len = PyList_Size(special_registry);

	for (i = 0; i < special_len; i++) {
		PyObject* entry = PyList_GetItem(special_registry, i);
		PyObject* pyclass = PyTuple_GET_ITEM(entry, 0);
		PyObject* pysel = PyTuple_GET_ITEM(entry, 1);

		if (pyclass == NULL || pysel == NULL) continue;
		
		if (
			(PyUnicode_Check(pysel) && PyObjC_is_ascii_string(pysel, sel_getName(sel)))
#if PY_MAJOR_VERSION == 2
		     || (PyString_Check(pysel) && strcmp(PyString_AsString(pysel), sel_getName(sel)) == 0)
#else
		     || (PyBytes_Check(pysel) && strcmp(PyBytes_AsString(pysel), sel_getName(sel)) == 0)
#endif
		     ) {

			if (!special_class) {
				special_class = pyclass;
				Py_INCREF(special_class);
				result = PyTuple_GET_ITEM(entry, 2);

			} else if (pyclass == Py_None) {
				Py_DECREF(special_class);
				special_class = pyclass;
				Py_INCREF(special_class);
				result = PyTuple_GET_ITEM(entry, 2);

			} else if (PyType_IsSubtype(
					(PyTypeObject*)special_class,
					(PyTypeObject*)pyclass
				    )) {
				Py_DECREF(special_class);
				special_class = pyclass;
				Py_INCREF(special_class);
				result = PyTuple_GET_ITEM(entry, 2);
			}
		}
	}
	Py_XDECREF(special_class);
	if (!result) goto error;

	return PyCapsule_GetPointer(result, "objc.__memblock__");

error:
	PyErr_Format(PyObjCExc_Error,
		"PyObjC: don't know how to call method '%s'", 
			sel_getName(sel));
	return NULL;
}


PyObjC_CallFunc 
PyObjC_FindCallFunc(Class class, SEL sel)
{
/*
 * TODO: Should add special case code for NSUndoManager: If this
 * is a selector that is forwarded to the 'target' we should get
 * the caller for the target instead of for this object!
 */
	struct registry* special;

	if (special_registry == NULL) return PyObjCFFI_Caller;

	special = search_special(class, sel);
	if (special) {
		return special->call_to_objc;
	} else {
		PyErr_Clear();
	}

	return PyObjCFFI_Caller;
}

static struct registry*
find_signature(char* signature)
{
	PyObject* o;
	struct registry* r;
	char signature_buf[1024];
	int res;

	res = PyObjCRT_SimplifySignature(
			signature, 
			signature_buf, 
			sizeof(signature_buf));
	if (res == -1) {
		PyErr_SetString(PyObjCExc_Error, "cannot simplify signature");
		return NULL;
	}	

	if (signature_registry == NULL) goto error;

	PyObject* key = PyBytes_FromString(signature_buf);
	if (key == NULL) {
		return NULL;
	}
	o = PyDict_GetItem(signature_registry, key);
	Py_DECREF(key);
	if (o == NULL) goto error;

	r = PyCapsule_GetPointer(o, "objc.__memblock__");
	return r;

error:
	PyErr_Format(PyObjCExc_Error,
		"PyObjC: don't know how to call a method with "
		"signature '%s'", signature);
	return NULL;
}

extern IMP 
PyObjC_MakeIMP(Class class, Class super_class, PyObject* sel, PyObject* imp)
{
	struct registry* generic;
	struct registry* special;
	SEL aSelector = PyObjCSelector_GetSelector(sel);
	PyObjCFFI_ClosureFunc func = NULL;
	IMP retval;
	PyObjCMethodSignature* methinfo;

	if (super_class != nil) {
		special = search_special(super_class, aSelector);
		if (special) {
			func = special->call_to_python;
		} else {
			PyErr_Clear();
		}
	}

	if (func == NULL) {
		generic = find_signature(PyObjCSelector_Signature(sel));
		if (generic != NULL) {
			func = generic->call_to_python;
		} 
	}

	if (func == PyObjCUnsupportedMethod_IMP) {
		PyErr_Format(PyExc_TypeError,
			"Implementing %s in Python is not supported",
			sel_getName(aSelector));
		return NULL;
	}

	if (func != NULL) {
		methinfo = PyObjCMethodSignature_ForSelector(
				class, (PyObjCSelector_GetFlags(sel) & PyObjCSelector_kCLASS_METHOD) != 0,
				PyObjCSelector_GetSelector(sel),
				PyObjCSelector_Signature(sel),
				PyObjCNativeSelector_Check(sel));
		if (methinfo == NULL) {
			return NULL;
		}
		retval = PyObjCFFI_MakeClosure(methinfo, func, imp);
		if (retval != NULL) {
			Py_INCREF(imp);
		}
		Py_DECREF(methinfo);
		return retval;
	} else {
		PyErr_Clear();
		methinfo = PyObjCMethodSignature_ForSelector(
				class, (PyObjCSelector_GetFlags(sel) & PyObjCSelector_kCLASS_METHOD) != 0,
				PyObjCSelector_GetSelector(sel),
				PyObjCSelector_Signature(sel),
				PyObjCNativeSelector_Check(sel));
		if (methinfo == NULL) {
			return NULL;
		}
		retval = PyObjCFFI_MakeIMPForSignature(
				methinfo, PyObjCSelector_GetSelector(sel), imp);
		Py_DECREF(methinfo);
		return retval;
	}
}

void  
PyObjCUnsupportedMethod_IMP(
	ffi_cif* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)), 
	void** args, 
	void* userdata __attribute__((__unused__)))
{
	[NSException raise:NSInvalidArgumentException
		format:@"Implementing %s from Python is not supported for %@",
			*(id*)args[0], sel_getName(*(SEL*)args[1])];
}

PyObject* 
PyObjCUnsupportedMethod_Caller(
	PyObject* meth, 
	PyObject* self, 
	PyObject* args __attribute__((__unused__)))
{
#if PY_MAJOR_VERSION == 2
	PyObject* repr;

	repr = PyObject_Repr(self);
	if (repr == NULL || !PyString_Check(repr)) {
		Py_XDECREF(repr);
		PyErr_Format(PyExc_TypeError,
			"Cannot call '%s' on instances of '%s' from Python",
			sel_getName(PyObjCSelector_GetSelector(meth)),
			Py_TYPE(self)->tp_name);
		return NULL;
	}

	PyErr_Format(PyExc_TypeError,
		"Cannot call '%s' on '%s' from Python",
		sel_getName(PyObjCSelector_GetSelector(meth)),
		PyString_AS_STRING(repr));
	Py_DECREF(repr);
	return NULL;
#else
	PyErr_Format(PyExc_TypeError,
		"Cannot call '%s' on '%R' from Python",
		sel_getName(PyObjCSelector_GetSelector(meth)),
		self);
	return NULL;
#endif

}
