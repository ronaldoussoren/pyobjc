#ifndef OBJC_MODHELPER_H
#define OBJC_MODHELPER_H

/*
 * Use this in helper modules for the objc package, and in wrappers
 * for functions that deal with objective-C objects/classes
 * 
 * This header defines some utility wrappers for importing and using 
 * the objective-C module.
 *
 * NOTES:
 * - I (ronald) access the core pyobj in such a 'strange' way to avoid
 *   linking with that module. 
 * - This interface is in development, the the API will probably change in
 *   incompatible ways.
 *
 * $Id: pyobjc-api.h,v 1.12 2003/05/11 14:11:14 ronaldoussoren Exp $
 */

#include <Python.h>
#include <objc/objc.h>

#import <Foundation/NSException.h>

#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>

/* On 10.1 there are no defines for the OS version. */
#ifndef MAC_OS_X_VERSION_10_1
#define MAC_OS_X_VERSION_10_1 1010
#define MAC_OS_X_VERSION_MAX_ALLOWED MAC_OS_X_VERSION_10_1
#endif

#ifndef MAC_OS_X_VERSION_10_2
#define MAC_OS_X_VERSION_10_2 1020
#endif

#endif

/* Earlier versions of Python don't define PyDoc_STRVAR */
#ifndef PyDoc_STR
#define PyDoc_VAR(name)         static char name[]
#define PyDoc_STR(str)          (str)
#define PyDoc_STRVAR(name, str) PyDoc_VAR(name) = PyDoc_STR(str)
#endif

#define PYOBJC_API_VERSION -1
#define PYOBJC_API_NAME "__C_API__"

/* 
 * Only add items to the end of this list!
 */
typedef int (RegisterMethodMappingFunctionType)(
			Class, 
			SEL, 
			PyObject *(*)(PyObject*, PyObject*, PyObject*),
			IMP);

struct pyobjc_api {
	int	      api_version;	/* API version */
	int	      struct_len;	/* Length of this struct */
	PyTypeObject* class_type;	/* PyObjCClass_Type    */
	PyTypeObject* object_type;	/* PyObjCObject_Type   */
	PyTypeObject* select_type;	/* ObjCSelector_Type */

	/* ObjC_RegisterMethodMapping */
	RegisterMethodMappingFunctionType *register_method_mapping;

	/* ObjC_RegisterSignatureMapping */
	int (*register_signature_mapping)(
			char*,
			PyObject *(*)(PyObject*, PyObject*, PyObject*),
			IMP);

	/* PyObjCObject_GetObject */
	id (*obj_get_object)(PyObject*);

	/* PyObjCObject_ClearObject */
	void (*obj_clear_object)(PyObject*);

	/* PyObjCClass_GetClass */
	Class (*cls_get_class)(PyObject*);

	/* PyObjCClass_New */
	PyObject* (*cls_to_python)(Class cls);

	/* ObjC_PythonToId */
	id (*python_to_id)(PyObject*);

	/* ObjC_IdToPython */
	PyObject* (*id_to_python)(id);

	/* ObjCErr_FromObjC */
	void (*err_objc_to_python)(NSException*);

	/* ObjCErr_ToObjC */
	void (*err_python_to_objc)(void);

	/* ObjC_PythonToObjC */
	int (*py_to_objc)(const char*, PyObject*, void*);

	/* ObjC_ObjCToPython */
	PyObject* (*objc_to_py)(const char*, void*);

	/* PyObjC_CallPython */
	PyObject* (*call_to_python)(id, SEL, PyObject*);

	/* ObjC_SizeOfType */
	int 	   (*sizeof_type)(const char*);

	/* ObjCSelector_GetClass */
	Class	   (*sel_get_class)(PyObject* sel);

	/* ObjCSelector_GetSelector */
	SEL	   (*sel_get_sel)(PyObject* sel);

	/* PyObjCBool_Check */
	int	   (*bool_check)(PyObject* obj);

	/* PyObjCBool_FromLong */
	PyObject*  (*bool_init)(long i);

