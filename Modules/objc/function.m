/*
 * Wrapper for "simple" global functions
 */
#include "pyobjc.h"

typedef struct {
	PyObject_HEAD
	ffi_cif*  cif;
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
		NULL,
		0,
		0,
		NULL
	}
};

static PyObject* 
func_call(PyObject* self, PyObject* args, PyObject* kwds)
{
	PyErr_SetString(PyExc_NotImplementedError, "calling objc.function objects");
	return NULL;
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
	(destructor)func_dealloc,		/* tp_dealloc */
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
	0					/* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
	, 0,					/* tp_del */
#endif
};



PyObject* 
PyObjCFunc_New(PyObject* name, void* func, const char* signature, PyObject* doc)
{
	func_object* result;
	PyObjCMethodSignature* sig;
	
	sig = PyObjCMethodSignature_FromSignature(signature);
	if (sig == NULL) return NULL;

	result = PyObject_NEW(func_object, &PyObjCFunc_Type);
	if (result == NULL) return NULL;


	result->cif = PyObjCFFI_CIFForSignature(sig, 0);
	PyObjCMethodSignature_Free(sig);
	if (result->cif == NULL) {
		Py_DECREF(result);
		return NULL;	
	}

	result->function = func;

	result->doc = doc;
	Py_XINCREF(doc);

	result->name = name;
	Py_XINCREF(name);
	
	return (PyObject*)result;
}
