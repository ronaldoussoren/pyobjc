#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/* A basic wrapper for C's "FILE*"
 * that implements a usable API.
 *
 * NOTE: The locking using critical section is not very fine grained,
 * but that shouldn't be a problem given how little FILE* objects
 * are used in Objective-C APIs.
 */

static PyObject* FILE_Type;

#define FILE_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)FILE_Type)

struct file_object {
    PyObject_HEAD

    FILE* _Nullable fp;
};

static PyObject* _Nullable file_new(PyTypeObject* type __attribute__((__unused__)),
                                    PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"path", "mode", NULL};
    FILE*        fp;
    char*        fname;
    char*        mode;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "ss", keywords, &fname, &mode)) {
        return NULL;
    }

    fp = fopen(fname, mode);

    if (fp == NULL) {
        return PyErr_SetFromErrno(PyExc_OSError);
    }

    CLANG_SUPPRESS /* leaking 'fopen' result */
        return FILE_create(fp);
}

static void
file_dealloc(PyObject* self)
{
    /* Don't close the file, we don't own the
     * FILE* reference.
     */
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(self);
#endif
    PyObject_Free(self);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

static PyObject* _Nullable file_close(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    FILE*               fp;

    Py_BEGIN_CRITICAL_SECTION(_self);
    fp       = self->fp;
    self->fp = NULL;
    Py_END_CRITICAL_SECTION();

    if (fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closing closed file");
        return NULL;
    }

    if (fclose(fp) < 0) {
        /* This is very unlikely, restore previous value */
        Py_BEGIN_CRITICAL_SECTION(_self);
        self->fp = fp;
        Py_END_CRITICAL_SECTION();
        return PyErr_SetFromErrno(PyExc_OSError);
    }

    Py_RETURN_NONE;
}

static PyObject* _Nullable file_flush(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    PyObject*           retval;
    int                 result;

    Py_BEGIN_CRITICAL_SECTION(_self);

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        retval = NULL;
    } else {
        result = fflush(self->fp);
        if (result != 0) {
            retval = PyErr_SetFromErrno(PyExc_OSError);
        } else {
            Py_INCREF(Py_None);
            retval = Py_None;
        }
    }
    Py_END_CRITICAL_SECTION();
    return retval;
}

static PyObject* _Nullable file_errors(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    int                 result;

    Py_BEGIN_CRITICAL_SECTION(_self);

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        result = -1;
    } else {
        result = ferror(self->fp) != 0;
    }

    Py_END_CRITICAL_SECTION();

    switch (result) {
    case -1:
        return NULL;
    case 0:
        Py_RETURN_FALSE;
    default:
        Py_RETURN_TRUE;
    }
}

static PyObject* _Nullable file_at_eof(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    int                 result;

    Py_BEGIN_CRITICAL_SECTION(_self);

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        result = -1;
    } else {
        result = feof(self->fp) != 0;
    }
    Py_END_CRITICAL_SECTION();

    switch (result) {
    case -1:
        return NULL;
    case 0:
        Py_RETURN_FALSE;
    default:
        Py_RETURN_TRUE;
    }
}

static PyObject* _Nullable file_tell(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    long                offset;
    PyObject*           retval;

    Py_BEGIN_CRITICAL_SECTION(_self);
    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        retval = NULL;
    } else {
        offset = ftell(self->fp);
        if (offset < 0) {
            retval = PyErr_SetFromErrno(PyExc_OSError);
        } else {
            retval = PyLong_FromLong(offset);
        }
    }
    Py_END_CRITICAL_SECTION();
    return retval;
}

static PyObject* _Nullable file_seek(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"offset", "whence", NULL};

    struct file_object* self = (struct file_object*)_self;
    Py_ssize_t          offset;
    int                 whence;
    long                result;
    PyObject*           retval;

    Py_BEGIN_CRITICAL_SECTION(_self);
    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        retval = NULL;
    } else if (!PyArg_ParseTupleAndKeywords(args, kwds, "ni", keywords, &offset,
                                            &whence)) {
        retval = NULL;
    } else {
        result = fseek(self->fp, offset, whence);
        if (result < 0) {
            retval = PyErr_SetFromErrno(PyExc_OSError);
        } else {
            Py_INCREF(Py_None);
            retval = Py_None;
        }
    }
    Py_END_CRITICAL_SECTION();

    return retval;
}

static PyObject* _Nullable file_fileno(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    int                 fd;
    PyObject*           retval;

    Py_BEGIN_CRITICAL_SECTION(_self);
    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        retval = NULL;
    } else {
        fd = fileno(self->fp);
        /* According to the manpage this function cannot fail */

        retval = PyLong_FromLong(fd);
    }
    Py_END_CRITICAL_SECTION();
    return retval;
}

static PyObject* _Nullable file_write(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"buffer", NULL};

    struct file_object* self = (struct file_object*)_self;
    void*               buffer;
    Py_ssize_t          buffer_size;
    size_t              result;
    PyObject*           retval;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "y#", keywords, &buffer, &buffer_size)) {
        return NULL;
    }

    Py_BEGIN_CRITICAL_SECTION(_self);
    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        retval = NULL;
    } else {
        result = fwrite(buffer, 1, buffer_size, self->fp);
        retval = PyLong_FromSize_t(result);
    }
    Py_END_CRITICAL_SECTION();
    return retval;
}

