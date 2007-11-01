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

PyDoc_STRVAR(func_metadata_doc, "Return a dict that describes the metadata for this function.");
static PyObject* func_metadata(PyObject* self)
{
	return PyObjCMethodSignature_AsDict(((func_object*)self)->methinfo);
}

static PyMethodDef func_methods[] = {
	{
		  "__metadata__",
	    	  (PyCFunction)func_metadata,
	          METH_NOARGS,
		  func_metadata_doc
	},
	{ 0, 0, 0, 0 }
};



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
	int allArgsPresent = 0;
	int r;
	int cif_arg_count;
	BOOL variadicAllArgs = NO;

	unsigned char* argbuf = NULL;
	ffi_type* arglist[64];
	void*     values[64];
	void**	  byref = NULL;
	struct byref_attr* byref_attr = NULL;
	ffi_cif cif;
	ffi_cif* volatile cifptr;

	PyObject* retval;	

	if (self->methinfo->suggestion != NULL) {
		PyErr_SetObject(PyExc_TypeError, self->methinfo->suggestion);
		return NULL;
	}


	if (self->methinfo->ob_size >= 63) {
		PyErr_Format(PyObjCExc_Error,
			"wrapping a function with %"PY_FORMAT_SIZE_T"d arguments, at most 64 "
			"are supported", self->methinfo->ob_size);
		return NULL;
	}

	if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
		PyErr_SetString(PyExc_TypeError,
			"keyword arguments not supported");
		return NULL;
	}

	argbuf_len = PyObjCRT_SizeOfReturnType(self->methinfo->rettype.type);
	r = PyObjCFFI_CountArguments(
		self->methinfo, 0,
		&byref_in_count, &byref_out_count, &plain_count,
		&argbuf_len, &variadicAllArgs);
	if (r == -1) {
		return NULL;
	}

	if (variadicAllArgs) {
		if (byref_in_count != 0 || byref_out_count != 0) {
			PyErr_Format(PyExc_TypeError, "Sorry, printf format with by-ref args not supported");
			return NULL;
		}
		if (PyTuple_Size(args) < self->methinfo->ob_size) {
			PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
			self->methinfo->ob_size - 2, PyTuple_Size(args));
			return NULL;
		}
	} else if (PyTuple_Size(args) == self->methinfo->ob_size) {
		allArgsPresent = 1;

	} else if (PyTuple_Size(args) != (plain_count + byref_in_count)) {
		PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
			plain_count + byref_in_count, PyTuple_Size(args));
		return NULL;
	} else {
		if (PyErr_WarnEx(PyExc_DeprecationWarning, 
			"Not all arguments to an Objective-C function are present", 1) < 0) {
			return NULL;
		}
	}


	argbuf = PyMem_Malloc(argbuf_len);
	if (argbuf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	if (variadicAllArgs) {
		if (PyObjCFFI_AllocByRef(self->methinfo->ob_size+PyTuple_Size(args), &byref, &byref_attr) < 0) {
			goto error;
		}
	} else {
		if (PyObjCFFI_AllocByRef(self->methinfo->ob_size, &byref, &byref_attr) < 0) {
			goto error;
		}
	}

	cif_arg_count = PyObjCFFI_ParseArguments(
		self->methinfo, 0, args,
		PyObjCRT_SizeOfReturnType(self->methinfo->rettype.type),
		argbuf, argbuf_len, byref, byref_attr, arglist, values,
		allArgsPresent);
	if (cif_arg_count == -1) {
		goto error;
	}

	if (variadicAllArgs) {
		r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, cif_arg_count,
			signature_to_ffi_return_type(self->methinfo->rettype.type), arglist);
		if (r != FFI_OK) {
			PyErr_Format(PyExc_RuntimeError,
				"Cannot setup FFI CIF [%d]", r);
				goto error;
		}
		cifptr = &cif;

	} else {
		cifptr = self->cif;
	}

	PyObjC_DURING
		ffi_call(cifptr, FFI_FN(self->function), argbuf, values);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		goto error;
	}

	retval = PyObjCFFI_BuildResult(self->methinfo, 0, argbuf, byref, 
			byref_attr, byref_out_count, NULL, 0, values);

	if (variadicAllArgs) {
		if (PyObjCFFI_FreeByRef(self->methinfo->ob_size+PyTuple_Size(args), byref, byref_attr) < 0) {
			byref = NULL; byref_attr = NULL;
			goto error;
		}
	} else {
		if (PyObjCFFI_FreeByRef(self->methinfo->ob_size, byref, byref_attr) < 0) {
			byref = NULL; byref_attr = NULL;
			goto error;
		}
	}
	PyMem_Free(argbuf); argbuf = NULL;
	return retval;

error:
	if (variadicAllArgs) {
		if (PyObjCFFI_FreeByRef(PyTuple_Size(args), byref, byref_attr) < 0) {
			byref = NULL; byref_attr = NULL;
			goto error;
		}
	} else {
		if (PyObjCFFI_FreeByRef(self->methinfo->ob_size, byref, byref_attr) < 0) {
			byref = NULL; byref_attr = NULL;
			goto error;
		}
	}
	if (argbuf) {
		PyMem_Free(argbuf);
	}
	return NULL;
}

static void 
func_dealloc(PyObject* s)
{
	func_object* self = (func_object*)s;

	Py_XDECREF(self->doc); self->doc = NULL;
	Py_XDECREF(self->name); self->name = NULL;
	Py_XDECREF(self->module); self->module = NULL;
	if (self->cif != NULL) {
		PyObjCFFI_FreeCIF(self->cif);
	}
	Py_XDECREF(self->methinfo);
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
	PyObject_GenericGetAttr,		/* tp_getattro */
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
	func_methods,				/* tp_methods */
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
PyObjCFunc_New(PyObject* name, void* func, const char* signature, PyObject* doc, PyObject* meta)
{
	func_object* result;
	

	result = PyObject_NEW(func_object, &PyObjCFunc_Type);
	if (result == NULL) return NULL;

	result->function = NULL;
	result->doc = NULL;
	result->name = NULL;
	result->module = NULL;

	result->methinfo= PyObjCMethodSignature_WithMetaData(signature, meta);
	if (result->methinfo == NULL) {
		Py_DECREF(result->methinfo);
		return NULL;
	}

	result->function = func;

	result->doc = doc;
	Py_XINCREF(doc);

	result->name = name;
	Py_XINCREF(name);
	result->cif = PyObjCFFI_CIFForSignature(result->methinfo);
	if (result->cif == NULL) {
		Py_DECREF(result);
		return NULL;	
	}
	
	return (PyObject*)result;
}

PyObjCMethodSignature* PyObjCFunc_GetMethodSignature(PyObject* func)
{
	return ((func_object*)func)->methinfo;
}
