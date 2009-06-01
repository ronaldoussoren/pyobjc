/*
 * Implementation of objective-C object wrapper
 *
 * NOTE: We're using CFRetain and CFRelease to manage the retaincount of the Objective-C 
 * objects because that will do the right thing when Garbage Collection is involved.
 */
#include "pyobjc.h"

#include <stddef.h>

#include <objc/Object.h>

/* 
 * Support for NSKeyValueObserving on MacOS X 10.3 and later.
 *      
 */     

/* 
 * XXX: for reasons beyond my current comprehension the "legacy" block must be active, otherwise we
 * get a fatal python error.
 */
#if !defined(MAC_OS_X_VERSION_MIN_REQUIRED) || MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_3

/* Deal with platforms that don't support KVO */

static int
_KVOHackLevel(void) {
	static int _checkedKVO = 0;
	if (_checkedKVO == 0) {
		if ([NSObject instancesRespondToSelector:@selector(willChangeValueForKey:)] &&
			[NSObject instancesRespondToSelector:@selector(didChangeValueForKey:)]) {
			_checkedKVO = 1; 

		} else {

			_checkedKVO = -1;
		}
	}
	return _checkedKVO;
}

static void
_UseKVO(NSObject *self, NSString *key, BOOL willChange)
{           
    PyObjC_DURING
        int _checkedKVO = _KVOHackLevel();
        if (_checkedKVO == -1 || [key characterAtIndex:0] == (unichar)'_') {
		/* pass */
        } else if (willChange) {
            [self willChangeValueForKey:key];
        } else {
            [self didChangeValueForKey:key];
        }
    PyObjC_HANDLER
    PyObjC_ENDHANDLER
}           

#else 

static void
_UseKVO(NSObject *self, NSString *key, BOOL willChange)
{           
    PyObjC_DURING
        if ([key characterAtIndex:0] == (unichar)'_') {
	    /* pass */
	} else if (willChange) {
            [self willChangeValueForKey:key];
        } else {
            [self didChangeValueForKey:key];
        }
    PyObjC_HANDLER
    PyObjC_ENDHANDLER
}           

#endif
			
static PyObject*
object_new(
	PyTypeObject*  type __attribute__((__unused__)),
	PyObject* args,
	PyObject* kwds)
{
static char* keywords[] = { "cobject", NULL };
	PyObject* arg = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "|O", keywords, &arg)) {
		return NULL;
	}

	if (arg == NULL || !PyCObject_Check(arg)) {
		PyErr_SetString(PyExc_TypeError, 
			"Use class methods to instantiate new Objective-C objects");
		return NULL;
	} else {
		NSObject* v = PyCObject_AsVoidPtr(arg);

		return pythonify_c_value(@encode(NSObject), &v);
	}
}

static PyObject*
object_repr(PyObject* _self)
{
	PyObjCObject* self = (PyObjCObject*)_self;
	PyObject* res;

	if (self->flags & PyObjCObject_kMAGIC_COOKIE) {
		return PyString_FromFormat(
			"<%s objective-c magic instance %p>",
			self->ob_type->tp_name, self->objc_object);
	}

	if ((self->flags & PyObjCObject_kUNINITIALIZED) == 0 && !PyObjCObject_IsClassic(self)) {
		/* Try to call the method 'description', which is the ObjC
		 * equivalent of __repr__. If that fails we'll fall back to
		 * the default repr.
		 * Don't call 'description' for uninitialized objects, that
		 * is undefined behaviour and will crash the interpreter sometimes.
		 */
		res = PyObject_CallMethod((PyObject*)self, "description", NULL);
		if (res == NULL) {
			PyErr_Clear();
		} else {
			return res;
		}
	}
	return PyString_FromFormat(
		"<%s objective-c instance %p>",
		self->ob_type->tp_name, self->objc_object);
}

static void
object_del(PyObject* obj __attribute__((__unused__)))
{
	/* Dummy function, we do not want the default implementation */
}


