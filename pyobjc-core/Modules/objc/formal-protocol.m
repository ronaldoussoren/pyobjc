/*
 * Implementation of support type for formal protocols.
 *
 * See the module DOCSTR for more information.
 *
 * XXX: 
 * - deal with optional methods (new in ObjC 2.0)
 * - creating new protocols isn't actually supported in ObjC 2.0
 */
#include "pyobjc.h"

PyDoc_STRVAR(proto_cls_doc,
"objc.formal_protocol(name, supers, selector_list)\n"
"\n"
"This class is used to proxy Objective-C formal protocols, and can also be \n"
"used to define new formal protocols.\n"
"");

typedef struct {
	PyObject_HEAD

	Protocol* objc;
} PyObjCFormalProtocol;


static void
proto_dealloc(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	PyObjC_UnregisterPythonProxy(self->objc, object);
	Py_TYPE(object)->tp_free(object);
}


static PyObject*
proto_repr(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	const char* name;

	name = protocol_getName(self->objc);
	if (name == NULL) {
		name = "<nil>";
	}

	return PyText_FromFormat("<%s %s at %p>", Py_TYPE(self)->tp_name, name, (void*)self);
}

static PyObject*
proto_get__class__(PyObject* object __attribute__((__unused__)), void* closure __attribute__((__unused__)))
{
	return PyObjCClass_New([Protocol class]);
}

static PyObject*
proto_get__name__(PyObject* object, void* closure __attribute__((__unused__)))
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	const char* name = protocol_getName(self->objc);

	if (name == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	return PyText_FromString(name);
}


static PyObject*
proto_new(PyTypeObject* type __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
static	char*	keywords[] = { "name", "supers", "selectors", NULL };
	char* name;
	PyObject* supers;
	PyObject* selectors;
	Py_ssize_t i, len;

	PyObjCFormalProtocol* result = NULL;
	Protocol* theProtocol;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sOO:formal_protocol",
			keywords, &name, &supers, &selectors)) { 
		return NULL;
	}

	if (supers != Py_None) {
		supers = PySequence_Fast(supers, "supers need to be a sequence of objc.formal_protocols");
		if (supers == NULL) return NULL;
		len = PySequence_Fast_GET_SIZE(supers);
		for (i = 0; i < len; i++) {
			PyObject* v = PySequence_Fast_GET_ITEM(supers, i);
			if (!PyObjCFormalProtocol_Check(v)) {
				PyErr_SetString(PyExc_TypeError, "supers need to be a sequence of objc.formal_protocols");
				Py_DECREF(supers);
				return NULL;
			}
		}

	} else {
		Py_INCREF(supers);
	}

	selectors = PySequence_Fast(selectors, "selectors need to be a sequence of selectors");
	if (selectors == NULL) {
		Py_DECREF(supers);
		return NULL;
	}

	len = PySequence_Fast_GET_SIZE(selectors);
	for (i = 0; i < len; i++) {
		PyObject* sel = PySequence_Fast_GET_ITEM(selectors, i);
		if (!PyObjCSelector_Check(sel)) {
			PyErr_SetString(PyExc_TypeError, "Selectors is not a list of selectors");
			Py_DECREF(supers);
			return NULL;
		}
	}


	if (objc_allocateProtocol == NULL) {
		/* Protocol creation API is new in OSX 10.7, can will be weak-linked when
		 * building on OSX 10.7 with a 10.6 deployment target.
		 */
		Py_DECREF(selectors);
		PyErr_SetString(PyObjCExc_Error, "Cannot create formal protocols on this platform");
		return NULL;
	}

	theProtocol = objc_allocateProtocol(name);
	if (theProtocol == NULL) {
		PyErr_NoMemory();
		goto error;
	}

	if (supers != Py_None) {
		len = PySequence_Fast_GET_SIZE(supers);
		for (i = 0; i < len; i++) {
			PyObject* v = PySequence_Fast_GET_ITEM(supers, i);
			protocol_addProtocol(theProtocol, PyObjCFormalProtocol_GetProtocol(v));
		}
	}


	len = PySequence_Fast_GET_SIZE(selectors);
	for (i = 0; i < len; i++) {
		PyObject* sel = PySequence_Fast_GET_ITEM(selectors, i);
		SEL theSel = PyObjCSelector_GetSelector(sel);
		const char* theSignature = PyObjCSelector_Signature(sel);
		if (theSignature == NULL) {
			goto error;
		}
		protocol_addMethodDescription(
			theProtocol, 
			theSel, 
			theSignature, 
			(BOOL)PyObjCSelector_Required(sel), 
			PyObjCSelector_IsClassMethod(sel)?NO:YES);
	}

	objc_registerProtocol(theProtocol);

	result = (PyObjCFormalProtocol*)PyObject_New(
			PyObjCFormalProtocol, &PyObjCFormalProtocol_Type);
	if (result == NULL) goto error;

	Py_DECREF(selectors);
	Py_DECREF(supers);

	result->objc = theProtocol;
	PyObjC_RegisterPythonProxy(result->objc, (PyObject*)result);
	return (PyObject*)result;

