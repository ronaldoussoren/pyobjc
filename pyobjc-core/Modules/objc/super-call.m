/*
 * super-call.m -- Finding the right dispatch function for a method-call
 *
 * This file defines a registry that is used to find the right function to
 * call when a method is called. There are 3 variants:
 *
 * - Call the method from python
 * - Call the python implementation of a method from Objective-C
 *
 * XXX: Add API to dump the registry for inspection.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/* XXX: Use a minimal python type instead of a capsule */
struct registry {
    PyObjC_CallFunc         call_to_objc;
    PyObjC_MakeIMPBlockFunc make_call_to_python_block;
};

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
    PyObjC_Assert(signature_registry == NULL, -1);
    PyObjC_Assert(special_registry == NULL, -1);

    signature_registry = PyDict_New();
    if (signature_registry == NULL) // LCOV_BR_EXCL_LINE
        return -1;                  // LCOV_EXCL_LINE

    special_registry = PyDict_New();
    if (special_registry == NULL) // LCOV_BR_EXCL_LINE
        return -1;                // LCOV_EXCL_LINE

    return 0;
}

static void
memblock_capsule_cleanup(PyObject* ptr)
{
    void* mem = PyCapsule_GetPointer(ptr, "objc.__memblock__");

#ifdef PyObjC_DEBUG
    if (mem == NULL)
        PyObjCErr_InternalError();
#endif

    PyMem_Free(mem);
}

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

    PyObjC_Assert(special_registry != NULL, -1);

    if (!make_call_to_python_block) {
        PyErr_SetString(PyObjCExc_Error,
                        "PyObjC_RegisterMethodMapping: all functions required");
        return -1;
    }

    if (!call_to_objc) {
        call_to_objc = PyObjCFFI_Caller;
    }

    if (class == nil) {
        pyclass = Py_None;
        Py_INCREF(Py_None);
    } else {
        pyclass = PyObjCClass_New(class);
        if (pyclass == NULL) { // LCOV_BR_EXCL_LINE
            return -1;         // LCOV_EXCL_LINE
        }
    }

    v = PyMem_Malloc(sizeof(*v));
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return -1;
        // LCOV_EXCL_STOP
    }
    v->call_to_objc              = call_to_objc;
    v->make_call_to_python_block = make_call_to_python_block;

    entry = PyTuple_New(2);
    if (entry == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(v);
        return -1;
        // LCOV_EXCL_STOP
    }

    PyTuple_SET_ITEM(entry, 0, pyclass);
    PyTuple_SET_ITEM(entry, 1,
                     PyCapsule_New(v, "objc.__memblock__", memblock_capsule_cleanup));

    if (PyTuple_GET_ITEM(entry, 1) == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(entry);
        return -1;
        // LCOV_EXCL_STOP
    }

    lst = PyDict_GetItemStringWithError(special_registry, sel_getName(sel));
    if (lst == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(entry);
        return -1;
        // LCOV_EXCL_STOP
    } else if (lst == NULL) {
        lst = PyList_New(0);
        if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
                special_registry, sel_getName(sel), lst)
            == -1) {
            // LCOV_EXCL_START
            Py_DECREF(lst);
            Py_DECREF(entry);
            return -1;
            // LCOV_EXCL_STOP
        }
    } else {
        Py_INCREF(lst);
    }

    if (PyList_Append(lst, entry) < 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(lst);
        Py_DECREF(entry);
        return -1;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(lst);
    Py_DECREF(entry);

    PyObjC_MappingCount += 1;

    return 0;
}

