/*
 * Support for callback functions/structs in the FSEvents frameework.
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <CoreServices/CoreServices.h>

NS_ASSUME_NONNULL_BEGIN

static const void* _Nullable m_retain_python(const void* _Nullable value)
{
    PyGILState_STATE state = PyGILState_Ensure();

    Py_XINCREF((PyObject*)value);

    PyGILState_Release(state);

    return value;
}

static void
m_release_python(const void* _Nullable value)
{
    PyGILState_STATE state = PyGILState_Ensure();

    Py_XDECREF((PyObject*)value);

    PyGILState_Release(state);
}

// LCOV_EXCL_START
// The description is here for debugging support, cannot be
// triggered during testing.
static CFStringRef _Nullable m_copyDescription_python(const void* value)
{
    CFStringRef result;
    PyObject*   description;
    int         r;

    PyGILState_STATE state = PyGILState_Ensure();

    description = PyObject_Repr((PyObject*)value);
    if (description == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    r = PyObjC_PythonToObjC(@encode(CFStringRef), description, &result);
    Py_DECREF(description);
    if (r == -1) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    /* description is autoreleased, we should donate a reference to
     * our caller
     */
    CFRetain(result);

    PyGILState_Release(state);
    return result;
}
// LCOV_EXCL_STOP

static FSEventStreamContext m_python_context_template = {
    0, NULL, m_retain_python, m_release_python, m_copyDescription_python};

