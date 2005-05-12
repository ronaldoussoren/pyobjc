/*
 * Implementation of the class PyObjCClass_Type, that is the class representing
 * Objective-C classes.
 *
 */
#include "pyobjc.h"

#include <stddef.h>

/*
 * Support for NSData/NSMutableData to have buffer API
 *
 */

static
int nsdata_getreadbuffer(PyObject *pyself, int segment __attribute__((unused)), void **ptrptr) {
	NSData *self = (NSData *)PyObjCObject_GetObject(pyself);
	assert(segment == 0);
	if (ptrptr != NULL) {
		*ptrptr = (void *)[self bytes];
	}
	return (int)[self length];
}

static
int nsmutabledata_getwritebuffer(PyObject *pyself, int segment __attribute__((unused)), void **ptrptr) {
	NSMutableData *self = (NSMutableData *)PyObjCObject_GetObject(pyself);
	assert(segment == 0);
	if (ptrptr != NULL) {
		*ptrptr = (void *)[self mutableBytes];
	}
	return (int)[self length];
}

static
int nsdata_getsegcount(PyObject *pyself, int *lenp) {
	NSData *self = (NSData *)PyObjCObject_GetObject(pyself);
	if (lenp != NULL) {
		*lenp = (int)[self length];
	}
	return 1;
}

static PyBufferProcs nsdata_as_buffer = {
	(getreadbufferproc)&nsdata_getreadbuffer,
	NULL,
	(getsegcountproc)&nsdata_getsegcount,
	NULL
};

static PyBufferProcs nsmutabledata_as_buffer = {
	(getreadbufferproc)&nsdata_getreadbuffer,
	(getwritebufferproc)&nsmutabledata_getwritebuffer,
	(getsegcountproc)&nsdata_getsegcount,
	NULL
};


PyDoc_STRVAR(class_doc,
"objc_class(name, bases, dict) -> a new Objective-C class\n"
"\n"
"objc_class is the meta-type for Objective-C classes. It should not be\n"
"necessary to manually create instances of this type, those are \n"
"created by subclassing and existing Objective-C class.\n"
"\n"
"The list of bases must start with an existing Objective-C class, and \n"
"cannot contain other Objective-C classes. The list may contain\n"
"informal_interface objects, those are used during the calculation of\n"
"method signatures and will not be visible in the list of base-classes\n"
"of the created class."
);

PyObject* PyObjC_ClassExtender = NULL;

static int add_class_fields(Class objc_class, PyObject* dict);
static int add_convenience_methods(Class cls, PyObject* type_dict);
static int update_convenience_methods(PyObject* cls);

/*
 *
 *  Class Registry
 *
 */

/*!
 * @const class_registry
 * @discussion
 *    This structure is used to keep references to all class objects created
 *    by this module. This is necessary to be able to avoid creating two
 *    wrappers for an Objective-C class.
 *
 *    The key is the Objective-C class, the value is its wrapper.
 */
static NSMapTable* class_registry = NULL;

/*!
 * @function objc_class_register
 * @abstract Add a class to the class registry
 * @param objc_class An Objective-C class
 * @param py_class   The python wrapper for the Objective-C class
 * @result Returns -1 on error, 0 on success
 */
static int 
objc_class_register(Class objc_class, PyObject* py_class)
{
	if (class_registry == NULL) {
		class_registry = NSCreateMapTable(
			PyObjCUtil_PointerKeyCallBacks,
			PyObjCUtil_PointerValueCallBacks, 
			PYOBJC_EXPECTED_CLASS_COUNT);
	}

	if (NSMapGet(class_registry, objc_class)) {
		PyErr_BadInternalCall();
		return -1;
	}

	Py_INCREF(py_class); 
	NSMapInsert(class_registry, objc_class, py_class);

	return 0;
}

#if 0 /* Not used at the moment */
/*!
 * @function objc_class_unregister
 * @abstract Remove a class from the class registry
 * @param objc_class An Objective-C class
 * @result Returns -1 on error, 0 on success
 */
static int 
objc_class_unregister(Class objc_class)
{
	PyObject* val;
	if (class_registry == NULL) return 0;

	val = NSMapGet(class_registry, objc_class);
	Py_XDECREF(val);
	NSMapRemove(class_registry, objc_class);
	return 0;
}
#endif


/*!
 * @function objc_class_locate
 * @abstract Find the Python wrapper for an Objective-C class
 * @param objc_class An Objective-C class
 * @result Returns the Python wrapper for the class, or NULL
 * @discussion
 *     This function does not raise an Python exception when the
 *     wrapper cannot be found.
 */
static PyObject*
objc_class_locate(Class objc_class)
{
	PyObject* result;

	if (class_registry == NULL) return NULL;
	if (objc_class == NULL) return NULL;

	result = NSMapGet(class_registry, objc_class);
	Py_XINCREF(result);
	return result;
}


/*
 * Create a new objective-C class, as a subclass of 'type'. This is
 * PyObjCClass_Type.tp_new.
 *
 * Note: This function creates new _classes_
 */


