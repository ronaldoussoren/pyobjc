/*
 * Implementation of 'native' and 'python' selectors
 *
 * TODO:
 * - Maybe it is better to fold the three types into one, especially because
 *   only one of them is exposed to python code.
 */
#include <Python.h>
#include "compile.h" /* from Python */
#include "pyobjc.h"
#include "objc_support.h"

/*
 * First section deals with registering replacement signatures for methods.
 * This is meant to be used to add _C_IN, _C_OUT and _C_INOUT specifiers for
 * pass-by-reference parameters.
 *
 * We register class names because the actual class may not yet be available. 
 * The list of replacments is not sorted in any way, it is expected to be 
 * short and the list won't be checked very often.\
 *
 * Alternative implementation: { SEL: [ (class_name, signature), ... ], ... }
 */
static PyObject* replacement_signatures = NULL;

struct replacement_signature
{
	char* class_name;
	SEL   selector;
	char* signature;
};

static void
free_replacement_signature(void* value)
{
	PyMem_Free(((struct replacement_signature*)value)->class_name);
	PyMem_Free(((struct replacement_signature*)value)->signature);
	PyMem_Free(value);
}

int 
ObjC_SignatureForSelector(char* class_name, SEL selector, char* signature)
{
	struct replacement_signature* value;
	PyObject*                      sublist;

	value = PyMem_Malloc(sizeof(*value));
	if (value == NULL) {
		PyErr_NoMemory();
		return -1;
	}
	value->class_name = ObjC_strdup(class_name);
	if (value->class_name == NULL) {
		PyMem_Free(value);
		PyErr_NoMemory();
		return -1;
	}
	
	value->selector = selector;
	value->signature = ObjC_strdup(signature);
	if (value->signature == NULL) {
		PyMem_Free(value);
		PyErr_NoMemory();
		return -1;
	}

	if (replacement_signatures == NULL) {
		replacement_signatures = PyDict_New();
	}

	sublist = PyDict_GetItemString(replacement_signatures, 
		(char*)SELNAME(value->selector));
	if (sublist == NULL) {
		sublist = PyList_New(0);
		PyDict_SetItemString(replacement_signatures,
			(char*)SELNAME(value->selector), sublist);
		Py_DECREF(sublist);
	}

	PyList_Append(sublist, 
		PyCObject_FromVoidPtr(value, free_replacement_signature));
	return 0;
}

static char* 
ObjC_FindReplacementSignature(Class cls, SEL selector)
{
	int i;
	int len;
	struct replacement_signature* cur ;
	Class found_class = nil;
	char* found_signature = NULL;
	PyObject* sublist;

	if (replacement_signatures == NULL) {
		return NULL;
	}

	sublist = PyDict_GetItemString(replacement_signatures, (char*)SELNAME(selector));
	if (sublist == NULL) return NULL;

	len = PyList_Size(sublist);
	for (i = 0; i < len; i++) {
		Class cur_class;

		cur = PyCObject_AsVoidPtr(
			PyList_GetItem(sublist, i));

		if (cur->selector != selector) {
			continue;
		}

		cur_class = objc_lookUpClass(cur->class_name);
		if (cur_class == nil) {
			continue;
		}

		if (!PyObjCClass_IsSubClass(cls, cur_class)) {
			continue;
		}

		if (found_class != NULL) {
			if (PyObjCClass_IsSubClass(found_class, cur_class)) {
				continue;
			}
		}
	
		found_class = cur_class;
		found_signature = cur->signature;
	}

	return found_signature;
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

static PyObject*
pysel_new(PyTypeObject* type, PyObject* args, PyObject* kwds);

PyDoc_STRVAR(base_signature_doc, "Objective-C signature for the method");
static PyObject*
base_signature(ObjCSelector* self, void* closure __attribute__((__unused__)))
{
	return PyString_FromString(self->sel_signature);
}

PyDoc_STRVAR(base_selector_doc, "Objective-C name for the method");
static PyObject*
base_selector(ObjCSelector* self, void* closure __attribute__((__unused__)))
{
	return PyString_FromString(SELNAME(self->sel_selector));
}

PyDoc_STRVAR(base_class_doc, "Objective-C Class that defines the method");
static PyObject*
base_class(ObjCNativeSelector* self, void* closure __attribute__((__unused__)))
{
	if (self->sel_class != nil) {
		return PyObjCClass_New(self->sel_class);
	}
	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(base_class_method_doc, 
	"True if this is a class method, False otherwise");
static PyObject*
base_class_method(ObjCNativeSelector* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->sel_flags & ObjCSelector_kCLASS_METHOD));
}

