#include "pyobjc.h"

/* XXX: Also store reference to subclass IMP? */
typedef struct {
	PyObject_HEAD
	IMP imp;
	PyObjC_CallFunc callfunc;
	PyObjCMethodSignature* signature;
	SEL selector;
	int flags;
} PyObjCIMPObject;

PyObject* PyObjCIMP_New(
		IMP imp, 
		SEL selector,
		PyObjC_CallFunc callfunc,
		PyObjCMethodSignature* signature,
		int flags)
{
	PyObjCIMPObject* result;

	result = PyObject_New(PyObjCIMPObject, &PyObjCIMP_Type);
	if (result == NULL) return NULL;

	result->imp = imp;
	result->selector = selector;
	result->callfunc = callfunc;
	result->signature = signature;
	if (signature) {
		PyObjCMethodSignature_Retain(signature);
	}
	result->flags = flags;
	return (PyObject*)result;
}

SEL PyObjCIMP_GetSelector(PyObject* self)
{
	if (!PyObjCIMP_Check(self)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	return ((PyObjCIMPObject*)self)->selector;
}

IMP PyObjCIMP_GetIMP(PyObject* self)
{
	if (!PyObjCIMP_Check(self)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	return ((PyObjCIMPObject*)self)->imp;
}

int PyObjCIMP_GetFlags(PyObject* self)
{
	if (!PyObjCIMP_Check(self)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	return ((PyObjCIMPObject*)self)->flags;
}

PyObjC_CallFunc PyObjCIMP_GetCallFunc(PyObject* self)
{
	if (!PyObjCIMP_Check(self)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	return ((PyObjCIMPObject*)self)->callfunc;
}

PyObjCMethodSignature*   PyObjCIMP_GetSignature(PyObject* self)
{
	if (!PyObjCIMP_Check(self)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	return ((PyObjCIMPObject*)self)->signature;
}

/* ========================================================================= */


static PyObject*
imp_call(PyObjCIMPObject* self, PyObject* args)
{
	PyObject* pyself;
	PyObjC_CallFunc execute = NULL;
	PyObject* res;
	int       argslen;
	PyObject* arglist;
	int       i;

	argslen = PyTuple_Size(args);
	if (argslen < 1) {
		PyErr_SetString(PyExc_TypeError, "Missing argument: self");
		return NULL;
	}

	pyself = PyTuple_GetItem(args, 0);
	if (pyself == NULL) {
		return NULL;
	}

	execute = self->callfunc;

	if (PyObjCObject_Check(pyself) 
		&& (PyObjCObject_Flags(pyself) & PyObjCObject_kUNINITIALIZED) 
		&& !(self->flags & PyObjCSelector_kINITIALIZER)) {

		char buf[1024];

		snprintf(buf, sizeof(buf), 
			"Calling IMP %s on unitialized object %p of class %s\n",
			PyObjCRT_SELName(self->selector),
			(void*)PyObjCObject_GetObject(pyself),
			GETISA(PyObjCObject_GetObject(pyself))->name);

		if (PyErr_Warn(PyExc_RuntimeWarning, buf) < 0) {
			return NULL;
		}
	}


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

	if (res && PyObjCObject_Check(res)) {
		if (self->flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
			((PyObjCObject*)res)->flags |= PyObjCObject_kUNINITIALIZED;
		}
		if (self->flags & PyObjCSelector_kINITIALIZER) {
			if (((PyObjCObject*)res)->flags & PyObjCObject_kUNINITIALIZED)
			{
				((PyObjCObject*)res)->flags &= 
					~PyObjCObject_kUNINITIALIZED;
			}
		}
				
		if (self->flags & PyObjCSelector_kDONATE_REF) {
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
imp_repr(PyObjCIMPObject* self)
{
	char buf[256];

	snprintf(buf, sizeof(buf), 
		"<IMP %s at %p>",
		PyObjCRT_SELName(self->selector),
		self);
	return PyString_FromString(buf);
}

static void
imp_dealloc(PyObjCIMPObject* self)
{
	PyObjCMethodSignature_Free(self->signature);
	PyObject_Free(self);
}

#if 0
PyDoc_STRVAR(imp_signature_doc, "Objective-C signature for the IMP");
static PyObject*
imp_signature(PyObjCIMPObject* self, void* closure __attribute__((__unused__)))
{
	/* XXX */
	return PyString_FromString(self->signature);
}
#endif

PyDoc_STRVAR(imp_selector_doc, "Objective-C name for the IMP");
static PyObject*
imp_selector(PyObjCIMPObject* self, void* closure __attribute__((__unused__)))
{
	return PyString_FromString(PyObjCRT_SELName(self->selector));
}

PyDoc_STRVAR(imp_class_method_doc, 
	"True if this is a class method, False otherwise");
static PyObject*
imp_class_method(PyObjCIMPObject* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->flags & PyObjCSelector_kCLASS_METHOD));
}

PyDoc_STRVAR(imp_donates_ref_doc, 
"True if this is method transfers ownership of the returned object, False otherwise\n"
"\n"
"NOTE: This field is used by the implementation to adjust reference counts."
);
static PyObject*
imp_donates_ref(PyObjCIMPObject* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->flags & PyObjCSelector_kDONATE_REF));
}

PyDoc_STRVAR(imp_returns_self_doc, 
"True if this is method returns a reallocated 'self', False otherwise\n"
"\n"
"NOTE: This field is used by the implementation."
);
static PyObject*
imp_returns_self(PyObjCIMPObject* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->flags & PyObjCSelector_kRETURNS_SELF));
}

PyDoc_STRVAR(imp_is_alloc_doc, 
"True if this is method returns a a freshly allocated object (uninitialized)\n"
"\n"
"NOTE: This field is used by the implementation."
);
static PyObject*
imp_is_alloc(PyObjCIMPObject* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->flags & PyObjCSelector_kRETURNS_UNINITIALIZED));
}
PyDoc_STRVAR(imp_is_initializer_doc, 
"True if this is method is an object initializer\n"
"\n"
"NOTE: This field is used by the implementation."
);
static PyObject*
imp_is_initializer(PyObjCIMPObject* self, void* closure __attribute__((__unused__)))
{
	return PyObjCBool_FromLong(0 != (self->flags & PyObjCSelector_kINITIALIZER));
}