static PyObject*
class_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", "bases", "dict", NULL };
	char* name;
	PyObject* bases;
	PyObject* dict;
	PyObject* res;
	PyObject* v;
	int       i;
	int       len;
	Class      objc_class = NULL;
	Class	   super_class = NULL;
	PyObject*  py_super_class = NULL;
	PyObjCClassObject* info;
	PyObject* protocols;
	PyObject* real_bases;
	PyObject* delmethod;
	PyObject* useKVOObj;
	PyObjCRT_Ivar_t var;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sOO:__new__",
			keywords, &name, &bases, &dict)) {
		return NULL;
	}

	if (!PyTuple_Check(bases)) {
		PyErr_SetString(PyExc_TypeError, "'bases' must be tuple");
		return NULL;
	}

	len  = PyTuple_Size(bases);
	if (len < 1) {
		PyErr_SetString(PyExc_TypeError, "'bases' must not be empty");
		return NULL;
	}

	py_super_class = PyTuple_GET_ITEM(bases, 0);
	if (py_super_class == NULL) {
		return NULL;
	}

	if (!PyObjCClass_Check(py_super_class)) {
		PyErr_SetString(PyExc_TypeError, 
				"first base class must "
				"be objective-C based");
		return NULL;
	}
	super_class = PyObjCClass_GetClass(py_super_class);
	if (super_class) {
		PyObjCClass_CheckMethodList(py_super_class, 1);
	}

	/*
	 * __pyobjc_protocols__ contains the list of protocols supported
	 * by an existing class.
	 */
	protocols = PyObject_GetAttrString(py_super_class, 
		"__pyobjc_protocols__");
	if (protocols == NULL) {
		PyErr_Clear();
		protocols = PyList_New(0);
		if (protocols == NULL) return NULL;
	} else {
		PyObject* seq;
		int protocols_len;

		seq = PySequence_Fast(protocols, 
			"__pyobjc_protocols__ not a sequence?");
		if (seq == NULL) {
			Py_DECREF(protocols);
			return NULL;
		}
		Py_DECREF(protocols);

		protocols_len = PySequence_Fast_GET_SIZE(seq);
		protocols = PyList_New(protocols_len);
		if (protocols == NULL) {
			return NULL;
		}
		for (i = 0; i < protocols_len; i++) {
			PyList_SET_ITEM(protocols, i, 
				PySequence_Fast_GET_ITEM(seq, i));
			Py_INCREF(PySequence_Fast_GET_ITEM(seq, i));
		}
		Py_DECREF(seq);
	}

	real_bases = PyList_New(0);
	if (real_bases == NULL) {
		Py_DECREF(protocols);
		return NULL;
	}
	PyList_Append(real_bases, py_super_class);
	if (PyErr_Occurred()) {
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}

	for (i = 1; i < len; i++) {
		v = PyTuple_GET_ITEM(bases, i);
		if (v == NULL) {
			return NULL;
		}
		if (PyObjCClass_Check(v)) {
			Py_DECREF(protocols);
			Py_DECREF(real_bases);
			PyErr_SetString(PyExc_TypeError, 
					"multiple objective-C bases");
			return NULL;
		} else if (PyObjCInformalProtocol_Check(v)) {
			PyList_Append(protocols, v);
		} else if (PyObjCFormalProtocol_Check(v)) {
			PyList_Append(protocols, v);
		} else {
			PyList_Append(real_bases, v);
		}
	}


	/* First generate the objective-C class. This may change the
	 * class dict.
	 */
	objc_class = PyObjCClass_BuildClass(super_class, protocols, name, dict);
	if (objc_class == NULL) {
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}

	/* PyObjCClass_BuildClass may have changed the super_class */
	super_class = objc_class->super_class;
	py_super_class = PyObjCClass_New(super_class);
	if (py_super_class == NULL) {
		(void)PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	} else {
		PyObjCClass_CheckMethodList(py_super_class, 1);
	}

	Py_INCREF(py_super_class);
	Py_DECREF(PyList_GET_ITEM(real_bases, 0));
	PyList_SET_ITEM(real_bases, 0, py_super_class);

	v = PyList_AsTuple(real_bases);
	if (v == NULL) {
		(void)PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}
	Py_DECREF(real_bases);
	real_bases = v;

	/* Verify that the class conforms to all protocols it claims to 
	 * conform to.
	 */
	len = PyList_Size(protocols);
	for (i = 0; i < len; i++) {
		PyObject* p = PyList_GetItem(protocols, i);

		if (p == NULL) {
			PyErr_Clear();
			continue;
		}

		if (PyObjCInformalProtocol_Check(p)) {
			if (!PyObjCInformalProtocol_CheckClass(
					p, name, py_super_class, dict)) {
				Py_DECREF(real_bases);
				Py_DECREF(protocols);
				(void)PyObjCClass_UnbuildClass(objc_class);
				return NULL;
			}
		} else if (PyObjCFormalProtocol_Check(p)) {
			if (!PyObjCFormalProtocol_CheckClass(
					p, name, py_super_class, dict)) {
				Py_DECREF(real_bases);
				Py_DECREF(protocols);
				(void)PyObjCClass_UnbuildClass(objc_class);
				return NULL;
			}
		}
	}

	/*
	 * add __pyobjc_protocols__ to the class-dict.
	 */
	v = PyList_AsTuple(protocols);
	if (v == NULL) {
		Py_DECREF(real_bases);
		Py_DECREF(protocols);
		(void)PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}

	PyDict_SetItemString(dict, "__pyobjc_protocols__", v);
	Py_DECREF(v);
		

	/*
	 * Users can define a __del__ method. We special-case this to
	 * avoid triggering the default mechanisms for this method: The
	 * method should only be called when the Objective-C side of the
	 * instance is deallocated, not whenever the Python proxy is.
	 */
	delmethod = PyDict_GetItemString(dict, "__del__");
	if (delmethod == NULL) {
		PyErr_Clear();
	} else {
		Py_INCREF(delmethod);
		if (PyDict_DelItemString(dict, "__del__") < 0) {
			(void)PyObjCClass_UnbuildClass(objc_class);
			Py_DECREF(protocols);
			Py_DECREF(real_bases);
			return NULL;
		}
	}

	/* Add convenience methods like '__eq__'. Must do it before
	 * call to super-class implementation, because '__*' methods
	 * are treated specially there.
	 */
	if (add_convenience_methods(objc_class, dict) < 0) {
		(void)PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}

	/* call super-class implementation */
	args = Py_BuildValue("(sOO)", name, real_bases, dict);
	res =  PyType_Type.tp_new(type, args, NULL);
	if (res == NULL) {
		Py_DECREF(args);
		Py_DECREF(real_bases);
		(void)PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}
	Py_DECREF(args);
	Py_DECREF(real_bases); 
	args = NULL;
	real_bases = NULL;
	
	Py_DECREF(protocols);
	protocols = NULL;

	if (objc_class_register(objc_class, res) < 0) {
		Py_DECREF(res);
		(void)PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}

	info = (PyObjCClassObject*)res;
	info->class = objc_class;
	info->sel_to_py = NULL; 
	info->method_magic = objc_methodlist_magic(objc_class);
	info->dictoffset = 0;
	info->useKVO = 0;
    info->keysetoffset = 0;
	info->delmethod = delmethod;
	info->hasPythonImpl = 1;

	PyObjCClass_FinishClass(objc_class);

	var = class_getInstanceVariable(objc_class, "__dict__");
	if (var != NULL) {
		info->dictoffset = var->ivar_offset;
	}

	useKVOObj = PyDict_GetItemString(dict, "__useKVO__");
	if (useKVOObj != NULL) {
		info->useKVO = PyObject_IsTrue(useKVOObj);
	}

	var = class_getInstanceVariable(objc_class, "__pyobjc_kvo_stack__");
	if (var != NULL) {
		info->keysetoffset = var->ivar_offset;
	}

	Py_INCREF(res);
	return res;
}


