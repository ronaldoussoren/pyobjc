#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <SecurityInterface/SFAuthorizationView.h>

static int
parse_itemset(PyObject* value, AuthorizationItemSet* itemset)
{
    itemset->items = NULL;

    if (value == Py_None) {
        return 1;

    } else {
        PyObject*  seq = PySequence_Tuple(value);
        Py_ssize_t i;
        if (seq == NULL) {
            return 0;
        }
        itemset->count = PyTuple_GET_SIZE(seq);
        itemset->items = PyMem_Malloc(sizeof(AuthorizationItem) * PyTuple_GET_SIZE(seq));
        if (itemset->items == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            return 0;
            // LCOV_EXCL_STOP
        }

        for (i = 0; i < PyTuple_GET_SIZE(seq); i++) {
            PyObject* cur_seq = PySequence_Tuple(PyTuple_GET_ITEM(seq, i));
            if (cur_seq == NULL) {
                PyErr_Format(PyExc_TypeError, "items[%ld] is not a sequence", (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }
            if (PyTuple_GET_SIZE(cur_seq) != 4) {
                PyErr_Format(PyExc_TypeError, "items[%ld] is not a sequence of 4 items",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }

            if (!PyBytes_Check(PyTuple_GET_ITEM(cur_seq, 0))) {
                PyErr_Format(PyExc_TypeError, "items[%ld].name is not a byte string",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }

            itemset->items[i].name = PyBytes_AsString(PyTuple_GET_ITEM(cur_seq, 0));

            if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GET_ITEM(cur_seq, 1),
                                    &(itemset->items[i].valueLength))
                == -1) {
                PyErr_Format(PyExc_TypeError, "items[%ld].valueLength is not an integer",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }

            if (PyTuple_GET_ITEM(cur_seq, 2) == Py_None) {
                if (itemset->items[i].valueLength != 0) {
                    PyErr_Format(PyExc_TypeError,
                                 "items[%ld].value is None, valueLength != 0", (long)i);
                    PyMem_Free(itemset->items);
                    return 0;
                }

                itemset->items[i].value = NULL;

            } else {
                if (!PyBytes_Check(PyTuple_GET_ITEM(cur_seq, 2))
                    || PyBytes_Size(PyTuple_GET_ITEM(cur_seq, 2))
                           != (Py_ssize_t)itemset->items[i].valueLength) {
                    PyErr_Format(PyExc_TypeError,
                                 "items[%ld].value is not a byte string of length %ld",
                                 (long)i, (long)(itemset->items[i].valueLength));
                    PyMem_Free(itemset->items);
                    return 0;
                }

                itemset->items[i].value = PyBytes_AsString(PyTuple_GET_ITEM(cur_seq, 2));
            }

            if (PyObjC_PythonToObjC(@encode(UInt32), PyTuple_GET_ITEM(cur_seq, 3),
                                    &(itemset->items[i].flags))
                == -1) {
                PyErr_Format(PyExc_TypeError, "items[%ld].flags is not an integer",
                             (long)i);
                PyMem_Free(itemset->items);
                return 0;
            }
        }
    }
    return 1;
}

static void
free_itemset(AuthorizationItemSet* itemset)
{
    PyMem_Free(itemset->items);
}

static PyObject*
build_itemset(AuthorizationItemSet* _Nonnull itemset)
{
    PyObject* result = NULL;
    PyObject* t      = NULL;
    PyObject* o      = NULL;

    assert(itemset != NULL);

    UInt32 i;
    result = PyTuple_New(itemset->count);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    for (i = 0; i < itemset->count; i++) {
        Py_ssize_t         packed = -1;
        AuthorizationItem* item   = itemset->items + i;

        t = PyObjC_CreateRegisteredStruct("{_AuthorizationItem=^cL^vI}",
                                          sizeof("{_AuthorizationItem=^cL^vI}") - 1, NULL,
                                          &packed);
        if (t == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        o = PyBytes_FromString(item->name);
        if (o == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        if (PySequence_SetItem(t, 0, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        o = PyLong_FromUnsignedLong(item->valueLength);
        if (o == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        if (PySequence_SetItem(t, 1, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        if (item->value == NULL) {
            o = Py_None;
            Py_INCREF(Py_None);
        } else {
            o = PyBytes_FromStringAndSize(item->value, item->valueLength);
            if (o == NULL)  // LCOV_BR_EXCL_LINE
                goto error; // LCOV_EXCL_LINE
        }

        if (PySequence_SetItem(t, 2, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        o = PyLong_FromUnsignedLong(item->flags);
        if (o == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        if (PySequence_SetItem(t, 3, o) == -1) // LCOV_BR_EXCL_LINE
            goto error;                        // LCOV_EXCL_LINE

        Py_CLEAR(o);

        PyTuple_SET_ITEM(result, i, t);
    }
    return result;

error:
    // LCOV_EXCL_START
    Py_CLEAR(result);
    Py_CLEAR(t);
    Py_CLEAR(o);
    return NULL;
    // LCOV_EXCL_STOP
}

static PyObject*
call_authorizationRights(PyObject* method, PyObject* self,
                         PyObject* const* arguments __attribute__((__unused__)),
                         size_t           nargs)
{
    struct objc_super    super;
    AuthorizationRights* rights;
    PyObject*            py_rights;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            rights = ((AuthorizationRights * (*)(struct objc_super*, SEL))
                          objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method));

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    if (rights == NULL)
        Py_RETURN_NONE;
    py_rights = build_itemset(rights);
    return py_rights;
}

static PyObject*
call_setAuthorizationRights_(PyObject* method, PyObject* self, PyObject* const* arguments,
                             size_t nargs)
{
    struct objc_super   super;
    AuthorizationRights rights;
    PyObject*           py_rights;

    rights.items = NULL;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }
    py_rights = arguments[0];

    if (!parse_itemset(py_rights, &rights)) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            ((void (*)(struct objc_super*, SEL, AuthorizationRights*))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), &rights);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    free_itemset(&rights);

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    Class cls;

    if (PyObjC_ImportAPI(m) == -1) // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE

    cls = objc_lookUpClass("SFAuthorizationView");
    if (cls == Nil) { // LCOV_BR_EXCL_LINE
        return 0;     // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(authorizationRights),
                                     call_authorizationRights,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(setAuthorizationRights:),
                                     call_setAuthorizationRights_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_SecurityInterface",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__SecurityInterface(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__SecurityInterface(void)
{
    return PyModuleDef_Init(&mod_module);
}
