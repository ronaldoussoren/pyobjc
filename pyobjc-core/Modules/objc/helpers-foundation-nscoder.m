#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable call_NSCoder_encodeValueOfObjCType_at_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    PyObject*         value;
    void*             buf;
    Py_ssize_t        size;
    int               err;
    struct objc_super super;
    Py_buffer         view;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (PyObject_GetBuffer(arguments[0], &view, PyBUF_CONTIG_RO) == -1) {
        return NULL;
    }

    if (!PyObjCRT_IsValidEncoding(view.buf, view.len)) {
        PyErr_SetString(PyObjCExc_InternalError, "type encoding is not valid");
        return NULL;
    }

    value = arguments[1];

    size = PyObjCRT_SizeOfType(view.buf);
    if (size == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }

    buf = PyMem_Malloc(size);
    if (buf == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyBuffer_Release(&view);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    err = depythonify_c_value(view.buf, value, buf);
    if (err == -1) {
        PyBuffer_Release(&view);
        PyMem_Free(buf);
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, char*, void*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), view.buf,
                    buf);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, char*, void*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), view.buf, buf);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(buf);
    PyBuffer_Release(&view);

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static IMP
mkimp_NSCoder_encodeValueOfObjCType_at_(PyObject*              callable,
                                        PyObjCMethodSignature* methinfo
                                        __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id, const char*, const void*) =
        ^(id _Nullable self, const char* typestr, const void* buf) {
          PyObject* result = NULL;
          PyObject* v1     = NULL;
          PyObject* v2     = NULL;
          PyObject* pyself = NULL;
          int       cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          v1 = PyBytes_FromString(typestr);
          if (v1 == NULL)
              goto error;

          v2 = pythonify_c_value(typestr, buf);
          if (v2 == NULL)
              goto error;

          PyObject* arglist[4] = {NULL, pyself, v1, v2};
          result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                     3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v1);
          v1 = NULL;
          Py_DECREF(v2);
          v2 = NULL;

          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;

          if (result == NULL)
              goto error;

          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_SetString(PyExc_TypeError, "Must return None");
              goto error;
          }

          Py_DECREF(result);
          PyGILState_Release(state);
          return;

      error:
          Py_XDECREF(v1);
          Py_XDECREF(v2);
          if (pyself != NULL) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_encodeArrayOfObjCType_count_at_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    NSUInteger        count;
    NSUInteger        i;
    Py_ssize_t        value_len;
    PyObject*         value;
    void*             buf;
    Py_ssize_t        size;
    int               err;
    struct objc_super super;
    Py_buffer         view;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (PyObject_GetBuffer(arguments[0], &view, PyBUF_CONTIG_RO) == -1) {
        return NULL;
    }
    if (!PyObjCRT_IsValidEncoding(view.buf, view.len)) {
        PyErr_SetString(PyObjCExc_InternalError, "type encoding is not valid");
        return NULL;
    }
    if (depythonify_c_value(@encode(NSUInteger), arguments[1], &count) == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }
    value = arguments[2];

    size = PyObjCRT_SizeOfType(view.buf);
    if (size == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }

    buf = PyMem_Malloc(size * (count + 1));
    if (buf == NULL) {
        PyBuffer_Release(&view);
        PyErr_NoMemory();
        return NULL;
    }

    if (!PySequence_Check(value)) {
        PyBuffer_Release(&view);
        PyMem_Free(buf);
        PyErr_SetString(PyExc_TypeError, "Need sequence of objects");
        return NULL;
    }

    value_len = PySequence_Size(value);
    if (value_len == -1) {
        PyBuffer_Release(&view);
        PyMem_Free(buf);
        return NULL;

    } else if ((NSUInteger)value_len > count) {
        PyBuffer_Release(&view);
        PyMem_Free(buf);
        PyErr_SetString(PyExc_ValueError, "Inconsistent arguments");
        return NULL;
    }

    for (i = 0; i < count; i++) {
        err = depythonify_c_value(view.buf, PySequence_GetItem(value, i),
                                  ((char*)buf) + (size * i));
        if (err == -1) {
            PyBuffer_Release(&view);
            PyMem_Free(buf);
            return NULL;
        }
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, char*, NSUInteger, void*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), view.buf,
                    count, buf);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, char*, NSUInteger,
                           void*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), view.buf, count, buf);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(buf);
    PyBuffer_Release(&view);

    if (PyErr_Occurred())
        return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