static PyObject*
class_repr(PyObject* obj)
{
	Class cls = PyObjCClass_GetClass(obj);

	if (cls) {
		return PyString_FromFormat(
			"<objective-c class %s at %p>", 
			cls->name, (void*)cls);
	} else {
		return PyString_FromFormat(
			"%s", "<objective-c class NIL>");
	}
}


static void
class_dealloc(PyObject* cls)
{
	char buf[1024];

	snprintf(buf, sizeof(buf), "Deallocating objective-C class %s", ((PyTypeObject*)cls)->tp_name);

	/* This should never happen */
	Py_FatalError(buf);
}

void 
PyObjCClass_CheckMethodList(PyObject* cls, int recursive)
{
	PyObjCClassObject* info;
	int		   magic;

	info = (PyObjCClassObject*)cls;

	if (info->class == NULL) return;

	while (info->class != NULL) {

		if ((info->method_magic != 
				(magic = objc_methodlist_magic(info->class))) || (info->generation != PyObjC_MappingCount)) {

			int r;

			r = add_class_fields(
				info->class,
				((PyTypeObject*)cls)->tp_dict);
			if (r < 0) {
				PyErr_SetString(PyExc_RuntimeError,
					"Cannot rescan method table");
				return;
			}
			info->generation = PyObjC_MappingCount;

			r =  update_convenience_methods(cls);
			if (r < 0) {
				PyErr_SetString(PyExc_RuntimeError,
					"Cannot rescan method table");
				return;
			}
			info->method_magic = magic;
			if (info->sel_to_py) {
				Py_XDECREF(info->sel_to_py);
				info->sel_to_py = PyDict_New();
			}
		}

		if (!recursive) break;
		if (info->class->super_class == NULL) break;
		cls = PyObjCClass_New(info->class->super_class);
		Py_DECREF(cls);
		info = (PyObjCClassObject*)cls;
	}
}


