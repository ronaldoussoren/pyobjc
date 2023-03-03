#include "pyobjc.h"
NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyObject_HEAD

    void*      array;
    Py_ssize_t itemsize;
    char       typestr[];
} PyObjCVarList;

#if PY_VERSION_HEX < 0x030a0000
static PyObject* _Nullable varlist_new(PyObject* self __attribute__((__unused__)),
                                       PyObject* args __attribute__((__unused__)),
                                       PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "cannot create 'objc.varlist' instances");
    return NULL;
}
#endif

PyDoc_STRVAR(varlist_as_tuple_doc,
             "as_tuple(count)\n" CLINIC_SEP "\n"
             "Return a tuple containing the first ``count`` elements of "
             "this list");

static int
check_index(PyObjCVarList* self, Py_ssize_t idx)
{
    if (idx < 0) {
        /* Indeterminate size, cannot access from the 'end' */
        PyErr_SetString(PyExc_ValueError,
                        "objc.varlist does not support negative indexes");
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

static PyObject* _Nullable varlist_as_tuple(PyObject* _self, PyObject* args,
                                            PyObject* kwds)
{
    static char* keywords[] = {"count", NULL};

    PyObjCVarList* self = (PyObjCVarList*)_self;

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
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
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

PyDoc_STRVAR(varlist_as_buffer_doc,
             "as_buffer(count)\n" CLINIC_SEP "\n"
             "Return a memoryview referencing the memory for the first ``count`` "
             "elements of this list.");

static PyObject* _Nullable varlist_as_buffer(PyObject* _self, PyObject* args,
                                             PyObject* kwds)
{
    static char* keywords[] = {"count", NULL};

    PyObjCVarList* self = (PyObjCVarList*)_self;

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

    if (PyBuffer_FillInfo( // LCOV_BR_EXCL_LINE
            &info, _self, self->array, buffer_size, 0, PyBUF_FULL)
        < 0) {
        return NULL; // LCOV_EXCL_LINE
    }

    return PyMemoryView_FromBuffer(&info);
}

static PyObject* _Nullable varlist__getitem__(PyObject* _self, Py_ssize_t idx)
{
    PyObjCVarList* self = (PyObjCVarList*)_self;

    if (check_index(self, idx) == -1) {
        return NULL;
    }

    return pythonify_c_value(self->typestr,
                             ((unsigned char*)self->array) + (idx * self->itemsize));
}

static PyObject* _Nullable varlist__getslice__(PyObject* _self, Py_ssize_t start,
                                               Py_ssize_t stop)
{
    PyObjCVarList* self = (PyObjCVarList*)_self;
    PyObject*      result;
    Py_ssize_t     idx;

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
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

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
varlist__setslice__(PyObject* _self, Py_ssize_t start, Py_ssize_t stop, PyObject* newval)
{
    PyObjCVarList* self = (PyObjCVarList*)_self;
    Py_ssize_t     idx;
    PyObject*      seq;

    if (check_index(self, start) == -1) {
        return -1;
    }

    if (check_index(self, stop) == -1) {
        return -1;
    }

    if (stop < start) {
        stop = start;
    }

    seq = PySequence_Fast(newval, "New value must be a sequence");
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
        int       r = depythonify_c_value(
            self->typestr, v, ((unsigned char*)self->array) + (idx * self->itemsize));
        if (r == -1) {
            Py_DECREF(seq);
            return -1;
        }
    }
    Py_DECREF(seq);
    return 0;
}

static int
varlist__setitem__(PyObject* _self, Py_ssize_t idx, PyObject* _Nullable value)
{
    PyObjCVarList* self = (PyObjCVarList*)_self;

    if (check_index(self, idx) == -1) {
        return -1;
    }

    return depythonify_c_value(self->typestr, value,
                               ((unsigned char*)self->array) + (idx * self->itemsize));
}

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

static PyObject* _Nullable varlist_subscript(PyObject* self, PyObject* item)
{
    if (PyIndex_Check(item)) {
        Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);
        if (i == -1 && PyErr_Occurred()) {
            return NULL;
        }
        return varlist__getitem__(self, i);

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
            PyErr_Format(PyExc_ValueError,
                         "objc.varlist doesn't support slice steps other than 1");
            return NULL;
        }

        return varlist__getslice__(self, start, stop);

    } else {
        PyErr_Format(PyExc_TypeError, "objc.varlist indices must be integers, got %.200s",
                     Py_TYPE(item)->tp_name);
        return NULL;
    }
}

static int
varlist_ass_subscript(PyObject* self, PyObject* item, PyObject* _Nullable value)
{
    if (PyIndex_Check(item)) {
        Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);
        if (i == -1 && PyErr_Occurred()) {
            return -1;
        }
        return varlist__setitem__(self, i, value);

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
            PyErr_Format(PyExc_ValueError,
                         "objc.varlist doesn't support slice steps other than 1");
            return -1;
        }

        return varlist__setslice__(self, start, stop, value);

    } else {
        PyErr_Format(PyExc_TypeError, "objc.varlist indices must be integers, got %.200s",
                     Py_TYPE(item)->tp_name);
        return -1;
    }
}