static IMP
mkimp_NSCoder_encodeArrayOfObjCType_count_at_(PyObject*              callable,
                                              PyObjCMethodSignature* methinfo
                                              __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id, const char*, NSUInteger, const void*) =
        ^(id _Nullable self, const char* typestr, NSUInteger count, const void* buf) {
          PyObject*  result = NULL;
          PyObject*  v1     = NULL;
          PyObject*  v2     = NULL;
          PyObject*  values = NULL;
          Py_ssize_t size;
          NSUInteger i;
          PyObject*  pyself = NULL;
          int        cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          size = PyObjCRT_SizeOfType(typestr);
          if (size == -1)
              goto error;

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v1 = PyBytes_FromString(typestr);
          if (v1 == NULL)
              goto error;

          v2 = PyLong_FromLong(count);
          if (v2 == NULL)
              goto error;

          values = PyTuple_New(count);
          if (values == NULL)
              goto error;

          for (i = 0; i < count; i++) {
              PyObject* v = pythonify_c_value(typestr, ((char*)buf) + (i * size));
              if (v == NULL)
                  goto error;
              PyTuple_SET_ITEM(values, i, v);
          }

          PyObject* arglist[5] = {NULL, pyself, v1, v2, values};

          result = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                       4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v1);
          v1 = NULL;
          Py_DECREF(v2);
          v2 = NULL;
          Py_DECREF(values);
          values = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;

          if (result == NULL)
              goto error;

          if (result != Py_None) {
              PyErr_SetString(PyExc_TypeError, "Must return None");
              Py_DECREF(result);
              goto error;
          }
          Py_DECREF(result);
          PyGILState_Release(state);
          return;

      error:
          Py_XDECREF(v1);
          Py_XDECREF(v2);
          Py_XDECREF(values);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_decodeValueOfObjCType_at_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    void*             buf;
    PyObject*         value;
    Py_ssize_t        size;
    struct objc_super super;
    PyObject*         py_buf;
    Py_buffer         view;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (PyObject_GetBuffer(arguments[0], &view, PyBUF_CONTIG_RO) == -1) {
        return NULL;
    }
    if (!PyObjCRT_IsValidEncoding(view.buf, view.len)) {
        PyErr_SetString(PyObjCExc_InternalError, "type encoding is not valid");
        return NULL;
    }
    py_buf = arguments[1];

    if (py_buf != Py_None) {
        PyBuffer_Release(&view);
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    size = PyObjCRT_SizeOfType(view.buf);
    if (size == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }
    buf = PyMem_Malloc(size);
    if (buf == NULL) {
        PyBuffer_Release(&view);
        PyErr_NoMemory();
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, char*, void*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), view.buf,
                    buf);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, char*, void*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), view.buf, buf);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        PyMem_Free(buf);
        PyBuffer_Release(&view);
        return NULL;
    }

    value = pythonify_c_value(view.buf, buf);
    PyMem_Free(buf);
    PyBuffer_Release(&view);
    if (value == NULL) {
        return NULL;
    }

    return value;
}

