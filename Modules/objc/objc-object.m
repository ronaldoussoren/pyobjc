/*
 * Implementation of objective-C object wrapper
 */
#include "pyobjc.h"

#include <stddef.h>

#include <objc/Object.h>



/*
 * Basic freelist. 
 * - to delete an object: obj_freelist[obj_freelist_top++] = OBJ
 * - to create an object: OBJ = obj_freelist[--obj_freelist_top];
 */
#if 0
#define FREELIST_SIZE 1024

static PyObject* obj_freelist[FREELIST_SIZE];
static int obj_freelist_top = 0;
#endif


static NSMapTable* proxy_dict = NULL;

static PyObject* 
find_existing_proxy(id objc_obj)
{
	PyObject* v;

	if (proxy_dict == NULL) return NULL;

	v = NSMapGet(proxy_dict, objc_obj);
	Py_XINCREF(v);
	return v;
}

static void 
unregister_proxy(id objc_obj)
{
	if (proxy_dict == NULL) return;
	if (objc_obj == nil) return;

	NSMapRemove(proxy_dict, objc_obj);
}

static int
register_proxy(PyObject* proxy_obj) 
{
	id objc_obj;

	if (PyObjCObject_Check(proxy_obj)) {
		objc_obj = PyObjCObject_GetObject(proxy_obj);
	} else if (PyObjCClass_Check(proxy_obj)) {
		objc_obj = PyObjCClass_GetClass(proxy_obj);
	} else if (PyObjCUnicode_Check(proxy_obj)) {
		objc_obj = PyObjCUnicode_Extract(proxy_obj);
	} else {
		PyErr_SetString(PyExc_TypeError, 
			"bad argument for register_proxy");
		return -1;
	}
	assert(objc_obj != nil);

	if (proxy_dict == NULL)  {
		proxy_dict =  NSCreateMapTable(
			PyObjCUtil_PointerKeyCallBacks,
			PyObjCUtil_PointerValueCallBacks, 
			500);

		if (proxy_dict == NULL) {
			PyErr_SetString(PyExc_RuntimeError,
					"Cannot create NSMapTable");
			return -1;
		}
	}


	NSMapInsert(proxy_dict, objc_obj, proxy_obj);

	return 0;
}



static PyObject*
object_new(
	PyTypeObject*  type __attribute__((__unused__)),
	PyObject* args __attribute__((__unused__)), 
	PyObject* kwds __attribute__((__unused__)))
{
	PyErr_SetString(PyExc_TypeError, 
		"Use class methods to instantiate new Objective-C objects");
	return NULL;
}

static PyObject*
object_repr(PyObjCObject* self)
{
	char buffer[256];
	PyObject* res;

	if ((self->flags & PyObjCObject_kUNINITIALIZED) == 0 && !PyObjCObject_IsClassic(self)) {
		/* Try to call the method 'description', which is the ObjC
		 * equivalent of __repr__. If that fails we'll fall back to
		 * the default repr.
		 * Don't call 'description' for uninitialized objects, that
		 * crashes the interpreter for several classes.
		 */
		res = PyObject_CallMethod((PyObject*)self, "description", NULL);
		if (res == NULL) {
			PyErr_Clear();
		} else {
			return res;
		}
	}
	snprintf(buffer, sizeof(buffer), "<%s objective-c instance %p>",
		self->ob_type->tp_name, self->objc_object);

	return PyString_FromString(buffer);
}

#if PY_VERSION_HEX >= 0x020300A2
static void
object_del(PyObject* obj __attribute__((__unused__)))
{
	/* Dummy function, we do not want the default implementation */
}
#endif