static PyGetSetDef imp_getset[] = {
	{
		"isInitializer",
		(getter)imp_is_initializer,
		0,
		imp_is_initializer_doc,
		0
	},
	{
		"isAlloc",
		(getter)imp_is_alloc,
		0,
		imp_is_alloc_doc,
		0
	},
	{
		"doesDonateReference",
		(getter)imp_donates_ref,
		0,
		imp_donates_ref_doc,
		0
	},
	{
		"isClassMethod",
		(getter)imp_class_method,
		0,
		imp_class_method_doc,
		0
	},
#if 0
	{ 
		"signature", 
		(getter)imp_signature, 
		0,
		imp_signature_doc, 
		0
	},
#endif
	{ 
		"selector",  
		(getter)imp_selector, 
		0, 
		imp_selector_doc,
		0
	},
	{
		"returnsSelf",
		(getter)imp_returns_self,
		0,
		imp_returns_self_doc,
		0
	},
	{ 
		"__name__",  
		(getter)imp_selector, 
		0, 
		imp_selector_doc,
		0
	},
	{ 0, 0, 0, 0, 0 }
};


PyTypeObject PyObjCIMP_Type = {
	PyObject_HEAD_INIT(NULL)
	0,					/* ob_size */
	"objc.IMP",				/* tp_name */
	sizeof(PyObjCIMPObject),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	(destructor)imp_dealloc,		/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	(reprfunc)imp_repr,			/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	(ternaryfunc)imp_call,			/* tp_call */
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
	imp_getset,				/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
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


/* ========================================================================= */

static PyObject*
call_instanceMethodForSelector_(PyObject* method, PyObject* self, PyObject* args)
{
	PyObject* sel;
	SEL selector;
	struct objc_super super;
	IMP retval;
	PyObject* attr;
	PyObject* res;

	if (!PyArg_ParseTuple(args, "O", &sel)) {
		return NULL;
	}

	if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
		return NULL;
	}

	if (!PyObjCClass_Check(self)) {
		PyErr_Format(PyExc_TypeError, 
			"Expecting instance of 'objc.objc_class' as 'self', "
			"got '%s'", self->ob_type->tp_name);
		return NULL;
	}

	PyObjC_DURING
		RECEIVER(super) = PyObjCSelector_GET_CLASS(method);
		super.class = GETISA(PyObjCSelector_GET_CLASS(method));

		retval = (IMP)objc_msgSendSuper(&super,
			PyObjCSelector_GET_SELECTOR(method),
			selector);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		retval = NULL;

	PyObjC_ENDHANDLER

	if (retval == NULL) {
		if (PyErr_Occurred()) {
			return NULL;
		}
		Py_INCREF(Py_None);
		return Py_None;
	}

	attr = PyObjCClass_FindSelector(self, selector);
	if (attr == NULL) {
		return NULL;
	}

	if (!ObjCNativeSelector_Check(attr)) {
		PyErr_SetString(PyExc_TypeError, "XXX");
		return NULL;
	}

	res = PyObjCIMP_New(
			retval,
			selector,
			((ObjCNativeSelector*)attr)->sel_call_func,
			((ObjCNativeSelector*)attr)->sel_oc_signature,
			PyObjCSelector_GetFlags(attr)
		);
	Py_DECREF(attr);
	return res;
}

