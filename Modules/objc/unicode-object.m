/*
 * Custom subclass of PyUnicode_Type, to allow for transparent bridging of
 * strings
 */

#include "pyobjc.h"

#include <stddef.h>

typedef struct {
	PyUnicodeObject	base;
	PyObject*	weakrefs;
	id		nsstr;
} PyObjCUnicodeObject;

PyDoc_STRVAR(class_doc,
	"objc.pyobjc_unicode\n"
	"\n"
	"Subclass of unicode for representing NSString values. Use \n"
	"the method pyobjc_NSString to access the NSString. \n"
	"Note that instances are immutable and won't be updated when\n"
	"the value of the NSString changes."
);

static void
class_dealloc(PyObject* obj)
{
	id nsstr = ((PyObjCUnicodeObject*)obj)->nsstr;
	PyObject* weakrefs = ((PyObjCUnicodeObject*)obj)->weakrefs;

	[nsstr release];

	if (weakrefs) {
		PyObject_ClearWeakRefs(obj);
	}

	PyUnicode_Type.tp_dealloc(obj);
}

static PyObject* 
meth_nsstring(PyObject* self)
{
	return PyObjCObject_New(((PyObjCUnicodeObject*)self)->nsstr);
}

static PyObject* 
meth_syncNSString(PyObjCUnicodeObject* self)
{
	PyUnicodeObject  dummy;
	const char* utf8 = [self->nsstr UTF8String];
	PyUnicodeObject* tmp = (PyUnicodeObject*)PyUnicode_DecodeUTF8(utf8, strlen(utf8), "strict");

	if (tmp == NULL) return NULL;

	
	PyUnicode_AS_UNICODE(&dummy) = PyMem_NEW(Py_UNICODE,
		PyUnicode_GET_SIZE(tmp));
	if (PyUnicode_AS_UNICODE(&dummy) == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	PyMem_Free(PyUnicode_AS_UNICODE(self));
	PyUnicode_AS_UNICODE(self) = PyUnicode_AS_UNICODE(&dummy);
	PyUnicode_GET_SIZE(self) = PyUnicode_GET_SIZE(tmp);
	memcpy((char*)PyUnicode_AS_DATA(self), PyUnicode_AS_DATA(tmp),
		PyUnicode_GET_DATA_SIZE(tmp));

	self->base.hash = -1;
	if (PyUnicode_GET_SIZE(tmp) == 0) {
		self->base.hash = 0;
	}
	Py_XDECREF(self->base.defenc);
	self->base.defenc = tmp->defenc;
	Py_XINCREF(tmp->defenc);
	Py_DECREF(tmp);

	Py_INCREF(Py_None);
	return Py_None;
}

/*
 * Make sure objc_unicode objects don't get pickled.
 *
 * See meth_reduce in objc-object.m for details.
 */
static PyObject*
meth_reduce(PyObject* self)
{
	PyObject* retVal;
	PyObject *v, *v2;

	retVal = PyTuple_New(2);
	if (retVal == NULL) {
		return NULL;
	}

	v = (PyObject*)&PyUnicode_Type;
	Py_INCREF(v);
	PyTuple_SET_ITEM(retVal, 0, v);

	v = PyUnicode_FromObject(self);
	if (v == NULL ) {
		Py_DECREF(retVal);
		return NULL;
	}

	v2 = PyTuple_New(1);
	if (v2 == NULL) {
		Py_DECREF(v);
		Py_DECREF(retVal);
		return NULL;
	}
	PyTuple_SET_ITEM(v2, 0, v);
	PyTuple_SET_ITEM(retVal, 1, v2);

	return retVal;
}

static PyMethodDef class_methods[] = {
	{
	  "nsstring",
	  (PyCFunction)meth_nsstring,
	  METH_NOARGS,
	  "directly access NSString instance"
	},
	{
	  "syncFromNSString",
	  (PyCFunction)meth_syncNSString,
	  METH_NOARGS,
	  "Copy contents of the NSString to the unicode object"
	},
	{
	  "__reduce__",
	  (PyCFunction)meth_reduce,
	  METH_NOARGS,
	  "Used for pickling"
	},
        { 0, 0, 0, 0 } /* sentinel */
};

static PyObject* 
class_new(
	PyTypeObject* type __attribute__((__unused__)), 
	PyObject* args __attribute__((__unused__)), 
	PyObject* kwds __attribute__((__unused__)))
{
	PyErr_SetString(PyExc_TypeError, "Cannot create objc.unicode from Python");
	return NULL;
}

PyTypeObject PyObjCUnicode_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.pyobjc_unicode",			/* tp_name */
	sizeof(PyObjCUnicodeObject),		/* tp_basicsize */
	0,			 		/* tp_itemsize */
	/* methods */
	class_dealloc,	 			/* tp_dealloc */
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
	0,					/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
 	class_doc,				/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	offsetof(PyObjCUnicodeObject, weakrefs),	/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	class_methods,				/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
	&PyUnicode_Type,			/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	class_new,				/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
        0,                                      /* tp_bases */
        0,                                      /* tp_mro */
        0,                                      /* tp_cache */
        0,                                      /* tp_subclasses */
        0                                       /* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
        , 0                                     /* tp_del */
#endif
};

PyObject* 
PyObjCUnicode_New(NSString* value)
{
	const char* utf8 = [value UTF8String];
	PyUnicodeObject* tmp = (PyUnicodeObject*)PyUnicode_DecodeUTF8(utf8, strlen(utf8), "strict");
	PyObjCUnicodeObject* result;

	if (tmp == NULL) return NULL;

	result = PyObject_New(PyObjCUnicodeObject, &PyObjCUnicode_Type);
	PyUnicode_AS_UNICODE(result) = PyMem_NEW(Py_UNICODE,
		PyUnicode_GET_SIZE(tmp));
	if (PyUnicode_AS_UNICODE(result) == NULL) {
		Py_DECREF((PyObject*)result);
		PyErr_NoMemory();
		return NULL;
	}
	PyUnicode_GET_SIZE(result) = PyUnicode_GET_SIZE(tmp);
	memcpy((char*)PyUnicode_AS_DATA(result), PyUnicode_AS_DATA(tmp),
		PyUnicode_GET_DATA_SIZE(tmp));

	result->base.hash = -1;

	if (PyUnicode_GET_SIZE(tmp) == 0) {
		result->base.hash = 0;
	}

	result->base.defenc = tmp->defenc;
	Py_XINCREF(tmp->defenc);
	Py_DECREF(tmp);

	result->weakrefs = 0;
	result->nsstr = value;
	[value retain];

	return (PyObject*)result;
}

NSString*
PyObjCUnicode_Extract(PyObject* value)
{
	if (!PyObjCUnicode_Check(value)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	return ((PyObjCUnicodeObject*)value)->nsstr;
}
