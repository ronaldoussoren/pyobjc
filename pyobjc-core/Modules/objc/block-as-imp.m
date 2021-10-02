/*
 * Use `imp_implementationWithBlock` to create
 * method IMP's for selectors that have a specific
 * method signature.
 *
 * Add commonly implemented signatures to this file,
 * esp. for performance critical methods.
 *
 * XXX: Something similar can be done for common
 *      kinds of blocks!
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static id create_void_noargs(PyObject* callable, PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id) = ^(id _Nullable self) {
            PyGILState_STATE state = PyGILState_Ensure();

            int cookie;
            PyObject* pyself = PyObjCObject_NewTransient(self, &cookie);

            PyObject* args[2] = { NULL, pyself };
            PyObject* result = PyObject_Vectorcall(callable, args+1, 1|PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
            if (result == NULL) goto error;
            Py_DECREF(result);

            /* XXX: move check in function/macro for easier reuse */
            if (result != Py_None) {
                PyErr_Format(PyExc_ValueError,
                     "%R: void return, but did return a value",
                     callable);
                goto error;
            }


            PyObjCObject_ReleaseTransient(pyself, cookie);
            PyGILState_Release(state);
            return;

        error:
            if (pyself) {
                PyObjCObject_ReleaseTransient(pyself, cookie);
            }
            PyObjCErr_ToObjCWithGILState(&state);
    };

    return [block copy];
}

static id create_id_noargs(PyObject* callable, PyObjCMethodSignature* methinfo)
{
    BOOL already_retained = methinfo->rettype->alreadyRetained;
    BOOL already_cfretained = methinfo->rettype->alreadyCFRetained;

    Py_INCREF(callable);

    id _Nullable (^block)(id _Nullable ) = ^(id _Nullable self) {
            PyGILState_STATE state = PyGILState_Ensure();

            int cookie;
            PyObject* pyself = PyObjCObject_NewTransient(self, &cookie);

            PyObject* args[2] = { NULL, pyself };
            PyObject* result = PyObject_Vectorcall(callable, args+1, 1|PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
            if (result == NULL) goto error;

            id oc_result = nil;
            if (depythonify_python_object(result, &oc_result) == -1) {
                goto error;
            }
            if (already_retained) {
                /* Must return a 'new' instead of a borrowed
                 * reference.
                 */
                [oc_result retain];

            } else if (already_cfretained) {
                /* Must return a 'new' instead of a borrowed
                 * reference.
                 */
                CFRetain(oc_result);

            } else if (Py_REFCNT(result) == 1) {
                /* make sure return value doesn't die before
                 * the caller can get its hands on it.
                 */
                [[oc_result retain] autorelease];
            }
            PyObjCObject_ReleaseTransient(pyself, cookie);
            PyGILState_Release(state);
            return oc_result;

        error:
            if (pyself) {
                PyObjCObject_ReleaseTransient(pyself, cookie);
            }
            PyObjCErr_ToObjCWithGILState(&state);
    };

    return [block copy];
}

static struct block_generator {
   const char* typestr;
   id (*creator)(PyObject*, PyObjCMethodSignature*);
} registry[] = {
    /* XXX: After testing add variants with 1 and 2  arguments as well */
    /* XXX: Also: drawRect (and variants) */
   { "v@:", create_void_noargs },
   { "@@:", create_id_noargs },

   { NULL, NULL }
};


IMP _Nullable blockimpForSignature(SEL sel, const char* typestr, PyObject* callable, PyObjCMethodSignature* methinfo)
{
   PyObjC_Assert(callable != NULL, NULL);
   PyObjC_Assert(typestr != NULL, NULL);

    if (validate_callable_signature(callable, sel, methinfo) == -1) {
        return NULL;
    }


   /* XXX: Linear search should be acceptable here */
   for (struct block_generator* cur = registry; cur->typestr != NULL; cur++) {
       if (strcmp(typestr, cur->typestr) != 0) continue;

       id block = cur->creator(callable, methinfo);
       return imp_implementationWithBlock(block);
   }

   return NULL;
}

NS_ASSUME_NONNULL_END
