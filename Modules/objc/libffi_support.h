#ifndef PyObjC_FFI_SUPPORT_H
#define PyObjC_FFI_SUPPORT_H

#include "ffi.h"

typedef void (*PyObjCFFI_ClosureFunc)(ffi_cif*, void*, void**, void*);

void PyObjCFFI_FreeCIF(ffi_cif* cif);
ffi_cif* PyObjCFFI_CIFForSignature(PyObjCMethodSignature* signature, int* pArgOffset);
IMP PyObjCFFI_MakeClosure(PyObjCMethodSignature* signature,
			PyObjCFFI_ClosureFunc func, void* userdata);
void* PyObjCFFI_FreeClosure(IMP closure);

IMP PyObjCFFI_MakeIMPForSignature(char* signature, PyObject* callable);
IMP PyObjCFFI_MakeIMPForPyObjCSelector(PyObjCSelector *aSelector);
PyObject *PyObjCFFI_Caller(PyObject *aMeth, PyObject* self, PyObject *args);

#endif /* PyObjC_FFI_SUPPORT_H */
