/*
 * Generic support for opaque pointer types, such as NSZone*
 */
#include "pyobjc.h"

typedef struct {
	PyObject_HEAD
	void* pointer_value;
} OpaquePointerObject;

static PyMemberDef opaque_members[] = {
	{
		"__pointer__",
		T_LONG,
		offsetof(OpaquePointerObject, pointer_value),
		READONLY,
		"raw value of the pointer"
	},
	{ 0, 0, 0, 0, 0 }
};

static PyObject*
as_cobject(PyObject* self)
{
	if (((OpaquePointerObject*)self)->pointer_value == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}
	return PyCObject_FromVoidPtr(((OpaquePointerObject*)self)->pointer_value, NULL);
}

static PyMethodDef opaque_methods[] = {
	{
		  "__cobject__",
		  (PyCFunction)as_cobject,
		  METH_NOARGS,
		  "get a CObject representing this object"
	},
	{ 0, 0, 0, 0 }
};


static PyObject* 
opaque_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "cobject", NULL };
	PyObject* arg = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "|O", keywords, &arg)) {
		return NULL;
	}

	if (arg == NULL || !PyCObject_Check(arg)) {
		PyErr_Format(PyExc_TypeError, "Cannot create %s objects",
				type->tp_name);
		return NULL;
	} else {
		OpaquePointerObject* result;

		result = PyObject_New(OpaquePointerObject, type);
		if (result == NULL) {
			return NULL;
		}
		result->pointer_value = PyCObject_AsVoidPtr(arg);
		return (PyObject*)result;
	}
}

static void
opaque_dealloc(PyObject* self)
{
	PyObject_Del(self);
}

static void
opaque_from_c(
	ffi_cif* cif __attribute__((__unused__)),
	void* retval,
	void** args,
	void* userdata)
{
	void* pointer_value = *(void**)args[0];
	PyTypeObject* opaque_type = (PyTypeObject*)userdata;
	OpaquePointerObject* result;

	result = PyObject_New(OpaquePointerObject, opaque_type);
	if (result == NULL) {
		*(PyObject**)retval = NULL;
		return;
	}
	result->pointer_value = pointer_value;
	*(PyObject**)retval = (PyObject*)result;
}

static void
opaque_to_c(
	ffi_cif* cif __attribute__((__unused__)),
	void* retval,
	void** args,
	void* userdata)
{
	PyObject* obj = *(PyObject**)args[0];
	void* pObj = *(void**)args[1];
	PyTypeObject* opaque_type = (PyTypeObject*)userdata;

	if (!PyObject_TypeCheck((obj), opaque_type)) {
		*(void**)pObj = (void*)0xDEADBEEF; /* force errors */
		PyErr_Format(PyExc_TypeError, 
			"Need instance of %s, got instance of %s",
			opaque_type->tp_name, obj->ob_type->tp_name);
		*(int*)retval = -1;
		return;
	}

	*(void**)pObj = ((OpaquePointerObject*)obj)->pointer_value;
	*(int*)retval = 0;
}


/*
 * Usage:
 * 	PyDict_SetItemString(moduleDict, "NSZonePointer",
 * 		PyObjCCreateOpaquePointerType(
 * 			"Foundation.NSZonePointer",
 * 			@encode(NSZone*),
 *	 		NSZonePointer_doc));
 */
