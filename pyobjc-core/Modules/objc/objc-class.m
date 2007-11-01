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
Py_ssize_t nsdata_getreadbuffer(PyObject *pyself, Py_ssize_t segment __attribute__((unused)), void **ptrptr) {
	NSData *self = (NSData *)PyObjCObject_GetObject(pyself);
	assert(segment == 0);
	if (ptrptr != NULL) {
		*ptrptr = (void *)[self bytes];
	}
	return (int)[self length];
}

static
Py_ssize_t nsmutabledata_getwritebuffer(PyObject *pyself, Py_ssize_t segment __attribute__((unused)), void **ptrptr) {
	NSMutableData *self = (NSMutableData *)PyObjCObject_GetObject(pyself);
	assert(segment == 0);
	if (ptrptr != NULL) {
		*ptrptr = (void *)[self mutableBytes];
	}
	return (int)[self length];
}

static
Py_ssize_t nsdata_getsegcount(PyObject *pyself, Py_ssize_t *lenp) {
	NSData *self = (NSData *)PyObjCObject_GetObject(pyself);
	if (lenp != NULL) {
		*lenp = (Py_ssize_t)[self length];
	}
	return 1;
}

static PyBufferProcs nsdata_as_buffer = {
	nsdata_getreadbuffer,
	NULL,
	nsdata_getsegcount,
	NULL
};