error:
	Py_DECREF(selectors);
	Py_DECREF(supers);

	return NULL;
}

static PyObject*
proto_name(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	const char* name = protocol_getName(self->objc);

	if (name == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	return PyText_FromString(name);
}

static PyObject*
proto_conformsTo_(PyObject* object, PyObject* args)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	PyObject* protocol;
	Protocol* objc_protocol;

	if (!PyArg_ParseTuple(args, "O", &protocol)) {
		return NULL;
	}

	if (!PyObjCFormalProtocol_Check(protocol)) {
		PyErr_SetString(PyExc_TypeError, "Expecting a formal protocol");
		return NULL;
	}
	objc_protocol = PyObjCFormalProtocol_GetProtocol(protocol);

	if (protocol_conformsToProtocol(self->objc, objc_protocol)) {
		return PyBool_FromLong(1);
	} else {
		return PyBool_FromLong(0);
	}
}

static int
append_method_list(PyObject* lst, Protocol* protocol, BOOL isRequired, BOOL isInstance)
{
	struct objc_method_description * methods;
	unsigned int method_count, i;


	methods = protocol_copyMethodDescriptionList(protocol, isRequired, isInstance, &method_count);
	if (!methods) {
		return 0;
	}

	for (i = 0; i < method_count; i++) {
		char buf[512];
		PyObjCRT_SimplifySignature(methods[i].types, buf, sizeof(buf));
		PyObject* item = Py_BuildValue(
#if PY_MAJOR_VERSION == 2
			"{sssssO}",
#else
			"{sysysO}",
#endif
			"selector", sel_getName(methods[i].name),
			"typestr",  buf,
			"required", isRequired?Py_True:Py_False);
		if (item == NULL) {
			free(methods);
			return -1;
		}
		if (PyList_Append(lst, item) < 0) {
			Py_DECREF(item);
			free(methods);
			return -1;
		}
		Py_DECREF(item);
	}

	free(methods);
	return 0;
}


static PyObject* 
instanceMethods(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	int r;

	PyObject* result = PyList_New(0);
	if (result == NULL) {
		return NULL;
	}

	r = append_method_list(result, self->objc, YES, YES);
	if (r == -1) {
		Py_DECREF(result);
		return NULL;
	}

	r = append_method_list(result, self->objc, NO, YES);
	if (r == -1) {
		Py_DECREF(result);
		return NULL;
	}

	return result;

}

static PyObject* 
classMethods(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	int r;

	PyObject* result = PyList_New(0);
	if (result == NULL) {
		return NULL;
	}

	r = append_method_list(result, self->objc, YES, NO);
	if (r == -1) {
		Py_DECREF(result);
		return NULL;
	}

	r = append_method_list(result, self->objc, NO, NO);
	if (r == -1) {
		Py_DECREF(result);
		return NULL;
	}

	return result;

}