int
PyObjC_RegisterSignatureMapping(char* signature, PyObjC_CallFunc call_to_objc,
                                PyObjC_MakeIMPBlockFunc make_call_to_python_block)
{
    struct registry* v;
    PyObject*        entry;
    int              r;

    PyObjC_Assert(signature_registry != NULL, -1);

    PyObject* key = PyBytes_FromStringAndSize(NULL, strlen(signature) + 10);
    if (key == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }

    r = PyObjCRT_SimplifySignature(signature, PyBytes_AS_STRING(key),
                                   PyBytes_GET_SIZE(key));
    if (r == -1) {
        Py_DECREF(key);
        PyErr_Format(PyObjCExc_Error, "cannot simplify signature '%s'", signature);
        return -1;
    }

    if (!call_to_objc || !make_call_to_python_block) {
        Py_DECREF(key);
        PyErr_SetString(PyObjCExc_Error,
                        "PyObjC_RegisterSignatureMapping: all functions required");
        return -1;
    }

    v = PyMem_Malloc(sizeof(*v));
    if (v == NULL) {
        Py_DECREF(key);
        PyErr_NoMemory();
        return -1;
    }
    v->call_to_objc              = call_to_objc;
    v->make_call_to_python_block = make_call_to_python_block;

    entry = PyCapsule_New(v, "objc.__memblock__", memblock_capsule_cleanup);
    if (entry == NULL) {
        Py_DECREF(key);
        PyMem_Free(v);
        return -1;
    }

    if (_PyBytes_Resize(&key, strlen(PyBytes_AS_STRING(key)) + 1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(entry);
        return -1;
        // LCOV_EXCL_STOP
    }

    if (PyDict_SetItem(signature_registry, key, entry) < 0) {
        Py_DECREF(key);
        Py_DECREF(entry);
        return -1;
    }
    Py_DECREF(key);
    Py_DECREF(entry);
    PyObjC_MappingCount += 1;

    return 0;
}

/*
 * May of may not raise an exception when the return value is NULL
 */
static struct registry* _Nullable search_special(Class class, SEL sel)
{
    PyObject*  result        = NULL;
    PyObject*  special_class = NULL;
    PyObject*  search_class  = NULL;
    PyObject*  lst;
    Py_ssize_t i;

    if (special_registry == NULL)
        goto error;
    if (!class)
        goto error;

    search_class = PyObjCClass_New(class);
    if (search_class == NULL) // LCOV_BR_EXCL_LINE
        goto error;           // LCOV_EXCL_LINE

    lst = PyDict_GetItemStringWithError(special_registry, sel_getName(sel));
    if (lst == NULL) {
        goto error;
    }

    Py_INCREF(lst);

    /*
     * Look for the most specific match:
     * - class in the list item is either the class we're looking
     *   for, or the "closest" superclass. The list item class
     *   can be 'None', which is less specific than any other class.
     * - later items in the list with the same list item class
     *   are preferred over earlier items (those are metadata that
     *   was added later).
     */
    for (i = 0; i < PyList_GET_SIZE(lst); i++) {
        PyObject* entry   = PyList_GET_ITEM(lst, i);
        PyObject* pyclass = PyTuple_GET_ITEM(entry, 0);

        if (pyclass == NULL) // LCOV_BR_EXCL_LINE
            continue;        // LCOV_EXCL_LINE
        if (pyclass != Py_None
            && !PyType_IsSubtype((PyTypeObject*)search_class, (PyTypeObject*)pyclass)) {
            continue;
        }

        if (!special_class) {
            /* No match yet, use */
            special_class = pyclass;
            result        = PyTuple_GET_ITEM(entry, 1);

        } else if (pyclass == Py_None) {
            /* Already have a match, Py_None is less specific */
            continue;

        } else if (PyType_IsSubtype((PyTypeObject*)special_class,
                                    (PyTypeObject*)pyclass)) {
            /* special_type is a superclass of search_class,
             * but a subclass of the current match, hence it is
             * a more specific match or a simular match later in the
             * list.
             */
            special_class = pyclass;
            result        = PyTuple_GET_ITEM(entry, 1);
        }
    }
    Py_XDECREF(search_class);
    if (!result)
        goto error;

    return PyCapsule_GetPointer(result, "objc.__memblock__");

error:
    return NULL;
}

static struct registry* _Nullable find_signature(const char* signature)
{
    PyObject* o;
    int       res;

    if (signature_registry == NULL) {
        return NULL;
    }

    PyObject* key = PyBytes_FromStringAndSize(NULL, strlen(signature) + 10);
    if (key == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    res = PyObjCRT_SimplifySignature(signature, PyBytes_AS_STRING(key),
                                     PyBytes_GET_SIZE(key));
    if (res == -1) {
        Py_DECREF(key);
        PyErr_Format(PyObjCExc_Error, "cannot simplify signature '%s'", signature);
        return NULL;
    }

    if ( // LCOV_BR_EXCL_LINE
        _PyBytes_Resize(&key, strlen(PyBytes_AS_STRING(key)) + 1) == -1) {
        return NULL; // LCOV_EXCL_LINE
    }
    o = PyDict_GetItemWithError(signature_registry, key);
    Py_DECREF(key);
    if (o == NULL)
        return NULL;

    return PyCapsule_GetPointer(o, "objc.__memblock__");
}

PyObjC_CallFunc _Nullable PyObjC_FindCallFunc(Class class, SEL sel, const char* signature)
{
    struct registry* special;

    PyObjC_Assert(special_registry != NULL, NULL);

    special = search_special(class, sel);
    if (special) {
        return special->call_to_objc;
    } else if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;               // LCOV_EXCL_LINE
    }

    special = find_signature(signature);
    if (special) {
        return special->call_to_objc;
    } else if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;               // LCOV_EXCL_LINE
    }

    return PyObjCFFI_Caller;
}

/*
 * XXX: Ideally there'd be a function to clean up the IMP, that requires
 *      additional state though.
 *
 * XXX: Remove class argument
 */
extern IMP
PyObjC_MakeIMP(Class class __attribute__((__unused__)), Class _Nullable super_class,
               PyObject* sel, PyObject* imp)
{
    struct registry*        generic;
    struct registry*        special;
    SEL                     aSelector = PyObjCSelector_GetSelector(sel);
    PyObjC_MakeIMPBlockFunc func      = NULL;
    IMP                     retval;
    PyObjCMethodSignature*  methinfo;

    methinfo = PyObjCSelector_GetMetadata(sel);
    if (methinfo == NULL) {
        return NULL;
    }

    if (super_class != nil) {
        special = search_special(super_class, aSelector);
        if (special) {
            func = special->make_call_to_python_block;
        } else if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;               // LCOV_EXCL_LINE
        }
    }

    if (func == NULL) {
        generic = find_signature(methinfo->signature);
        if (generic != NULL) {
            func = generic->make_call_to_python_block;
        } else if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;               // LCOV_EXCL_LINE
        }
    }

    if (func == PyObjCUnsupportedMethod_IMP) {
        PyErr_Format(PyExc_TypeError, "Implementing %s in Python is not supported",
                     sel_getName(aSelector));
        return NULL;
    }

    if (func != NULL) {
        retval = func(imp, methinfo);
        return retval;
    } else {
        PyErr_Clear();

        retval =
            PyObjCFFI_MakeIMPForSignature(methinfo, PyObjCSelector_GetSelector(sel), imp);

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
    PyErr_Format(PyExc_TypeError, "Cannot call '%s' on '%R' from Python",
                 sel_getName(PyObjCSelector_GetSelector(meth)), self);
    return NULL;
}
// LCOV_EXCL_STOP

NS_ASSUME_NONNULL_END
