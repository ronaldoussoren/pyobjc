#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <CFNetwork/CFNetwork.h>
#import <CoreServices/CoreServices.h>

NS_ASSUME_NONNULL_BEGIN

static const void*
mod_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

// LCOV_EXCL_START
// This function is at best using during C-level debugging.
static CFStringRef _Nullable mod_copyDescription(const void* info)
{
    PyObject*        repr;
    PyGILState_STATE state = PyGILState_Ensure();

    repr = PyObject_Repr((PyObject*)info);
    if (repr == NULL) {
        PyErr_Clear();
        PyGILState_Release(state);
        return (CFStringRef)CFRetain([NSString stringWithFormat:@"<pyinfo at %p>", info]);
    } else {
        NSString* result =
            [NSString stringWithFormat:@"<pyinfo %s>", PyUnicode_AsUTF8(repr)];
        Py_CLEAR(repr);
        PyGILState_Release(state);
        return (CFStringRef)CFRetain(result);
    }
}
// LCOV_EXCL_STOP

static CFStreamClientContext mod_CFStreamClientContext = {
    .version         = 0,
    .copyDescription = (CFStringRef (*)(void*))mod_copyDescription,
    .retain          = (void* (*)(void*))mod_retain,
    .release         = (void (*)(void*))mod_release,
    .info            = NULL};

static CFHostClientContext mod_CFHostClientContext = {0, NULL, mod_retain, mod_release,
                                                      0};

static CFNetServiceClientContext mod_CFNetServiceClientContext = {0, NULL, mod_retain,
                                                                  mod_release, 0};

static void
mod_CFProxyAutoConfigurationResultCallback(void* _context, CFArrayRef proxyList,
                                           CFErrorRef error)
{
    PyObject* context = (PyObject*)_context;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_func = PyTuple_GetItem(context, 0);
    PyObject* py_ctx  = PyTuple_GetItem(context, 1);

    PyObject* py_list = PyObjC_IdToPython((NSObject*)(NSArray*)proxyList);
    if (py_list == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }
    PyObject* py_error = PyObjC_IdToPython((NSObject*)(NSError*)error);
    if (py_error == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_list);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* rv = PyObject_CallFunction(py_func, "ONN", py_ctx, py_list, py_error);
    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(rv);

    PyGILState_Release(state);
}

static void
mod_CFNetServiceClientCallBack(CFNetServiceRef service, CFStreamError* error,
                               void* _context)
{
    PyObject* context = (PyObject*)_context;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_func = PyTuple_GetItem(context, 0);
    PyObject* py_ctx  = PyTuple_GetItem(context, 1);

    PyObject* py_service = PyObjC_IdToPython((NSObject*)service);
    if (py_service == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }
    PyObject* py_error = PyObjC_ObjCToPython("{CFStreamError=qi}", (void*)error);
    if (py_error == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_service);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* rv = PyObject_CallFunction(py_func, "NNO", py_service, py_error, py_ctx);

    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(rv);

    PyGILState_Release(state);
}

