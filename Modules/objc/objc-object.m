/*
 * Implementation of objective-C object wrapper
 */
#include <Python.h>
#include "pyobjc.h"
#include "objc_support.h"
#include <stddef.h>
#include <objc/Object.h>

#import <Foundation/NSString.h> /*XXX*/

/*
 * We use weakreferences to make sure that every objective-C object has 
 * at most one python proxy. This allows users to use the 'is' operator
 * to check if two proxy instances refer to the same objective-C object.
 *
 */
#ifndef PyOBJC_UNIQUE_PROXY

#define find_existing_proxy(objc_obj) NULL
#define register_proxy(proxy_obj)  0

#else /* PyOBJC_UNIQUE_PROXY */

/*
 * There are two functions:
 * - register_proxy
 *   Add the proxy for an objective-C object to the weakref dictionary
 * - find_existing_proxy
 *   Find the existing proxy for an objective-C object
 *
 * 'unregister_proxy_func' is used to remove a proxy from the dictionary when
 * there are no more references to that proxy. Note that we use the 'self' 
 * object to pass the key that should be remove, that seems to be the easiest
 * (but ugly) method of creating a closure.
 */

static PyObject* proxy_dict = NULL;

struct unregister_data {
	PyObject* function;
	PyObject* key;
};

static PyObject* unregister_proxy_func(PyObject* self, PyObject* args)
{
	PyObject* weakref = NULL;
	struct unregister_data* data;


	if (!PyArg_ParseTuple(args, "O:unregister_proxy", &weakref)) {
		PyErr_BadInternalCall();
		return NULL;
	}

	data = PyCObject_AsVoidPtr(self);

	PyDict_DelItem(proxy_dict, data->key);
	if (PyErr_Occurred()) PyErr_Clear();
	Py_DECREF(data->function);
	Py_DECREF(data->key);
	Py_DECREF(self);
	free(data);

	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef unregister_proxy_method_def = {
	"unregister_proxy",
	unregister_proxy_func,
	METH_VARARGS|METH_KEYWORDS,
	NULL
};

static PyObject* 
find_existing_proxy(id objc_obj)
{
	PyObject* v;
	PyObject* key;

	if (proxy_dict == NULL) return NULL;

	key = PyInt_FromLong((long)objc_obj);
	v = PyDict_GetItem(proxy_dict, key);
	Py_DECREF(key); key = NULL;
	if (v == NULL) return NULL;

	v = PyWeakref_GetObject(v);
	if (v) {
		OC_CheckRevive(v);
		Py_INCREF(v);
	}

	return v;
}

static int
register_proxy(PyObject* proxy_obj) 
{
	id objc_obj;
	PyObject* v;
	PyObject* unregister_proxy;
	struct unregister_data* data;

	if (ObjCObject_Check(proxy_obj)) {
		objc_obj = ObjCObject_GetObject(proxy_obj);
	} else if (ObjCClass_Check(proxy_obj)) {
		objc_obj = ObjCClass_GetClass(proxy_obj);
	} else {
		PyErr_SetString(PyExc_TypeError, 
			"bad argument for register_proxy");
		return -1;
	}
		

	if (proxy_dict == NULL)  {
		proxy_dict = PyDict_New();
		if (proxy_dict == NULL) return -1;

	}

	data = malloc(sizeof(*data));
	data->key = PyInt_FromLong((long)objc_obj);
	data->function = NULL;


	unregister_proxy = PyCFunction_New(
		&unregister_proxy_method_def, PyCObject_FromVoidPtr(data, NULL));
	if (unregister_proxy == NULL) {
		Py_DECREF(proxy_dict);
		return -1;
	}
	data->function  = unregister_proxy;

	v = PyWeakref_NewProxy(proxy_obj, unregister_proxy);
	if (v == NULL) {
		return -1;
	}

	Py_INCREF(data->key);
	PyDict_SetItem(proxy_dict, data->key, v);
	if (PyErr_Occurred()) return -1;
	Py_DECREF(v); 

	return 0;
}

#endif /* PyOBJC_UNIQUE_PROXY */

int ObjC_RegisterClassProxy(Class cls, PyObject* classProxy)
{
	return register_proxy(classProxy);
}

static PyObject*
object_new(PyTypeObject*  type, PyObject* args, PyObject* kwds)
{
	PyErr_SetString(PyExc_TypeError, 
		"Use class methods to instantiate new Objective-C objects");
	return NULL;
}

static PyObject*
object_repr(ObjCObject* self)
{
	char buffer[256];

	snprintf(buffer, sizeof(buffer), "<%s objective-c instance %p>",
		self->ob_type->tp_name, self->objc_object);

	return PyString_FromString(buffer);
}

static void
object_dealloc(PyObject* obj)
{
	if (((ObjCObject*)obj)->weak_refs != NULL) {
		 PyObject_ClearWeakRefs(obj);
 	}
	[((ObjCObject*)obj)->objc_object release];
	obj->ob_type->tp_free(obj);
}

static PyObject*
object_getattro(PyObject* obj, PyObject* name)
{
	PyObject* result;

	ObjCClass_CheckMethodList((PyObject*)obj->ob_type);

	result = PyObject_GenericGetAttr(obj, name);
	if (result) return result;

	PyErr_Clear();
	NS_DURING
		result = ObjCSelector_FindNative(obj, PyString_AsString(name));
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}


PyTypeObject ObjCObject_Type = {
	PyObject_HEAD_INIT(&ObjCClass_Type)
	0,					/* ob_size */
	"objc_object",				/* tp_name */
	sizeof(ObjCObject),			/* tp_basicsize */
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
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE 
		| Py_TPFLAGS_HAVE_WEAKREFS, 	/* tp_flags */
 	0,					/* tp_doc */
 	0,					/* tp_traverse */
 	0,					/* tp_clear */
	0,					/* tp_richcompare */
	offsetof(ObjCObject, weak_refs),	/* tp_weaklistoffset */
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
	PyType_GenericAlloc,			/* tp_alloc */
	object_new,				/* tp_new */
	0,		        		/* tp_free */
};



PyObject* ObjCObject_New(id objc_object)
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

	cls_type = (PyTypeObject*)ObjCClass_New(cls);
	if (cls_type == NULL) {
		return NULL;
	}

	res = cls_type->tp_alloc(cls_type, 0);
	if (res == NULL) {
		return NULL;
	}

	/* This should be in the tp_alloc for the new class, but 
	 * adding a tp_alloc to ObjCClass_Type doesn't seem to help
	 */
	ObjCClass_CheckMethodList((PyObject*)res->ob_type);
	
	((ObjCObject*)res)->weak_refs = NULL;
	((ObjCObject*)res)->objc_object = objc_object;
	((ObjCObject*)res)->is_paired = 0;

	if (strcmp(GETISA(objc_object)->name, "NSAutoreleasePool") != 0) {
		/* NSAutoreleasePool doesn't like retain */
		[objc_object retain];
	}

	if (register_proxy(res) < 0) {
		Py_DECREF(res);
		return NULL;
	}

	return res;
}

PyObject* ObjCObject_FindSelector(PyObject* object, SEL selector)
{
	PyObject* meth;
	
	meth = ObjCClass_FindSelector((PyObject*)object->ob_type, selector);

	if (meth == NULL) {
		return NULL;
	} else {
		return meth;
	}	
}

id        (ObjCObject_GetObject)(PyObject* object)
{
	if (!ObjCObject_Check(object)) {
		ObjCErr_Set(PyExc_TypeError,
			"objc.objc_object expected, got %s",
			object->ob_type->tp_name);
		
	}
	return ObjCObject_GetObject(object);
}
