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

struct pyobjc_api objc_api = {
    .api_version = PYOBJC_API_VERSION,
    .struct_len  = sizeof(struct pyobjc_api),
    .register_method_mapping =
        /* Cast is needed because of ffi_cif */
    (RegisterMethodMappingFunctionType*)PyObjC_RegisterMethodMapping,
    .obj_get_object            = PyObjCObject_GetObject,
    .cls_get_class             = PyObjCClass_GetClass,
    .depythonify_python_object = depythonify_python_object,
    .id_to_python              = id_to_python,
    .err_objc_to_python        = PyObjCErr_FromObjC,
    .py_to_objc                = depythonify_c_value,
    .objc_to_py                = pythonify_c_value,
    .sizeof_type               = PyObjCRT_SizeOfType,
    .sel_get_class             = PyObjCSelector_GetClass,
    .sel_get_sel               = PyObjCSelector_GetSelector,
    .register_pointer_wrapper  = PyObjCPointerWrapper_Register,
    .unsupported_method_imp    = (IMP _Nullable(*)(
        PyObject* _Nonnull, PyObject* _Nonnull))PyObjCUnsupportedMethod_IMP,
    .unsupported_method_caller = PyObjCUnsupportedMethod_Caller,
    .err_python_to_objc_gil    = PyObjCErr_ToObjCWithGILState,
    .free_c_array              = PyObjC_FreeCArray,
    .py_to_c_array             = PyObjC_PythonToCArray,
    .c_array_to_py             = PyObjC_CArrayToPython,
    .imp_type                  = NULL,
    .imp_get_imp               = PyObjCIMP_GetIMP,
    .imp_get_sel               = PyObjCIMP_GetSelector,
    .newtransient              = PyObjCObject_NewTransient,
    .releasetransient          = PyObjCObject_ReleaseTransient,
    .pyobjc_null               = &PyObjC_NULL,
    .dep_c_array_count         = depythonify_c_array_count,
    .varlistnew                = PyObjCVarList_New,
    .pyobjcobject_convert      = PyObjCObject_Convert,
    .register_id_alias         = PyObjCPointerWrapper_RegisterID,
    .memview_check             = PyObjCMemView_Check,
    .memview_new               = PyObjCMemView_New,
    .memview_getbuffer         = PyObjCMemView_GetBuffer,
    .checkargcount             = PyObjC_CheckArgCount,
    .checknokwnames            = PyObjC_CheckNoKwnames,
    .createopaquepointertype   = PyObjCCreateOpaquePointerType,
};

int
PyObjCAPI_Register(PyObject* module)
{
    objc_api.imp_type = (PyTypeObject*)PyObjCIMP_Type;
    PyObject* API     = PyCapsule_New(&objc_api, "objc." PYOBJC_API_NAME, NULL);

    if (API == NULL) // LCOV_BR_EXCL_LINE
        return -1;   // LCOV_EXCL_LINE

    if (PyModule_AddObject(module, PYOBJC_API_NAME, API) < 0) { // LCOV_BR_EXCL_LINE
        Py_DECREF(API);                                         // LCOV_EXCL_LINE
        return -1;                                              // LCOV_EXCL_LINE
    }
    return 0;
}