static IMP
mkimp_NSCoder_decodeValueOfObjCType_at_(PyObject*              callable,
                                        PyObjCMethodSignature* methinfo
                                        __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id, const char*, void*) =
        ^(id _Nullable self, const char* typestr, void* buf) {
          PyObject* result = NULL;
          PyObject* v      = NULL;
          int       err;
          PyObject* pyself = NULL;
          int       cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v = PyBytes_FromString(typestr);
          if (v == NULL)
              goto error;

          PyObject* arglist[4] = {NULL, pyself, v, Py_None};
          result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                     3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v);
          v = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL)
              goto error;

          err = depythonify_c_value(typestr, result, buf);
          Py_DECREF(result);
          if (err == -1)
              goto error;

          PyGILState_Release(state);
          return;

      error:
          Py_XDECREF(v);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
          return;
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_decodeValueOfObjCType_at_size_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    PyObject*         value;
    void*             buf;
    Py_ssize_t        size;
    struct objc_super super;
    PyObject*         py_buf;
    Py_buffer         view;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (PyObject_GetBuffer(arguments[0], &view, PyBUF_CONTIG_RO) == -1) {
        return NULL;
    }
    if (!PyObjCRT_IsValidEncoding(view.buf, view.len)) {
        PyErr_SetString(PyObjCExc_InternalError, "type encoding is not valid");
        return NULL;
    }
    py_buf = arguments[1];
    if (depythonify_c_value(@encode(Py_ssize_t), arguments[2], &size) == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }

    if (py_buf != Py_None) {
        PyBuffer_Release(&view);
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    buf = PyMem_Malloc(size);
    if (buf == NULL) {
        PyBuffer_Release(&view);
        PyErr_NoMemory();
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, char*, void*, NSUInteger))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), view.buf,
                    buf, size);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, char*, void*,
                           NSUInteger))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), view.buf, buf, size);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        PyBuffer_Release(&view);
        PyMem_Free(buf);
        return NULL;
    }

    value = pythonify_c_value(view.buf, buf);
    PyMem_Free(buf);
    if (value == NULL) {
        PyBuffer_Release(&view);
        return NULL;
    }

    PyBuffer_Release(&view);
    return value;
}

static IMP
mkimp_NSCoder_decodeValueOfObjCType_at_size_(PyObject*              callable,
                                             PyObjCMethodSignature* methinfo
                                             __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id, const char*, void*, NSUInteger) =
        ^(id _Nullable self, const char* typestr, void* buf, NSUInteger size) {
          PyObject* result = NULL;
          PyObject* v1     = NULL;
          PyObject* v2     = NULL;
          int       err;
          PyObject* pyself = NULL;
          int       cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v1 = PyBytes_FromString(typestr);
          if (v1 == NULL)
              goto error;

          v2 = PyLong_FromLong(size);
          if (v2 == NULL)
              goto error;

          PyObject* arglist[5] = {NULL, pyself, v1, Py_None, v2};

          result = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                       4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v1);
          v1 = NULL;
          Py_DECREF(v2);
          v2 = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL)
              goto error;

          err = depythonify_c_value(typestr, result, buf); // XXX
          Py_DECREF(result);
          if (err == -1)
              goto error;

          PyGILState_Release(state);
          return;

      error:
          Py_XDECREF(v1);
          Py_XDECREF(v2);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
          return;
        };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_decodeArrayOfObjCType_count_at_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    NSUInteger        count;
    NSUInteger        i;
    PyObject*         result;
    PyObject*         py_buf;
    void*             buf;
    Py_ssize_t        size;
    struct objc_super super;
    Py_buffer         view;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (PyObject_GetBuffer(arguments[0], &view, PyBUF_CONTIG_RO) == -1) {
        return NULL;
    }
    if (!PyObjCRT_IsValidEncoding(view.buf, view.len)) {
        PyErr_SetString(PyObjCExc_InternalError, "type encoding is not valid");
        return NULL;
    }
    if (depythonify_c_value(@encode(NSUInteger), arguments[1], &count) == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }

    py_buf = arguments[2];

    if (py_buf != Py_None) {
        PyBuffer_Release(&view);
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    size = PyObjCRT_SizeOfType(view.buf);
    if (size == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }

    buf = PyMem_Malloc(size * (count + 1));
    if (buf == NULL) {
        PyBuffer_Release(&view);
        PyErr_NoMemory();
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, char*, NSUInteger, void*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), view.buf,
                    count, buf);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, char*, NSUInteger,
                           void*))objc_msgSendSuper)(&super,
                                                     PyObjCSelector_GetSelector(method),
                                                     view.buf, (NSUInteger)count, buf);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        PyBuffer_Release(&view);
        PyMem_Free(buf);
        return NULL;
    }

    result = PyTuple_New(count);
    if (result == NULL) {
        PyBuffer_Release(&view);
        PyMem_Free(buf);
        return NULL;
    }

    for (i = 0; i < count; i++) {
        PyTuple_SET_ITEM(result, i,
                         pythonify_c_value(view.buf, ((char*)buf) + (size * i)));
        if (PyTuple_GetItem(result, i) == NULL) {
            Py_DECREF(result);
            PyMem_Free(buf);
            return NULL;
        }
    }

    PyBuffer_Release(&view);
    PyMem_Free(buf);
    return result;
}