	/* PyObjC_InitSuper */
	void	(*fill_super)(struct objc_super*, Class, id);

	/* PyObjC_InitSuperCls */
	void	(*fill_super_cls)(struct objc_super*, Class);
};


#ifndef PYOBJC_BUILD

#ifndef PYOBJC_METHOD_STUB_IMPL
static struct pyobjc_api*	ObjC_API;
#endif /* PYOBJC_METHOD_STUB_IMPL */

#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, ObjC_API->object_type)
#define PyObjCClass_Check(obj)  PyObject_TypeCheck(obj, ObjC_API->class_type)
#define ObjCSelector_Check(obj)  PyObject_TypeCheck(obj, ObjC_API->class_type)

#define PyObjCObject_GetObject (ObjC_API->obj_get_object)
#define PyObjCObject_ClearObject (ObjC_API->obj_clear_object)
#define PyObjCClass_GetClass   (ObjC_API->cls_get_class)
#define PyObjCClass_New 	     (ObjC_API->cls_to_python)
#define ObjCSelector_GetClass (ObjC_API->sel_get_class)
#define ObjCSelector_GetSelector (ObjC_API->sel_get_sel)
#define ObjC_PythonToId      (ObjC_API->python_to_id)
#define ObjC_IdToPython      (ObjC_API->id_to_python)
#define ObjCErr_FromObjC     (ObjC_API->err_objc_to_python)
#define ObjCErr_ToObjC       (ObjC_API->err_python_to_objc)
#define ObjC_PythonToObjC    (ObjC_API->py_to_objc)
#define ObjC_ObjCToPython    (ObjC_API->objc_to_py)
#define PyObjC_CallPython	     (ObjC_API->call_to_python)
#define ObjC_RegisterMethodMapping (ObjC_API->register_method_mapping)
#define ObjC_RegisterSignatureMapping (ObjC_API->register_signature_mapping)
#define ObjC_SizeOfType      (ObjC_API->sizeof_type)
#define ObjC_PythonToObjC   (ObjC_API->py_to_objc)
#define ObjC_ObjCToPython   (ObjC_API->objc_to_py)
#define PyObjCBool_Check   (ObjC_API->bool_check)
#define PyObjCBool_FromLong   (ObjC_API->bool_init)
#define PyObjC_InitSuper	(ObjC_API->fill_super)
#define PyObjC_InitSuperCls	(ObjC_API->fill_super_cls)

#ifndef PYOBJC_METHOD_STUB_IMPL
static int
ObjC_ImportModule(PyObject* calling_module)
{
	PyObject* m;
	PyObject* d;
	PyObject* api_obj;
	PyObject* name = PyString_FromString("objc._objc");
	
	m = PyImport_Import(name);
	Py_DECREF(name);
	if (m == NULL) {
		return -1;
	}

	d = PyModule_GetDict(m);
	if (d == NULL) {
		PyErr_SetString(PyExc_RuntimeError, 
			"No dict in objc module");
		return -1;
	}

	api_obj = PyDict_GetItemString(d, PYOBJC_API_NAME);
	if (api_obj == NULL) {
		PyErr_SetString(PyExc_RuntimeError, 
			"No C_API in objc module");
		return -1;
	}
	ObjC_API = PyCObject_AsVoidPtr(api_obj);
	if (ObjC_API == NULL) return 0;
	if (ObjC_API->api_version != PYOBJC_API_VERSION) return 0;

	Py_INCREF(api_obj);

	/* Current pyobjc implementation doesn't allow deregistering 
	 * information, avoid unloading of users of the C-API.
	 * (Yes this is ugle, patches to fix this situation are apriciated)
	 */
	Py_INCREF(calling_module);

	return 0;
}
#endif /* PYOBJC_METHOD_STUB_IMPL */

#else /* PyObjC_BUILD */

extern struct pyobjc_api	objc_api;

#endif /* !PYOBJC_BUILD */
#endif /*  OBJC_MODHELPER_H */
