/*
 * alloc_hack.m -- Implementation of alloc_hack.h
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable call_NSObject_alloc(PyObject* method, PyObject* self,
                                               PyObject* const* arguments
                                               __attribute__((__unused__)),
                                               size_t nargs)
{
    id                result = nil;
    struct objc_super spr;
    IMP               anIMP;
    Class             aClass;
    SEL               aSel;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    /* objc.selector and friends already check this */
    /* XXX: No they don't, class methods can be accessed through
     *      instances for Python subclasses...
     */
    // assert(PyObjCClass_Check(self));

    if (unlikely(PyObjCIMP_Check(method))) {
        anIMP = PyObjCIMP_GetIMP(method);

        if (PyObjCClass_Check(self)) {
            aClass = PyObjCClass_GetClass(self);
        } else {
            aClass = object_getClass(PyObjCObject_GetObject(self));
        }

        aSel = PyObjCIMP_GetSelector(method);

        Py_BEGIN_ALLOW_THREADS
            @try {
                result = ((id(*)(Class, SEL))anIMP)(aClass, aSel);

            } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
                PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
                result = nil;
            }
        Py_END_ALLOW_THREADS

    } else {
        spr.super_class = (Class _Nonnull)object_getClass(PyObjCSelector_GetClass(method));
        if (PyObjCClass_Check(self)) { // LCOV_BR_EXCL_LINE
            spr.receiver = (id _Nonnull)PyObjCClass_GetClass(self);
        } else {
            /* It is not possible to resolve class methods through an instance */
            // LCOV_EXCL_START
            spr.receiver = (id _Nonnull)object_getClass(PyObjCObject_GetObject(self));
            // LCOV_EXCL_STOP
        }
        aSel = PyObjCSelector_GetSelector(method);

        Py_BEGIN_ALLOW_THREADS
            @try {
                result = ((id(*)(struct objc_super*, SEL))objc_msgSendSuper)(&spr, aSel);

            } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
                PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
                result = nil;
            }
        Py_END_ALLOW_THREADS
    }

    if (unlikely(result == nil && PyErr_Occurred())) {
        return NULL;
    }

    if (result == nil) {
        Py_RETURN_NONE;
    }

    PyObject* rval = PyObjC_FindPythonProxy(result);
    if (rval != NULL) {
        /* Found an existing proxy
         * Compensate for the +1 retainCount from +alloc
         */
        if (object_getClass(result) != NSAutoreleasePool_class) { // LCOV_BR_EXCL_LINE
            [result release];
        }
        return rval;
    }

    /* The 'NO' ensures that the proxy object doesn't retain, which
     * compensates for the +1 from +alloc
     */
    rval =  PyObjCObject_New(result, PyObjCObject_kDEFAULT, NO);
    if (rval == NULL) { // LCOV_BR_EXCL_LINE
        return rval; // LCOV_EXCL_LINE
    }

    PyObject* actual = PyObjC_RegisterPythonProxy(result, rval);
    Py_DECREF(rval);
    return actual;
}