static IMP
mkimp_NSCoder_decodeArrayOfObjCType_count_at_(PyObject*              callable,
                                              PyObjCMethodSignature* methinfo
                                              __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id, const char*, NSUInteger, void*) =
        ^(id _Nullable self, const char* typestr, NSUInteger count, void* buf) {
          PyObject*  result;
          PyObject*  v1  = NULL;
          PyObject*  v2  = NULL;
          PyObject*  seq = NULL;
          Py_ssize_t size;
          NSUInteger i;
          int        res;
          PyObject*  pyself = NULL;
          int        cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          size = PyObjCRT_SizeOfType(typestr);
          if (size == -1)
              goto error;

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v1 = PyBytes_FromString(typestr);
          if (v1 == NULL)
              goto error;

          v2 = PyLong_FromLong(count);
          if (v2 == NULL)
              goto error;

          PyObject* arglist[5] = {NULL, pyself, v1, v2, Py_None};

          result = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                       4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v1);
          v1 = NULL;
          Py_DECREF(v2);
          v2 = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL) {
              PyObjCErr_ToObjCWithGILState(&state);
              return;
          }

          seq = PySequence_Fast(result, "Return-value must be a sequence");
          Py_DECREF(result);
          if (seq == NULL)
              goto error;

          if ((NSUInteger)PySequence_Fast_GET_SIZE(seq) != count) {
              PyErr_SetString(PyExc_TypeError, "return value must be a of correct size");
              goto error;
          }

          for (i = 0; i < count; i++) {
              res = depythonify_c_value(typestr, PySequence_Fast_GET_ITEM(seq, i),
                                        ((char*)buf) + (i * size));
              if (res == -1)
                  goto error;
          }
          Py_DECREF(seq);
          PyGILState_Release(state);
          return;

      error:
          Py_XDECREF(v1);
          Py_XDECREF(v2);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          Py_XDECREF(seq);
          PyObjCErr_ToObjCWithGILState(&state);
        };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_encodeBytes_length_(PyObject*        method,
                                                            PyObject*        self,
                                                            PyObject* const* arguments,
                                                            size_t           nargs)
{
    NSUInteger length;
    Py_buffer  view;

    struct objc_super super;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value(@encode(NSUInteger), arguments[1], &length)) {
        return NULL;
    }

    if (PyObject_GetBuffer(arguments[0], &view, PyBUF_CONTIG_RO) == -1) {
        return NULL;
    }

    if (length > (size_t)view.len) {
        PyErr_Format(PyExc_ValueError,
                     "length %" PY_FORMAT_SIZE_T "d > len(buf) %" PY_FORMAT_SIZE_T "d",
                     length, view.len);
        PyBuffer_Release(&view);
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, void*, NSUInteger))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), view.buf,
                    length);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, void*, NSUInteger))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), view.buf, length);
            }
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyBuffer_Release(&view);

    if (PyErr_Occurred())
        return NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

