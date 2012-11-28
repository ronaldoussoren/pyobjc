#include "pyobjc.h"

/*
 * descriptor objc_ivar
 *
 * We start of with a descriptor object that allows the user to access 
 * (read and write) objective-C instance variables. 
 *
 * These descriptors are used in two places:
 * 1) the wrapper for objective-C classes and objects use these to provide
 *    access to existing instance variables
 * 2) the user can define new instance variables (most likely 'outlets') when
 *    defining subclasses of objective-C classes.
 */

static void
ivar_dealloc(PyObject* _ivar)
{
	PyObjCInstanceVariable* ivar = (PyObjCInstanceVariable*)_ivar;
	if (ivar->name) {
		PyMem_Free(ivar->name);
	}
	PyMem_Free(ivar->type);
	Py_TYPE(ivar)->tp_free((PyObject*)ivar);
}

static PyObject*
ivar_repr(PyObject* _self)
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	if (self->isOutlet) {
		if (self->name) {
			return PyText_FromFormat("<IBOutlet %s>", self->name);
		} else {
			return PyText_FromString("<IBOutlet>");
		}
	} else {
		if (self->name) {
			return PyText_FromFormat("<instance-variable %s>", self->name);
		} else {
			return PyText_FromString("<instance-variable>");
		}
	}
}

static PyObject*
ivar_descr_get(PyObject* _self, PyObject* obj, PyObject* type __attribute__((__unused__)))
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	Ivar var;
	id   objc;
	PyObject* res;

	if (!obj || PyObjCClass_Check(obj)) {
		PyErr_SetString(PyExc_TypeError,
			"Cannot access Objective-C instance-variables "
			"through class");
		return NULL;
	}

	if (!PyObjCObject_Check(obj)) {
		PyErr_SetString(PyExc_TypeError, 
		    "objc_ivar descriptor on a non-objc object");
		return NULL;
	}
	objc = PyObjCObject_GetObject(obj);
	if (objc == NULL) {
		PyErr_SetString(PyExc_TypeError,
		   "Cannot access Objective-C instance-variables of NULL");
		return NULL;
	}

	if (self->name == NULL) {
		PyErr_SetString(PyExc_TypeError,
			"Using unnamed instance variable");
		return NULL;
	}

	var = class_getInstanceVariable(
			object_getClass(objc), self->name);
	if (var == NULL) {
		PyErr_SetString(PyExc_RuntimeError, 
		    "objc_ivar descriptor for non-existing instance variable");
		return NULL;
	}	

	if (self->isSlot) {
		res = *(PyObject**)(((char*)objc) + ivar_getOffset(var));

		if (res == NULL) {
			PyErr_Format(PyExc_AttributeError,
				"No attribute %s\n", ivar_getName(var));
		} else {
			Py_INCREF(res);
		}
	} else {
		const char* encoding = ivar_getTypeEncoding(var);

		if (encoding[0] == _C_ID) {
			/* An object */
			id value = object_getIvar(objc, var);
			res = pythonify_c_value(
				encoding, &value);
		} else {
			res = pythonify_c_value(
				encoding,
				((char*)objc) + ivar_getOffset(var));
		}
	}
	return res;
}

static int
ivar_descr_set(PyObject* _self, PyObject* obj, PyObject* value)
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	volatile Ivar var;
	id   objc;
	Py_ssize_t  size;
	int res;

	if (value == NULL && !self->isSlot) {
		PyErr_SetString(PyExc_TypeError,
			"Cannot delete Objective-C instance variables");
		return -1;
	}

	if (!obj || PyObjCClass_Check(obj)) {
		PyErr_SetString(PyExc_TypeError,
			"Cannot access Objective-C instance-variables "
			"through class");
		return -1;
	}

	if (!PyObjCObject_Check(obj)) {
		PyErr_SetString(PyExc_TypeError, 
		    "objc_ivar descriptor on a non-objc object");
		return -1;
	}
	objc = PyObjCObject_GetObject(obj); 
	if (objc == NULL) {
		PyErr_SetString(PyExc_TypeError,
		   "Cannot access Objective-C instance-variables of NULL");
		return -1;
	}

	if (self->name == NULL) {
		PyErr_SetString(PyExc_TypeError,
			"Using unnamed instance variable");
		return -1;
	}


	if (self->ivar == NULL) {
		var = class_getInstanceVariable(
				object_getClass(objc), self->name);
		if (var == NULL) {
			PyErr_SetString(PyExc_RuntimeError, 
			    "objc_ivar descriptor for non-existing instance "
			    "variable");
			return -1;
		}	
		self->ivar = var;
	} else {
		var = self->ivar;
	}
	
	//NSString* ocName = [NSString stringWithUTF8String:self->name];
	// [objc willChangeValueForKey:ocName];

	if (self->isSlot) {
		PyObject** slotval = (PyObject**)(
				((char*)objc) + ivar_getOffset(var));
		Py_XINCREF(value);
		Py_XDECREF(*slotval);
		*slotval = value;

		// [objc didChangeValueForKey:ocName];
		return 0;
	}

	if (strcmp(ivar_getTypeEncoding(var), @encode(id)) == 0) {
		/* Automagically manage refcounting of instance variables */
		id new_value;

		res = depythonify_c_value(@encode(id), value, &new_value);
		if (res == -1) {
			// [objc didChangeValueForKey:ocName];
			return -1;
		}

		if (!self->isOutlet) {
			PyObjC_DURING
				id old_value = object_getIvar(objc, var);
				[new_value retain];
				[old_value release];
			PyObjC_HANDLER
				NSLog(@"PyObjC: ignoring exception during attribute replacement: %@", localException);
			PyObjC_ENDHANDLER
		}

		object_setIvar(objc, var, new_value);
		// [objc didChangeValueForKey:ocName];

		return 0;
	}

	size = PyObjCRT_SizeOfType(ivar_getTypeEncoding(var));
	if (size == -1) {
		// [objc didChangeValueForKey:ocName];
		return -1;
	}
	res = depythonify_c_value(ivar_getTypeEncoding(var), value, 
		(void*)(((char*)objc)+ivar_getOffset(var)));
	if (res == -1) {
		// [objc didChangeValueForKey:ocName];
		return -1;
	}

	// [objc didChangeValueForKey:ocName];
	return 0;
}

