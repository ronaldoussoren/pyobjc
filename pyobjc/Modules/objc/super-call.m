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
#include <Python.h>
#include "pyobjc.h"
#include "objc_support.h"
#include "super-call.h"

struct registry
{
	ObjC_CallFunc_t call_to_self;
	ObjC_CallFunc_t call_to_super;
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

int ObjC_RegisterMethodMapping(Class class, SEL sel, 
	ObjC_CallFunc_t call_to_self,  
	ObjC_CallFunc_t call_to_super,
	IMP		    call_to_python)
{
	struct registry* v;
	const char*      selname = SELNAME(sel);
	PyObject*        pyclass;
	PyObject* 	 entry;

	if (signature_registry == NULL) {
		if (init_registry() < 0) return -1;
	}

	if (!call_to_self || !call_to_super || !call_to_python) {
		PyErr_SetString(ObjCExc_error, 
			"ObjC_RegisterMethodMapping: all functions required");
		return NULL;
	}

	pyclass = ObjCClass_New(class);
	if (pyclass == NULL) return -1;

	v = PyMem_Malloc(sizeof(*v));
	if (v == NULL) {
		PyErr_NoMemory();
		return -1;
	}
	v->call_to_self   = call_to_self;
	v->call_to_super  = call_to_super;
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

/*
 * This function removes junk numbers from 'signature' and copies it into
 * 'buf'.
 *
 * Ronald: I'd like to replace this by a function that doesn't use 
 * NSMethodSignature. I think objc_support contains enough intelligence to
 * do this. objc_support doesn't work correctly with (structs containing) 
 * bitfields, but neither does NSMethodSignature.
 */
static void
simplify_signature(char* signature, char* buf, size_t buflen)
{
	int                i, argcount;
	NSMethodSignature* sig;

	sig = [NSMethodSignature signatureWithObjCTypes:signature];
	snprintf(buf, buflen, "%s", [sig methodReturnType]);
	buflen -= strlen(buf);
	buf += strlen(buf);

	argcount = [sig numberOfArguments];
	for (i = 0; i < argcount; i++) {
		snprintf(buf, buflen, "%s", 
			[sig getArgumentTypeAtIndex:i]);
		buflen -= strlen(buf);
		buf += strlen(buf);
	}

	/* Ronald: In theory the release below is not necessary, but 
	 * (1) it doesn't cause runtime errors later on and (2) seems to
	 * solve a memory leak
	 */
	[sig release]; 
}


	
int ObjC_RegisterSignatureMapping(
	char*           signature,
	ObjC_CallFunc_t call_to_super,
	IMP		call_to_python)
{
	struct registry* v;
	PyObject* 	 entry;
	char             signature_buf[1024];

	if (special_registry == NULL) {
		if (init_registry() < 0) return -1;
	}
		

	simplify_signature(signature, signature_buf, sizeof(signature_buf));
	if (PyErr_Occurred()) return -1;

	if (!call_to_super || !call_to_python) {
		PyErr_SetString(ObjCExc_error, 
		   "ObjC_RegisterSignatureMapping: all functions required");
		return NULL;
	}

	v = PyMem_Malloc(sizeof(*v));
	if (v == NULL) {
		PyErr_NoMemory();
		return -1;
	}
	v->call_to_self   = NULL;
	v->call_to_super  = call_to_super;
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
search_special(Class class, SEL sel)
{
	PyObject* 	 result = NULL;
	PyObject*        special_class = NULL;
	int              special_len, i;

	if (special_registry == NULL) {
		ObjCErr_Set(ObjCExc_error,
			"No super-caller for %s\n", SELNAME(sel));
		return NULL;
	}

	special_len = PyList_Size(special_registry);

	for (i = 0; i < special_len; i++) {
		PyObject* entry = PyList_GetItem(special_registry, i);
		PyObject* pyclass = PyTuple_GetItem(entry, 0);
		PyObject* pysel = PyTuple_GetItem(entry, 1);

		if (pyclass == NULL || pysel == NULL) continue;
		
		if (strcmp(PyString_AsString(pysel), SELNAME(sel)) == 0) {
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
			"No super-caller for %s\n", SELNAME(sel));
		return NULL;
	}
}


ObjC_CallFunc_t ObjC_FindSelfCaller(Class class, SEL sel)
{
	ObjC_CallFunc_t result;
	struct registry* rec;

#if 0 /* def OC_WITH_LIBFFI */
	result = ObjC_FFICaller;
#else
	result = execute_and_pythonify_objc_method;
#endif
	if (special_registry == NULL) return result;

	/* Check the list of exceptions */
	rec = search_special(class, sel);
	if (rec) {
		result = rec->call_to_self;
	}

	return result;
}

static struct registry*
find_signature(char* signature)
{
	PyObject* o;
	struct registry* r;
	char   signature_buf[1024];

	simplify_signature(signature, signature_buf, sizeof(signature_buf));

	if (signature_registry == NULL) {
		ObjCErr_Set(ObjCExc_error,
			"No forwarder for signature %s\n", signature);
		return NULL;
	}

	o = PyDict_GetItemString(signature_registry, signature_buf);
	if (o == NULL) {
		ObjCErr_Set(ObjCExc_error,
			"No forwarder for signature %s\n", signature);
		return NULL;
	}

	r = PyCObject_AsVoidPtr(o);
	return r;
}

#ifdef OC_WITH_LIBFFI
static struct registry* create_ffi(char* signature)
{
	IMP ffiImp = NULL;
	int r;

	PyErr_Clear();

	ffiImp = ObjC_MakeIMPForSignature(signature);
	if (ffiImp == NULL) 
		goto error;

	r = ObjC_RegisterSignatureMapping(signature, ObjC_FFICaller, ffiImp);
	if (r == -1) {
		PyErr_Print();
		goto error;
	}

	return find_signature(signature);
error:
	/* TODO: Clean up ffiImp */
	return NULL;
}

#endif /* OC_WITH_LIBFFI */


IMP ObjC_FindIMPForSignature(char* signature)
{
	struct registry* r;

	r = find_signature(signature);
	if (r) {
		return r->call_to_python;
	}

#ifdef OC_WITH_LIBFFI

	r = create_ffi(signature);
	if (r) {
		return r->call_to_python;
	}

#endif /* OC_WITH_LIBFFI */

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

	objc_class = ObjCClass_New(class);
	if (objc_class == NULL) return NULL;
	
	objc_sel = ObjCClass_FindSelector(objc_class, sel);
	if (objc_sel == NULL) return NULL;

	
	special = search_special(class, sel);
	if (special) {
		return special->call_to_python;
	} else {
		PyErr_Clear();
	}

	generic = find_signature(ObjCSelector_Signature(objc_sel));
	if (generic) {
		return generic->call_to_python;
	}

#ifdef OC_WITH_LIBFFI

	generic = create_ffi(ObjCSelector_Signature(objc_sel));
	if (generic) {
		return generic->call_to_python;
	}

#endif /* OC_WITH_LIBFFI */

	return NULL;
}


ObjC_CallFunc_t ObjC_FindSupercaller(Class class, SEL sel)
{
	struct registry* generic;
	struct registry* special;
	METHOD           m;

#ifndef OC_WITH_LIBFFI
	m = class_getInstanceMethod(class, sel);
	if (!m) {
		ObjCErr_Set(ObjCExc_error,
			"Class %s does not respond to %s",
			class->name, SELNAME(sel));
		return NULL;
	}
#endif

	special = search_special(class, sel);
	if (special) {
		return special->call_to_super;
	} else {
		PyErr_Clear();
	}

#ifndef OC_WITH_LIBFFI 
	generic = find_signature(m->method_types);
	if (generic) {
		return generic->call_to_super;
	}
#endif

#ifdef OC_WITH_LIBFFI 
	return ObjC_FFICaller;

#if 0
	generic = create_ffi(m->method_types);
	if (generic) {
		return generic->call_to_super;
	}
#endif

#endif /* OC_WITH_LIBFFI */

	return NULL;
}

void ObjC_FindCaller(Class class, SEL sel, ObjC_CallFunc_t* call_self, ObjC_CallFunc_t* call_super)
{
	/* TODO: Inline these */
	*call_self = ObjC_FindSelfCaller(class, sel);
	*call_super = ObjC_FindSupercaller(class, sel);
}