static IMP
mkimp_NSObject_alloc(PyObject*              callable,
                     PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);
    id (^block)(id) = ^(Class _Nullable self) {
      id        rv = nil;
      int       err;
      PyObject* v      = NULL;
      PyObject* result = NULL;

      PyObjC_BEGIN_WITH_GIL

          v = id_to_python(self);
          if (unlikely(v == NULL)) { // LCOV_BR_EXCL_LINE
              PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
          } // LCOV_EXCL_LINE
          v = PyObjC_AdjustSelf(v);
          if (unlikely(v == NULL)) { // LCOV_BR_EXCL_LINE
              PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
          } // LCOV_EXCL_LINE

          PyObject* args[2] = {NULL, v};
          result            = PyObject_Vectorcall((PyObject*)callable, args + 1,
                                                  1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);

          Py_CLEAR(v);
          if (unlikely(result == NULL)) {
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE

          err = depythonify_python_object(result, &rv);
          if (unlikely(err == -1)) {
              Py_DECREF(result);
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE

          [rv retain];
          Py_DECREF(result);

      PyObjC_END_WITH_GIL

      /* +alloc returns a +1 reference */
      return rv;
    };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSObject_dealloc(PyObject* method, PyObject* self,
                                                 PyObject* const* arguments
                                                 __attribute__((__unused__)),
                                                 size_t nargs)
{
    struct objc_super spr;
    IMP               anIMP;
    NSObject*         anInstance;
    SEL               aSel;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    /* objc.selector and friends already check this */
    assert(PyObjCObject_Check(self));

    if (unlikely(PyObjCIMP_Check(method))) {
        anIMP      = PyObjCIMP_GetIMP(method);
        anInstance = PyObjCObject_GetObject(self);
        aSel       = PyObjCIMP_GetSelector(method);

        Py_BEGIN_ALLOW_THREADS
            @try {
                ((void (*)(id, SEL))anIMP)(anInstance, aSel); // LCOV_BR_EXCL_LINE

            } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
                PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
            }
        Py_END_ALLOW_THREADS

    } else {
        spr.super_class = PyObjCSelector_GetClass(method);
        spr.receiver    = PyObjCObject_GetObject(self);
        aSel            = PyObjCSelector_GetSelector(method);

        Py_BEGIN_ALLOW_THREADS
            @try {
                ((void (*)(struct objc_super*, SEL))objc_msgSendSuper)(&spr, aSel);

            } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
                PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
            }
        Py_END_ALLOW_THREADS
    }

    /* After the call to dealloc the 'objc_object' value is garbage,
     * ensure that there's still a valid reference until the proxy is
     * deallocated.
     */
    PyObjC_UnregisterPythonProxy(((PyObjCObject*)self)->objc_object, self);
    if (!(((PyObjCObject*)self)->flags & PyObjCObject_kSHOULD_NOT_RELEASE)) {
        [NSNull_null retain];
    }
    ((PyObjCObject*)self)->objc_object = NSNull_null;

    if (unlikely(PyErr_Occurred())) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_NSObject_dealloc(PyObject*              callable,
                       PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id) = ^(Class _Nullable self) {
      PyObject* pyself = NULL;
      PyObject* result = NULL;
      int       cookie;

      PyObjC_BEGIN_WITH_GIL
          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) { // LCOV_BR_EXCL_LINE
              PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
          } // LCOV_EXCL_LINE

          PyObject* args[2] = {NULL, pyself};
          result            = PyObject_Vectorcall(callable, args + 1,
                                                  1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          PyObjCObject_ReleaseTransient(pyself, cookie);
          if (result == NULL) {
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE

          if (unlikely(result != Py_None)) {
              PyErr_Format(PyExc_TypeError,
                           "dealloc should return None, returned instance"
                           " of %s",
                           Py_TYPE(result)->tp_name);
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE

          Py_DECREF(result);

      PyObjC_END_WITH_GIL
    };
    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_NSObject_release(PyObject* method, PyObject* self,
                                                 PyObject* const* arguments
                                                 __attribute__((__unused__)),
                                                 size_t nargs)
{
    struct objc_super spr;
    IMP               anIMP;
    id                anInstance;
    SEL               aSel;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    /* objc.selector and friends already check this */
    assert(PyObjCObject_Check(self));

    if (unlikely(PyObjCIMP_Check(method))) {
        anIMP      = PyObjCIMP_GetIMP(method);
        anInstance = PyObjCObject_GetObject(self);
        aSel       = PyObjCIMP_GetSelector(method);

        Py_BEGIN_ALLOW_THREADS
            @try {
                ((void (*)(id, SEL))anIMP)(anInstance, aSel);

            } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
                PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
            }
        Py_END_ALLOW_THREADS

    } else {
        spr.super_class = PyObjCSelector_GetClass(method);
        spr.receiver    = PyObjCObject_GetObject(self);
        aSel            = PyObjCSelector_GetSelector(method);

        Py_BEGIN_ALLOW_THREADS
            @try {
                ((void (*)(struct objc_super*, SEL))objc_msgSendSuper)(&spr, aSel);

            } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
                PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
            }
        Py_END_ALLOW_THREADS
    }

    if (unlikely(PyErr_Occurred())) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static PyObject* _Nullable call_NSObject_retain(PyObject* method, PyObject* self,
                                                PyObject* const* arguments
                                                __attribute__((__unused__)),
                                                size_t nargs)
{
    struct objc_super spr;
    IMP               anIMP;
    id                anInstance;
    SEL               aSel;
    id                retval = nil;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    /* objc.selector and friends already check this */
    assert(PyObjCObject_Check(self));

    /*
     * XXX:
     * The code below does not release the GIL to fix a problem
     * with test_nsobject.py, which would hang the interpreter
     * otherwise. I'm not sure yet what the root cause of that
     * hang is.
     */
    if (PyObjCIMP_Check(method)) {
        anIMP      = PyObjCIMP_GetIMP(method);
        anInstance = PyObjCObject_GetObject(self);
        aSel       = PyObjCIMP_GetSelector(method);

        // Py_BEGIN_ALLOW_THREADS
        @try {
            retval = ((id(*)(id, SEL))anIMP)(anInstance, aSel);

        } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
        // Py_END_ALLOW_THREADS

    } else {
        spr.super_class = PyObjCSelector_GetClass(method);
        spr.receiver    = PyObjCObject_GetObject(self);
        aSel            = PyObjCSelector_GetSelector(method);

        // Py_BEGIN_ALLOW_THREADS
        @try {
            retval = ((id(*)(struct objc_super*, SEL))objc_msgSendSuper)(&spr, aSel);

        } @catch (NSObject* localException) { // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
        // Py_END_ALLOW_THREADS
    }

    if (PyErr_Occurred()) {
        return NULL;
    }

    return id_to_python(retval);
}

static IMP
mkimp_NSObject_release(PyObject*              callable,
                       PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);
    void (^block)(id) = ^(Class _Nullable self) {
      PyObject* result = NULL;
      PyObject* pyself;
      int       cookie;

      PyObjC_BEGIN_WITH_GIL
          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) { // LCOV_BR_EXCL_LINE
              PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
          } // LCOV_EXCL_LINE

          PyObject* args[2] = {NULL, pyself};
          result            = PyObject_Vectorcall(callable, args + 1,
                                                  1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE
          PyObjCObject_ReleaseTransient(pyself, cookie);

          if (result != Py_None) {
              PyErr_Format(PyExc_TypeError,
                           "release should return None, returned instance"
                           " of %s",
                           Py_TYPE(result)->tp_name);
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE

          Py_DECREF(result);

      PyObjC_END_WITH_GIL
    };
    return imp_implementationWithBlock(block);
}

static IMP
mkimp_NSObject_retain(PyObject*              callable,
                      PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);
    id (^block)(id) = ^(Class _Nullable self) {
      PyObject* result = NULL;
      PyObject* pyself;
      int       cookie;
      int       err;
      id        rv;

      PyObjC_BEGIN_WITH_GIL
          pyself = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) { // LCOV_BR_EXCL_LINE
              PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
          } // LCOV_EXCL_LINE

          PyObject* pyargs[2] = {NULL, pyself};
          result              = PyObject_Vectorcall(callable, pyargs + 1,
                                                    1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          PyObjCObject_ReleaseTransient(pyself, cookie);
          if (result == NULL) {
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE

          err = depythonify_python_object(result, &rv);
          Py_DECREF(result);
          if (err == -1) {
              PyObjC_GIL_FORWARD_EXC();
          } // LCOV_EXCL_LINE

      PyObjC_END_WITH_GIL
      return rv;
    };
    return imp_implementationWithBlock(block);
}

int
PyObjC_setup_nsobject(PyObject* module __attribute__((__unused__)))
{
    int r;

    r = PyObjC_RegisterMethodMapping(objc_lookUpClass("NSObject"), @selector(alloc),
                                     call_NSObject_alloc, mkimp_NSObject_alloc);
    if (r != 0)    // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    r = PyObjC_RegisterMethodMapping(objc_lookUpClass("NSObject"), @selector(dealloc),
                                     call_NSObject_dealloc, mkimp_NSObject_dealloc);
    if (r != 0)    // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    r = PyObjC_RegisterMethodMapping(objc_lookUpClass("NSObject"), @selector(retain),
                                     call_NSObject_retain, mkimp_NSObject_retain);
    if (r != 0)    // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    r = PyObjC_RegisterMethodMapping(objc_lookUpClass("NSObject"), @selector(release),
                                     call_NSObject_release, mkimp_NSObject_release);
    if (r != 0)    // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    return 0;
}

NS_ASSUME_NONNULL_END