static void
object_dealloc(PyObject* obj)
{
	/*
  	 * Save exception information, needed because releasing the object
	 * might clear or modify the exception state.
	 */
	PyObject* ptype, *pvalue, *ptraceback;
	PyErr_Fetch(&ptype, &pvalue, &ptraceback);

	if (PyObjCObject_IsBlock(obj)) {
		PyObjCMethodSignature* v = PyObjCObject_GetBlock(obj);
		Py_XDECREF(v);
		PyObjCObject_SET_BLOCK(obj, NULL);	
	}
			

	if (PyObjCObject_GetFlags(obj) != PyObjCObject_kDEALLOC_HELPER 
			&& PyObjCObject_GetObject(obj) != nil) {
		/* Release the proxied object, we don't have to do this when
		 * there is no proxied object.
		 */
		PyObjC_UnregisterPythonProxy(
			PyObjCObject_GetObject(obj), obj);

		if (PyObjCObject_IsClassic(obj)) {
			/* pass */

		} else if ((((PyObjCObject*)obj)->flags
				& PyObjCObject_kSHOULD_NOT_RELEASE)) {
			/* pass */

		} else if (((PyObjCObject*)obj)->flags 
				& PyObjCObject_kUNINITIALIZED) {
			/* Freeing of an uninitialized object, just leak because 
			 * there is no reliable manner to free such objects.
			 *
			 * - [obj release] doesn't work because some classes 
			 *   cause crashes for uninitialized objects
			 * - [[obj init] release] also doesn't work because 
			 *   not all classes implement -init
			 * - [obj dealloc] doesn't work for class 
			 *   clusters like NSArray.
			 */
			char buf[256];
			snprintf(buf, sizeof(buf), 
				"leaking an uninitialized object of type %s",
				obj->ob_type->tp_name);
			PyErr_Warn(PyObjCExc_UnInitDeallocWarning, buf);
			((PyObjCObject*)obj)->objc_object = nil;

		} else {
			PyObjC_DURING
				if (((PyObjCObject*)obj)->flags & PyObjCObject_kCFOBJECT) {
					CFRelease(((PyObjCObject*)obj)->objc_object);
				} else if (strcmp(object_getClassName(((PyObjCObject*)obj)->objc_object), 
						"NSAutoreleasePool") != 0) {

				        CFRelease(((PyObjCObject*)obj)->objc_object);
				} else {
					CFRelease(((PyObjCObject*)obj)->objc_object);
				}

			PyObjC_HANDLER
				NSLog(@"PyObjC: Exception during dealloc of proxy: %@",
					localException);

			PyObjC_ENDHANDLER
			((PyObjCObject*)obj)->objc_object = nil;
		}
	}

	obj->ob_type->tp_free(obj);

	PyErr_Restore(ptype, pvalue, ptraceback);
}


static inline PyObject*
_type_lookup(PyTypeObject* tp, PyObject* name)
{
	Py_ssize_t i, n;
	PyObject *mro, *base, *dict;
	PyObject *descr = NULL;
	PyObject* protDict;

	/* Look in tp_dict of types in MRO */
	mro = tp->tp_mro;
	assert(mro != NULL);
	assert(PyTuple_Check(mro));
	n = PyTuple_GET_SIZE(mro);
	for (i = 0; i < n; i++) {
		base = PyTuple_GET_ITEM(mro, i);

		if (PyClass_Check(base)) {
			dict = ((PyClassObject*)base)->cl_dict;
			protDict = NULL;
		} else {
			assert(PyType_Check(base));
			protDict = NULL;
			if (PyObjCClass_Check(base)) {
				PyObjCClass_CheckMethodList(base, 0);
				protDict = ((PyObjCClassObject*)base)->protectedMethods;
			}

			dict = ((PyTypeObject *)base)->tp_dict;
		}
		assert(dict && PyDict_Check(dict));
		descr = PyDict_GetItem(dict, name);
		if (descr != NULL) {
			break;
		}

		if (protDict) {
			descr = PyDict_GetItem(protDict, name);
			if (descr != NULL) {
				break;
			}
		}
	}

	return descr;
}

