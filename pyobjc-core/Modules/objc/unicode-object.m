/*
 * Custom subclass of PyUnicode_Type, to allow for transparent bridging of
 * strings
 */

#include "pyobjc.h"

#include <stddef.h>
#include <Foundation/NSString.h>

typedef struct {
	PyUnicodeObject	base;
	PyObject*	weakrefs;
	id		nsstr;
	PyObject* py_nsstr;
} PyObjCUnicodeObject;

PyDoc_STRVAR(class_doc,
	"objc.pyobjc_unicode\n"
	"\n"
	"Subclass of unicode for representing NSString values. Use \n"
	"the method nsstring to access the NSString. \n"
	"Note that instances are immutable and won't be updated when\n"
	"the value of the NSString changes."
);

static void
class_dealloc(PyObject* obj)
{
	PyObjCUnicodeObject* uobj = (PyObjCUnicodeObject*)obj;
	id nsstr = uobj->nsstr;
	PyObject* weakrefs = uobj->weakrefs;
	PyObject* py_nsstr = uobj->py_nsstr;

	PyObjC_UnregisterPythonProxy(nsstr, obj);

	Py_XDECREF(py_nsstr);
	if (nsstr) {
		CFRelease(nsstr);
	}

	if (weakrefs) {
		PyObject_ClearWeakRefs(obj);
	}

	PyUnicode_Type.tp_dealloc(obj);
}

static PyObject* 
meth_nsstring(PyObject* self)
{
	PyObjCUnicodeObject* uobj = (PyObjCUnicodeObject*)self;
	if (uobj->py_nsstr == NULL) {
		uobj->py_nsstr = PyObjCObject_New(uobj->nsstr, 
				PyObjCObject_kDEFAULT, YES);
	}
	Py_INCREF(uobj->py_nsstr);
	return uobj->py_nsstr;
}


static PyObject*
meth_getattro(PyObject *o, PyObject *attr_name)
{
	PyObject *res;
	res = PyObject_GenericGetAttr(o, attr_name);
	if (res == NULL) {
		PyErr_Clear();
		PyObject *py_nsstr = meth_nsstring(o);
		res = PyObject_GenericGetAttr(py_nsstr, attr_name);
		Py_XDECREF(py_nsstr);
	}
	return res;
}

static PyObject*
meth_reduce(PyObject* self)
{
	PyObject* retVal = NULL;
	PyObject *v = NULL;
	PyObject *v2 = NULL;

	retVal = PyTuple_New(2);
	if (retVal == NULL) goto error;

	v = (PyObject*)&PyUnicode_Type;
	Py_INCREF(v);
	PyTuple_SET_ITEM(retVal, 0, v);

	v = PyUnicode_FromObject(self);
	if (v == NULL ) goto error;

	v2 = PyTuple_New(1);
	if (v2 == NULL) goto error;
	PyTuple_SET_ITEM(v2, 0, v);
	PyTuple_SET_ITEM(retVal, 1, v2);

	return retVal;

error:
	Py_XDECREF(retVal);
	Py_XDECREF(v);
	return NULL;
}

static PyMethodDef class_methods[] = {
	{
	  "nsstring",
	  (PyCFunction)meth_nsstring,
	  METH_NOARGS,
	  "directly access NSString instance"
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
nsstring_get__pyobjc_object__(PyObject *self, void *closure __attribute__((__unused__))) {
	return meth_nsstring(self);
}

static PyGetSetDef nsstring_getsetters[] = {
	{
		"__pyobjc_object__",
		(getter)nsstring_get__pyobjc_object__, NULL,
		"raw NSString instance",
		NULL
	},
	{
		NULL,
		NULL, NULL,
		NULL,
		NULL
	}
};

static PyObject* 
class_new(
	PyTypeObject* type __attribute__((__unused__)), 
	PyObject* args __attribute__((__unused__)), 
	PyObject* kwds __attribute__((__unused__)))
{
	PyErr_SetString(PyExc_TypeError, 
			"Cannot create instances of 'objc.unicode' in Python");
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
	meth_getattro,		/* tp_getattro */
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
	nsstring_getsetters,			/* tp_getset */
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
	0,                                      /* tp_weaklist */
	0                                       /* tp_del */
};

PyObject* 
PyObjCUnicode_New(NSString* value)
{
	/* Conversion to PyUnicode without creating an autoreleased object.
	 *
	 * NOTE: A final optimization is removing the copy of 'characters', but
	 * that can only be done when sizeof(unichar) == Py_UNICODE_SIZE.
	 *
	 * The reason for doing this: NSThread 
	 *     +detachNewThreadSelector:toTarget:withObject:, with a string
	 *     as one of the arguments.
	 *
	 * Another reason is that the following loop 'leaks' memory when using
	 * -UTF8String:
	 *  	while True:
	 *  		NSString.alloc().init()
	 *
	 *  while the following doesn't:
	 *
	 *  	while True:
	 *  		NSArray.alloc().init()
	 */
	PyObjCUnicodeObject* result;
// XXX - I don't know how to get gcc to let me use sizeof(unichar)
#ifdef PyObjC_UNICODE_FAST_PATH
	int length = [value length];
	result = PyObject_New(PyObjCUnicodeObject, &PyObjCUnicode_Type);
	PyUnicode_AS_UNICODE(result) = PyMem_NEW(Py_UNICODE, length);
	if (PyUnicode_AS_UNICODE(result) == NULL) {
		Py_DECREF((PyObject*)result);
		PyErr_NoMemory();
		return NULL;
	}
	[value getCharacters:(unichar *)PyUnicode_AS_UNICODE(result)];
	PyUnicode_GET_SIZE(result) = length;
#else
	int i, length;
	unichar* volatile characters = NULL;
	NSRange range;

	PyObjC_DURING
		length = [value length];
		characters = PyMem_Malloc(sizeof(unichar) * length);
		if (characters == NULL) {
			PyErr_NoMemory();
			NS_VALUERETURN(NULL, PyObject*);
		}

		range = NSMakeRange(0, length);

		[value getCharacters: characters range: range];

	PyObjC_HANDLER
		if (characters) {
			PyMem_Free(characters);
			characters = NULL;
		}
		PyObjCErr_FromObjC(localException);
		NS_VALUERETURN(NULL, PyObject*);
	PyObjC_ENDHANDLER

	result = PyObject_New(PyObjCUnicodeObject, &PyObjCUnicode_Type);
	PyUnicode_AS_UNICODE(result) = PyMem_NEW(Py_UNICODE, length);
	if (PyUnicode_AS_UNICODE(result) == NULL) {
		Py_DECREF((PyObject*)result);
		PyMem_Free(characters); characters = NULL;
		PyErr_NoMemory();
		return NULL;
	}
	PyUnicode_GET_SIZE(result) = length;
	for (i = 0; i < length; i++) {
		PyUnicode_AS_UNICODE(result)[i] = (Py_UNICODE)(characters[i]);
	}
	PyMem_Free(characters); characters = NULL;
#endif

	result->base.defenc = NULL;

	result->base.hash = -1;

	if (PyUnicode_GET_SIZE(result) == 0) {
		result->base.hash = 0;
	}

	result->weakrefs = NULL;
	result->py_nsstr = NULL;
	result->nsstr = value;
	CFRetain(value);

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