static void
m_FSEVentStreamCallback(ConstFSEventStreamRef streamRef,
                        void* _Nullable clientCallbackInfo, size_t numEvents,
                        void* eventPaths, const FSEventStreamEventFlags eventFlags[],
                        const FSEventStreamEventId eventIds[])
{
    PyGILState_STATE         state = PyGILState_Ensure();
    FSEventStreamCreateFlags flags;
    PyObject*                callback;
    PyObject*                info;
    PyObject*                v;
    PyObject*                paths;

    v = PyTuple_GET_ITEM((PyObject*)clientCallbackInfo, 0);
    if (PyObjC_PythonToObjC(@encode(FSEventStreamCreateFlags), v, &flags)
        < 0) {                                //  LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }

    info     = PyTuple_GET_ITEM((PyObject*)clientCallbackInfo, 1);
    callback = PyTuple_GET_ITEM((PyObject*)clientCallbackInfo, 2);

    if (flags & kFSEventStreamCreateFlagUseCFTypes) {
        /* The evenPaths are an CFArray */
        paths = PyObjC_ObjCToPython(@encode(CFArrayRef), &eventPaths);
        if (paths == NULL) {                      // LCOV_BR_EXCL_LINE
            PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
        }
    } else {
        /* The evenPaths are a CArray of C strings */
        paths = PyObjC_CArrayToPython(@encode(char*), eventPaths, numEvents);
        if (paths == NULL) {                      // LCOV_BR_EXCL_LINE
            PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
        }
    }

    PyObject* py_streamRef = PyObjC_ObjCToPython(@encode(FSEventStreamRef), &streamRef);
    if (py_streamRef == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(paths);
        PyObjCErr_ToObjCWithGILState(&state);
        // LCOV_EXCL_STPP
    }
    PyObject* py_eventFlags = PyObjC_CArrayToPython(@encode(FSEventStreamCreateFlags),
                                                    (void*)eventFlags, numEvents);
    if (py_eventFlags == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(paths);
        Py_DECREF(py_streamRef);
        PyObjCErr_ToObjCWithGILState(&state);
        // LCOV_EXCL_STOP
    }
    PyObject* py_eventIds =
        PyObjC_CArrayToPython(@encode(FSEventStreamEventId), (void*)eventIds, numEvents);
    if (py_eventIds == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(paths);
        Py_DECREF(py_streamRef);
        Py_DECREF(py_eventFlags);
        PyObjCErr_ToObjCWithGILState(&state);
        // LCOV_EXCL_STOP
    }

    PyObject* result =
        PyObject_CallFunction(callback, "OOnOOO", py_streamRef, info, numEvents, paths,
                              py_eventFlags, py_eventIds);
    Py_DECREF(paths);
    Py_DECREF(py_streamRef);
    Py_DECREF(py_eventFlags);
    Py_DECREF(py_eventIds);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static PyObject* _Nullable m_FSEventStreamCreate(PyObject* meth,
                                                 PyObject* _Nonnull const* _Nonnull args,
                                                 size_t nargs)
{
    if (PyObjC_CheckArgCount(meth, 7, 7, nargs) == -1) {
        return NULL;
    }

    CFAllocatorRef allocator;
    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    CFArrayRef pathsToWatch;
    if (PyObjC_PythonToObjC(@encode(CFArrayRef), args[3], &pathsToWatch) < 0) {
        return NULL;
    }

    FSEventStreamEventId sinceWhen;
    if (PyObjC_PythonToObjC(@encode(FSEventStreamEventId), args[4], &sinceWhen) < 0) {
        return NULL;
    }

    CFTimeInterval latency;
    if (PyObjC_PythonToObjC(@encode(CFTimeInterval), args[5], &latency) < 0) {
        return NULL;
    }

    FSEventStreamCreateFlags flags;
    if (PyObjC_PythonToObjC(@encode(FSEventStreamCreateFlags), args[6], &flags) < 0) {
        return NULL;
    }

    /*
     * Build the actual callback info, which includes the flags because
     * the arguments passed to the callback vary based on the value of
     * flags.
     */
    PyObject* info = PyTuple_Pack(3, args[6], args[2], args[1]);
    if (info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    FSEventStreamContext context = m_python_context_template;
    context.info                 = info;

    FSEventStreamRef stream = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            stream = FSEventStreamCreate(allocator, m_FSEVentStreamCallback, &context,
                                         pathsToWatch, sinceWhen, latency, flags);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            stream = NULL;                       // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(info);

    if (stream == NULL && PyErr_Occurred()) { // LCOV_EXCL_LINE
        return NULL;                          // LCOV_EXCL_LINE
    }

    if (stream == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(FSEventStreamRef), &stream);
    // FSEventStreamRef is not a CF type (AFAIK), hence the user is
    // responsible for maintaining the refcount.
    // FSEventStreamRelease(stream);
    return result;
}

static PyObject* _Nullable m_FSEventStreamCreateRelativeToDevice(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    if (PyObjC_CheckArgCount(meth, 8, 8, nargs) == -1) {
        return NULL;
    }

    CFAllocatorRef allocator;
    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    dev_t deviceToWatch;
    if (PyObjC_PythonToObjC(@encode(dev_t), args[3], &deviceToWatch) < 0) {
        return NULL;
    }

    CFArrayRef pathsToWatch;
    if (PyObjC_PythonToObjC(@encode(CFArrayRef), args[4], &pathsToWatch) < 0) {
        return NULL;
    }

    FSEventStreamEventId sinceWhen;
    if (PyObjC_PythonToObjC(@encode(FSEventStreamEventId), args[5], &sinceWhen) < 0) {
        return NULL;
    }

    CFTimeInterval latency;
    if (PyObjC_PythonToObjC(@encode(CFTimeInterval), args[6], &latency) < 0) {
        return NULL;
    }

    FSEventStreamCreateFlags flags;
    if (PyObjC_PythonToObjC(@encode(FSEventStreamCreateFlags), args[7], &flags) < 0) {
        return NULL;
    }

    /*
     * Build the actual callback info, which includes the flags because
     * the arguments passed to the callback vary based on the value of
     * flags.
     */
    PyObject* info = PyTuple_Pack(3, args[7], args[2], args[1]);
    if (info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    FSEventStreamContext context = m_python_context_template;
    context.info                 = info;

    FSEventStreamRef stream = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            stream = FSEventStreamCreateRelativeToDevice(
                allocator, m_FSEVentStreamCallback, &context, deviceToWatch, pathsToWatch,
                sinceWhen, latency, flags);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            stream = NULL;                       // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(info);

    if (stream == NULL && PyErr_Occurred()) { // LCOV_EXCL_LINE
        return NULL;                          // LCOV_EXCL_LINE
    }

    if (stream == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(FSEventStreamRef), &stream);
    // FSEventStreamRef is not a CF type (AFAIK), hence the user is
    // responsible for maintaining the refcount.
    // FSEventStreamRelease(stream);
    return result;
}

static PyMethodDef mod_methods[] = {

    {
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

    if (PyObjCRegister_FunctionCaller(FSEventStreamCreate, m_FSEventStreamCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(FSEventStreamCreateRelativeToDevice,
                                      m_FSEventStreamCreateRelativeToDevice)
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
    .m_name     = "_FSEvents",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__FSEvents(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__FSEvents(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
