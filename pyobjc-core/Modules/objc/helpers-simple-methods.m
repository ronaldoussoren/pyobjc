/*
 * Highly experimental, will likely be removed
 *
 * Custom caller and IMP for simple enough method signatures,
 * similar to what's in block-as-imp.[hm]. Primarily to determine
 * which of the two has the least overhead.
 *
 * This would require a change to the internal API, and updates
 * to framework bindings, to use for real: the current API does
 * not have enough information to handler "already_retained"
 * return values (and arguments) correctly.
 */

#include "pyobjc.h"

#if 0
static PyObject*
call_void__noargs(PyObject* method, PyObject* self,
                                       PyObject*const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) return NULL;

    int isIMP = PyObjCIMP_Check(method);
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                objc_superSetReceiver(super, PyObjCObject_GetObject(self));
                objc_superSetClass(super, PyObjCSelector_GetClass(method));

                ((void (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static void
imp_void__noargs(ffi_cif* cif __attribute__((__unused__)),
                                      void* resp __attribute__((__unused__)), void** args,
                                      void* callable)
{
    id    self    = *(id*)args[0];

    PyObject* result  = NULL;
    PyObject* pyself  = NULL;
    int       cookie  = 0;

    PyGILState_STATE state = PyGILState_Ensure();

    pyself = PyObjCObject_NewTransient(self, &cookie);

    PyObject* arglist[2] = { NULL, pyself };
    result = PyObject_Vectorcall((PyObject*)callable, arglist+1, 1|PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);

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
    if (pyself != NULL) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }
    PyObjCErr_ToObjCWithGILState(&state);
}

#endif

int
PyObjC_setup_simple_methods(void)
{
    //    if (PyObjC_RegisterSignatureMapping("v@:", call_void__noargs, imp_void__noargs)
    //    == -1) return -1;
    return 0;
}
