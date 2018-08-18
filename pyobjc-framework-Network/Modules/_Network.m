#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#include <Network/Network.h>

static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};

static int add_constant(PyObject* m, const char* name, char* typestr, const void* value)
{
    PyObject* v;
    int r;

    v = PyObjC_ObjCToPython(typestr, (void*)value);
    if (v == NULL) {
        return -1;
    }

    r = PyModule_AddObject(m, name, v);

    return r;
}

/* Python glue */
PyObjC_MODULE_INIT(_Network)
{
    PyObject* m;
    nw_connection_send_completion_t t;
    nw_content_context_t t2;
    nw_parameters_configure_protocol_block_t p;

    m = PyObjC_MODULE_CREATE(_Network)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
    t = NW_CONNECTION_SEND_IDEMPOTENT_CONTENT; if (add_constant(m, "NW_CONNECTION_SEND_IDEMPOTENT_CONTENT", @encode(nw_connection_send_completion_t), &t) != 0) goto error;
    t2 = NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT; if (add_constant(m, "NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT", @encode(nw_content_context_t), &t2) != 0) goto error;
    t2 = NW_CONNECTION_FINAL_MESSAGE_CONTEXT; if (add_constant(m, "NW_CONNECTION_FINAL_MESSAGE_CONTEXT", @encode(nw_content_context_t), &t2) != 0) goto error;
    t2 = NW_CONNECTION_DEFAULT_STREAM_CONTEXT; if (add_constant(m, "NW_CONNECTION_DEFAULT_STREAM_CONTEXT", @encode(nw_content_context_t), &t2) != 0) goto error;
    p = NW_PARAMETERS_DEFAULT_CONFIGURATION; if (add_constant(m, "NW_PARAMETERS_DEFAULT_CONFIGURATION", @encode(nw_parameters_configure_protocol_block_t), &p) != 0) goto error;
    p = NW_PARAMETERS_DISABLE_PROTOCOL; if (add_constant(m, "NW_PARAMETERS_DISABLE_PROTOCOL", @encode(nw_parameters_configure_protocol_block_t), &p) != 0) goto error;
#pragma clang diagnostic pop

    PyObjC_INITDONE();

error:
    PyObjC_INITERROR();

}