static IMP
mkimp_NSCoder_encodeBytes_length_(PyObject* callable, PyObjCMethodSignature* methinfo
                                  __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id, const char*, NSUInteger) =
        ^(id _Nullable self, const char* bytes, NSUInteger length) {
          PyObject* result;
          PyObject* v1     = NULL;
          PyObject* v2     = NULL;
          PyObject* pyself = NULL;
          int       cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v1 = PyBytes_FromStringAndSize(bytes, length);
          if (v1 == NULL)
              goto error;

          v2 = PyLong_FromLong(length);
          if (v2 == NULL)
              goto error;

          PyObject* arglist[4] = {NULL, pyself, v1, v2};

          result = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                       3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v1);
          v1 = NULL;
          Py_DECREF(v2);
          v2 = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL)
              goto error;

          if (result != Py_None) {
              PyErr_SetString(PyExc_TypeError, "Must return None");
              Py_DECREF(result);
              goto error;
          }
          Py_DECREF(result);
          PyGILState_Release(state);
          return;

      error:
          Py_XDECREF(v1);
          Py_XDECREF(v2);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_decodeBytesWithReturnedLength_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    char*             bytes;
    NSUInteger        size = 0;
    PyObject*         v;
    PyObject*         result;
    PyObject*         py_buf;
    struct objc_super super;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    py_buf = arguments[0];

    if (py_buf != Py_None) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                bytes = ((void* (*)(id, SEL, NSUInteger*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), &size);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                bytes =
                    ((void* (*)(struct objc_super*, SEL, NSUInteger*))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), &size);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            bytes = NULL;
        }
    Py_END_ALLOW_THREADS

    if (bytes == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }

        result = PyTuple_New(2);
        if (result == NULL) {
            return NULL;
        }

        PyTuple_SET_ITEM(result, 0, Py_None);
        Py_INCREF(Py_None);

        v = pythonify_c_value(@encode(unsigned), &size);
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SET_ITEM(result, 1, v);
        return result;
    }

    result = PyTuple_New(2);
    if (result == NULL) {
        return NULL;
    }

    v = PyBytes_FromStringAndSize((char*)bytes, size);
    if (v == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    PyTuple_SET_ITEM(result, 0, v);

    v = pythonify_c_value(@encode(unsigned), &size);
    if (v == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    PyTuple_SET_ITEM(result, 1, v);

    return result;
}

static IMP
mkimp_NSCoder_decodeBytesWithReturnedLength_(PyObject*              callable,
                                             PyObjCMethodSignature* methinfo
                                             __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void* (^block)(id, NSUInteger*) = ^(id _Nullable self, NSUInteger* length) {
      PyObject* result;
      PyObject* pyself = NULL;
      int       cookie = 0;

      PyGILState_STATE state = PyGILState_Ensure();

      pyself = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL)
          goto error;

      PyObject* arglist[3] = {NULL, pyself, Py_None};
      result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      PyObjCObject_ReleaseTransient(pyself, cookie);
      pyself = NULL;
      if (result == NULL)
          goto error;

      if (!PyTuple_Check(result)) {
          Py_DECREF(result);
          PyErr_SetString(PyExc_ValueError, "Should return (bytes, length)");
          goto error;
      }

      OCReleasedBuffer* temp =
          [[OCReleasedBuffer alloc] initWithPythonBuffer:PyTuple_GET_ITEM(result, 0)
                                                writable:NO];
      Py_DECREF(result);
      if (temp == nil) {
          goto error;
      }

      *length = [temp length];

      [temp autorelease];
      PyGILState_Release(state);
      return [temp buffer];

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }
      PyObjCErr_ToObjCWithGILState(&state);
      return NULL;
    };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_decodeBytesForKey_returnedLength_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    char*             bytes;
    NSUInteger        size = 0;
    PyObject*         v;
    PyObject*         result;
    PyObject*         py_buf;
    id                key;
    struct objc_super super;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value(@encode(id), arguments[0], &key) == -1) {
        return NULL;
    }
    py_buf = arguments[1];

    if (py_buf != NULL) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                bytes = ((void* (*)(id, SEL, id, NSUInteger*))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), key,
                    (NSUInteger*)&size);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                bytes = ((void* (*)(struct objc_super*, SEL, id,
                                    NSUInteger*))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), key, &size);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            bytes = NULL;
        }
    Py_END_ALLOW_THREADS

    if (bytes == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }

        result = PyTuple_New(2);
        if (result == NULL) {
            return NULL;
        }

        PyTuple_SET_ITEM(result, 0, Py_None);
        Py_INCREF(Py_None);

        v = pythonify_c_value(@encode(unsigned), &size);
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SET_ITEM(result, 1, v);
        return result;
    }

    result = PyTuple_New(2);
    if (result == NULL) {
        return NULL;
    }

    v = PyBytes_FromStringAndSize(bytes, size);
    if (v == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    PyTuple_SET_ITEM(result, 0, v);

    v = pythonify_c_value(@encode(NSUInteger), &size);
    if (v == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    PyTuple_SET_ITEM(result, 1, v);

    return result;
}

static IMP
mkimp_NSCoder_decodeBytesForKey_returnedLength_(PyObject*              callable,
                                                PyObjCMethodSignature* methinfo
                                                __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void* (^block)(id, NSString*, NSUInteger*) =
        ^(id _Nullable self, NSString* key, NSUInteger* length) {
          PyObject*  result;
          PyObject*  v1 = NULL;
          PyObject*  v2 = NULL;
          NSUInteger len;
          PyObject*  pyself = NULL;
          int        cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v1 = id_to_python(self);
          if (v1 == NULL)
              goto error;

          v2 = id_to_python(key);
          if (v2 == NULL)
              goto error;

          PyObject* arglist[3] = {NULL, v1, v2};
          result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                     2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v1);
          v1 = NULL;
          Py_DECREF(v2);
          v2 = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL)
              goto error;

          if (!PyTuple_Check(result)) {
              Py_DECREF(result);
              PyErr_SetString(PyExc_ValueError, "Should return (bytes, length)");
              goto error;
          }

          OCReleasedBuffer* tmp =
              [[OCReleasedBuffer alloc] initWithPythonBuffer:PyTuple_GET_ITEM(result, 0)
                                                    writable:NO];
          Py_DECREF(result);
          if (tmp == nil) {
              goto error;
          }

          [tmp autorelease];

          if (depythonify_c_value(@encode(NSUInteger), PyTuple_GetItem(result, 1), &len)
              < 0) {
              goto error;
          }

          if (len < [tmp length]) {
              PyErr_SetString(PyExc_ValueError, "Should return (bytes, length)");
              goto error;
          }

          *length = len;

          PyGILState_Release(state);
          return [tmp buffer];

      error:
          Py_XDECREF(v1);
          Py_XDECREF(v2);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
          return NULL;
        };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSCoder_encodeBytes_length_forKey_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    id                key;
    struct objc_super super;
    Py_buffer         view;

