/*
 * This file defines the glue code that is needed to access the objc module
 * from other modules.
 *
 * Why would you want to do that?
 * - To wrap native functions that use Objective-C objects as arguments or
 *   return values
 * - To add custom wrappers for troublesome methods in specific classes
 * - To generic support for additional method signatures
 */
#include "pyobjc.h"

#ifdef PyObjCObject_GetObject
#undef PyObjCObject_GetObject
#endif


static id
python_to_id(PyObject* object)
{
    id result;
    int err;

    err = depythonify_c_value(@encode(id), object, &result);
    if (err == -1) {
        return nil;
    }

    return result;
}

static PyObject*
id_to_python(id object)
{
    PyObject* result;

    result = pythonify_c_value(@encode(id), &object);
    return result;
}

static Class
sel_get_class(PyObject* sel)
{
    if (!PyObjCNativeSelector_Check(sel)) {
        PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
        return NULL;
    }
    return ((PyObjCNativeSelector*)sel)->sel_class;
}

static SEL
sel_get_sel(PyObject* sel)
{
    if (!PyObjCSelector_Check(sel)) {
        PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
        return NULL;
    }
    return ((PyObjCSelector*)sel)->sel_selector;
}

static void
fill_super(struct objc_super* super, Class cls, id receiver)
{
    objc_superSetReceiver(*super, receiver);
    objc_superSetClass(*super, cls);
}

static void
fill_super_cls(struct objc_super* super, Class cls, Class self)
{
    objc_superSetReceiver(*super, self);
    objc_superSetClass(*super, object_getClass(cls));
}

static int
depythonify_c_array_count2(const char* type, Py_ssize_t count, BOOL strict, PyObject* value, void* datum)
{
    return depythonify_c_array_count(type, count, strict, value, datum, NO, NO);
}




struct pyobjc_api objc_api = {
    .api_version                = PYOBJC_API_VERSION,
    .struct_len                 = sizeof(struct pyobjc_api),
    .register_method_mapping    =  (RegisterMethodMappingFunctionType*)PyObjC_RegisterMethodMapping,
    .obj_get_object             = PyObjCObject_GetObject,
    .cls_get_class              = PyObjCClass_GetClass,
    .python_to_id               = python_to_id,
    .id_to_python               = id_to_python,
    .err_objc_to_python         = PyObjCErr_FromObjC,
    .py_to_objc                 = depythonify_c_value,
    .objc_to_py                 = pythonify_c_value,
    .sizeof_type                = PyObjCRT_SizeOfType,
    .sel_get_class              = sel_get_class,
    .sel_get_sel                = sel_get_sel,
    .fill_super                 = fill_super,
    .fill_super_cls             = fill_super_cls,
    .register_pointer_wrapper   = PyObjCPointerWrapper_Register,
    .unsupported_method_imp     = (void(*)(void*,void*,void**,void*))PyObjCUnsupportedMethod_IMP,
    .unsupported_method_caller  = PyObjCUnsupportedMethod_Caller,
    .err_python_to_objc_gil     = PyObjCErr_ToObjCWithGILState,
    .free_c_array               = PyObjC_FreeCArray,
    .py_to_c_array              = PyObjC_PythonToCArray,
    .c_array_to_py              = PyObjC_CArrayToPython,
    .imp_type                   = &PyObjCIMP_Type,
    .imp_get_imp                = PyObjCIMP_GetIMP,
    .imp_get_sel                = PyObjCIMP_GetSelector,
    .newtransient               = PyObjCObject_NewTransient,
    .releasetransient           = PyObjCObject_ReleaseTransient,
    .pyobjc_null                = &PyObjC_NULL,
    .dep_c_array_count          = depythonify_c_array_count2,
    .varlistnew                 = PyObjC_VarList_New,
    .pyobjcobject_convert       = PyObjCObject_Convert,
};

int PyObjCAPI_Register(PyObject* module)
{
#if PY_MAJOR_VERSION == 2
    PyObject* API = PyCObject_FromVoidPtr(&objc_api, NULL);
#else
    PyObject* API = PyCapsule_New(&objc_api, "objc." PYOBJC_API_NAME, NULL);
#endif

    if (API == NULL) return -1;

    if (PyModule_AddObject(module, PYOBJC_API_NAME, API) < 0) {
        Py_DECREF(API);
        return -1;
    }
    return 0;
}