static PyObject** _get_dictptr(PyObject* obj)
{
	Py_ssize_t dictoffset;
	id obj_object;
	dictoffset = PyObjCClass_DictOffset((PyObject*)obj->ob_type);
	if (dictoffset == 0) return NULL;
	obj_object = PyObjCObject_GetObject(obj);
	assert(obj_object != nil);
	return (PyObject**)(((char*)obj_object) + dictoffset);
}


static PyObject *
object_getattro(PyObject *obj, PyObject * volatile name)
{
	PyTypeObject *tp = NULL;
	PyObject *descr = NULL;
	PyObject *res = NULL;
	descrgetfunc f;
	PyObject** dictptr;
	char* namestr;
	id obj_inst;

	if (!PyString_Check(name)){
#ifdef Py_USING_UNICODE
		/* The Unicode to string conversion is done here because the
		   existing tp_setattro slots expect a string object as name
		   and we wouldn't want to break those. */
		if (PyUnicode_Check(name)) {
			name = PyUnicode_AsEncodedString(name, NULL, NULL);
			if (name == NULL)
				return NULL;
		}
		else
#endif
		{
			PyErr_Format(PyExc_TypeError,
				"attribute name must be string, got %s",
				name->ob_type->tp_name);
			return NULL;
		}
	}
	else {
		Py_INCREF(name);
	}


	namestr = PyString_AS_STRING(name);

	obj_inst = PyObjCObject_GetObject(obj);
	if (!obj_inst) {
		PyErr_Format(PyExc_AttributeError,
		     "cannot access attribute '%.400s' of NIL '%.50s' object",
		     PyString_AS_STRING(name),
		     obj->ob_type->tp_name);
		goto done;
	}

	if (PyObjCObject_GetFlags(obj) & PyObjCObject_kMAGIC_COOKIE) {
		/* A magic cookie object, don't treat this like a normal
		 * object because that might cause havoc.
		 */

	} else {
		/* Special hack for KVO on MacOS X, when an object is observed it's 
		 * ISA is changed by the runtime. We change the python type as well.
		 */
		tp = (PyTypeObject*)PyObjCClass_New(object_getClass(obj_inst));

		descr = NULL;

		if (tp != obj->ob_type) {
			/* Workaround for KVO implementation feature */
			PyObject* dict;

			if (tp->tp_dict == NULL) {
				if (PyType_Ready(tp) < 0)
					goto done;
			}

// XXX: You'd expect the code below works, but it actually doesn't. Need to check why.
//			Py_DECREF(obj->ob_type);
//			obj->ob_type = tp;
//			

			PyObjCClass_CheckMethodList((PyObject*)tp, 0);
			dict = tp->tp_dict;

			assert(dict && PyDict_Check(dict));
			descr = PyDict_GetItem(dict, name);
		}
		Py_DECREF(tp); tp = NULL;
	}

	tp = obj->ob_type;
	if (tp->tp_dict == NULL) {
		if (PyType_Ready(tp) < 0)
			goto done;
	}

	/* replace _PyType_Lookup */
	if (descr == NULL) {
		descr = _type_lookup(tp, name);
	}

	f = NULL;
	if (descr != NULL &&
	    PyType_HasFeature(descr->ob_type, Py_TPFLAGS_HAVE_CLASS)) {
		f = descr->ob_type->tp_descr_get;
		if (f != NULL && PyDescr_IsData(descr)) {
			res = f(descr, obj, (PyObject*)obj->ob_type);
			goto done;
		}
	}

	if (strcmp(PyString_AS_STRING(name), "__del__") == 0) {
		res = PyObjCClass_GetDelMethod((PyObject*)obj->ob_type);
		if (res != NULL) {
			/* XXX: bind self */	
		}
		goto done;
	}

	/* First try the __dict__ */
	dictptr = _get_dictptr(obj);

	if (dictptr != NULL) {
		PyObject *dict;

		if (strcmp(PyString_AS_STRING(name), "__dict__") == 0) {
			res = *dictptr;
			if (res == NULL) {
				*dictptr = PyDict_New();
				if (*dictptr == NULL) {
					PyErr_Clear();
				}
				res = *dictptr;
			}
			if (res != NULL) {
				Py_INCREF(res);
				goto done;
			}
		} else {
			dict = *dictptr;
			if (dict != NULL) {
				res = PyDict_GetItem(dict, name);
				if (res != NULL) {
					Py_INCREF(res);
					goto done;
				}
			}
		}
	}

	if (f != NULL) {
		res = f(descr, obj, (PyObject*)obj->ob_type);
		goto done;
	}

	if (descr != NULL) {
		Py_INCREF(descr);
		res = descr;
		goto done;
	}

	if (!PyObjCObject_IsClassic(obj)) {
		res = PyObjCSelector_FindNative(obj, namestr);
		if (res) goto done;
	}

	PyErr_Format(PyExc_AttributeError,
	     "'%.50s' object has no attribute '%.400s'",
	     tp->tp_name, namestr);

done:
	if (res != NULL) {
		/* class methods cannot be accessed through instances */
		if (PyObjCSelector_Check(res) 
				&& PyObjCSelector_IsClassMethod(res)) {
			Py_DECREF(res);
			PyErr_Format(PyExc_AttributeError,
			     "'%.50s' object has no attribute '%.400s'",
			     tp->tp_name, PyString_AS_STRING(name));
			res = NULL;
		}
	}

	Py_DECREF(name);
	return res;
}


