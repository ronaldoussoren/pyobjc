#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <SystemConfiguration/SystemConfiguration.h>

NS_ASSUME_NONNULL_BEGIN

/*
 * Context definitions
 *
 * Note that the use of a tuple object for the context 'info'
 * is safe because the tuple is fully owned by the context object,
 * free-threading doesn't change this.
 */

static const void*
mod_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_XINCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_XDECREF((PyObject*)info);
    PyGILState_Release(state);
}

static SCDynamicStoreContext mod_SCDynamicStoreContext = {
    0,           /* version */
    NULL,        /* info */
    mod_retain,  /* retain */
    mod_release, /* release */
    NULL         /* copyDescription */
};

static SCPreferencesContext mod_SCPreferencesContext = {
    0,           /* version */
    NULL,        /* info */
    mod_retain,  /* retain */
    mod_release, /* release */
    NULL         /* copyDescription */
};

static SCNetworkConnectionContext mod_SCNetworkConnectionContext = {
    0,           /* version */
    NULL,        /* info */
    mod_retain,  /* retain */
    mod_release, /* release */
    NULL         /* copyDescription */
};

static SCNetworkReachabilityContext mod_SCNetworkReachabilityContext = {
    0,           /* version */
    NULL,        /* info */
    mod_retain,  /* retain */
    mod_release, /* release */
    NULL         /* copyDescription */
};

/* Callback implementations */

static void
mod_SCDynamicStoreCallBack(SCDynamicStoreRef store, CFArrayRef changedKeys, void* _info)
{
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* info      = (PyObject*)_info;
    PyObject* callable  = PyTuple_GetItem(info, 0);
    PyObject* real_info = PyTuple_GetItem(info, 1);
    PyObject* py_store  = PyObjC_ObjCToPython(@encode(SCDynamicStoreRef), &store);
    if (py_store == NULL) {                   // LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }

    PyObject* py_keys = PyObjC_ObjCToPython(@encode(CFArrayRef), &changedKeys);
    if (py_keys == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_store);
        PyObjCErr_ToObjCWithGILState(&state);
        // LCOV_EXCL_STOP
    }

    PyObject* result =
        PyObject_CallFunction(callable, "NNO", py_store, py_keys, real_info);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static void
mod_SCPreferencesCallBack(SCPreferencesRef          prefs,
                          SCPreferencesNotification notificationType, void* _info)
{
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* info      = (PyObject*)_info;
    PyObject* callable  = PyTuple_GetItem(info, 0);
    PyObject* real_info = PyTuple_GetItem(info, 1);
    PyObject* py_prefs  = PyObjC_ObjCToPython(@encode(SCPreferencesRef), &prefs);
    if (py_prefs == NULL) {                   // LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }
    PyObject* py_type =
        PyObjC_ObjCToPython(@encode(SCPreferencesNotification), &notificationType);
    if (py_type == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_prefs);
        PyObjCErr_ToObjCWithGILState(&state);
        // LCOV_EXCL_STOP
    }

    PyObject* result =
        PyObject_CallFunction(callable, "NNO", py_prefs, py_type, real_info);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

// LCOV_EXCL_START
// This API is related to dial in interfaces, cannot test this
// in my testing setup.
static void
mod_SCNetworkConnectionCallBack(SCNetworkConnectionRef    connection,
                                SCNetworkConnectionStatus status, void* _info)
{
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* info      = (PyObject*)_info;
    PyObject* callable  = PyTuple_GetItem(info, 0);
    PyObject* real_info = PyTuple_GetItem(info, 1);
    PyObject* py_connection =
        PyObjC_ObjCToPython(@encode(SCNetworkConnectionRef), &connection);
    if (py_connection == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    PyObject* py_status =
        PyObjC_ObjCToPython(@encode(SCNetworkConnectionStatus), &status);
    if (py_status == NULL) {
        Py_DECREF(py_connection);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result =
        PyObject_CallFunction(callable, "NNO", py_connection, py_status, real_info);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}
// LCOV_EXCL_STOP

static void
mod_SCNetworkReachabilityCallBack(SCNetworkReachabilityRef target,
                                  SCNetworkConnectionFlags flags, void* _info)
{
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* info      = (PyObject*)_info;
    PyObject* callable  = PyTuple_GetItem(info, 0);
    PyObject* real_info = PyTuple_GetItem(info, 1);
    PyObject* py_target = PyObjC_ObjCToPython(@encode(SCNetworkReachabilityRef), &target);
    if (py_target == NULL) {                  // LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }
    PyObject* py_flags = PyObjC_ObjCToPython(@encode(SCNetworkConnectionFlags), &flags);
    if (py_flags == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_target);
        PyObjCErr_ToObjCWithGILState(&state);
        // LCOV_EXCL_STOP
    }

    PyObject* result =
        PyObject_CallFunction(callable, "NNO", py_target, py_flags, real_info);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

/* And finally the function wrappers */

static PyObject* _Nullable mod_SCDynamicStoreCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef allocator;
    CFStringRef    name;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFStringRef), args[1], &name) < 0) {
        return NULL;
    }

    PyObject* real_info = PyTuple_Pack(2, args[2], args[3]);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    SCDynamicStoreRef     store = NULL;
    SCDynamicStoreContext real_context;
    real_context      = mod_SCDynamicStoreContext;
    real_context.info = real_info;

    Py_BEGIN_ALLOW_THREADS
        @try {
            store = SCDynamicStoreCreate(allocator, name, mod_SCDynamicStoreCallBack,
                                         &real_context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            store = NULL;                        // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS
    Py_DECREF(real_info);

    if (store == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (PyErr_Occurred()) {
            return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
        // LCOV_EXCL_STOP
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(SCDynamicStoreRef), &store);
    CFRelease(store);

    return result;
}

static PyObject* _Nullable mod_SCDynamicStoreCreateWithOptions(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef  allocator;
    CFDictionaryRef storeOptions;
    CFStringRef     name;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFStringRef), args[1], &name) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), args[2], &storeOptions) < 0) {
        return NULL;
    }

    PyObject* real_info = PyTuple_Pack(2, args[3], args[4]);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    SCDynamicStoreRef     store = NULL;
    SCDynamicStoreContext real_context;
    real_context      = mod_SCDynamicStoreContext;
    real_context.info = real_info;

    Py_BEGIN_ALLOW_THREADS
        @try {
            store = SCDynamicStoreCreateWithOptions(
                allocator, name, storeOptions, mod_SCDynamicStoreCallBack, &real_context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            store = NULL;                        // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS
    Py_DECREF(real_info);

    if (store == NULL) {

        if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;        // LCOV_EXCL_LINE
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(SCDynamicStoreRef), &store);
    if (store != NULL) {
        CFRelease(store);
    }

    return result;
}

static PyObject* _Nullable mod_SCPreferencesSetCallback(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    SCPreferencesRef prefs;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(SCPreferencesRef), args[0], &prefs) < 0) {
        return NULL;
    }

    PyObject* real_info = PyTuple_Pack(2, args[1], args[2]);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    SCPreferencesContext real_context;
    real_context      = mod_SCPreferencesContext;
    real_context.info = real_info;

    Boolean result = FALSE;
    Py_BEGIN_ALLOW_THREADS
        @try {
            result =
                SCPreferencesSetCallback(prefs, mod_SCPreferencesCallBack, &real_context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            result = FALSE;                      // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (!result) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(real_info);

        if (PyErr_Occurred()) {
            return NULL;
        }
        // LCOV_EXCL_STOP
    } // LCOV_EXCL_LINE

    return PyBool_FromLong(result);
}

