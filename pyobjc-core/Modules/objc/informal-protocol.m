/*
 * Implementation of support type for informal protocols.
 *
 * See the module DOCSTR for more information.
 */
#include "pyobjc.h"

PyDoc_STRVAR(proto_cls_doc,
"objc.informal_protocol(name, selector_list)\n"
"\n"
"This class can be used to specify which methods are supported by an informal\n"
"protocol. Instances of this type can by used while creating subclasses of \n"
"objective-C classes to automaticly specify method signatures et.al."
"");

typedef struct {
	PyObject_HEAD

	PyObject* name;
	PyObject* selectors;
} PyObjCInformalProtocol;


static PyObject* selToProtocolMapping = NULL;


static void
proto_dealloc(PyObject* object)
{
	PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)object;	
#if 0
	/*
	 * For some reason this code causes a crash, while it should
	 * be the reverse of the code in proto_new.
	 */
	Py_ssize_t len = PyTuple_Size(self->selectors);
	Py_ssize_t i;

	for (i = 0; i < len; i++) {
		PyObjCSelector* tmp =
			(PyObjCSelector*)PyTuple_GET_ITEM(
				self->selectors, i);
		
		PyDict_DelItemString(selToProtocolMapping,
			sel_getName(tmp->sel_selector));
	}
#endif

	Py_XDECREF(self->selectors);
	object->ob_type->tp_free(object);
}

static PyObject*
proto_repr(PyObject* object)
{
	PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)object;	

	return PyString_FromFormat("<%s %s at %p>", self->ob_type->tp_name, PyString_AsString(self->name), (void*)self);
}

static PyObject*
proto_new(PyTypeObject* type __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
static	char*	keywords[] = { "name", "selectors", NULL };
	PyObjCInformalProtocol* result;
	PyObject* name;
	PyObject* selectors;
	Py_ssize_t       i, len;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO:informal_protocol",
			keywords, &name, &selectors)) { 
		return NULL;
	}

	if (!PyString_Check(name)) {
		PyErr_SetString(PyExc_TypeError,
			"Name must be a string");
		return NULL;
	}

	selectors = PySequence_Tuple(selectors);
	if (selectors == NULL) {
		return NULL;
	}

	result = (PyObjCInformalProtocol*)PyObject_New(
			PyObjCInformalProtocol, &PyObjCInformalProtocol_Type);

	result->name = name;
	result->selectors = selectors;

	len = PyTuple_GET_SIZE(selectors);
	for (i = 0; i < len; i++) {
		if (!PyObjCSelector_Check(
				PyTuple_GET_ITEM(selectors, i))) {
			PyErr_Format(PyExc_TypeError, 
				"Item %"PY_FORMAT_SIZE_T"d is not a selector", i);
			Py_DECREF(result);
			return NULL;
		}
	}

	if (selToProtocolMapping == NULL) {
		selToProtocolMapping = PyDict_New();
		if (selToProtocolMapping == NULL) {
			Py_DECREF(result);
			return NULL;
		}
	}

	for (i = 0; i < len; i++) {
		PyObjCSelector* tmp =
			(PyObjCSelector*)PyTuple_GET_ITEM(selectors, i);
		
		PyDict_SetItemString(selToProtocolMapping,
			(char*)sel_getName(tmp->sel_selector),
			(PyObject*)result);
	}

	Py_XINCREF(name);

	return (PyObject*)result;
}

static int 
proto_traverse(PyObject* self, visitproc visit, void* handle)
{
	PyObjCInformalProtocol* me = (PyObjCInformalProtocol*)self;	
	int                   err;

	err = visit(me->name, handle);
	if (err) return err;
	err = visit(me->selectors, handle);	
	if (err) return err;
	return 0;
}

static PyMemberDef proto_members[] = {
	{
		"__name__",
		T_OBJECT,
		offsetof(PyObjCInformalProtocol, name),
		READONLY,
		NULL
	},
	{
		"selectors",
		T_OBJECT,
		offsetof(PyObjCInformalProtocol, selectors),
		READONLY,
		NULL
	},

	{ 0, 0, 0, 0, 0 }
};

PyTypeObject PyObjCInformalProtocol_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.informal_protocol",		/* tp_name */
	sizeof(PyObjCInformalProtocol),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	proto_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	proto_repr,				/* tp_repr */
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
 	proto_cls_doc,				/* tp_doc */
 	proto_traverse,				/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	proto_members,				/* tp_members */
	0, /* proto_getset , */			/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	proto_new,				/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
        0,                                      /* tp_bases */
        0,                                      /* tp_mro */
        0,                                      /* tp_cache */
        0,                                      /* tp_subclasses */
        0,                                      /* tp_weaklist */
        0                                       /* tp_del */
};


/*
 * Find information about a selector in the protocol.
 *
 * Return NULL if no information can be found, but does not set an
 * exception.
 */
