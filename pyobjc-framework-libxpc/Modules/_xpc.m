/*#define Py_LIMITED_API 0x03060000*/
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#include <xpc/xpc.h>

static PyObject*
mod_xpc_dictionary_create(PyObject* mod __attribute__((__unused__)), PyObject* args)
{
    PyObject*  keys;
    PyObject*  values;
    Py_ssize_t nitems;

    if (!PyArg_ParseTuple(args, "OOn", &keys, &values, &nitems)) {
        return NULL;
    }

    keys = PySequence_Tuple(keys);
    if (keys == NULL) {
        return NULL;
    }
    values = PySequence_Tuple(values);
    if (values == NULL) {
        Py_DECREF(keys);
        return NULL;
    }

    if (PyTuple_Size(keys) != nitems) {
        Py_DECREF(keys);
        Py_DECREF(values);
        PyErr_Format(PyExc_ValueError, "Expecting keys sequence of exactly %ld items",
                     nitems);
        return NULL;
    }

    if (PyTuple_Size(values) != nitems) {
        Py_DECREF(keys);
        Py_DECREF(values);
        PyErr_Format(PyExc_ValueError, "Expecting values sequence of exactly %ld items",
                     nitems);
        return NULL;
    }

    for (Py_ssize_t i = 0; i < nitems; i++) {
        if (!PyBytes_Check(PyTuple_GET_ITEM(keys, i))) {
            PyErr_SetString(PyExc_TypeError, "Keys should be sequence of bytes");
            Py_DECREF(keys);
            Py_DECREF(values);
            return NULL;
        }
    }

    const char** key_array = PyMem_Malloc(sizeof(char*) * nitems);
    if (key_array == NULL) {
        Py_DECREF(keys);
        Py_DECREF(values);
        PyErr_NoMemory();
        return NULL;
    }
    id* value_array = PyMem_Malloc(sizeof(id) * nitems);
    if (value_array == NULL) {
        Py_DECREF(keys);
        Py_DECREF(values);
        PyMem_Free(key_array);
        PyErr_NoMemory();
        return NULL;
    }

    for (Py_ssize_t i = 0; i < nitems; i++) {
        key_array[i] = PyBytes_AsString(PyTuple_GET_ITEM(keys, i));
        if (depythonify_python_object(PyTuple_GET_ITEM(values, i), value_array + i)
            == -1) {
            Py_DECREF(keys);
            Py_DECREF(values);
            PyMem_Free(key_array);
            PyMem_Free(value_array);
        }
    }

    xpc_object_t result = xpc_dictionary_create(key_array, value_array, nitems);
    Py_DECREF(keys);
    Py_DECREF(values);
    PyMem_Free(key_array);
    PyMem_Free(value_array);

    PyObject* rv = PyObjC_IdToPython(result);
    xpc_release(result);
    return rv;
}

static PyMethodDef mod_methods[] = {
    {.ml_name  = "xpc_dictionary_create",
     .ml_meth  = (PyCFunction)mod_xpc_dictionary_create,
     .ml_flags = METH_VARARGS,
     .ml_doc   = "xpc_dictionary_create(keys, values, nitem, /)" CLINIC_SEP},

    {0, 0, 0, 0} /* sentinel */
};

static int
add_constant(PyObject* m, const char* name, char* typestr, const void* value)
{
    PyObject* v;
    int       r;

    v = PyObjC_ObjCToPython(typestr, (void*)value);
    if (v == NULL) {
        return -1;
    }

    r = PyModule_AddObject(m, name, v);

    return r;
}

static int
add_bytes_constant(PyObject* m, const char* name, const char* value)
{
    PyObject* v;
    int       r;

    v = PyBytes_FromString(value);
    if (v == NULL) {
        return -1;
    }

    r = PyModule_AddObject(m, name, v);

    return r;
}

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunknown-pragmas"
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