static PyObject* _Nullable file_readline(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    char                buffer[2048];
    char*               result;
    PyObject*           retval;

    Py_BEGIN_CRITICAL_SECTION(_self);
    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        Py_EXIT_CRITICAL_SECTION();
        return NULL;
    } else {
        result = fgets(buffer, 2048, self->fp);
        if (result == NULL) {
            retval = PyBytes_FromStringAndSize("", 0);
        } else {
            retval = PyBytes_FromString(result);
        }
    }
    Py_END_CRITICAL_SECTION();
    return retval;
}

static PyObject* _Nullable file_read(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"size", NULL};

    struct file_object* self = (struct file_object*)_self;
    PyObject*           buffer;
    Py_ssize_t          buffer_size;
    size_t              result;

    Py_BEGIN_CRITICAL_SECTION(_self);

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Using closed file");
        buffer = NULL;
    } else if (!PyArg_ParseTupleAndKeywords(args, kwds, "n", keywords, &buffer_size)) {
        buffer = NULL;
    } else {
        buffer = PyBytes_FromStringAndSize(NULL, buffer_size);
        if (buffer != NULL) {
            result = fread(PyBytes_AsString(buffer), 1, buffer_size, self->fp);

            _PyBytes_Resize(&buffer, result);
        }
    }
    Py_END_CRITICAL_SECTION();
    return buffer;
}

static PyMethodDef file_methods[] = {{.ml_name  = "readline",
                                      .ml_meth  = (PyCFunction)file_readline,
                                      .ml_flags = METH_NOARGS,
                                      .ml_doc   = "read a line from the file"},
                                     {.ml_name  = "read",
                                      .ml_meth  = (PyCFunction)file_read,
                                      .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                      .ml_doc   = "read from the file"},
                                     {.ml_name  = "write",
                                      .ml_meth  = (PyCFunction)file_write,
                                      .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                      .ml_doc   = "write to the file"},
                                     {.ml_name  = "seek",
                                      .ml_meth  = (PyCFunction)file_seek,
                                      .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                      .ml_doc   = "write to the file"},
                                     {
                                         .ml_name  = "has_errors",
                                         .ml_meth  = (PyCFunction)file_errors,
                                         .ml_flags = METH_NOARGS,
                                     },
                                     {
                                         .ml_name  = "at_eof",
                                         .ml_meth  = (PyCFunction)file_at_eof,
                                         .ml_flags = METH_NOARGS,
                                     },
                                     {.ml_name  = "tell",
                                      .ml_meth  = (PyCFunction)file_tell,
                                      .ml_flags = METH_NOARGS,
                                      .ml_doc   = "write to the file"},
                                     {.ml_name  = "fileno",
                                      .ml_meth  = (PyCFunction)file_fileno,
                                      .ml_flags = METH_NOARGS,
                                      .ml_doc   = "write to the file"},
                                     {.ml_name  = "flush",
                                      .ml_meth  = (PyCFunction)file_flush,
                                      .ml_flags = METH_NOARGS,
                                      .ml_doc   = "flush the file buffers"},
                                     {.ml_name  = "close",
                                      .ml_meth  = (PyCFunction)file_close,
                                      .ml_flags = METH_NOARGS,
                                      .ml_doc   = "close the file"},

                                     {.ml_name = NULL,
                                      /* Sentinel */}};

PyDoc_STRVAR(file_doc, "Wrapper around a FILE* object");

static PyType_Slot file_slots[] = {
    {.slot = Py_tp_new, .pfunc = (void*)&file_new},
    {.slot = Py_tp_dealloc, .pfunc = (void*)&file_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&file_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&file_methods},

    {0, NULL} /* sentinel */
};

static PyType_Spec file_spec = {
    .name      = "objc.FILE",
    .basicsize = sizeof(struct file_object),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = file_slots,
};

PyObject* _Nullable FILE_create(FILE* fp)
{
    struct file_object* self;

    assert(fp != NULL);

    self = PyObject_NEW(struct file_object, (PyTypeObject*)FILE_Type);
    if (self == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }
    self->fp = fp;
    return (PyObject*)self;
}

FILE* _Nullable FILE_get(PyObject* fp)
{
    if (!FILE_Check(fp)) {
        PyErr_Format(PyExc_TypeError, "Expecting objc.FILE, got %.100s",
                     Py_TYPE(fp)->tp_name);
        return NULL;
    }

    return ((struct file_object*)fp)->fp;
}

int
FILE_Setup(PyObject* module)
{
    FILE_Type = PyType_FromSpec(&file_spec);
    if (FILE_Type == NULL) { // LCOV_BR_EXCL_LINE
        return -1;           // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(module, "FILE", FILE_Type) == -1) { // LCOV_BR_EXCL_LINE
        return -1;                                             // LCOV_EXCL_LINE
    }
    Py_INCREF(FILE_Type);

    return 0;
}

NS_ASSUME_NONNULL_END
