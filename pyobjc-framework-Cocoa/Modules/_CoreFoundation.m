#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_CoreFoundation_CFBag.m"
#include "_CoreFoundation_CFBinaryHeap.m"
#include "_CoreFoundation_CFBitVector.m"
#include "_CoreFoundation_CFCalendar.m"
#include "_CoreFoundation_CFDictionary.m"
#include "_CoreFoundation_CFFileDescriptor.m"
#include "_CoreFoundation_CFMachPort.m"
#include "_CoreFoundation_CFMessagePort.m"
#include "_CoreFoundation_CFNumber.m"
#include "_CoreFoundation_CFNumberFormatter.m"
#include "_CoreFoundation_CFReadStream.m"
#include "_CoreFoundation_CFRunLoopObserver.m"
#include "_CoreFoundation_CFRunLoopSource.m"
#include "_CoreFoundation_CFRunLoopTimer.m"
#include "_CoreFoundation_CFSet.m"
#include "_CoreFoundation_CFSocket.m"
#include "_CoreFoundation_CFTree.m"
#include "_CoreFoundation_CFWriteStream.m"

static PyMethodDef mod_methods[] = {
    COREFOUNDATION_CFBAG_METHODS COREFOUNDATION_CFBINARYHEAP_METHODS
        COREFOUNDATION_BITVECTOR_METHODS COREFOUNDATION_CALENDAR_METHODS
            COREFOUNDATION_DICTIONARY_METHODS COREFOUNDATION_FILEDESCRIPTOR_METHODS
                COREFOUNDATION_MACHPORT_METHODS COREFOUNDATION_MESSAGEPORT_METHODS
                    COREFOUNDATION_NUMBER_METHODS COREFOUNDATION_NUMBERFORMATTER_METHODS
                        COREFOUNDATION_READSTREAM_METHODS COREFOUNDATION_RUNLOOP_METHODS
                            COREFOUNDATION_RUNLOOPSOURCE_METHODS
                                COREFOUNDATION_RUNLOOPTIMER_METHODS
                                    COREFOUNDATION_SET_METHODS
                                        COREFOUNDATION_SOCKET_METHODS
                                            COREFOUNDATION_TREE_METHODS
                                                COREFOUNDATION_WRITESTREAM_METHODS

    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;

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
    .m_name     = "_CoreFoundation",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__CoreFoundation(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__CoreFoundation(void)
{
    return PyModuleDef_Init(&mod_module);
}
