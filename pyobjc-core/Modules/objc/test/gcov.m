#include "Python.h"
#include "pyobjc-api.h"

#include <CoreFoundation/CoreFoundation.h>

extern void __gcov_flush(void);

static PyObject*
do_flush(PyObject* m __attribute__((__unused__)))
{
#ifdef COVERAGE
    __gcov_flush();
#endif
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {{
                                        "flush",
                                        (PyCFunction)do_flush,
                                        METH_NOARGS,
                                        NULL,
                                    },
                                    {0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "gcov", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_gcov(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_gcov(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    return m;
}
