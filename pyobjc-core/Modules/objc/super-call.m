/*
 * super-call.m -- Finding the right dispatch function for a method-call
 *
 * This file defines a registry that is used to find the right function to
 * call when a method is called. There are 3 variants:
 *
 * - Call the method from python
 * - Call the python implementation of a method from Objective-C
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

struct registry {
    PyObjC_CallFunc         call_to_objc;
    PyObjC_MakeIMPBlockFunc make_call_to_python_block;
};

#ifdef Py_GIL_DISABLED
static PyMutex registry_mutex = {0};
#endif

/* Dict mapping from signature-string to a 'struct registry' */
static PyObject* signature_registry = (PyObject* _Nonnull)NULL;

/* Dict mapping from selector to a list of (Class, struct registry) tuples */
static PyObject* special_registry = (PyObject* _Nonnull)NULL;

/*
 * Initialize the data structures
 */
int
PyObjC_InitSuperCallRegistry(void)
{
    assert(signature_registry == NULL);
    assert(special_registry == NULL);

    signature_registry = PyDict_New();
    if (unlikely(signature_registry == NULL)) // LCOV_BR_EXCL_LINE
        return -1;                            // LCOV_EXCL_LINE

    special_registry = PyDict_New();
    if (unlikely(special_registry == NULL)) // LCOV_BR_EXCL_LINE
        return -1;                          // LCOV_EXCL_LINE

    return 0;
}

// LCOV_EXCL_START
/* The code in this file only adds new values to
 * the registry, but never clears them. Because of
 * this the capsules are never released.
 */
static void
memblock_capsule_cleanup(PyObject* ptr)
{
    void* mem = PyCapsule_GetPointer(ptr, "objc.__memblock__");

    assert(mem != NULL);
    PyMem_Free(mem);
}
// LCOV_EXCL_STOP

/*
 * Add a custom mapping for a method in a class
 */
int
PyObjC_RegisterMethodMapping(_Nullable Class class, SEL sel, PyObjC_CallFunc call_to_objc,
                             PyObjC_MakeIMPBlockFunc make_call_to_python_block)
{
    struct registry* v;
    PyObject*        pyclass;
    PyObject*        entry;
    PyObject*        lst;
    PyObject*        py_selname;
    int              r;
    int              retval = 0;

    assert(special_registry != NULL);
    assert(call_to_objc != NULL);
    assert(make_call_to_python_block != NULL);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_mutex);
#endif