PyObject*
PyObjCCreateOpaquePointerType(
		const char* name, 
		const char* typestr,
		const char* docstr)
{
static const char convert_cif_signature[] = { _C_INT, _C_PTR, _C_VOID, _C_PTR, _C_VOID, 0 };
static const char new_cif_signature[]     = { _C_PTR, _C_VOID, _C_PTR, _C_VOID, 0 };
static  ffi_cif* convert_cif = NULL;
static  ffi_cif* new_cif = NULL;

	PyHeapTypeObject* newType = NULL;
	PyObjCPointerWrapper_ToPythonFunc from_c = NULL;
	PyObjCPointerWrapper_FromPythonFunc to_c = NULL;
	ffi_closure* cl = NULL;
	ffi_status rv;
	int r;
	PyObject* v = NULL;
	PyObject* w = NULL;

	if (new_cif == NULL) {
		PyObjCMethodSignature* signature;
		signature = PyObjCMethodSignature_FromSignature(new_cif_signature);
		new_cif = PyObjCFFI_CIFForSignature(signature);
		Py_DECREF(signature);
		if (new_cif == NULL) {
			return NULL;
		}
	}

	if (convert_cif == NULL) {
		PyObjCMethodSignature* signature;
		signature = PyObjCMethodSignature_FromSignature(convert_cif_signature); 
		convert_cif = PyObjCFFI_CIFForSignature(signature);
		Py_DECREF(signature);
		if (convert_cif == NULL) {
			return NULL;
		}
	}


	newType = (PyHeapTypeObject*)PyType_Type.tp_alloc(&PyType_Type, 0);
	if (newType == NULL) {
		return NULL;
	}
#if PY_VERSION_HEX < 0x02050000
# define ht_type type
# define ht_name name
#endif
	//memcpy(newType, &opaque_template, sizeof(*newType));
	newType->ht_type.tp_basicsize = sizeof(OpaquePointerObject);
	newType->ht_type.tp_dealloc = opaque_dealloc;
	newType->ht_type.tp_getattro = PyObject_GenericGetAttr;
	newType->ht_type.tp_flags = Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HEAPTYPE;
	newType->ht_type.tp_methods = opaque_methods;
	newType->ht_type.tp_members = opaque_members;
	newType->ht_type.tp_new = opaque_new;

	newType->ht_type.tp_as_number = &newType->as_number;
	newType->ht_type.tp_as_mapping = &newType->as_mapping;
	newType->ht_type.tp_as_sequence = &newType->as_sequence;
	newType->ht_type.tp_as_buffer = &newType->as_buffer;

	/* Force type to be a heap type. Not only is that technically correct, 
	 * it also makes the type mutable (annoyingly enough all heap types 
	 * and only heap types are mutable).
	 */
	newType->ht_type.tp_flags |= Py_TPFLAGS_HEAPTYPE;
	newType->ht_type.tp_flags &= ~Py_TPFLAGS_HAVE_GC;

	newType->ht_name = PyString_FromString(name);
	if (newType->ht_name == NULL) {
		PyMem_Free(newType);
		PyErr_NoMemory();
		return NULL;
	}
	newType->ht_type.tp_name = PyString_AsString(newType->ht_name);

	v = PyDict_New();
	if (v == NULL) {
		goto error_cleanup;
	}

	w = PyString_FromString(typestr);
	if (w ==  NULL) {
		goto error_cleanup;
	}

	if (PyDict_SetItemString(v, "__typestr__", w) != 0) {
		goto error_cleanup;
	}
	Py_DECREF(w); w = NULL;

	newType->ht_type.tp_dict = v; v = NULL;

	if (docstr != NULL) {
		newType->ht_type.tp_doc = PyObjCUtil_Strdup(docstr);
		if (newType->ht_type.tp_doc == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
	}

	cl = PyObjC_malloc_closure();
	if (cl == NULL) {
		goto error_cleanup;
	}

	newType->ht_type.tp_alloc = PyType_GenericAlloc;
	Py_INCREF(newType->ht_type.ob_type);
	PyType_Ready((PyTypeObject*)newType);
	Py_INCREF((PyObject*)newType);
	Py_INCREF((PyObject*)newType);
	Py_INCREF((PyObject*)newType);


	rv = ffi_prep_closure(cl, convert_cif, opaque_to_c, newType);
	if (rv != FFI_OK) {
		PyErr_Format(PyExc_RuntimeError,
			"Cannot create FFI closure: %d", rv);
		goto error_cleanup;
	}
	to_c = (PyObjCPointerWrapper_FromPythonFunc)cl;
	cl = NULL;

	cl = PyObjC_malloc_closure();
	if (cl == NULL) {
		goto error_cleanup;
	}

	rv = ffi_prep_closure(cl, new_cif, opaque_from_c, newType);
	if (rv != FFI_OK) {
		PyErr_Format(PyExc_RuntimeError,
			"Cannot create FFI closure: %d", rv);
		goto error_cleanup;
	}
	from_c = (PyObjCPointerWrapper_ToPythonFunc)cl;
	cl = NULL;

	r = PyObjCPointerWrapper_Register(typestr, from_c, to_c);
	if (r == -1) {
		goto error_cleanup;
	}

	return (PyObject*)newType;

error_cleanup:
	if (newType) {
		if (newType->ht_type.tp_name) PyMem_Free((char*)newType->ht_type.tp_name);
		if (newType->ht_type.tp_doc) PyMem_Free((char*)newType->ht_type.tp_doc);
		Py_XDECREF(newType->ht_type.tp_dict);
		PyMem_Free(newType);
	}
	if (cl) {
		PyObjC_free_closure(cl);
	}
	if (to_c) {
		PyObjC_free_closure((ffi_closure*)to_c);
	}
	if (from_c) {
		PyObjC_free_closure((ffi_closure*)from_c);
	}
	Py_XDECREF(v);
	Py_XDECREF(w);
	return NULL;
}