static PyObject*
class_getattro(PyObject* self, PyObject* name)
{
	PyObject* result = NULL;

	/* Python will look for a number of "private" attributes during 
	 * normal operations, such as when building subclasses. Avoid a
	 * method rescan when that happens.
	 *
	 * NOTE: This method should be rewritten, copy the version of type()
	 *       and modify as needed, that would avoid unnecessary rescans
	 * 	 of superclasses. The same strategy is used in object_getattro.
	 */
	if (PyString_Check(name) 
			&& strncmp(PyString_AS_STRING(name), "__", 2) == 0 
			&& strcmp(PyString_AS_STRING(name), "__dict__") != 0) {
		result = PyType_Type.tp_getattro(self, name);
		if (result != NULL) {
			return result;
		}
		PyErr_Clear();
	}

	PyObjCClass_CheckMethodList(self, 1);
	
	result = PyType_Type.tp_getattro(self, name);
	if (result != NULL) {
		return result;
	}

	/* Try to find the method anyway */
	PyErr_Clear();
	result = PyObjCSelector_FindNative(self, PyString_AsString(name));

	if (result != NULL) {
		int res = PyDict_SetItem(((PyTypeObject*)self)->tp_dict, name, result);
		PyObjCNativeSelector* x = (PyObjCNativeSelector*)result;

		if (x->sel_flags & PyObjCSelector_kCLASS_METHOD) {
			x->sel_self = self;
			Py_INCREF(x->sel_self);
		}
		if (res < 0) {
			if (PyObjC_VerboseLevel) {
				PySys_WriteStderr(
					"PyObjC[class_getattro]: Cannot "
					"add new method to dict:\n");
				PyErr_Print();
			}
			PyErr_Clear();
		}
	}
	return result;
}

static int
class_setattro(PyObject* self, PyObject* name, PyObject* value)
{
	int res;
	if (value == NULL) {
		/* delattr(), deny the operation when the name is bound
		 * to a selector.
		 */
		PyObject* old_value = class_getattro(self, name);
		if (old_value == NULL) {
			PyErr_Clear();
			return PyType_Type.tp_setattro(self, name, value);

		} else if (PyObjCSelector_Check(old_value)) {
			Py_DECREF(old_value);
			if (!PyString_Check(name)) {
				PyErr_SetString(PyExc_AttributeError, 
						"cannot delete selectors");
			} else {
				PyErr_Format(PyExc_AttributeError,
					"Cannot remove selector '%s' in '%s'",
					PyString_AS_STRING(name),
					self->ob_type->tp_name
				);
			}
			return -1;
		}
	} else if (PyObjCNativeSelector_Check(value)) {
		PyErr_SetString(PyExc_TypeError,
			"Assigning native selectors is not supported");
		return -1;

	} else if (PyObjCSelector_Check(value) 
			|| PyFunction_Check(value) 
			|| PyMethod_Check(value) 
			|| PyObject_TypeCheck(value, &PyClassMethod_Type)
		) {
		/*
		 * Assignment of a function: create a new method in the ObjC
		 * runtime.
		 */
		PyObject* newVal;
		int r;
		struct objc_method* objcMethod;
		struct objc_method_list* methodsToAdd;
		
		newVal = PyObjCSelector_FromFunction(
				name, value, self, NULL);
		if (newVal == NULL) {
			return -1;
		} 
		if (!PyObjCSelector_Check(newVal)) {
			Py_DECREF(newVal);
			PyErr_SetString(PyExc_ValueError, 
					"cannot convert callable to selector");
			return -1;
		}

		methodsToAdd = PyObjCRT_AllocMethodList(1);
		if (methodsToAdd == NULL) {
			Py_DECREF(newVal);
			PyErr_NoMemory();
			return -1;
		}

		methodsToAdd->method_count = 1;
		objcMethod = methodsToAdd->method_list;
		objcMethod->method_name = PyObjCSelector_GetSelector(newVal);
		objcMethod->method_types = strdup(
				PyObjCSelector_Signature(newVal));

		if (objcMethod->method_types == NULL) {
			free(methodsToAdd);
			Py_DECREF(newVal);
			return -1;
		}
		objcMethod->method_imp = PyObjCFFI_MakeIMPForPyObjCSelector(
				(PyObjCSelector*)newVal);
		if (objcMethod->method_imp == NULL) {
			free((char*)objcMethod->method_types);
			free(methodsToAdd);
			Py_DECREF(newVal);
			PyErr_NoMemory();
			return -1;
		}

		r = PyDict_SetItem(((PyTypeObject*)self)->tp_dict, name, newVal);
		Py_DECREF(newVal);
		if (r == -1) {
			free((char*)objcMethod->method_types);
			free(methodsToAdd);
			PyErr_NoMemory();
			return -1;
		}

		
		if (PyObjCSelector_IsClassMethod(newVal)) {
			PyObjCRT_ClassAddMethodList(
					GETISA(PyObjCClass_GetClass(self)), 
					methodsToAdd);
		} else {
			PyObjCRT_ClassAddMethodList(
					PyObjCClass_GetClass(self), 
					methodsToAdd);
		}
		return 0;
	}

	res = PyType_Type.tp_setattro(self, name, value);
	return res;
}

