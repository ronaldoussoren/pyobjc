#ifndef PyObjC_FFI_SUPPORT_H
#define PyObjC_FFI_SUPPORT_H

#include "ffi.h"

#ifndef FFI_CLOSURES
#    error "Need FFI_CLOSURES!"
#endif

struct byref_attr {
    int token;
    PyObject* buffer;
};

typedef void (*PyObjCFFI_ClosureFunc)(ffi_cif*, void*, void**, void*);

extern void PyObjCFFI_FreeCIF(ffi_cif* cif);
extern ffi_cif* PyObjCFFI_CIFForSignature(PyObjCMethodSignature* signature);
extern IMP PyObjCFFI_MakeClosure(PyObjCMethodSignature* signature,
            PyObjCFFI_ClosureFunc func, void* userdata);
extern void* PyObjCFFI_FreeClosure(IMP closure);

extern IMP PyObjCFFI_MakeIMPForSignature(PyObjCMethodSignature* methinfo, SEL sel, PyObject* callable);
extern IMP PyObjCFFI_MakeIMPForPyObjCSelector(PyObjCSelector *aSelector);
extern PyObject *PyObjCFFI_Caller(PyObject *aMeth, PyObject* self, PyObject *args);
extern void PyObjCFFI_FreeIMP(IMP imp);

typedef void (*PyObjCBlockFunction)(void*, ...);
extern PyObjCBlockFunction PyObjCFFI_MakeBlockFunction(PyObjCMethodSignature* sig, PyObject* callable);
extern void PyObjCFFI_FreeBlockFunction(PyObjCBlockFunction value);

extern int PyObjCFFI_CountArguments(
    PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
    Py_ssize_t* byref_in_count,
    Py_ssize_t* byref_out_count,
    Py_ssize_t* plain_count,
    Py_ssize_t* argbuf_len,
    BOOL* havePrintf);

extern Py_ssize_t PyObjCFFI_ParseArguments(
    PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
    PyObject* args, Py_ssize_t argbuf_cur, unsigned char* argbuf, Py_ssize_t argbuf_len,
    void** byref, struct byref_attr* byref_attr,
    ffi_type** arglist, void** values);

extern PyObject* PyObjCFFI_BuildResult(
    PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
    void* pRetval, void** byref, struct byref_attr* byref_attr,
    Py_ssize_t byref_out_count,
    PyObject* self, int flags, void** argvalues);

extern int PyObjCFFI_AllocByRef(Py_ssize_t argcount, void*** byref, struct byref_attr** byref_attr);
extern int PyObjCFFI_FreeByRef(Py_ssize_t argcount, void** byref, struct byref_attr* byref_attr);

/* XXX: rename me */
extern ffi_type* signature_to_ffi_return_type(const char* argtype);


typedef void (*PyObjC_callback_function)(void);
extern PyObjC_callback_function PyObjCFFI_MakeFunctionClosure(PyObjCMethodSignature* methinfo, PyObject* callable);

#endif /* PyObjC_FFI_SUPPORT_H */
