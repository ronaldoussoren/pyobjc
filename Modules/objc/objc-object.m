/*
 * Implementation of objective-C object wrapper
 */
#include <Python.h>
#include "pyobjc.h"
#include "objc_support.h"
#include <stddef.h>
#include <objc/Object.h>

static NSMapTable* proxy_dict = NULL;

static PyObject* 
find_existing_proxy(id objc_obj)
{
	PyObject* v;

	if (proxy_dict == NULL) return NULL;

	v = NSMapGet(proxy_dict, objc_obj);
	if (v == NULL) {
		return NULL;
	}

	Py_INCREF(v);
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
		abort();
		objc_obj = PyObjCClass_GetClass(proxy_obj);
	} else if (PyObjCUnicode_Check(proxy_obj)) {
		abort();
		objc_obj = PyObjCUnicode_Extract(proxy_obj);
	} else {
		PyErr_SetString(PyExc_TypeError, 
			"bad argument for register_proxy");
		return -1;
	}

	if (proxy_dict == NULL)  {
		proxy_dict =  NSCreateMapTable(ObjC_PointerKeyCallBacks,
			ObjC_PointerValueCallBacks, 500);

		if (proxy_dict == NULL) return -1;
	}


	NSMapInsert(proxy_dict, objc_obj, proxy_obj);

	return 0;
}


static PyObject*
object_new(PyTypeObject*  type, PyObject* args, PyObject* kwds)
{
	PyErr_SetString(PyExc_TypeError, 
		"Use class methods to instantiate new Objective-C objects");
	return NULL;
}

static PyObject*
object_repr(PyObjCObject* self)
{
	char buffer[256];

	snprintf(buffer, sizeof(buffer), "<%s objective-c instance %p>",
		self->ob_type->tp_name, self->objc_object);

	return PyString_FromString(buffer);
}

static void
object_del(PyObject* obj)
{
	/* Dummy function, we do not want the default implementation */
}


static void
object_dealloc(PyObject* obj)
{
	unregister_proxy(PyObjCObject_GetObject(obj));

	/* If the object is not yet initialized we try to initialize it before
	 * releasing the reference. This is necessary because of a misfeature
	 * of MacOS X: [[NSTextView alloc] release] crashes (at least upto 10.2)
	 * and this is not a bug according to Apple.
	 */
	if (((PyObjCObject*)obj)->flags & PyObjCObject_kUNINITIALIZED) {
		/* Lets hope 'init' is always a valid initializer */
		NS_DURING
			[[((PyObjCObject*)obj)->objc_object init] release];
		NS_HANDLER
			NSLog(@"PyObjC: Exception during dealloc of proxy: %@",
				localException);
		NS_ENDHANDLER

	} else {
		NS_DURING
			[((PyObjCObject*)obj)->objc_object release];
		NS_HANDLER
			NSLog(@"PyObjC: Exception during dealloc of proxy: %@",
				localException);
		NS_ENDHANDLER
	}

	obj->ob_type->tp_free(obj);
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
		assert(PyType_Check(base));

		if (PyObjCClass_Check(base)) {
			PyObjCClass_CheckMethodList(base);
		}

		dict = ((PyTypeObject *)base)->tp_dict;
		assert(dict && PyDict_Check(dict));
		descr = PyDict_GetItem(dict, name);
		if (descr != NULL)
			break;
	}

	return descr;
}

static PyObject** _get_dictptr(PyObject* obj)
{
	int dictoffset = PyObjCClass_DictOffset((PyObject*)obj->ob_type);

	if (dictoffset == 0) return NULL;

	return (PyObject**)(((char*)PyObjCObject_GetObject(obj)) + dictoffset);
}