static int
class_compare(PyObject* self, PyObject* other)
{
	Class self_class;
	Class other_class;
	int   v;

	if (!PyObjCClass_Check(other)) {
		PyErr_SetString(PyExc_NotImplementedError, "Cmp with other");
		return -1;
	}

	/* This is as arbitrary as the default tp_compare, but nicer for
	 * the user
	 */
	self_class = PyObjCClass_GetClass(self);
	other_class = PyObjCClass_GetClass(other);

	if (self_class == other_class) return 0;
	if (!self_class) return -1;
	if (!other_class) return 1;

	v = strcmp(
		self_class->name, 
		other_class->name);

	/* Python requires -1, 0 or 1, but strcmp on MacOS X returns
	 * 'negative', 0 or 'positive'
	 */
	if (v < 0) return -1;
	if (v == 0) return 0;
	return 1;
}

static long
class_hash(PyObject* self)
{
	return (long)self;
}

PyDoc_STRVAR(cls_get_classMethods_doc,
"The attributes of this field are the class methods of this object. This can\n"
"be used to force access to a class method."
);
static PyObject*
cls_get_classMethods(PyObject* self, void* closure __attribute__((__unused__)))
{
	return PyObjCMethodAccessor_New(self, 1);
}

PyDoc_STRVAR(cls_get_instanceMethods_doc,
"The attributes of this field are the instance methods of this object. This \n"
"can be used to force access to an instance method."
);
static PyObject*
cls_get_instanceMethods(PyObject* self, void* closure __attribute__((__unused__)))
{
	return PyObjCMethodAccessor_New(self, 0);
}

static PyObject*
cls_get__name__(PyObject* self, void* closure __attribute__((__unused__)))
{
	Class cls = PyObjCClass_GetClass(self);
	if (cls == NULL) {
		return PyString_FromString("objc.objc_class");
	} else {
		return PyString_FromString(cls->name);
	}
}

static PyGetSetDef class_getset[] = {
		{
				"pyobjc_classMethods",
				(getter)cls_get_classMethods,
				NULL,
				cls_get_classMethods_doc,
				0
		},
		{
				"pyobjc_instanceMethods",
				(getter)cls_get_instanceMethods,
				NULL,
				cls_get_instanceMethods_doc,
				0
		},
	{
		/* Access __name__ through a property: Objective-C name 
		 * might change due to posing.
		 */
		"__name__",
		(getter)cls_get__name__,
		NULL,
		NULL,
		0
	},
		{ 0, 0, 0, 0, 0 }
};

static PyMemberDef class_members[] = {
	{
		"__useKVO__",
		T_INT,
		offsetof(PyObjCClassObject, useKVO),
		0,
		"Use KVO notifications when setting attributes from Python",
	},
	{ NULL, 0, 0, 0, NULL}
};


PyTypeObject PyObjCClass_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc_class",				/* tp_name */
	sizeof (PyObjCClassObject),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	class_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	class_compare,				/* tp_compare */
	class_repr,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	class_hash,				/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	class_getattro,				/* tp_getattro */
	class_setattro,				/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT 
		| Py_TPFLAGS_BASETYPE,		/* tp_flags */
	class_doc,				/* tp_doc */
	0,					/* tp_traverse */
	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	class_members,					/* tp_members */
	class_getset,				/* tp_getset */
	&PyType_Type,				/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	class_new,				/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,                                      /* tp_mro */
	0,                                      /* tp_cache */
	0,                                      /* tp_subclasses */
	0,                                      /* tp_weaklist */
	0                                       /* tp_del */
};

/* FIXME: objc_support.[hm] also has version of this function! */
char*
PyObjC_SELToPythonName(SEL sel, char* buf, size_t buflen)
{
	size_t res = snprintf(buf, buflen, "%s", PyObjCRT_SELName(sel));
	char* cur;

	if (res != strlen(PyObjCRT_SELName(sel))) {
		return NULL;
	}
	if (PyObjC_IsPythonKeyword(buf)) {
		res = snprintf(buf, buflen, "%s__", PyObjCRT_SELName(sel));
		if (res != 2+strlen(PyObjCRT_SELName(sel))) {
			return NULL;
		}
		return buf;
	}
	cur = strchr(buf, ':');
	while (cur) {
		*cur = '_';
		cur = strchr(cur, ':');
	}
	return buf;
}

/*
 * Add methods and descriptors for the instance variables to the dict.
 *
 * Add only the items for this specific class, the items from the super-class
 * are found through inheritance.
 *
 * We add instance methods, class methods and instance variables in that 
 * order, methods always override variables (most classes provide accessor
 * methods with the same name as the variables and this order is the least
 * surprising)
 */
