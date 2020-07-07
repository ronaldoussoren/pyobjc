#define Py_LIMITED_API 0x03060000
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
     PyModuleDef_HEAD_INIT,
     "_Network",
     NULL,                                        
     0,
     mod_methods,                                 
     NULL,                                        
     NULL,                                        
     NULL,                                        
     NULL};                                       

PyObject* PyInit__Network(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__Network(void)
{
    PyObject*                                m;
    nw_connection_send_completion_t          t;
    nw_content_context_t                     t2;
    nw_parameters_configure_protocol_block_t p;

    m = PyModule_Create(&mod_module);
    if (!m) { return NULL; }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
    t = NW_CONNECTION_SEND_IDEMPOTENT_CONTENT;
    if (add_constant(m, "NW_CONNECTION_SEND_IDEMPOTENT_CONTENT",
                     @encode(nw_connection_send_completion_t), &t)
        != 0)
        goto error;
    t2 = NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT;
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
    p = NW_PARAMETERS_DEFAULT_CONFIGURATION;
    if (add_constant(m, "NW_PARAMETERS_DEFAULT_CONFIGURATION",
                     @encode(nw_parameters_configure_protocol_block_t), &p)
        != 0)
        goto error;
    p = NW_PARAMETERS_DISABLE_PROTOCOL;
    if (add_constant(m, "NW_PARAMETERS_DISABLE_PROTOCOL",
                     @encode(nw_parameters_configure_protocol_block_t), &p)
        != 0)
        goto error;
#pragma clang diagnostic pop

    return m;

error:
    return NULL;
}
