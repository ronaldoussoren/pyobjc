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
	int len = PyTuple_Size(self->selectors);
	int i;

	for (i = 0; i < len; i++) {
		ObjCSelector* tmp =
			(ObjCSelector*)PyTuple_GET_ITEM(
				self->selectors, i);
		
		PyDict_DelItemString(selToProtocolMapping,
			SELNAME(tmp->sel_selector));
	}
#endif

	Py_XDECREF(self->selectors);
	object->ob_type->tp_free(object);
}

static PyObject*
proto_repr(PyObject* object)
{
	char buf[1024];

	PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)object;	

	snprintf(buf, sizeof(buf), "<%s %s at %p>",
		self->ob_type->tp_name, PyString_AsString(self->name),
		(void*)self);
	return PyString_FromString(buf);
}

static PyObject*
proto_new(PyTypeObject* type __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
static	char*	keywords[] = { "name", "selectors", "warnIfUndeclared", NULL };
	PyObjCInformalProtocol* result;
	PyObject* name;
	PyObject* selectors;
	int       i, len;
	int	  warnIfUndeclared = 1;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO|i:informal_protocol",
			keywords, &name, &selectors, &warnIfUndeclared)) { 
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

	result = (PyObjCInformalProtocol*)PyObject_New(
			PyObjCInformalProtocol, &PyObjCInformalProtocol_Type);

	result->name = name;
	result->selectors = selectors;

#if 1
	if (warnIfUndeclared) {
		len = PyTuple_Size(result->selectors);
		for (i = 0; i < len; i++) {
			if (!ObjCSelector_Check(
					PyTuple_GET_ITEM(selectors, i))) {
				PyErr_Format(PyExc_TypeError, 
					"Item %d is not a selector", i);
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
			ObjCSelector* tmp =
				(ObjCSelector*)PyTuple_GET_ITEM(selectors, i);
			
			PyDict_SetItemString(selToProtocolMapping,
				(char*)SELNAME(tmp->sel_selector),
				name);
		}
	}
#endif

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
        0                                       /* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
        , 0                                     /* tp_del */
#endif
};


/*
 * Find information about a selector in the protocol.
 *
 * Return NULL if no information can be found, but does not set an
 * exception.
 */
PyObject* 
PyObjCInformalProtocol_FindSelector(PyObject* obj, SEL selector)
{
	PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;	
	int i, len;
	PyObject* cur;
	PyObject* seq;

	if (!PyObjCInformalProtocol_Check(obj)) {
		ObjCErr_Set(PyExc_TypeError, 
			"First argument is not an objc.informal_protocol");
		return 0;
	}
	/* XXX: should use PySequence_Fast */
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

		if (ObjCSelector_Check(cur)) {
			if (ObjCSelector_Selector(cur) == selector) {
				Py_DECREF(seq);
				return cur;
			}
		}
	}
	Py_DECREF(seq);
	return NULL;
}

/*
 * Verify that 'cls' conforms to the informal protocol
 */
int	
PyObjCInformalProtocol_CheckClass(PyObject* obj, PyObject* cls)
{
	PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;	
	int i, len;
	PyObject* cur;
	PyObject* seq;

	if (!PyObjCInformalProtocol_Check(obj)) {
		ObjCErr_Set(PyExc_TypeError, 
			"First argument is not an objc.informal_protocol");
		return 0;
	}
	if (!PyObjCClass_Check(cls)) {
		ObjCErr_Set(PyExc_TypeError, 
			"Second argument is not an objc.objc_class");
		return 0;
	}
	seq = PySequence_Fast(self->selectors, "selector list not a sequence");
	if (seq == NULL) {
		return 0;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0; i < len; i++) {
		cur = PySequence_Fast_GET_ITEM(seq, i);
		if (cur == NULL) {
			continue;
		}

		if (ObjCSelector_Check(cur)) {
			SEL sel = ObjCSelector_Selector(cur);
			PyObject* m;

			m = PyObjCClass_FindSelector(cls, sel);
			if (m == NULL && ObjCSelector_Required(cur)) {
				ObjCErr_Set(PyExc_TypeError,
					"class %s does not implement protocol "
					"%s: no implementation for %s",
					((PyTypeObject*)cls)->tp_name,
					PyString_AsString(self->name),
					SELNAME(sel));
				Py_DECREF(seq);
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
					Py_DECREF(seq);
					return 0;
				}
			} else {
				PyErr_Clear();
			}
		}
	}
	Py_DECREF(seq);
	return 1;
}



