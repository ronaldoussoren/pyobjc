/*
 * This file implements the object/type used to implement
 *	anObject.pyobjc_classMethods.description()
 * and
 *	anObject.pyobjc_instanceMethods.description()
 *
 * NOTES:
 *	Does not support reflection. That can be added when
 *	needed.
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
			objc_object = GETISA(objc_object);
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


	if (strcmp(GETISA(objc_object)->name, "_NSZombie") == 0) {
		PyErr_Format(PyExc_AttributeError,
			"Cannot access NSProxy.%s", name);
		return NULL;
	}

	if (class_method && strcmp(((Class)objc_object)->name, "NSProxy") == 0 ){
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
		objc_object = GETISA(objc_object);
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
	struct objc_method_list* mlist;
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
			cls = GETISA(obj);
			bound_self = (PyObject*)self->ob_type;
			objc_class = GETISA(cls); 
		} else {
			cls = GETISA(obj);
			objc_class = cls;
			bound_self = self;
		}

	} else if (PyObjCClass_Check(self)) {
		cls = PyObjCClass_GetClass(self);
		objc_class = cls;
		if (class_method) {
			objc_class = GETISA(cls);
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
		mlist = PyObjCRT_NextMethodList(objc_class, &iterator);
		while (mlist != NULL) {
			PyObjCRT_Method_t meth;
			PyObject* v;
			int i;

			for (i = 0; i < mlist->method_count; i++) {
				char* name;

				meth = mlist->method_list + i;
				name = PyObjC_SELToPythonName(meth->method_name, 
					buf, sizeof(buf));
				
				v = PyObject_GetAttrString(self, name);
				if (v == NULL) {
					PyErr_Clear();
				} else if (!PyObjCSelector_Check(v)) {
					Py_DECREF(v);
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
						cls, meth->method_name,
						meth->method_types, class_method);
					if (v == NULL) {
						Py_DECREF(res);
						return NULL;
					}
				}

				if (PyDict_SetItemString(res, name, v) == -1) {
					Py_DECREF(v); 
					Py_DECREF(res);
					return NULL;
				}
				Py_DECREF(v);

			}
			mlist = PyObjCRT_NextMethodList(objc_class, &iterator);
		}

		objc_class = ((Class)objc_class)->super_class;
		cls = ((Class)cls)->super_class;
	}

	return res;
}
	

typedef struct {
	PyObject_HEAD
	PyObject*	base;
	int		class_method;
} ObjCMethodAccessor;

static void
obj_dealloc(ObjCMethodAccessor* self)
{
	Py_XDECREF(self->base);
	self->base = NULL;

	if (self->ob_type->tp_free) {
		self->ob_type->tp_free((PyObject*)self);
	} else {
		PyObject_Del(self);
	}
}

static PyObject*
obj_getattro(ObjCMethodAccessor* self, PyObject* name)
{
	PyObject* result;
	int	  class_method;

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


	result = PyObject_GenericGetAttr((PyObject*)self, name);
	if (result == NULL) {
		PyErr_Clear();
	} else {
		return result;
	}

	/* First try to access through base, this way the method replacements
	 * in objc._convenience are seen here.
	 */
	result = PyObject_GetAttr(self->base, name);
	if (result == NULL) {
		PyErr_Clear();
	} else if (!PyObjCSelector_Check(result)) {
		Py_DECREF(result);
		result = NULL;
	} else {
		class_method = ((PyObjCSelector*)result)->sel_flags & PyObjCSelector_kCLASS_METHOD;
		if (!self->class_method  == !class_method) {
			/* NOTE: ! is used to normalize the values */
			return result;
		} 
		Py_XDECREF(result);
		result = NULL;
	}

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
obj_repr(ObjCMethodAccessor* self)
{
	char buf[1024];
	PyObject* repr;

	repr = PyObject_Repr(self->base);
	if (repr == NULL) return NULL;
	if (!PyString_Check(repr)) {
		PyErr_SetString(PyExc_TypeError, "base repr was not a string");
		return NULL;
	}

	snprintf(buf, sizeof(buf), 
		"<%s method-accessor for %s>",
		self->class_method?"class":"instance",
		PyString_AS_STRING(repr));
	Py_DECREF(repr);
	return PyString_FromString(buf);
}

static PyTypeObject ObjCMethodAccessor_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,					/* ob_size */
	"objc.method_acces",			/* tp_name */
	sizeof(ObjCMethodAccessor),		/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	(destructor)obj_dealloc,	 	/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	(reprfunc)obj_repr,			/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	(getattrofunc)obj_getattro,		/* tp_getattro */
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
	0					/* tp_weaklist */
#if PY_VERSION_HEX >= 0x020300A2
	, 0					/* tp_del */
#endif
};

PyObject* ObjCMethodAccessor_New(PyObject* base, int class_method)
{
	ObjCMethodAccessor* result;

	result = PyObject_New(ObjCMethodAccessor, &ObjCMethodAccessor_Type);
	if (result == NULL) return NULL;

	result->base = base;
	Py_XINCREF(base);
	result->class_method = class_method;

	return (PyObject*)result;
}
