#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
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

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_Network", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__Network(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__Network(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

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

    return m;

error:
    return NULL;
}
