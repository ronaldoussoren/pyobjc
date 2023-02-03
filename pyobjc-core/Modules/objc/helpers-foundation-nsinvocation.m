#include "pyobjc.h"

static PyObject*
call_NSInvocation_setArgument_atIndex_(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    NSMethodSignature* signature;
    const char*        tp;
    PyObject*          py_value;
    NSUInteger         index;
    void*              buf;
    Py_ssize_t         sz;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1) {
        return NULL;
    }
    py_value = arguments[0];
    if (depythonify_c_value(@encode(NSUInteger), arguments[1], &index) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

            tp = [signature getArgumentTypeAtIndex:index];

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            signature = NULL;
            tp        = NULL;
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    sz = PyObjCRT_SizeOfType(tp);
    if (sz == -1) {
        return NULL;
    }

    buf = PyMem_Malloc(sz);
    if (buf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    if (depythonify_c_value(tp, py_value, buf) == -1) {
        PyMem_Free(buf);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                ((void (*)(id, SEL, void*, NSUInteger))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), buf,
                    index);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, void*, NSUInteger))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), buf, index);
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(buf);

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
call_NSInvocation_setReturnValue_(PyObject* method, PyObject* self,
                                  PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    NSMethodSignature* signature;
    const char*        tp;
    PyObject*          py_value;
    void*              buf;
    Py_ssize_t         sz;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }
    py_value = arguments[0];

    Py_BEGIN_ALLOW_THREADS
        @try {
            signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

            tp = [signature methodReturnType];

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            signature = NULL;
            tp        = NULL;
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    sz = PyObjCRT_SizeOfType(tp);
    if (sz == -1) {
        return NULL;
    }

    buf = PyMem_Malloc(sz);
    if (buf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    if (depythonify_c_value(tp, py_value, buf) == -1) {
        PyMem_Free(buf);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                ((void (*)(id, SEL, void*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), buf);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, void*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), buf);
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(buf);

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
call_NSInvocation_getArgument_atIndex_(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    NSMethodSignature* signature;
    const char*        tp;
    PyObject*          py_value;
    NSUInteger         index;
    void*              buf;
    Py_ssize_t         sz;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1) {
        return NULL;
    }
    py_value = arguments[0];
    if (depythonify_c_value(@encode(NSUInteger), arguments[1], &index) == -1) {
        return NULL;
    }
    if (py_value != Py_None) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

            tp = [signature getArgumentTypeAtIndex:index];

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            signature = NULL;
            tp        = NULL;
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    sz = PyObjCRT_SizeOfType(tp);
    if (sz == -1) {
        return NULL;
    }

    buf = PyMem_Malloc(sz);
    if (buf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                ((void (*)(id, SEL, void*, NSUInteger))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), buf,
                    index);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, void*, NSUInteger))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), buf, index);
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        PyMem_Free(buf);
        return NULL;
    }

    py_value = pythonify_c_value(tp, buf);
    PyMem_Free(buf);
    if (py_value == NULL) {
        return NULL;
    }

    return py_value;
}

static PyObject*
call_NSInvocation_getReturnValue_(PyObject* method, PyObject* self,
                                  PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    NSMethodSignature* signature;
    const char*        tp;
    PyObject*          py_value;
    void*              buf;
    Py_ssize_t         sz;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }
    py_value = arguments[0];

    if (py_value != Py_None) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

            tp = [signature methodReturnType];

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            signature = NULL;
            tp        = NULL;
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    sz = PyObjCRT_SizeOfType(tp);
    if (sz == -1) {
        return NULL;
    }

    buf = PyMem_Malloc(sz);
    if (buf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                ((void (*)(id, SEL, void*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), buf);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, void*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), buf);
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        PyMem_Free(buf);
        return NULL;
    }

    py_value = pythonify_c_value(tp, buf);
    PyMem_Free(buf);
    if (py_value == NULL) {
        return NULL;
    }

    return py_value;
}

int
PyObjC_setup_nsinvocation(PyObject* module __attribute__((__unused__)))
{
    Class classNSInvocation = objc_lookUpClass("NSInvocation");

    if (PyObjC_RegisterMethodMapping(classNSInvocation, @selector(setArgument:atIndex:),
                                     call_NSInvocation_setArgument_atIndex_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSInvocation, @selector(setReturnValue:),
                                     call_NSInvocation_setReturnValue_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSInvocation, @selector(getArgument:atIndex:),
                                     call_NSInvocation_getArgument_atIndex_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSInvocation, @selector(getReturnValue:),
                                     call_NSInvocation_getReturnValue_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {
        return -1;
    }

    return 0;
}
