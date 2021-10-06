#include "pyobjc.h"
NS_ASSUME_NONNULL_BEGIN

/*
 * XXX: Vectorcall variants for as_tuple and as_buffer
 *
 * Both should be fairly easy as there is only one argument,
 * although supporting keyword arguments complicates things.
 */

typedef struct {
    PyObject_HEAD

    void*      array;
    Py_ssize_t itemsize;
    char       typestr[];
} PyObjC_VarList;

PyDoc_STRVAR(object_as_tuple_doc,
             "as_tuple(count)\n" CLINIC_SEP "\n"
             "Return a tuple containing the first ``count`` elements of "
             "this list");

static int
check_index(PyObjC_VarList* self, Py_ssize_t idx)
{
    if (idx < 0) {
        /* Indeterminate size, cannot access from the 'end' */
        PyErr_SetString(PyExc_ValueError, "objc.varlist does not support negative indexes");
        return -1;
    }

    if (idx >= PY_SSIZE_T_MAX / self->itemsize) {
        /* Integer overflow, index cannot be correct */
        PyErr_Format(PyExc_IndexError, "Index '%" PY_FORMAT_SIZE_T "d' out of range",
                     idx);
        return -1;
    }
    return 0;
}

static PyObject* _Nullable
object_as_tuple(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"count", NULL};

    PyObjC_VarList* self = (PyObjC_VarList*)_self;

    Py_ssize_t i, length;
    PyObject*  result;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "n", keywords, &length)) {
        return NULL;
    }

    if (length >= PY_SSIZE_T_MAX / self->itemsize) {
        /* Integer overflow, index cannot be correct */
        PyErr_Format(PyExc_OverflowError, "Index '%" PY_FORMAT_SIZE_T "d' out of range",
                     length);
        return NULL;
    }

    result = PyTuple_New(length);
    if (result == NULL) {
        return NULL;
    }

    for (i = 0; i < length; i++) {
        PyObject* v = pythonify_c_value(self->typestr, ((unsigned char*)self->array)
                                                                + (i * self->itemsize));
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SET_ITEM(result, i, v);
    }
    return result;
}


PyDoc_STRVAR(object_as_buffer_doc,
             "as_buffer(count)\n" CLINIC_SEP "\n"
             "Return a memoryview referencing the memory for the first ``count`` "
             "elements of this list.");

static PyObject* _Nullable
object_as_buffer(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"count", NULL};

    PyObjC_VarList* self = (PyObjC_VarList*)_self;

    Py_ssize_t buffer_size, length;
    Py_buffer  info;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "n", keywords, &length)) {
        return NULL;
    }

    if (length >= PY_SSIZE_T_MAX / self->itemsize) {
        /* Calculating the buffer size would overflow */
        PyErr_Format(PyExc_OverflowError, "Index '%" PY_FORMAT_SIZE_T "d' out of range",
                     length);

        return NULL;
    }

    buffer_size = length * self->itemsize;

    if (PyBuffer_FillInfo(&info, _self, self->array, buffer_size, 0, PyBUF_FULL) < 0) {
        return NULL;
    }

    return PyMemoryView_FromBuffer(&info);
}


static PyObject* _Nullable
object__getitem__(PyObject* _self, Py_ssize_t idx)
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;

    if (check_index(self, idx) == -1) {
        return NULL;
    }

    return pythonify_c_value(self->typestr,
                             ((unsigned char*)self->array) + (idx * self->itemsize));
}


