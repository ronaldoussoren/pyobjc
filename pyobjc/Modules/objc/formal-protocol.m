/*
 * Implementation of support type for formal protocols.
 *
 * See the module DOCSTR for more information.
 */
#include "pyobjc.h"

struct Protocol_struct {
	@defs(Protocol);
};

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
	object->ob_type->tp_free(object);
}


static PyObject*
proto_repr(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	const char* name;

	name = [self->objc name];
	if (name == NULL) {
		name = "<nil>";
	}

	return PyString_FromFormat("<%s %s at %p>", self->ob_type->tp_name, name, (void*)self);
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
	const char* name = [self->objc name];

	if (name == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	return PyString_FromString(name);
}


static PyObject*
proto_new(PyTypeObject* type __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
static	char*	keywords[] = { "name", "supers", "selectors", NULL };
	PyObjCFormalProtocol* result = NULL;
	char* name;
	PyObject* supers;
	PyObject* selectors;
	int i, len;
	int numInstance = 0;
	int numClass = 0;
	struct Protocol_struct* theProtocol = NULL;
	struct objc_method_description* c;

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
		if (sel == NULL || !PyObjCSelector_Check(sel)) {
			PyErr_SetString(PyExc_TypeError,
				"selectors need to be a sequence of selectors");
			Py_DECREF(supers);
			Py_DECREF(selectors);
			return NULL;
		}
		if (PyObjCSelector_GetFlags(sel)&PyObjCSelector_kCLASS_METHOD) {
			numClass++;
		} else {
			numInstance++;
		}
	}

	/* Allocate the protocol with alloc+init, don't shortcut through
	 * malloc, that doesn't work.
	 */
	theProtocol = (struct Protocol_struct*)[[Protocol alloc] init];
	if (theProtocol == NULL) {
		PyErr_NoMemory();
		goto error;
	}

	theProtocol->protocol_name = strdup(name);
	if (theProtocol->protocol_name == NULL) {
		PyErr_NoMemory();
		goto error;
	}

	if (supers == Py_None) {
		theProtocol->protocol_list = NULL;
	} else {
		len = PySequence_Fast_GET_SIZE(supers);
		theProtocol->protocol_list = malloc(
			sizeof(struct objc_protocol_list) +
			(1+len) * sizeof(Protocol*));
		theProtocol->protocol_list->next = NULL;
		theProtocol->protocol_list->count = len;
		for (i = 0; i < len; i++) {
			PyObject* v = PySequence_Fast_GET_ITEM(supers, i);
			theProtocol->protocol_list->list[i] =
				PyObjCFormalProtocol_GetProtocol(v);
			if (theProtocol->protocol_list->list[i] == NULL) {
				goto error;
			}
		}
		theProtocol->protocol_list->list[i] = NULL;
	}

	if (numInstance != NULL) {
		theProtocol->instance_methods = malloc(
			sizeof(struct objc_method_description_list) +
			(1+numInstance)  * sizeof(struct objc_method_description));
		if (theProtocol->instance_methods == NULL) {
			PyErr_NoMemory();
			goto error;
		}
		theProtocol->instance_methods->count = 0;
	}
	if (numClass != NULL) {
		theProtocol->class_methods = malloc(
			sizeof(struct objc_method_description_list) + 
			(1+numClass)  * sizeof(struct objc_method_description));
		if (theProtocol->class_methods == NULL) {
			PyErr_NoMemory();
			goto error;
		}
		theProtocol->class_methods->count = 0;
	}

	len = PySequence_Fast_GET_SIZE(selectors);
	for (i = 0; i < len; i++) {
		PyObject* sel = PySequence_Fast_GET_ITEM(selectors, i);
		SEL theSel = PyObjCSelector_GetSelector(sel);
		char* theSignature = PyObjCSelector_Signature(sel);

		if (PyObjCSelector_GetFlags(sel)&PyObjCSelector_kCLASS_METHOD) {
			c = &(theProtocol->class_methods->list[
				theProtocol->class_methods->count++]);
			c->name = theSel;
			c->types = strdup(theSignature);
			if (c->types == NULL) goto error;
		} else {
			c = &(theProtocol->instance_methods->list[
				theProtocol->instance_methods->count++]);
			c->name = theSel;
			c->types = strdup(theSignature);
			if (c->types == NULL) goto error;
		}
	}

	if (theProtocol->instance_methods) {
		c = &(theProtocol->instance_methods->list[
			theProtocol->instance_methods->count]);
		c->name = NULL;
		c->types = NULL;
	}

	if (theProtocol->class_methods) {
		c = &(theProtocol->class_methods->list[
			theProtocol->class_methods->count]);
		c->name = NULL;
		c->types = NULL;
	}


	result = (PyObjCFormalProtocol*)PyObject_New(
			PyObjCFormalProtocol, &PyObjCFormalProtocol_Type);
	if (result == NULL) goto error;

	Py_DECREF(selectors);
	Py_DECREF(supers);

	result->objc = (Protocol*)theProtocol;
	PyObjC_RegisterPythonProxy(result->objc, (PyObject*)result);
	return (PyObject*)result;

error:
	Py_DECREF(selectors);
	Py_DECREF(supers);

	if (theProtocol == NULL) return NULL;

	if (theProtocol->protocol_name != NULL) {
		free(theProtocol->protocol_name);
	}

	if (theProtocol->protocol_list != NULL) {
		free(theProtocol->protocol_list);
	}

	if (theProtocol->instance_methods != NULL) {
		for (i = 0; i < theProtocol->instance_methods->count; i++) {
			c = theProtocol->instance_methods->list + i;
			if (c->name) {
				free(c->name);
			}
		}
		free(theProtocol->instance_methods);
	}

	if (theProtocol->class_methods != NULL) {
		for (i = 0; i < theProtocol->class_methods->count; i++) {
			c = theProtocol->class_methods->list + i;
			if (c->name) {
				free(c->name);
			}
		}
		free(theProtocol->class_methods);
	}
	return NULL;
}