static PyObject *
object_getattro(PyObject *obj, PyObject *name)
{
	PyTypeObject *tp = obj->ob_type;
	PyObject *descr = NULL;
	PyObject *res = NULL;
	descrgetfunc f;
	long dictoffset;
	PyObject **dictptr;

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
			PyErr_SetString(PyExc_TypeError,
					"attribute name must be string");
			return NULL;
		}
	}
	else
		Py_INCREF(name);

	if (tp->tp_dict == NULL) {
		if (PyType_Ready(tp) < 0)
			goto done;
	}

	/* replace _PyType_Lookup */
	descr = _type_lookup(tp, name);

	f = NULL;
	if (descr != NULL &&
	    PyType_HasFeature(descr->ob_type, Py_TPFLAGS_HAVE_CLASS)) {
		f = descr->ob_type->tp_descr_get;
		if (f != NULL && PyDescr_IsData(descr)) {
			res = f(descr, obj, (PyObject *)obj->ob_type);
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
		res = f(descr, obj, (PyObject *)obj->ob_type);
		goto done;
	}

	if (descr != NULL) {
		Py_INCREF(descr);
		res = descr;
		goto done;
	}

	NS_DURING
		res = ObjCSelector_FindNative(obj, PyString_AS_STRING(name));
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		res = NULL;
	NS_ENDHANDLER

	if (res) goto done;

	PyErr_Format(PyExc_AttributeError,
		     "'%.50s' object has no attribute '%.400s'",
		     tp->tp_name, PyString_AS_STRING(name));
  done:
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
			PyErr_SetString(PyExc_TypeError,
					"attribute name must be string");
			return -1;
		}
	}
	else
		Py_INCREF(name);

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
	Py_DECREF(name);
	return res;
}

PyDoc_STRVAR(obj_get_classMethods_doc,
"The attributes of this field are the class methods of this object. This can\n"
"be used to force access to a class method."
);
static PyObject*
obj_get_classMethods(PyObjCObject* self, void* closure)
{
	return ObjCMethodAccessor_New((PyObject*)self, 1);
}

PyDoc_STRVAR(obj_get_instanceMethods_doc,
"The attributes of this field are the instance methods of this object. This\n"
"can be used to force access to a class method."
);
static PyObject*
obj_get_instanceMethods(PyObjCObject* self, void* closure)
{
	return ObjCMethodAccessor_New((PyObject*)self, 0);
}

static PyGetSetDef obj_getset[] = {
	{
		"pyobjc_classMethods",
		(getter)obj_get_classMethods,
		NULL,
		obj_get_classMethods_doc,
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

PyObjCClassObject PyObjCObject_Type = {{
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
	0,					/* tp_methods */
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
	0,					/* tp_free */
	0,					/* tp_is_gc */
	0,					/* tp_bases */
	0,					/* tp_mro */
	0,					/* tp_cache */
	0,					/* tp_subclasses */
	0,					/* tp_weaklist */
	(destructor)object_del				/* tp_del */
}, 0};



PyObject* 
PyObjCObject_New(id objc_object)
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
	//res = (PyObject*)PyObject_New(PyObjCObject, cls_type);
	if (res == NULL) {
		return NULL;
	}

	/* This should be in the tp_alloc for the new class, but 
	 * adding a tp_alloc to PyObjCClass_Type doesn't seem to help
	 */
	PyObjCClass_CheckMethodList((PyObject*)res->ob_type);
	
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
	PyObjCClass_CheckMethodList((PyObject*)res->ob_type);
	
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
		ObjCErr_Set(PyExc_TypeError,
			"objc.objc_object expected, got %s",
			object->ob_type->tp_name);
		
	}
	return PyObjCObject_GetObject(object);
}

void        
PyObjCObject_ClearObject(PyObject* object)
{
	if (!PyObjCObject_Check(object)) {
		ObjCErr_Set(PyExc_TypeError,
			"objc.objc_object expected, got %s",
			object->ob_type->tp_name);
		
	}
	unregister_proxy(((PyObjCObject*)object)->objc_object);
	((PyObjCObject*)object)->objc_object = nil;
}