/*
 * Given the failure mode of most protocol problems it might be better to
 * just generate an exception.
 */
int	
PyObjCInformalProtocol_Warnings(char* name, PyObject* clsDict, PyObject* protocols)
{
	PyObject* seq;
	int len, i;
	PyObject* keys;
	int  haveWarnings = 0;
	PyObject* protoMap;

	if (selToProtocolMapping == NULL) return 0;
	
	protoMap = PyDict_New();
	if (protoMap == NULL) {
		return -1;
	}

	if (!PyDict_Check(clsDict)) {
		PyErr_SetString(PyExc_TypeError, 
			"class dict is not a dictionary");
		Py_DECREF(protoMap);
		return -1;
	}
		

	/*
	 * protoMap will contain the protocol names as keys, this makes 
	 * checking protocols easier.
	 */
	seq = PySequence_Fast(protocols, "protocol list is not a sequence");
	if (seq == NULL) {
		Py_DECREF(protoMap);
		return -1;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0;i < len; i++) {
		PyObjCInformalProtocol* obj =
			(PyObjCInformalProtocol*)PySequence_Fast_GET_ITEM(
				seq, i);
		if (PyDict_SetItem(protoMap,  obj->name, (PyObject*)obj) < 0) {
			Py_DECREF(seq);
			Py_DECREF(protoMap);
			return -1;
		}  else {
			Py_INCREF(obj->name);
			Py_INCREF(obj);
		}
	}
	Py_DECREF(seq);
	seq = NULL;

	/*
	 * Actually perform the check.
	 */
	keys = PyDict_Keys(clsDict);
	if (keys == NULL) {
		Py_DECREF(protoMap);
		return -1;
	}

	seq = PySequence_Fast(keys, "Dict keys not a sequence!?");
	Py_DECREF(keys); keys = NULL;
	if (seq == NULL) {
		Py_DECREF(protoMap);
		return -1;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	for (i = 0;i < len; i++) {
		PyObject* o = PySequence_Fast_GET_ITEM(seq, i);
		PyObject* p;
		PyObject* q;

		q = PyDict_GetItem(clsDict, o);
		if (q == NULL) {
			PyErr_Clear();
			continue;
		}

		if (!ObjCSelector_Check(q)) {
			continue;
		}

		p = PyDict_GetItemString(selToProtocolMapping,
			(char*)SELNAME(((ObjCSelector*)q)->sel_selector));
		if (p == NULL) {
			PyErr_Clear();
			continue;
		}

		if ((q = PyDict_GetItem(protoMap, p)) == NULL) {
			/* Oops, we seem to be implementing a protocol
			 * without saying it.
			 */
			 char buf[1024];

			 snprintf(buf, sizeof(buf),
			 	"Class %s is implementing part of protocol %s "
				"without declaring this (method %s)",
				name, PyString_AS_STRING(p),
				PyString_AS_STRING(o));
			 haveWarnings = 1;
			 PyErr_Warn(PyObjCExc_ProtocolWarning, buf);
			 if (PyErr_Occurred()) {
				Py_DECREF(seq);
			 	Py_DECREF(protoMap);
				return -1;
			 }
		}
	}
	Py_DECREF(seq);

	Py_DECREF(protoMap);
	return 0;
}
