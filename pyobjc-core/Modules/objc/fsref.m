/*
 * A custom wrapper for the (opaque) FSRef structure.
 */
#include "pyobjc.h"
#import <CoreServices/CoreServices.h>

NS_ASSUME_NONNULL_BEGIN

#pragma GCC diagnostic   ignored "-Wdeprecated-declarations"
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

/*
 * Interface of the FSRef type:
 *
 * FSRef.from_pathname(value)
 *   # -> returns new FSRef instance for posix path 'value'
 *
 * aref.as_pathname()
 *  # -> returns a Unicode string with the posix path
 *
 * aref.as_carbon()
 *  # -> return a Carbon.File.FSRef instance (only
 *  #    available when Carbon support is enabled in Python)
 *
 * aref.data
 *  # -> read-only property with the bytes in the FSRef
 */

typedef struct {
    PyObject_HEAD

    FSRef ref;
} PyObjCFSRefObject;

static PyObject* _Nullable fsref_as_bytes(PyObject* ref, void* _Nullable closure
                                          __attribute__((__unused__)))
{
    return PyBytes_FromStringAndSize((char*)&((PyObjCFSRefObject*)ref)->ref,
                                     sizeof(FSRef));
}

static PyObject* _Nullable fsref_sizeof(PyObject* ref)
{
    return PyLong_FromSsize_t(Py_TYPE(ref)->tp_basicsize);
}

static PyObject* _Nullable fsref_as_path(PyObject* ref)
{
    OSStatus rc;
    UInt8    buffer[1024];

    rc = FSRefMakePath(&((PyObjCFSRefObject*)ref)->ref, buffer, sizeof(buffer));
    if (rc != 0) {
        PyErr_Format(PyExc_OSError, "MAC Error %d", rc);

        return NULL;
    }

    return PyUnicode_DecodeFSDefault((char*)buffer);
}

static PyObject* _Nullable fsref_from_path(PyObject* self __attribute__((__unused__)),
                                           PyObject* path)
{
    PyObject* value;
    FSRef     result;
    Boolean   isDirectory;
    OSStatus  rc;

    if (!PyUnicode_Check(path)) {
        PyErr_SetString(PyExc_TypeError, "Expecting string");
        return NULL;
    }

    value = PyUnicode_EncodeFSDefault(path);
    if (value == NULL)
        return NULL;
    PyObjC_Assert(PyBytes_Check(value), NULL);

    rc = FSPathMakeRef((UInt8*)PyBytes_AsString(value), &result, &isDirectory);
    Py_DECREF(value);
    if (rc != 0) {
        PyErr_Format(PyExc_OSError, "MAC Error %d", rc);
        return NULL;
    }

    return PyObjC_decode_fsref(&result);
}

#if PY_VERSION_HEX < 0x030a0000
static PyObject* _Nullable fsref_new(PyObject* self __attribute__((__unused__)),
                                     PyObject* args __attribute__((__unused__)),
                                     PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "cannot create 'objc.FSRef' instances");
    return NULL;
}
#endif

static PyGetSetDef fsref_getset[] = {{
                                         .name = "data",
                                         .get  = fsref_as_bytes,
                                         .doc  = "bytes in the FSRef",
                                     },
                                     {
                                         .name = NULL /* SENTINEL */
                                     }};

static PyMethodDef fsref_methods[] = {
    {.ml_name  = "as_pathname",
     .ml_meth  = (PyCFunction)fsref_as_path,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "as_pathname()\n" CLINIC_SEP "\nReturn POSIX path for this object"},
    {.ml_name  = "from_pathname",
     .ml_meth  = (PyCFunction)fsref_from_path,
     .ml_flags = METH_O | METH_CLASS,
     .ml_doc =
         "from_pathname(path)\n" CLINIC_SEP "\nCreate FSRef instance for an POSIX path"},

    {
        .ml_name  = "__sizeof__",
        .ml_meth  = (PyCFunction)fsref_sizeof,
        .ml_flags = METH_NOARGS,
    },
    {
        .ml_name = NULL /* SENTINEL */
    }};

static PyType_Slot fsref_slots[] = {
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_setattro, .pfunc = (void*)&PyObject_GenericSetAttr},
    {.slot = Py_tp_methods, .pfunc = (void*)&fsref_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&fsref_getset},
#if PY_VERSION_HEX < 0x030a0000
    {.slot = Py_tp_new, .pfunc = (void*)&fsref_new},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec fsref_spec = {
    .name      = "objc.FSRef",
    .basicsize = sizeof(PyObjCFSRefObject),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif

    .slots = fsref_slots,
};

PyObject* PyObjCFSRef_Type;

int
PyObjC_encode_fsref(PyObject* value, void* buffer)
{
    if (PyObjCFSRef_Check(value)) {
        *(FSRef*)buffer = ((PyObjCFSRefObject*)value)->ref;
        return 0;
    }

    PyErr_SetString(PyExc_ValueError, "Cannot convert value to FSRef");
    return -1;
}

PyObject* _Nullable PyObjC_decode_fsref(const void* buffer)
{
    PyObjCFSRefObject* result =
        PyObject_New(PyObjCFSRefObject, (PyTypeObject*)PyObjCFSRef_Type);

    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    result->ref = *(const FSRef*)buffer;
    return (PyObject*)result;
}

int
PyObjCFSRef_Setup(PyObject* module)
{
    PyObject* tmp = PyType_FromSpec(&fsref_spec);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }
    PyObjCFSRef_Type = tmp;

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "FSRef", PyObjCFSRef_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCFSRef_Type);
    return 0;
}

NS_ASSUME_NONNULL_END
