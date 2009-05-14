/*
 * This file implements the object/type used to implement
 *	anObject.pyobjc_classMethods.description()
 * and
 *	anObject.pyobjc_instanceMethods.description()
 */
#include "pyobjc.h"

static PyObject* 
find_selector(PyObject* self, char* name, int class_method)
{
	SEL   sel = PyObjCSelector_DefaultSelector(name);
	volatile id    objc_object;
	NSMethodSignature* methsig;
	char  buf[1024];
	volatile int   unbound_instance_method = 0;
	char* flattened;

	if (name[0] == '_' && name[1] == '_') {
		/*
		 * FIXME: Some classes (NSFault, NSFinalProxy) crash hard
		 * on these names
		 */
		PyErr_Format(PyExc_AttributeError,
			"No selector %s", name);
		return NULL;
	}

	if (PyObjCClass_Check(self)) {
		objc_object = (id)PyObjCClass_GetClass(self);

		if (!class_method) {
			unbound_instance_method = 1;
		}
	} else if (PyObjCObject_Check(self)) {
		objc_object = PyObjCObject_GetObject(self);
		if (objc_object == NULL) {
			PyErr_SetString(PyExc_AttributeError, 
				"nil has no methods");
			return NULL;
		}

		if (class_method) {
			objc_object = (id)object_getClass(objc_object);
		}
	} else {
		PyErr_Format(PyExc_TypeError,
			"Need Objective-C class or instance, got "
			"a %s", self->ob_type->tp_name);
		return NULL;
	}

	if (objc_object == nil) {
		PyErr_Format(PyExc_AttributeError,
			"<nil> doesn't have attribute %s", name);
		return NULL;
	}


	if (strcmp(object_getClassName(objc_object), "_NSZombie") == 0) {
		PyErr_Format(PyExc_AttributeError,
			"Cannot access NSProxy.%s", name);
		return NULL;
	}

	if (class_method && strcmp(class_getName((Class)objc_object), "NSProxy") == 0 ){
		if (sel == @selector(methodSignatureForSelector:)) {
			PyErr_Format(PyExc_AttributeError,
				"Cannot access NSProxy.%s", name);
			return NULL;
		}
	}


	PyObjC_DURING
		if (unbound_instance_method) {
			methsig = [objc_object instanceMethodSignatureForSelector:sel];
		} else {
			methsig = [objc_object methodSignatureForSelector:sel];
		}

	PyObjC_HANDLER
		methsig = nil;

	PyObjC_ENDHANDLER

	if (methsig == NULL) {
		PyErr_Format(PyExc_AttributeError,
			"No selector %s", name);
		return NULL;
	}

	if (!class_method) {
		objc_object = (id)object_getClass(objc_object);
	}

	flattened = PyObjC_NSMethodSignatureToTypeString(
			methsig, buf, sizeof(buf));
	if (flattened == NULL) {
		return NULL;
	}

	return PyObjCSelector_NewNative((Class)objc_object, sel,
		flattened, class_method);
}

static PyObject*
make_dict(PyObject* self, int class_method)
{
	Class     cls;
	PyObject* res;
	Method* methods;
	unsigned int i, method_count;
	void* iterator;
	char  buf[256];
	Class    objc_class;
	PyObject* bound_self;

	if (PyObjCObject_Check(self)) {
		id obj = PyObjCObject_GetObject(self);
		if (obj == NULL) {
			return PyDict_New();
		}

		if (class_method) {
			cls = object_getClass(obj);
			bound_self = (PyObject*)self->ob_type;
			objc_class = object_getClass(cls); 
		} else {
			cls = object_getClass(obj);
			objc_class = cls;
			bound_self = self;
		}

	} else if (PyObjCClass_Check(self)) {
		cls = PyObjCClass_GetClass(self);
		objc_class = cls;
		if (class_method) {
			objc_class = object_getClass(cls);
			bound_self = self;
		} else {
			bound_self = NULL;
		}

	} else {
		PyErr_BadInternalCall();
		return NULL;
	}

	res = PyDict_New();
	if (res == NULL) {
		return NULL;
	}

	while (objc_class != NULL && cls != NULL) {
		iterator = NULL;
		methods = class_copyMethodList(objc_class, &method_count);
		if (methods == NULL) {
			objc_class = class_getSuperclass((Class)objc_class);
			cls = class_getSuperclass((Class)cls);
		}

		for (i = 0; i < method_count; i++) {
			PyObject* v;
			char* name;

			name = PyObjC_SELToPythonName(
					method_getName(methods[i]), 
					buf, sizeof(buf));
			
			v = PyObject_GetAttrString(self, name);
			if (v == NULL) {
				PyErr_Clear();
			} else if (!PyObjCSelector_Check(v)) {
				Py_DECREF(v);
				free(methods);
				v = NULL;
			} else {
				int cm;
				cm = ((PyObjCSelector*)v)->sel_flags & PyObjCSelector_kCLASS_METHOD;
				if (!cm  != !class_method) {
					Py_DECREF(v);
					v = NULL;
				}
			}

			if (v == NULL) {
				v = PyObjCSelector_NewNative(
					cls, method_getName(methods[i]),
					method_getTypeEncoding(methods[i]), 
					class_method);
				if (v == NULL) {
					free(methods);
					Py_DECREF(res);
					return NULL;
				}
			}

			if (PyDict_SetItemString(res, name, v) == -1) {
				Py_DECREF(v); 
				Py_DECREF(res);
				free(methods);
				return NULL;
			}
			Py_DECREF(v);

		}

		free(methods);

		objc_class = class_getSuperclass((Class)objc_class);
		cls = class_getSuperclass((Class)cls);
	}

	return res;
}
	