PyDoc_STRVAR(base_required_doc, 
	"True if this is a required method, False otherwise");
static PyObject*
base_required(ObjCNativeSelector* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->sel_flags & ObjCSelector_kREQUIRED));
}

PyDoc_STRVAR(base_donates_ref_doc, 
"True if this is method transfers ownership of the returned object, False otherwise\n"
"\n"
"NOTE: This field is used by the implementation to adjust reference counts."
);
static PyObject*
base_donates_ref(ObjCNativeSelector* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->sel_flags & ObjCSelector_kDONATE_REF));
}
static int
base_donates_ref_setter(ObjCNativeSelector* self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
	if (PyObject_IsTrue(newVal)) {
		self->sel_flags |= ObjCSelector_kDONATE_REF;
	} else {
		self->sel_flags &= ~ObjCSelector_kDONATE_REF;
	}
	return 0;
}

PyDoc_STRVAR(base_returns_self_doc, 
"True if this is method returns a reallocated 'self', False otherwise\n"
"\n"
"NOTE: This field is used by the implementation."
);
static PyObject*
base_returns_self(ObjCNativeSelector* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->sel_flags & ObjCSelector_kRETURNS_SELF));
}
static int
base_returns_self_setter(ObjCNativeSelector* self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
	if (PyObject_IsTrue(newVal)) {
		self->sel_flags |= ObjCSelector_kRETURNS_SELF;
	} else {
		self->sel_flags &= ~ObjCSelector_kRETURNS_SELF;
	}
	return 0;
}
PyDoc_STRVAR(base_is_alloc_doc, 
"True if this is method returns a a freshly allocated object (uninitialized)\n"
"\n"
"NOTE: This field is used by the implementation."
);
static PyObject*
base_is_alloc(ObjCNativeSelector* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->sel_flags & ObjCSelector_kRETURNS_UNINITIALIZED));
}
static int
base_is_alloc_setter(ObjCNativeSelector* self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
	if (PyObject_IsTrue(newVal)) {
		self->sel_flags |= ObjCSelector_kRETURNS_UNINITIALIZED;
	} else {
		self->sel_flags &= ~ObjCSelector_kRETURNS_UNINITIALIZED;
	}
	return 0;
}
PyDoc_STRVAR(base_is_initializer_doc, 
"True if this is method is an object initializer\n"
"\n"
"NOTE: This field is used by the implementation."
);
static PyObject*
base_is_initializer(ObjCNativeSelector* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->sel_flags & ObjCSelector_kINITIALIZER));
}
static int
base_is_initializer_setter(ObjCNativeSelector* self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
	if (PyObject_IsTrue(newVal)) {
		self->sel_flags |= ObjCSelector_kINITIALIZER;
	} else {
		self->sel_flags &= ~ObjCSelector_kINITIALIZER;
	}
	return 0;
}

static PyGetSetDef base_getset[] = {
	{
		"isInitializer",
		(getter)base_is_initializer,
		(setter)base_is_initializer_setter,
		base_is_initializer_doc,
		0
	},
	{
		"isAlloc",
		(getter)base_is_alloc,
		(setter)base_is_alloc_setter,
		base_is_alloc_doc,
		0
	},
	{
		"doesDonateReference",
		(getter)base_donates_ref,
		(setter)base_donates_ref_setter,
		base_donates_ref_doc,
		0
	},
	{
		"isRequired",
		(getter)base_required,
		0,
		base_required_doc,
		0
	},
	{
		"isClassMethod",
		(getter)base_class_method,
		0,
		base_class_method_doc,
		0
	},
	{ 
		"definingClass", 
		(getter)base_class, 
		0,
		base_class_doc, 
		0
	},
	{ 
		"signature", 
		(getter)base_signature, 
		0,
		base_signature_doc, 
		0
	},
	{ 
		"selector",  
		(getter)base_selector, 
		0, 
		base_selector_doc,
		0
	},
	{
		"returnsSelf",
		(getter)base_returns_self,
		(setter)base_returns_self_setter,
		base_returns_self_doc,
		0
	},
	{ 
		"__name__",  
		(getter)base_selector, 
		0, 
		base_selector_doc,
		0
	},
	{ 0, 0, 0, 0, 0 }
};