#ifdef PyObjC_DEBUG
    if (unlikely(!make_call_to_python_block)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_Error,
                        "PyObjC_RegisterMethodMapping: all functions required");
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }
#endif

    py_selname = PyUnicode_FromString(sel_getName(sel));
    if (unlikely(py_selname == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }

    if (class == nil) {
        pyclass = Py_None;
        Py_INCREF(Py_None);
    } else {
        pyclass = PyObjCClass_New(class);
        if (unlikely(pyclass == NULL)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(py_selname);
            retval = -1;
            goto exit;
            // LCOV_EXCL_STOP
        }
    }

    v = PyMem_Malloc(sizeof(*v));
    if (unlikely(v == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_selname);
        Py_DECREF(pyclass);
        PyErr_NoMemory();
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }
    v->call_to_objc              = call_to_objc;
    v->make_call_to_python_block = make_call_to_python_block;

    entry = Py_BuildValue(
        "(ON)", pyclass, PyCapsule_New(v, "objc.__memblock__", memblock_capsule_cleanup));
    if (unlikely(entry == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_selname);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }

    if (unlikely(PyTuple_GET_ITEM(entry, 1) == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_selname);
        Py_DECREF(entry);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }

    r = PyDict_GetItemRef(special_registry, py_selname, &lst);

    switch (r) { // LCOV_BR_EXCL_LINE
    case -1:
        // LCOV_EXCL_START
        Py_DECREF(py_selname);
        Py_DECREF(entry);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    case 0:
        lst = PyList_New(0);
        if (unlikely(lst == NULL)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(py_selname);
            Py_DECREF(entry);
            retval = -1;
            goto exit;
            // LCOV_EXCL_STOP
        }
        if (unlikely(PyDict_SetItem( // LCOV_BR_EXCL_LINE
                         special_registry, py_selname, lst)
                     == -1)) {
            // LCOV_EXCL_START
            Py_DECREF(py_selname);
            Py_DECREF(lst);
            Py_DECREF(entry);
            retval = -1;
            goto exit;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(py_selname);

        /* case 1: fallthrough */
    }

    if (unlikely(PyList_Append(lst, entry) < 0)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(lst);
        Py_DECREF(entry);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(lst);
    Py_DECREF(entry);

    PyObjC_MappingCount += 1;

exit:
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif
    return retval;
}

int
PyObjC_RegisterSignatureMapping(char* signature, PyObjC_CallFunc call_to_objc,
                                PyObjC_MakeIMPBlockFunc make_call_to_python_block)
{
    struct registry* v;
    PyObject*        entry;
    int              r;
    int              retval = 0;

    assert(signature_registry != NULL);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_mutex);
#endif

    PyObject* key = PyBytes_FromStringAndSize(NULL, strlen(signature) + 10);
    if (unlikely(key == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }

    r = PyObjCRT_SimplifySignature(signature, PyBytes_AS_STRING(key),
                                   PyBytes_GET_SIZE(key));
    if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyErr_Format(PyObjCExc_Error, "cannot simplify signature '%s'", signature);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }

#ifdef PyObjC_DEBUG
    if (unlikely(!call_to_objc || !make_call_to_python_block)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyErr_SetString(PyObjCExc_Error,
                        "PyObjC_RegisterSignatureMapping: all functions required");
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }
#endif

    v = PyMem_Malloc(sizeof(*v));
    if (unlikely(v == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyErr_NoMemory();
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }
    v->call_to_objc              = call_to_objc;
    v->make_call_to_python_block = make_call_to_python_block;

    entry = PyCapsule_New(v, "objc.__memblock__", memblock_capsule_cleanup);
    if (unlikely(entry == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyMem_Free(v);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }

    if (unlikely( // LCOV_BR_EXCL_LINE
            _PyBytes_Resize(&key, strlen(PyBytes_AS_STRING(key)) + 1))) {
        // LCOV_EXCL_START
        Py_DECREF(entry);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }

    if (unlikely( // LCOV_BR_EXCL_LINE
            PyDict_SetItem(signature_registry, key, entry) < 0)) {
        // LCOV_EXCL_START
        Py_DECREF(key);
        Py_DECREF(entry);
        retval = -1;
        goto exit;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(key);
    Py_DECREF(entry);
    PyObjC_MappingCount += 1;

exit:
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif
    return retval;
}

/*
 * May of may not raise an exception when the return value is NULL
 */
static struct registry* _Nullable search_special(Class class, SEL sel)
{
    PyObject*  result        = NULL;
    PyObject*  special_class = NULL;
    PyObject*  search_class  = NULL;
    PyObject*  py_selname    = NULL;
    PyObject*  lst;
    Py_ssize_t i;
    int        r;

    assert(special_registry != NULL);
    assert(class != Nil);
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_mutex);
#endif

    py_selname = PyUnicode_FromString(sel_getName(sel));
    if (unlikely(py_selname == NULL)) { // LCOV_BR_EXCL_LINE
        goto error;                     // LCOV_EXCL_LINE
    }

    search_class = PyObjCClass_New(class);
    if (unlikely(search_class == NULL)) // LCOV_BR_EXCL_LINE
        goto error;                     // LCOV_EXCL_LINE

    r = PyDict_GetItemRef(special_registry, py_selname, &lst);
    switch (r) { // LCOV_BR_EXCL_LINE
    case -1:
        goto error; // LCOV_EXCL_LINE
    case 0:
        goto error;
        /* case 1: fallthrough */
    }

    /*
     * Look for the most specific match:
     * - class in the list item is either the class we're looking
     *   for, or the "closest" superclass. The list item class
     *   can be 'None', which is less specific than any other class.
     * - later items in the list with the same list item class
     *   are preferred over earlier items (those are metadata that
     *   was added later).
     */
    Py_ssize_t len = PyList_Size(lst);
    for (i = 0; i < len; i++) {
        PyObject* entry = PyList_GetItemRef(lst, i);
        if (unlikely(entry == NULL)) { // LCOV_BR_EXCL_LINE
            goto error;                // LCOV_EXCL_LINE
        }
        PyObject* pyclass = PyTuple_GET_ITEM(entry, 0);

        if (unlikely(pyclass == NULL)) { // LCOV_BR_EXCL_LINE
            Py_DECREF(entry);            // LCOV_EXCL_LINE
            continue;                    // LCOV_EXCL_LINE
        }

        if (pyclass == Py_None) {
            /* pass */
        } else if (!PyType_IsSubtype((PyTypeObject*)search_class,
                                     (PyTypeObject*)pyclass)) {
            /* Current entry is not for a superclass of search_class */
            Py_DECREF(entry);
            continue;
        } else {
            /* Current entry is for a superclass of search_class */
            if (special_class != NULL && special_class != Py_None) {
                if (!PyType_IsSubtype((PyTypeObject*)pyclass,
                                      (PyTypeObject*)special_class)) {
                    /* The new class is not more specific than the old one */
                    Py_DECREF(entry);
                    continue;
                }
            }
        }

        if (special_class == NULL) {
            /* No match yet, use */
            Py_CLEAR(special_class);
            Py_CLEAR(result);
            special_class = pyclass;
            Py_INCREF(special_class);
            result = PyTuple_GET_ITEM(entry, 1);
            Py_INCREF(result);
            Py_DECREF(entry);

        } else if (pyclass == Py_None) {
            /* Already have a match, Py_None is less specific */
            Py_DECREF(entry);
            continue;

        } else if (special_class == Py_None
                   || PyType_IsSubtype((PyTypeObject*)pyclass,
                                       (PyTypeObject*)search_class)) {
            /* special_type is a superclass of search_class,
             * but a subclass of the current match, hence it is
             * a more specific match or a similar match later in the
             * list.
             */
            Py_CLEAR(special_class);
            Py_CLEAR(result);
            special_class = pyclass;
            Py_INCREF(special_class);
            result = PyTuple_GET_ITEM(entry, 1);
            Py_INCREF(result);
            Py_DECREF(entry);
        }
    } // LCOV_BR_EXCL_LINE
    if (!result)
        goto error;

    Py_CLEAR(special_class);
    Py_CLEAR(search_class);
    Py_CLEAR(py_selname);

    struct registry* rv = PyCapsule_GetPointer(result, "objc.__memblock__");
    Py_DECREF(result);
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif
    return rv;

error:
    Py_CLEAR(special_class);
    Py_CLEAR(py_selname);
    Py_CLEAR(search_class);
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif
    return NULL;
}

static struct registry* _Nullable find_signature(const char* signature)
{
    PyObject*        o = NULL;
    int              res;
    struct registry* result = NULL;

    assert(signature_registry != NULL);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_mutex);
#endif
    PyObject* key = PyBytes_FromStringAndSize(NULL, strlen(signature) + 10);
    if (unlikely(key == NULL)) { // LCOV_BR_EXCL_LINE
        goto exit;               // LCOV_EXCL_LINE
    }

    res = PyObjCRT_SimplifySignature(signature, PyBytes_AS_STRING(key),
                                     PyBytes_GET_SIZE(key));
    if (unlikely(res == -1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyErr_Format(PyObjCExc_Error, "cannot simplify signature '%s'", signature);
        goto exit;
        // LCOV_EXCL_STOP
    }

    int r = _PyBytes_Resize(&key, strlen(PyBytes_AS_STRING(key)) + 1);
    if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
        goto exit;           // LCOV_EXCL_LINE
    }
    if (PyDict_GetItemRef(signature_registry, key, &o) != 1) {
        Py_DECREF(key);
        goto exit;
    }
    Py_DECREF(key);
    result = PyCapsule_GetPointer(o, "objc.__memblock__");
    Py_DECREF(o);

exit:
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif
    return result;
}

PyObjC_CallFunc _Nullable PyObjC_FindCallFunc(Class class, SEL sel, const char* signature)
{
    struct registry* special;
    PyObjC_CallFunc  result;

    assert(special_registry != NULL);

    special = search_special(class, sel);
    if (special) {
        result = special->call_to_objc;
    } else if (unlikely(PyErr_Occurred())) { // LCOV_BR_EXCL_LINE
        result = NULL;                       // LCOV_EXCL_LINE
    } else {                                 // LCOV_EXCL_LINE
        special = find_signature(signature);
        if (special) {
            result = special->call_to_objc;
        } else if (unlikely(PyErr_Occurred())) { // LCOV_BR_EXCL_LINE
            result = NULL;                       // LCOV_EXCL_LINE
        } else {                                 // LCOV_EXCL_LINE
            result = PyObjCFFI_Caller;
        }
    }

    if (result == &PyObjCUnsupportedMethod_Caller) {
        PyErr_Format(PyExc_TypeError, "Cannot call '%s' on instance of '%s' from Python",
                     sel_getName(sel), class_getName(class));
        result = NULL;
    }

    return result;
}

extern IMP
PyObjC_MakeIMP(Class class, PyObject* sel)
{
    struct registry*        generic;
    struct registry*        special;
    SEL                     aSelector = PyObjCSelector_GetSelector(sel);
    PyObjC_MakeIMPBlockFunc func      = NULL;
    IMP                     retval;
    PyObjCMethodSignature*  methinfo;

    methinfo = PyObjCSelector_GetMetadata(sel);
    if (unlikely(methinfo == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                  // LCOV_EXCL_LINE
    }

    /* XXX: class will always be non-Nil given the function interface */
    if (class != nil) { // LCOV_BR_EXCL_LINE
        special = search_special(class, aSelector);
        if (special) {
            func = special->make_call_to_python_block;
        } else if (unlikely(PyErr_Occurred())) { // LCOV_BR_EXCL_LINE
            Py_CLEAR(methinfo);                  // LCOV_EXCL_LINE
            return NULL;                         // LCOV_EXCL_LINE
        }
    }

    if (func == NULL) {
        generic = find_signature(methinfo->signature);
        if (generic != NULL) {
            func = generic->make_call_to_python_block;
        } else if (unlikely(PyErr_Occurred())) { // LCOV_BR_EXCL_LINE
            return NULL;                         // LCOV_EXCL_LINE
        }
    }

    if (func == PyObjCUnsupportedMethod_IMP) {
        PyErr_Format(PyExc_TypeError, "Implementing %s in Python is not supported",
                     sel_getName(aSelector));
        return NULL;
    }

    Method meth;
    if (PyObjCSelector_IsClassMethod(sel)) {
        meth = class_getClassMethod(class, PyObjCSelector_GetSelector(sel));
    } else {
        meth = class_getInstanceMethod(class, PyObjCSelector_GetSelector(sel));
    }
    if (meth) {
        const char* meth_encoding = method_getTypeEncoding(meth);
        if (unlikely(meth_encoding == NULL)) { // LCOV_BR_EXCL_LINE
            /* method_getTypeEncoding should only return NULL when
             * meth is NULL.
             */
            // LCOV_EXCL_START
            PyErr_Format(PyObjCExc_BadPrototypeError,
                         "%R cannot determine class type encoding", sel);
            return NULL;
            // LCOV_EXCL_STOP
        }

        if (!PyObjCRT_SignaturesEqual(meth_encoding,
                                      PyObjCSelector_GetNativeSignature(sel))) {

            PyErr_Format(
                PyObjCExc_BadPrototypeError,
                "%R has signature that is not compatible with ObjC runtime: %s != %s",
                sel, meth_encoding, PyObjCSelector_GetNativeSignature(sel));
            return NULL;
        }
    }

    if (func != NULL) {
        return func(sel, methinfo);
    } else {
        PyErr_Clear();

        retval =
            PyObjCFFI_MakeIMPForSignature(methinfo, PyObjCSelector_GetSelector(sel), sel);

        if (retval == NULL && PyErr_ExceptionMatches(PyExc_NotImplementedError)) {
            PyObject* exc       = NULL;
            PyObject* tp        = NULL;
            PyObject* traceback = NULL;

            PyErr_Fetch(&tp, &exc, &traceback);
            PyErr_NormalizeException(&tp, &exc, &traceback);

            Py_INCREF(exc);
            PyErr_Restore(tp, exc, traceback);

            PyErr_Format(PyExc_NotImplementedError, "Cannot generate IMP for %s",
                         sel_getName(aSelector));

            PyObject* new_exc = NULL;

            PyErr_Fetch(&tp, &new_exc, &traceback);
            PyErr_NormalizeException(&tp, &new_exc, &traceback);
            Py_INCREF(new_exc);
            PyErr_Restore(tp, new_exc, traceback);
            PyException_SetCause(new_exc, exc);
            Py_DECREF(new_exc);
        }

        return retval;
    }
}

// LCOV_EXCL_START
/* The two functions below are never called */
IMP
PyObjCUnsupportedMethod_IMP(PyObject* _Nonnull callable __attribute__((__unused__)),
                            PyObjCMethodSignature* _Nonnull methinfo
                            __attribute__((__unused__)))
{
    @throw [NSException
        exceptionWithName:NSInvalidArgumentException
                   reason:@"Implementing this method from Python is not supported"
                 userInfo:nil];
}

PyObject*
PyObjCUnsupportedMethod_Caller(PyObject* meth, PyObject* self,
                               PyObject* const* args __attribute__((__unused__)),
                               size_t           nargs __attribute__((__unused__)))
{
    SEL sel;
    if (PyObjCSelector_Check(meth)) {
        sel = PyObjCSelector_GetSelector(meth);
    } else {
        assert(PyObjCIMP_Check(meth));
        sel = PyObjCIMP_GetSelector(meth);
    }

    PyErr_Format(PyExc_TypeError, "Cannot call '%s' on '%R' from Python",
                 sel_getName(sel), self);
    return NULL;
}
// LCOV_EXCL_STOP

NS_ASSUME_NONNULL_END
