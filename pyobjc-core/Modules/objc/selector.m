/*
 * Implementation of 'native' and 'python' selectors
 *
 * TODO:
 * - Maybe it is better to fold the three types into one, especially because
 *   only one of them is exposed to python code.
 */
#include "pyobjc.h"

#include "compile.h" /* from Python */
#include "opcode.h"

#include <objc/Object.h>

/*
 * First section deals with registering replacement signatures for methods.
 * This is meant to be used to add _C_IN, _C_OUT and _C_INOUT specifiers for
 * pass-by-reference parameters.
 *
 * We register class names because the actual class may not yet be available. 
 * The list of replacements is not sorted in any way, it is expected to be 
 * short and the list won't be checked very often.\
 *
 * Alternative implementation: { SEL: [ (class_name, signature), ... ], ... }
 */
static PyObject* replacement_signatures = NULL;

int 
ObjC_SignatureForSelector(char* class_name, SEL selector, char* signature)
{
	PyObject* replacement;
	PyObject* name_str;
	PyObject* selector_str;;
	int r;

	if (replacement_signatures == NULL) {
		replacement_signatures = PyObjC_NewRegistry();
		if (replacement_signatures == NULL) {
			return -1;
		}
	}

	replacement = PyString_FromString(signature);
	if (replacement == NULL)  {
		return -1;
	}

	name_str = PyString_FromString(class_name);
	if (name_str == NULL)  {
		Py_DECREF(replacement);
		return -1;
	}

	selector_str = PyString_FromString(sel_getName(selector));
	if (name_str == NULL)  {
		Py_DECREF(replacement);
		Py_DECREF(name_str);
		return -1;
	}

	r = PyObjC_AddToRegistry(replacement_signatures, name_str, selector_str,
			replacement);

	Py_DECREF(replacement);
	Py_DECREF(name_str);
	Py_DECREF(selector_str);

	return r;
}

static char* 
PyObjC_FindReplacementSignature(Class cls, SEL selector)
{
	PyObject* replacement;
	char* result;


	if (replacement_signatures == NULL) {
		return NULL;
	}

	replacement = PyObjC_FindInRegistry(
			replacement_signatures, cls, selector);
	if (replacement == NULL) {
		return NULL;
	}

	result = PyString_AsString(replacement);
	Py_DECREF(replacement);

	return result;
}

static char* pysel_default_signature(PyObject* callable);

/* Need to check instance-method implementation! */
/* Maybe we can subclass 'PyMethod_Type' */

/*
 * Base type for objective-C selectors
 *
 * selectors are callable objects with the following attributes:
 * - 'signature': The objective-C signature of the method
 * - 'selector':  The name in the objective-C runtime
 */

PyObjCMethodSignature*
PyObjCSelector_GetMetadata(PyObject* _self)
{
	PyObjCSelector* self = (PyObjCSelector*)_self;

	if (self->sel_methinfo == NULL) {
		self->sel_methinfo = PyObjCMethodSignature_ForSelector(
			self->sel_class,
			self->sel_selector,
			self->sel_python_signature);
		if (self->sel_methinfo == NULL) return NULL;

		if (PyObjCPythonSelector_Check(_self)) {
			Py_ssize_t i;

			((PyObjCPythonSelector*)_self)->numoutput = 0;
			for (i = 0; i < ((PyObjCPythonSelector*)_self)->sel_methinfo->ob_size; i++) {
				if (((PyObjCPythonSelector*)_self)->sel_methinfo->argtype[i].type[0] == _C_OUT) {
					((PyObjCPythonSelector*)_self)->numoutput ++;
				}
			}
		}
	}
	return self->sel_methinfo;
}


PyDoc_STRVAR(sel_metadata_doc, "Return a dict that describes the metadata for this method, including metadata for the 2 hidden ObjC parameters (self and _sel) ");
static PyObject* sel_metadata(PyObject* self)
{
	PyObject* result = PyObjCMethodSignature_AsDict(PyObjCSelector_GetMetadata(self));
	int r;

	if (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kCLASS_METHOD) {
		r = PyDict_SetItemString(result, "classmethod", Py_True);
	} else {
		r = PyDict_SetItemString(result, "classmethod", Py_False);
	}
	if (r == -1) {
		Py_DECREF(result);
		return NULL;
	}

	if (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
		r = PyDict_SetItemString(result, "return_uninitialized_object", Py_True);
		if (r == -1) {
			Py_DECREF(result);
			return NULL;
		}
	}
	return result;
}

static PyMethodDef sel_methods[] = {
	{
		  "__metadata__",
	    	  (PyCFunction)sel_metadata,
	          METH_NOARGS,
		  sel_metadata_doc
	},
	{ 0, 0, 0, 0 }
};

static PyObject*
pysel_new(PyTypeObject* type, PyObject* args, PyObject* kwds);

PyDoc_STRVAR(base_self_doc, "'self' object for bound methods, None otherwise");
static PyObject*
base_self(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCSelector* self = (PyObjCSelector*)_self;
	if (self->sel_self) {
		Py_INCREF(self->sel_self);
		return self->sel_self;
	} else {
		Py_INCREF(Py_None);
		return Py_None;
	}
}

PyDoc_STRVAR(base_signature_doc, "Objective-C signature for the method");
static PyObject*
base_signature(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCSelector* self = (PyObjCSelector*)_self;
	return PyString_FromString(self->sel_python_signature);
}

