/*
 * registry.m -- Storing and finding exception data.
 *
 * This file defines generic functionality to store exception data for
 * a class/method.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

BOOL PyObjC_UpdatingMetaData = NO;

PyObject* _Nullable PyObjC_NewRegistry(void) { return PyDict_New(); }

int
PyObjC_AddToRegistry(PyObject* registry, PyObject* class_name, PyObject* selector,
                     PyObject* value)
{
    int       result;
    PyObject* sublist;

    PyObjC_Assert(PyBytes_Check(class_name), -1);
    PyObjC_Assert(PyBytes_Check(selector), -1);

    sublist = PyDict_GetItemWithError(registry, selector);
    if (sublist == NULL && PyErr_Occurred()) {
        return -1;
    }
    if (sublist == NULL) {
        sublist = PyList_New(0);
        result  = PyDict_SetItem(registry, selector, sublist);
        Py_DECREF(sublist);
        if (result == -1) {
            return -1;
        }
    }

    if (!PyObjC_UpdatingMetaData) {
        PyObjC_MappingCount += 1;
    }

    /*
     * Check if there is a registration for *class_name* in
     * *sublist*, if so replace that registration.
     */
    for (Py_ssize_t i = 0; i < PyList_GET_SIZE(sublist); i++) {
        PyObject* item = PyList_GET_ITEM(sublist, i);

        PyObjC_Assert(PyTuple_CheckExact(item), -1);
        PyObjC_Assert(PyTuple_GET_SIZE(item) == 2, -1);

        int r = PyObject_RichCompareBool(PyTuple_GET_ITEM(item, 0), class_name, Py_EQ);
        if (r == -1)
            return -1;
        if (r) {
            Py_DECREF(PyTuple_GET_ITEM(item, 1));
            PyTuple_SET_ITEM(item, 1, value);
            Py_INCREF(value);
            return 0;
        }
    }

    PyObject* item = Py_BuildValue("(OO)", class_name, value);
    if (item == NULL) {
        return -1;
    }
    result = PyList_Append(sublist, item);
    Py_DECREF(item);
    return result;
}

PyObject* _Nullable PyObjC_FindInRegistry(PyObject* registry, Class cls, SEL selector)
{
    Py_ssize_t i;
    Py_ssize_t len;
    PyObject*  cur;
    Class      found_class = nil;
    PyObject*  found_value = NULL;
    PyObject*  sublist;

    if (registry == NULL) {
        return NULL;
    }

    PyObject* k = PyBytes_FromString(sel_getName(selector));

    sublist = PyDict_GetItemWithError(registry, k);
    Py_DECREF(k);
    if (sublist == NULL)
        return NULL;

    len = PyList_Size(sublist);
    for (i = 0; i < len; i++) {
        Class cur_class;

        cur = PyList_GET_ITEM(sublist, i);
        if (cur == NULL) {
            PyErr_Clear();
            continue;
        }

        PyObjC_Assert(PyTuple_CheckExact(cur), NULL);

        PyObject* nm = PyTuple_GET_ITEM(cur, 0);
        if (PyBytes_Check(nm)) {
            cur_class = objc_lookUpClass(PyBytes_AsString(nm));

        } else {
            PyErr_SetString(PyExc_TypeError,
                            "Exception registry class name is not a byte string");
            return NULL;
        }

        if (cur_class == nil) {
            continue;
        }

        if (!PyObjC_class_isSubclassOf(cls, cur_class)
            && !PyObjC_class_isSubclassOf(cls,
                                          (Class _Nonnull)object_getClass(cur_class))) {
            continue;
        }

        if (found_class != NULL && found_class != cur_class) {
            if (PyObjC_class_isSubclassOf(found_class, cur_class)) {
                continue;
            }
        }

        found_class = cur_class;
        Py_INCREF(PyTuple_GET_ITEM(cur, 1));
        Py_XDECREF(found_value);
        found_value = PyTuple_GET_ITEM(cur, 1);
    }

    return found_value;
}

PyObject* _Nullable PyObjC_CopyRegistry(PyObject*            registry,
                                        PyObjC_ItemTransform value_transform)
{
    PyObject*  result = PyDict_New();
    PyObject*  key;
    PyObject*  sublist;
    Py_ssize_t pos = 0;
    if (result == NULL) {
        return NULL;
    }

    while (PyDict_Next(registry, &pos, &key, &sublist)) {
        Py_ssize_t i, len;
        PyObject*  sl_new;

#ifdef PyObjC_DEBUG
        if (!PyList_CheckExact(sublist)) {
            PyErr_SetString(PyObjCExc_InternalError, "sublist of registry is not a list");
            goto error;
        }
#endif

        len    = PyList_GET_SIZE(sublist);
        sl_new = PyList_New(len);
        if (sl_new == NULL)
            goto error;
        if (PyDict_SetItem(result, key, sl_new) == -1) {
            Py_DECREF(sl_new);
            goto error;
        }
        Py_DECREF(sl_new);

        for (i = 0; i < len; i++) {
            PyObject* item;
            PyObject* new_item;

            item     = PyList_GET_ITEM(sublist, i);
            new_item = Py_BuildValue("(ON)", PyTuple_GET_ITEM(item, 0),
                                     value_transform(PyTuple_GET_ITEM(item, 1)));
            if (new_item == NULL)
                goto error;

            PyList_SET_ITEM(sl_new, i, new_item);
        }
    }

    return result;

error:
    Py_DECREF(result);
    return NULL;
}

NS_ASSUME_NONNULL_END