static void
object_dealloc(PyObject* obj)
{
	/* XXX: This should not be necessary, but if we don't do this we
	 * sometimes loose exception information...
	 */
	PyObject* ptype, *pvalue, *ptraceback;
	PyErr_Fetch(&ptype, &pvalue, &ptraceback);

	if (PyObjCObject_GetFlags(obj) != PyObjCObject_kDEALLOC_HELPER 
			&& PyObjCObject_GetObject(obj) != nil) {
		/* Release the proxied object, we don't have to do this when
		 * there is no proxied object!
		 */
		unregister_proxy(PyObjCObject_GetObject(obj));


		/* If the object is not yet initialized we try to initialize 
		 * it before releasing the reference. This is necessary 
		 * because of a misfeature of MacOS X: 
		 * [[NSTextView alloc] release] crashes (at least upto 10.2)
		 * and this is not a bug according to Apple.
		 */
		if (PyObjCObject_IsClassic(obj)) {
			/* pass */

		} else if (((PyObjCObject*)obj)->flags 
				& PyObjCObject_kUNINITIALIZED) {
			/* Freeing of an unitialized object, just leak because 
			 * there is no reliable manner to free such objects.
			 *
			 * - [obj release] doesn't work because some classes 
			 *   cause crashes for unitialized objects
			 * - [[obj init] release] also doesn't work because 
			 *   not all classes implement -init
			 * - [obj dealloc] also doesn't work for class 
			 *   clusters like NSArray.
			 */
			char buf[256];

			snprintf(buf, sizeof(buf), 
				"leaking an unitialized object of type %s",
				obj->ob_type->tp_name);
			PyErr_Warn(PyObjCExc_UnInitDeallocWarning, buf);
			((PyObjCObject*)obj)->objc_object = nil;
		} else {
			PyObjC_DURING
				[((PyObjCObject*)obj)->objc_object release];

			PyObjC_HANDLER
				NSLog(@"PyObjC: Exception during dealloc of proxy: %@",
					localException);

			PyObjC_ENDHANDLER
			((PyObjCObject*)obj)->objc_object = nil;
		}
	}

#ifdef FREELIST_SIZE
	/* Push self onto the freelist */
	if (obj_freelist_top == FREELIST_SIZE) {
		obj->ob_type->tp_free(obj);
	} else {
		obj_freelist[obj_freelist_top++] = obj;
		obj->ob_refcnt = 0xDEADBEEF;
	}
#else
	obj->ob_type->tp_free(obj);
#endif

	PyErr_Restore(ptype, pvalue, ptraceback);
}


static inline PyObject*
_type_lookup(PyTypeObject* tp, PyObject* name)
{
	int i, n;
	PyObject *mro, *base, *dict;
	PyObject *descr = NULL;

	/* Look in tp_dict of types in MRO */
	mro = tp->tp_mro;
	assert(mro != NULL);
	assert(PyTuple_Check(mro));
	n = PyTuple_GET_SIZE(mro);
	for (i = 0; i < n; i++) {
		base = PyTuple_GET_ITEM(mro, i);

		if (PyClass_Check(base)) {
			dict = ((PyClassObject*)base)->cl_dict;
		} else {
			assert(PyType_Check(base));
			if (PyObjCClass_Check(base)) {
				PyObjCClass_CheckMethodList(base, 0);
			}

			dict = ((PyTypeObject *)base)->tp_dict;
		}
		assert(dict && PyDict_Check(dict));
		descr = PyDict_GetItem(dict, name);
		if (descr != NULL) {
			break;
		}
	}

	return descr;
}