PyDoc_STRVAR(base_native_signature_doc, "original Objective-C signature for the method");
static PyObject*
base_native_signature(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCSelector* self = (PyObjCSelector*)_self;
	if (self->sel_native_signature == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	return PyString_FromString(self->sel_native_signature);
}

static int
base_signature_setter(PyObject* _self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
	PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
	char* t;
	if (!PyString_Check(newVal)) {
		PyErr_SetString(PyExc_TypeError, "signature must be string");
		return -1;
	}

	t = PyObjCUtil_Strdup(PyString_AsString(newVal));
	if (t == NULL) {
		PyErr_NoMemory();
		return -1;
	}

	PyMem_Free(self->sel_python_signature);
	self->sel_python_signature = t;
	return 0;
}

PyDoc_STRVAR(base_selector_doc, "Objective-C name for the method");
static PyObject*
base_selector(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCSelector* self = (PyObjCSelector*)_self;
	return PyString_FromString(sel_getName(self->sel_selector));
}

PyDoc_STRVAR(base_class_doc, "Objective-C Class that defines the method");
static PyObject*
base_class(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
	if (self->sel_class != nil) {
		return PyObjCClass_New(self->sel_class);
	}
	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(base_class_method_doc, 
	"True if this is a class method, False otherwise");
static PyObject*
base_class_method(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
	return PyBool_FromLong(0 != (self->sel_flags & PyObjCSelector_kCLASS_METHOD));
}

PyDoc_STRVAR(base_required_doc, 
	"True if this is a required method, False otherwise");
static PyObject*
base_required(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
	return PyBool_FromLong(0 != (self->sel_flags & PyObjCSelector_kREQUIRED));
}




static PyGetSetDef base_getset[] = {
	{
		"isRequired",
		base_required,
		0,
		base_required_doc,
		0
	},
	{
		"isClassMethod",
		base_class_method,
		0,
		base_class_method_doc,
		0
	},
	{ 
		"definingClass", 
		base_class, 
		0,
		base_class_doc, 
		0
	},
	{ 
		"signature", 
		base_signature, 
		base_signature_setter,
		base_signature_doc, 
		0
	},
	{
		"native_signature",
		base_native_signature,
		0,
		base_native_signature_doc,
		0
	},
	{ 
		"self", 
		base_self, 
		0,
		base_self_doc, 
		0
	},
	{ 
		"selector",  
		base_selector, 
		0, 
		base_selector_doc,
		0
	},
	{ 
		"__name__",  
		base_selector, 
		0, 
		base_selector_doc,
		0
	},
	{ 0, 0, 0, 0, 0 }
};


static void
sel_dealloc(PyObject* object)
{
	PyObjCSelector* self = (PyObjCSelector*)object;	
	Py_XDECREF(self->sel_methinfo);
	self->sel_methinfo = NULL;

	PyMem_Free(self->sel_python_signature);
	self->sel_python_signature = NULL;

	if (self->sel_native_signature != NULL) {
		PyMem_Free(self->sel_native_signature);
		self->sel_native_signature = NULL;
	}
	if (self->sel_self) { 
		Py_DECREF(self->sel_self); 
		self->sel_self = NULL;
	}
	object->ob_type->tp_free(object);
}

static int
base_descr_set(
		PyObject* self __attribute__((__unused__)), 
		PyObject* obj __attribute__((__unused__)), PyObject* value)
{
	if (value == NULL) {
		PyErr_SetString(PyExc_TypeError, "cannot delete a method");
	} else {
		/* Dummy, setattr of the class deals with this */
		PyErr_SetString(PyExc_TypeError, "cannot change a method");
	}
	return -1;
}


PyDoc_STRVAR(base_selector_type_doc,
"selector(function, [, selector] [, signature] [, isClassMethod=0]\n"
"    [, returnType] [, argumentTypes] [, isRequired=True]) -> selector\n"
"\n"
"Return an Objective-C method from a function. The other arguments \n"
"specify attributes of the Objective-C method.\n"
"\n"
"function:\n"
"  A function object with at least one argument. The first argument will\n"
"  be used to pass 'self'. This argument may be None when defining an\n"
"  informal_protocol object. The function must not be a ``staticmethod``\n"
"  instance. \n"
"selector:\n"
"  The name of the Objective-C method. The default value of this\n"
"  attribute is the name of the function, with all underscores replaced\n"
"  by colons.\n"
"signature:\n"
"  Method signature for the Objective-C method. This should be a raw\n"
"  Objective-C method signature, including specifications for 'self' and\n"
"  '_cmd'. The default value a signature that describes a method with\n"
"  arguments of type 'id' and a return-value of the same type.\n"
"argumentTypes, returnType:\n"
"  Alternative method for specifying the method signature. returnType is\n"
"  the return type and argumentTypes describes the list of arguments. The \n"
"  returnType is optional and defaults to 'void' (e.g. no return value).\n"
"  Both are specified using a subset of the Py_BuildValue syntax:\n"
"  - s, z, S: an NSString (id)\n"
"  - b: a byte (char)\n"
"  - h: a short integer (short int)\n"
"  - i: an integer (int)\n"
"  - l: a long integer (long int)\n"
"  - c: a single character (char)\n"
"  - f: a single precision float (float)\n"
"  - d: a double precision float (double)\n"
"  - O: any object (id)\n"
"  It is not allowed to specify both 'argumentTypes' and 'signature'\n"
"isClassMethod:\n"
"  True if the method is a class method, false otherwise. The default is \n"
"  False, unless the function is an instance of ``classmethod``.\n"
"isRequired:\n"
"  True if this is a required method in an informal protocol, False\n"
"  otherwise. The default value is 'True'. This argument is only used\n"
"  when defining an 'informal_protocol' object.\n"
);
PyTypeObject PyObjCSelector_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.selector",			/* tp_name */
	sizeof(PyObjCSelector),			/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	sel_dealloc,	 			/* tp_dealloc */
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
 	base_selector_type_doc,			/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	sel_methods,				/* tp_methods */
	0,					/* tp_members */
	base_getset,				/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	base_descr_set,				/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	pysel_new,				/* tp_new */
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
 * Selector type for 'native' selectors (that is, selectors that are not
 * implemented as python methods)
 */
static PyObject*
objcsel_repr(PyObject* _self)
{
	PyObjCNativeSelector* sel = (PyObjCNativeSelector*)_self;
	PyObject *rval;
	if (sel->sel_self == NULL) {
		rval = PyString_FromFormat("<unbound native-selector %s in %s>", sel_getName(sel->sel_selector), class_getName(sel->sel_class));
	} else {
		PyObject* selfrepr = PyObject_Repr(sel->sel_self);
		if (selfrepr == NULL) {
			return NULL;
		}
		if (!PyString_Check(selfrepr)) {
			Py_DECREF(selfrepr);
			return NULL;
		}
		rval = PyString_FromFormat("<native-selector %s of %s>", sel_getName(sel->sel_selector), PyString_AS_STRING(selfrepr));
		Py_DECREF(selfrepr);
	}
	return rval;
}


static PyObject*
objcsel_call(PyObject* _self, PyObject* args, PyObject* kwds)
{
	PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
	PyObject* pyself = self->sel_self;
	PyObjC_CallFunc execute = NULL;
	PyObject* res;
	PyObject* pyres;

	if (kwds != NULL && PyObject_Size(kwds) != 0) {
		PyErr_SetString(PyExc_TypeError, 
		    "Objective-C selectorrs don't support keyword arguments");
		return NULL;
	}

	if (pyself == NULL) {
		int       argslen;
		argslen = PyTuple_Size(args);
		if (argslen < 1) {
			PyErr_SetString(PyExc_TypeError,
				"Missing argument: self");
			return NULL;
		}
		pyself = PyTuple_GET_ITEM(args, 0);
		if (pyself == NULL) {
			return NULL;
		}
	}

	if (self->sel_call_func) {
		execute = self->sel_call_func;
	} else {
		execute = PyObjC_FindCallFunc(
				self->sel_class, 
				self->sel_selector);
		if (execute == NULL) return NULL;
		self->sel_call_func = execute;
	}

	if (self->sel_self != NULL) {
		pyres = res = execute((PyObject*)self, self->sel_self, args);
		if (pyres != NULL
			&& PyTuple_Check(pyres)
			&& PyTuple_GET_SIZE(pyres) > 1
			&& PyTuple_GET_ITEM(pyres, 0) == pyself) {
			pyres = pyself;
		}

		if (PyObjCObject_Check(self) && (((PyObjCObject*)self->sel_self)->flags & PyObjCObject_kUNINITIALIZED)) {
			if (self->sel_self != pyres && !PyErr_Occurred()) {
				PyObjCObject_ClearObject(pyself);
			}
		}
	} else {
		PyObject* arglist;
		PyObject* myClass;
		Py_ssize_t i;
		Py_ssize_t argslen;

		argslen = PyTuple_Size(args);
		arglist = PyTuple_New(argslen - 1);
		for (i = 1; i < argslen; i++) {
			PyObject* v = PyTuple_GET_ITEM(args, i);
			if (v == NULL) {
				Py_DECREF(arglist);
				return NULL;
			}

			PyTuple_SET_ITEM(arglist, i-1, v);
			Py_INCREF(v);
		}

		myClass = PyObjCClass_New(self->sel_class);
		if (!(PyObject_IsInstance(pyself, myClass)
			|| (PyString_Check(pyself) && class_isSubclassOf(self->sel_class, [NSString class])) 
			|| (PyUnicode_Check(pyself) && class_isSubclassOf(self->sel_class, [NSString class])) 
		)) {
			Py_DECREF(arglist);
			Py_DECREF(myClass);
			PyErr_Format(PyExc_TypeError,
				"Expecting instance of %s as self, got one "
				"of %s", class_getName(self->sel_class),
				pyself->ob_type->tp_name);
			return NULL;
		}
		Py_DECREF(myClass);
		

		pyres = res = execute((PyObject*)self, pyself, arglist);
		if (pyres != NULL
			&& PyTuple_Check(pyres)
			&& PyTuple_GET_SIZE(pyres) > 1
			&& PyTuple_GET_ITEM(pyres, 0) == pyself) {
			pyres = pyself;
		}

		Py_DECREF(arglist);
	}

	if (pyres && PyObjCObject_Check(pyres)) {
		if (self->sel_flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
			((PyObjCObject*)pyres)->flags |= PyObjCObject_kUNINITIALIZED;
		} else if (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED) {
			((PyObjCObject*)pyself)->flags &= 
				~PyObjCObject_kUNINITIALIZED;
			if (self->sel_self && self->sel_self != pyres && !PyErr_Occurred()) {
				PyObjCObject_ClearObject(self->sel_self);
			}
		}
	}

	return res;
}

static PyObject*
objcsel_descr_get(PyObject* _self, PyObject* volatile obj, PyObject* class)
{
	PyObjCNativeSelector* meth = (PyObjCNativeSelector*)_self;
	PyObjCNativeSelector* result;

	if (meth->sel_self != NULL || obj == Py_None) {
		Py_INCREF(meth);
		return (PyObject*)meth;
	} 

	if (class != nil && PyType_Check(class) && PyType_IsSubtype((PyTypeObject*)class, &PyObjCClass_Type)) {
		class = PyObjCClass_ClassForMetaClass(class);
	}

	/* Bind 'self' */
	if (meth->sel_flags & PyObjCSelector_kCLASS_METHOD) {
		obj = class;
	}
	result = PyObject_New(PyObjCNativeSelector, &PyObjCNativeSelector_Type);
	result->sel_selector   = meth->sel_selector;
	result->sel_python_signature  = PyObjCUtil_Strdup(meth->sel_python_signature);
	if (result->sel_python_signature == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	if (meth->sel_native_signature != NULL) {
		result->sel_native_signature = PyObjCUtil_Strdup(meth->sel_native_signature);
		if (result->sel_native_signature == NULL) {
			Py_DECREF(result);
			return NULL;
		}
	} else {
		result->sel_native_signature = NULL;
	}
	result->sel_flags = meth->sel_flags;
	result->sel_class = meth->sel_class;

	if (meth->sel_call_func == NULL) {
		meth->sel_call_func = PyObjC_FindCallFunc(meth->sel_class,
			meth->sel_selector);
	}
	result->sel_call_func = meth->sel_call_func;

	result->sel_methinfo = PyObjCSelector_GetMetadata((PyObject*)meth);
	if (result->sel_methinfo) {
		Py_INCREF(result->sel_methinfo);
	} else {
		PyErr_Clear();
	}

	result->sel_self = obj;
	if (result->sel_self) {
		Py_INCREF(result->sel_self);
	}

	return (PyObject*)result;
}



PyTypeObject PyObjCNativeSelector_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.native_selector",			/* tp_name */
	sizeof(PyObjCNativeSelector),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	sel_dealloc,				/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	objcsel_repr,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	objcsel_call,				/* tp_call */
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
	0,					/* tp_getset */
	&PyObjCSelector_Type,			/* tp_base */
	0,					/* tp_dict */
	objcsel_descr_get,			/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	0,					/* tp_new */
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



static Class Object_class = nil;

PyObject*
PyObjCSelector_FindNative(PyObject* self, const char* name)
{
	volatile SEL   sel = PyObjCSelector_DefaultSelector(name);
	PyObject* retval;

	NSMethodSignature* methsig;
	char  buf[1024];

	if (Object_class == nil) {
		Object_class = [Object class];
	}

	if (name[0] == '_' && name[1] == '_') {
		/* No known Objective-C class has methods whose name
		 * starts with '__' or '_:'. This allows us to shortcut
		 * lookups for special names, which speeds up tools like
		 * pydoc.
		 */
		PyErr_Format(PyExc_AttributeError,
			"No attribute %s", name);
		return NULL;
	}

	if (PyObjCClass_Check(self)) {
		Class cls = PyObjCClass_GetClass(self);

		if (!cls) {
			PyErr_Format(PyExc_AttributeError,
				"No attribute %s", name);
			return NULL;
		}
		if (strcmp(class_getName(cls), "_NSZombie") == 0) {
			PyErr_Format(PyExc_AttributeError,
				"No attribute %s", name);
			return NULL;
		}

		if (strcmp(class_getName(cls), "NSProxy") == 0) {
			if (sel == @selector(methodSignatureForSelector:)) {
				PyErr_Format(PyExc_AttributeError,
					"Accessing NSProxy.%s is not supported",
					name);
				return NULL;
			}
		}

		NS_DURING
			if ([cls instancesRespondToSelector:sel]) {
				methsig = [cls instanceMethodSignatureForSelector:sel];
				retval = PyObjCSelector_NewNative(cls, sel, 
					PyObjC_NSMethodSignatureToTypeString(methsig, buf, sizeof(buf)), 0);
			} else if ((cls != Object_class) && nil != (methsig = [(NSObject*)cls methodSignatureForSelector:sel])) {
				retval = PyObjCSelector_NewNative(cls, sel, 
					PyObjC_NSMethodSignatureToTypeString(
						methsig, buf, sizeof(buf)), 1);
			} else {
				PyErr_Format(PyExc_AttributeError,
					"No attribute %s", name);
				retval = NULL;
			}
		NS_HANDLER
			PyErr_Format(PyExc_AttributeError,
				"No attribute %s", name);
			retval = NULL;

		NS_ENDHANDLER

		return retval;

	} else if (PyObjCObject_Check(self)) {
		id object;

		object = PyObjCObject_GetObject(self);

		if (nil != (methsig = [object methodSignatureForSelector:sel])){
			PyObjCNativeSelector* res;

			res =  (PyObjCNativeSelector*)PyObjCSelector_NewNative(
				object_getClass(object), sel, 
				PyObjC_NSMethodSignatureToTypeString(methsig, 
					buf, sizeof(buf)), 0);
			if (res != NULL) {
				/* Bind the method to self */
				res->sel_self = self;
				Py_INCREF(res->sel_self);
			}
			return (PyObject*)res;
		} else {
			PyErr_Format(PyExc_AttributeError,
				"No attribute %s", name);
			return NULL;
		}
	} else {
		PyErr_SetString(PyExc_RuntimeError,
			"PyObjCSelector_FindNative called on plain "
			"python object");
		return NULL;
	}
}


PyObject*
PyObjCSelector_NewNative(Class class, 
			SEL selector, const char* signature, int class_method)
{
	PyObjCNativeSelector* result;
	const char* native_signature = signature;
	char* repl_sig;

	repl_sig = PyObjC_FindReplacementSignature(class, selector);
	if (repl_sig) {
		signature = repl_sig;
	}

	result = PyObject_New(PyObjCNativeSelector, &PyObjCNativeSelector_Type);
	if (result == NULL) return NULL;

	result->sel_selector = selector;
	result->sel_python_signature = PyObjCUtil_Strdup(signature);
	result->sel_native_signature = PyObjCUtil_Strdup(native_signature);
	if (result->sel_python_signature == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	result->sel_self = NULL;
	result->sel_class = class;
	result->sel_call_func = NULL;
	result->sel_methinfo = NULL;
	result->sel_flags = 0;
	if (class_method) {
		result->sel_flags |= PyObjCSelector_kCLASS_METHOD;
	}
	if (sel_isEqual(selector, @selector(alloc)) || sel_isEqual(selector, @selector(allocWithZone:))) {
		  result->sel_flags |= PyObjCSelector_kRETURNS_UNINITIALIZED;
	}
	return (PyObject*)result;
}


static char gSheetMethodSignature[] = { _C_VOID, _C_ID, _C_SEL, _C_ID, _C_INT, _C_PTR , _C_VOID, 0 };

PyObject*
PyObjCSelector_New(PyObject* callable, 
	SEL selector, char* signature, int class_method, Class cls)
{
	PyObjCPythonSelector* result;
	if (signature == NULL) {
		const char* selname = sel_getName(selector);
		size_t len = strlen(selname);
		if (len > 30 && strcmp(selname+len-30, "DidEnd:returnCode:contextInfo:") == 0) {
			signature = PyObjCUtil_Strdup(gSheetMethodSignature);
		} else {
			signature = pysel_default_signature(callable);
		}
	} else {
		signature = PyObjCUtil_Strdup(signature);
	}
	if (signature == NULL) return NULL;

	result = PyObject_New(PyObjCPythonSelector, &PyObjCPythonSelector_Type);
	if (result == NULL) return NULL;

	result->sel_selector = selector;
	result->sel_python_signature = signature;
	result->sel_native_signature = PyObjCUtil_Strdup(signature);
	if (result->sel_native_signature == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyObjC_RemoveInternalTypeCodes(result->sel_native_signature);

	result->sel_self = NULL;
	result->sel_class = cls;
	result->sel_flags = 0;
	result->sel_methinfo = NULL; /* We might not know the class right now */

	if (PyObjCPythonSelector_Check(callable)) {
		callable = ((PyObjCPythonSelector*)callable)->callable;
	}
	if (PyFunction_Check(callable)) {
		result->argcount = ((PyCodeObject*)PyFunction_GetCode(callable))->co_argcount;
	}  else if (PyMethod_Check(callable)) {
		if (PyMethod_Self(callable) == NULL) {
			result->argcount = ((PyCodeObject*)PyFunction_GetCode(PyMethod_Function(callable)))->co_argcount;
		} else {
			result->argcount = ((PyCodeObject*)PyFunction_GetCode(PyMethod_Function(callable)))->co_argcount - 1;
		}
	} else if (callable == Py_None) {
		result->argcount = 0;

	} else {
		/* Should not happen... */
		result->argcount = -1;
		abort();

	}

	if (class_method) {
		result->sel_flags |= PyObjCSelector_kCLASS_METHOD;
	}
	if (sel_isEqual(selector, @selector(alloc)) || sel_isEqual(selector, @selector(allocWithZone:))) {
		  result->sel_flags |= PyObjCSelector_kRETURNS_UNINITIALIZED;
	}

	result->callable = callable;
	Py_INCREF(result->callable);

	return (PyObject*)result;
}
	

/*
 * Selector type for python selectors (that is, selectors that are 
 * implemented as python methods)
 *
 * This one can be allocated from python code.
 */

static PyObject*
pysel_repr(PyObject* _self)
{
	PyObjCPythonSelector* sel = (PyObjCPythonSelector*)_self;
	PyObject *rval;

	if (sel->sel_self == NULL) {
		if (sel->sel_class) {
			rval = PyString_FromFormat("<unbound selector %s of %s at %p>", sel_getName(sel->sel_selector), class_getName(sel->sel_class), sel);
		} else {
			rval = PyString_FromFormat("<unbound selector %s at %p>", sel_getName(sel->sel_selector), sel);
		}
	} else {
		PyObject* selfrepr = PyObject_Repr(sel->sel_self);
		if (selfrepr == NULL) {
			return NULL;
		}
		if (!PyString_Check(selfrepr)) {
			Py_DECREF(selfrepr);
			return NULL;
		}
		rval = PyString_FromFormat("<selector %s of %s>", sel_getName(sel->sel_selector), PyString_AS_STRING(selfrepr));
		Py_DECREF(selfrepr);
	}
	return rval;
}


/*
 * Calling the method from Python is sligtly complicated by the fact that
 * output arguments are optionally present (both in the method signature
 * and the actual argument list).
 *
 * pysel_call needs to compensate for this, which is done by this function.
 */
static PyObject* 
compensate_arglist(PyObject* _self, PyObject* args, PyObject* kwds)
{
	/* XXX: need to do a full metadata processing run here to get exactly the right
	 * semantics, we also have to do a metadata run on the result!
	 */
	PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
	BOOL argsmatch;
	Py_ssize_t i;
	Py_ssize_t first_arg;

	if (self->sel_methinfo == NULL) {
		/* Make sure we actually have metadata */
		PyObjCSelector_GetMetadata(_self);
	}
	if (self->numoutput == 0) {
		Py_INCREF(args);
		return args;
	}


	if (kwds && PyDict_Size(kwds) != 0) {
		/* XXX: we cannot do anything here without reimplementing Python's argument
		 * matching code...
		 */
		Py_INCREF(args);
		return args;
	}

	argsmatch = ((PyTuple_Size(args) + (self->sel_self?1:0)) == self->argcount);

	first_arg = self->sel_self ? 0 : 1;

	if (self->argcount == self->sel_methinfo->ob_size-1) { /* the selector has an implicit '_sel' argument as well */
		/* All arguments are present, including output arguments */
		if (argsmatch) {
			for (i = 2; i < self->sel_methinfo->ob_size; i++) {
				if (self->sel_methinfo->argtype[i].type[0] == _C_OUT) {
					PyObject* a = PyTuple_GET_ITEM(args, first_arg + i - 2);
					if (a != Py_None && a != PyObjC_NULL) {
						PyErr_Format(PyExc_TypeError, 
							"argument %" PY_FORMAT_SIZE_T "d is an output argument but is passed a value other than None or objc.NULL (%s)",
							i-1-first_arg, PyObject_REPR(args));
						return NULL;
					}
				}
			}
			Py_INCREF(args);
			return args;
		} else {
			if ((PyTuple_Size(args) + (self->sel_self?1:0)) != (self->argcount - self->numoutput)) {
				/* There's the wrong number of arguments */
				PyErr_Format(PyExc_TypeError,
					"expecting %" PY_FORMAT_SIZE_T "d arguments, got %" PY_FORMAT_SIZE_T "d", self->argcount - (self->sel_self?1:0), PyTuple_Size(args));
				return NULL;
			}

			PyObject* real_args;
			Py_ssize_t pyarg;


			real_args = PyTuple_New(self->argcount - (self->sel_self?1:0));
			if (real_args == NULL) {
				return NULL;
			}

			pyarg = 0;
			if (self->sel_self == NULL) {
				pyarg = 1;
				PyTuple_SET_ITEM(real_args, 0, PyTuple_GET_ITEM(args, 0));
				Py_INCREF(PyTuple_GET_ITEM(args, 0));
			}

			PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(_self);
			for (i = 2; i < methinfo->ob_size; i++) {
				if (methinfo->argtype[i].type[0] == _C_OUT) {
					PyTuple_SET_ITEM(real_args, i-2+first_arg, Py_None);
					Py_INCREF(Py_None); 
				} else {
					PyTuple_SET_ITEM(real_args, i-2+first_arg, PyTuple_GET_ITEM(args, pyarg));
					Py_INCREF(PyTuple_GET_ITEM(args, pyarg));
					pyarg++;
				}
			}

			return real_args;
		}

	} else {
		/* Not all arguments are present, output arguments should
		 * be excluded.
		 */
		if (argsmatch) {
			Py_INCREF(args);
			return args;
		} else {
			if (PyTuple_Size(args) + (self->sel_self?1:0) != self->argcount + self->numoutput) {
				/* There's the wrong number of arguments */
				PyErr_Format(PyExc_TypeError,
					"expecting %" PY_FORMAT_SIZE_T "d arguments, got %" PY_FORMAT_SIZE_T "d", self->argcount - (self->sel_self?1:0), PyTuple_Size(args));
				return NULL;
			}
			PyObject* real_args;
			Py_ssize_t pyarg;

			real_args = PyTuple_New(self->argcount - (self->sel_self?1:0));
			if (real_args == NULL) {
				return NULL;
			}

			pyarg = 0;
			if (self->sel_self == NULL) {
				pyarg = 1;
				PyTuple_SET_ITEM(real_args, 0, PyTuple_GET_ITEM(args, 0));
				Py_INCREF(PyTuple_GET_ITEM(args, 0));
			}

			PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(_self);
			for (i = 2; i < methinfo->ob_size; i++) {
				if (methinfo->argtype[i].type[0] != _C_OUT) {
					PyTuple_SET_ITEM(real_args, pyarg, PyTuple_GET_ITEM(args, i-2+first_arg));
					Py_INCREF(PyTuple_GET_ITEM(args, i-2+first_arg));
					pyarg++;
				}
			}

			return real_args;
		}
	}
}

static PyObject*
pysel_call(PyObject* _self, PyObject* args, PyObject* kwargs)
{
	PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
	PyObject* result;

	if (self->callable == NULL) {
		PyErr_Format(PyExc_TypeError, 
			"Calling abstract methods with selector %s",
			sel_getName(self->sel_selector));
		return NULL;
	}

	args = compensate_arglist(_self, args, kwargs);
	if (args == NULL) {
		return NULL;
	}

	if (!PyMethod_Check(self->callable)) {
		if (self->sel_self == NULL) {
			PyObject* self_arg;
			if (PyTuple_Size(args) < 1) {
				Py_DECREF(args);
				PyErr_SetString(PyObjCExc_Error, "need self argument");
				return NULL;
			}
			self_arg = PyTuple_GET_ITEM(args, 0);
			if (!PyObjCObject_Check(self_arg) && !PyObjCClass_Check(self_arg)) {
				Py_DECREF(args);
				PyErr_Format(PyExc_TypeError, 
					"Expecting an Objective-C class or "
					"instance as self, got a %s",
					self_arg->ob_type->tp_name);
				return NULL;
			}
		}

		/* normal function code will perform other checks */
	}

	/*
	 * Assume callable will check arguments
	 */
	if (self->sel_self == NULL) { 
		result  = PyObject_Call(self->callable, args, kwargs);
		Py_DECREF(args);

	} else {
		Py_ssize_t argc = PyTuple_Size(args);
		PyObject* actual_args = PyTuple_New(argc+1);
		Py_ssize_t i;

		if (actual_args == NULL) {
			return NULL;
		}
		Py_INCREF(self->sel_self);
		PyTuple_SetItem(actual_args, 0, self->sel_self);
		for (i = 0; i < argc; i++) {
			PyObject* v = PyTuple_GET_ITEM(args, i);
			Py_XINCREF(v);
			PyTuple_SET_ITEM(actual_args, i+1, v);
		}
		result = PyObject_Call(self->callable, 
			actual_args, kwargs);	
		Py_DECREF(actual_args);
		Py_DECREF(args);
	}

	if ( result && (self->sel_self) && (PyObjCObject_Check(self->sel_self)) &&
	     ((PyObjCObject*)self->sel_self)->flags & PyObjCObject_kUNINITIALIZED) {

	     ((PyObjCObject*)self->sel_self)->flags &= ~PyObjCObject_kUNINITIALIZED;

	}

	return result;
}

static char* 
pysel_default_signature(PyObject* callable)
{
	PyCodeObject* func_code;
	Py_ssize_t    arg_count;
	char*         result;
	const unsigned char *buffer;
	Py_ssize_t    buffer_len;
	Py_ssize_t    i;
	int           was_none;
	
	if (PyFunction_Check(callable)) {
		func_code = (PyCodeObject*)PyFunction_GetCode(callable);
	} else if (PyMethod_Check(callable)) {
		func_code = (PyCodeObject*)PyFunction_GetCode(PyMethod_Function(callable));
	} else {
		PyErr_SetString(PyExc_TypeError,
			"Cannot calculate default method signature");
		return NULL;
	}

	arg_count = func_code->co_argcount;
	if (arg_count < 1) {
		PyErr_SetString(PyExc_TypeError,
			"Objective-C callable methods must take at least one argument");
		return NULL;
	}

	
	/* arguments + return-type + selector */
	result = PyMem_Malloc(arg_count+3);
	if (result == 0) {
		PyErr_NoMemory();
		return NULL;
	}

	/* We want: v@:@... (final sequence of arg_count-1 @-chars) */
	memset(result, _C_ID, arg_count+2);
	result[0] = _C_VOID;
	result[2] = _C_SEL;
	result[arg_count+2] = '\0';

	if (PyObject_AsReadBuffer(func_code->co_code, (const void **)&buffer, &buffer_len)) {
		return NULL;
	}

	/* 
	   Scan bytecode to find return statements.  If any non-bare return
	   statement exists, then set the return type to @ (id).
	*/
	was_none = 0;
	for (i=0; i<buffer_len; ++i) {
		int op = buffer[i];
		if (op == LOAD_CONST && buffer[i+1] == 0 && buffer[i+2] == 0) {
			was_none = 1;
		} else {
			if (op == RETURN_VALUE) {
				if (!was_none) {
					result[0] = _C_ID;
					break;
				}
			}
			was_none = 0;
		}
		if (op >= HAVE_ARGUMENT) {
			i += 2;
		}
	}
	return result;
}

static SEL
pysel_default_selector(PyObject* callable)
{
	char buf[1024]; 
	char* cur;
	PyObject* name = PyObject_GetAttrString(callable, "__name__");

	if (name == NULL) return NULL;

	if (!PyString_Check(name)) {
		return NULL;
	}

	strncpy(buf, PyString_AS_STRING(name), sizeof(buf)-1);

	cur = strchr(buf, '_');
	while (cur != NULL) {
		*cur = ':';
		cur = strchr(cur, '_');
	}
	return sel_registerName(buf);
}

SEL
PyObjCSelector_DefaultSelector(const char* methname)
{
	char buf[1024]; 
	char* cur;
	Py_ssize_t ln;

	strncpy(buf, methname, sizeof(buf)-1);
	ln = strlen(buf);

	cur = buf + ln;
	if (cur - buf > 3) {
		if (cur[-1] != '_') {
			return sel_registerName(buf);
		}

		if (cur[-1] == '_' && cur[-2] == '_') {
			cur[-2] = '\0';
			if (PyObjC_IsPythonKeyword(buf)) {
				return sel_registerName(buf);
			}
			cur[-2] = '_';
		}
	}

	/* Skip leading underscores, '_doFoo_' is probably '_doFoo:' in 
	 * Objective-C, not ':doFoo:'.
	 *
	 * Also if the name starts and ends with two underscores, return
	 * it unmodified. This avoids mangling of Python's special methods.
	 *
	 * Both are heuristics and could be the wrong choice, but either 
	 * form is very unlikely to exist in ObjC code.
	 */
	cur = buf;

	if (ln > 5) {
		if (cur[0] == '_' && cur[1] == '_' &&
		    cur[ln-1] == '_' && cur[ln-2] == '_') {
			return sel_registerName(buf);
		}
	}

	while (*cur == '_') {
		cur++;
	}

	/* Replace all other underscores by colons */
	cur = strchr(cur, '_');
	while (cur != NULL) {
		*cur = ':';
		cur = strchr(cur, '_');
	}
	return sel_registerName(buf);
}

static char
pytype_to_objc(char val)
{
	switch (val) {
	case 's': case 'z': case 'S': return _C_ID;
	case 'b': return _C_CHR;
	case 'h': return _C_SHT;
	case 'i': return _C_INT;
	case 'l': return _C_LNG;
	case 'c': return _C_CHR;
	case 'f': return _C_FLT;
	case 'd': return _C_DBL;
	case 'O': return _C_ID;
	default:
		PyErr_Format(PyExc_ValueError, "Unrecognized type character: %c", val);
		return 0;
	}
}

static char*
python_signature_to_objc(char* rettype, char* argtypes, char* buf, 
	size_t buflen)
{
	char* result = buf;

	if (buflen < 4) {
		PyErr_SetString(PyExc_RuntimeError, 
			"Too small buffer for python_signature_to_objc");
		return NULL;
	}
	if (rettype) {
		if (*rettype == 0) {
			*buf = _C_VOID;
		} else if (rettype[1] != 0) {
			PyErr_SetString(PyExc_ValueError,
				"Only recognizing simple type specifiers");
			return NULL;
		}
		*buf = pytype_to_objc(*rettype);
		if (*buf == 0) return NULL;
	} else {
		*buf = _C_VOID;
	}
	buf++;

	/* self and selector, required */
	*buf++ = '@';
	*buf++ = ':';

	buflen -= 3;

	if (!argtypes) {
		*buf++ = '\0';
		return result;
	}
	
	/* encode arguments */
	while (buflen > 0 && *argtypes) {
		*buf = pytype_to_objc(*argtypes++);
		if (*buf == 0) return NULL;
		buf++;
		buflen --;
	}

	if (buflen == 0) {
		PyErr_SetString(PyExc_RuntimeError, 
			"Too small buffer for python_signature_to_objc");
		return NULL;
	}
	*buf = 0;
	return result;
}
	

/* TODO: Check value of 'signature' */
static PyObject*
pysel_new(PyTypeObject* type __attribute__((__unused__)), 
	  PyObject* args, PyObject* kwds)
{
static	char*	keywords[] = { "function", "selector", "signature", 
				"isClassMethod", "argumentTypes", 
				"returnType", "isRequired", NULL };
	PyObjCPythonSelector* result;
	PyObject* callable;
	char*     signature = NULL;
	char* 	  argtypes = NULL;
	char*     rettype = NULL;
	char*	  selector = NULL;
	SEL       objc_selector;
	int	  class_method = 0;
	char      signature_buf[1024];
	int       required = 1;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|ssissi:selector",
			keywords, &callable, &selector, &signature,
			&class_method, &argtypes, &rettype, &required)) {
		return NULL;
	}

	if (signature != NULL && (rettype != NULL || argtypes != NULL)) {
		PyErr_SetString(PyExc_TypeError,
			"selector: provide either the objective-C signature, "
			"or the python signature but not both");
		return NULL;
	}

	if (rettype || argtypes) {
		signature = python_signature_to_objc(rettype, argtypes,
			signature_buf, sizeof(signature_buf));
		if (signature == NULL) return NULL;
	} else if (signature != NULL) {
		/* Check if the signature string is valid */
		const char* cur;

		cur = signature;
		while (*cur != '\0') {
			cur = PyObjCRT_SkipTypeSpec(cur);
			if (cur == NULL) {
				PyErr_SetString(
					PyExc_ValueError, 
					"invalid signature");
				return NULL;
			}
		}
	}


	if (callable != Py_None && !PyCallable_Check(callable)) {
		PyErr_SetString(PyExc_TypeError,
			"argument 'method' must be callable");
		return NULL;
	}

	if (PyObject_TypeCheck(callable, &PyClassMethod_Type)) {
		/* Special treatment for 'classmethod' instances */
		PyObject* tmp = PyObject_CallMethod(callable, "__get__", "OO",
				Py_None, &PyList_Type);
		if (tmp == NULL) {
			return NULL;
		} 

		if (PyFunction_Check(tmp)) {
			/* A 'staticmethod' instance, cannot convert */
			Py_DECREF(tmp);
			PyErr_SetString(PyExc_TypeError,
					"cannot use staticmethod as the "
					"callable for a selector.");
			return NULL;
		}
		
		callable = PyObject_GetAttrString(tmp, "im_func");
		Py_DECREF(tmp);
		if (callable == NULL) {
			return NULL;
		}
	} else {
		Py_INCREF(callable);
	}

	if (selector == NULL) {
		objc_selector = pysel_default_selector(callable);
	} else {
		objc_selector = sel_registerName(selector);
	}
		
	result = (PyObjCPythonSelector*)PyObjCSelector_New(callable,
			objc_selector, signature, class_method, nil);
	Py_DECREF(callable);
	if (!result) {
		return NULL;
	}
	if (required) {
		result->sel_flags |= PyObjCSelector_kREQUIRED;
	}
	return (PyObject *)result;
}

static PyObject*
pysel_descr_get(PyObject* _meth, PyObject* obj, PyObject* class)
{
	PyObjCPythonSelector* meth = (PyObjCPythonSelector*)_meth;
	PyObjCPythonSelector* result;

	if (meth->sel_self != NULL || obj == Py_None) {
		Py_INCREF(meth);
		return (PyObject*)meth;
	}

	/* Bind 'self' */
	if (meth->sel_flags & PyObjCSelector_kCLASS_METHOD) {
		obj = class;
		if (PyType_Check(obj) && PyType_IsSubtype((PyTypeObject*)obj, &PyObjCClass_Type)) {
			obj = PyObjCClass_ClassForMetaClass(obj);
		}
	}
	result = PyObject_New(PyObjCPythonSelector, &PyObjCPythonSelector_Type);
	result->sel_selector   = meth->sel_selector;
	result->sel_class   = meth->sel_class;
	result->sel_python_signature  = PyObjCUtil_Strdup(meth->sel_python_signature);
	if (result->sel_python_signature == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	if (meth->sel_native_signature) {
		result->sel_native_signature  = PyObjCUtil_Strdup(meth->sel_native_signature);
		if (result->sel_native_signature == NULL) {
			Py_DECREF(result);
			return NULL;
		}
	} else {
		result->sel_native_signature = NULL;
	}

	result->sel_methinfo = PyObjCSelector_GetMetadata((PyObject*)meth);
	Py_XINCREF(result->sel_methinfo);
	result->argcount = meth->argcount;
	result->numoutput = meth->numoutput;

	result->sel_self       = obj;
	result->sel_flags = meth->sel_flags;
	result->callable = meth->callable;
	if (result->sel_self) {
		Py_INCREF(result->sel_self);
	}
	if (result->callable) {
		Py_INCREF(result->callable);
	}
	return (PyObject*)result;
}


static void
pysel_dealloc(PyObject* obj)
{
	Py_DECREF(((PyObjCPythonSelector*)obj)->callable);
	(((PyObjCPythonSelector*)obj)->callable) = NULL;
	sel_dealloc(obj);
}

PyDoc_STRVAR(pysel_get_callable_doc, 
"Returns the python 'function' that implements this method.\n"
"\n"
);
static PyObject*
pysel_get_callable(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
	Py_INCREF(self->callable);
	return self->callable;
}

PyDoc_STRVAR(pysel_docstring_doc,
	"The document string for a method");
static PyObject*
pysel_docstring(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;

	PyObject* docstr = PyObject_GetAttrString(self->callable, "__doc__");
	return docstr;
}

static PyGetSetDef pysel_getset[] = {
	{
		"callable",
		pysel_get_callable,
		0,
		pysel_get_callable_doc,
		0
	},
	{
		"__doc__",
		pysel_docstring,
		0,
		pysel_docstring_doc,
		0
	},

	{
		NULL,
		NULL,
		NULL,
		NULL,
		0
	}
};

PyTypeObject PyObjCPythonSelector_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.python_selector",			/* tp_name */
	sizeof(PyObjCPythonSelector),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	pysel_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	pysel_repr,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	pysel_call,				/* tp_call */
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
	pysel_getset,				/* tp_getset */
	&PyObjCSelector_Type,			/* tp_base */
	0,					/* tp_dict */
	pysel_descr_get,			/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	0,					/* tp_new */
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

char* PyObjCSelector_Signature(PyObject* obj)
{
	return ((PyObjCSelector*)obj)->sel_python_signature;
}

Class      
PyObjCSelector_GetClass(PyObject* sel)
{
	if (!PyObjCNativeSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
		return NULL;
	}
	return ((PyObjCNativeSelector*)sel)->sel_class;
}

SEL      
PyObjCSelector_GetSelector(PyObject* sel)
{
	if (!PyObjCSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
		return NULL;
	}
	return ((PyObjCSelector*)sel)->sel_selector;
}


int   PyObjCSelector_Required(PyObject* obj)
{
	return (((PyObjCSelector*)obj)->sel_flags & PyObjCSelector_kREQUIRED) != 0;
}

int   PyObjCSelector_IsClassMethod(PyObject* obj)
{
	return (PyObjCSelector_GetFlags(obj) & PyObjCSelector_kCLASS_METHOD) != 0;
}

int   PyObjCSelector_GetFlags(PyObject* obj)
{
	return ((PyObjCSelector*)obj)->sel_flags;
}


/*
 * Find the signature of 'selector' in the list of protocols.
 */
static char*
find_protocol_signature(PyObject* protocols, SEL selector, int is_class_method)
{
	Py_ssize_t len;
	Py_ssize_t i;
	PyObject* proto;
	PyObject* info;

	if (!PyList_Check(protocols)) {
		PyErr_Format(PyObjCExc_InternalError,
			"Protocol-list is not a 'list', but '%s'",
			protocols->ob_type->tp_name);
		return NULL;
	}

	/* First try the explicit protocol definitions */
	len = PyList_GET_SIZE(protocols);
	for (i = 0; i < len; i++) {
		proto = PyList_GET_ITEM(protocols, i);
		if (proto == NULL) {
			PyErr_Clear();
			continue;
		}

		if (PyObjCFormalProtocol_Check(proto)) {
			const char* signature;
			
			signature = PyObjCFormalProtocol_FindSelectorSignature(
					proto, selector, is_class_method
			);
			if (signature != NULL) {
				return (char*)signature;
			}
		}

		info = PyObjCInformalProtocol_FindSelector(proto, selector, is_class_method);
		if (info != NULL) {
			return PyObjCSelector_Signature(info);
		}
	}

	/* Then check if another protocol users this selector */
	proto = PyObjCInformalProtocol_FindProtocol(selector);
	if (proto == NULL) {
		PyErr_Clear();
		return NULL;
	}

	info = PyObjCInformalProtocol_FindSelector(proto, selector, is_class_method);
	if (info != NULL) {
		if (PyList_Append(protocols, proto) < 0) {
			return NULL;
		}
		Py_INCREF(proto);
		return PyObjCSelector_Signature(info);
	}
	
	return NULL;
}

PyObject* 
PyObjCSelector_FromFunction(
	PyObject* pyname,
	PyObject* callable,
	PyObject* template_class,
	PyObject* protocols)
{
	char*     oc_name;
	SEL	  selector;
	Method    meth;
	int       is_class_method = 0;
	Class     oc_class = PyObjCClass_GetClass(template_class);
	PyObject* value;
	PyObject* super_sel;

	if (oc_class == NULL) {
		return NULL;
	}

	if (PyObjCPythonSelector_Check(callable)) {
		PyObjCPythonSelector* result;

		if (((PyObjCPythonSelector*)callable)->callable == NULL || ((PyObjCPythonSelector*)callable)->callable == Py_None) {
			PyErr_SetString(PyExc_ValueError, "selector object without callable");
			return NULL;
		}
		result = PyObject_New(PyObjCPythonSelector, &PyObjCPythonSelector_Type);
		result->sel_selector = ((PyObjCPythonSelector*)callable)->sel_selector;
		result->numoutput = ((PyObjCPythonSelector*)callable)->numoutput;
		result->argcount = ((PyObjCPythonSelector*)callable)->argcount;
		result->sel_methinfo = PyObjCSelector_GetMetadata(callable);
		Py_XINCREF(result->sel_methinfo);
		result->sel_class   = oc_class;
		result->sel_python_signature  = PyObjCUtil_Strdup(
				((PyObjCPythonSelector*)callable)->sel_python_signature);
		if (result->sel_python_signature == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		result->sel_native_signature = NULL;
		result->sel_self       = NULL;
		result->sel_flags = ((PyObjCPythonSelector*)callable)->sel_flags;
		result->callable = ((PyObjCPythonSelector*)callable)->callable;
		if (result->callable) {
			Py_INCREF(result->callable);
		}
		return (PyObject*)result;
	}

	if (!PyFunction_Check(callable) && !PyMethod_Check(callable) &&
		(callable->ob_type != &PyClassMethod_Type)) {
	
		PyErr_SetString(PyExc_TypeError, 
				"expecting function, method or classmethod");
		return NULL;
	}


	if (callable->ob_type == &PyClassMethod_Type) {
		/*
		 * This is a 'classmethod' or 'staticmethod'. 'classmethods'
		 * will be converted to class 'selectors', 'staticmethods' are
		 * returned as-is.
		 */
		PyObject* tmp;
		is_class_method = 1;
		tmp = PyObject_CallMethod(callable, "__get__", "OO",
				Py_None, template_class);
		if (tmp == NULL) {
			return NULL;
		}

		if (PyFunction_Check(tmp)) {
			/* A 'staticmethod', don't convert to a selector */
			Py_DECREF(tmp);
			Py_INCREF(callable);
			return callable;
		}

		callable = PyObject_GetAttrString(tmp, "im_func");
		Py_DECREF(tmp);
		if (callable == NULL) {
			return NULL;
		}
	}

	if (pyname == NULL) {
		/* No name specified, use the function name */
		pyname = PyObject_GetAttrString(callable, "__name__");
		if (pyname == NULL) {
			return NULL;
		}
		oc_name = PyString_AS_STRING(pyname);
		selector = PyObjCSelector_DefaultSelector(oc_name);
		Py_DECREF(pyname);
		oc_name = NULL;

	} else if (!PyString_Check(pyname)) {
		PyErr_SetString(PyExc_TypeError, 
			"method name must be a string");
		return NULL;
	} else {
		oc_name = PyString_AS_STRING(pyname);
		selector = PyObjCSelector_DefaultSelector(oc_name);
	}

	/* XXX: This seriously fails if a class method has a different signature
	 * than an instance method of the same name!
	 *
	 *
	 * We eagerly call PyObjCClass_FindSelector because some ObjC
	 * classes are not fully initialized until they are actually used,
	 * and the code below doesn't seem to count but PyObjCClass_FindSelector
	 * is.
	 */
	super_sel = PyObjCClass_FindSelector(template_class, selector, is_class_method);

	if (is_class_method) {
		meth = class_getClassMethod(oc_class, selector);
	} else {
		meth = class_getInstanceMethod(oc_class, selector);
		
		if (!meth && !sel_isEqual(selector, @selector(copyWithZone:)) && !sel_isEqual(selector, @selector(mutableCopyWithZone:))) {
		        /* Look for a classmethod, but don't do that for copyWithZone:
			 * because that method is commonly defined in Python, and
			 * overriding "NSObject +copyWithZone:" is almost certainly
			 * not the intended behaviour.
			 */
			meth = class_getClassMethod(oc_class, selector);
			if (meth) {
				is_class_method = 1;
			}
		}
	}

	if (meth) {
		/* The function overrides a method in the 
		 * objective-C class.
		 *
		 * Get the signature through the python wrapper,
		 * the user may have specified a more exact
		 * signature!
		 */
		if (super_sel == NULL) {
			return NULL;
		}

		value = PyObjCSelector_New(
			callable, 
			selector, 
			PyObjCSelector_Signature(super_sel),
			is_class_method,
			oc_class);
		Py_DECREF(super_sel);
	} else {
		char* signature = NULL;

		PyErr_Clear(); /* The call to PyObjCClass_FindSelector failed */
		if (protocols != NULL) {
			signature = find_protocol_signature(
					protocols, selector, is_class_method);
			if (signature == NULL && PyErr_Occurred()) {
				return NULL;
			}
		} 

		value = PyObjCSelector_New(
			callable, 
			selector, 
			signature,
			is_class_method,
			oc_class);
	}
	return value;
}

PyObject* PyObjCSelector_Copy(PyObject* selector)
{
	if (PyObjCPythonSelector_Check(selector)) {
		return pysel_descr_get(selector, NULL, NULL);
	} else if (PyObjCNativeSelector_Check(selector)) {
		return objcsel_descr_get(selector, NULL, NULL);
	} else {
		PyErr_SetString(PyExc_TypeError, "copy non-selector");
		return NULL;
	}
}
