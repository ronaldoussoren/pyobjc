#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#include <dispatch/dispatch.h>

static PyObject*
m_dispatch_data_create_map(
    PyObject* self __attribute__((__unused__)),
    PyObject* args)
{
    PyObject* py_data;
    PyObject* py_buffer;
    PyObject* py_size;
    PyObject* py_result;
    PyObject* py_memview;

    id data, result;
    const void* buffer = NULL;
    size_t size = 0;

    if (!PyArg_ParseTuple(args, "OOO", &py_data, &py_buffer, &py_size)) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(id), py_data, &data) == -1) {
        return NULL;
    }
    if (py_buffer != Py_None) {
        PyErr_SetString(PyExc_TypeError, "Buffer must be None");
        return NULL;
    }
    if (py_size != Py_None) {
        PyErr_SetString(PyExc_TypeError, "Size must be None");
        return NULL;
    }

    result = (id)dispatch_data_create_map((dispatch_data_t)data, &buffer, &size);
    py_result = PyObjC_IdToPython(result);
    if (result) {
        [result release];
    }
    if (py_result == NULL) {
        return NULL;
    }


#if Py_MAJOR_VERSION == 3
    py_memview = PyMemoryView_FromMemory(buffer, size, PyBuf_READ)
#else
    Py_buffer bufinfo;

    if (PyBuffer_FillInfo(&bufinfo, NULL, (void*)buffer, size, 1, PyBUF_SIMPLE) == -1) {
        Py_DECREF(py_result);
        return NULL;
    }
    py_memview = PyMemoryView_FromBuffer(&bufinfo);
#endif
    if (py_memview == NULL) {
        Py_DECREF(py_result);
        return NULL;
    }

    return Py_BuildValue("(NNk)", py_result, py_memview, (unsigned long)size);
}

static PyMethodDef mod_methods[] = {
    {
        "dispatch_data_create_map",
        (PyCFunction)m_dispatch_data_create_map,
        METH_VARARGS,
        NULL
    },
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
PyObjC_MODULE_INIT(_libdispatch)
{
    PyObject* m;
    dispatch_source_type_t s;

    m = PyObjC_MODULE_CREATE(_libdispatch)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    id v = (id)DISPATCH_QUEUE_CONCURRENT; if (add_constant(m, "DISPATCH_QUEUE_CONCURRENT", @encode(id), &v) != 0) goto error;
    v = (id)dispatch_data_empty; if (add_constant(m, "dispatch_data_empty", @encode(id), &v) != 0) goto error;
    if (add_constant(m, "DISPATCH_DATA_DESTRUCTOR_FREE", @encode(id), &DISPATCH_DATA_DESTRUCTOR_FREE) != 0) goto error;
    if (add_constant(m, "DISPATCH_DATA_DESTRUCTOR_MUNMAP", @encode(id), &DISPATCH_DATA_DESTRUCTOR_MUNMAP) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_DATA_ADD; if (add_constant(m, "DISPATCH_SOURCE_TYPE_DATA_ADD", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_DATA_OR; if (add_constant(m, "DISPATCH_SOURCE_TYPE_DATA_OR", @encode(dispatch_source_type_t), &s) != 0) goto error;

#if PyObjC_BUILD_RELEASE >= 1013
    if (@available(macOS 10.13, *)) {
        s = DISPATCH_SOURCE_TYPE_DATA_REPLACE; if (add_constant(m, "DISPATCH_SOURCE_TYPE_DATA_REPLACE", @encode(dispatch_source_type_t), &s) != 0) goto error;
    }
#endif


    s = DISPATCH_SOURCE_TYPE_WRITE; if (add_constant(m, "DISPATCH_SOURCE_TYPE_MACH_SEND", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_MACH_RECV; if (add_constant(m, "DISPATCH_SOURCE_TYPE_MACH_RECV", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_MEMORYPRESSURE; if (add_constant(m, "DISPATCH_SOURCE_TYPE_MEMORYPRESSURE", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_PROC; if (add_constant(m, "DISPATCH_SOURCE_TYPE_PROC", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_READ; if (add_constant(m, "DISPATCH_SOURCE_TYPE_READ", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_SIGNAL; if (add_constant(m, "DISPATCH_SOURCE_TYPE_SIGNAL", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_TIMER; if (add_constant(m, "DISPATCH_SOURCE_TYPE_TIMER", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_VNODE; if (add_constant(m, "DISPATCH_SOURCE_TYPE_VNODE", @encode(dispatch_source_type_t), &s) != 0) goto error;
    s = DISPATCH_SOURCE_TYPE_WRITE; if (add_constant(m, "DISPATCH_SOURCE_TYPE_WRITE", @encode(dispatch_source_type_t), &s) != 0) goto error;

    /*
     * Register a number of struct pointer types that are actually Objective-C objects
     */
    if (PyObjCPointerWrapper_RegisterID("dispatch_queue_t", "^{dispatch_queue_s=}") < 0) goto error;
    if (PyObjCPointerWrapper_RegisterID("dispatch_data_t", "^{dispatch_data_s=}") < 0) goto error;
    if (PyObjCPointerWrapper_RegisterID("dispatch_io_t", "^{dispatch_io_s=}") < 0) goto error;
    if (PyObjCPointerWrapper_RegisterID("dispatch_queue_attr_t", "^{dispatch_queue_attr_s=}") < 0) goto error;
    if (PyObjCPointerWrapper_RegisterID("dispatch_semaphore_t", "^{dispatch_semaphore_s=}") < 0) goto error;

    PyObjC_INITDONE();

error:
    PyObjC_INITERROR();

}
