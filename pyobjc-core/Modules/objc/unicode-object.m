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
		res = PyObject_GetAttr(py_nsstr, attr_name);
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
	PyVarObject_HEAD_INIT(&PyType_Type, 0)
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
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};


#if PY_VERSION_HEX >= 0x03030000
   /* 
    * Python 3.3 introduced a new, more efficient representation
    * for unicode objects. 
    *
    * This function cannot use the most efficient
    * representation where the character data is stored in the same
    * memory block as the object header because PyObjCUnicode adds
    * more data to the object header, which PyUnicode does not
    * expect.
    *
    * This function therefore creates a "legacy string, ready" (see
    * unicodeobject.h in the python 3.3 source tree for more information)
    *
    *
    * XXX: I'm not very happy about this implementation, it is too verbose
    *      and seems to be even more fragile than the implementation for
    *      older python versions.
    */
PyObject* 
PyObjCUnicode_New(NSString* value)
{
	PyObjCUnicodeObject* result;
        PyASCIIObject *ascii;
        PyCompactUnicodeObject *compact;

	NSInteger i, length;
	unichar* volatile characters = NULL;
	NSRange range;

	PyObjC_DURING
		length = [value length];
		characters = PyObject_MALLOC(sizeof(unichar) * (length+1));
		if (characters == NULL) {
			PyErr_NoMemory();
			NS_VALUERETURN(NULL, PyObject*);
		}

		range = NSMakeRange(0, length);

		[value getCharacters: characters range: range];
		characters[length] = 0;

	PyObjC_HANDLER
		if (characters) {
			PyMem_Free(characters);
			characters = NULL;
		}
		PyObjCErr_FromObjC(localException);
		NS_VALUERETURN(NULL, PyObject*);
	PyObjC_ENDHANDLER

	result = PyObject_New(PyObjCUnicodeObject, &PyObjCUnicode_Type);
	ascii = (PyASCIIObject*)result;
	compact = (PyCompactUnicodeObject*)result;

	ascii->hash = -1;
	ascii->wstr = NULL;
	ascii->length = length;

	ascii->state.compact = 0;
	ascii->state.ready = 1;
	ascii->state.interned = SSTATE_NOT_INTERNED;

	compact->utf8_length = 0;
	compact->utf8 = NULL;
	compact->wstr_length = 0;

	result->base.data.any = NULL;

	Py_UCS4 maxchar = 0;
	int nr_surrogates = 0;
	for (i = 0; i < length; i++) {
		Py_UCS4 cur = (Py_UCS4)characters[i];
		if (Py_UNICODE_IS_HIGH_SURROGATE(cur) && (
			i < length - 1) && (
			Py_UNICODE_IS_LOW_SURROGATE(characters[i+1]))) {
			Py_UCS4 ch = Py_UNICODE_JOIN_SURROGATES(
				characters[i],
				characters[i+1]);
			i++;
			nr_surrogates++;
			if (ch > maxchar) {
				maxchar = ch;
			}
		} else if (cur > maxchar) {
			maxchar = cur;
		}
	}
	if (maxchar <= 128) {
		ascii->state.ascii = 1; 
		ascii->state.kind = PyUnicode_1BYTE_KIND;
	} else if (maxchar <= 255) {
		ascii->state.ascii = 0; 
		ascii->state.kind = PyUnicode_1BYTE_KIND;
	} else if (maxchar <= 0xFFFF) {
		ascii->state.ascii = 0; 
		ascii->state.kind = PyUnicode_2BYTE_KIND;
	} else {
		ascii->state.ascii = 0; 
		ascii->state.kind = PyUnicode_4BYTE_KIND;
	}

	/* Create storage for the code points and copy the data */
	result->base.data.any = NULL;
	if (ascii->state.kind == PyUnicode_1BYTE_KIND) {
		result->base.data.latin1 = PyObject_MALLOC(sizeof(Py_UCS1) * (length + 1 - nr_surrogates));
		if (result->base.data.latin1 == NULL) {
			Py_DECREF((PyObject*)result);
			PyMem_Free(characters); characters = NULL;
			PyErr_NoMemory();
			return NULL;
		}
		Py_UCS1* latin1_cur = result->base.data.latin1;
		for (i = 0; i < length; i++) {
			if (Py_UNICODE_IS_HIGH_SURROGATE(characters[i]) && (
				i < length - 1) && (
				Py_UNICODE_IS_LOW_SURROGATE(characters[i+1]))) {
				Py_UCS4 ch = Py_UNICODE_JOIN_SURROGATES(
					characters[i],
					characters[i+1]);
				*latin1_cur++ =  (Py_UCS1)ch;
				i++;
			} else {
				*latin1_cur++ =  (Py_UCS1)characters[i];
			}
		}
		*latin1_cur = 0;
		ascii->length = length - nr_surrogates;
		if (ascii->state.ascii) {
			/* With ASCII representation the UTF8 representation is 
			 * also known without further calculation, and MUST be
			 * filled according to the spec
			 */
			compact->utf8_length = length - nr_surrogates;
			compact->utf8 = (char*)result->base.data.latin1;
		}

	} else if (ascii->state.kind == PyUnicode_2BYTE_KIND) {
		if (nr_surrogates == 0) {
			/* No surrogates and 2BYTE_KIND, this means the unichar buffer 
			 * can be reused as storage for the python unicode string
			 */
			ascii->length = length;
			result->base.data.ucs2 = (Py_UCS2*)characters;
			characters = NULL;

		} else {
			result->base.data.ucs2 = PyObject_MALLOC(sizeof(Py_UCS2) * (length + 1 - nr_surrogates));
			if (result->base.data.ucs2 == NULL) {
				Py_DECREF((PyObject*)result);
				PyMem_Free(characters); characters = NULL;
				PyErr_NoMemory();
				return NULL;
			}
			Py_UCS2* ucs2_cur = result->base.data.ucs2;
			for (i = 0; i < length; i++) {
				if (Py_UNICODE_IS_HIGH_SURROGATE(characters[i]) && (
					i < length - 1) && (
					Py_UNICODE_IS_LOW_SURROGATE(characters[i+1]))) {
					Py_UCS4 ch = Py_UNICODE_JOIN_SURROGATES(
						characters[i],
						characters[i+1]);
					*ucs2_cur++ =  (Py_UCS2)ch;
					i++;
				} else {
					*ucs2_cur++ =  (Py_UCS2)characters[i];
				}
			}
			ascii->length = length - nr_surrogates;
			*ucs2_cur = 0;
		}
#if SIZEOF_WCHAR_T == 2
		ascii->wstr = (wchar_t*)(result->base.data.ucs4);
		compact->wstr_length = ascii->length;
#endif

	} else { /* 4BYTE_KIND */
		result->base.data.ucs4 = PyObject_MALLOC(sizeof(Py_UCS4) * (length + 1 - nr_surrogates));
		if (result->base.data.ucs4 == NULL) {
			Py_DECREF((PyObject*)result);
			PyMem_Free(characters); characters = NULL;
			PyErr_NoMemory();
			return NULL;
		}

		Py_UCS4* ucs4_cur = result->base.data.ucs4;
		for (i = 0; i < length; i++) {
			if (Py_UNICODE_IS_HIGH_SURROGATE(characters[i]) && (
				i < length - 1) && (
				Py_UNICODE_IS_LOW_SURROGATE(characters[i+1]))) {
				Py_UCS4 ch = Py_UNICODE_JOIN_SURROGATES(
					characters[i],
					characters[i+1]);

				if (ch > 0x10ffff) {
					/* Unicode spec has a maximum code point value and
					 * Python 3.3 enforces this, keep surrogate pair 
					 * to avoid an error.
					 */
					*ucs4_cur++ =  (Py_UCS4)characters[i];
				} else {
					*ucs4_cur++ =  (Py_UCS4)ch;
					i++;
				}
			} else {
				*ucs4_cur++ =  (Py_UCS4)characters[i];
			}
		}
		*ucs4_cur = 0;
		ascii->length = length - nr_surrogates;
#if SIZEOF_WCHAR_T == 4
		ascii->wstr = (wchar_t*)(result->base.data.ucs4);
		compact->wstr_length = ascii->length;
#endif
	}


	if (characters != NULL) {
		PyObject_DEL(characters); 
		characters = NULL;
	}


#ifdef Py_DEBUG
	/* Check that the unicode object is correct */
	_PyUnicode_CheckConsistency((PyObject*)result, 1);
#endif

	/* Finally store PyUnicode specific data */
	result->weakrefs = NULL;
	result->py_nsstr = NULL;
	result->nsstr = value;
	CFRetain(value);

	return (PyObject*)result;
}

