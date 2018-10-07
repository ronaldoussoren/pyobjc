#include "pyobjc.h"

#if PY_MAJOR_VERSION == 3
/* A basic wrapper for C's "FILE*"
 * that implements a usable API.
 */

struct file_object {
    PyObject_HEAD

    FILE* fp;
};


static PyObject*
file_new(
    PyTypeObject* type __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "path", "mode", NULL };
    FILE* fp;
    char* fname;
    char* mode;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "ss", keywords, &fname, &mode)) {
        return NULL;
    }


    fp = fopen(fname, mode);

    if (fp == NULL) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    return FILE_create(fp);
}

static void
file_dealloc(PyObject* self)
{
    /* Don't close the file, we don't own the
     * FILE* reference.
     */
    PyObject_Free(self);
}


static PyObject*
file_close(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closing closed file");
        return NULL;
    }

    if (fclose(self->fp) < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    self->fp = NULL;

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
file_errors(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    int result;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closing closed file");
        return NULL;
    }

    result = ferror(self->fp);

    return PyBool_FromLong(result);
}

static PyObject*
file_at_eof(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    int result;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closing closed file");
        return NULL;
    }

    result = feof(self->fp);

    return PyBool_FromLong(result);
}

static PyObject*
file_tell(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    long offset;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closing closed file");
        return NULL;
    }

    offset = ftell(self->fp);
    if (offset < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    return PyLong_FromLong(offset);
}

static PyObject*
file_seek(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "offset", "whence", NULL };

    struct file_object* self = (struct file_object*)_self;
    Py_ssize_t offset;
    int whence;
    long result;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closed file");
        return NULL;
    }

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "ni", keywords, &offset, &whence)) {
        return NULL;
    }

    result = fseek(self->fp, offset, whence);
    if (result < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
file_fileno(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    int fd;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closing closed file");
        return NULL;
    }

    fd = fileno(self->fp);
    if (fd < 0) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    return PyLong_FromLong(fd);
}

static PyObject*
file_write(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "buffer", NULL };

    struct file_object* self = (struct file_object*)_self;
    void* buffer;
    Py_ssize_t buffer_size;
    size_t result;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closed file");
        return NULL;
    }

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "y#", keywords, &buffer, &buffer_size)) {
        return NULL;
    }

    result = fwrite(buffer, 1, buffer_size, self->fp);
    return Py_BuildValue("k", (unsigned long)result);
}

static PyObject*
file_readline(PyObject* _self)
{
    struct file_object* self = (struct file_object*)_self;
    char buffer[2048];
    char* result;

    result = fgets(buffer, 2048, self->fp);
    if (result == NULL) {
        return PyBytes_FromStringAndSize("", 0);
    } else {
        return PyBytes_FromString(result);
    }
}

static PyObject*
file_read(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = { "size", NULL };

    struct file_object* self = (struct file_object*)_self;
    PyObject* buffer;
    Py_ssize_t buffer_size;
    size_t result;

    if (self->fp == NULL) {
        PyErr_SetString(PyExc_ValueError, "Closed file");
        return NULL;
    }

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "n", keywords, &buffer_size)) {
        return NULL;
    }

    buffer = PyBytes_FromStringAndSize(NULL, buffer_size);
    if (buffer == NULL) {
        return NULL;
    }

    result = fread(PyBytes_AsString(buffer), 1, buffer_size, self->fp);

    _PyBytes_Resize(&buffer, result);
    return buffer;
}

static PyMethodDef file_methods[] = {
    {
        .ml_name    = "readline",
        .ml_meth    = (PyCFunction)file_readline,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "read a line from the file"
    },
    {
        .ml_name    = "read",
        .ml_meth    = (PyCFunction)file_read,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = "read from the file"
    },
    {
        .ml_name    = "write",
        .ml_meth    = (PyCFunction)file_write,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = "write to the file"
    },
    {
        .ml_name    = "seek",
        .ml_meth    = (PyCFunction)file_seek,
        .ml_flags   = METH_VARARGS|METH_KEYWORDS,
        .ml_doc     = "write to the file"
    },
    {
        .ml_name    = "has_errors",
        .ml_meth    = (PyCFunction)file_errors,
        .ml_flags   = METH_NOARGS,
    },
    {
        .ml_name    = "at_eof",
        .ml_meth    = (PyCFunction)file_at_eof,
        .ml_flags   = METH_NOARGS,
    },
    {
        .ml_name    = "tell",
        .ml_meth    = (PyCFunction)file_tell,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "write to the file"
    },
    {
        .ml_name    = "fileno",
        .ml_meth    = (PyCFunction)file_fileno,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "write to the file"
    },
    {
        .ml_name    = "close",
        .ml_meth    = (PyCFunction)file_close,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "close the file"
    },

    {   .ml_name = NULL, /* Sentinel */ }
};

PyTypeObject FILE_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.FILE",
    .tp_basicsize   = sizeof (struct file_object),
    .tp_itemsize    = 0,
    .tp_new         = file_new,
    .tp_dealloc     = file_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = "Wrapper around a FILE* object",
    .tp_methods     = file_methods,
};

PyObject* FILE_create(FILE* fp)
{
    struct file_object* self;
    if (fp == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    self = PyObject_NEW(struct file_object, &FILE_Type);
    self->fp = fp;
    return (PyObject*)self;
}


FILE* FILE_get(PyObject* fp)
{
    if (!FILE_Check(fp)) {
        PyErr_SetString(PyExc_TypeError, "Not a FILE wrapper");
        return NULL;
    }

    return ((struct file_object*)fp)->fp;
}

#endif
