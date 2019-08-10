#include "pyobjc.h"

static PyObject*
call_NSData_bytes(PyObject* method, PyObject* self, PyObject* arguments)
{
    const void* bytes;
    NSUInteger bytes_len;
    PyObject* result;
    struct objc_super super;

    if (!PyArg_ParseTuple(arguments, "")) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            objc_superSetReceiver(super, PyObjCObject_GetObject(self));
            objc_superSetClass(super, PyObjCSelector_GetClass(method));
            bytes = ((void* (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method));
            bytes_len = ((NSUInteger(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, @selector(length));

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            result = NULL;
            bytes = NULL;
            bytes_len = 0;
        }
    Py_END_ALLOW_THREADS

    if (bytes == NULL && PyErr_Occurred())
        return NULL;

    if (bytes == NULL) {
        /* Creating a memory view with a NULL pointer will
         * fail in 3.4 (and possibly earlier), use a
         * bytes object instead.
         */
        return PyBytes_FromStringAndSize("", 0);
    }

    /* 2.7 or later: use a memory view */
    Py_buffer info;
    if (PyBuffer_FillInfo(&info, self, (void*)bytes, bytes_len, 1, PyBUF_FULL_RO) < 0) {
        return NULL;
    }
    result = PyMemoryView_FromBuffer(&info);

    return result;
}

static void
imp_NSData_bytes(ffi_cif* cif __attribute__((__unused__)), void* resp, void** args,
                 void* callable)
{
    id self = *(id*)args[0];
    // SEL _meth = *(SEL*)args[1];
    void** pretval = (void**)resp;

    PyObject* result;
    PyObject* arglist = NULL;
    PyObject* pyself = NULL;
    int cookie = 0;

    PyGILState_STATE state = PyGILState_Ensure();

    arglist = PyTuple_New(1);
    if (arglist == NULL)
        goto error;

    pyself = PyObjCObject_NewTransient(self, &cookie);
    if (pyself == NULL)
        goto error;
    PyTuple_SetItem(arglist, 0, pyself);
    Py_INCREF(pyself);

    result = PyObject_Call((PyObject*)callable, arglist, NULL);
    Py_DECREF(arglist);
    arglist = NULL;
    PyObjCObject_ReleaseTransient(pyself, cookie);
    pyself = NULL;
    if (result == NULL)
        goto error;

    if (result == Py_None) {
        *pretval = NULL;
        Py_DECREF(result);
        PyGILState_Release(state);
        return;
    }

    {
        OCReleasedBuffer* temp = [[OCReleasedBuffer alloc] initWithPythonBuffer:result
                                                                       writable:NO];
        if (temp == nil) {
            *pretval = NULL;
            goto error;
        }
        [temp autorelease];
        *pretval = [temp buffer];
        PyGILState_Release(state);
    }
    return;

error:
    Py_XDECREF(arglist);
    if (pyself) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }
    PyObjCErr_ToObjCWithGILState(&state);
    *pretval = NULL;
}

static PyObject*
call_NSMutableData_mutableBytes(PyObject* method, PyObject* self, PyObject* arguments)
{
    void* bytes;
    NSUInteger bytes_len;
    PyObject* result;
    struct objc_super super;

    if (!PyArg_ParseTuple(arguments, "")) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            objc_superSetReceiver(super, PyObjCObject_GetObject(self));
            objc_superSetClass(super, PyObjCSelector_GetClass(method));

            bytes = ((void* (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method));
            bytes_len = ((NSUInteger(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, @selector(length));

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            result = NULL;
            bytes = NULL;
            bytes_len = 0;
        }
    Py_END_ALLOW_THREADS

    if (bytes == NULL && PyErr_Occurred())
        return NULL;

    if (bytes == NULL) {
        /* PyMemoryView doesn't like null pointers, and those
         * are nonsensical here anyway.
         */
        PyErr_SetString(PyExc_ValueError, "NULL pointer in NSMutableData");
        return NULL;
    }

    /* 2.7 or later: use a memory view */
    Py_buffer info;
    if (PyBuffer_FillInfo(&info, self, bytes, bytes_len, 0, PyBUF_FULL) < 0) {
        return NULL;
    }
    result = PyMemoryView_FromBuffer(&info);

    return result;
}

static void
imp_NSMutableData_mutableBytes(ffi_cif* cif __attribute__((__unused__)), void* resp,
                               void** args, void* callable)
{
    id self = *(id*)args[0];
    // SEL _meth = *(SEL*)args[1];
    void** pretval = (void**)resp;
    PyObject* result;
    PyObject* arglist = NULL;
    PyObject* pyself = NULL;
    int cookie = 0;

    PyGILState_STATE state = PyGILState_Ensure();

    arglist = PyTuple_New(1);
    if (arglist == NULL)
        goto error;

    pyself = PyObjCObject_NewTransient(self, &cookie);
    if (pyself == NULL)
        goto error;
    PyTuple_SetItem(arglist, 0, pyself);
    Py_INCREF(pyself);

    result = PyObject_Call((PyObject*)callable, arglist, NULL);
    Py_DECREF(arglist);
    arglist = NULL;
    PyObjCObject_ReleaseTransient(pyself, cookie);
    pyself = NULL;
    if (result == NULL)
        goto error;

    if (result == Py_None) {
        *pretval = NULL;
        Py_DECREF(result);
        PyGILState_Release(state);
        return;
    }

    OCReleasedBuffer* temp = [[OCReleasedBuffer alloc] initWithPythonBuffer:result
                                                                   writable:YES];
    if (temp == nil) {
        *pretval = NULL;
        goto error;
    }
    [temp autorelease];
    *pretval = [temp buffer];
    PyGILState_Release(state);
    return;

error:
    Py_XDECREF(arglist);
    if (pyself) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }
    *pretval = NULL;
    PyObjCErr_ToObjCWithGILState(&state);
}

int
PyObjC_setup_nsdata(void)
{
    Class classNSData = objc_lookUpClass("NSData");
    Class classNSMutableData = objc_lookUpClass("NSMutableData");

    if (classNSData != NULL) {

        if (PyObjC_RegisterMethodMapping(classNSData, @selector(bytes), call_NSData_bytes,
                                         imp_NSData_bytes) < 0) {
            return -1;
        }
    }

    if (classNSMutableData != NULL) {

        if (PyObjC_RegisterMethodMapping(classNSMutableData, @selector(mutableBytes),
                                         call_NSMutableData_mutableBytes,
                                         imp_NSMutableData_mutableBytes) < 0) {
            return -1;
        }
    }

    return 0;
}
