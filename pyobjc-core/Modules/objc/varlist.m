#include "pyobjc.h"


typedef struct {
	PyObject_HEAD

	const char*	tp;
	void*		array;
	Py_ssize_t      itemsize;
} PyObjC_VarList;

PyDoc_STRVAR(object_as_tuple_doc,
	"as_tuple(count)\n"
	"\n"
	"Return a tuple containing the first ``count`` elements of "
	"this list"
);
static PyObject*
object_as_tuple(PyObject* _self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "length", NULL };

	PyObjC_VarList* self = (PyObjC_VarList*)_self;

	Py_ssize_t i, length;
	PyObject*  result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, Py_ARG_SIZE_T, keywords, &length)) {
		return NULL;
	}

	result = PyTuple_New(length);
	if (result == NULL) {
		return NULL;
	}

	for (i = 0; i < length; i++) {
		PyObject* v = pythonify_c_value(self->tp, ((unsigned char*)self->array) + (i * self->itemsize));
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		PyTuple_SET_ITEM(result, i, v);
	}
	return result;
}


static PyObject*
object__getitem__(PyObject* _self, Py_ssize_t idx)
{
	PyObjC_VarList* self = (PyObjC_VarList*)_self;
	
	return pythonify_c_value(self->tp, ((unsigned char*)self->array) + (idx * self->itemsize));
}

static PyObject*
object__getslice__(PyObject* _self, Py_ssize_t start, Py_ssize_t stop)
{
	PyObjC_VarList* self = (PyObjC_VarList*)_self;
	PyObject* result;
	Py_ssize_t idx;

	if (start < 0 || stop < 0) {
		PyErr_SetString(PyExc_ValueError,
			"objc.varlist doesn't support slices with negative indexes");
		return NULL;
	}
	if (stop < start) {
		stop = start;
	}

	result = PyTuple_New(stop - start);

	for (idx = start; idx < stop; idx++) {
		PyObject* v =  pythonify_c_value(
			self->tp, 
			((unsigned char*)self->array) + (idx * self->itemsize));
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		PyTuple_SET_ITEM(result, idx - start, v);
	}

	return result;
}

static int
object__setslice__(PyObject* _self, Py_ssize_t start, Py_ssize_t stop, PyObject*newval)
{
	PyObjC_VarList* self = (PyObjC_VarList*)_self;
	Py_ssize_t idx;
	PyObject* seq;

	if (start < 0 || stop < 0) {
		PyErr_SetString(PyExc_ValueError,
			"objc.varlist doesn't support slices with negative indexes");
		return -1;
	}
	if (stop < start) {
		stop = start;
	}

	seq = PySequence_Fast(newval, "New value must be sequence");
	if (seq == NULL) {
		return -1;
	}

	if (PySequence_Fast_GET_SIZE(seq) != stop - start) {
		PyErr_SetString(PyExc_ValueError,
		   "objc.varlist slice assignment doesn't support resizing");
		Py_DECREF(seq);
		return -1;
	}


	for (idx = start; idx < stop; idx++) {
		PyObject* v =  PySequence_Fast_GET_ITEM(seq, idx-start);
		int r = depythonify_c_value(
			self->tp, 
			v, 
			((unsigned char*)self->array) + (idx * self->itemsize));
		if (r == -1) {
			Py_DECREF(seq);
			return -1;
		}
	}
	Py_DECREF(seq);
	return 0;
}

/*
 * XXX: this might mess up reference counts if this is an array of objects,
 * but there's no rules about ownership in arbitrary arrays.
 */
static int
object__setitem__(PyObject* _self, Py_ssize_t idx, PyObject* value)
{
	PyObjC_VarList* self = (PyObjC_VarList*)_self;

	return depythonify_c_value(self->tp, value, ((unsigned char*)self->array) + (idx * self->itemsize));
}

static PySequenceMethods object_tp_as_list = {
	NULL,			/* sq_length */
	NULL,			/* sq_concat */
	NULL,			/* sq_repeat */
	object__getitem__,	/* sq_item */
	object__getslice__,	/* sq_slice */
	object__setitem__,	/* sq_ass_item */
	object__setslice__,	/* sq_ass_slice */
	NULL,			/* sq_contains */
	NULL,			/* sq_inplace_concat */
	NULL,			/* sq_inplace_repeat */
};


static PyObject* 
object_new(
	PyTypeObject* type __attribute__((__unused__)), 
	PyObject* args __attribute__((__unused__)), 
	PyObject* kwds __attribute__((__unused__)))
{
	PyErr_SetString(PyExc_TypeError, 
			"Cannot create instances of 'objc.varlist' in Python");
	return NULL;
}

static void
object_dealloc(PyObject* _self)
{
	PyObjC_VarList* self = (PyObjC_VarList*)_self;

	PyMem_Free((char*)(self->tp));
	PyObject_Del(_self);
}	

PyDoc_STRVAR(object_doc,
	"objc.varlist\n"
	"\n"
	"A list of an unspecified size. Use ``obj.as_tuple(count)`` to \n"
	"convertto a python tuple, or ``obj[index]`` to fetch a single item"
);

static PyMethodDef object_methods[] = {
        {
		"as_tuple",
		(PyCFunction)object_as_tuple,
		METH_VARARGS|METH_KEYWORDS,
		object_as_tuple_doc
	},

	{ 0, 0, 0, 0 }
};

PyTypeObject PyObjC_VarList_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.varlist",				/* tp_name */
	sizeof(PyObjC_VarList),			/* tp_basicsize */
	0,			 		/* tp_itemsize */
	/* methods */
	object_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	0,					/* tp_repr */
	0,					/* tp_as_number */
	&object_tp_as_list,			/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	PyObject_GenericGetAttr,		/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
 	object_doc,				/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0, 					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	object_methods,				/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	object_new,				/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
	0,                                      /* tp_bases */
	0,                                      /* tp_mro */
	0,                                      /* tp_cache */
	0,                                      /* tp_subclasses */
	0,                                      /* tp_weaklist */
	0                                       /* tp_del */
#if PY_VERSION_HEX >= 0x02060000
	, 0					/* tp_version_tag */
#endif

};

PyObject* 
PyObjC_VarList_New(const char* tp, void* array)
{
	PyObjC_VarList* result;

	tp  = PyObjCUtil_Strdup(tp);
	if (tp == NULL) {
		return NULL;
	}
	if (*tp == _C_VOID) {
		*(char*)tp = _C_CHAR_AS_TEXT;
	}
	result = PyObject_New(PyObjC_VarList, &PyObjC_VarList_Type);
	if (result == NULL) {
		return NULL;
	}
	result->tp = tp;
	result->array = array;
	result->itemsize = PyObjCRT_AlignedSize(tp);

	return (PyObject*)result;
}