typedef struct {
	PyObject_HEAD
	PyObject*	base;
	int		class_method;
} ObjCMethodAccessor;

static void
obj_dealloc(PyObject* _self)
{
	ObjCMethodAccessor* self = (ObjCMethodAccessor*)_self;
	Py_XDECREF(self->base);
	self->base = NULL;

	if (self->ob_type->tp_free) {
		self->ob_type->tp_free((PyObject*)self);
	} else {
		PyObject_Del(self);
	}
}

static PyObject*
obj_getattro(PyObject* _self, PyObject* name)
{
	ObjCMethodAccessor* self = (ObjCMethodAccessor*)_self;
	PyObject* result = NULL;

	if (!PyString_Check(name)) {
		PyErr_Format(PyExc_TypeError, 
			"Expecting string, got %s",
			name->ob_type->tp_name);
		return NULL;
	}

	if (strcmp(PyString_AS_STRING(name), "__dict__") == 0) {

		PyObject* dict;
		dict = make_dict(self->base, self->class_method);
		return dict;

		/*
		 * Ronald: I'd prefer to add the code below, because our 
		 * __dict__ cannot be modified, but then dir() doesn't work.
		 * The current version is save enough, but might give surprising
		 * behaviour (you can change pyobjc_instancMethods.__dict__,
		 * but those changes have no effect).
		result  = PyDictProxy_New(dict);
		Py_DECREF(dict);
		return result;
		 */
	}

	if (strcmp(PyString_AS_STRING(name), "__methods__") == 0) {
		PyErr_SetString(PyExc_AttributeError,
			"No such attribute: __methods__");
		return NULL;
	}

	if (strcmp(PyString_AS_STRING(name), "__members__") == 0) {
		PyErr_SetString(PyExc_AttributeError,
			"No such attribute: __members__");
		return NULL;
	}

	if (self->class_method) {
		if (PyObjCClass_Check(self->base)) {
			result = PyObject_GetAttr(self->base, name);
		} else {
			/* Getting a class method of an instance? */
			result = PyObject_GetAttr((PyObject*)(self->base->ob_type), name);
		}

	} else {
		if (PyObjCClass_Check(self->base)) {
			/* Walk the mro and look in the class dict */
			PyObject* mro = ((PyTypeObject*)self->base)->tp_mro;
			Py_ssize_t i, len;

			len = PyTuple_GET_SIZE(mro);
			for (i = 0; i < len && result == NULL; i++) {
				PyObject* c = PyTuple_GET_ITEM(mro, i);
				if (!PyObjCClass_Check(c)) continue;

				PyObject* dict = ((PyTypeObject*)c)->tp_dict;
				PyObject* v = PyDict_GetItem(dict, name);
				if (v != NULL) {
					if (PyObjCSelector_Check(v)) {
						/* Found it, use the 
						 * descriptor mechanism to
						 * fetch the actual result
						 */
						v = v->ob_type->tp_descr_get(v, NULL, (PyObject*)v->ob_type);
						result = v;
						Py_INCREF(result);
						break;
					}
				}
			}
	
		} else {
			result = PyObject_GetAttr(self->base, name);
		}
	}

	if (result != NULL) {
		if (!PyObjCSelector_Check(result)) {
			Py_DECREF(result);
			result = NULL;
		} else {
			return result;
		}
	}

	/* Didn't find the selector the first trip around, try harder. */
	result = find_selector(self->base, 
		PyString_AS_STRING(name), self->class_method);
	if (result == NULL) return result;

	if (self->class_method && PyObjCObject_Check(self->base)) {
		/* Class method */
		((PyObjCSelector*)result)->sel_self = (PyObject*)(self->base->ob_type);
	} else if (!self->class_method && PyObjCClass_Check(self->base)) {
		/* Unbound instance method */
		((PyObjCSelector*)result)->sel_self = NULL;
	} else {
		/* Bound instance method */
		((PyObjCSelector*)result)->sel_self = self->base;
	}
	Py_XINCREF(((PyObjCSelector*)result)->sel_self);
	return result;
}

static PyObject*
obj_repr(PyObject* _self)
{
	ObjCMethodAccessor* self = (ObjCMethodAccessor*)_self;
	PyObject* rval;
	PyObject* repr;

	repr = PyObject_Repr(self->base);
	if (repr == NULL) return NULL;
	if (!PyString_Check(repr)) {
		PyErr_SetString(PyExc_TypeError, "base repr was not a string");
		return NULL;
	}


	rval = PyString_FromFormat("<%s method-accessor for %s>",
		self->class_method ? "class" : "instance",
		PyString_AS_STRING(repr));
	Py_DECREF(repr);
	return rval;
}

PyTypeObject PyObjCMethodAccessor_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.method_acces",			/* tp_name */
	sizeof(ObjCMethodAccessor),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	obj_dealloc,	 			/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	obj_repr,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	obj_getattro,				/* tp_getattro */
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
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0, 					/* tp_subclasses */
	0,					/* tp_weaklist */
	0					/* tp_del */
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

};

PyObject* PyObjCMethodAccessor_New(PyObject* base, int class_method)
{
	ObjCMethodAccessor* result;

	result = PyObject_New(ObjCMethodAccessor, &PyObjCMethodAccessor_Type);
	if (result == NULL) return NULL;

	result->base = base;
	Py_XINCREF(base);
	result->class_method = class_method;

	return (PyObject*)result;
}
