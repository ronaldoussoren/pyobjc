#ifndef OBJC_MODHELPER_H
#define OBJC_MODHELPER_H

/*
 * Use this in helper modules for the objc package, and in wrappers
 * for functions that deal with objective-C objects/classes
 * 
 * This header defines some utility wrappers for importing and using 
 * the core bridge. 
 *
 * This is the *only* header file that should be used to access 
 * functionality in the core bridge.
 *
 * $Id: pyobjc-api.h,v 1.17 2003/06/28 12:57:51 ronaldoussoren Exp $
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

/* Current API version, increase whenever:
 * - Semantics of current functions change
 * - Functions are removed
 * Do not increase when adding a new function, the struct_len field
 * can be used for detecting if a function has been added.
 *
 * HISTORY:
 * - Version 2.2 adds PyObjCUnsupportedMethod_IMP 
 *       and PyObjCUnsupportedMethod_Caller 
 * - Version 2.1 adds PyObjCPointerWrapper_Register 
 * - Version 2 adds an argument to PyObjC_InitSuper
 */
#define PYOBJC_API_VERSION 2

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
	size_t	      struct_len;	/* Length of this struct */
	PyTypeObject* class_type;	/* PyObjCClass_Type    */
	PyTypeObject* object_type;	/* PyObjCObject_Type   */
	PyTypeObject* select_type;	/* PyObjCSelector_Type */

	/* PyObjC_RegisterMethodMapping */
	RegisterMethodMappingFunctionType *register_method_mapping;

	/* PyObjC_RegisterSignatureMapping */
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

	/* PyObjC_PythonToId */
	id (*python_to_id)(PyObject*);

	/* PyObjC_IdToPython */
	PyObject* (*id_to_python)(id);

	/* PyObjCErr_FromObjC */
	void (*err_objc_to_python)(NSException*);

	/* PyObjCErr_ToObjC */
	void (*err_python_to_objc)(void);

	/* PyObjC_PythonToObjC */
	int (*py_to_objc)(const char*, PyObject*, void*);

	/* PyObjC_ObjCToPython */
	PyObject* (*objc_to_py)(const char*, void*);

	/* PyObjC_CallPython */
	PyObject* (*call_to_python)(id, SEL, PyObject*);

	/* PyObjC_SizeOfType */
	int 	   (*sizeof_type)(const char*);

	/* PyObjCSelector_GetClass */
	Class	   (*sel_get_class)(PyObject* sel);

	/* PyObjCSelector_GetSelector */
	SEL	   (*sel_get_sel)(PyObject* sel);

	/* PyObjCBool_Check */
	int	   (*bool_check)(PyObject* obj);

	/* PyObjCBool_FromLong */
	PyObject*  (*bool_init)(long i);

	/* PyObjC_InitSuper */ 	
	void	(*fill_super)(struct objc_super*, Class, id);

	/* PyObjC_InitSuperCls */
	void	(*fill_super_cls)(struct objc_super*, Class, Class);

	/* PyObjCPointerWrapper_Register */ 
	int  (*register_pointer_wrapper)(
		        const char*, PyObject* (*pythonify)(void*),
			int (*depythonify)(PyObject*, void*)
		);

	IMP  unsupported_method_imp;
	PyObject* (*unsupported_method_caller)(PyObject*, PyObject*, PyObject*);
};


#ifndef PYOBJC_BUILD

#ifndef PYOBJC_METHOD_STUB_IMPL
static struct pyobjc_api*	PyObjC_API;
#endif /* PYOBJC_METHOD_STUB_IMPL */

#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, PyObjC_API->object_type)
#define PyObjCClass_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->class_type)
#define PyObjCSelector_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->select_type)
#define PyObjCObject_GetObject (PyObjC_API->obj_get_object)
#define PyObjCObject_ClearObject (PyObjC_API->obj_clear_object)
#define PyObjCClass_GetClass   (PyObjC_API->cls_get_class)
#define PyObjCClass_New 	     (PyObjC_API->cls_to_python)
#define PyObjCSelector_GetClass (PyObjC_API->sel_get_class)
#define PyObjCSelector_GetSelector (PyObjC_API->sel_get_sel)
#define PyObjC_PythonToId      (PyObjC_API->python_to_id)
#define PyObjC_IdToPython      (PyObjC_API->id_to_python)
#define PyObjCErr_FromObjC     (PyObjC_API->err_objc_to_python)
#define PyObjCErr_ToObjC       (PyObjC_API->err_python_to_objc)
#define PyObjC_PythonToObjC    (PyObjC_API->py_to_objc)
#define PyObjC_ObjCToPython    (PyObjC_API->objc_to_py)
#define PyObjC_CallPython	     (PyObjC_API->call_to_python)
#define PyObjC_RegisterMethodMapping (PyObjC_API->register_method_mapping)
#define PyObjC_RegisterSignatureMapping (PyObjC_API->register_signature_mapping)
#define PyObjC_SizeOfType      (PyObjC_API->sizeof_type)
#define PyObjC_PythonToObjC   (PyObjC_API->py_to_objc)
#define PyObjC_ObjCToPython   (PyObjC_API->objc_to_py)
#define PyObjCBool_Check   (PyObjC_API->bool_check)
#define PyObjCBool_FromLong   (PyObjC_API->bool_init)
#define PyObjC_InitSuper	(PyObjC_API->fill_super)
#define PyObjC_InitSuperCls	(PyObjC_API->fill_super_cls)
#define PyObjCPointerWrapper_Register (PyObjC_API->register_pointer_wrapper)
#define PyObjCUnsupportedMethod_IMP (PyObjC_API->unsupported_method_imp)
#define PyObjCUnsupportedMethod_Caller (PyObjC_API->unsupported_method_caller)


static inline int PyObjCObject_Convert(PyObject* object, void* pvar)
{
	id* pid = (id*)pvar;

	*pid = PyObjC_PythonToId(object);
			        
	if (PyErr_Occurred()) {
	    return 0;
        } 
	return 1;
}


#ifndef PYOBJC_METHOD_STUB_IMPL
static int
PyObjC_ImportAPI(PyObject* calling_module)
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
	PyObjC_API = PyCObject_AsVoidPtr(api_obj);
	if (PyObjC_API == NULL) {
		return 0;
	}
	if (PyObjC_API->api_version != PYOBJC_API_VERSION) {
		PyErr_SetString(PyExc_RuntimeError,
			"Wrong version of PyObjC C API");
		return -1;
	}
	
	if (PyObjC_API->struct_len < sizeof(struct pyobjc_api)) {
		PyErr_SetString(PyExc_RuntimeError,
			"Wrong struct-size of PyObjC C API");
		return -1;
	}

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