static PyObject* _Nullable mod_SCNetworkConnectionCreateWithServiceID(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef allocator;
    CFStringRef    serviceID;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFStringRef), args[1], &serviceID) < 0) {
        return NULL;
    }

    PyObject* real_info = PyTuple_Pack(2, args[2], args[3]);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    SCNetworkConnectionContext real_context;
    real_context      = mod_SCNetworkConnectionContext;
    real_context.info = real_info;

    SCNetworkConnectionRef result = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            result = SCNetworkConnectionCreateWithServiceID(
                allocator, serviceID, mod_SCNetworkConnectionCallBack, &real_context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            result = NULL;                       // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(real_info);

    if (result == NULL)       // LCOV_BR_EXCL_LINE
        if (PyErr_Occurred()) // LCOV_EXCL_LINE
            return NULL;      // LCOV_EXCL_LINE

    PyObject* rv = PyObjC_ObjCToPython(@encode(SCNetworkConnectionRef), &result);
    if (result != NULL) { // LCOV_BR_EXCL_LINE
        CFRelease(result);
    }
    return rv;
}

static PyObject* _Nullable mod_SCNetworkReachabilitySetCallback(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    SCNetworkReachabilityRef target;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(SCNetworkReachabilityRef), args[0], &target) < 0) {
        return NULL;
    }

    PyObject* real_info = PyTuple_Pack(2, args[1], args[2]);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    SCNetworkReachabilityContext real_context;
    real_context      = mod_SCNetworkReachabilityContext;
    real_context.info = real_info;

    Boolean result = FALSE;
    Py_BEGIN_ALLOW_THREADS
        @try {
            result = SCNetworkReachabilitySetCallback(
                target, mod_SCNetworkReachabilityCallBack, &real_context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            result = FALSE;                      // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS
    Py_DECREF(real_info);

    if (!result) // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
            return NULL;      // LCOV_EXCL_LINE
    // LCOV_EXCL_STOP

    return PyBool_FromLong(result);
}

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyObjCRegister_FunctionCaller(SCDynamicStoreCreate, mod_SCDynamicStoreCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(SCDynamicStoreCreateWithOptions,
                                      mod_SCDynamicStoreCreateWithOptions)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(SCPreferencesSetCallback,
                                      mod_SCPreferencesSetCallback)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(SCNetworkConnectionCreateWithServiceID,
                                      mod_SCNetworkConnectionCreateWithServiceID)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(SCNetworkReachabilitySetCallback,
                                      mod_SCNetworkReachabilitySetCallback)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_SystemConfiguration",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__SystemConfiguration(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__SystemConfiguration(void)
{
    return PyModuleDef_Init(&mod_module);
}
NS_ASSUME_NONNULL_END