static int
add_class_fields(Class objc_class, PyObject* dict)
{
	Class     cls;
	struct objc_method_list* mlist;
	void*     iterator;
	PyObject* descr;
	char      selbuf[1024];

	if (objc_class == NULL) return 0;

	/*
	 * First add instance methods
	 */

	iterator = 0;
	mlist = PyObjCRT_NextMethodList(objc_class, &iterator);
	while (mlist != NULL) {
		int i;
		PyObjCRT_Method_t meth;

		for (i = 0; i < mlist->method_count; i++) {
			char* name;
			PyObject* curItem;

			meth = mlist->method_list + i;

			name = (char*)PyObjC_SELToPythonName(
						meth->method_name, 
						selbuf, 
						sizeof(selbuf));

			curItem = PyDict_GetItemString(dict, name);
			if (curItem == NULL) {
				PyErr_Clear();
			} else if (!PyObjCNativeSelector_Check(curItem)) {
				continue;
			}

			descr = PyObjCSelector_NewNative(
					objc_class,
					meth->method_name,
					meth->method_types,
					0);

			if (PyDict_SetItemString(
					dict, 
					name,
					descr) != 0) {

				Py_DECREF(descr); 
				return -1;
			}
			Py_DECREF(descr); 
		}
		mlist = PyObjCRT_NextMethodList(objc_class, &iterator);
	}



	/* 
	 * Then add class methods
	 */

	cls = GETISA(objc_class);
	iterator = 0;
	mlist = PyObjCRT_NextMethodList(cls, &iterator);
	while (mlist != NULL) {
		int i;
		PyObjCRT_Method_t meth;

		for (i = 0; i < mlist->method_count; i++) {
			meth = mlist->method_list + i;

			PyObjC_SELToPythonName(
				meth->method_name, 
				selbuf, 
				sizeof(selbuf));

			if ((descr = PyDict_GetItemString(dict, selbuf))) {
				if (!PyObjCSelector_Check(descr)) {
					continue;
				} else if (!(((PyObjCSelector*)descr)->sel_flags & PyObjCSelector_kCLASS_METHOD)) {
					continue;
				} else if (PyObjCPythonSelector_Check(descr)) {
					continue;
				}
			}

			descr = PyObjCSelector_NewNative(
				objc_class,
				meth->method_name,
				meth->method_types,
				1);

			if (PyDict_SetItemString(dict, 
					selbuf,
					descr) != 0) {
				Py_DECREF(descr);
				return -1;
			}
			Py_DECREF(descr);
		}
		mlist = PyObjCRT_NextMethodList(cls, &iterator);
	}

#if PyOBJC_ACCESS_INSTANCE_VARIABLES
	/*
	 * Finally add instance variables.
	 *
	 * This code is currently disabled to match the Objective-C
	 * semantics.
	 */
	if (objc_class->ivars) {
		int i;
		struct objc_ivar *var;
		for (i = 0; i < objc_class->ivars->ivar_count; i++) {
			var = objc_class->ivars->ivar_list + i;

			if (PyDict_GetItemString(dict, var->ivar_name)) {
				continue;
			}

			descr = PyObjCInstanceVariable_New(var->ivar_name);
			if (descr == NULL) {
				return -1;
			}
			if (PyDict_SetItemString(dict, 
					var->ivar_name, descr) != 0) {
				Py_DECREF(descr);
				return -1;
			}
			Py_DECREF(descr);
		}
	}
#endif

	return  0;
}

/*
 * Create a new objective-C class  proxy.
 *
 * NOTES:
 * - proxies are subclasses of PyObjCClass_Type
 * - subclass relations in objetive-C are retained in python
 * - this looks a lot like PyObjCClass_Type.tp_new, but it is _not_ the
 *   same!
 */
PyObject* 
PyObjCClass_New(Class objc_class)
{
	PyObject* args;
	PyObject* dict;
	PyObject* result;
	PyObject* bases;
	PyObjCClassObject* info;
	PyObjCRT_Ivar_t var;

	result = objc_class_locate(objc_class);
	if (result != NULL) {
		return result;
	}

#ifdef GNU_RUNTIME
	/*
	 * FIXME: we do get unresolved classes when fetching the class list
	 * (especially when loading multiple frameworks). I'm not sure why
	 * this occurs, it might be the way we link/compile our code.
	 *
	 * The test below seems to fix the problems, but is obviously a hack.
	 */
	if (!CLS_ISRESOLV(objc_class)) {
		extern void __objc_resolve_class_links(void);
		__objc_resolve_class_links();
	}
#endif

	dict = PyDict_New();
	PyDict_SetItemString(dict, "__slots__", PyTuple_New(0));

	bases = PyTuple_New(1);

	if (objc_class->super_class == NULL) {
		PyTuple_SET_ITEM(bases, 0, (PyObject*)&PyObjCObject_Type);
		Py_INCREF(((PyObject*)&PyObjCObject_Type));
	} else {
		PyTuple_SET_ITEM(bases, 0, 
			PyObjCClass_New(objc_class->super_class));
	} 
	args = PyTuple_New(3);
	PyTuple_SetItem(args, 0, PyString_FromString(objc_class->name));
	PyTuple_SetItem(args, 1, bases);
	PyTuple_SetItem(args, 2, dict);

	result = PyType_Type.tp_new(&PyObjCClass_Type, args, NULL);
	Py_DECREF(args);
	if (result == NULL) return NULL;

	info = (PyObjCClassObject*)result;
	info->class = objc_class;
	info->sel_to_py = NULL;
	info->method_magic = 0;
	info->dictoffset = 0;
	info->useKVO = 0;
	info->delmethod = NULL;
	info->hasPythonImpl = 0;

	/* XXX: Hack to support buffer API */
	if (strcmp(objc_class->name, "NSData") == 0) {
		((PyTypeObject *)result)->tp_as_buffer = &nsdata_as_buffer;
	} else if (strcmp(objc_class->name, "NSMutableData") == 0) {
		((PyTypeObject *)result)->tp_as_buffer = &nsmutabledata_as_buffer;
	}

	var = class_getInstanceVariable(objc_class, "__dict__");
	if (var != NULL) {
		info->dictoffset = var->ivar_offset;
	}

	if (PyObject_SetAttrString(result, 
			"__module__", PyObjCClass_DefaultModule) < 0) {
		PyErr_Clear();
	}


	objc_class_register(objc_class, result);

	return result;
}


