/*
 * Implementation of support type for informal protocols.
 *
 * See the module DOCSTR for more information.
 */
#include <Python.h>
#include "structmember.h"	/* needed for PyMemberDef */
#include "pyobjc.h"
#include "objc_support.h"

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
} ObjCInformalProtocol;



static void
proto_dealloc(PyObject* object)
{
	ObjCInformalProtocol* self = (ObjCInformalProtocol*)object;	

	Py_XDECREF(self->selectors);
	object->ob_type->tp_free(object);
}

static PyObject*
proto_repr(PyObject* object)
{
	char buf[1024];

	ObjCInformalProtocol* self = (ObjCInformalProtocol*)object;	

	snprintf(buf, sizeof(buf), "<%s %s at %p>",
		self->ob_type->tp_name, PyString_AsString(self->name),
		self);
	return PyString_FromString(buf);
}

static PyObject*
proto_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
static	char*	keywords[] = { "name", "selectors", NULL };
	ObjCInformalProtocol* result;
	PyObject* name;
	PyObject* selectors;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO:informal_protocol",
			keywords, &name, &selectors)) { 
		return NULL;
	}

	if (!PyString_Check(name)) {
		PyErr_SetString(PyExc_TypeError,
			"Name must be a string");
		return NULL;
	}

	if (!PySequence_Check(selectors)) {
		PyErr_SetString(PyExc_TypeError,
			"must provide list of selectors");
		return NULL;
	}

	selectors = PySequence_Tuple(selectors);
	if (selectors == NULL) {
		return NULL;
	}

	result = (ObjCInformalProtocol*)PyObject_New(
			ObjCInformalProtocol, &ObjCInformalProtocol_Type);

	result->name = name;
	result->selectors = selectors;

	Py_XINCREF(name);

	return (PyObject*)result;
}

static int proto_traverse(PyObject* self, visitproc visit, void* handle)
{
	ObjCInformalProtocol* me = (ObjCInformalProtocol*)self;	
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
		offsetof(ObjCInformalProtocol, name),
		READONLY,
		NULL
	},
	{
		"selectors",
		T_OBJECT,
		offsetof(ObjCInformalProtocol, selectors),
		READONLY,
		NULL
	},

	{ 0, 0, 0, 0, 0 }
};

PyTypeObject ObjCInformalProtocol_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.informal_protocol",		/* tp_name */
	sizeof(ObjCInformalProtocol),		/* tp_basicsize */
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
};


/*
 * Find information about a selector in the protocol.
 *
 * Return NULL if no information can be found, but does not set an
 * exception.
 */
PyObject* ObjCIPFindInfo(PyObject* obj, SEL selector)
{
	ObjCInformalProtocol* self = (ObjCInformalProtocol*)obj;	
	int i, len;
	PyObject* cur;

	if (!ObjCInformalProtocol_Check(obj)) {
		ObjCErr_Set(PyExc_TypeError, 
			"First argument is not an objc.informal_protocol");
		return 0;
	}
	len = PySequence_Length(self->selectors);
	for (i = 0; i < len; i++) {
		cur = PySequence_GetItem(self->selectors, i);
		if (cur == NULL) {
			PyErr_Print();
			continue;
		}

		if (ObjCSelector_Check(cur)) {
			if (ObjCSelector_Selector(cur) == selector) {
				return cur;
			}
		}

		Py_DECREF(cur);
	}
	return NULL;
}

/*
 * Verify that 'cls' conforms to the informal protocol
 */
int	ObjCIPVerify(PyObject* obj, PyObject* cls)
{
	ObjCInformalProtocol* self = (ObjCInformalProtocol*)obj;	
	int i, len;
	PyObject* cur;

	if (!ObjCInformalProtocol_Check(obj)) {
		ObjCErr_Set(PyExc_TypeError, 
			"First argument is not an objc.informal_protocol");
		return 0;
	}
	if (!PyObjCClass_Check(cls)) {
		ObjCErr_Set(PyExc_TypeError, 
			"Second argument is not an objc.objc_class");
		return 0;
	}

	len = PySequence_Length(self->selectors);
	for (i = 0; i < len; i++) {
		cur = PySequence_GetItem(self->selectors, i);
		if (cur == NULL) {
			PyErr_Print();
			continue;
		}

		if (ObjCSelector_Check(cur)) {
			SEL sel = ObjCSelector_Selector(cur);
			PyObject* m;

			m = PyObjCClass_FindSelector(cls, sel);
			if (m == NULL && ObjCSelector_Required(cur)) {
				PyErr_Print();
				ObjCErr_Set(PyExc_TypeError,
					"class %s does not implement protocol "
					"%s: no implementation for %s",
					((PyTypeObject*)cls)->tp_name,
					PyString_AsString(self->name),
					SELNAME(sel));
				Py_DECREF(cur);
				return 0;
			}
			if (m) {
				if (strcmp(ObjCSelector_Signature(m),
					ObjCSelector_Signature(cur)) != 0) {

					ObjCErr_Set(PyExc_TypeError,
						"class %s does not implement "
						"protocol %s: incorrect "
						"signature for method %s",
						((PyTypeObject*)cls)->tp_name,
						PyString_AsString(self->name),
						SELNAME(sel));
					Py_DECREF(cur);
					return 0;
				}
			} else {
				PyErr_Clear();
			}
		}

		Py_DECREF(cur);
	}
	return 1;
}
