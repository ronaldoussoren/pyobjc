#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#undef PySequence_Fast_GET_ITEM
#define PySequence_Fast_GET_ITEM(o, i)                                                   \
    (PyList_Check(o) ? PyList_GetItem(o, i) : PyTuple_GetItem(o, i))

#undef PySequence_Fast_GET_SIZE
#define PySequence_Fast_GET_SIZE(o) (PyList_Check(o) ? PyList_Size(o) : PyTuple_Size(o))

#import <Foundation/Foundation.h>
#import <SecurityInterface/SFAuthorizationView.h>

static int
parse_itemset(PyObject* value, AuthorizationItemSet* itemset)
{
    itemset->items = NULL;

    if (value == Py_None) {
        return 1;

    } else {
        PyObject*  seq = PySequence_Fast(value, "itemset must be a sequence or None");
        Py_ssize_t i;
        if (seq == NULL) {
            return 0;
        }
        itemset->count = PySequence_Fast_GET_SIZE(seq);
        itemset->items =
            PyMem_Malloc(sizeof(AuthorizationItem) * PySequence_Fast_GET_SIZE(seq));
        if (itemset->items == NULL) {
            PyErr_NoMemory();
            return 0;
        }

        for (i = 0; i < PySequence_Fast_GET_SIZE(seq); i++) {
            if (PyObjC_PythonToObjC("{_AuthorizationItem=^cL^vI}",
                                    PySequence_Fast_GET_ITEM(seq, i), itemset->items + i)
                < 0) {
                PyMem_Free(itemset->items);
                return 0;
            }
        }
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

/* Python glue */
static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "_SecurityInterface",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit__SecurityInterface(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__SecurityInterface(void)
{
    PyObject* m;
    Class     cls;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    cls = objc_lookUpClass("SFAuthorizationView");
    if (cls == NULL) {
        return m;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(authorizationRights),
                                     call_authorizationRights,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return NULL;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(setAuthorizationRights:),
                                     call_setAuthorizationRights_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return NULL;
    }

    return m;
}
