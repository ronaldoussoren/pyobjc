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

struct registry
{
	ObjC_CallFunc_t call_to_objc;
	IMP		call_to_python;
};
	
/* Dict mapping from signature-string to a 'struct registry' */
static PyObject* signature_registry = NULL;

/* List of 3-tuples: (Class, "selector", 'struct registry' */
static PyObject* special_registry  = NULL;

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

int PyObjC_RegisterMethodMapping(Class class, SEL sel, 
	ObjC_CallFunc_t call_to_objc,
	IMP		    call_to_python)
{
	struct registry* v;
	const char*      selname = PyObjCRT_SELName(sel);
	PyObject*        pyclass;
	PyObject* 	 entry;

	if (signature_registry == NULL) {
		if (init_registry() < 0) return -1;
	}

	if (!call_to_python) {
		PyErr_SetString(ObjCExc_error, 
			"PyObjC_RegisterMethodMapping: all functions required");
		return -1;
	}

	if (!call_to_objc) {
		call_to_objc = ObjC_FFICaller;
	}

	pyclass = PyObjCClass_New(class);
	if (pyclass == NULL) return -1;

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
	PyTuple_SET_ITEM(entry, 1, PyString_InternFromString(selname));
	PyTuple_SET_ITEM(entry, 2, PyCObject_FromVoidPtr(v, (PyMem_Free)));

	if (PyErr_Occurred()) {
		Py_DECREF(entry);
		return -1;
	}

	if (PyList_Append(special_registry, entry) < 0) {
		Py_DECREF(entry);
		return -1;
	}

	return 0;
}

void
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
			// XXX: should signal an error
			abort();
			return;
		}

		memcpy(buf, cur, end-cur);
		buflen -= (end-cur);
		buf += (end-cur);
		*buf = '\0';
		cur = next;
	}
}


	
int PyObjC_RegisterSignatureMapping(
	char*           signature,
	ObjC_CallFunc_t call_to_objc,
	IMP		call_to_python)
{
	struct registry* v;
	PyObject* 	 entry;
	char             signature_buf[1024];

	if (special_registry == NULL) {
		if (init_registry() < 0) return -1;
	}
		

	PyObjCRT_SimplifySignature(signature, signature_buf, sizeof(signature_buf));
	if (PyErr_Occurred()) return -1;

	if (!call_to_objc || !call_to_python) {
		PyErr_SetString(ObjCExc_error, 
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

	entry = PyCObject_FromVoidPtr(v, (PyMem_Free));
	if (entry == NULL) {
		PyMem_Free(v);
		return -1;
	}

	if (PyDict_SetItemString(signature_registry, signature_buf, entry) < 0){
		Py_DECREF(entry);
		return -1;
	}
	Py_DECREF(entry); 

	return 0;
}


static struct registry*
search_special(Class class __attribute__((__unused__)), SEL sel)
{
	PyObject* 	 result = NULL;
	PyObject*        special_class = NULL;
	int              special_len, i;

	if (special_registry == NULL) {
		ObjCErr_Set(ObjCExc_error,
			"PyObjC: don't know how to call method %s", 
			PyObjCRT_SELName(sel));
		return NULL;
	}

	special_len = PyList_Size(special_registry);

	for (i = 0; i < special_len; i++) {
		PyObject* entry = PyList_GetItem(special_registry, i);
		PyObject* pyclass = PyTuple_GetItem(entry, 0);
		PyObject* pysel = PyTuple_GetItem(entry, 1);

		if (pyclass == NULL || pysel == NULL) continue;
		
		if (strcmp(PyString_AsString(pysel), PyObjCRT_SELName(sel)) == 0) {
			if (!special_class) {
				special_class = pyclass;
				result = PyTuple_GetItem(entry, 2);
			} else if (PyType_IsSubtype((PyTypeObject*)pyclass, 
					(PyTypeObject*)special_class)) {
				special_class = pyclass;
				result = PyTuple_GetItem(entry, 2);
			}
		}
	}

	if (result) {
		return PyCObject_AsVoidPtr(result);
	} else {
		ObjCErr_Set(ObjCExc_error,
			"PyObjC: don't know how to call method %s", 
			PyObjCRT_SELName(sel));
		return NULL;
	}
}


ObjC_CallFunc_t ObjC_FindCallFunc(Class class, SEL sel)
{
/*
 * TODO: Should add special case code for NSUndoManager: If this
 * is a selector that is forwarded to the 'target' we should get
 * the caller for the target instead of for this object!
 */
	struct registry* special;

	if (special_registry == NULL) return ObjC_FFICaller;

	special = search_special(class, sel);
	if (special) {
		return special->call_to_objc;
	} else {
		PyErr_Clear();
	}

	return ObjC_FFICaller;
}

static struct registry*
find_signature(char* signature)
{
	PyObject* o;
	struct registry* r;
	char   signature_buf[1024];

	PyObjCRT_SimplifySignature(signature, signature_buf, sizeof(signature_buf));
	if (signature_registry == NULL) {
		ObjCErr_Set(ObjCExc_error,
			"PyObjC: don't know how to call a method with "
			"signature %s", signature);
		return NULL;
	}

	o = PyDict_GetItemString(signature_registry, signature_buf);
	if (o == NULL) {
		ObjCErr_Set(ObjCExc_error,
			"PyObjC: don't know how to call a method with "
			"signature %s", signature);
		return NULL;
	}

	r = PyCObject_AsVoidPtr(o);
	return r;
}

static struct registry* create_ffi(char* signature)
{
	IMP ffiImp = NULL;
	int r;

	PyErr_Clear();

	ffiImp = ObjC_MakeIMPForSignature(signature, NULL);
	if (ffiImp == NULL) 
		goto error;

	r = PyObjC_RegisterSignatureMapping(signature, ObjC_FFICaller, ffiImp);
	if (r == -1) {
		goto error;
	}

	return find_signature(signature);
error:
	/* TODO: Clean up ffiImp */
	return NULL;
}


IMP ObjC_FindIMPForSignature(char* signature)
{
	struct registry* r;

	r = find_signature(signature);
	if (r) {
		return r->call_to_python;
	}

	r = create_ffi(signature);
	if (r) {
		return r->call_to_python;
	}

	return NULL;
}

IMP ObjC_FindIMP(Class class, SEL sel)
{
	struct registry* generic;
	struct registry* special;
	PyObject*        objc_class;
	PyObject*        objc_sel;

	/* Search using the python wrapper of the class: That one may have
	 * a more specific method signature.
	 */

	objc_class = PyObjCClass_New(class);
	if (objc_class == NULL) return NULL;
	
	objc_sel = PyObjCClass_FindSelector(objc_class, sel);
	if (objc_sel == NULL) return NULL;

	special = search_special(class, sel);
	if (special) {
		return special->call_to_python;
	} else {
		PyErr_Clear();
	}

	generic = find_signature(PyObjCSelector_Signature(objc_sel));
	if (generic) {
		return generic->call_to_python;
	}

	generic = create_ffi(PyObjCSelector_Signature(objc_sel));
	if (generic) {
		return generic->call_to_python;
	}

	return NULL;
}
