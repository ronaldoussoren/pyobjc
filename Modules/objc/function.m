/*
 * Wrapper for simple global functions. Simple functions are those without
 * arguments that require additional effort.
 */
#include "pyobjc.h"

typedef struct {
	PyObject_HEAD
	ffi_cif*  cif;
	PyObjCMethodSignature* methinfo;
	void*     function;
	PyObject* doc;
	PyObject* name;
	PyObject* module;
} func_object;


static PyMemberDef func_members[] = {
	{
		"__doc__",
		T_OBJECT,
		offsetof(func_object, doc),
		READONLY,
		NULL
	},
	{
		"__name__",
		T_OBJECT,
		offsetof(func_object, name),
		READONLY,
		NULL
	},
	{
		"__module__",
		T_OBJECT,
		offsetof(func_object, module),
		0,
		NULL
	},
	{
		NULL,
		0,
		0,
		0,
		NULL
	}
};

static PyObject* 
func_call(PyObject* s, PyObject* args, PyObject* kwds)
{
	func_object* self = (func_object*)s;
	Py_ssize_t byref_in_count;
	Py_ssize_t byref_out_count;
	Py_ssize_t plain_count;
	Py_ssize_t argbuf_len;
	int r;

	unsigned char* argbuf;
	ffi_type* arglist[64];
	void*     values[64];
	void**	  byref;

	PyObject* retval;	

	if (self->methinfo->nargs >= 63) {
		PyErr_Format(PyObjCExc_Error,
			"wrapping a function with %"PY_FORMAT_SIZE_T"d arguments, at most 64 "
			"are supported", self->methinfo->nargs);
		return NULL;
	}

	if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
		PyErr_SetString(PyExc_TypeError,
			"keyword arguments not supported");
		return NULL;
	}

	argbuf_len = PyObjCRT_SizeOfReturnType(self->methinfo->rettype);
	r = PyObjCFFI_CountArguments(
		self->methinfo, 0,
		&byref_in_count, &byref_out_count, &plain_count,
		&argbuf_len);
	if (r == -1) {
		return NULL;
	}

	if (PyTuple_Size(args) != (plain_count + byref_in_count)) {
		PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
			plain_count + byref_in_count, PyTuple_Size(args));
		return NULL;
	}

	argbuf = PyMem_Malloc(argbuf_len);
	if (argbuf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	byref = PyMem_Malloc(sizeof(void*) * self->methinfo->nargs);
	if (byref == NULL) {
		PyErr_NoMemory();
		PyMem_Free(argbuf);
		return NULL;
	}

	argbuf_len = PyObjCRT_SizeOfReturnType(self->methinfo->rettype);
	r = PyObjCFFI_ParseArguments(
		self->methinfo, 0, args,
		argbuf_len, argbuf, byref, arglist, values);
	if (r == -1) {
		PyMem_Free(argbuf);
		PyMem_Free(byref);
		return NULL;
	}

	PyObjC_DURING
		ffi_call(self->cif, FFI_FN(self->function), argbuf, values);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		PyMem_Free(argbuf);
		PyMem_Free(byref);
		return NULL;
	}

	retval = PyObjCFFI_BuildResult(self->methinfo, 0, argbuf, byref, 
			byref_out_count, NULL, 0);
	PyMem_Free(argbuf);
	PyMem_Free(byref);
	return retval;
}

static void 
func_dealloc(PyObject* s)
{
	func_object* self = (func_object*)s;

	Py_XDECREF(self->doc);
	Py_XDECREF(self->name);
	Py_XDECREF(self->module);
	if (self->cif != NULL) {
		PyObjCFFI_FreeCIF(self->cif);
	}
	if (self->methinfo != NULL) {
		PyObjCMethodSignature_Free(self->methinfo);
	}
	PyObject_Free(s);
}

PyTypeObject PyObjCFunc_Type =
{
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.function",			/* tp_name */
	sizeof (func_object),			/* tp_basicsize */
	0,					/* tp_itemsize */
  
	/* methods */
	func_dealloc,				/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	0,					/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,					/* tp_as_mapping */
	0,					/* tp_hash */
	func_call,				/* tp_call */
	0,					/* tp_str */
	0,					/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
	"Wrapper around a Objective-C function",/* tp_doc */
	0,					/* tp_traverse */
	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	func_members,				/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	0,					/* tp_new */
	0,					/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0,					/* tp_subclasses */
	0,					/* tp_weaklist */
	0					/* tp_del */
};



PyObject* 
PyObjCFunc_New(PyObject* name, void* func, const char* signature, PyObject* doc)
{
	func_object* result;
	

	result = PyObject_NEW(func_object, &PyObjCFunc_Type);
	if (result == NULL) return NULL;
	
	result->methinfo= PyObjCMethodSignature_FromSignature(signature);
	if (result->methinfo == NULL) return NULL;

	result->function = func;

	result->doc = doc;
	Py_XINCREF(doc);

	result->name = name;
	Py_XINCREF(name);

	result->module = NULL;

	result->cif = PyObjCFFI_CIFForSignature(result->methinfo, 0);
	if (result->cif == NULL) {
		Py_DECREF(result);
		return NULL;	
	}

	
	return (PyObject*)result;
}
