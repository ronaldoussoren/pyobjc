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
        if (itemset->items == NULL) {
            PyErr_NoMemory();
            Py_DECREF(seq);
            return 0;
        }

        for (i = 0; i < PyTuple_GET_SIZE(seq); i++) {
            if (PyObjC_PythonToObjC("{_AuthorizationItem=^cL^vI}",
                                    PyTuple_GET_ITEM(seq, i), itemset->items + i)
                < 0) {
                PyMem_Free(itemset->items);
                Py_DECREF(seq);
                return 0;
            }
        }
        Py_DECREF(seq);
    }
    return 1;
}

static PyObject*
build_itemset(AuthorizationItemSet* itemset)
{
    PyObject* result;

    if (itemset == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    } else {
        UInt32 i;
        result = PyTuple_New(itemset->count);
        if (result == NULL) {
            return NULL;
        }

        for (i = 0; i < itemset->count; i++) {
            PyObject* t =
                PyObjC_ObjCToPython("{_AuthorizationItem=^cL^vI}", itemset->items + i);
            if (t == NULL) {
                Py_DECREF(result);
                return NULL;
            }
            PyTuple_SetItem(result, i, t);
        }
    }
    return result;
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

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    py_rights = build_itemset(rights);
    if (rights != NULL) {
        /* XXX: Not sure if this is needed */
        AuthorizationFreeItemSet(rights);
    }
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

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyMem_Free(rights.items);

    if (PyErr_Occurred()) {
        return NULL;
    }

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

    if (PyObjC_ImportAPI(m) == -1)
        return -1;

    cls = objc_lookUpClass("SFAuthorizationView");
    if (cls == Nil) {
        return 0;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(authorizationRights),
                                     call_authorizationRights,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(setAuthorizationRights:),
                                     call_setAuthorizationRights_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
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