static void
sel_dealloc(PyObject* object)
{
	ObjCSelector* self = (ObjCSelector*)object;	

	/* HACK */
	if (ObjCNativeSelector_Check(self)) {
		[((ObjCNativeSelector*)self)->sel_oc_signature release];
	}

	PyMem_Free(self->sel_signature);
	self->sel_signature = NULL;
	if (self->sel_self) { 
		Py_DECREF(self->sel_self); 
		self->sel_self = NULL;
	}
	object->ob_type->tp_free(object);
}

/* Ronald: This is probably a bit too much documentation... */
PyDoc_STRVAR(base_selector_type_doc,
"selector(function, [, signature] [, selector] [, isClassMethod=0]\n"
"    [, returnType] [, argumentTypes] [, isRequired=True]) -> selector\n"
"\n"
"Return an Objective-C method from a function. The other arguments \n"
"specify attributes of the Objective-C method.\n"
"\n"
"function:\n"
"  A function object with at least one argument. The first argument will\n"
"  be used to pass 'self'. This argument may be None when defining an\n"
"  informal_protocol object.\n"
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
"  True if the method is a class method, false otherwise"
"isRequired:\n"
"  True if this is a required method in an informal protocol, False\n"
"  otherwise. The default value is 'True'. This argument is only used\n"
"  when defining an 'informal_protocol' object.\n"
);
PyTypeObject ObjCSelector_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.selector",			/* tp_name */
	sizeof(ObjCSelector),			/* tp_basicsize */
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
	0,					/* tp_methods */
	0,					/* tp_members */
	base_getset,				/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
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
        0                                       /* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
        , 0                                     /* tp_del */
#endif
};


/*
 * Selector type for 'native' selectors (that is, selectors that are not
 * implemented as python methods)
 */
static PyObject*
objcsel_repr(ObjCNativeSelector* sel)
{
	char buf[256];

	if (sel->sel_self == NULL) {
		snprintf(buf, sizeof(buf),
			"<unbound native-selector %s in %s>", 
			SELNAME(sel->sel_selector), sel->sel_class->name);
	} else {
		PyObject* selfrepr = PyObject_Repr(sel->sel_self);
		if (selfrepr == NULL) {
			return NULL;
		}
		if (!PyString_Check(selfrepr)) {
			Py_DECREF(selfrepr);
			return NULL;
		}
		snprintf(buf, sizeof(buf),
			"<native-selector %s of %s>", 
			SELNAME(sel->sel_selector),
			PyString_AS_STRING(selfrepr));
		Py_DECREF(selfrepr);
	}

	return PyString_FromString(buf);
}


static PyObject*
objcsel_call(ObjCNativeSelector* self, PyObject* args)
{
	PyObject* pyself = self->sel_self;
	ObjC_CallFunc_t execute = NULL;
	PyObject* res;

	if (pyself == NULL) {
		int       argslen;
		argslen = PyTuple_Size(args);
		if (argslen < 1) {
			ObjCErr_Set(PyExc_TypeError,
				"Missing self argument\n");
			return NULL;
		}
		pyself = PyTuple_GetItem(args, 0);
		if (pyself == NULL) {
			return NULL;
		}
	}

	if (self->sel_call_func) {
		execute = self->sel_call_func;
	} else {
		execute = ObjC_FindCallFunc(
				self->sel_class, 
				self->sel_selector);
		if (execute == NULL) return NULL;
		self->sel_call_func = execute;
	}

	if (self->sel_self && PyObjCObject_Check(self->sel_self) 
	    && (((PyObjCObject*)self->sel_self)->flags & PyObjCObject_kUNINITIALIZED)
	    && !(self->sel_flags & ObjCSelector_kINITIALIZER)) {

		PySys_WriteStderr(
			"Calling non-initializer (%s) on unitialized object %p of class %s\n",
			SELNAME(self->sel_selector),
			(void*)PyObjCObject_GetObject(self->sel_self),
			GETISA(PyObjCObject_GetObject(self->sel_self))->name);
	}



	if (self->sel_self != NULL) {
		res = execute((PyObject*)self, self->sel_self, args);
	} else {
		PyObject* arglist;
		int       i;
		int       argslen;

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

		res = execute((PyObject*)self, pyself, arglist);
		Py_DECREF(arglist);
	}

	if (res && PyObjCObject_Check(res)) {
		if (self->sel_flags & ObjCSelector_kRETURNS_UNINITIALIZED) {
			((PyObjCObject*)res)->flags |= PyObjCObject_kUNINITIALIZED;
		}
		if (self->sel_flags & ObjCSelector_kINITIALIZER) {
			if (((PyObjCObject*)res)->flags & PyObjCObject_kUNINITIALIZED)
			{
				((PyObjCObject*)res)->flags &= 
					~PyObjCObject_kUNINITIALIZED;
			}
		}
				
		if (self->sel_flags & ObjCSelector_kDONATE_REF) {
			/* Ownership transfered to us, but 'execute' method has
			 * increased retainCount, the retainCount is now one 
			 * too high
			 */
			id obj = PyObjCObject_GetObject(res);
			[obj release];
		}
	}
	return res;
}

