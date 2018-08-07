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
 * WARNING: this file is not part of the public interface of PyObjC and
 * might change or be removed without warning or regard for backward
 * compatibility.
 */

#include <objc/objc.h>

#import <Foundation/Foundation.h>

#include "pyobjc-compat.h"

#include <objc/objc-runtime.h>

/* Current API version, increase whenever:
 * - Semantics of current functions change
 * - Functions are removed
 *
 * Do not increase when adding a new function, the struct_len field
 * can be used for detecting if a function has been added.
 */
#define PYOBJC_API_VERSION 20

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
    int api_version; /* API version */
    size_t struct_len; /* Length of this struct */
    RegisterMethodMappingFunctionType *register_method_mapping;
    id (*obj_get_object)(PyObject*);
    Class (*cls_get_class)(PyObject*);
    id (*python_to_id)(PyObject*);
    PyObject* (*id_to_python)(id);
    void (*err_objc_to_python)(NSException*);
    int (*py_to_objc)(const char*, PyObject*, void*);
    PyObject* (*objc_to_py)(const char*, void*);
    Py_ssize_t (*sizeof_type)(const char*);
    Class (*sel_get_class)(PyObject* sel);
    SEL (*sel_get_sel)(PyObject* sel);
    void (*fill_super)(struct objc_super*, Class, id);
    void (*fill_super_cls)(struct objc_super*, Class, Class);
    int (*register_pointer_wrapper)(
            const char*, const char*, PyObject* (*pythonify)(void*),
            int (*depythonify)(PyObject*, void*)
        );
    void (*unsupported_method_imp)(void*, void*, void**, void*);
    PyObject* (*unsupported_method_caller)(PyObject*, PyObject*, PyObject*);
    void (*err_python_to_objc_gil)(PyGILState_STATE* state);
    int (*simplify_sig)(const char* signature, char* buf, size_t buflen);
    void (*free_c_array)(int,void*);
    int (*py_to_c_array)(BOOL, BOOL, const char*, PyObject*, void**, Py_ssize_t*, PyObject**);
    PyObject* (*c_array_to_py)(const char*, void*, Py_ssize_t);
    PyTypeObject* imp_type;
    IMP (*imp_get_imp)(PyObject*);
    SEL (*imp_get_sel)(PyObject*);
    PyObject* (*newtransient)(id objc_object, int* cookie);
    void (*releasetransient)(PyObject* proxy, int cookie);
    PyObject** pyobjc_null;
    int (*dep_c_array_count)(const char* type, Py_ssize_t count, BOOL strict, PyObject* value, void* datum);
    PyObject* (*varlistnew)(const char* tp, void* array);
    int (*pyobjcobject_convert)(PyObject*,void*);
    int (*register_id_alias)(const char*, const char*);
};

#ifndef PYOBJC_BUILD

#ifndef PYOBJC_METHOD_STUB_IMPL
static struct pyobjc_api* PyObjC_API;
#endif /* PYOBJC_METHOD_STUB_IMPL */

#define PyObjCIMP_Check(obj) PyObject_TypeCheck(obj, PyObjC_API->imp_type)
#define PyObjCObject_GetObject (PyObjC_API->obj_get_object)
#define PyObjCClass_GetClass (PyObjC_API->cls_get_class)
#define PyObjCSelector_GetClass (PyObjC_API->sel_get_class)
#define PyObjCSelector_GetSelector (PyObjC_API->sel_get_sel)
#define PyObjC_PythonToId (PyObjC_API->python_to_id)
#define PyObjC_IdToPython (PyObjC_API->id_to_python)
#define PyObjCErr_FromObjC (PyObjC_API->err_objc_to_python)
#define PyObjCErr_ToObjCWithGILState (PyObjC_API->err_python_to_objc_gil)
#define PyObjC_PythonToObjC (PyObjC_API->py_to_objc)
#define PyObjC_ObjCToPython (PyObjC_API->objc_to_py)
#define PyObjC_RegisterMethodMapping (PyObjC_API->register_method_mapping)
#define PyObjC_InitSuper (PyObjC_API->fill_super)
#define PyObjC_InitSuperCls (PyObjC_API->fill_super_cls)
#define PyObjCPointerWrapper_Register (PyObjC_API->register_pointer_wrapper)
#define PyObjCUnsupportedMethod_IMP (PyObjC_API->unsupported_method_imp)
#define PyObjCUnsupportedMethod_Caller (PyObjC_API->unsupported_method_caller)
#define PyObjCRT_SizeOfType (PyObjC_API->sizeof_type)
#define PyObjC_FreeCArray (PyObjC_API->free_c_array)
#define PyObjC_PythonToCArray (PyObjC_API->py_to_c_array)
#define PyObjC_CArrayToPython (PyObjC_API->c_array_to_py)
#define PyObjCIMP_GetIMP (PyObjC_API->imp_get_imp)
#define PyObjCIMP_GetSelector (PyObjC_API->imp_get_sel)
#define PyObjCObject_NewTransient (PyObjC_API->newtransient)
#define PyObjCObject_ReleaseTransient (PyObjC_API->releasetransient)
#define PyObjC_NULL (*(PyObjC_API->pyobjc_null))
#define PyObjC_DepythonifyCArray (PyObjC_API->dep_c_array_count)
#define PyObjC_VarList_New (PyObjC_API->varlistnew)
#define PyObjCObject_Convert (PyObjC_API->pyobjcobject_convert)
#define PyObjCPointerWrapper_RegisterID (PyObjC_API->register_id_alias)

typedef void (*PyObjC_Function_Pointer)(void);
typedef struct PyObjC_function_map {
    const char* name;
    PyObjC_Function_Pointer function;
} PyObjC_function_map;



#ifndef PYOBJC_METHOD_STUB_IMPL

static inline PyObject*
PyObjC_CreateInlineTab(PyObjC_function_map* map)
{
#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 7
    return PyCObject_FromVoidPtr(map, NULL);
#else
    return PyCapsule_New(map, "objc.__inline__", NULL);
#endif
}

static inline int
PyObjC_ImportAPI(PyObject* calling_module)
{
    PyObject* m;
    PyObject* d;
    PyObject* api_obj;
#if PY_MAJOR_VERSION == 2
    PyObject* name = PyString_FromString("objc");
#else
    PyObject* name = PyUnicode_FromString("objc");
#endif

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
#if PY_MAJOR_VERSION == 2 && PY_VERSION_MAJOR < 7
    PyObjC_API = (struct pyobjc_api *)PyCObject_AsVoidPtr(api_obj);
#else
    PyObjC_API = (struct pyobjc_api *)PyCapsule_GetPointer(api_obj, "objc." PYOBJC_API_NAME);
#endif
    if (PyObjC_API == NULL) {
        return 0;
    }
    if (PyObjC_API->api_version != PYOBJC_API_VERSION) {
        PyErr_Format(PyExc_RuntimeError,
            "Wrong version of PyObjC C API (got %d, expected %d)",
            (int)PyObjC_API->api_version, (int)PYOBJC_API_VERSION);
        return -1;
    }

    if (PyObjC_API->struct_len < sizeof(struct pyobjc_api)) {
        PyErr_Format(PyExc_RuntimeError,
            "Wrong struct-size of PyObjC C API (got %d, expected %d)",
            (int)PyObjC_API->struct_len, (int)sizeof(struct pyobjc_api));
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

extern struct pyobjc_api objc_api;
extern int PyObjCAPI_Register(PyObject* module);

#endif /* !PYOBJC_BUILD */

#endif /* PyObjC_API_H */