static int
ivar_init(PyObject* _self, PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "name", "type", "isOutlet", NULL };
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	char* name = NULL;
	char* type = @encode(id);
	PyObject* isOutletObj = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
				"|s"Py_ARG_BYTES"O:objc_ivar",
			keywords, &name, &type, &isOutletObj)) {
		return -1;
	}

	if (name) {
		self->name = PyObjCUtil_Strdup(name);
		if (self->name == NULL) {
			return -1;
		}
	} else  {
		self->name = NULL;
	}
	self->type = PyObjCUtil_Strdup(type);
	if(self->type == NULL) {
		if (name) {
			PyMem_Free(self->name);
		}
		return -1;
	}
	if (isOutletObj) {
		self->isOutlet = PyObject_IsTrue(isOutletObj);
	} else {
		self->isOutlet = 0;
	}
	self->ivar = NULL;
	self->isSlot = 0;

	return 0;
}

static PyObject*
ivar_class_setup(PyObject* _self, PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "name", "class_dict", "instance_method_list", "class_method_list", NULL };
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	char* name;
	PyObject* class_dict;
	PyObject* instance_method_list;
	PyObject* class_method_list;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sO!O!O!", keywords,
			&name,
			&PyDict_Type, &class_dict, 
			&PySet_Type, &instance_method_list,
			&PySet_Type, &class_method_list
		)){
		return NULL;
	}

	if (self->name == NULL) {
		self->name = PyObjCUtil_Strdup(name);
	}

	Py_INCREF(Py_None);
	return Py_None;
}


static PyMethodDef ivar_methods[] = {
	{
		"__pyobjc_class_setup__",
		(PyCFunction)ivar_class_setup,
		METH_VARARGS|METH_KEYWORDS,
		NULL
	},

	{
		NULL, NULL, 0, NULL
	}
};


PyDoc_STRVAR(ivar_doc,
"ivar(name, type='@', isOutlet=False) -> instance-variable\n"
"\n"
"Creates a descriptor for accessing an Objective-C instance variable.\n\n"
"This should only be used in the definition of Objective-C subclasses, and\n"
"will then automaticly define the instance variable in the objective-C side.\n"
"\n"
"'type' is optional and should be a signature string.\n"
"\n"
"The name is optional in class definitions and will default to the name the\n"
"value is assigned to"
);

PyDoc_STRVAR(ivar_typestr_doc,
		        "The Objective-C type encoding");
static PyObject*
ivar_get_typestr(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;

	return PyBytes_FromString(self->type);
}

PyDoc_STRVAR(ivar_name_doc,
		        "The Objective-C name");
static PyObject*
ivar_get_name(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;


	if (self->name) {
		return PyText_FromString(self->name);
	} else {
		Py_INCREF(Py_None);
		return Py_None;
	}
}

PyDoc_STRVAR(ivar_isOutlet_doc,
		        "True if the instance variable is an IBOutlet");
static PyObject*
ivar_get_isOutlet(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	PyObject* result = self->isOutlet ? Py_True : Py_False;
	Py_INCREF(result);
	return result;
}

PyDoc_STRVAR(ivar_isSlot_doc,
		        "True if the instance variable is a Python slot");
static PyObject*
ivar_get_isSlot(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	PyObject* result = self->isSlot ? Py_True : Py_False;
	Py_INCREF(result);
	return result;
}