static PyObject*
descriptionForInstanceMethod_(PyObject* object, PyObject* sel)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	SEL aSelector = NULL;
	struct objc_method_description descr;

	if (PyObjCSelector_Check(sel)) {
		aSelector = PyObjCSelector_GetSelector(sel);
#if PY_MAJOR_VERSION == 2
	} else if (PyUnicode_Check(sel)) {
		PyObject* bytes = PyUnicode_AsEncodedString(sel, NULL, NULL);
		if (bytes == NULL) {
			return NULL;
		}
		char* s = PyBytes_AsString(bytes);
		if (s == NULL || *s == '\0') {
			PyErr_SetString(PyExc_ValueError, 
					"empty selector name");
			return NULL;
		}

		aSelector = sel_getUid(s);
		Py_DECREF(bytes);

#endif
	} else if (PyBytes_Check(sel)) {
		char* s = PyBytes_AsString(sel);
		if (*s == '\0') {
			PyErr_SetString(PyExc_ValueError, 
					"empty selector name");
			return NULL;
		}

		aSelector = sel_getUid(s);
	} else {
		PyErr_Format(PyExc_TypeError, "expecting a SEL, got instance of '%s'",
				Py_TYPE(sel)->tp_name);
		return NULL;
	}

	descr = protocol_getMethodDescription(self->objc, aSelector, YES, YES);
	if (descr.name == NULL) {
		descr = protocol_getMethodDescription(self->objc, aSelector, NO, YES);
	}

	if (descr.name == NULL) {
		Py_INCREF(Py_None);
		return Py_None;

	} else {
		char buf[512];
		PyObjCRT_SimplifySignature(descr.types, buf, sizeof(buf));
		return Py_BuildValue(
#if PY_MAJOR_VERSION == 2
			"(ss)",
#else
			"(yy)",
#endif
			sel_getName(descr.name),
			buf);
	}
}

static PyObject*
descriptionForClassMethod_(PyObject* object, PyObject* sel)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	SEL aSelector = NULL;
	struct objc_method_description descr;

	if (PyObjCSelector_Check(sel)) {
		aSelector = PyObjCSelector_GetSelector(sel);
#if PY_MAJOR_VERSION == 2
	} else if (PyUnicode_Check(sel)) {
		PyObject* bytes = PyUnicode_AsEncodedString(sel, NULL, NULL);
		if (bytes == NULL) {
			return NULL;
		}
		char* s = PyBytes_AsString(bytes);
		if (s == NULL || *s == '\0') {
			PyErr_SetString(PyExc_ValueError, 
					"empty selector name");
			return NULL;
		}

		aSelector = sel_getUid(s);
		Py_DECREF(bytes);

#endif
	} else if (PyBytes_Check(sel)) {
		char* s = PyBytes_AsString(sel);
		if (*s == '\0') {
			PyErr_SetString(PyExc_ValueError, 
					"empty selector name");
			return NULL;
		}

		aSelector = sel_getUid(s);
	} else {
		PyErr_Format(PyExc_TypeError, "expecting a SEL, got instance of '%s'",
				Py_TYPE(sel)->tp_name);
		return NULL;
	}

	descr = protocol_getMethodDescription(self->objc, aSelector, YES, NO);
	if (descr.name == NULL) {
		descr = protocol_getMethodDescription(self->objc, aSelector, NO, NO);
	}
	if (descr.name == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	} else {
		char buf[256];
		PyObjCRT_SimplifySignature(descr.types, buf, sizeof(buf));
		return Py_BuildValue(
#if PY_MAJOR_VERSION == 2
			"(ss)",
#else
			"(yy)",
#endif
			sel_getName(descr.name),
			buf);
	}
}

