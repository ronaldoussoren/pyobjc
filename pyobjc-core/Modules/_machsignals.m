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
    PyObject* tmp;
    PyObject* callable;
    int       signum;
    /* this is abuse of msgh_id */
    signum = ((mach_msg_header_t*)msg)->msgh_id;
    if (!signalmapping) { // LCOV_BR_EXCL_LINE
        return;           // LCOV_EXCL_LINE
    }
    PyObjC_BEGIN_WITH_GIL
        tmp = PyLong_FromLong((long)signum);
        if (tmp == NULL) {            // LCOV_BR_EXCL_LINE
            PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            __builtin_unreachable();  // LOCV_EXCL_LINE
        }

        callable = PyDict_GetItem(signalmapping, tmp);
        if (!callable) {
            Py_DECREF(tmp);
            PyObjC_GIL_RETURNVOID;
        }
        Py_INCREF(callable);
        Py_DECREF(tmp);

        tmp = PyObject_CallFunction(callable, "i", signum);
        Py_DECREF(callable);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }
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

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "_machsignals",
                                        machsignals_doc,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit__machsignals(void);
PyObject* __attribute__((__visibility__("default"))) PyInit__machsignals(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (m == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    CFMachPortRef      e_port;
    CFRunLoopSourceRef e_rls;

    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return NULL;               // LCOV_EXCL_LINE
    }

    signalmapping = PyDict_New();
    if (!signalmapping) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, "_signalmapping", signalmapping) // LCOV_BR_EXCL_LINE
        == -1) {                                               // LCOV_BR_EXCL_LINE
        return NULL;                                           // LCOV_EXCL_LINE
    }

    e_port      = CFMachPortCreate(NULL, SIGCallback, NULL, NULL);
    exit_m_port = CFMachPortGetPort(e_port);
    e_rls       = CFMachPortCreateRunLoopSource(NULL, e_port, 0);
    CFRunLoopAddSource(CFRunLoopGetCurrent(), e_rls, kCFRunLoopDefaultMode);
    CFRelease(e_rls);

    return m;
}