static PyGetSetDef ivar_getset[] = {
	{
		"__typestr__",
		ivar_get_typestr,
		0,
		ivar_typestr_doc,
		0
	},
	{
		"__name__",
		ivar_get_name,
		0,
		ivar_name_doc,
		0
	},
	{
		"__isOutlet__",
		ivar_get_isOutlet,
		0,
		ivar_isOutlet_doc,
		0
	},
	{
		"__isSlot__",
		ivar_get_isSlot,
		0,
		ivar_isSlot_doc,
		0
	},
	{ 0, 0, 0, 0, 0 }
};


PyTypeObject PyObjCInstanceVariable_Type = {
	PyVarObject_HEAD_INIT(&PyType_Type, 0)             
	"ivar",                             
	sizeof(PyObjCInstanceVariable),                       
	0,                                           
	ivar_dealloc,               		/* tp_dealloc */
	0,                                      /* tp_print */
	0,                                      /* tp_getattr */
	0,                                      /* tp_setattr */
	0,                                      /* tp_compare */
	ivar_repr,                    		/* tp_repr */
	0,                                      /* tp_as_number */
	0,                                      /* tp_as_sequence */
	0,                                      /* tp_as_mapping */
	0,                                      /* tp_hash */
	0,                                      /* tp_call */
	0,                                      /* tp_str */
	PyObject_GenericGetAttr,                /* tp_getattro */
	0,                                      /* tp_setattro */
	0,                                      /* tp_as_buffer */
	Py_TPFLAGS_DEFAULT, 			/* tp_flags */
	ivar_doc,                               /* tp_doc */
	0,                                      /* tp_traverse */
	0,                                      /* tp_clear */
	0,                                      /* tp_richcompare */
	0,                                      /* tp_weaklistoffset */
	0,                                      /* tp_iter */
	0,                                      /* tp_iternext */
	ivar_methods,                           /* tp_methods */
	0,                                      /* tp_members */
	ivar_getset,                            /* tp_getset */
	0,                                      /* tp_base */
	0,                                      /* tp_dict */
	ivar_descr_get,           		/* tp_descr_get */
	ivar_descr_set,           		/* tp_descr_set */
	0,                                      /* tp_dictoffset */
	ivar_init,                    		/* tp_init */
	PyType_GenericAlloc,                    /* tp_alloc */
	PyType_GenericNew,                      /* tp_new */
	0,                                      /* tp_free */
	0,                                      /* tp_is_gc */
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

/* Set the name of an ivar if it doesn't already have one 
 * This should only be used during class construction.
 */
int 
PyObjCInstanceVariable_SetName(PyObject* value, PyObject* name)
{
	if (!PyObjCInstanceVariable_Check(value)) {
		PyErr_SetString(PyExc_TypeError, "unexpected type for ivar.setname");
		return -1;
	}

	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)value;
	if (self->name) {
		return 0;
	} 

	if (PyUnicode_Check(name)) {
		PyObject* bytes = PyUnicode_AsEncodedString(name, NULL, NULL);
		if (bytes == NULL) {
			return -1;
		}

		char* b = PyBytes_AsString(bytes);
		if (b == NULL || *b == '\0') {
			PyErr_SetString(PyExc_ValueError, "Empty name");
			return -1;
		}
		self->name = PyObjCUtil_Strdup(b);
		Py_DECREF(bytes);
		if (self->name == NULL) {
			PyErr_NoMemory();
			return -1;
		}

#if PY_MAJOR_VERSION == 2
	} else if (PyString_Check(name)) {
		self->name = PyObjCUtil_Strdup(PyString_AS_STRING(name));
#endif
	} else {
		PyErr_SetString(PyExc_TypeError, 
			"Implied instance variable name is not a string");
		return -1;
	}

	return (self->name == NULL?-1:0);
}

PyObject* 
PyObjCInstanceVariable_New(char* name)
{
	PyObject* result;

	result = PyObjCInstanceVariable_Type.tp_alloc(&PyObjCInstanceVariable_Type, 0);
	if (result == NULL) {
		return NULL;
	}
	((PyObjCInstanceVariable*)result)->type = PyObjCUtil_Strdup("");
	if (((PyObjCInstanceVariable*)result)->type == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	((PyObjCInstanceVariable*)result)->isOutlet = 0;
	((PyObjCInstanceVariable*)result)->isSlot = 0;
	((PyObjCInstanceVariable*)result)->ivar = 0;
	((PyObjCInstanceVariable*)result)->name = PyObjCUtil_Strdup(name);
	if (((PyObjCInstanceVariable*)result)->name == NULL) {
		PyMem_Free(((PyObjCInstanceVariable*)result)->type);
		Py_DECREF(result);
		return NULL;
	}
	return result;
}