static PyObject*
proto_name(PyObject* object)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	const char* name = [self->objc name];

	if (name == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	return PyString_FromString(name);
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

	if ([self->objc conformsTo:objc_protocol]) {
		return PyBool_FromLong(1);
	} else {
		return PyBool_FromLong(0);
	}
}

static PyObject*
descriptionForInstanceMethod_(PyObject* object, PyObject* sel)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	SEL aSelector = NULL;
	struct objc_method_description* descr;

	if (PyObjCSelector_Check(sel)) {
		aSelector = PyObjCSelector_GetSelector(sel);
	} else if (PyString_Check(sel)) {
		char* s = PyString_AsString(sel);
		if (*s == '\0') {
			PyErr_SetString(PyExc_ValueError, 
					"empty selector name");
			return NULL;
		}

		aSelector = PyObjCRT_SELUID(s);
	} else {
		PyErr_Format(PyExc_TypeError, "expecting a SEL, got instance of %s",
				sel->ob_type->tp_name);
		return NULL;
	}

	descr = [self->objc descriptionForInstanceMethod:aSelector];
	if (descr == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	} else {
		return Py_BuildValue("(ss)",
			PyObjCRT_SELName(descr->name),
			descr->types);
	}
}

static PyObject*
descriptionForClassMethod_(PyObject* object, PyObject* sel)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;	
	SEL aSelector = NULL;
	struct objc_method_description* descr;

	if (PyObjCSelector_Check(sel)) {
		aSelector = PyObjCSelector_GetSelector(sel);
	} else if (PyString_Check(sel)) {
		char* s = PyString_AsString(sel);
		if (*s == '\0') {
			PyErr_SetString(PyExc_ValueError, 
					"empty selector name");
			return NULL;
		}

		aSelector = PyObjCRT_SELUID(s);
	}

	descr = [self->objc descriptionForClassMethod:aSelector];
	if (descr == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	} else {
		return Py_BuildValue("(ss)",
			PyObjCRT_SELName(descr->name),
			descr->types);
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
	{ 0, 0, 0, 0 }
};

static PyGetSetDef proto_getset[] = {
	{
		"X__class__",
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
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
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
	struct objc_method_description* descr;

	if (isClassMethod) {
		descr = [self->objc descriptionForClassMethod: selector];
	} else {
		descr = [self->objc descriptionForInstanceMethod: selector];
	}
	if (descr) {
		return descr->types;
	}
	return NULL;
}

static int 
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


extern PyObject* findSelInDict(PyObject* clsdict, SEL selector);
extern int signaturesEqual(char* sig1, char* sig2);


static int
do_verify(
	const char* protocol_name, 
	struct objc_method_description* descr, 
	int is_class __attribute__((__unused__)), 
	char* name,
	PyObject* super_class, 
	PyObject* clsdict)
{
	PyObject* meth;

	/* TODO: take classmethodness into account */

	meth = findSelInDict(clsdict, descr->name);
	if (meth == NULL || !PyObjCSelector_Check(meth)) {

		meth = PyObjCClass_FindSelector(super_class, descr->name);
		if (meth == NULL || !PyObjCSelector_Check(meth)) {
			PyErr_Format(PyExc_TypeError,
				"class %s does not full implement protocol "
				"%s: no implementation for %s",
				name,
				protocol_name,
				PyObjCRT_SELName(descr->name));
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
		PyObjCRT_SELName(descr->name),
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
    PyObject* clsdict)
{
	struct Protocol_struct* cur; 
	int i, r;

	cur = (struct Protocol_struct*)protocol;

	if (cur->protocol_list) {
		for (i = 0; i < cur->protocol_list->count; i++) {
			r = do_check(protocol_name, cur->protocol_list->list[i], name, super_class, clsdict);
			if (r == 0) return r;
		}
	}

	if (cur->instance_methods) {
		for (i = 0; i < cur->instance_methods->count; i++) {
			if (!do_verify(protocol_name, cur->instance_methods->list + i, 0, name, super_class, clsdict)) {
				return 0;
			}
		}
	} 
	if (cur->class_methods) {
		for (i = 0; i < cur->class_methods->count; i++) {
			if (!do_verify(protocol_name, cur->class_methods->list + i, 1, name, super_class, clsdict)) {
				return 0;
			}
		}
	} 
	return 1;
}

int	
PyObjCFormalProtocol_CheckClass(
	PyObject* obj, char* name, PyObject* super_class, PyObject* clsdict)
{
	PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)obj;	

	if (!PyObjCFormalProtocol_Check(obj)) {
		PyErr_Format(PyExc_TypeError,
			"First argument is not an 'objc.formal_protocol' but "
			"'%s'", obj->ob_type->tp_name);
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

	return do_check([self->objc name], self->objc, name, super_class, clsdict);
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
			"Expecting objc.formal_protocol, got %s",
			self->ob_type->tp_name);
		return NULL;
	}

	return self->objc;
}
