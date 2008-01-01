#ifndef PyObjC_FFI_SUPPORT_H
#define PyObjC_FFI_SUPPORT_H

#ifdef WITH_SYSTEM_FFI
#include <ffi/ffi.h>
#else
#include "ffi.h"
#endif

#ifndef FFI_CLOSURES
#    error "Need FFI_CLOSURES!"
#endif

struct byref_attr {
	int       token;
	PyObject* buffer;
};

typedef void (*PyObjCFFI_ClosureFunc)(ffi_cif*, void*, void**, void*);

void PyObjCFFI_FreeCIF(ffi_cif* cif);
ffi_cif* PyObjCFFI_CIFForSignature(PyObjCMethodSignature* signature);
IMP PyObjCFFI_MakeClosure(PyObjCMethodSignature* signature,
			PyObjCFFI_ClosureFunc func, void* userdata);
void* PyObjCFFI_FreeClosure(IMP closure);

IMP PyObjCFFI_MakeIMPForSignature(PyObjCMethodSignature* methinfo, PyObject* callable);
IMP PyObjCFFI_MakeIMPForPyObjCSelector(PyObjCSelector *aSelector);
PyObject *PyObjCFFI_Caller(PyObject *aMeth, PyObject* self, PyObject *args);
void PyObjCFFI_FreeIMP(IMP imp);


int PyObjCFFI_CountArguments(
	PyObjCMethodSignature* methinfo, Py_ssize_t argOffset, 
	Py_ssize_t* byref_in_count,
	Py_ssize_t* byref_out_count,
	Py_ssize_t* plain_count,
	Py_ssize_t* argbuf_len,
	BOOL* havePrintf);

int PyObjCFFI_ParseArguments(
	PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
	PyObject* args, Py_ssize_t argbuf_cur, unsigned char* argbuf, Py_ssize_t argbuf_len,
	void** byref, struct byref_attr* byref_attr,
	ffi_type** arglist, void** values,
	BOOL allArgsPresent);

PyObject* PyObjCFFI_BuildResult(
	PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
	void* pRetval, void** byref, struct byref_attr* byref_attr, 
	Py_ssize_t byref_out_count,
	PyObject* self, int flags, void** argvalues);

int PyObjCFFI_AllocByRef(int argcount, void*** byref, struct byref_attr** byref_attr);
int PyObjCFFI_FreeByRef(int argcount, void** byref, struct byref_attr* byref_attr);

/* XXX: rename me */
ffi_type* signature_to_ffi_return_type(const char* argtype);


typedef void (*PyObjC_callback_function)(void);
PyObjC_callback_function PyObjCFFI_MakeFunctionClosure(PyObjCMethodSignature* methinfo, PyObject* callable);


#endif /* PyObjC_FFI_SUPPORT_H */
