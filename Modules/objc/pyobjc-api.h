#ifndef PyObjC_API_H
#define PyObjC_API_H

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
 * $Id: pyobjc-api.h,v 1.34 2004/05/21 20:44:31 ronaldoussoren Exp $
 */

#include <Python.h>
#include <objc/objc.h>

#import <Foundation/NSException.h>

#if PY_VERSION_HEX < 0x020300b0 

#ifndef PyGILState_Ensure

typedef int PyGILState_STATE;

#define PyGILState_Ensure(void)  (0)
static inline void PyGILState_Release(
		PyGILState_STATE state __attribute__((__unused__))) 
{
	/* EMPTY */
}

#endif

/* threading support */
#define PyObjC_DURING \
		NS_DURING

#define PyObjC_HANDLER NS_HANDLER

#define PyObjC_ENDHANDLER \
		NS_ENDHANDLER \

#define PyObjC_BEGIN_WITH_GIL \
	{ \
		PyGILState_STATE _GILState; \
		_GILState = PyGILState_Ensure(); 

#define PyObjC_GIL_FORWARD_EXC() \
		do { \
            PyObjCErr_ToObjCWithGILState(&_GILState); \
		} while (0)


#define PyObjC_GIL_RETURN(val) \
		do { \
			PyGILState_Release(_GILState); \
			return (val); \
		} while (0)

#define PyObjC_GIL_RETURNVOID \
		do { \
			PyGILState_Release(_GILState); \
			return; \
		} while (0)


#define PyObjC_END_WITH_GIL \
		PyGILState_Release(_GILState); \
	}


#else /* Python 2.3 and later */

/* threading support */
#define PyObjC_DURING \
		Py_BEGIN_ALLOW_THREADS \
		NS_DURING

#define PyObjC_HANDLER NS_HANDLER

#define PyObjC_ENDHANDLER \
		NS_ENDHANDLER \
		Py_END_ALLOW_THREADS

#define PyObjC_BEGIN_WITH_GIL \
	{ \
		PyGILState_STATE _GILState; \
		_GILState = PyGILState_Ensure(); 

#define PyObjC_GIL_FORWARD_EXC() \
		do { \
            PyObjCErr_ToObjCWithGILState(&_GILState); \
		} while (0)


#define PyObjC_GIL_RETURN(val) \
		do { \
			PyGILState_Release(_GILState); \
			return (val); \
		} while (0)

#define PyObjC_GIL_RETURNVOID \
		do { \
			PyGILState_Release(_GILState); \
			return; \
		} while (0)


#define PyObjC_END_WITH_GIL \
		PyGILState_Release(_GILState); \
	}

#endif




#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>

/* On 10.1 there are no defines for the OS version. */
#ifndef MAC_OS_X_VERSION_10_1
#define MAC_OS_X_VERSION_10_1 1010
#define MAC_OS_X_VERSION_MAX_ALLOWED MAC_OS_X_VERSION_10_1
#define PyObjC_COMPILING_ON_MACOSX_10_1
#endif

#ifndef MAC_OS_X_VERSION_10_2
#define MAC_OS_X_VERSION_10_2 1020
#endif


#else /* RUNTIME_GNU */