static int
object_setattro(PyObject *obj, PyObject *name, PyObject *value)
{
	PyTypeObject *tp = obj->ob_type;
	PyObject *descr;
	descrsetfunc f;
	PyObject** dictptr;
	int res;
	id obj_inst;
	NSString *obj_name;
	
	if (!PyString_Check(name)) {
#ifdef Py_USING_UNICODE
		/* The Unicode to string conversion is done here because the
		   existing tp_setattro slots expect a string object as name
		   and we wouldn't want to break those. */
		if (PyUnicode_Check(name)) {
			name = PyUnicode_AsEncodedString(name, NULL, NULL);
			if (name == NULL)
				return -1;
		}
		else
#endif
		{
			PyErr_Format(PyExc_TypeError,
				"attribute name must be string, got %s",
				name->ob_type->tp_name);
			return -1;
		}
	} else {
		Py_INCREF(name);
	}

	obj_inst = PyObjCObject_GetObject(obj);
	if (obj_inst == nil) {
		PyErr_Format(PyExc_AttributeError,
		     "Cannot set '%s.400s' on NIL '%.50s' object",
		     PyString_AS_STRING(name),
		     tp->tp_name);
		Py_DECREF(name);
		return -1;
	}

	obj_name = nil;
	if (((PyObjCClassObject*)tp)->useKVO) {
		if ((PyObjCObject_GetFlags(obj) & PyObjCObject_kUNINITIALIZED) == 0) {
			obj_name = [NSString stringWithUTF8String:PyString_AS_STRING(name)];
			_UseKVO((NSObject *)obj_inst, obj_name, YES);
		}
	}
	descr = _type_lookup(tp, name);
	f = NULL;
	if (descr != NULL &&
	    PyType_HasFeature(descr->ob_type, Py_TPFLAGS_HAVE_CLASS)) {
		f = descr->ob_type->tp_descr_set;
		if (f != NULL && PyDescr_IsData(descr)) {
			res = f(descr, obj, value);
			goto done;
		}
	}

	dictptr = _get_dictptr(obj);
	if (dictptr != NULL) {
		PyObject *dict;

		dict = *dictptr;
		
		if (dict == NULL && value != NULL) {
			dict = PyDict_New();
			if (dict == NULL) {
				res = -1;
				goto done;
			}
			
			*dictptr = dict;
		}
		if (dict != NULL) {
			if (value == NULL) {
				res = PyDict_DelItem(dict, name);
			} else {
				res = PyDict_SetItem(dict, name, value);
			}
			if (res < 0 && PyErr_ExceptionMatches(PyExc_KeyError)) {
				PyErr_SetObject(PyExc_AttributeError, name);
			}
			goto done;
		}
	}

	if (f != NULL) {
		res = f(descr, obj, value);
		goto done;
	}

	if (descr == NULL) {
		PyErr_Format(PyExc_AttributeError,
			     "'%.50s' object has no attribute '%.400s'",
			     tp->tp_name, PyString_AS_STRING(name));
		res = -1;
		goto done;
	}

	PyErr_Format(PyExc_AttributeError,
		     "'%.50s' object attribute '%.400s' is read-only",
		     tp->tp_name, PyString_AS_STRING(name));
	res = -1;
  done:
	if (obj_inst && obj_name) {
		_UseKVO((NSObject *)obj_inst, obj_name, NO);
	}
	Py_DECREF(name);
	return res;
}

