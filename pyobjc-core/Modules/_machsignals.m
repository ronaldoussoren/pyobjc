/*
 * Signal handling integrated into the default runloop
 * on the thread that imports this extension.
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#include <CoreFoundation/CoreFoundation.h>
#include <mach/mach.h>
#include <mach/mach_error.h>

PyDoc_STRVAR(machsignals_doc,
             "_machsignals - signal handling integrated into the runloop\n"
             "\n"
             "This module exports a dictionary that contains the functions that \n"
             "should be called when a signal is caught.\n"
             "\n"
             "The function 'handle_signal' installs a C signal handler that will \n"
             "make sure our signal handler is called.");

static mach_port_t exit_m_port = MACH_PORT_NULL;
static PyObject*   signalmapping;

static void
SIGCallback(CFMachPortRef port __attribute__((__unused__)), void* msg,
            CFIndex size __attribute__((__unused__)),
            void*   info __attribute__((__unused__)))
{
    PyObject* callable;
    int       signum;
    int       r;
    /* this is abuse of msgh_id */
    signum = ((mach_msg_header_t*)msg)->msgh_id;
    if (!signalmapping) { // LCOV_BR_EXCL_LINE
        return;           // LCOV_EXCL_LINE
    }
    PyObjC_BEGIN_WITH_GIL
        PyObject* result;
        PyObject* py_signum = PyLong_FromLong((long)signum);
        if (py_signum == NULL) {      // LCOV_BR_EXCL_LINE
            PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
        } else {                      // LCOV_EXCL_LINE
            r = PyDict_GetItemRef(signalmapping, py_signum, &callable);
            switch (r) { // LCOV_BR_EXCL_LINE
            case 0:
                Py_DECREF(py_signum);
                PyObjC_GIL_RETURNVOID;
            case -1:
                Py_DECREF(py_signum);     // LCOV_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            case 1:
#if PY_VERSION_HEX >= 0x03090000
                result = PyObject_CallOneArg(callable, py_signum);
#else
                result = PyObject_CallFunction(callable, "O", py_signum);
#endif
                Py_DECREF(py_signum);
                Py_DECREF(callable);
                if (result == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                } else { // LCOV_EXCL_LINE
                    Py_DECREF(result);
                }
            }
        } // LCOV_EXCL_LINE
    PyObjC_END_WITH_GIL
}

static void
HandleSIG(int signum)
{
    /*
     * Send a mach_msg to ourselves (since that is signal safe) telling us
     * to handle a signal.
     */
    mach_msg_header_t header;

    header.msgh_bits        = MACH_MSGH_BITS(MACH_MSG_TYPE_MAKE_SEND, 0);
    header.msgh_remote_port = exit_m_port;
    header.msgh_local_port  = MACH_PORT_NULL;
    header.msgh_size        = sizeof(header);
    /* this is abuse of msgh_id */
    header.msgh_id = signum;

    (void)mach_msg_send(&header);
}

PyDoc_STRVAR(machsignals_handleSignal_doc,
             "handle_signal(signum) -> None\n"
             "\n"
             "Handle a signal using the registered mach callback\n"
             "Raises an ObjC exception if the callback fails");
static PyObject*
machsignals_handleSignal(PyObject* self __attribute__((__unused__)), PyObject* args,
                         PyObject* kwds)
{
    static char* keywords[] = {"signum", 0};
    int          signum;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "i:handleSignal", keywords, &signum)) {
        return NULL;
    }

    signal(signum, HandleSIG);

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {
    {"handle_signal", (PyCFunction)machsignals_handleSignal, METH_VARARGS | METH_KEYWORDS,
     machsignals_handleSignal_doc},
    {0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    CFMachPortRef      e_port;
    CFRunLoopSourceRef e_rls;

    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    signalmapping = PyDict_New();
    if (!signalmapping) { // LCOV_BR_EXCL_LINE
        return -1;        // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, "_signalmapping", signalmapping) // LCOV_BR_EXCL_LINE
        == -1) {                                               // LCOV_BR_EXCL_LINE
        return -1;                                             // LCOV_EXCL_LINE
    }

    e_port      = CFMachPortCreate(NULL, SIGCallback, NULL, NULL);
    exit_m_port = CFMachPortGetPort(e_port);
    e_rls       = CFMachPortCreateRunLoopSource(NULL, e_port, 0);
    CFRunLoopAddSource(CFRunLoopGetCurrent(), e_rls, kCFRunLoopDefaultMode);
    CFRelease(e_rls);

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
    .m_name     = "_machsignals",
    .m_doc      = machsignals_doc,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__machsignals(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__machsignals(void)
{
    return PyModuleDef_Init(&mod_module);
}