static PyBufferProcs nsmutabledata_as_buffer = {
	nsdata_getreadbuffer,
	nsmutabledata_getwritebuffer,
	nsdata_getsegcount,
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

static int add_class_fields(Class objc_class, PyObject* dict, PyObject* protDict, PyObject* classDict); 
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
static NSMapTable* metaclass_to_class = NULL;

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

static int 
objc_metaclass_register(PyTypeObject* meta_class, Class class)
{
	if (metaclass_to_class == NULL) {
		metaclass_to_class = NSCreateMapTable(
			PyObjCUtil_PointerKeyCallBacks,
			PyObjCUtil_PointerValueCallBacks, 
			PYOBJC_EXPECTED_CLASS_COUNT);
	}

	if (NSMapGet(metaclass_to_class, meta_class)) {
		PyErr_BadInternalCall();
		return -1;
	}

	Py_INCREF(meta_class); 
	NSMapInsert(metaclass_to_class, meta_class, class);

	return 0;
}

static Class
objc_metaclass_locate(PyObject* meta_class)
{
	Class result;

	if (metaclass_to_class == NULL) return NULL;
	if (meta_class == NULL) return NULL;

	result = NSMapGet(metaclass_to_class, meta_class);
	return result;
}

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



/* Create a new objective-C metaclass proxy 
 *
 * Returns a new reference.
 */
static PyTypeObject* 
PyObjCClass_NewMetaClass(Class objc_class)
{
	PyTypeObject* result;
	Class objc_meta_class = object_getClass(objc_class);

	if (unlikely(class_isMetaClass(objc_class))) {
		objc_meta_class = objc_class;
	}

	if (objc_meta_class == nil) {
		Py_INCREF(&PyObjCClass_Type);
		return &PyObjCClass_Type;
	}

	/* Create a metaclass proxy for the metaclass of the given class */
	result = (PyTypeObject*)objc_class_locate(objc_meta_class);
	if (result != NULL) {
		return result;
	}

	Class super_class = nil;
	
	if (unlikely(class_isMetaClass(objc_class))) {
		super_class = class_getSuperclass(objc_meta_class);
		if (!class_isMetaClass(super_class)) {
			/* NSObject's metaclass inherits from NSObject, don't
			 * model that in Python. */
			super_class = nil;
		}
	} else {
		super_class = class_getSuperclass(objc_class);
	}

	PyTypeObject* py_super_class;
	if (super_class == nil) {
		Py_INCREF(&PyObjCClass_Type);
		py_super_class = &PyObjCClass_Type;
	} else {
		py_super_class = PyObjCClass_NewMetaClass(super_class);
		if (py_super_class == NULL) {
			return NULL;
		}
	}

	/* We now know the superclass of our metaclass, build the actual
	 * metaclass.
	 */
	PyObject* dict = PyDict_New();
	PyObject* bases = PyTuple_New(1);
	
	PyTuple_SET_ITEM(bases, 0, (PyObject*)py_super_class);

	PyObject* args = PyTuple_New(3);
	PyTuple_SetItem(args, 0, 
			PyString_FromString(class_getName(objc_class)));
	PyTuple_SetItem(args, 1, bases);
	PyTuple_SetItem(args, 2, dict);

	result = (PyTypeObject*)PyType_Type.tp_new(&PyType_Type, args, NULL);
	Py_DECREF(args);
	if (result == NULL) return NULL;

	if (objc_class_register(objc_meta_class, (PyObject*)result) == -1) {
		Py_DECREF(result);
		return NULL;
	}

	if (objc_metaclass_register(result, objc_class) == -1) {
		/* Whoops, no such thing */
		//objc_class_unregister(objc_meta_class);
		return NULL;
	}

	return (PyTypeObject*)result;
}


/*
 * Create a new objective-C class, as a subclass of 'type'. This is
 * PyObjCClass_Type.tp_new.
 *
 * Note: This function creates new _classes_
 */


static PyObject*
class_new(PyTypeObject* type __attribute__((__unused__)), 
		PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", "bases", "dict", NULL };
	char* name;
	PyObject* bases;
	PyObject* dict;
	PyObject* old_dict;
	PyObject* res;
	PyObject* k;
	PyObject* metadict;
	PyObject* v;
	Py_ssize_t i;
	Py_ssize_t len;
	Class      objc_class = NULL;
	Class	   super_class = NULL;
	PyObject*  py_super_class = NULL;
	PyObjCClassObject* info;
	PyObject* keys;
	PyObject* protocols;
	PyObject* real_bases;
	PyObject* delmethod;
	PyObject* useKVOObj;
	Ivar var;
	PyObject* protectedMethods = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sOO:__new__",
			keywords, &name, &bases, &dict)) {
		return NULL;
	}

	if (!PyTuple_Check(bases)) {
		PyErr_SetString(PyExc_TypeError, "'bases' must be tuple");
		return NULL;
	}

	len = PyTuple_Size(bases);
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

	protectedMethods = PyDict_New();
	if (protectedMethods == NULL) {
		return NULL;
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
		Py_ssize_t protocols_len;

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

	metadict = PyDict_New();
	if (metadict == NULL) {
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		return NULL;
	}

	/* First generate the objective-C class. This may change the
	 * class dict.
	 */
	objc_class = PyObjCClass_BuildClass(super_class, protocols, name, dict, metadict);
	if (objc_class == NULL) {
		Py_DECREF(protocols);
		Py_DECREF(metadict);
		Py_DECREF(real_bases);
		return NULL;
	}

	/* PyObjCClass_BuildClass may have changed the super_class */
	super_class = class_getSuperclass(objc_class);
	py_super_class = PyObjCClass_New(super_class);
	if (py_super_class == NULL) {
		(void)PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		Py_DECREF(metadict);
		return NULL;
	} else {
		PyObjCClass_CheckMethodList(py_super_class, 1);
	}

	Py_DECREF(PyList_GET_ITEM(real_bases, 0));
	PyList_SET_ITEM(real_bases, 0, py_super_class);

	v = PyList_AsTuple(real_bases);
	if (v == NULL) {
		(void)PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(metadict);
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
				Py_DECREF(metadict);
				(void)PyObjCClass_UnbuildClass(objc_class);
				return NULL;
			}
		} else if (PyObjCFormalProtocol_Check(p)) {
			if (!PyObjCFormalProtocol_CheckClass(
					p, name, py_super_class, dict, metadict)) {
				Py_DECREF(real_bases);
				Py_DECREF(protocols);
				Py_DECREF(metadict);
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
		Py_DECREF(metadict);
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
			Py_DECREF(metadict);
			return NULL;
		}
	}

	/* Add convenience methods like '__eq__'. Must do it before
	 * call to super-class implementation, because '__*' methods
	 * are treated specially there.
	 */
	old_dict = PyDict_Copy(dict);
	if (old_dict == NULL) {
		(void)PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		Py_DECREF(metadict);
		return NULL;
	}


		
	if (add_convenience_methods(objc_class, dict) < 0) {
		(void)PyObjCClass_UnbuildClass(objc_class);
		Py_DECREF(old_dict);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		Py_DECREF(metadict);
		return NULL;
	}

	PyTypeObject* metatype = PyObjCClass_NewMetaClass(objc_class);
	if (metatype == NULL) {
		Py_DECREF(old_dict);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		Py_DECREF(metadict);
		return NULL;
	}
	if (PyDict_Update(metatype->tp_dict, metadict) == -1) {
		Py_DECREF(old_dict);
		Py_DECREF(protocols);
		Py_DECREF(real_bases);
		Py_DECREF(metadict);
		return NULL;
	}
	Py_DECREF(metadict); metadict = NULL;

	/* call super-class implementation */
	args = Py_BuildValue("(sOO)", name, real_bases, dict);

	/* The actual superclass might be different due to introduction
	 * of magic intermediate classes, therefore explicitly refer to the
	 * metatype we just created.
	 */
	res =  PyType_Type.tp_new(metatype, args, NULL);
	Py_DECREF(metatype);
	if (res == NULL) {
		Py_DECREF(args);
		Py_DECREF(real_bases);
		Py_DECREF(protocols);
		Py_DECREF(old_dict);
		(void)PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}
	Py_DECREF(args);
	Py_DECREF(real_bases); 
	args = NULL;
	real_bases = NULL;
	
	Py_DECREF(protocols);
	protocols = NULL;

	/* Register the proxy as soon as possible, we can get initialize calls
	 * very early on with the ObjC 2.0 runtime.
	 */
	PyObjC_RegisterPythonProxy(objc_class, res);

	if (objc_class_register(objc_class, res) < 0) {
		PyObjC_UnregisterPythonProxy(objc_class, res);
		Py_DECREF(res);
		Py_DECREF(old_dict);
		(void)PyObjCClass_UnbuildClass(objc_class);
		return NULL;
	}

	PyObjCClass_FinishClass(objc_class);

	info = (PyObjCClassObject*)res;
	info->class = objc_class;
	info->sel_to_py = NULL; 
	info->method_magic = PyObjC_methodlist_magic(objc_class);
	info->dictoffset = 0;
	info->useKVO = 0;
	info->delmethod = delmethod;
	info->hasPythonImpl = 1;
	info->isCFWrapper = 0;
	info->protectedMethods = protectedMethods;


	var = class_getInstanceVariable(objc_class, "__dict__");
	if (var != NULL) {
		info->dictoffset = ivar_getOffset(var);
	}

	useKVOObj = PyDict_GetItemString(dict, "__useKVO__");
	if (useKVOObj != NULL) {
		info->useKVO = PyObject_IsTrue(useKVOObj);
	}


	keys = PyDict_Keys(dict);
	if (keys == NULL) {
		Py_DECREF(old_dict);
		return NULL;
	}
	
	/* Merge the "difference" to pick up new selectors */
	len = PyList_GET_SIZE(keys);
	for (i=0; i < len; i++) {
		k = PyList_GET_ITEM(keys, i);
		if (PyDict_GetItem(old_dict, k) == NULL) {
			v = PyDict_GetItem(dict, k);
			if (v != NULL && PyObject_SetAttr(res, k, v) == -1) {
				PyErr_Clear();
			}
		}
	}

	Py_DECREF(keys);
	Py_DECREF(old_dict);
	
	/* This is an "extra" ref */
	Py_INCREF(res);
	return res;
}


