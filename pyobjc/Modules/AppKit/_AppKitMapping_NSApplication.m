/*
 * NSModalSession support
 *
 * NSModalSession are opaque values, the 'pointer' attribute is provided to be 
 * able to check if two NSModalSessions are actually the same.
 */

typedef struct SessionWrapper {
	PyObject_HEAD
	NSModalSession* ptr;
} SessionWrapper;

static PyObject* 
Session_pointer_get(
	SessionWrapper* self, 
	void* closure __attribute__((__unused__)))
{
	return PyInt_FromLong((long)self->ptr);
}

static PyObject* 
Session_new(PyTypeObject* type __attribute__((__unused__)),
	PyObject* args __attribute__((__unused__)), 
	PyObject* kwds __attribute__((__unused__)))
{
	PyErr_SetString(PyExc_TypeError, "Cannot create NSModalSession objects");
	return NULL;
}

static void
Session_dealloc(PyObject* self)
{
	PyObject_Del(self);
}



static PyGetSetDef Session_getset[] = {
	{
		"pointer",
		(getter)Session_pointer_get,
		NULL,
		NULL,
		NULL
	},
	{
		NULL,
		NULL,
		NULL,
		NULL,
		NULL
	}
};

PyTypeObject SessionWrapper_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"NSModalSession",			/* tp_name */
	sizeof(SessionWrapper),			/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	Session_dealloc, 			/* tp_dealloc */
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
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,			/* tp_flags */
 	0,					/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	0,					/* tp_members */
	Session_getset,				/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	Session_new,				/* tp_new */
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

#define SessionWrapper_Check(obj) PyObject_TypeCheck((obj), &SessionWrapper_Type)


/* This should do for now, although we should generate a new type for this */
static PyObject* 
NSModalSession_New(void* ptr __attribute__((__unused__)))
{
	SessionWrapper* res;

	res  = PyObject_New(SessionWrapper, &SessionWrapper_Type);
	if (res == NULL) {
		return NULL;
	}
	res->ptr = ptr;
	return (PyObject*)res;
}

static int 
NSModalSession_Convert(PyObject* value, void* pSessionPtr)
{
	if (SessionWrapper_Check(value)) {
		*(void**)pSessionPtr = ((SessionWrapper*)value)->ptr;
		return 0;
	}
	PyErr_SetString(PyExc_ValueError, "Require NSModalSession object");
	return -1;
}

static int 
_pyobjc_install_NSApplication(void)
{
	int r = 0;

	r = PyObjCPointerWrapper_Register(@encode(NSModalSession), 
		NSModalSession_New, NSModalSession_Convert);
	if (r == -1) return -1;

	return 0;
}
