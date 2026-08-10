#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#include <xpc/xpc.h>

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable mod_xpc_dictionary_create(
    PyObject* meth __attribute__((__unused__)), PyObject* _Nonnull const* _Nonnull args,
    size_t    nargs)
{
    PyObject* keys;
    PyObject* values;
    size_t    nitems;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(size_t), args[2], &nitems) == -1) {
        return NULL;
    }

    keys = PySequence_Tuple(args[0]);
    if (keys == NULL) {
        return NULL;
    }
    values = PySequence_Tuple(args[1]);
    if (values == NULL) {
        Py_DECREF(keys);
        return NULL;
    }

    assert(PyTuple_Check(keys));
    assert(PyTuple_Check(values));

    if ((size_t)PyTuple_GET_SIZE(keys) != nitems) {
        Py_DECREF(keys);
        Py_DECREF(values);
        PyErr_Format(PyExc_ValueError,
                     "Expecting sequence of exactly %ld items for 'keys'", nitems);
        return NULL;
    }

    if ((size_t)PyTuple_GET_SIZE(values) != nitems) {
        Py_DECREF(keys);
        Py_DECREF(values);
        PyErr_Format(PyExc_ValueError,
                     "Expecting sequence of exactly %ld items for 'values'", nitems);
        return NULL;
    }

    for (size_t i = 0; i < nitems; i++) {
        if (!PyBytes_Check(PyTuple_GET_ITEM(keys, i))) {
            PyErr_SetString(PyExc_TypeError, "Keys should be sequence of bytes");
            Py_DECREF(keys);
            Py_DECREF(values);
            return NULL;
        }
    }

    const char** key_array = PyMem_Malloc(sizeof(char*) * nitems);
    if (key_array == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(keys);
        Py_DECREF(values);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }
    id* value_array = PyMem_Malloc(sizeof(id) * nitems);
    if (value_array == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(keys);
        Py_DECREF(values);
        PyMem_Free(key_array);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (size_t i = 0; i < nitems; i++) {
        key_array[i] = PyBytes_AsString(PyTuple_GET_ITEM(keys, i));
        if (depythonify_python_object(PyTuple_GET_ITEM(values, i), value_array + i)
            == -1) {
            Py_DECREF(keys);
            Py_DECREF(values);
            PyMem_Free(key_array);
            PyMem_Free(value_array);
            return NULL;
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
    {0, 0, 0, 0} /* sentinel */
};

static int
add_constant(PyObject* m, const char* name, char* typestr, const void* value)
{
    PyObject* v;
    int       r;

    v = PyObjC_ObjCToPython(typestr, (void*)value);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        return -1;   // LCOV_EXCL_LINE
    }

    r = PyModule_AddObject(m, name, v);
    if (r == -1)      // LCOV_BR_EXCL_LINE
        Py_DECREF(v); // LCOV_EXCL_LINE

    return r;
}

static int
add_bytes_constant(PyObject* m, const char* name, const char* value)
{
    PyObject* v;
    int       r;

    v = PyBytes_FromString(value);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        return -1;   // LCOV_EXCL_LINE
    }

    r = PyModule_AddObject(m, name, v);
    if (r == -1)      // LCOV_BR_EXCL_LINE
        Py_DECREF(v); // LCOV_EXCL_LINE

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

static int
mod_exec_module(PyObject* module)
{
    if (PyObjC_ImportAPI(module) == -1) // LCOV_BR_EXCL_LINE
        return -1;                      // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller( // LCOV_BR_EXCL_LINE
            xpc_dictionary_create, mod_xpc_dictionary_create)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    /*
     * Register a number of struct pointer types that are actually Objective-C objects
     */
    if (PyObjCPointerWrapper_RegisterID("xpc_activity_t", "^{_xpc_activity_s=}")
        < 0)        // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    if (PyObjCPointerWrapper_RegisterID("xpc_object_t", "^{_xpc_object_s=}")
        < 0)        // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE
    if (PyObjCPointerWrapper_RegisterID("xpc_type_t", "^{_xpc_type_s=}")
        < 0)        // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE
    if (PyObjCPointerWrapper_RegisterID("xpc_connection_t", "^{_xpc_connection_s=}")
        < 0)        // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE
    if (PyObjCPointerWrapper_RegisterID("xpc_endpoint", "^{_xpc_endpoint_s=}")
        < 0)        // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    for (struct bytes_constants* cur = BYTES_CONSTANTS; cur->name != NULL; cur++) {
        if (cur->value == NULL) // LCOV_BR_EXCL_LINE
            continue;           // LCOV_EXCL_LINE
        if (add_bytes_constant(module, cur->name, *(cur->value))
            != 0)       // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    for (struct int64_constants* cur = INT64_CONSTANTS; cur->name != NULL; cur++) {
        if (cur->value == NULL) // LCOV_BR_EXCL_LINE
            continue;           // LCOV_EXCL_LINE
        PyObject* v = PyLong_FromLong(*(cur->value));
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        if (PyModule_AddObject(module, cur->name, v) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(v);
            goto error;
            // LCOV_EXCL_STOP
        }
    }

    id v = (id)XPC_TYPE_ACTIVITY;
    if (add_constant(module, "XPC_TYPE_ACTIVITY", @encode(id), &v)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    v = (id)XPC_ACTIVITY_CHECK_IN;
    if (add_constant(module, "XPC_ACTIVITY_CHECK_IN", @encode(id), &v)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    v = (id)XPC_TYPE_ENDPOINT;
    if (add_constant(module, "XPC_TYPE_ENDPOINT", @encode(id), &v)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    xpc_object_t d;

    d = XPC_ERROR_CONNECTION_INTERRUPTED;
    if (add_constant(module, "XPC_ERROR_CONNECTION_INTERRUPTED", @encode(xpc_object_t),
                     &d)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    d = XPC_ERROR_CONNECTION_INVALID;
    if (add_constant(module, "XPC_ERROR_CONNECTION_INVALID", @encode(xpc_object_t), &d)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    d = XPC_ERROR_TERMINATION_IMMINENT;
    if (add_constant(module, "XPC_ERROR_TERMINATION_IMMINENT", @encode(xpc_object_t), &d)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

#if PyObjC_BUILD_RELEASE >= 1200
    if (__builtin_available(macOS 12.0, *)) { // LCOV_BR_EXCL_LINE
        d = XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT;
        if (add_constant(module, "XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT",
                         @encode(xpc_object_t), &d)
            != 0)       // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1200 */

    xpc_type_t t;
    t = XPC_TYPE_NULL;
    if (add_constant(module, "XPC_TYPE_NULL", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_BOOL;
    if (add_constant(module, "XPC_TYPE_BOOL", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_INT64;
    if (add_constant(module, "XPC_TYPE_INT64", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_UINT64;
    if (add_constant(module, "XPC_TYPE_UINT64", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_DOUBLE;
    if (add_constant(module, "XPC_TYPE_DOUBLE", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_DATE;
    if (add_constant(module, "XPC_TYPE_DATE", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_DATA;
    if (add_constant(module, "XPC_TYPE_DATA", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_STRING;
    if (add_constant(module, "XPC_TYPE_STRING", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_UUID;
    if (add_constant(module, "XPC_TYPE_UUID", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_FD;
    if (add_constant(module, "XPC_TYPE_FD", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_SHMEM;
    if (add_constant(module, "XPC_TYPE_SHMEM", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_ARRAY;
    if (add_constant(module, "XPC_TYPE_ARRAY", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_DICTIONARY;
    if (add_constant(module, "XPC_TYPE_DICTIONARY", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_ERROR;
    if (add_constant(module, "XPC_TYPE_ERROR", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

#if PyObjC_BUILD_RELEASE >= 1300
    t = XPC_TYPE_SESSION;
    if (add_constant(module, "XPC_TYPE_SESSION", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    t = XPC_TYPE_RICH_ERROR;
    if (add_constant(module, "XPC_TYPE_RICH_ERROR", @encode(xpc_type_t), &t)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE
#endif              /* PyObjC_BUILD_RELEASE >= 1300 */

    xpc_object_t b = XPC_BOOL_TRUE;
    if (add_constant(module, "XPC_BOOL_TRUE", @encode(xpc_object_t), &b)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    b = XPC_BOOL_FALSE;
    if (add_constant(module, "XPC_BOOL_FALSE", @encode(xpc_object_t), &b)
        != 0)       // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    return 0;

error:
    return -1; // LCOV_EXCL_LINE
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* Subinterpreters are not yet supported because of PyObjC_API */
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
    .m_name     = "_xpc",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__xpc(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__xpc(void)
{
    return PyModuleDef_Init(&mod_module);
}
NS_ASSUME_NONNULL_END