static void
mod_CFNetServiceMonitorClientCallBack(CFNetServiceMonitorRef  monitor,
                                      CFNetServiceRef         service,
                                      CFNetServiceMonitorType typeInfo, CFDataRef rdata,
                                      CFStreamError* error, void* _context)
{
    PyObject* context = (PyObject*)_context;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_func = PyTuple_GetItem(context, 0);
    PyObject* py_ctx  = PyTuple_GetItem(context, 1);

    PyObject* py_monitor = PyObjC_IdToPython((NSObject*)monitor);
    if (py_monitor == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* py_service = PyObjC_IdToPython((NSObject*)service);
    if (py_service == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_monitor);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* py_typeInfo =
        PyObjC_ObjCToPython(@encode(CFNetServiceMonitorType), &typeInfo);
    if (py_typeInfo == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_monitor);
        Py_DECREF(py_service);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* py_rdata = PyObjC_IdToPython((NSObject*)(NSData*)rdata);
    if (py_rdata == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_monitor);
        Py_DECREF(py_service);
        Py_DECREF(py_typeInfo);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* py_error = PyObjC_ObjCToPython("{CFStreamError=qi}", (void*)error);
    if (py_error == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_monitor);
        Py_DECREF(py_service);
        Py_DECREF(py_typeInfo);
        Py_DECREF(py_rdata);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* rv = PyObject_CallFunction(py_func, "NNNNNO", py_monitor, py_service,
                                         py_typeInfo, py_rdata, py_error, py_ctx);

    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(rv);

    PyGILState_Release(state);
}

static void
mod_CFHostClientCallBack(CFHostRef host, CFHostInfoType typeInfo,
                         const CFStreamError* error, void* _context)
{
    PyObject* context = (PyObject*)_context;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_func = PyTuple_GetItem(context, 0);
    PyObject* py_ctx  = PyTuple_GetItem(context, 1);

    PyObject* py_host = PyObjC_IdToPython((NSObject*)host);
    if (py_host == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }
    PyObject* py_info = PyObjC_ObjCToPython(@encode(CFHostInfoType), &typeInfo);
    if (py_info == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_host);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* py_error = PyObjC_ObjCToPython("{CFStreamError=qi}", (void*)error);
    if (py_error == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_host);
        Py_DECREF(py_info);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* rv =
        PyObject_CallFunction(py_func, "NNNO", py_host, py_info, py_error, py_ctx);

    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(rv);

    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFNetworkExecuteProxyAutoConfigurationScript(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFStringRef script;
    CFURLRef    url;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[0], (id*)&script) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[1], (id*)&url) == -1) {
        return NULL;
    }

    PyObject* py_context = PyTuple_Pack(2, args[2], args[3]);
    if (py_context == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;          // LCOV_EXCL_LINE
    }

    CFStreamClientContext context = mod_CFStreamClientContext;
    context.info                  = py_context;

    CFRunLoopSourceRef ref = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CFNetworkExecuteProxyAutoConfigurationScript(
                script, url, mod_CFProxyAutoConfigurationResultCallback, &context);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            ref = NULL;                          // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

    return rv;
}

static PyObject* _Nullable mod_CFNetworkExecuteProxyAutoConfigurationURL(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFURLRef script;
    CFURLRef url;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[0], (id*)&script) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[1], (id*)&url) == -1) {
        return NULL;
    }

    PyObject* py_context = PyTuple_Pack(2, args[2], args[3]);
    if (py_context == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;          // LCOV_EXCL_LINE
    }

    CFStreamClientContext context = mod_CFStreamClientContext;
    context.info                  = py_context;

    CFRunLoopSourceRef ref = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CFNetworkExecuteProxyAutoConfigurationURL(
                script, url, mod_CFProxyAutoConfigurationResultCallback, &context);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            ref = NULL;                          // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) { // LCOV_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

    return rv;
}

static PyObject* _Nullable mod_CFHostSetClient(PyObject* meth,
                                               PyObject* _Nonnull const* _Nonnull args,
                                               size_t nargs)
{
    CFHostRef host;
    Boolean   ok = 0;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[0], (id*)&host) == -1) {
        return NULL;
    }
    if (args[1] == Py_None) {
        Py_BEGIN_ALLOW_THREADS
            @try {
                ok = CFHostSetClient(host, NULL, NULL);
            } @catch (NSException* localException) { // LCOV_EXCL_LINE
                PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            }
        Py_END_ALLOW_THREADS

        if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;        // LCOV_EXCL_LINE
        }

        return PyBool_FromLong(!!ok);
    }

    PyObject* py_context = PyTuple_Pack(2, args[1], args[2]);
    if (py_context == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;          // LCOV_EXCL_LINE
    }

    CFHostClientContext context = mod_CFHostClientContext;
    context.info                = py_context;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ok = CFHostSetClient(host, mod_CFHostClientCallBack, &context);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return PyBool_FromLong(!!ok);
}