static PyObject*
call_methodForSelector_(PyObject* method, PyObject* self, PyObject* args)
{
	PyObject* sel;
	SEL selector;
	struct objc_super super;
	IMP retval;
	PyObject* attr;
	PyObject* res;

	if (!PyArg_ParseTuple(args, "O", &sel)) {
		return NULL;
	}

	if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
		return NULL;
	}

	if (PyObjCClass_Check(self)) {
		RECEIVER(super) = PyObjCSelector_GET_CLASS(method);
		super.class = GETISA(PyObjCSelector_GET_CLASS(method));
	} else {
		RECEIVER(super) = PyObjCObject_GetObject(self);
		super.class = PyObjCSelector_GetClass(method);
	}

	PyObjC_DURING
		retval = (IMP)objc_msgSendSuper(&super,
			PyObjCSelector_GET_SELECTOR(method),
			selector);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		retval = NULL;
	PyObjC_ENDHANDLER

	if (retval == NULL) {
		if (PyErr_Occurred()) {
			return NULL;
		}
		Py_INCREF(Py_None);
		return Py_None;
	}

	/* XXX:
	 * Let's hope class and instance methods with the same name have the
	 * same interface. I guess that will be true most of the time because
	 * the meta class is a subclass of NSObject.
	 */
	if (PyObjCClass_Check(self)) {
		attr = PyObjCClass_FindSelector(self, selector);
	} else {
		attr = PyObjCObject_FindSelector(self, selector);
	}
	if (attr == NULL) {
		return NULL;
	}

	if (!ObjCNativeSelector_Check(attr)) {
		PyErr_SetString(PyExc_TypeError, "XXX");
		return NULL;
	}

	res = PyObjCIMP_New(
			retval,
			selector,
			((ObjCNativeSelector*)attr)->sel_call_func,
			((ObjCNativeSelector*)attr)->sel_oc_signature,
			PyObjCSelector_GetFlags(attr)
		);
	Py_DECREF(attr);
	return res;
}

int PyObjCIMP_SetUpMethodWrappers(void)
{
	int r;

	r = PyObjC_RegisterMethodMapping(
			nil, 
			@selector(instanceMethodForSelector:),
			call_instanceMethodForSelector_,
			PyObjCUnsupportedMethod_IMP);
	if (r == -1) return -1;

	r = PyObjC_RegisterMethodMapping(
			nil, 
			@selector(methodForSelector:),
			call_methodForSelector_,
			PyObjCUnsupportedMethod_IMP);
	if (r == -1) return -1;

	return 0;
}