static PyMethodDef proto_methods[] = {
	{
		"name",
		(PyCFunction)proto_name,
		METH_NOARGS,
		"Return the  protocol name",
	},
	{
		"conformsTo_",
		(PyCFunction)proto_conformsTo_,
		METH_VARARGS,
		"Does this protocol conform to another protocol"
	},
	{
		"descriptionForInstanceMethod_",
		(PyCFunction)descriptionForInstanceMethod_,
		METH_O,
		"Description for an instance method in the protocol"
	},
	{
		"descriptionForClassMethod_",
		(PyCFunction)descriptionForClassMethod_,
		METH_O,
		"Description for a class method in the protocol"
	},
	{
		"instanceMethods",
		(PyCFunction)instanceMethods,
		METH_NOARGS,
		"List of instance methods in this protocol"
	},
	{
		"classMethods",
		(PyCFunction)classMethods,
		METH_NOARGS,
		"List of class methods in this protocol"
	},
	{ 0, 0, 0, 0 }
};

static PyGetSetDef proto_getset[] = {
	{
		"__class__",
		(getter)proto_get__class__,
		NULL,
		NULL,
		0
	},
	{
		"__name__",
		(getter)proto_get__name__,
		NULL,
		NULL,
		0
	},
	{ NULL, NULL, NULL, NULL, 0 }
};

PyTypeObject PyObjCFormalProtocol_Type = {
	PyVarObject_HEAD_INIT(&PyType_Type, 0)
	"objc.formal_protocol",			/* tp_name */
	sizeof(PyObjCFormalProtocol),		/* tp_basicsize */
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
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	proto_methods,				/* tp_methods */
	0,					/* tp_members */
	proto_getset,				/* tp_getset */
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
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};


/*
 * Find information about a selector in the protocol.
 *
 * Return NULL if no information can be found, but does not set an
 * exception.
 */
const char* 
PyObjCFormalProtocol_FindSelectorSignature(PyObject* object, SEL selector, int isClassMethod)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	struct objc_method_description descr;

	descr = protocol_getMethodDescription(self->objc, selector, YES, !isClassMethod);
	if (descr.name != NULL) {
		return descr.types;
	}
	descr = protocol_getMethodDescription(self->objc, selector, NO, !isClassMethod);
	if (descr.name != NULL) {
		return descr.types;
	}
	return NULL;
}

static int
do_verify(
	const char* protocol_name, 
	struct objc_method_description* descr, 
	BOOL is_class, 
	BOOL is_required,
	char* name,
	PyObject* super_class, 
	PyObject* clsdict, PyObject* metadict)
{
	PyObject* meth;

	if (is_class) {
		meth = findSelInDict(metadict, descr->name);
	} else {
		meth = findSelInDict(clsdict, descr->name);
	}
	if (meth == NULL || !PyObjCSelector_Check(meth)) {
		
		meth = PyObjCClass_FindSelector(super_class, descr->name, is_class);
		if (meth == NULL || !PyObjCSelector_Check(meth)) {
			if (is_required) {
				PyErr_Format(PyExc_TypeError,
					"class %s does not full implement protocol "
					"%s: no implementation for %s",
					name,
					protocol_name,
					sel_getName(descr->name));
				return 0;
			} else {
				/* Method is not required, ignore */
				return 1;
			}
		}
	}

	if (is_class) {
		if (!PyObjCSelector_IsClassMethod(meth)) {
			PyErr_Format(PyExc_TypeError,
				"class %s does not correctly implement "
				"protocol %s: method %s is not a "
				"class method",
				name,
				protocol_name,
				sel_getName(descr->name)
			);
			return 0;
		}
	} else {
		if (PyObjCSelector_IsClassMethod(meth)) {
			PyErr_Format(PyExc_TypeError,
				"class %s does not correctly implement "
				"protocol %s: method %s is not an "
				"instance method",
				name,
				protocol_name,
				sel_getName(descr->name)
			);
			return 0;
		}
	}

	if (signaturesEqual(descr->types, 
				PyObjCSelector_Signature(meth))) {
		return 1;
	} 

	PyErr_Format(PyExc_TypeError,
		"class %s does not correctly implement "
		"protocol %s: the signature for method %s "
		"is %s instead of %s",
		name,
		protocol_name,
		sel_getName(descr->name),
		PyObjCSelector_Signature(meth),
		descr->types);
	return 0;
}

