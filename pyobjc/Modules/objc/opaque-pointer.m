/*
 * Generic support for opaque pointer types, such as NSZone*
 */
#include "pyobjc.h"

#ifndef FFI_CLOSURES
#    error "Need FFI_CLOSURES!"
#endif

typedef struct {
	PyObject_HEAD
	void* pointer_value;
} OpaquePointerObject;

static PyMemberDef opaque_members[] = {
	{
		"pointer",
		T_LONG,
		offsetof(OpaquePointerObject, pointer_value),
		READONLY,
		"raw value of the pointer"
	},
	{ 0, 0, 0, 0, 0 }
};

static PyObject* 
opaque_new(
	PyTypeObject* type,
	PyObject* args __attribute__((__unused__)),
	PyObject* kwds __attribute__((__unused__)))
{
	PyErr_Format(PyExc_TypeError, "Cannot create %s objects",
			type->tp_name);
	return NULL;
}

static void
opaque_dealloc(PyObject* self)
{
	PyObject_Del(self);
}

static PyTypeObject opaque_template = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"OpaquePointerWrapper",			/* tp_name */
	sizeof(OpaquePointerObject),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	opaque_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	0,					/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	PyObject_GenericGetAttr,		/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
	0,					/* tp_doc */
	0,					/* tp_traverse */
	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	opaque_members,				/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	opaque_new,				/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
	0,                                      /* tp_bases */
	0,                                      /* tp_mro */
	0,                                      /* tp_cache */
	0,                                      /* tp_subclasses */
	0,                                      /* tp_weaklist */
	0                                       /* tp_del */
};

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
static  ffi_cif* convert_cif = NULL;
static  ffi_cif* new_cif = NULL;

	PyTypeObject* newType = NULL;
	PyObjCPointerWrapper_ToPythonFunc from_c = NULL;
	PyObjCPointerWrapper_FromPythonFunc to_c = NULL;
	ffi_closure* cl = NULL;
	ffi_status rv;
	int r;
	PyObject* v = NULL;
	PyObject* w = NULL;

	if (new_cif == NULL) {
		PyObjCMethodSignature* signature;
		signature = PyObjCMethodSignature_FromSignature("^v^v");
		new_cif = PyObjCFFI_CIFForSignature(signature);
		PyObjCMethodSignature_Free(signature);
		if (new_cif == NULL) {
			return NULL;
		}
	}

	if (convert_cif == NULL) {
		PyObjCMethodSignature* signature;
		signature = PyObjCMethodSignature_FromSignature("i^v^v");
		convert_cif = PyObjCFFI_CIFForSignature(signature);
		PyObjCMethodSignature_Free(signature);
		if (convert_cif == NULL) {
			return NULL;
		}
	}


	newType = malloc(sizeof(*newType));
	if (newType == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	memcpy(newType, &opaque_template, sizeof(*newType));

	newType->tp_name = strdup(name);
	if (newType->tp_name == NULL) {
		free(newType);
		PyErr_NoMemory();
		return NULL;
	}

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

	newType->tp_dict = v; v = NULL;

	if (docstr != NULL) {
		newType->tp_doc = strdup(docstr);
		if (newType->tp_doc == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
	}

	cl = malloc(sizeof(*cl));
	if (cl == NULL) {
		PyErr_NoMemory();
		goto error_cleanup;
	}

	PyType_Ready(newType);
	Py_INCREF(newType);
	Py_INCREF(newType);
	Py_INCREF(newType);

	rv = ffi_prep_closure(cl, convert_cif, opaque_to_c, newType);
	if (rv != FFI_OK) {
		PyErr_Format(PyExc_RuntimeError,
			"Cannot create FFI closure: %d", rv);
		goto error_cleanup;
	}
	to_c = (PyObjCPointerWrapper_FromPythonFunc)cl;
	cl = NULL;

	cl = malloc(sizeof(*cl));
	if (cl == NULL) {
		PyErr_NoMemory();
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
		if (newType->tp_name) free((char*)newType->tp_name);
		if (newType->tp_doc) free((char*)newType->tp_doc);
		Py_XDECREF(newType->tp_dict);
		free(newType);
	}
	if (cl) {
		free(cl);
	}
	if (to_c) {
		free(to_c);
	}
	if (from_c) {
		free(from_c);
	}
	Py_XDECREF(v);
	Py_XDECREF(w);
	return NULL;
}