#if 0
    /* XXX: This doesn't match the objective-C API (missing 'length')!
     *
     * The converted code matches the PyArg_Parse stanza and needs to be fixed
     * (with a backward compat note in the changelog)
     *
     * Plan:
     * - Make 'length' an optional argument for now (but warnings.warn about it)
     * - Document change in changelog
     * - Make length required in PyObjC 9.

     */
    if (!PyArg_ParseTuple(arguments, "y#O&", &bytes, &size, PyObjCObject_Convert, &key)) {
        return NULL;
    }
#endif

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;
    if (PyObject_GetBuffer(arguments[0], &view, PyBUF_CONTIG_RO) == -1) {
        return NULL;
    }
    if (depythonify_c_value(@encode(id), arguments[1], &key) == -1) {
        PyBuffer_Release(&view);
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, void*, NSUInteger, id))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), view.buf,
                    (NSUInteger)view.len, key);
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                ((void (*)(struct objc_super*, SEL, void*, NSUInteger,
                           id))objc_msgSendSuper)(&super,
                                                  PyObjCSelector_GetSelector(method),
                                                  view.buf, (NSUInteger)view.len, key);
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyBuffer_Release(&view);

    if (PyErr_Occurred()) {
        return NULL;
    }
    Py_INCREF(Py_None);
    return Py_None;
}

