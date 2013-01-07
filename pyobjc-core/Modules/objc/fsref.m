/*
 * A custom wrapper for the (opaque) FSRef structure.
 */
#include "pyobjc.h"
#import <CoreServices/CoreServices.h>

#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#pragma clang diagnostic ignored "-Wdeprecated-declarations"


#if USE_TOOLBOX_OBJECT_GLUE
#include "pymactoolbox.h"
#endif

/*
 * Interface of the FSRef type:
 *
 * FSRef.from_pathname(value)
 *   # -> returns new FSRef instance for posix path 'value'
 *  
 * aref.as_pathname() 
 *  # -> returns a Unicode string with the posix path
 *
 * aref.as_carbon()
 *  # -> return a Carbon.File.FSRef instance (only
 *  #    available when Carbon support is enabled in Python)
 *
 * aref.data
 *  # -> read-only property with the bytes in the FSRef
 *
 * This is more or less the same interface as Carbon.File.FSRef, but
 * excluding API wrappers.
 */

typedef struct {
	PyObject_HEAD

	FSRef	ref;
} PyObjC_FSRefObject;

static PyObject* fsref_as_bytes(PyObject* ref, void* closure __attribute__((__unused__)))
{
	if (!PyObjC_FSRefCheck(ref)) {
		PyErr_SetString(PyExc_TypeError, "self is not a FSRef");
	}

	return PyBytes_FromStringAndSize(
			(char*)&((PyObjC_FSRefObject*)ref)->ref,
			sizeof(FSRef));
}

#if USE_TOOLBOX_OBJECT_GLUE
static PyObject* fsref_as_carbon(PyObject* ref)
{
	if (!PyObjC_FSRefCheck(ref)) {
		PyErr_SetString(PyExc_TypeError, "self is not a FSRef");
	}

	return PyMac_BuildFSRef((&((PyObjC_FSRefObject*)ref)->ref));
}
#endif

static PyObject* fsref_as_path(PyObject* ref)
{
	OSStatus rc;
	UInt8 buffer[1024];

	if (!PyObjC_FSRefCheck(ref)) {
		PyErr_SetString(PyExc_TypeError, "self is not a FSRef");
	}

	rc = FSRefMakePath( &((PyObjC_FSRefObject*)ref)->ref,
			buffer, sizeof(buffer));
	if (rc != 0) {
#if (PY_MAJOR_VERSION == 2) && defined (USE_TOOLBOX_OBJECT_GLUE)
		PyMac_Error(rc);
#else
		PyErr_Format(PyExc_OSError, "MAC Error %d", rc);
#endif
		return NULL;
	}

	return PyUnicode_DecodeUTF8((char*)buffer,
			strlen((char*)buffer), NULL);
}

static PyObject* fsref_from_path(PyObject* self __attribute__((__unused__)), PyObject* path)
{
	PyObject* value;
	FSRef result;
	Boolean isDirectory;
	OSStatus rc;

	if (PyUnicode_Check(path)) {
		value = PyUnicode_AsEncodedString(path, NULL, NULL);
#if PY_MAJOR_VERSION == 2
	} else if(PyString_Check(path)) {
		value = path; Py_INCREF(path);
#endif
	} else {
		PyErr_SetString(PyExc_TypeError, "Expecting string");
		return NULL;
	}

	if (value == NULL) return NULL;

	rc = FSPathMakeRef((UInt8*)PyBytes_AsString(value), &result, &isDirectory);
	Py_DECREF(value);
	if (rc != 0) {
#if (PY_MAJOR_VERSION == 2) && defined(USE_TOOLBOX_OBJECT_GLUE)
		PyMac_Error(rc);
#else
		PyErr_Format(PyExc_OSError, "MAC Error %d", rc);
#endif
		return NULL;
	}

	return PyObjC_decode_fsref(&result);
}

static PyGetSetDef fsref_getset[] = {
	{
		"data",
		fsref_as_bytes,
		0,
		"bytes in the FSRef",
		0
	},
	{ 0, 0, 0, 0, 0}
};


static PyMethodDef fsref_methods[] = {
	{
		"as_pathname",
		(PyCFunction)fsref_as_path,
		METH_NOARGS,
		"return POSIX path for this object (Unicode string)"
	},
	{
		"from_pathname",
		(PyCFunction)fsref_from_path,
		METH_O|METH_CLASS,
		"create FSRef instance for an POSIX path"
	},
	
#if USE_TOOLBOX_OBJECT_GLUE
	{
		"as_carbon",
		(PyCFunction)fsref_as_carbon,
		METH_NOARGS,
		"return Carbon.File.FSRef instance for this object"
	},
#endif

	{ 0, 0, 0, 0 }
};


PyTypeObject PyObjC_FSRefType = {
	PyVarObject_HEAD_INIT(&PyType_Type, 0)
	"objc.FSRef",				/* tp_name */
	sizeof(PyObjC_FSRefObject),		/* tp_basicsize */
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
	fsref_methods,				/* tp_methods */
	0,					/* tp_members */
	fsref_getset,				/* tp_getset */
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


int PyObjC_encode_fsref(PyObject* value, void* buffer)
{
#if USE_TOOLBOX_OBJECT_GLUE
	/* We cannot test if 'arg' is an instance of Carbon.File.FSRef... */
	if (PyMac_GetFSRef(value, (FSRef*)buffer) == 1) {
		return 0;
	}
	PyErr_Clear();
#endif

	if (PyObjC_FSRefCheck(value)) {
		*(FSRef*)buffer = ((PyObjC_FSRefObject*)value)->ref;
		return 0;
	}

	PyErr_SetString(PyExc_ValueError, "Cannot convert value to FSRef");
	return -1;
}


PyObject* PyObjC_decode_fsref(void* buffer)
{
	PyObjC_FSRefObject* result = PyObject_New(
			PyObjC_FSRefObject, &PyObjC_FSRefType);
	if (result == NULL) {
		return NULL;
	}
	result->ref = *(FSRef*)buffer;
	return (PyObject*)result;
}