static PyObject*
objcsel_descr_get(ObjCNativeSelector* meth, PyObject* obj, PyObject* class)
{
	ObjCNativeSelector* result;
	
	if (meth->sel_self != NULL || obj == Py_None) {
		Py_INCREF(meth);
		return (PyObject*)meth;
	} 

	/* Bind 'self' */
	if (meth->sel_flags & ObjCSelector_kCLASS_METHOD) {
		obj = class;
	}
	result = PyObject_New(ObjCNativeSelector, &ObjCNativeSelector_Type);
	result->sel_selector   = meth->sel_selector;
	result->sel_signature  = ObjC_strdup(meth->sel_signature);
	if (result->sel_signature == NULL) {
		Py_DECREF(result);
		return PyErr_NoMemory();
	}
	result->sel_flags = meth->sel_flags;
	result->sel_class = meth->sel_class;

	if (meth->sel_call_func == NULL) {
		meth->sel_call_func = ObjC_FindCallFunc(meth->sel_class,
			meth->sel_selector);
	}
	result->sel_call_func = meth->sel_call_func;

	if (meth->sel_oc_signature == NULL) {
		meth->sel_oc_signature = [NSMethodSignature signatureWithObjCTypes:meth->sel_signature];
		[meth->sel_oc_signature retain];
	}
	result->sel_oc_signature = meth->sel_oc_signature;
	[result->sel_oc_signature retain];

	result->sel_self       = obj;
	if (result->sel_self) {
		Py_INCREF(result->sel_self);
	}

	return (PyObject*)result;
}



PyTypeObject ObjCNativeSelector_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.native_selector",			/* tp_name */
	sizeof(ObjCNativeSelector),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	sel_dealloc,				/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	(reprfunc)objcsel_repr,			/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	(ternaryfunc)objcsel_call,		/* tp_call */
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
	&ObjCSelector_Type,			/* tp_base */
	0,					/* tp_dict */
	(descrgetfunc)objcsel_descr_get,	/* tp_descr_get */
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
        0                                       /* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
        , 0                                     /* tp_del */
#endif
};


static char*
typestr_from_NSMethodSignature(NSMethodSignature* sig, char* buf, size_t buflen)
{
	char* result = buf;
	int arg_count = [sig numberOfArguments];
	int i;

	snprintf(buf, buflen, "%s", [sig methodReturnType]);
	buflen -= strlen(buf);
	buf += strlen(buf);

	if (buflen == 0) return NULL;

	for (i = 0; i < arg_count; i++) {
		snprintf(buf, buflen, "%s", [sig getArgumentTypeAtIndex:i]);
		buflen -= strlen(buf);
		buf += strlen(buf);

		if (buflen == 0) return NULL;
	}

	return result;
}
	

