/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 * With various updates by Ronald Oussoren and others ((C) 2002, 2003)
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * Created Mon Oct 28 12:38:18 1996.
 *
 */

#include "pyobjc.h"

static void
PyObjCPointer_dealloc (PyObject* _self)
{
	PyObjCPointer* self = (PyObjCPointer*)_self;
	Py_DECREF (self->type);
	PyObject_Free((PyObject*)self);
}

PyDoc_STRVAR(PyObjCPointer_unpack_doc,
	"Unpack the pointed value accordingly to its type.\n"
        "obj.unpack() -> value");
static PyObject *
PyObjCPointer_unpack (PyObject* _self)
{
	PyObjCPointer* self = (PyObjCPointer*)_self;

	if (self->ptr) {
		const char *type = PyString_AS_STRING (self->type);

		if (*type == _C_VOID) {
			PyErr_SetString (PyObjCExc_Error, 
				"Cannot dereference a pointer to void");
			return NULL;
		} else {
			return pythonify_c_value (type, self->ptr);
		}
        } else {
		Py_INCREF (Py_None);
		return Py_None;
        }
}

static PyMethodDef PyObjCPointer_methods[] =
{
	{
		"unpack",   
		(PyCFunction)PyObjCPointer_unpack,       
		METH_NOARGS,   
		PyObjCPointer_unpack_doc 
	},
	{ 0, 0, 0, 0 }
};

static PyMemberDef PyObjCPointer_members[] = {
	{
		"type",
		T_OBJECT,
		offsetof(PyObjCPointer, type),
		READONLY,
		NULL
	},
	{
		"pointerAsInteger",
		T_INT,
		offsetof(PyObjCPointer, ptr),
		READONLY,
		NULL
	},
	{ 0, 0, 0, 0, 0 }
};

PyTypeObject PyObjCPointer_Type =
{
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"PyObjCPointer",			/* tp_name */
	sizeof (PyObjCPointer),			/* tp_basicsize */
	sizeof (char),				/* tp_itemsize */
  
	/* methods */
	PyObjCPointer_dealloc,			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	0,					/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,					/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	0,					/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
	"Wrapper around a Objective-C Pointer",	/* tp_doc */
	0,					/* tp_traverse */
	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	PyObjCPointer_methods,			/* tp_methods */
	PyObjCPointer_members,			/* tp_members */
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
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};

PyObjCPointer *
PyObjCPointer_New(void *p, const char *t)
{
	Py_ssize_t size = PyObjCRT_SizeOfType (t);
	const char *typeend = PyObjCRT_SkipTypeSpec (t);
	PyObjCPointer *self;

	NSLog(@"PyObjCPointer created: at %p of type %s", p, t);

	if (size == -1) {
		return NULL;
	}
	if (typeend == NULL) {
		return NULL;
	}
  
	self = PyObject_NEW_VAR (PyObjCPointer, &PyObjCPointer_Type, size);
	if (self == NULL) {
		return NULL;
	}

	self->type = PyString_FromStringAndSize ((char *) t, typeend-t);

	if (size && p) {
		memcpy ((self->ptr = self->contents), p, size);
	} else {
		self->ptr = p;
	}
  
	return self;
}
