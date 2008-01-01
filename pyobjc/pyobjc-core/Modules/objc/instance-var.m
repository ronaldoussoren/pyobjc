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
	ivar->ob_type->tp_free((PyObject*)ivar);
}

static PyObject*
ivar_repr(PyObject* _self)
{
	PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
	if (self->isOutlet) {
		if (self->name) {
			return PyString_FromFormat("<IBOutlet %s>", self->name);
		} else {
			return PyString_FromString("<IBOutlet>");
		}
	} else {
		if (self->name) {
			return PyString_FromFormat("<instance-variable %s>", self->name);
		} else {
			return PyString_FromString("<instance-variable>");
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
	

	if (self->isSlot) {
		PyObject** slotval = (PyObject**)(
				((char*)objc) + ivar_getOffset(var));
		Py_XINCREF(value);
		Py_XDECREF(*slotval);
		*slotval = value;

		return 0;
	}

	if (strcmp(ivar_getTypeEncoding(var), @encode(id)) == 0) {
		/* Automagically manage refcounting of instance variables */
		id new_value;

		res = depythonify_c_value(@encode(id), value, &new_value);
		if (res == -1) {
			return -1;
		}

		if (!self->isOutlet) {
			PyObjC_DURING
				id old_value = object_getIvar(objc, var);
				[new_value retain];
				[old_value release];
			PyObjC_HANDLER
				NSLog(@"PyObjC: ignoring exception during attribute replacement", localException);
			PyObjC_ENDHANDLER
		}

		object_setIvar(objc, var, new_value);

		return 0;
	}

	size = PyObjCRT_SizeOfType(ivar_getTypeEncoding(var));
	if (size == -1) {
		return -1;
	}
	res = depythonify_c_value(ivar_getTypeEncoding(var), value, 
		(void*)(((char*)objc)+ivar_getOffset(var)));
	if (res == -1) {
		return -1;
	}

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

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "|ssO:objc_ivar",
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

PyTypeObject PyObjCInstanceVariable_Type = {
	PyObject_HEAD_INIT(&PyType_Type)             
	0,                                           
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
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_CLASS, /* tp_flags */
	ivar_doc,                               /* tp_doc */
	0,                                      /* tp_traverse */
	0,                                      /* tp_clear */
	0,                                      /* tp_richcompare */
	0,                                      /* tp_weaklistoffset */
	0,                                      /* tp_iter */
	0,                                      /* tp_iternext */
	0,                                      /* tp_selectors */
	0,                                      /* tp_members */
	0,                                      /* tp_getset */
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

	if (PyString_Check(name)) {
		self->name = PyObjCUtil_Strdup(PyString_AS_STRING(name));
	} else {
		char* v;
		if (depythonify_c_value(@encode(char*), name, &v) == -1) {
			return -1;
		}
		self->name = PyObjCUtil_Strdup(PyString_AS_STRING(name));
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