static PyObject*
class_repr(PyObject* obj)
{
	Class cls = PyObjCClass_GetClass(obj);

	if (cls) {
		const char* nm = class_getName(cls);
		if (strcmp(nm, "NSCFType") == 0) {
			return PyString_FromFormat(
				"<core-foundation class %s at %p>", 
				((PyTypeObject*)obj)->tp_name, (void*)cls);

		} else {
			return PyString_FromFormat(
				"<objective-c class %s at %p>", 
				nm, (void*)cls);
		}
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
				(magic = PyObjC_methodlist_magic(info->class))) || (info->generation != PyObjC_MappingCount)) {

			int r;

			r = add_class_fields(
				info->class,
				((PyTypeObject*)cls)->tp_dict,
				info->protectedMethods,
				cls->ob_type->tp_dict);
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
		if (class_getSuperclass(info->class) == NULL) break;
		cls = PyObjCClass_New(class_getSuperclass(info->class));
		Py_DECREF(cls); /* We don't actually need the reference, convert to a borrowed one */
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
	 *
	 * NOTE2: That rewrite should also cause this method to prefer class
	 *       methods over instance methods (and documentation should be 
	 *       added that you shouldn't look up instance methods through the
	 *       class).
	 *       
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


	} else if (((PyObjCClassObject*)self)->isCFWrapper) {
		/* This is a wrapper class for a CoreFoundation type
		 * that isn't tollfree bridged. Don't update the 
		 * Objective-C class because all CF types share the
		 * same ObjC class (except for the toll-free bridged
		 * ones).
		 */

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
		Method curMethod;
		Class  curClass;
		int r;
		BOOL b;
		
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
		
		if (PyObjCSelector_IsClassMethod(newVal)) {
			curMethod = class_getClassMethod(
					PyObjCClass_GetClass(self),
					PyObjCSelector_GetSelector(newVal));
			curClass = object_getClass(
						PyObjCClass_GetClass(self));
		} else {
			curMethod = class_getInstanceMethod(
					PyObjCClass_GetClass(self),
					PyObjCSelector_GetSelector(newVal));
			curClass = PyObjCClass_GetClass(self);
		}

		if (curMethod) {
			method_setImplementation(curMethod,
				PyObjCFFI_MakeIMPForPyObjCSelector(
					(PyObjCSelector*)newVal));
		} else {
			char* types = strdup(
				PyObjCSelector_Signature(newVal));
			if (types == NULL) {
				Py_DECREF(newVal);
				return -1;
			}
			b = class_addMethod(
				curClass,
				PyObjCSelector_GetSelector(newVal),
				PyObjCFFI_MakeIMPForPyObjCSelector(
					(PyObjCSelector*)newVal),
				types);
			if (!b) {
				free(types);
				Py_DECREF(newVal);
				return -1;
			}
		}

		if (PyObjCSelector_IsClassMethod(newVal)) {
			r = PyDict_SetItem(self->ob_type->tp_dict, name, newVal);

		} else {
			r = PyDict_SetItem(((PyTypeObject*)self)->tp_dict, name, newVal);
		}
		Py_DECREF(newVal);
		if (r == -1) {
			PyErr_NoMemory();
			return -1;
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
		class_getName(self_class), 
		class_getName(other_class));

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
		const char* nm = class_getName(cls);
		if (strcmp(nm, "NSCFType") == 0) {
			return PyString_FromString(((PyTypeObject*)self)->tp_name);
		} else {
			return PyString_FromString(nm);
		}
	}
}

