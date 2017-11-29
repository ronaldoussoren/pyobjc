#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <SecurityInterface/SFAuthorizationView.h>


static int parse_itemset(PyObject* value, AuthorizationItemSet* itemset)
{
    itemset->items = NULL;

    if (value == Py_None) {
        return 1;

    } else {
        PyObject* seq = PySequence_Fast(value, "itemset must be a sequence or None");
        Py_ssize_t i;
        if (seq == NULL) {
            return 0;
        }
        itemset->count = PySequence_Fast_GET_SIZE(seq);
        itemset->items = PyMem_Malloc(sizeof(AuthorizationItem) * PySequence_Fast_GET_SIZE(seq));
        if (itemset->items == NULL) {
            PyErr_NoMemory();
            return 0;
        }

        for (i = 0; i < PySequence_Fast_GET_SIZE(seq); i++) {
            if (PyObjC_PythonToObjC("{_AuthorizationItem=^cL^vI}", PySequence_Fast_GET_ITEM(seq, i), itemset->items + i) < 0) {
                PyMem_Free(itemset->items);
                return 0;
            }
        }
    }
    return 1;
}

static PyObject* build_itemset(AuthorizationItemSet* itemset)
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
            PyObject* t = PyObjC_ObjCToPython("{_AuthorizationItem=^cL^vI}", itemset->items + i);
            if (t == NULL) {
                Py_DECREF(result);
                return NULL;
            }
            PyTuple_SET_ITEM(result, i, t);
        }
    }
    return result;
}

static PyObject*
call_authorizationRights(
        PyObject* method, PyObject* self, PyObject* arguments)
{
    struct objc_super super;
    AuthorizationRights* rights;
    PyObject* py_rights;

    if (!PyArg_ParseTuple(arguments, "")) {
        return NULL;
    }

    PyObjC_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));

        rights = ((AuthorizationRights*(*)(struct objc_super*, SEL))objc_msgSendSuper)(&super,
            PyObjCSelector_GetSelector(method));

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
    PyObjC_ENDHANDLER

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
call_setAuthorizationRights_(
        PyObject* method, PyObject* self, PyObject* arguments)
{
    struct objc_super super;
    AuthorizationRights rights;
    PyObject* py_rights;

    rights.items = NULL;

    if (!PyArg_ParseTuple(arguments, "O", &py_rights)) {
        return NULL;
    }

    if (!parse_itemset(py_rights, &rights)) {
        return NULL;
    }

    PyObjC_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));

        ((void(*)(struct objc_super*, SEL, AuthorizationRights*))objc_msgSendSuper)(&super,
            PyObjCSelector_GetSelector(method), &rights);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
    PyObjC_ENDHANDLER

    PyMem_Free(rights.items);

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}


static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_SecurityInterface)
{
    PyObject* m;
    Class cls;

    m = PyObjC_MODULE_CREATE(_SecurityInterface)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    cls= objc_lookUpClass("SFAuthorizationView");
    if (cls == NULL) {
        PyObjC_INITDONE();
    }

    if (PyObjC_RegisterMethodMapping(
        cls,
        @selector(authorizationView),
        call_authorizationRights,
        PyObjCUnsupportedMethod_IMP) < 0) {

        PyObjC_INITERROR();
    }

    if (PyObjC_RegisterMethodMapping(
        cls,
        @selector(setAuthorizationView:),
        call_setAuthorizationRights_,
        PyObjCUnsupportedMethod_IMP) < 0) {

        PyObjC_INITERROR();
    }

    PyObjC_INITDONE();
}