Class 
PyObjCClass_GetClass(PyObject* cls)
{
	if (!PyObjCClass_Check(cls)) {
		PyErr_Format(PyObjCExc_InternalError,
			"PyObjCClass_GetClass called for non-class (%s)",
			cls->ob_type->tp_name);
		return nil;
	}
	
	return ((PyObjCClassObject*)cls)->class;
}

PyObject* 
PyObjCClass_FindSelector(PyObject* cls, SEL selector)
{
	PyObjCClassObject* info;
	PyObject*          result;
	PyObject*          attributes;
	PyObject*          key;
	PyObject*          v;
	int                i;
	int                len;


	if (!PyObjCClass_Check(cls)) {
		PyErr_Format(PyObjCExc_InternalError,
			"PyObjCClass_GetClass called for non-class (%s)",
			cls->ob_type->tp_name);
		return NULL;
	}

	PyObjCClass_CheckMethodList(cls, 1);
	
	info = (PyObjCClassObject*)cls;
	if (info->sel_to_py == NULL) {
		info->sel_to_py = PyDict_New();
		if (info->sel_to_py == NULL) {
			return NULL;
		}
	}

	/* First check the cache */

	result = PyDict_GetItemString(info->sel_to_py, 
				(char*)PyObjCRT_SELName(selector));	
	if (result != NULL) {
		if (result == Py_None) {
			/* negative cache entry */
			PyErr_Format(PyExc_AttributeError,
				"No selector %s",
				PyObjCRT_SELName(selector));
			return NULL;
		}
		Py_INCREF(result);
		return result;
	}

	/* Not in the cache, walk the attribute list */

	attributes = PyObject_Dir(cls);
	if (attributes == NULL) {
		return NULL;
	}

	v = PySequence_Fast(attributes, "PyObject_Dir didn't return a list");
	if (v == NULL) {
		Py_DECREF(attributes);
		return NULL;
	}

	Py_DECREF(attributes);
	attributes = v; 
	v = NULL;

	len = PySequence_Fast_GET_SIZE(attributes);
	for (i = 0; i < len; i++) {
		key = PySequence_Fast_GET_ITEM(attributes, i);
		if (key == NULL) {
			Py_DECREF(attributes);
			return NULL;
		}

#ifdef  PyObjC_COMPILING_ON_MACOSX_10_1
	/* On MacOSX we get hard crashes for the method signature of this
	 * method. This seems to be a problem with the Objective-C runtime 
	 * and/or Cocoa because a simple ObjC program gives the same error.
	 * 
	 * As this method should never be forwarded to Python anyway we can
	 * safely ignore it here.
	 */
		if (PyString_Check(key) && 
				strcmp(PyString_AS_STRING(key), "__pyobjc_PythonObject__") == 0) {
			continue;

		}
#endif

		v = PyObject_GetAttr(cls, key);
		if (v == NULL) {
			PyErr_Clear();
			continue;
		}

		if (PyObjCSelector_Check(v)) {
			if (PyObjCRT_SameSEL(
					((PyObjCSelector*)v)->sel_selector, 
					selector)) {

				Py_DECREF(attributes);
				PyDict_SetItemString(info->sel_to_py,
					(char*)PyObjCRT_SELName(selector), v);
				return v;
			}
		} 
		Py_DECREF(v);
	}

	Py_DECREF(attributes);

	/* If all else fails, ask the actual class (getattro also does this) */
	result = PyObjCSelector_FindNative(cls, 
				PyObjCRT_SELName(selector));
	if (result) {
		return result;
	}

	PyErr_Format(PyExc_AttributeError,
		"No selector %s", PyObjCRT_SELName(selector));
	PyDict_SetItemString(info->sel_to_py, 
			(char*)PyObjCRT_SELName(selector), Py_None);
	return NULL;
}

int 
PyObjCClass_IsSubClass(Class child, Class parent)
{
	if (parent == nil) return 1;

	while (child != nil) {
		if (child == parent) return 1;
		child = child->super_class;	
	}
	return 0;
}

int
PyObjCClass_KeySetOffset(PyObject* cls)
{
	return ((PyObjCClassObject*)cls)->keysetoffset;
}


int
PyObjCClass_DictOffset(PyObject* cls)
{
	return ((PyObjCClassObject*)cls)->dictoffset;
}

PyObject*
PyObjCClass_GetDelMethod(PyObject* cls)
{
	PyObjCClassObject* info;
	info = (PyObjCClassObject*)cls;
	Py_XINCREF(info->delmethod);
	return info->delmethod;
}