#ifndef objc_msgSendSuper
#  define objc_msgSendSuper(super, op, args...) \
	((super)->self == NULL                           \
	 	? 0                                      \
		: (                                      \
			class_get_instance_method(       \
				(super)->class, (op)     \
			)->method_imp)(                  \
				(super)->self,           \
				(op) ,##args))

#  define objc_msgSendSuper_stret(resultptr, super, op, args...) \
	do { \
		typedef __typeof__(*resultptr)(*STRET_IMP)(id, SEL, ...); \
\
		if ((super)->self) { \
			STRET_IMP _stretfunc_ = (STRET_IMP)class_get_instance_method( \
					(super)->class, (op));	\
			*(resultptr) = _stretfunc_((super)->self,(op) ,##args);\
		} \
	} while(0)

#endif /* objc_msgSendSuper */

#endif	/* RUNTIME_GNU */

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
 * - Version 3 adds another argument to PyObjC_CallPython
 * - Version 4 adds PyObjCErr_ToObjCGILState
 * - Version 4.1 adds PyObjCRT_AlignOfType and PyObjCRT_SizeOfType
 *         (PyObjC_SizeOfType is now deprecated)
 * - Version 4.2 adds PyObjCRT_SELName
 * - Version 4.3 adds PyObjCRT_SimplifySignature
 * - Version 4.4 adds PyObjC_FreeCArray, PyObjC_PythonToCArray and
 *   		PyObjC_CArrayToPython
 * - Version 5 modifies the signature for PyObjC_RegisterMethodMapping,
 *	PyObjC_RegisterSignatureMapping and PyObjCUnsupportedMethod_IMP,
 *      adds PyObjC_RegisterStructType and removes PyObjC_CallPython
 * - Version 6 adds PyObjCIMP_Type, PyObjCIMP_GetIMP and PyObjCIMP_GetSelector
 * - Version 7 adds PyObjCErr_AsExc, PyGILState_Ensure
 * - Version 8 adds PyObjCObject_IsUninitialized,
        removes PyObjCSelector_IsInitializer
 * - Version 9 (???)
 * - Version 10 changes the signature of PyObjCRT_SimplifySignature
 */
#define PYOBJC_API_VERSION 10

#define PYOBJC_API_NAME "__C_API__"

/* 
 * Only add items to the end of this list!
 */
typedef int (RegisterMethodMappingFunctionType)(
			Class, 
			SEL, 
			PyObject *(*)(PyObject*, PyObject*, PyObject*),
			void (*)(void*, void*, void**, void*));

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
			void (*)(void*, void*, void**, void*));

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

	void (*unsupported_method_imp)(void*, void*, void**, void*);
	PyObject* (*unsupported_method_caller)(PyObject*, PyObject*, PyObject*);

	/* PyObjCErr_ToObjCWithGILState */
	void (*err_python_to_objc_gil)(PyGILState_STATE* state);

	/* PyObjCRT_AlignOfType */
	int (*alignof_type)(const char* typestr);

	/* PyObjCRT_SELName */
	const char* (*selname)(SEL sel);

	/* PyObjCRT_SimplifySignature */
	int (*simplify_sig)(char* signature, char* buf, size_t buflen);

	/* PyObjC_FreeCArray */
	void    (*free_c_array)(int,void*);

	/* PyObjC_PythonToCArray */
	int     (*py_to_c_array)(const char*, PyObject*, PyObject*, void**, int*);
	
	/* PyObjC_CArrayToPython */
	PyObject* (*c_array_to_py)(const char*, void*, int);

	/* PyObjC_RegisterStructType */
	PyObject* (*register_struct)(const char*, const char*, const char*, initproc, int, const char**);

	/* PyObjCIMP_Type */
	PyTypeObject* imp_type;

	/* PyObjCIMP_GetIMP */
	IMP  (*imp_get_imp)(PyObject*);

	/* PyObjCIMP_GetSelector */
	SEL  (*imp_get_sel)(PyObject*);

    /* PyObjCErr_AsExc */
    NSException* (*err_python_to_nsexception)(void);

    /* PyGILState_Ensure */
    PyGILState_STATE (*gilstate_ensure)(void);

    int (*obj_is_uninitialized)(PyObject*);
};


#ifndef PYOBJC_BUILD

#ifndef PYOBJC_METHOD_STUB_IMPL
static struct pyobjc_api*	PyObjC_API;
#endif /* PYOBJC_METHOD_STUB_IMPL */

#define PyObjCObject_Check(obj) PyObject_TypeCheck(obj, PyObjC_API->object_type)
#define PyObjCClass_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->class_type)
#define PyObjCSelector_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->select_type)
#define PyObjCIMP_Check(obj)  PyObject_TypeCheck(obj, PyObjC_API->imp_type)
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
#define PyObjCErr_ToObjCWithGILState       (PyObjC_API->err_python_to_objc_gil)
#define PyObjCErr_AsExc        (PyObjC_API->err_python_to_nsexception)
#define PyObjC_PythonToObjC    (PyObjC_API->py_to_objc)
#define PyObjC_ObjCToPython    (PyObjC_API->objc_to_py)
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
#define PyObjCRT_SizeOfType      (PyObjC_API->sizeof_type)
#define PyObjCRT_AlignOfType	(PyObjC_API->alignof_type)
#define PyObjCRT_SELName	(PyObjC_API->selname)
#define PyObjCRT_SimplifySignature	(PyObjC_API->simplify_sig)
#define PyObjC_FreeCArray	(PyObjC_API->free_c_array)
#define PyObjC_PythonToCArray	(PyObjC_API->py_to_c_array)
#define PyObjC_CArrayToPython	(PyObjC_API->c_array_to_py)
#define PyObjC_RegisterStructType   (PyObjC_API->register_struct)
#define PyObjCIMP_GetIMP   (PyObjC_API->imp_get_imp)
#define PyObjCIMP_GetSelector   (PyObjC_API->imp_get_sel)
#define PyObjCObject_IsUninitialized (PyObjC_API->obj_is_uninitialized)


/* XXX: Check if we can use the following function in the bridge itself,
 * if so: move these to a seperate C file. These are inline to avoid warnings
 * and code-bloat for files that don't use these functions.
 */

static inline int 
PyObjCObject_Convert(PyObject* object, void* pvar)
{
	id* pid = (id*)pvar;

	*pid = PyObjC_PythonToId(object);
			        
	if (PyErr_Occurred()) {
	    return 0;
        } 
	return 1;
}


static inline int 
PyObjC_ConvertBOOL(PyObject* object, void* pvar)
{
    BOOL* pbool = (BOOL*)pvar;

    if (PyObject_IsTrue(object)) {
        *pbool = YES;
    } else {
        *pbool = NO;
    }

    return 1;
}

static inline int 
PyObjC_ConvertChar(PyObject* object, void* pvar)
{
    char* pchar = (char*)pvar;

    if (!PyString_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expecting string of len 1");
        return 0;
    }

    if (PyString_Size(object) != 1) {
        PyErr_SetString(PyExc_TypeError, "Expecting string of len 1");
        return 0;
    }

    *pchar = *PyString_AsString(object);
    return 1;
}

static inline int 
PyObjCSelector_Convert(PyObject* object, void* pvar)
{ 
    int r;

    if (object == Py_None) {
        *(SEL*)pvar = NULL;
        return 1;
    }
    if (PyObjCSelector_Check(object)) {
        *(SEL*)pvar = PyObjCSelector_GetSelector(object);
        return 1;
    }
    if (!PyString_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expected string");
        return 0;
    }

    r = PyObjC_PythonToObjC(@encode(SEL), object, pvar);
    if (r == -1) {
	    return 0;
    }	 
    return 1;
}

static inline int 
PyObjCClass_Convert(PyObject* object, void* pvar)
{
    if (!PyObjCClass_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expected objective-C class");
        return 0;
    }

    *(Class*)pvar = PyObjCClass_GetClass(object);
    if (*(Class*)pvar == NULL) return 0;
    return 1;
}



#ifndef PYOBJC_METHOD_STUB_IMPL

static int
PyObjC_ImportAPI(PyObject* calling_module)
{
	PyObject* m;
	PyObject* d;
	PyObject* api_obj;
	PyObject* name = PyString_FromString("_objc");
	
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
#endif /*  PyObjC_API_H */