static struct bytes_constants {
    const char*        name;
    const char* const* value;
} BYTES_CONSTANTS[] = {
    {"XPC_ACTIVITY_INTERVAL", &XPC_ACTIVITY_INTERVAL},
    {"XPC_ACTIVITY_REPEATING", &XPC_ACTIVITY_REPEATING},
    {"XPC_ACTIVITY_DELAY", &XPC_ACTIVITY_DELAY},
    {"XPC_ACTIVITY_GRACE_PERIOD", &XPC_ACTIVITY_GRACE_PERIOD},
    {"XPC_ACTIVITY_PRIORITY", &XPC_ACTIVITY_PRIORITY},
    {"XPC_ACTIVITY_PRIORITY_MAINTENANCE", &XPC_ACTIVITY_PRIORITY_MAINTENANCE},
    {"XPC_ACTIVITY_PRIORITY_UTILITY", &XPC_ACTIVITY_PRIORITY_UTILITY},
    {"XPC_ACTIVITY_ALLOW_BATTERY", &XPC_ACTIVITY_ALLOW_BATTERY},
    {"XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP", &XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP},
#if PyObjC_BUILD_RELEASE >= 1200
    {"XPC_ACTIVITY_PREVENT_DEVICE_SLEEP", &XPC_ACTIVITY_PREVENT_DEVICE_SLEEP},
#endif /* PyObjC_BUILD_RELEASE >= 1200 */
    {"XPC_ERROR_KEY_DESCRIPTION", &XPC_ERROR_KEY_DESCRIPTION},
    {"XPC_EVENT_KEY_NAME", &XPC_EVENT_KEY_NAME},

    {NULL, NULL}};

static struct int64_constants {
    const char*    name;
    const int64_t* value;
} INT64_CONSTANTS[] = {{"XPC_ACTIVITY_INTERVAL_1_MIN", &XPC_ACTIVITY_INTERVAL_1_MIN},
                       {"XPC_ACTIVITY_INTERVAL_5_MIN", &XPC_ACTIVITY_INTERVAL_5_MIN},
                       {"XPC_ACTIVITY_INTERVAL_15_MIN", &XPC_ACTIVITY_INTERVAL_15_MIN},
                       {"XPC_ACTIVITY_INTERVAL_30_MIN", &XPC_ACTIVITY_INTERVAL_30_MIN},
                       {"XPC_ACTIVITY_INTERVAL_1_HOUR", &XPC_ACTIVITY_INTERVAL_1_HOUR},
                       {"XPC_ACTIVITY_INTERVAL_4_HOURS", &XPC_ACTIVITY_INTERVAL_4_HOURS},
                       {"XPC_ACTIVITY_INTERVAL_8_HOURS", &XPC_ACTIVITY_INTERVAL_8_HOURS},
                       {"XPC_ACTIVITY_INTERVAL_1_DAY", &XPC_ACTIVITY_INTERVAL_1_DAY},
                       {"XPC_ACTIVITY_INTERVAL_7_DAYS", &XPC_ACTIVITY_INTERVAL_7_DAYS},

                       {NULL, NULL}};

