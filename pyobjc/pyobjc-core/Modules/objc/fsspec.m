/*
 * A custom wrapper for the (opaque) FSSpec structure.
 */
#include "pyobjc.h"
#import <CoreServices/CoreServices.h>


#if USE_TOOLBOX_OBJECT_GLUE
#include "pymactoolbox.h"
#endif

/*
 * Interface of the FSSpec type:
 *
 * FSSpec.from_pathname(value)
 *   # -> returns new FSSpec instance for posix path 'value'
 *  
 * aspec.as_pathname() 
 *  # -> returns a Unicode string with the posix path
 *
 * aspec.as_carbon()
 *  # -> return a Carbon.File.FSSpec instance (only
 *  #    available when Carbon support is enabled in Python)
 *
 * aspec.data
 *  # -> read-only property with the bytes in the FSSpec
 *
 * This is more or less the same interface as Carbon.File.FSSpec, but
 * excluding API wrappers.
 */

typedef struct {
	PyObject_HEAD

	FSSpec	ref;
} PyObjC_FSSpecObject;

static PyObject* fsspec_as_bytes(PyObject* ref, void* closure __attribute__((__unused__)))
{
	if (!PyObjC_FSSpecCheck(ref)) {
		PyErr_SetString(PyExc_TypeError, "self is not a FSSpec");
	}

	return PyBytes_FromStringAndSize(
			(char*)&((PyObjC_FSSpecObject*)ref)->ref,
			sizeof(FSSpec));
}

#if defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__)
static PyObject* fsspec_as_carbon(PyObject* ref)
{
	if (!PyObjC_FSSpecCheck(ref)) {
		PyErr_SetString(PyExc_TypeError, "self is not a FSSpec");
	}

	return PyMac_BuildFSSpec((&((PyObjC_FSSpecObject*)ref)->ref));
}
#endif

static PyGetSetDef fsspec_getset[] = {
	{
		"data",
		fsspec_as_bytes,
		0,
		"bytes in the FSSpec",
		0
	},
	{ 0, 0, 0, 0, 0}
};


static PyMethodDef fsspec_methods[] = {
#if defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__)
	{
		"as_carbon",
		(PyCFunction)fsspec_as_carbon,
		METH_NOARGS,
		"return Carbon.File.FSSpec instance for this object"
	},
#endif

	{ 0, 0, 0, 0 }
};


PyTypeObject PyObjC_FSSpecType = {
	PyVarObject_HEAD_INIT(&PyType_Type, 0)
	"objc.FSSpec",				/* tp_name */
	sizeof(PyObjC_FSSpecObject),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	0,					/* tp_dealloc */
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
	PyObject_GenericSetAttr,		/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
 	0,					/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	fsspec_methods,				/* tp_methods */
	0,					/* tp_members */
	fsspec_getset,				/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	0,					/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
	0,                                      /* tp_bases */
	0,                                      /* tp_mro */
	0,                                      /* tp_cache */
	0,                                      /* tp_subclasses */
	0,                                      /* tp_weaklist */
	0                                       /* tp_del */
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};


int PyObjC_encode_fsspec(PyObject* value, void* buffer)
{
#if defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__)
	/* We cannot test if 'arg' is an instance of Carbon.File.FSSpec... */
	if (PyMac_GetFSSpec(value, (FSSpec*)buffer) == 1) {
		return 0;
	}
	PyErr_Clear();
#endif

	if (PyObjC_FSSpecCheck(value)) {
		*(FSSpec*)buffer = ((PyObjC_FSSpecObject*)value)->ref;
		return 0;
	}

	PyErr_SetString(PyExc_ValueError, "Cannot convert value to FSSpec");
	return -1;
}


PyObject* PyObjC_decode_fsspec(void* buffer)
{
	PyObjC_FSSpecObject* result = PyObject_New(
			PyObjC_FSSpecObject, &PyObjC_FSSpecType);
	if (result == NULL) {
		return NULL;
	}
	result->ref = *(FSSpec*)buffer;
	return (PyObject*)result;
}