PyDoc_STRVAR(cls_version_doc, "get/set the version of a class");
static PyObject* 
cls_get_version(PyObject* self, void* closure __attribute__((__unused__)))
{
	Class cls = PyObjCClass_GetClass(self);
	if (cls == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	} else {
		return PyInt_FromLong(class_getVersion(cls));
	}
}
static  int
cls_set_version(PyObject* self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
	Class cls = PyObjCClass_GetClass(self);
	int   val;
	int   r;

	r = depythonify_c_value(@encode(int), newVal, &val);
	if (r == -1) {
		return -1;
	}
	class_setVersion(cls, val);
	return 0;
}


static PyGetSetDef class_getset[] = {
	{
		"pyobjc_classMethods",
		cls_get_classMethods,
		NULL,
		cls_get_classMethods_doc,
		0
	},
	{
		"pyobjc_instanceMethods",
		cls_get_instanceMethods,
		NULL,
		cls_get_instanceMethods_doc,
		0
	},
	{
		"__version__",
		cls_get_version,
		cls_set_version,
		cls_version_doc,
		0
	},

	{
		/* Access __name__ through a property: Objective-C name 
		 * might change due to posing.
		 */
		"__name__",
		cls_get__name__,
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

char*
PyObjC_SELToPythonName(SEL sel, char* buf, size_t buflen)
{
	size_t res = snprintf(buf, buflen, "%s", sel_getName(sel));
	char* cur;

	if (res != strlen(sel_getName(sel))) {
		return NULL;
	}
	if (PyObjC_IsPythonKeyword(buf)) {
		res = snprintf(buf, buflen, "%s__", sel_getName(sel));
		if (res != 2+strlen(sel_getName(sel))) {
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
add_class_fields(Class objc_class, PyObject* pubDict, PyObject* protDict, PyObject* classDict)
{
	Class     cls;
	Method*   methods;
	unsigned int method_count, i;
	PyObject* descr;
	char      selbuf[1024];
	PyObject* dict;

	if (objc_class == NULL) return 0;

	/*
	 * First add instance methods
	 */

	methods = class_copyMethodList(objc_class, &method_count);
	for (i = 0; i < method_count; i++) {
		char* name;
		PyObject* curItem;

		dict = pubDict;
		if (*sel_getName(method_getName(methods[i])) == '_') {
			if (PyObjC_HideProtected) {
				dict = protDict;
			}
		}
		name = (char*)PyObjC_SELToPythonName(
					method_getName(methods[i]), 
					selbuf, 
					sizeof(selbuf));
		if (name == NULL) continue;

		curItem = PyDict_GetItemString(dict, name);
		if (curItem == NULL) {
			PyErr_Clear();
		} else if (!PyObjCNativeSelector_Check(curItem)) {
			continue;
		}

		descr = PyObjCSelector_NewNative(
				objc_class,
				method_getName(methods[i]),
				method_getTypeEncoding(methods[i]),
				NO);

		if (PyDict_SetItemString(
				dict, 
				name,
				descr) != 0) {

			Py_DECREF(descr); 
			free(methods);
			return -1;
		}
		Py_DECREF(descr); 
	}
	free(methods);



	/* 
	 * Then add class methods
	 */


	cls = object_getClass(objc_class);
	methods = class_copyMethodList(cls, &method_count);
	for (i = 0; i < method_count; i++) {
		PyObject* curItem;
		char* name;

		dict = classDict;

		name = PyObjC_SELToPythonName(
			method_getName(methods[i]), 
			selbuf, 
			sizeof(selbuf));
		if (name == NULL) continue;

		curItem = PyDict_GetItemString(dict, name);
		if (curItem == NULL) {
		} else if (!PyObjCNativeSelector_Check(curItem)) {
			continue;
		}

		descr = PyObjCSelector_NewNative(
			objc_class,
			method_getName(methods[i]),
			method_getTypeEncoding(methods[i]),
			YES);

		if (PyDict_SetItemString(dict, 
				selbuf,
				descr) != 0) {
			Py_DECREF(descr);
			free(methods);
			return -1;
		}
		Py_DECREF(descr);
	}
	free(methods);

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
 *
 * Returns a new reference.
 */
PyObject* 
PyObjCClass_New(Class objc_class)
{
	PyObject* args;
	PyObject* dict;
	PyObject* result;
	PyObject* bases;
	PyObjCClassObject* info;
	Ivar var;
	PyObject* protectedMethods;
	PyTypeObject* metaclass;
	const char* className;

	result = objc_class_locate(objc_class);
	if (result != NULL) {
		return result;
	}

	protectedMethods = PyDict_New();
	if (protectedMethods == NULL) {
		return NULL;
	}

	if (class_isMetaClass(objc_class)) {
		result =  (PyObject*)PyObjCClass_NewMetaClass(objc_class);
		Py_DECREF(result);
		return result;
	}

	metaclass = PyObjCClass_NewMetaClass(objc_class);
	if (metaclass == NULL) {
		Py_DECREF(protectedMethods);
		return NULL;
	}


	dict = PyDict_New();
	PyDict_SetItemString(dict, "__slots__", PyTuple_New(0));

	bases = PyTuple_New(1);

	if (class_getSuperclass(objc_class) == NULL) {
		PyTuple_SET_ITEM(bases, 0, (PyObject*)&PyObjCObject_Type);
		Py_INCREF(((PyObject*)&PyObjCObject_Type));
	} else {
		PyTuple_SET_ITEM(bases, 0, 
			PyObjCClass_New(class_getSuperclass(objc_class)));
	} 
	args = PyTuple_New(3);
	className = class_getName(objc_class);
	PyTuple_SetItem(args, 0, PyString_FromString(className));
	PyTuple_SetItem(args, 1, bases);
	PyTuple_SetItem(args, 2, dict);
	bases = NULL; dict = NULL;

	result = PyType_Type.tp_new(metaclass, args, NULL);
	Py_DECREF(args); Py_DECREF(metaclass);
	if (result == NULL) return NULL;

	info = (PyObjCClassObject*)result;
	info->class = objc_class;
	info->sel_to_py = NULL;
	info->method_magic = 0;
	info->dictoffset = 0;
	info->useKVO = 0;
	info->delmethod = NULL;
	info->hasPythonImpl = 0;
	info->isCFWrapper = 0;
	info->protectedMethods = protectedMethods;

	/*
	 * Support the buffer protocol in the wrappers for NSData and
	 * NSMutableData, the only two classes where this makes sense.
	 */
	if (strcmp(className, "NSData") == 0) {
		((PyTypeObject *)result)->tp_as_buffer = &nsdata_as_buffer;
	} else if (strcmp(className, "NSMutableData") == 0) {
		((PyTypeObject *)result)->tp_as_buffer = &nsmutabledata_as_buffer;
	}

	var = class_getInstanceVariable(objc_class, "__dict__");
	if (var != NULL) {
		info->dictoffset = ivar_getOffset(var);
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
PyObjCClass_FindSelector(PyObject* cls, SEL selector, BOOL class_method)
{
	PyObjCClassObject* info;
	PyObject*          result;

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
				(char*)sel_getName(selector));	
	if (result != NULL) {
		if (result == Py_None) {
			/* negative cache entry */
			PyErr_Format(PyExc_AttributeError,
				"No selector %s",
				sel_getName(selector));
			return NULL;
		}
		Py_INCREF(result);
		return result;
	}


	/* Not in the cache. Walk the MRO to check
	 * every method object.
	 *
	 * (We could also generate the most likely
	 * python name and check that, but the most
	 * likely reason we're called is that this
	 * method doesn't exist or isn't good enough)
	 */

	PyObject* mro = ((PyTypeObject*)cls)->tp_mro;
	Py_ssize_t i, n;

	n = PyTuple_GET_SIZE(mro);
	for (i = 0; i < n; i++) {
		PyObject* c = PyTuple_GET_ITEM(mro, i);

		if (!PyObjCClass_Check(c)) {
			continue;
		}

		PyObject* dict;
		
		if (class_method) {
			dict = c->ob_type->tp_dict;
		} else {
			dict = ((PyTypeObject*)c)->tp_dict;
		}

		PyObject* value;
		Py_ssize_t pos = 0;

		while (PyDict_Next(dict, &pos, NULL, &value)) {
			if (!PyObjCSelector_Check(value)) continue;

			if (sel_isEqual(PyObjCSelector_GetSelector(value), selector)) {
				PyDict_SetItemString(info->sel_to_py, 
					(char*)sel_getName(selector), value);	
				Py_INCREF(value);
				return value;
			}
		}
	}

	/* If all else fails, ask the actual class (getattro also does this) */
	result = PyObjCSelector_FindNative(cls, 
				sel_getName(selector));
	if (result) {
		return result;
	}

	PyErr_Format(PyExc_AttributeError,
		"No selector %s", sel_getName(selector));
	PyDict_SetItemString(info->sel_to_py, 
			(char*)sel_getName(selector), Py_None);
	return NULL;
}

Py_ssize_t
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

	if (class_getSuperclass(cls) == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(class_getSuperclass(cls));
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(class_getName(cls));
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
	Py_ssize_t i, len;

	if (PyObjC_ClassExtender == NULL || cls == NULL) return 0;

	if (!PyObjCClass_Check(cls)) {
		PyErr_SetString(PyExc_TypeError, "not a class");
		return -1;
	}

	objc_cls = PyObjCClass_GetClass(cls);

	if (class_getSuperclass(objc_cls) == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(class_getSuperclass(objc_cls));
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(class_getName(objc_cls));
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


PyObject* PyObjCClass_ClassForMetaClass(PyObject* meta)
{
	if (meta == NULL) return NULL;

	return PyObjCClass_New(objc_metaclass_locate(meta));
}
