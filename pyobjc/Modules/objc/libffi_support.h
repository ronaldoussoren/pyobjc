#ifndef PyObjC_FFI_SUPPORT_H
#define PyObjC_FFI_SUPPORT_H

#include "ffi.h"

typedef void (*PyObjCFFI_ClosureFunc)(ffi_cif*, void*, void**, void*);

void PyObjCFFI_FreeCIF(ffi_cif* cif);
ffi_cif* PyObjCFFI_CIFForSignature(PyObjCMethodSignature* signature);
IMP PyObjCFFI_MakeClosure(PyObjCMethodSignature* signature,
			PyObjCFFI_ClosureFunc func, void* userdata);
void* PyObjCFFI_FreeClosure(IMP closure);

IMP PyObjCFFI_MakeIMPForSignature(char* signature, PyObject* callable);
IMP PyObjCFFI_MakeIMPForPyObjCSelector(PyObjCSelector *aSelector);
PyObject *PyObjCFFI_Caller(PyObject *aMeth, PyObject* self, PyObject *args);

int PyObjCFFI_CountArguments(
	PyObjCMethodSignature* methinfo, Py_ssize_t argOffset, 
	Py_ssize_t* byref_in_count,
	Py_ssize_t* byref_out_count,
	Py_ssize_t* plain_count,
	Py_ssize_t* argbuf_len);

int PyObjCFFI_ParseArguments(
	PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
	PyObject* args, Py_ssize_t argbuf_cur, unsigned char* argbuf,
	void** byref,
	ffi_type** arglist, void** values);

PyObject* PyObjCFFI_BuildResult(
	PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
	void* pRetval, void** byref, Py_ssize_t byref_out_count,
	PyObject* self, int flags);

#endif /* PyObjC_FFI_SUPPORT_H */