static PyObject** _get_dictptr(PyObject* obj)
{
	int dictoffset;
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
	PyTypeObject *tp;
	PyObject *descr = NULL;
	PyObject *res = NULL;
	descrgetfunc f;
	PyObject **dictptr;
	char*      namestr;
	Class obj_class;
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
	else
		Py_INCREF(name);


	namestr = PyString_AS_STRING(name);

	/* Special hack for KVO on MacOS X, when an object is observed it's 
	 * ISA is changed by the runtime. We change the python type as well.
	 */
	obj_inst = PyObjCObject_GetObject(obj);
	if (obj_inst == nil) {
		PyErr_Format(PyExc_AttributeError,
		     "cannot access attribute '%.400s' of NIL '%.50s' object",
		     PyString_AS_STRING(name),
		     obj->ob_type->tp_name);
		goto done;
	}


	obj_class = GETISA(obj_inst);
	tp = (PyTypeObject*)PyObjCClass_New(obj_class);

	descr = NULL;
	if (tp != obj->ob_type) {
		/* Workaround for KVO implementation feature */
		PyObject* dict;

		if (tp->tp_dict == NULL) {
			if (PyType_Ready(tp) < 0)
				goto done;
		}

		PyObjCClass_CheckMethodList((PyObject*)tp, 0);
		dict = tp->tp_dict;

		assert(dict && PyDict_Check(dict));
		descr = PyDict_GetItem(dict, name);
	}
	Py_DECREF(tp);

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
			/* TODO: bind self */	
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
	int res = -1;
	


	if (!PyString_Check(name)){
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
	}
	else
		Py_INCREF(name);

	if (PyObjCObject_GetObject(obj) == nil) {
		PyErr_Format(PyExc_AttributeError,
		     "Cannot set '%s.400s' on NIL '%.50s' object",
		     PyString_AS_STRING(name),
		     tp->tp_name);
		goto done;
	}

	if (tp->tp_dict == NULL) {
		if (PyType_Ready(tp) < 0)
			goto done;
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
			if (dict == NULL)
				goto done;
			
			*dictptr = dict;
		}
		if (dict != NULL) {
			if (value == NULL)
				res = PyDict_DelItem(dict, name);
			else
				res = PyDict_SetItem(dict, name, value);
			if (res < 0 && PyErr_ExceptionMatches(PyExc_KeyError))
				PyErr_SetObject(PyExc_AttributeError, name);
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
		goto done;
	}

	PyErr_Format(PyExc_AttributeError,
		     "'%.50s' object attribute '%.400s' is read-only",
		     tp->tp_name, PyString_AS_STRING(name));
  done:

#if 0
	/* XXX: This would introduce some form of support for KeyValueObserving
	 * but, I'm not sure if this is the right approach. If this is, this 
	 * code needs more work: the name must be transformed to 
	 * a KeyValueCoding key (e.g. '_name' -> 'name')
	 */

#if defined(MACOSX) && MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
	/* KeyValueObserving support. If an attribute is changed by assignment,
	 * send out the notification.
	 */
	if (!PyErr_Occurred()) {
		id key = PyObjC_PythonToId(name);
		if (key == NULL && PyErr_Occurred()) {
			/* Cannot convert the name, ignore this */
			PyErr_Clear();
		} else {
			[PyObjCObject_GetObject(obj) didChangeValueForKey:key];
		}
	}
#endif

#endif

	Py_DECREF(name);
	return res;
}

#if 0 /* No longer used */
PyDoc_STRVAR(obj_get_classMethods_doc,
"The attributes of this field are the class methods of this object. This can\n"
"be used to force access to a class method."
);
static PyObject*
obj_get_classMethods(PyObjCObject* self, void* closure __attribute__((__unused__)))
{
	return ObjCMethodAccessor_New((PyObject*)self, 1);
}
#endif

PyDoc_STRVAR(objc_get_real_class_doc, "Return the current ISA of the object");
static PyObject* objc_get_real_class(PyObject* self, void* closure __attribute__((__unused__)))
{
	id obj_object;
	PyObject* ret;
	obj_object = PyObjCObject_GetObject(self);
	assert(obj_object != nil);
	ret = PyObjCClass_New(GETISA(obj_object));
	if (ret != (PyObject*)self->ob_type) {
		/* XXX doesn't this leak a reference to the original ob_type? */
		self->ob_type = (PyTypeObject*)ret;
		Py_INCREF(ret);
	}
	return ret;
}

PyDoc_STRVAR(obj_get_instanceMethods_doc,
"The attributes of this field are the instance methods of this object. This\n"
"can be used to force access to a class method."
);
static PyObject*
obj_get_instanceMethods(PyObjCObject* self, void* closure __attribute__((__unused__)))
{
	return ObjCMethodAccessor_New((PyObject*)self, 0);
}