static int
do_check(
    const char* protocol_name,
    Protocol* protocol, 
    char* name, 
    PyObject* super_class, 
    PyObject* clsdict,
    PyObject* metadict)
{
	int r;
	unsigned idx;

	unsigned parentCount;
	Protocol** parents = protocol_copyProtocolList(protocol, &parentCount);
	if (parents) {
		for (idx = 0; idx < parentCount; idx++) {
			r = do_check(protocol_name, parents[idx], name, super_class, clsdict, metadict);
			if (r == 0) {
				free(parents);
				return r;
			}
		}
		free(parents);
	}

	unsigned int methCount;
	struct objc_method_description* methinfo;

	methCount = 0;
	methinfo = protocol_copyMethodDescriptionList(protocol, YES, YES, &methCount);
	if (methinfo) {
		for (idx = 0; idx < methCount; idx++) {
			if (!do_verify(protocol_name, methinfo + idx, NO, YES, name, super_class, clsdict, metadict)) {
				free(methinfo);
				return 0;
			}
		}
		free(methinfo);
	}

	methinfo = protocol_copyMethodDescriptionList(protocol, NO, YES, &methCount);
	if (methinfo) {
		for (idx = 0; idx < methCount; idx++) {
			if (!do_verify(protocol_name, methinfo + idx, NO, NO, name, super_class, clsdict, metadict)) {
				free(methinfo);
				return 0;
			}
		}
		free(methinfo);
	}

	methinfo = protocol_copyMethodDescriptionList(protocol, YES, NO, &methCount);
	if (methinfo) {
		for (idx = 0; idx < methCount; idx++) {
			if (!do_verify(protocol_name, methinfo + idx, YES, YES, name, super_class, clsdict, metadict)) {
				free(methinfo);
				return 0;
			}
		}
		free(methinfo);
	}

	methinfo = protocol_copyMethodDescriptionList(protocol, NO, NO, &methCount);
	if (methinfo) {
		for (idx = 0; idx < methCount; idx++) {
			if (!do_verify(protocol_name, methinfo + idx, YES, NO, name, super_class, clsdict, metadict)) {
				free(methinfo);
				return 0;
			}
		}
		free(methinfo);
	}

	return 1;
}

int	
PyObjCFormalProtocol_CheckClass(
	PyObject* obj, char* name, PyObject* super_class, PyObject* clsdict, PyObject* metadict)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)obj;	

	if (!PyObjCFormalProtocol_Check(obj)) {
		PyErr_Format(PyExc_TypeError,
			"First argument is not an 'objc.formal_protocol' but "
			"'%s'", Py_TYPE(obj)->tp_name);
		return 0;
	}
	if (!PyObjCClass_Check(super_class)) {
		PyErr_Format(PyExc_TypeError,
			"Third argument is not an 'objc.objc_class' but "
			"'%s'", Py_TYPE(super_class)->tp_name);
		return 0;
	}
	if (!PyDict_Check(clsdict)) {
		PyErr_Format(PyExc_TypeError,
			"Fourth argument is not a 'dict' but '%s'",
			Py_TYPE(clsdict)->tp_name);
		return 0;
	}

	return do_check(protocol_getName(self->objc), self->objc, name, super_class, clsdict, metadict);
}

PyObject* PyObjCFormalProtocol_ForProtocol(Protocol* protocol)
{
	PyObjCFormalProtocol* result;

	result = (PyObjCFormalProtocol*)PyObject_New(
			PyObjCFormalProtocol, &PyObjCFormalProtocol_Type);
	if (result == NULL) {
		return NULL;
	}

	result->objc = protocol;
	PyObjC_RegisterPythonProxy(result->objc, (PyObject*)result);
	return (PyObject*)result;
}

Protocol* PyObjCFormalProtocol_GetProtocol(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	

	if (!PyObjCFormalProtocol_Check(self)) {
		PyErr_Format(PyExc_TypeError, 
			"Expecting objc.formal_protocol, got instance of '%s'",
			Py_TYPE(self)->tp_name);
		return NULL;
	}

	return self->objc;
}