static IMP
mkimp_NSCoder_encodeBytes_length_forKey_(PyObject*              callable,
                                         PyObjCMethodSignature* methinfo
                                         __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id, const char*, NSUInteger, NSString*) =
        ^(id _Nullable self, const char* bytes, NSUInteger length, NSString* key) {
          PyObject* result;
          PyObject* v1     = NULL;
          PyObject* v2     = NULL;
          PyObject* v3     = NULL;
          PyObject* pyself = NULL;
          int       cookie = 0;

          PyGILState_STATE state = PyGILState_Ensure();

          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL)
              goto error;

          v1 = PyBytes_FromStringAndSize(bytes, length);
          if (v1 == NULL)
              goto error;

          v2 = PyLong_FromLong(length);
          if (v2 == NULL)
              goto error;

          v3 = id_to_python(key);
          if (v3 == NULL)
              goto error;

          PyObject* arglist[5] = {NULL, pyself, v1, v2, v3};
          result               = PyObject_Vectorcall((PyObject*)callable, arglist + 1,
                                                     4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          Py_DECREF(v1);
          v1 = NULL;
          Py_DECREF(v2);
          v2 = NULL;
          Py_DECREF(v3);
          v3 = NULL;
          PyObjCObject_ReleaseTransient(pyself, cookie);
          pyself = NULL;
          if (result == NULL)
              goto error;

          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_SetString(PyExc_TypeError, "Must return None");
              goto error;
          }

          Py_DECREF(result);
          PyGILState_Release(state);
          return;

      error:
          Py_XDECREF(v1);
          Py_XDECREF(v2);
          Py_XDECREF(v3);
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };
    return imp_implementationWithBlock(block);
}

int
PyObjC_setup_nscoder(PyObject* module __attribute__((__unused__)))
{
    Class classNSCoder = objc_lookUpClass("NSCoder");

    if (PyObjC_RegisterMethodMapping(classNSCoder,
                                     @selector(encodeArrayOfObjCType:count:at:),
                                     call_NSCoder_encodeArrayOfObjCType_count_at_,
                                     mkimp_NSCoder_encodeArrayOfObjCType_count_at_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder, @selector(encodeValueOfObjCType:at:),
                                     call_NSCoder_encodeValueOfObjCType_at_,
                                     mkimp_NSCoder_encodeValueOfObjCType_at_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder,
                                     @selector(decodeArrayOfObjCType:count:at:),
                                     call_NSCoder_decodeArrayOfObjCType_count_at_,
                                     mkimp_NSCoder_decodeArrayOfObjCType_count_at_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder, @selector(decodeValueOfObjCType:at:),
                                     call_NSCoder_decodeValueOfObjCType_at_,
                                     mkimp_NSCoder_decodeValueOfObjCType_at_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder,
                                     @selector(decodeValueOfObjCType:at:size:),
                                     call_NSCoder_decodeValueOfObjCType_at_size_,
                                     mkimp_NSCoder_decodeValueOfObjCType_at_size_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder, @selector(encodeBytes:length:),
                                     call_NSCoder_encodeBytes_length_,
                                     mkimp_NSCoder_encodeBytes_length_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder, @selector(encodeBytes:length:forKey:),
                                     call_NSCoder_encodeBytes_length_forKey_,
                                     mkimp_NSCoder_encodeBytes_length_forKey_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder,
                                     @selector(decodeBytesWithReturnedLength:),
                                     call_NSCoder_decodeBytesWithReturnedLength_,
                                     mkimp_NSCoder_decodeBytesWithReturnedLength_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder,
                                     @selector(decodeBytesForKey:returnedLength::),
                                     call_NSCoder_decodeBytesForKey_returnedLength_,
                                     mkimp_NSCoder_decodeBytesForKey_returnedLength_)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(
            classNSCoder, @selector(decodeBytesWithoutReturnedLength),
            PyObjCUnsupportedMethod_Caller, PyObjCUnsupportedMethod_IMP)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder, @selector(encodeValuesOfObjCTypes:),
                                     PyObjCUnsupportedMethod_Caller,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {
        return -1;
    }

    if (PyObjC_RegisterMethodMapping(classNSCoder, @selector(decodeValuesOfObjCTypes:),
                                     PyObjCUnsupportedMethod_Caller,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {
        return -1;
    }

    return 0;
}

NS_ASSUME_NONNULL_END
