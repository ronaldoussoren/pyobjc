#ifndef PyObjC_FFI_SUPPORT_H
#define PyObjC_FFI_SUPPORT_H

#include <ffi/ffi.h>

NS_ASSUME_NONNULL_BEGIN

#ifndef FFI_CLOSURES
#error "Need FFI_CLOSURES!"
#endif

#define MAX_ARGCOUNT 64

struct byref_attr {
    int token;
    PyObject* _Nullable obj;
    Py_buffer view;
};

#define BYREF_ATTR_INT                                                                   \
    {                                                                                    \
        0, 0,                                                                            \
        {                                                                                \
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0                                              \
        }                                                                                \
    }

typedef void (*PyObjCFFI_ClosureFunc)(ffi_cif*, void*, void* _Nullable* _Nonnull, void*);
typedef void (*PyObjC_callback_function)(void);
typedef void (*PyObjCBlockFunction)(void*, ...);

#ifndef __arm64__
extern int PyObjCRT_ResultUsesStret(const char*) __attribute__((__pure__));
#endif

extern void PyObjCFFI_FreeCIF(ffi_cif*);
extern ffi_cif* _Nullable PyObjCFFI_CIFForSignature(PyObjCMethodSignature*);
extern IMP _Nullable PyObjCFFI_MakeClosure(PyObjCMethodSignature*, PyObjCFFI_ClosureFunc,
                                           void*);
extern void* PyObjCFFI_FreeClosure(IMP);
extern IMP _Nullable PyObjCFFI_MakeIMPForSignature(PyObjCMethodSignature*, SEL,
                                                   PyObject*);
extern IMP _Nullable PyObjCFFI_MakeIMPForPyObjCSelector(PyObjCSelector*);
extern PyObject* _Nullable PyObjCFFI_Caller(PyObject*, PyObject*,
                                            PyObject* _Nonnull const* _Nonnull, size_t);
extern void PyObjCFFI_FreeIMP(IMP);
extern PyObjCBlockFunction _Nullable PyObjCFFI_MakeBlockFunction(PyObjCMethodSignature*,
                                                                 PyObject*);
extern void PyObjCFFI_FreeBlockFunction(PyObjCBlockFunction);
extern int  PyObjCFFI_CountArguments(PyObjCMethodSignature*, Py_ssize_t, Py_ssize_t*,
                                     Py_ssize_t*, Py_ssize_t*, Py_ssize_t*, BOOL*);
extern Py_ssize_t PyObjCFFI_ParseArguments(PyObjCMethodSignature*, Py_ssize_t,
                                           PyObject* _Nonnull const* _Nonnull, size_t,
                                           Py_ssize_t, unsigned char*, Py_ssize_t,
                                           void* _Nullable* _Nonnull, struct byref_attr*,
                                           ffi_type* _Nullable* _Nonnull,
                                           void* _Nullable* _Nonnull);

extern PyObject* _Nullable PyObjCFFI_BuildResult(PyObjCMethodSignature*,
                                                 Py_ssize_t argOffset, void* pRetval,
                                                 void* _Nullable* _Nonnull,
                                                 struct byref_attr* byref_attr,
                                                 Py_ssize_t, PyObject* _Nullable, int,
                                                 void* _Nullable* _Nonnull);
extern int PyObjCFFI_FreeByRef(Py_ssize_t, void* _Nullable* _Nonnull, struct byref_attr*);
extern ffi_type* _Nullable PyObjCFFI_Typestr2FFI(const char*);
extern PyObjC_callback_function _Nullable PyObjCFFI_MakeFunctionClosure(
    PyObjCMethodSignature*, PyObject*);
extern Py_ssize_t validate_callable_signature(PyObject* callable, SEL sel,
                                              PyObjCMethodSignature* methinfo);

extern int PyObjCFFI_CallUsingInvocation(IMP method, NSInvocation* invocation);

#if PY_VERSION_HEX >= 0x03090000
/*
 * "Simple" variants that reduce calling overhead for a large subset
 * of APIs.
 */
#define MAX_ARGCOUNT_SIMPLE 8
extern PyObject* _Nullable PyObjCFFI_Caller_Simple(PyObject*, PyObject*,
                                                   PyObject* _Nonnull const* _Nonnull,
                                                   size_t);
extern PyObject* _Nullable PyObjCFFI_Caller_SimpleSEL(PyObject*, PyObject*,
                                                      PyObject* _Nonnull const* _Nonnull,
                                                      size_t);

extern Py_ssize_t PyObjCFFI_ParseArguments_Simple(PyObjCMethodSignature*, Py_ssize_t,
                                                  PyObject* _Nonnull const* _Nonnull,
                                                  size_t, Py_ssize_t, unsigned char*,
                                                  Py_ssize_t, void* _Nullable* _Nonnull);
extern PyObject* _Nullable PyObjCFFI_BuildResult_Simple(PyObjCMethodSignature*, void*,
                                                        PyObject* _Nullable, int);
#endif

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FFI_SUPPORT_H */