static PyGetSetDef obj_getset[] = {
#if 0
	{
		"pyobjc_classMethods",
		(getter)obj_get_classMethods,
		NULL,
		obj_get_classMethods_doc,
		0
	},
#endif
	{
		"pyobjc_ISA",
		(getter)objc_get_real_class,
		NULL,
		objc_get_real_class_doc,
		0
	},
	{
		"pyobjc_instanceMethods",
		(getter)obj_get_instanceMethods,
		NULL,
		obj_get_instanceMethods_doc,
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

static PyMethodDef obj_methods[] = {
	{
		"__reduce__",
		(PyCFunction)meth_reduce,
		METH_NOARGS,
		"Used for pickling"
	},
	{
		NULL,
		NULL,
		0,
		NULL
	}
};


PyObjCClassObject PyObjCObject_Type = {
#ifdef PyObjC_CLASS_INFO_IN_TYPE
   {
     {
#else
   {
#endif
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
	(reprfunc)object_repr,			/* tp_repr */
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
	0					/* tp_weaklist */
#ifdef PyObjC_CLASS_INFO_IN_TYPE
	, (destructor)object_del,		/* tp_del */
     }
     ,
     { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, /* as_number */
     { 0, 0, 0 },			/* as_mapping */
     { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },	/* as_sequence */
     { 0, 0, 0, 0 },			/* as_buffer */
     0,					/* name */
     0,					/* slots */
   }
   , 0, 0, 0, 0, 0, 0, 0
#else
   }
#endif
};

/*
 *  Allocate a proxy object for use during the call of __del__,
 *  this isn't a full-featured proxy object.
 */
PyObject* 
_PyObjCObject_NewDeallocHelper(id objc_object)
{
	Class cls; 
	PyObject* res;
	PyTypeObject* cls_type;

	assert(objc_object != nil);
	cls = GETISA(objc_object);
	cls_type = (PyTypeObject*)PyObjCClass_New(cls);
	if (cls_type == NULL) {
		return NULL;
	}

#ifdef FREELIST_SIZE
	if (obj_freelist_top == 0) {
		res = cls_type->tp_alloc(cls_type, 0);
		if (res == NULL) {
			return NULL;
		}
	} else {
		res = obj_freelist[obj_freelist_top-1];
		obj_freelist_top -= 1;
		if (res->ob_refcnt != 0xDEADBEEF) abort();
		res->ob_refcnt = 1;
		res->ob_type = cls_type;
	}
#else
	res = cls_type->tp_alloc(cls_type, 0);
	if (res == NULL) {
		return NULL;
	}
#endif

	PyObjCClass_CheckMethodList((PyObject*)res->ob_type, 1);
	
	assert(objc_object != nil);
	((PyObjCObject*)res)->objc_object = objc_object;
	((PyObjCObject*)res)->flags = PyObjCObject_kDEALLOC_HELPER;
	return res;
}

/*
 * Free the object allocated using '_PyObCObject_NewDeallocHelper'. If the
 * object has a refcnt > 1 when calling this function, the object is 
 * promoted to a full proxy object. This should only happen when someone
 * revives the object, it is unclear whether the ObjC runtime will accept
 * reviveing.
 */
void
_PyObjCObject_FreeDeallocHelper(PyObject* obj)
{
	if (obj->ob_refcnt != 1) {
		/* Someone revived this object, hopefully 
		 * Objective-C can deal with this.
		 */
		id objc_object = PyObjCObject_GetObject(obj);

		Py_DECREF(obj);

		if (strcmp(GETISA(objc_object)->name, 
						"NSAutoreleasePool") != 0) {
			/* NSAutoreleasePool doesn't like retain */
			[objc_object retain];
		}

		if (register_proxy(obj) < 0) {
			NSLog(@"Couldn't register revived proxy object!");
		}
		return;
	}
	Py_DECREF(obj);
}


PyObject* 
PyObjCObject_New(id objc_object)
{
	Class cls = [objc_object class];
	PyTypeObject* cls_type;
	PyObject*     res;

	res = find_existing_proxy(objc_object);
	if (res) return res;

	if (objc_object == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	cls_type = (PyTypeObject*)PyObjCClass_New(cls);
	if (cls_type == NULL) {
		return NULL;
	}

#ifdef FREELIST_SIZE
	if (obj_freelist_top == 0) {
		res = cls_type->tp_alloc(cls_type, 0);
		if (res == NULL) {
			return NULL;
		}
	} else {
		res = obj_freelist[obj_freelist_top-1];
		obj_freelist_top -= 1;
		if (res->ob_refcnt != 0xDEADBEEF) abort();
		res->ob_refcnt = 1;
		res->ob_type = cls_type;
	}
#else
	res = cls_type->tp_alloc(cls_type, 0);
	if (res == NULL) {
		return NULL;
	}
#endif

	/* This should be in the tp_alloc for the new class, but 
	 * adding a tp_alloc to PyObjCClass_Type doesn't seem to help
	 */
	PyObjCClass_CheckMethodList((PyObject*)res->ob_type, 1);
	
	assert(objc_object != nil);
	((PyObjCObject*)res)->objc_object = objc_object;
	((PyObjCObject*)res)->flags = 0;



	if (strcmp(GETISA(objc_object)->name, "NSAutoreleasePool") != 0) {
		/* NSAutoreleasePool doesn't like retain */
		/* XXX: Technicly we shouldn't call retain either if this
		 * is an uninitialized object.
		 */
		[objc_object retain];
	}

	if (register_proxy(res) < 0) {
		Py_DECREF(res);
		return NULL;
	}

	return res;
}

PyObject* 
PyObjCObject_NewClassic(id objc_object)
{
	Class cls = [objc_object class];
	PyTypeObject* cls_type;
	PyObject*     res;

	res = find_existing_proxy(objc_object);
	if (res) return res;

	if (objc_object == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	cls_type = (PyTypeObject*)PyObjCClass_New(cls);
	if (cls_type == NULL) {
		return NULL;
	}

#ifdef FREELIST_SIZE
	if (obj_freelist_top == 0) {
		res = cls_type->tp_alloc(cls_type, 0);
		if (res == NULL) {
			return NULL;
		}
	} else {
		res = obj_freelist[obj_freelist_top-1];
		obj_freelist_top -= 1;
		if (res->ob_refcnt != 0xDEADBEEF) abort();
		res->ob_refcnt = 1;
		res->ob_type = cls_type;
	}
#else
	res = cls_type->tp_alloc(cls_type, 0);
	if (res == NULL) {
		return NULL;
	}
#endif

	/* This should be in the tp_alloc for the new class, but 
	 * adding a tp_alloc to PyObjCClass_Type doesn't seem to help
	 */
	PyObjCClass_CheckMethodList((PyObject*)res->ob_type, 1);
	
	assert(objc_object != nil);
	((PyObjCObject*)res)->objc_object = objc_object;
	((PyObjCObject*)res)->flags = PyObjCObject_kCLASSIC;

	if (register_proxy(res) < 0) {
		Py_DECREF(res);
		return NULL;
	}

	return res;
}

PyObject* 
PyObjCObject_NewUnitialized(id objc_object)
{
	Class cls = GETISA(objc_object);
	PyTypeObject* cls_type;
	PyObject*     res;


	res = find_existing_proxy(objc_object);
	if (res) return res;

	if (objc_object == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	cls_type = (PyTypeObject*)PyObjCClass_New(cls);
	if (cls_type == NULL) {
		return NULL;
	}

	res = cls_type->tp_alloc(cls_type, 0);
	if (res == NULL) {
		return NULL;
	}

	/* This should be in the tp_alloc for the new class, but 
	 * adding a tp_alloc to PyObjCClass_Type doesn't seem to help
	 */
	PyObjCClass_CheckMethodList((PyObject*)res->ob_type, 1);
	
	assert(objc_object != nil);
	((PyObjCObject*)res)->objc_object = objc_object;
	((PyObjCObject*)res)->flags = 0;

	if (register_proxy(res) < 0) {
		Py_DECREF(res);
		return NULL;
	}

	return res;
}

PyObject* 
PyObjCObject_FindSelector(PyObject* object, SEL selector)
{
	PyObject* meth;
	
	meth = PyObjCClass_FindSelector((PyObject*)object->ob_type, selector);

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
    if (object == NULL) abort();
	if (!PyObjCObject_Check(object)) {
		PyErr_Format(PyExc_TypeError,
			"'objc.objc_object' expected, got '%s'",
			object->ob_type->tp_name);
		
	}
	unregister_proxy(((PyObjCObject*)object)->objc_object);
	((PyObjCObject*)object)->objc_object = nil;
}