PyDoc_STRVAR(objc_get_real_class_doc, "Return the current ISA of the object");
static PyObject* 
objc_get_real_class(PyObject* self, void* closure __attribute__((__unused__)))
{
	id obj_object;
	PyObject* ret;

	obj_object = PyObjCObject_GetObject(self);
	assert(obj_object != nil);
	ret = PyObjCClass_New(object_getClass(obj_object));
	if (ret != (PyObject*)self->ob_type) {
		Py_DECREF(self->ob_type);
		self->ob_type = (PyTypeObject*)ret;
		Py_INCREF(ret);
	}
	return ret;
}

PyDoc_STRVAR(obj_get_instanceMethods_doc,
"The attributes of this field are the instance methods of this object. This\n"
"can be used to force access to an instance method."
);
static PyObject*
obj_get_instanceMethods(PyObject* _self, void* closure __attribute__((__unused__)))
{
	PyObjCObject* self = (PyObjCObject*)_self;
	return PyObjCMethodAccessor_New((PyObject*)self, 0);
}

static PyObject*
obj_get_blocksignature(PyObject* self, void* closure __attribute__((__unused__)))
{
	if (PyObjCObject_IsBlock(self)) {
		PyObject* v = (PyObject*)PyObjCObject_GetBlock(self);
		if (v != NULL) {
			Py_INCREF(v);
			return v;
		}
	}
	Py_INCREF(Py_None);
	return Py_None;
}

static int
obj_set_blocksignature(PyObject* self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
	if (!PyObjCObject_IsBlock(self)) {
		PyErr_SetString(PyExc_TypeError, "You can only change this value on blocks");
		return  -1;
	}

	if (newVal != NULL) {
		if (!PyObjCMethodSignature_Check(newVal)) {
			PyErr_SetString(PyExc_TypeError, "New value must be a method signature");
			return -1;
		}
	}

	PyObject* v = (PyObject*)PyObjCObject_GetBlock(self);
	if (v != NULL) {
		Py_DECREF(v);
	}


	Py_XINCREF(newVal);
	PyObjCObject_SET_BLOCK(self, (PyObjCMethodSignature*)newVal);
	return 0;
}


static PyGetSetDef obj_getset[] = {
	{
		"pyobjc_ISA",
		objc_get_real_class,
		NULL,
		objc_get_real_class_doc,
		0
	},
	{
		"pyobjc_instanceMethods",
		obj_get_instanceMethods,
		NULL,
		obj_get_instanceMethods_doc,
		0
	},
	{
		"__block_signature__",
		obj_get_blocksignature,
		obj_set_blocksignature,
		"Call signature for a block, or None",
		0
	},
	{ 0, 0, 0, 0, 0 }
};

