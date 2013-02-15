#include "pyobjc.h"

#define VARLIST_TYPE(obj) (((char*)(obj)) + sizeof(PyObjC_VarList))
typedef struct {
    PyObject_HEAD

    void* array;
    Py_ssize_t itemsize;
} PyObjC_VarList;

PyDoc_STRVAR(object_as_tuple_doc,
    "as_tuple(count)\n"
    "\n"
    "Return a tuple containing the first ``count`` elements of "
    "this list"
);

static PyObject*
object_as_tuple(PyObject* _self, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "count", NULL };

    PyObjC_VarList* self = (PyObjC_VarList*)_self;

    Py_ssize_t i, length;
    PyObject*  result;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "n", keywords, &length)) {
        return NULL;
    }

    result = PyTuple_New(length);
    if (result == NULL) {
        return NULL;
    }

    for (i = 0; i < length; i++) {
        PyObject* v = pythonify_c_value(VARLIST_TYPE(self), ((unsigned char*)self->array) + (i * self->itemsize));
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SET_ITEM(result, i, v);
    }
    return result;
}


static PyObject*
object__getitem__(PyObject* _self, Py_ssize_t idx)
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;

    return pythonify_c_value(VARLIST_TYPE(self), ((unsigned char*)self->array) + (idx * self->itemsize));
}

static PyObject*
object__getslice__(PyObject* _self, Py_ssize_t start, Py_ssize_t stop)
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;
    PyObject* result;
    Py_ssize_t idx;

    if (start < 0 || stop < 0) {
        PyErr_SetString(PyExc_ValueError,
            "objc.varlist doesn't support slices with negative indexes");
        return NULL;
    }
    if (stop < start) {
        stop = start;
    }

    result = PyTuple_New(stop - start);

    for (idx = start; idx < stop; idx++) {
        PyObject* v =  pythonify_c_value(
            VARLIST_TYPE(self),
            ((unsigned char*)self->array) + (idx * self->itemsize));
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SET_ITEM(result, idx - start, v);
    }

    return result;
}

static int
object__setslice__(PyObject* _self, Py_ssize_t start, Py_ssize_t stop, PyObject* newval)
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;
    Py_ssize_t idx;
    PyObject* seq;

    if (start < 0 || stop < 0) {
        PyErr_SetString(PyExc_ValueError,
            "objc.varlist doesn't support slices with negative indexes");
        return -1;
    }
    if (stop < start) {
        stop = start;
    }

    seq = PySequence_Fast(newval, "New value must be sequence");
    if (seq == NULL) {
        return -1;
    }

    if (PySequence_Fast_GET_SIZE(seq) != stop - start) {
        PyErr_SetString(PyExc_ValueError,
           "objc.varlist slice assignment doesn't support resizing");
        Py_DECREF(seq);
        return -1;
    }

    for (idx = start; idx < stop; idx++) {
        PyObject* v =  PySequence_Fast_GET_ITEM(seq, idx-start);
        int r = depythonify_c_value(
            VARLIST_TYPE(self),
            v,
            ((unsigned char*)self->array) + (idx * self->itemsize));
        if (r == -1) {
            Py_DECREF(seq);
            return -1;
        }
    }
    Py_DECREF(seq);
    return 0;
}

static int
object__setitem__(PyObject* _self, Py_ssize_t idx, PyObject* value)
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;

    return depythonify_c_value(VARLIST_TYPE(self), value, ((unsigned char*)self->array) + (idx * self->itemsize));
}

static PySequenceMethods object_tp_as_list = {
    .sq_item      = object__getitem__,
    .sq_ass_item  = object__setitem__,
#if PY_MAJOR_VERSION == 2
    .sq_slice     = object__getslice__,
    .sq_ass_slice = object__setslice__,
#endif
};

static Py_ssize_t
sl_ind_get(PyObject* value)
{

    if (value == Py_None) {
        return -1;

    } else if (PyIndex_Check(value)) {
        Py_ssize_t result;
        result = PyNumber_AsSsize_t(value, PyExc_IndexError);
        if (result == -1 && PyErr_Occurred()) {
            result = -1;
        }
        return result;

    } else {
        PyErr_Format(PyExc_ValueError,
            "Slice index of unsupported type '%.200s'", Py_TYPE(value)->tp_name);
        return -1;
    }
}

