#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable call_NSData_bytes(PyObject* method, PyObject* self,
                                             PyObject* const* arguments
                                             __attribute__((__unused__)),
                                             size_t nargs)
{
    const void*       bytes;
    NSUInteger        bytes_len;
    struct objc_super super;
    Py_buffer         info;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = (id _Nonnull)PyObjCObject_GetObject(self);
            bytes             = ((void* (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method));
            bytes_len = ((NSUInteger(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, @selector(length));

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            bytes     = NULL;
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

    if (PyBuffer_FillInfo( // LCOV_BR_EXCL_LINE
            &info, self, (void*)bytes, bytes_len, 1, PyBUF_FULL_RO)
        < 0) {
        return NULL; // LCOV_EXCL_LINE
    }
    return PyMemoryView_FromBuffer(&info);
}

static IMP
mkimp_NSData_bytes(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void* (^block)(id) = ^(id _Nullable self) {
      PyObject* result;
      PyObject* pyself = NULL;
      int       cookie = 0;

      PyGILState_STATE state = PyGILState_Ensure();

      pyself = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL)
          goto error;

      PyObject* arglist[2] = {NULL, pyself};

      result = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                   1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      PyObjCObject_ReleaseTransient(pyself, cookie);
      pyself = NULL;
      if (result == NULL)
          goto error;

      if (result == Py_None) {
          Py_DECREF(result);
          PyGILState_Release(state);
          return NULL;
      }

      OCReleasedBuffer* temp = [[OCReleasedBuffer alloc] initWithPythonBuffer:result
                                                                     writable:NO];
      if (temp == nil) {
          goto error;
      }
      [temp autorelease];
      PyGILState_Release(state);
      return [temp buffer];

  error:
      PyObjCErr_ToObjCWithGILState(&state);
      return NULL;
    };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSMutableData_mutableBytes(PyObject*        method,
                                                           PyObject*        self,
                                                           PyObject* const* arguments
                                                           __attribute__((__unused__)),
                                                           size_t nargs)
{
    void*             bytes;
    NSUInteger        bytes_len;
    PyObject*         result;
    struct objc_super super;
    Py_buffer         info;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = (id _Nonnull)PyObjCObject_GetObject(self);

            bytes = ((void* (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method));
            bytes_len = ((NSUInteger(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, @selector(length));

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            result    = NULL;
            bytes     = NULL;
            bytes_len = 0;
        }
    Py_END_ALLOW_THREADS

    if (bytes == NULL && PyErr_Occurred())
        return NULL;

    if (bytes == NULL) {
        /* XXX: Requires a custom NSData subclass for to test */
        /* The selector may return NULL for empty buffers,
         * return an empty memoryview.
         *
         * XXX: The Foundation headers in the 12.1 SDK say
         *      this selector is not nullable, and hence should
         *      never by NULL.
         */
        return PyMemoryView_FromMemory("", 0, PyBUF_WRITE);
    }

    if (PyBuffer_FillInfo( // LCOV_BR_EXCL_LINE
            &info, self, bytes, bytes_len, 0, PyBUF_FULL)
        < 0) {
        return NULL; // LCOV_EXCL_LINE
    }
    result = PyMemoryView_FromBuffer(&info);

    return result;
}

static IMP
mkimp_NSMutableData_mutableBytes(PyObject* callable, PyObjCMethodSignature* methinfo
                                 __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void* (^block)(id) = ^(id _Nullable self) {
      PyObject* result;
      PyObject* pyself = NULL;
      int       cookie = 0;

      PyGILState_STATE state = PyGILState_Ensure();

      pyself = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL)
          goto error;

      PyObject* arglist[2] = {NULL, pyself};
      result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                 1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      PyObjCObject_ReleaseTransient(pyself, cookie);
      pyself = NULL;
      if (result == NULL)
          goto error;

      if (result == Py_None) {
          Py_DECREF(result);
          PyGILState_Release(state);
          return NULL;
      }

      OCReleasedBuffer* temp = [[OCReleasedBuffer alloc] initWithPythonBuffer:result
                                                                     writable:YES];
      if (temp == nil) {
          goto error;
      }
      [temp autorelease];
      PyGILState_Release(state);
      return [temp buffer];

  error:
      PyObjCErr_ToObjCWithGILState(&state);
      return NULL;
    };
    return imp_implementationWithBlock(block);
}

int
PyObjC_setup_nsdata(PyObject* module __attribute__((__unused__)))
{
    Class classNSData        = objc_lookUpClass("NSData");
    Class classNSMutableData = objc_lookUpClass("NSMutableData");

    if (classNSData != NULL) { // LCOV_BR_EXCL_LINE

        if (PyObjC_RegisterMethodMapping( // LCOV_BR_EXCL_LINE
                classNSData, @selector(bytes), call_NSData_bytes, mkimp_NSData_bytes)
            < 0) {
            return -1; // LCOV_EXCL_LINE
        }
    }

    if (classNSMutableData != NULL) { // LCOV_BR_EXCL_LINE

        if (PyObjC_RegisterMethodMapping( // LCOV_BR_EXCL_LINE
                classNSMutableData, @selector(mutableBytes),
                call_NSMutableData_mutableBytes, mkimp_NSMutableData_mutableBytes)
            < 0) {
            return -1; // LCOV_EXCL_LINE
        }
    }

    return 0;
}

NS_ASSUME_NONNULL_END