/*
 * We don't support pickling of Objective-C objects at the moment. The new
 * version 2 of the pickle protocol has a default pickle method for new-style
 * classes that doesn't work for us (it will write incomplete values to the
 * pickle). This method forces a failure during pickling.
 */
static PyObject*
meth_reduce(PyObject* self __attribute__((__unused__)))
{
	PyErr_SetString(PyExc_TypeError,
		"Cannot pickle Objective-C objects");
	return NULL;
}

static PyObject*
as_cobject(PyObject* self)
{
	if (PyObjCObject_GetObject(self) == nil) {
		Py_INCREF(Py_None);
		return Py_None;
	}
	return PyCObject_FromVoidPtr(PyObjCObject_GetObject(self), NULL);
}


static PyMethodDef obj_methods[] = {
	{
		"__reduce__",
		(PyCFunction)meth_reduce,
		METH_NOARGS,
		"Used for pickling"
	},
	{
		"__cobject__",
		(PyCFunction)as_cobject,
		METH_NOARGS,
		"Return a CObject representing this object"
	},
	{
		NULL,
		NULL,
		0,
		NULL
	}
};


PyObjCClassObject PyObjCObject_Type = {
   {
     {
	PyObject_HEAD_INIT(&PyObjCClass_Type)
	0,					/* ob_size */
	"objc_object",				/* tp_name */
	sizeof(PyObjCObject),			/* tp_basicsize */
	0,					/* tp_itemsize */
	/* methods */
	object_dealloc,		 		/* tp_dealloc */
	0,					/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	0,					/* tp_compare */
	object_repr,				/* tp_repr */
	0,					/* tp_as_number */
	0,					/* tp_as_sequence */
	0,		       			/* tp_as_mapping */
	0,					/* tp_hash */
	0,					/* tp_call */
	0,					/* tp_str */
	object_getattro,			/* tp_getattro */
	object_setattro,			/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT 
		| Py_TPFLAGS_BASETYPE,          /* tp_flags */
 	0,					/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	obj_methods,				/* tp_methods */
	0,					/* tp_members */
	obj_getset,				/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	PyType_GenericAlloc,			/* tp_alloc */
	object_new,				/* tp_new */
	0,		        		/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0, 					/* tp_subclasses */
	0,					/* tp_weaklist */
	(destructor)object_del			/* tp_del */
#if PY_VERSION_HEX >= 0x02060000
	, 0                                     /* tp_version_tag */
#endif

     },
     { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
#if PY_VERSION_HEX >= 0x02050000
       , 0
#endif
     }, /* as_number */
     { 0, 0, 0 },			/* as_mapping */
     { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },	/* as_sequence */
     { 0, 0, 0, 0 
#if PY_VERSION_HEX >= 0x02060000
	 , 0, 0
#endif
     },			/* as_buffer */
     0,					/* name */
     0,					/* slots */
   }, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
};

/*
 *  Allocate a proxy object for use during the call of __del__,
 *  this isn't a full-featured proxy object.
 */
PyObject* 
_PyObjCObject_NewDeallocHelper(id objc_object)
{
	PyObject* res;
	PyTypeObject* cls_type;

	assert(objc_object != nil);
	cls_type = (PyTypeObject*)PyObjCClass_New(object_getClass(objc_object));
	if (cls_type == NULL) {
		return NULL;
	}

	res = cls_type->tp_alloc(cls_type, 0);
	Py_DECREF(cls_type);
	if (res == NULL) {
		return NULL;
	}

	PyObjCClass_CheckMethodList((PyObject*)res->ob_type, 1);
	
	((PyObjCObject*)res)->objc_object = objc_object;
	((PyObjCObject*)res)->flags = PyObjCObject_kDEALLOC_HELPER;
	return res;
}