static PyObject* _Nullable
object__getslice__(PyObject* _self, Py_ssize_t start, Py_ssize_t stop)
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;
    PyObject*       result;
    Py_ssize_t      idx;

    if (check_index(self, start) == -1) {
        return NULL;
    }

    if (check_index(self, stop) == -1) {
        return NULL;
    }

    if (stop < start) {
        stop = start;
    }

    result = PyTuple_New(stop - start);

    for (idx = start; idx < stop; idx++) {
        PyObject* v = pythonify_c_value(self->typestr, ((unsigned char*)self->array)
                                                                + (idx * self->itemsize));
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
    Py_ssize_t      idx;
    PyObject*       seq;

    if (check_index(self, start) == -1) {
        return -1;
    }

    if (check_index(self, stop) == -1) {
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
        PyObject* v = PySequence_Fast_GET_ITEM(seq, idx - start);
        int r = depythonify_c_value(self->typestr, v,
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
object__setitem__(PyObject* _self, Py_ssize_t idx, PyObject* _Nullable value)
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;

    if (check_index(self, idx) == -1) {
        return -1;
    }

    return depythonify_c_value(self->typestr, value,
                               ((unsigned char*)self->array) + (idx * self->itemsize));
}

static PySequenceMethods object_tp_as_list = {
    .sq_item     = object__getitem__,
    .sq_ass_item = object__setitem__,
};

static Py_ssize_t
sl_ind_get(PyObject* value, int is_start)
{

    if (value == Py_None) {
        /* Unspecified index, this is only supported for the start
         * index (as we only support step size 1).
         */
        if (is_start) {
            return 0;
        } else {
            PyErr_SetString(PyExc_ValueError, "Slice end must be specified");
            return -1;
        }

    } else if (PyIndex_Check(value)) {
        return PyNumber_AsSsize_t(value, PyExc_IndexError);

    } else {
        PyErr_Format(PyExc_ValueError, "Slice index of unsupported type '%.200s'",
                     Py_TYPE(value)->tp_name);
        return -1;
    }
}

static PyObject* _Nullable
object_subscript(PyObject* self, PyObject* item)
{
    if (PyIndex_Check(item)) {
        Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);
        if (i == -1 && PyErr_Occurred()) {
            return NULL;
        }
        return object__getitem__(self, i);

    } else if (PySlice_Check(item)) {
        Py_ssize_t     start, stop, step;
        PySliceObject* sl = (PySliceObject*)item;

        start = sl_ind_get(sl->start, 1);
        if (start == -1 && PyErr_Occurred()) {
            return NULL;
        }

        stop = sl_ind_get(sl->stop, 0);
        if (stop == -1 && PyErr_Occurred()) {
            return NULL;
        }

        if (sl->step == Py_None) {
            step = 1;
        } else {
            step = sl_ind_get(sl->step, 0);
            if (step == -1 && PyErr_Occurred()) {
                return NULL;
            }
        }

        if (step != 1) {
            /* XXX: Might be cool to support other steps... */
            PyErr_Format(PyExc_ValueError,
                         "objc.varlist doesn't support slice steps other than 1");
            return NULL;
        }

        return object__getslice__(self, start, stop);

    } else {
        PyErr_Format(PyExc_TypeError, "objc.varlist indices must be integers, got %.200s",
                     Py_TYPE(item)->tp_name);
        return NULL;
    }
}

static int
object_ass_subscript(PyObject* self, PyObject* item, PyObject* _Nullable value)
{
    if (PyIndex_Check(item)) {
        Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);
        if (i == -1 && PyErr_Occurred()) {
            return -1;
        }
        return object__setitem__(self, i, value);

    } else if (PySlice_Check(item)) {
        Py_ssize_t     start, stop, step;
        PySliceObject* sl = (PySliceObject*)item;

        start = sl_ind_get(sl->start, 1);
        if (start == -1 && PyErr_Occurred()) {
            return -1;
        }

        stop = sl_ind_get(sl->stop, 0);
        if (stop == -1 && PyErr_Occurred()) {
            return -1;
        }

        if (sl->step == Py_None) {
            step = 1;
        } else {
            step = sl_ind_get(sl->step, 0);
            if (step == -1 && PyErr_Occurred()) {
                return -1;
            }
        }

        if (step != 1) {
            /* XXX: Might be cool to support other steps... */
            PyErr_Format(PyExc_ValueError,
                         "objc.varlist doesn't support slice steps other than 1");
            return -1;
        }

        return object__setslice__(self, start, stop, value);

    } else {
        PyErr_Format(PyExc_TypeError, "objc.varlist indices must be integers, got %.200s",
                     Py_TYPE(item)->tp_name);
        return -1;
    }
}

static PyMappingMethods object_tp_as_mapping = {.mp_subscript     = object_subscript,
                                                .mp_ass_subscript = object_ass_subscript};

static PyObject* _Nullable
object_new(PyTypeObject* type __attribute__((__unused__)),
           PyObject*     args __attribute__((__unused__)),
           PyObject*     kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError,
                    "Cannot create instances of 'objc.varlist'");
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
    "convert to a python tuple, or ``obj[index]`` to fetch a single item");

static PyObject* _Nullable
object_typestr_get(PyObject* _self, void* _Nullable closure __attribute__((__unused__)))
{
    PyObjC_VarList* self = (PyObjC_VarList*)_self;
    return PyBytes_FromString(self->typestr);
}

static PyGetSetDef object_getset[] = {
    {
        .name = "__typestr__",
        .get  = object_typestr_get,
        .doc  = "type encoding for elements of the array",
    },
    {
        .name = NULL /* SENTINEL */
    }};

static PyMethodDef object_methods[] = {{.ml_name  = "as_tuple",
                                        .ml_meth  = (PyCFunction)object_as_tuple,
                                        .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                        .ml_doc   = object_as_tuple_doc},
                                       {.ml_name  = "as_buffer",
                                        .ml_meth  = (PyCFunction)object_as_buffer,
                                        .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                        .ml_doc   = object_as_buffer_doc},
                                       {
                                           .ml_name = NULL /* SENTINEL */
                                       }};

PyTypeObject PyObjC_VarList_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.varlist",
    .tp_basicsize                                  = sizeof(PyObjC_VarList),
    .tp_itemsize                                   = 0,
    .tp_dealloc                                    = object_dealloc,
    .tp_as_sequence                                = &object_tp_as_list,
    .tp_as_mapping                                 = &object_tp_as_mapping,
    .tp_getattro                                   = PyObject_GenericGetAttr,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
    .tp_doc                                        = object_doc,
    .tp_methods                                    = object_methods,
    .tp_getset                                     = object_getset,
    .tp_new                                        = object_new,
};

PyObject*
PyObjC_VarList_New(const char* tp, void* array)
{
    PyObjC_VarList* result;
    const char*     end;

    end = PyObjCRT_SkipTypeSpec(tp);
    if (end == NULL) {
        return NULL;
    }
    while (end > tp && isdigit(end[-1])) {
        end--;
    }

    result = (PyObjC_VarList*)PyObject_Malloc(_PyObject_SIZE(&PyObjC_VarList_Type)
                                              + (end - tp) + 1);
    if (result == NULL) {
        return NULL;
    }
    PyObject_Init((PyObject*)result, &PyObjC_VarList_Type);
    result->array    = array;
    result->itemsize = PyObjCRT_AlignedSize(tp);
    if (unlikely(result->itemsize == -1)) {
        Py_DECREF(result);
        return NULL;
    }

    memcpy(result->typestr, tp, end - tp);
    result->typestr[end - tp] = '\0';

    if (result->typestr[0] == _C_VOID) {
        result->typestr[0] = _C_CHAR_AS_TEXT;
    }

    return (PyObject*)result;
}

NS_ASSUME_NONNULL_END