PyObject*
ObjCSelector_FindNative(PyObject* self, char* name)
{
	SEL   sel = ObjCSelector_DefaultSelector(name);

	NSMethodSignature* methsig;
	char  buf[1024];

	if (PyObjCClass_Check(self)) {
		Class cls = PyObjCClass_GetClass(self);

		if (!cls) {
			ObjCErr_Set(PyExc_AttributeError,
				"No attribute %s", name);
			return NULL;
		}

		if (strcmp(cls->name, "NSProxy") == 0) {
			if (sel == @selector(methodSignatureForSelector:)) {
				ObjCErr_Set(PyExc_AttributeError,
					"Cannot access NSProxy.%s", name);
				return NULL;
			}
		}

		if ([cls instancesRespondToSelector:sel]) {
			methsig = [cls instanceMethodSignatureForSelector:sel];
			return ObjCSelector_NewNative(cls, sel, 
				typestr_from_NSMethodSignature(methsig, buf, sizeof(buf)), 0);
		} else if (nil != (methsig = [cls methodSignatureForSelector:sel])) {
			return ObjCSelector_NewNative(cls, sel, 
				typestr_from_NSMethodSignature(methsig, buf, sizeof(buf)), 1);
		} else {
			ObjCErr_Set(PyExc_AttributeError,
				"No attribute %s", name);
			return NULL;
		}
	} else if (PyObjCObject_Check(self)) {
		id object;

		object = PyObjCObject_GetObject(self);

		if (nil != (methsig = [object methodSignatureForSelector:sel])){
			ObjCNativeSelector* res;

			res =  (ObjCNativeSelector*)ObjCSelector_NewNative(
				GETISA(object), sel, 
				typestr_from_NSMethodSignature(methsig, 
					buf, sizeof(buf)), 0);
			if (res != NULL) {
				/* Bind the method to self */
				res->sel_self = self;
				Py_INCREF(res->sel_self);
			}
			return (PyObject*)res;
		} else {
			ObjCErr_Set(PyExc_AttributeError,
				"No attribute %s", name);
			return NULL;
		}
	} else {
		ObjCErr_Set(PyExc_RuntimeError,
			"ObjCSelector_FindNative called on bad object");
		return NULL;
	}
}



PyObject*
ObjCSelector_NewNative(Class class, 
			SEL selector, char* signature, int class_method)
{
	ObjCNativeSelector* result;
	char* repl_sig;

	repl_sig = ObjC_FindReplacementSignature(class, selector);
	if (repl_sig) {
		signature = repl_sig;
	}

	result = PyObject_New(ObjCNativeSelector, &ObjCNativeSelector_Type);
	if (result == NULL) return NULL;

	result->sel_selector = selector;
	result->sel_signature = ObjC_strdup(signature);
	if (result->sel_signature == NULL) {
		Py_DECREF(result);
		return PyErr_NoMemory();
	}
	result->sel_self = NULL;
	result->sel_class = class;
	result->sel_call_func = NULL;
	result->sel_oc_signature = NULL;
	result->sel_flags = 0;
	if (class_method) {
		result->sel_flags |= ObjCSelector_kCLASS_METHOD;
	}
	return (PyObject*)result;
}