static void
mod_CFNetServiceBrowserClientCallBack(CFNetServiceBrowserRef browser, CFOptionFlags flags,
                                      CFTypeRef domainOrService, CFStreamError* error,
                                      void* _context)
{
    PyObject* context = (PyObject*)_context;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_func = PyTuple_GetItem(context, 0);
    PyObject* py_ctx  = PyTuple_GetItem(context, 1);

    PyObject* py_browser = PyObjC_IdToPython((NSObject*)browser);
    if (py_browser == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }
    PyObject* py_flags = PyObjC_ObjCToPython(@encode(CFOptionFlags), &flags);
    if (py_flags == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_browser);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* py_domainOrService = PyObjC_ObjCToPython("@", &domainOrService);
    if (py_domainOrService == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_browser);
        Py_DECREF(py_flags);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* py_error = PyObjC_ObjCToPython(@encode(CFStreamError), (void*)error);
    if (py_error == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_browser);
        Py_DECREF(py_flags);
        Py_DECREF(py_domainOrService);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
        // LCOV_EXCL_STOP
    }

    PyObject* rv = PyObject_CallFunction(py_func, "NNNNO", py_browser, py_flags,
                                         py_domainOrService, py_error, py_ctx);

    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(rv);

    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFNetServiceBrowserCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef allocator;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[0], (id*)&allocator) == -1) {
        return NULL;
    }

    PyObject* py_context = PyTuple_Pack(2, args[1], args[2]);
    if (py_context == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;          // LCOV_EXCL_LINE
    }

    CFNetServiceClientContext context = mod_CFNetServiceClientContext;
    context.info                      = py_context;

    CFNetServiceBrowserRef ref = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CFNetServiceBrowserCreate(
                allocator, mod_CFNetServiceBrowserClientCallBack, &context);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            ref = NULL;                          // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

    return rv;
}

static PyObject* _Nullable mod_CFNetServiceSetClient(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFNetServiceRef service;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[0], (id*)&service) == -1) {
        return NULL;
    }

    PyObject* py_context = PyTuple_Pack(2, args[1], args[2]);
    if (py_context == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;          // LCOV_EXCL_LINE
    }

    CFNetServiceClientContext context = mod_CFNetServiceClientContext;
    context.info                      = py_context;

    Boolean ok = NO;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ok = CFNetServiceSetClient(service, mod_CFNetServiceClientCallBack, &context);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            ok = NO;                             // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* rv = ok ? Py_True : Py_False;
    Py_INCREF(rv);

    return rv;
}

static PyObject* _Nullable mod_CFNetServiceMonitorCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef  allocator;
    CFNetServiceRef service;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[0], (id*)&allocator) == -1) {
        return NULL;
    }

    if (depythonify_python_object(args[1], (id*)&service) == -1) {
        return NULL;
    }

    PyObject* py_context = PyTuple_Pack(2, args[2], args[3]);
    if (py_context == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;          // LCOV_EXCL_LINE
    }

    CFNetServiceClientContext context = mod_CFNetServiceClientContext;
    context.info                      = py_context;

    CFNetServiceMonitorRef ref = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CFNetServiceMonitorCreate(
                allocator, service, mod_CFNetServiceMonitorClientCallBack, &context);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            ref = NULL;                          // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

    return rv;
}

static PyMethodDef mod_methods[] = {{
    0,
    0,
    0,
}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyObjCRegister_FunctionCaller(CFNetworkExecuteProxyAutoConfigurationScript,
                                      mod_CFNetworkExecuteProxyAutoConfigurationScript)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFNetworkExecuteProxyAutoConfigurationURL,
                                      mod_CFNetworkExecuteProxyAutoConfigurationURL)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFHostSetClient, mod_CFHostSetClient)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFNetServiceBrowserCreate,
                                      mod_CFNetServiceBrowserCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFNetServiceSetClient, mod_CFNetServiceSetClient)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFNetServiceSetClient, mod_CFNetServiceSetClient)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFNetServiceMonitorCreate,
                                      mod_CFNetServiceMonitorCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
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
    .m_name     = "_CFNetwork",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__CFNetwork(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__CFNetwork(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