void
_PyObjCObject_FreeDeallocHelper(PyObject* obj)
{
	if (obj->ob_refcnt != 1) {
		/* Someone revived this object. Objective-C doesn't like
		 * this at all, therefore warn the user about this and
		 * zero out the instance.
		 */
		char buf[256];
		snprintf(buf, sizeof(buf), 
			"revived Objective-C object of type %s. Object is zero-ed out.",
			obj->ob_type->tp_name);

		PyErr_Warn(PyObjCExc_ObjCRevivalWarning, buf);

		id objc_object = PyObjCObject_GetObject(obj);

		/* XXX: release the object */
		if (((PyObjCObject*)obj)->flags & PyObjCObject_kSHOULD_NOT_RELEASE) {
			/* pass */
		} else if (((PyObjCObject*)obj)->flags & PyObjCObject_kUNINITIALIZED) {
			/* pass */
		} else {
			CFRelease(objc_object);
		}

		PyObjC_UnregisterPythonProxy(
			objc_object, obj);
		((PyObjCObject*)obj)->objc_object = nil;

		Py_DECREF(obj);

		return;
	}
	Py_DECREF(obj);
}


PyObject* 
PyObjCObject_New(id objc_object, int flags, int retain)
{
	Class cls = object_getClass(objc_object);
	PyTypeObject* cls_type;
	PyObject*     res;

	res = PyObjC_FindPythonProxy(objc_object);
	if (res) return res;

	assert(objc_object != nil);

	cls_type = (PyTypeObject*)PyObjCClass_New(cls);
	if (cls_type == NULL) {
		return NULL;
	}

	res = cls_type->tp_alloc(cls_type, 0);
	Py_DECREF(cls_type);
	if (res == NULL) {
		return NULL;
	}

	if (cls_type->tp_basicsize == sizeof(PyObjCBlockObject)) {
		flags |= PyObjCObject_kBLOCK;
	}

	/* This should be in the tp_alloc for the new class, but 
	 * adding a tp_alloc to PyObjCClass_Type doesn't seem to help
	 */
	PyObjCClass_CheckMethodList((PyObject*)res->ob_type, 1);
	
	((PyObjCObject*)res)->objc_object = objc_object;
	((PyObjCObject*)res)->flags = flags;

	if (flags & PyObjCObject_kBLOCK) {
		((PyObjCBlockObject*)res)->signature = NULL;
        }

	if (retain) {
		if (strcmp(object_getClassName(objc_object), 
						"NSAutoreleasePool") != 0) {
			/* NSAutoreleasePool doesn't like retain */
			CFRetain(objc_object);
		}
	}

	/*
	 * Don't register if we use the default flags, other parts will do
	 * that if necessary. I don't like this, but don't want to pollute
	 * the interface of this function with yet another argument.
	 */
	if (flags != PyObjCObject_kDEFAULT) {
		PyObjC_RegisterPythonProxy(objc_object, res);
	}
	return res;
}

PyObject* 
PyObjCObject_FindSelector(PyObject* object, SEL selector)
{
	PyObject* meth;
	
	meth = PyObjCClass_FindSelector((PyObject*)object->ob_type, selector, NO);

	if (meth == NULL) {
		return NULL; 
	} else {
		return meth;
	}	
}

id
(PyObjCObject_GetObject)(PyObject* object)
{
	if (!PyObjCObject_Check(object)) {
		PyErr_Format(PyExc_TypeError,
			"'objc.objc_object' expected, got '%s'",
			object->ob_type->tp_name);
		
	}
	return PyObjCObject_GetObject(object);
}

void        
PyObjCObject_ClearObject(PyObject* object)
{
	if (!PyObjCObject_Check(object)) {
		PyErr_Format(PyExc_TypeError,
			"'objc.objc_object' expected, got '%s'",
			object->ob_type->tp_name);
		
	}
	PyObjC_UnregisterPythonProxy(
			((PyObjCObject*)object)->objc_object, object);
	((PyObjCObject*)object)->objc_object = nil;
}