PyObject*
ObjCSelector_New(PyObject* callable, 
	SEL selector, char* signature, int class_method)
{
	ObjCPythonSelector* result;

	result = PyObject_New(ObjCPythonSelector, &ObjCPythonSelector_Type);
	if (result == NULL) return NULL;

	result->sel_selector = selector;
	if (signature == NULL) {
		result->sel_signature = pysel_default_signature(callable);
	} else {
		result->sel_signature = ObjC_strdup(signature);
		if (result->sel_signature == NULL) {
			Py_DECREF(result);
			return PyErr_NoMemory();
		}
	}
	result->sel_self = NULL;
	result->sel_class = NULL;
	result->sel_flags = 0;
	result->callable = callable;
	if (class_method) {
		result->sel_flags |= ObjCSelector_kCLASS_METHOD;
	}
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
pysel_repr(ObjCPythonSelector* sel)
{
	char buf[256];

	if (sel->sel_self == NULL) {
		if (sel->sel_class) {
			snprintf(buf, sizeof(buf),
				"<unbound selector %s of %s>", 
				SELNAME(sel->sel_selector),
				sel->sel_class->name);
		} else {
			snprintf(buf, sizeof(buf),
				"<unbound selector %s>", 
				SELNAME(sel->sel_selector));
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
		snprintf(buf, sizeof(buf),
			"<selector %s of %s>", 
			SELNAME(sel->sel_selector),
			PyString_AS_STRING(selfrepr));
		Py_DECREF(selfrepr);
	}

	return PyString_FromString(buf);
}

static PyObject*
pysel_call(ObjCPythonSelector* self, PyObject* args, PyObject* kwargs)
{
	PyObject* result;

	if (self->callable == NULL) {
		ObjCErr_Set(PyExc_TypeError, 
			"Calling abstract methods with selector %s",
			self->sel_selector);
		return NULL;
	}

	if (!PyMethod_Check(self->callable)) {
		if (self->sel_self == NULL) {
			PyObject* self_arg;
			if (PyTuple_Size(args) < 1) {
				PyErr_SetString(ObjCExc_error, "need self argument");
				return NULL;
			}
			self_arg = PyTuple_GetItem(args, 0);
			if (!PyObjCObject_Check(self_arg) && !PyObjCClass_Check(self_arg)) {
				PyErr_SetString(ObjCExc_error, "bad self type");
				abort();
				return NULL;
			}
		}

		/* normal function code will perform other checks */
	}

	/* TODO: Do same if self->sel_self is NULL */
	if ( !(self->sel_flags & ObjCSelector_kINITIALIZER)
	     && (self->sel_self) && (PyObjCObject_Check(self->sel_self)) &&
	     ((PyObjCObject*)self->sel_self)->flags & PyObjCObject_kUNINITIALIZED) {

		PySys_WriteStderr(
		    "Calling non-initializer (%s) on unitialized object %p of class %s\n",
		    SELNAME(self->sel_selector),
		    (void*)PyObjCObject_GetObject(self->sel_self),
		    GETISA(PyObjCObject_GetObject(self->sel_self))->name);

	}

	/*
	 * Assume callable will check arguments
	 */
	if (self->sel_self == NULL) { 
		result  = PyObject_Call(self->callable, args, kwargs);

	} else {
		int       argc = PyTuple_Size(args);
		PyObject* actual_args = PyTuple_New(argc+1);
		int       i;

		if (actual_args == NULL) {
			return NULL;
		}
		Py_INCREF(self->sel_self);
		PyTuple_SetItem(actual_args, 0, self->sel_self);
		for (i = 0; i < argc; i++) {
			PyObject* v = PyTuple_GET_ITEM(args, i);
			/*if (v == NULL) return NULL;*/
			Py_XINCREF(v);
			PyTuple_SET_ITEM(actual_args, i+1, v);
		}
		result = PyObject_Call(self->callable, 
			actual_args, kwargs);	
		Py_DECREF(actual_args);
	}

	/* TODO: Do same if self->sel_self is NULL */
	if ( result && (self->sel_flags & ObjCSelector_kINITIALIZER)
	     && (self->sel_self) && (PyObjCObject_Check(self->sel_self)) &&
	     ((PyObjCObject*)self->sel_self)->flags & PyObjCObject_kUNINITIALIZED) {

	     ((PyObjCObject*)self->sel_self)->flags &= ~PyObjCObject_kUNINITIALIZED;
	    
	}

	return result;
}

static char* 
pysel_default_signature(PyObject* callable)
{
	PyCodeObject* func_code;
	int           arg_count;
	char*	      result;
	
	if (PyFunction_Check(callable)) {
		func_code = (PyCodeObject*)PyFunction_GetCode(callable);
	} else if (PyMethod_Check(callable)) {
		func_code = (PyCodeObject*)PyFunction_GetCode(PyMethod_Function(callable));
	} else {
		PyErr_SetString(PyExc_TypeError,
			"Cannot calculate signature");
		return NULL;
	}

	arg_count = func_code->co_argcount;

	/* arguments + return-type + selector */
	result = PyMem_Malloc(arg_count+3);
	if (result == 0) {
		PyErr_NoMemory();
		return NULL;
	}

	/* We want: @@:@... (final sequence of arg_count-1 @-chars) */
	memset(result, '@', arg_count+2);
	result[2] = ':';
	result[arg_count+2] = '\0';

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

	snprintf(buf, sizeof(buf), "%s", PyString_AS_STRING(name));	

	cur = strchr(buf, '_');
	while (cur != NULL) {
		*cur = ':';
		cur = strchr(cur, '_');
	}
	return sel_registerName(buf);
}

SEL
ObjCSelector_DefaultSelector(char* methname)
{
	char buf[1024]; 
	char* cur;

	snprintf(buf, sizeof(buf), "%s", methname);

	cur = strchr(buf, '_');
	while (cur != NULL) {
		*cur = ':';
		cur = strchr(cur, '_');
	}
	return sel_registerName(buf);
}

static char
pytype_to_objc(char val)
{
	char buf[128];
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
		snprintf(buf, sizeof(buf), 
			"Unrecognized type character: %c", val);
		PyErr_SetString(PyExc_ValueError, buf);
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
	

static PyObject*
pysel_new(PyTypeObject* type __attribute__((__unused__)), 
	  PyObject* args, PyObject* kwds)
{
static	char*	keywords[] = { "method", "selector", "signature", 
				"isClassMethod", "argumentTypes", 
				"returnType", "isRequired", NULL };
	ObjCPythonSelector* result;
	PyObject* callable;
	char*     signature = NULL;
	char* 	  argtypes = NULL;
	char*     rettype = NULL;
	char*	  selector = NULL;
	int	  class_method=0;
	char      signature_buf[1024];
	int       required=1;

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
	}


	if (callable != Py_None && !PyCallable_Check(callable)) {
		PyErr_SetString(PyExc_TypeError,
			"argument 'method' must be callable");
		return NULL;
	}

	result = (ObjCPythonSelector*)PyObject_New(
			ObjCPythonSelector, &ObjCPythonSelector_Type);
	if (signature == NULL) {
		result->sel_signature = pysel_default_signature(callable);
		if (result->sel_signature == NULL) {
			Py_DECREF(result);
			return NULL;
		}
	} else {
		result->sel_signature = ObjC_strdup(signature);
		if (result->sel_signature == 0) {
			return PyErr_NoMemory();
		}
	}
	if (selector == NULL) {
		result->sel_selector = pysel_default_selector(callable);
	} else {
		result->sel_selector = sel_registerName(selector);
	}
	result->callable = callable;
	result->sel_self = NULL;
	result->sel_flags = 0;
	result->sel_class = NULL;
	if (class_method) {
		result->sel_flags |= ObjCSelector_kCLASS_METHOD;
	}
	if (required) {
		result->sel_flags |= ObjCSelector_kREQUIRED;
	}
	Py_INCREF(callable);

	return (PyObject*)result;
}

static PyObject*
pysel_descr_get(ObjCPythonSelector* meth, PyObject* obj, PyObject* class)
{
	ObjCPythonSelector* result;

	if (meth->sel_self != NULL || obj == Py_None) {
		Py_INCREF(meth);
		return (PyObject*)meth;
	}

	/* Bind 'self' */
	if (meth->sel_flags & ObjCSelector_kCLASS_METHOD) {
		obj = class;
	}
	result = PyObject_New(ObjCPythonSelector, &ObjCPythonSelector_Type);
	result->sel_selector   = meth->sel_selector;
	result->sel_class   = meth->sel_class;
	result->sel_signature  = ObjC_strdup(meth->sel_signature);
	if (result->sel_signature == NULL) {
		Py_DECREF(result);
		return PyErr_NoMemory();
	}
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
	Py_DECREF(((ObjCPythonSelector*)obj)->callable);
	sel_dealloc(obj);
}

PyTypeObject ObjCPythonSelector_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.python_selector",			/* tp_name */
	sizeof(ObjCPythonSelector),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	pysel_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	(reprfunc)pysel_repr,			/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	(ternaryfunc)pysel_call,		/* tp_call */
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
	&ObjCSelector_Type,			/* tp_base */
	0,					/* tp_dict */
	(descrgetfunc)pysel_descr_get,		/* tp_descr_get */
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
        0                                       /* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
        , 0                                     /* tp_del */
#endif
};

char* ObjCSelector_Signature(PyObject* obj)
{
	return ((ObjCSelector*)obj)->sel_signature;
}

SEL   ObjCSelector_Selector(PyObject* obj)
{
	return ((ObjCSelector*)obj)->sel_selector;
}

int   ObjCSelector_Required(PyObject* obj)
{
	return (((ObjCSelector*)obj)->sel_flags & ObjCSelector_kREQUIRED) != 0;
}