#pragma clang diagnostic pop

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_xpc", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__xpc(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__xpc(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    /*
     * Register a number of struct pointer types that are actually Objective-C objects
     */
    if (PyObjCPointerWrapper_RegisterID("xpc_activity_t", "^{_xpc_activity_s=}") < 0)
        goto error;

    if (PyObjCPointerWrapper_RegisterID("xpc_object_t", "^{_xpc_object_s=}") < 0)
        goto error;
    if (PyObjCPointerWrapper_RegisterID("xpc_type_t", "^{_xpc_type_s=}") < 0)
        goto error;
    if (PyObjCPointerWrapper_RegisterID("xpc_connection_t", "^{_xpc_connection_s=}") < 0)
        goto error;
    if (PyObjCPointerWrapper_RegisterID("xpc_endpoint", "^{_xpc_endpoint_s=}") < 0)
        goto error;

    for (struct bytes_constants* cur = BYTES_CONSTANTS; cur->name != NULL; cur++) {
        if (cur->value == NULL)
            continue;
        if (add_bytes_constant(m, cur->name, *(cur->value)) != 0)
            goto error;
    }

    for (struct int64_constants* cur = INT64_CONSTANTS; cur->name != NULL; cur++) {
        if (cur->value == NULL)
            continue;
        PyObject* v = PyLong_FromLong(*(cur->value));
        if (v == NULL)
            goto error;

        if (PyModule_AddObject(m, cur->name, v) == -1) {
            Py_DECREF(v);
            goto error;
        }
    }

    id v = (id)XPC_TYPE_ACTIVITY;
    if (add_constant(m, "XPC_TYPE_ACTIVITY", @encode(id), &v) != 0)
        goto error;

    v = (id)XPC_ACTIVITY_CHECK_IN;
    if (add_constant(m, "XPC_ACTIVITY_CHECK_IN", @encode(id), &v) != 0)
        goto error;

    v = (id)XPC_TYPE_ENDPOINT;
    if (add_constant(m, "XPC_TYPE_ENDPOINT", @encode(id), &v) != 0)
        goto error;

    xpc_object_t d;

    d = XPC_ERROR_CONNECTION_INTERRUPTED;
    if (add_constant(m, "XPC_ERROR_CONNECTION_INTERRUPTED", @encode(xpc_object_t), &d)
        != 0)
        goto error;

    d = XPC_ERROR_CONNECTION_INVALID;
    if (add_constant(m, "XPC_ERROR_CONNECTION_INVALID", @encode(xpc_object_t), &d) != 0)
        goto error;

    d = XPC_ERROR_TERMINATION_IMMINENT;
    if (add_constant(m, "XPC_ERROR_TERMINATION_IMMINENT", @encode(xpc_object_t), &d) != 0)
        goto error;

#if PyObjC_BUILD_RELEASE >= 1200
    if (__builtin_available(macOS 12.0, *)) {
        d = XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT;
        if (add_constant(m, "XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT",
                         @encode(xpc_object_t), &d)
            != 0)
            goto error;
    }
#endif /* PyObjC_BUILD_RELEASE >= 1200 */

    xpc_type_t t;
    t = XPC_TYPE_NULL;
    if (add_constant(m, "XPC_TYPE_NULL", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_BOOL;
    if (add_constant(m, "XPC_TYPE_BOOL", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_INT64;
    if (add_constant(m, "XPC_TYPE_INT64", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_UINT64;
    if (add_constant(m, "XPC_TYPE_UINT64", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_DOUBLE;
    if (add_constant(m, "XPC_TYPE_DOUBLE", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_DATE;
    if (add_constant(m, "XPC_TYPE_DATE", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_DATA;
    if (add_constant(m, "XPC_TYPE_DATA", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_STRING;
    if (add_constant(m, "XPC_TYPE_STRING", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_UUID;
    if (add_constant(m, "XPC_TYPE_UUID", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_FD;
    if (add_constant(m, "XPC_TYPE_FD", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_SHMEM;
    if (add_constant(m, "XPC_TYPE_SHMEM", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_ARRAY;
    if (add_constant(m, "XPC_TYPE_ARRAY", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_DICTIONARY;
    if (add_constant(m, "XPC_TYPE_DICTIONARY", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_ERROR;
    if (add_constant(m, "XPC_TYPE_ERROR", @encode(xpc_type_t), &t) != 0)
        goto error;

#if PyObjC_BUILD_RELEASE >= 1300
    t = XPC_TYPE_SESSION;
    if (add_constant(m, "XPC_TYPE_SESSION", @encode(xpc_type_t), &t) != 0)
        goto error;

    t = XPC_TYPE_RICH_ERROR;
    if (add_constant(m, "XPC_TYPE_RICH_ERROR", @encode(xpc_type_t), &t) != 0)
        goto error;
#endif /* PyObjC_BUILD_RELEASE >= 1300 */

    xpc_object_t b = XPC_BOOL_TRUE;
    if (add_constant(m, "XPC_BOOL_TRUE", @encode(xpc_object_t), &b) != 0)
        goto error;

    b = XPC_BOOL_FALSE;
    if (add_constant(m, "XPC_BOOL_FALSE", @encode(xpc_object_t), &b) != 0)
        goto error;

    return m;

error:
    return NULL;
}