static PyObject*
object_subscript(PyObject* self, PyObject* item)
{
    if (PyIndex_Check(item)) {
        Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);
        if (i == -1 && PyErr_Occurred()) {
            return NULL;
        }
        return object__getitem__(self, i);

    } else if (PySlice_Check(item)) {
        Py_ssize_t start, stop, step;
        PySliceObject* sl = (PySliceObject*)item;

        start = sl_ind_get(sl->start);
        if (start == -1 && PyErr_Occurred()) {
            return NULL;
        }

        stop = sl_ind_get(sl->stop);
        if (stop == -1 && PyErr_Occurred()) {
            return NULL;
        }

        if (sl->step == Py_None) {
            step = 1;
        } else {
            step = sl_ind_get(sl->stop);
            if (step == -1 && PyErr_Occurred()) {
                return NULL;
            }
        }

        if (step != 1) {
            PyErr_Format(PyExc_ValueError,
                "objc.varlist doesn't support slice steps other than 1");
            return NULL;
        }

        return object__getslice__(self, start, stop);

    } else {
        PyErr_Format(PyExc_TypeError,
            "objc.varlist indices must be integers, got %.200s",
            Py_TYPE(item)->tp_name);
        return NULL;
    }
}

static int
object_ass_subscript(PyObject* self, PyObject* item, PyObject* value)
{
    if (PyIndex_Check(item)) {
        Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);
        if (i == -1 && PyErr_Occurred()) {
            return -1;
        }
        return object__setitem__(self, i, value);

    } else if (PySlice_Check(item)) {
        Py_ssize_t start, stop, step;
        PySliceObject* sl = (PySliceObject*)item;

        start = sl_ind_get(sl->start);
        if (start == -1 && PyErr_Occurred()) {
            return -1;
        }

        stop = sl_ind_get(sl->stop);
        if (stop == -1 && PyErr_Occurred()) {
            return -1;
        }

        if (sl->step == Py_None) {
            step = 1;
        } else {
            step = sl_ind_get(sl->stop);
            if (step == -1 && PyErr_Occurred()) {
                return -1;
            }
        }

        if (step != 1) {
            PyErr_Format(PyExc_ValueError,
                "objc.varlist doesn't support slice steps other than 1");
            return -1;
        }

        return object__setslice__(self, start, stop, value);

    } else {
        PyErr_Format(PyExc_TypeError,
            "objc.varlist indices must be integers, got %.200s",
            Py_TYPE(item)->tp_name);
        return -1;
    }
}

static PyMappingMethods  object_tp_as_mapping = {
    .mp_subscript     = object_subscript,
    .mp_ass_subscript = object_ass_subscript
};

static PyObject*
object_new(
    PyTypeObject* type __attribute__((__unused__)),
    PyObject* args __attribute__((__unused__)),
    PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError,
            "Cannot create instances of 'objc.varlist' in Python");
    return NULL;
}

static void
object_dealloc(PyObject* self)
{
    PyObject_Del(self);
}

PyDoc_STRVAR(object_doc,
    "objc.varlist\n"
    "\n"
    "A list of an unspecified size. Use ``obj.as_tuple(count)`` to \n"
    "convertto a python tuple, or ``obj[index]`` to fetch a single item"
);

static PyObject*
object_typestr_get(PyObject* self, void* closure __attribute__((__unused__)))
{
    return PyBytes_FromString(VARLIST_TYPE(self));
}

static PyGetSetDef object_getset[] = {
    {
        "__typestr__",
        object_typestr_get,
        0,
        "type encoding for elements of the array",
        0
    },
    { 0, 0, 0, 0, 0}
};

static PyMethodDef object_methods[] = {
        {
        "as_tuple",
        (PyCFunction)object_as_tuple,
        METH_VARARGS|METH_KEYWORDS,
        object_as_tuple_doc
    },

    { 0, 0, 0, 0 }
};

PyTypeObject PyObjC_VarList_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name            = "objc.varlist",
    .tp_basicsize       = sizeof(PyObjC_VarList),
    .tp_itemsize        = 0,
    .tp_dealloc         = object_dealloc,
    .tp_as_sequence     = &object_tp_as_list,
    .tp_as_mapping      = &object_tp_as_mapping,
    .tp_getattro        = PyObject_GenericGetAttr,
    .tp_flags           = Py_TPFLAGS_DEFAULT,
    .tp_doc             = object_doc,
    .tp_methods         = object_methods,
    .tp_getset          = object_getset,
    .tp_new             = object_new,
};

PyObject*
PyObjC_VarList_New(const char* tp, void* array)
{
    PyObjC_VarList* result;
    const char* end;
    char* tp_buf;

    end = PyObjCRT_SkipTypeSpec(tp);
    while (end > tp && isdigit(end[-1])) {
        end --;
    }

    result = (PyObjC_VarList*)PyObject_Malloc(_PyObject_SIZE(&PyObjC_VarList_Type) + (end-tp) + 1);
    if (result == NULL) {
        return NULL;
    }
    PyObject_Init((PyObject*)result, &PyObjC_VarList_Type);
    tp_buf = VARLIST_TYPE(result);
    result->array = array;
    result->itemsize = PyObjCRT_AlignedSize(tp);
    memcpy(tp_buf, tp, end-tp);
    tp_buf[end-tp] = '\0';

    if (*tp_buf == _C_VOID) {
        *tp_buf = _C_CHAR_AS_TEXT;
    }

    return (PyObject*)result;
}