static void
varlist_dealloc(PyObject* self)
{
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(self);
#endif
    PyObject_Del(self);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

PyDoc_STRVAR(varlist_doc,
             "objc.varlist\n"
             "\n"
             "A list of an unspecified size. Use ``obj.as_tuple(count)`` to \n"
             "convert to a python tuple, or ``obj[index]`` to fetch a single item");

static PyObject* _Nullable varlist_typestr_get(PyObject* _self, void* _Nullable closure
                                               __attribute__((__unused__)))
{
    PyObjCVarList* self = (PyObjCVarList*)_self;
    return PyBytes_FromString(self->typestr);
}

static PyGetSetDef varlist_getset[] = {
    {
        .name = "__typestr__",
        .get  = varlist_typestr_get,
        .doc  = "type encoding for elements of the array",
    },
    {
        .name = NULL /* SENTINEL */
    }};

static PyMethodDef varlist_methods[] = {{.ml_name  = "as_tuple",
                                         .ml_meth  = (PyCFunction)varlist_as_tuple,
                                         .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                         .ml_doc   = varlist_as_tuple_doc},
                                        {.ml_name  = "as_buffer",
                                         .ml_meth  = (PyCFunction)varlist_as_buffer,
                                         .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                         .ml_doc   = varlist_as_buffer_doc},
                                        {
                                            .ml_name = NULL /* SENTINEL */
                                        }};

static PyType_Slot varlist_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&varlist_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&varlist_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&varlist_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&varlist_getset},
    {.slot = Py_sq_item, .pfunc = (void*)&varlist__getitem__},
    {.slot = Py_sq_ass_item, .pfunc = (void*)&varlist__setitem__},
    {.slot = Py_mp_subscript, .pfunc = (void*)&varlist_subscript},
    {.slot = Py_mp_ass_subscript, .pfunc = (void*)&varlist_ass_subscript},
#if PY_VERSION_HEX < 0x030a0000
    {.slot = Py_tp_new, .pfunc = (void*)&varlist_new},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec varlist_spec = {
    .name      = "objc.varlist",
    .basicsize = sizeof(PyObjCVarList),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = varlist_slots,
};

PyObject* PyObjCVarList_Type = (PyObject* _Nonnull)NULL;

PyObject*
PyObjCVarList_New(const char* tp, void* array)
{
    PyObjCVarList* result;
    const char*    end;

    end = PyObjCRT_SkipTypeSpec(tp);
    if (end == NULL) { // LCOV_BR_EXCL_LINE
        /* This should never happen because the 'tp' argument
         * is either from the ObjC runtime, or is validated before
         * we get here.
         */
        return NULL; // LCOV_EXCL_LINE
    }
    while (end > tp && isdigit(end[-1])) {
        end--;
    }

    /* XXX: Use PyObject_New() + separate buffer for the encoding */
    result = (PyObjCVarList*)PyObject_Malloc(
        _PyObject_SIZE((PyTypeObject*)PyObjCVarList_Type) + (end - tp) + 1);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    (void)PyObject_Init((PyObject*)result, (PyTypeObject*)PyObjCVarList_Type);
    result->array    = array;
    result->itemsize = PyObjCRT_AlignedSize(tp);
    if (unlikely(result->itemsize == -1)) {
        /* Should never happen, type is already validated */
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    memcpy(result->typestr, tp, end - tp);
    result->typestr[end - tp] = '\0';

    if (result->typestr[0] == _C_VOID) {
        result->typestr[0] = _C_CHAR_AS_TEXT;
    }

    return (PyObject*)result;
}

int
PyObjCVarList_Setup(PyObject* module)
{
    PyObject* tmp = PyType_FromSpec(&varlist_spec);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }
    PyObjCVarList_Type = tmp;

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "varlist", PyObjCVarList_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCVarList_Type);
    return 0;
}

NS_ASSUME_NONNULL_END
