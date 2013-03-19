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
typedef void (*PyObjC_callback_function)(void);
typedef void (*PyObjCBlockFunction)(void*, ...);

extern int PyObjCRT_ResultUsesStret(const char*);
extern void PyObjCFFI_FreeCIF(ffi_cif*);
extern ffi_cif* PyObjCFFI_CIFForSignature(PyObjCMethodSignature*);
extern IMP PyObjCFFI_MakeClosure(PyObjCMethodSignature*, PyObjCFFI_ClosureFunc, void*);
extern void* PyObjCFFI_FreeClosure(IMP);
extern IMP PyObjCFFI_MakeIMPForSignature(PyObjCMethodSignature*, SEL, PyObject*);
extern IMP PyObjCFFI_MakeIMPForPyObjCSelector(PyObjCSelector*);
extern PyObject *PyObjCFFI_Caller(PyObject*, PyObject*, PyObject*);
extern void PyObjCFFI_FreeIMP(IMP);
extern PyObjCBlockFunction PyObjCFFI_MakeBlockFunction(PyObjCMethodSignature*, PyObject*);
extern void PyObjCFFI_FreeBlockFunction(PyObjCBlockFunction);
extern int PyObjCFFI_CountArguments(
    PyObjCMethodSignature*, Py_ssize_t, Py_ssize_t*,
    Py_ssize_t*, Py_ssize_t*, Py_ssize_t*, BOOL*);
extern Py_ssize_t PyObjCFFI_ParseArguments(
    PyObjCMethodSignature*, Py_ssize_t, PyObject*, Py_ssize_t, unsigned char*, Py_ssize_t,
    void**, struct byref_attr*, ffi_type**, void**);
extern PyObject* PyObjCFFI_BuildResult(
    PyObjCMethodSignature*, Py_ssize_t argOffset, void* pRetval, void**,
    struct byref_attr*byref_attr, Py_ssize_t, PyObject*, int, void**);
extern int PyObjCFFI_AllocByRef(Py_ssize_t, void***, struct byref_attr**);
extern int PyObjCFFI_FreeByRef(Py_ssize_t, void**, struct byref_attr*);
extern ffi_type* PyObjCFFI_Typestr2FFI(const char*);
extern PyObjC_callback_function PyObjCFFI_MakeFunctionClosure(PyObjCMethodSignature*, PyObject*);

#endif /* PyObjC_FFI_SUPPORT_H */