PyObject* 
PyObjCInformalProtocol_FindSelector(PyObject* obj, SEL selector, int isClassMethod)
{
	PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;	
	Py_ssize_t i, len;
	PyObject* cur;
	PyObject* seq;

	if (!PyObjCInformalProtocol_Check(obj)) {
		PyErr_Format(PyExc_TypeError, 
			"First argument is not an 'objc.informal_protocol' "
			"but '%s'", obj->ob_type->tp_name);
		return 0;
	}

	seq = PySequence_Fast(self->selectors,"selector list not a sequence?");
	if (seq == NULL) {
		return 0;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0; i < len; i++) {
		cur = PySequence_Fast_GET_ITEM(self->selectors, i);
		if (cur == NULL) {
			continue;
		}

		if (PyObjCSelector_Check(cur)) {
			int class_sel = (
				PyObjCSelector_GetFlags(cur) 
				& PyObjCSelector_kCLASS_METHOD) != 0;
			if ((isClassMethod && !class_sel) 
					|| (!isClassMethod && class_sel)) {
				continue;
			}

			if (sel_isEqual(PyObjCSelector_GetSelector(cur), selector)) {
				Py_DECREF(seq);
				return cur;
			}
		}
	}
	Py_DECREF(seq);
	return NULL;
}

PyObject*
findSelInDict(PyObject* clsdict, SEL selector)
{
	PyObject* values;
	PyObject* seq;
	Py_ssize_t       i, len;

	values = PyDict_Values(clsdict);
	if (values == NULL) {
		return NULL;
	}

	seq = PySequence_Fast(values, "PyDict_Values result not a sequence");
	if (seq == NULL) {
		return NULL;
	}
	
	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0; i < len; i++) {
		PyObject* v = PySequence_Fast_GET_ITEM(seq, i);
		if (!PyObjCSelector_Check(v)) continue;
		if (PyObjCSelector_GetSelector(v) == selector) {
			Py_DECREF(seq);
			Py_DECREF(values);
			Py_INCREF(v);
			return v;
		}
	}
	Py_DECREF(seq);
	Py_DECREF(values);
	return NULL;
}

int 
signaturesEqual(char* sig1, char* sig2)
{
	char buf1[1024];
	char buf2[1024];
	int r;

	/* Return 0 if the two signatures are not equal */
	if (strcmp(sig1, sig2) == 0) return 1;

	/* For some reason compiler-generated signatures contain numbers that
	 * are not used by the runtime. These are irrelevant for our comparison
	 */
	r = PyObjCRT_SimplifySignature(sig1, buf1, sizeof(buf1));
	if (r == -1) { 
		return 0; 
	}

	r = PyObjCRT_SimplifySignature(sig2, buf2, sizeof(buf2));
	if (r == -1) { 
		return 0; 
	}
	return strcmp(buf1, buf2) == 0;
}

/*
 * Verify that 'cls' conforms to the informal protocol
 */
int	
PyObjCInformalProtocol_CheckClass(
	PyObject* obj, char* name, PyObject* super_class, PyObject* clsdict)
{
	PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;	
	Py_ssize_t i, len;
	PyObject* cur;
	PyObject* seq;

	if (!PyObjCInformalProtocol_Check(obj)) {
		PyErr_Format(PyExc_TypeError, 
			"First argument is not an 'objc.informal_protocol' "
			"but '%s'", obj->ob_type->tp_name);
		return 0;
	}
	if (!PyObjCClass_Check(super_class)) {
		PyErr_Format(PyExc_TypeError, 
			"Third argument is not an 'objc.objc_class' but "
			"'%s'", super_class->ob_type->tp_name);
		return 0;
	}
	if (!PyDict_Check(clsdict)) {
		PyErr_Format(PyExc_TypeError, 
			"Fourth argument is not a 'dict' but '%s'",
			clsdict->ob_type->tp_name);
		return 0;
	}

	seq = PySequence_Fast(self->selectors, "selector list not a sequence");
	if (seq == NULL) {
		return 0;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0; i < len; i++) {
		SEL sel;
		PyObject* m;

		cur = PySequence_Fast_GET_ITEM(seq, i);
		if (cur == NULL) {
			continue;
		}

		if (!PyObjCSelector_Check(cur)) {
			continue;
		}

		sel = PyObjCSelector_GetSelector(cur);

		m = findSelInDict(clsdict, sel);
		if (m == NULL) {
			m = PyObjCClass_FindSelector(super_class, sel, PyObjCSelector_IsClassMethod(cur));
		}

		if (m == NULL || !PyObjCSelector_Check(m)) {
			Py_XDECREF(m);
			if (PyObjCSelector_Required(cur)) {
				PyErr_Format(PyExc_TypeError,
					"class %s does not fully implement "
					"protocol %s: no implementation for %s",
					name,
					PyString_AsString(self->name),
					sel_getName(sel));
					Py_DECREF(seq);
				return 0;
			} else {
				PyErr_Clear();
			}
		} else {
			if (!signaturesEqual(PyObjCSelector_Signature(m),
				PyObjCSelector_Signature(cur)) != 0) {

				PyErr_Format(PyExc_TypeError,
					"class %s does not correctly implement "
					"protocol %s: "
					"the signature for method %s is "
					"%s instead of %s",
					name,
					PyString_AsString(self->name),
					sel_getName(sel),
					PyObjCSelector_Signature(m),
					PyObjCSelector_Signature(cur)
				);
				Py_DECREF(seq);
				Py_DECREF(m);
				return 0;
			}
			Py_DECREF(m);
		}
	}
	Py_DECREF(seq);
	return 1;
}

PyObject*
PyObjCInformalProtocol_FindProtocol(SEL selector)
{
	PyObject* item;

	if (selToProtocolMapping == NULL) return NULL;

	item = PyDict_GetItemString(selToProtocolMapping, (char*)sel_getName(selector));
	if (item != NULL) {
		return item;
	}

	PyErr_Clear();
	return NULL;
}
