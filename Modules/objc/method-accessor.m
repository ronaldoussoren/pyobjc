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
#include "objc_support.h"

static char* 
flatten_signature(NSMethodSignature* sig, char* buf, int buflen)
{
	char* cur = buf;
	int   curlen = buflen;
	int   r;
	int   i, len;

	r = snprintf(cur, curlen, "%s", [sig methodReturnType]);
	if (r >= curlen) goto error;
	cur += r;
	curlen -= r;

	len = [sig numberOfArguments];
	for (i = 0; i < len; i ++) {
		r = snprintf(cur, curlen, "%s", [sig getArgumentTypeAtIndex:i]);
		if (r >= curlen) goto error;
		cur += r;
		curlen -= r;
	}
	*cur = '\0';
	return buf;

error:
	/* FIXME, however 1024 characters should be enough for any reasonable
	 * signature. E.g. this can wait until we run into problems.
	 */
	PyErr_SetString(PyExc_MemoryError, "PyObC: extremely long signature");
	return NULL;
}

static PyObject* 
find_selector(PyObject* self, char* name, int class_method)
{
	SEL   sel = ObjCSelector_DefaultSelector(name);
	id    objc_object;
	NSMethodSignature* methsig;
	char  buf[1024];
	int   unbound_instance_method = 0;
	char* flattened;

	if (strcmp(name, "__class__") == 0) {
		/* Someone does 'type(object.pybojc_instanceMethods)' */
		Py_INCREF(self->ob_type);
		return (PyObject*)self->ob_type;
	}

	if (name[0] == '_' && name[1] == '_') {
		/*
		 * FIXME: Some classes (NSFault, NSFinalProxy) crash hard
		 * on these names
		 */
		ObjCErr_Set(PyExc_AttributeError,
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
		ObjCErr_Set(PyExc_TypeError,
			"Need Objective-C class or instance, got "
			"a %s", self->ob_type->tp_name);
		return NULL;
	}

	if (class_method && strcmp(((Class)objc_object)->name, "NSProxy") == 0){
		if (sel == @selector(methodSignatureForSelector:)) {
			ObjCErr_Set(PyExc_AttributeError,
				"Cannot access NSProxy.%s", name);
			return NULL;
		}
	}

	if (unbound_instance_method) {
		methsig = [objc_object instanceMethodSignatureForSelector:sel];
	} else {
		methsig = [objc_object methodSignatureForSelector:sel];
	}

	if (methsig == NULL) {
		ObjCErr_Set(PyExc_AttributeError,
			"No selector %s", name);
		return NULL;
	}

	if (!class_method) {
		objc_object = GETISA(objc_object);
	}

	flattened = flatten_signature(methsig, buf, sizeof(buf));
	if (flattened == NULL) {
		return NULL;
	}

	return ObjCSelector_NewNative((Class)objc_object, sel,
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
	id    objc_class;
	PyObject* bound_self;

	if (PyObjCObject_Check(self)) {
		id obj = PyObjCObject_GetObject(self);
		if (obj == NULL) {
			return PyDict_New();
		}

		if (class_method) {
			cls = GETISA(GETISA(obj));
			bound_self = (PyObject*)self->ob_type;
			objc_class = GETISA(obj);
		} else {
			cls = GETISA(obj);
			objc_class = cls;
			bound_self = self;
		}

	} else if (PyObjCClass_Check(self)) {
		cls = PyObjCClass_GetClass(self);
		objc_class = cls;
		if (class_method) {
			cls = GETISA(cls);
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

	while (objc_class != NULL) {
		iterator = NULL;
		mlist = class_nextMethodList(objc_class, &iterator);
		while (mlist != NULL) {
			METHOD meth;
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
				} else if (!ObjCSelector_Check(v)) {
					Py_DECREF(v);
					v = NULL;
				} else {
					int cm;
					cm = ((ObjCSelector*)v)->sel_flags & ObjCSelector_kCLASS_METHOD;
					if (!cm  != !class_method) {
						Py_DECREF(v);
						v = NULL;
					}
				}

				if (v == NULL) {
					v = ObjCSelector_NewNative(
						objc_class, meth->method_name,
						meth->method_types, class_method);
					if (v == NULL) {
						Py_DECREF(res);
						return NULL;
					}
				}

				if (PyDict_SetItemString(res, name, v) == -1) {
					Py_DECREF(res);
					return NULL;
				}
				Py_DECREF(v);

			}
			mlist = class_nextMethodList(objc_class, &iterator);
		}

		objc_class = ((Class)objc_class)->super_class;
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
		ObjCErr_Set(PyExc_TypeError, 
			"Expecting string, got %s",
			name->ob_type->tp_name);
		return NULL;
	}

	if (strcmp(PyString_AS_STRING(name), "__dict__") == 0) {
		return make_dict(self->base, self->class_method);
	}

	/* First try to access through base, this way the method replacements
	 * in objc._convenience are seen here.
	 */
	result = PyObject_GetAttr(self->base, name);
	if (result == NULL) {
		PyErr_Clear();
	} else if (!ObjCSelector_Check(result)) {
		Py_DECREF(result);
		result = NULL;
	} else {
		class_method = ((ObjCSelector*)result)->sel_flags & ObjCSelector_kCLASS_METHOD;
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
		((ObjCSelector*)result)->sel_self = (PyObject*)(self->base->ob_type);
	} else if (!self->class_method && PyObjCClass_Check(self->base)) {
		/* Unbound instance method */
		((ObjCSelector*)result)->sel_self = NULL;
	} else {
		/* Bound instance method */
		((ObjCSelector*)result)->sel_self = self->base;
	}
	Py_XINCREF(((ObjCSelector*)result)->sel_self);
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
