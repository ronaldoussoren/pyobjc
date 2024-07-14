#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#include <Network/Network.h>

static PyMethodDef mod_methods[] = {
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

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;

    if (@available(macos 10.14, *)) {
        nw_connection_send_completion_t t = NW_CONNECTION_SEND_IDEMPOTENT_CONTENT;
        if (add_constant(m, "NW_CONNECTION_SEND_IDEMPOTENT_CONTENT",
                         @encode(nw_connection_send_completion_t), &t)
            != 0)
            goto error;
        nw_content_context_t t2 = NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT;
        if (add_constant(m, "NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT",
                         @encode(nw_content_context_t), &t2)
            != 0)
            goto error;
        t2 = NW_CONNECTION_FINAL_MESSAGE_CONTEXT;
        if (add_constant(m, "NW_CONNECTION_FINAL_MESSAGE_CONTEXT",
                         @encode(nw_content_context_t), &t2)
            != 0)
            goto error;
        t2 = NW_CONNECTION_DEFAULT_STREAM_CONTEXT;
        if (add_constant(m, "NW_CONNECTION_DEFAULT_STREAM_CONTEXT",
                         @encode(nw_content_context_t), &t2)
            != 0)
            goto error;
        nw_parameters_configure_protocol_block_t p = NW_PARAMETERS_DEFAULT_CONFIGURATION;
        if (add_constant(m, "NW_PARAMETERS_DEFAULT_CONFIGURATION",
                         @encode(nw_parameters_configure_protocol_block_t), &p)
            != 0)
            goto error;
        p = NW_PARAMETERS_DISABLE_PROTOCOL;
        if (add_constant(m, "NW_PARAMETERS_DISABLE_PROTOCOL",
                         @encode(nw_parameters_configure_protocol_block_t), &p)
            != 0)
            goto error;
    }

#if PyObjC_BUILD_RELEASE >= 1016
    if (@available(macos 10.16, *)) {
        nw_privacy_context_t c = NW_DEFAULT_PRIVACY_CONTEXT;
        if (add_constant(m, "NW_DEFAULT_PRIVACY_CONTEXT", @encode(nw_privacy_context_t),
                         &c)
            != 0)
            goto error;
    }
#endif

    return 0;

error:
    return -1;
}


static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_Network",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__Network(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__Network(void)
{
    return PyModuleDef_Init(&mod_module);
}