void
PyObjCClass_SetDelMethod(PyObject* cls, PyObject* m)
{
	PyObjCClassObject* info;
	info = (PyObjCClassObject*)cls;
	Py_XINCREF(m);
	Py_XDECREF(info->delmethod);
	info->delmethod = m;
}

int
PyObjCClass_HasPythonImplementation(PyObject* cls)
{
	PyObjCClassObject* info;
	info = (PyObjCClassObject*)cls;
	return info->hasPythonImpl;
}



/*!
 * @function add_convenience_methods
 * @abstract Add the convenience methods for a class wrapper
 * @param cls  An Objective-C class wrapper
 * @param type_dict the __dict__ for the new class
 * @result Returns -1 on error, 0 on success 
 * @discussion
 *     This function calls the PyObjC_ClassExtender function (if one is
 *     registered) and then updates the class __dict__. 
 */
static int
add_convenience_methods(Class cls, PyObject* type_dict)
{
	PyObject* super_class;
	PyObject* name;
	PyObject* res;
	PyObject* args;

	if (PyObjC_ClassExtender == NULL || cls == nil) return 0;

	if (cls->super_class == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(cls->super_class);
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(cls->name);
	if (name == NULL) {
		Py_DECREF(super_class);
		return -1;
	}

	args = PyTuple_New(3);
	if (args == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		return -1;
	}

	PyTuple_SET_ITEM(args, 0, super_class);
	PyTuple_SET_ITEM(args, 1, name);
	PyTuple_SET_ITEM(args, 2, type_dict);
	Py_INCREF(type_dict);

	res = PyObject_CallObject(PyObjC_ClassExtender, args);
	Py_DECREF(args);
	if (res == NULL) {
		return -1;
	}
	Py_DECREF(res);

	return 0;
}

/*!
 * @function update_convenience_methods
 * @abstract Update the convenience methods for a class
 * @param cls  An Objective-C class wrapper
 * @result Returns -1 on error, 0 on success 
 * @discussion
 *     This function calls the PyObjC_ClassExtender function (if one is
 *     registered) and then updates the class __dict__. 
 *
 *     NOTE: We change the __dict__ using a setattro function because the type
 *     doesn't notice the existance of new special methods otherwise.
 *
 *     NOTE2: We use PyType_Type.tp_setattro instead of PyObject_SetAttr because
 *     the tp_setattro of Objective-C class wrappers does not allow some of
 *     the assignments we do here.
 */
static int 
update_convenience_methods(PyObject* cls)
{
	PyObject* super_class;
	PyObject* name;
	PyObject* res;
	PyObject* args;
	Class     objc_cls;
	PyObject* dict;
	PyObject* keys;
	PyObject* v;
	int       i, len;

	if (PyObjC_ClassExtender == NULL || cls == NULL) return 0;

	if (!PyObjCClass_Check(cls)) {
		PyErr_SetString(PyExc_TypeError, "not a class");
		return -1;
	}

	objc_cls = PyObjCClass_GetClass(cls);

	if (objc_cls->super_class == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(objc_cls->super_class);
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(objc_cls->name);
	if (name == NULL) {
		Py_DECREF(super_class);
		return -1;
	}

	dict = /*PyDict_Copy*/(((PyTypeObject*)cls)->tp_dict);
	Py_INCREF(dict);
	if (dict == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		return -1;
	}

	args = PyTuple_New(3);
	if (args == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		Py_DECREF(dict);
		return -1;
	}

	PyTuple_SET_ITEM(args, 0, super_class);
	PyTuple_SET_ITEM(args, 1, name);
	PyTuple_SET_ITEM(args, 2, dict);

	res = PyObject_Call(PyObjC_ClassExtender, args, NULL);
	if (res == NULL) {
		Py_DECREF(args);
		return -1;
	}
	Py_DECREF(res);
	keys = PyDict_Keys(dict);
	if (keys == NULL) {
		Py_DECREF(args);
		return -1;
	}

	v = PySequence_Fast(keys, "PyDict_Keys didn't return a sequence");
	Py_DECREF(keys);
	if (v == NULL) {
		return -1;
	}
	keys = v;

	len = PySequence_Fast_GET_SIZE(keys);
	for (i = 0; i < len; i++) {
		PyObject* k = PySequence_Fast_GET_ITEM(keys, i);
		char*     n;
		
		if (k == NULL) {
			PyErr_Clear();
			continue;
		}

		if (!PyString_Check(k)) {
			continue;
		}
		n = PyString_AS_STRING(k);
		if (n[0] != '_' || n[1] != '_') {
			continue;
		}
		if (	   strcmp(n, "__dict__") == 0 
			|| strcmp(n, "__bases__") == 0
			|| strcmp(n, "__slots__") == 0
			|| strcmp(n, "__mro__") == 0
		   ) {

			continue;
		}

		v = PyDict_GetItem(dict, k);
		if (v == NULL) {
			PyErr_Clear();
			continue;
		}
		if (PyType_Type.tp_setattro(cls, k, v) == -1) {
			PyErr_Clear();
			continue;
		}
	}
	Py_DECREF(keys);
	Py_DECREF(args);

	return 0;
}