#else /* Python 3.2 and before */
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

#ifdef PyObjC_UNICODE_FAST_PATH
	Py_ssize_t length = [value length];
	NSRange range;

	if (length < 0) {
		PyErr_SetString(PyExc_SystemError, "string with negative length");
		return NULL;
	}
	result = PyObject_New(PyObjCUnicodeObject, &PyObjCUnicode_Type);
	Py_UNICODE* tptr = PyObject_MALLOC(sizeof(Py_UNICODE) * (length+1));
	tptr[0] = tptr[length] = 0;
	result->base.str = tptr;
	/*PyUnicode_AS_UNICODE(result) = tptr;*/
	tptr = NULL;

	if (PyUnicode_AS_UNICODE(result) == NULL) {
		Py_DECREF((PyObject*)result);
		PyErr_NoMemory();
		return NULL;
	}
	range = NSMakeRange(0, length);
	[value getCharacters:(unichar *)PyUnicode_AS_UNICODE(result) range:range];
	/*PyUnicode_GET_SIZE(result) = length;*/
	result->base.length = length;
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
	Py_UNICODE* tptr = PyObject_MALLOC(sizeof(Py_UNICODE) * (length+1));
	tptr[0] = tptr[length] = 0;
	result->base.str = tptr;
	if (PyUnicode_AS_UNICODE(result) == NULL) {
		Py_DECREF((PyObject*)result);
		PyMem_Free(characters); characters = NULL;
		PyErr_NoMemory();
		return NULL;
	}
	/*PyUnicode_GET_SIZE(result) = length;*/
	result->base.length = length;
	for (i = 0; i < length; i++) {
		PyUnicode_AS_UNICODE(result)[i] = (Py_UNICODE)(characters[i]);
	}
	PyMem_Free(characters); characters = NULL;
#endif


	result->base.hash = -1;
#if PY_MAJOR_VERSION == 3
	result->base.state = 0;
#endif
	result->base.defenc = NULL;

	if (PyUnicode_GET_SIZE(result) == 0) {
		result->base.hash = 0;
	}

	result->weakrefs = NULL;
	result->py_nsstr = NULL;
	result->nsstr = value;
	CFRetain(value);

	return (PyObject*)result;
}
#endif /* Python 3.2 and before */

NSString*
PyObjCUnicode_Extract(PyObject* value)
{
	if (!PyObjCUnicode_Check(value)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	return ((PyObjCUnicodeObject*)value)->nsstr;
}
