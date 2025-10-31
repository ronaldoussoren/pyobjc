/*
 * Wrappers for C structs
 *
 * Structs are represented as instance-like objects, with normal field access
 * (e.g. myRect.size), but can also be accessed like read-write tuples (e.g.
 * myRect[0]).
 *
 * Instances consist of the generic PyObject header followed by an array of
 * fields.
 *
 * NOTE: The basic implementation is quite generic, but the end of this file
 * is only useful for PyObjC.
 *
 * XXX: Can this be converted to PyType_FromSpec?
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/* This variable is initialized int the _Init function, called
 * before the API using the variable is called.
 */
static ffi_cif* _Nonnull init_cif = (ffi_cif* _Nonnull)NULL;

/*
 * First some helpers: easy access to the actual fields
 */
static inline PyObject*
GET_STRUCT_FIELD(PyObject* self, PyMemberDef* member)
{
    return *(PyObject**)(((char*)self) + member->offset);
}

static inline void
SET_STRUCT_FIELD(PyObject* self, PyMemberDef* member, PyObject* val)
{
    Py_XINCREF(val);
    PyObject* tmp = *(PyObject**)(((char*)self) + member->offset);
    *((PyObject**)(((char*)self) + member->offset)) = val;
    Py_XDECREF(tmp);
}

static inline Py_ssize_t
STRUCT_LENGTH(PyObject* self)
{
    return (Py_TYPE(self)->tp_basicsize - sizeof(PyObject)) / sizeof(PyObject*);
}

/*
 * Implementation of the sequence interface.
 */

static Py_ssize_t
struct_sq_length(PyObject* self)
{
    /* The object contains the generic PyObject header followed by an
     * array of PyObject*-s.
     */
    if (!PyObjC_StructsIndexable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences",
                     Py_TYPE(self)->tp_name);
        return -1;
    }
    return STRUCT_LENGTH(self);
}

static PyObject* _Nullable struct_sq_item(PyObject* self, Py_ssize_t offset)
{
    Py_ssize_t   len;
    PyMemberDef* member;
    PyObject*    res;

    if (!PyObjC_StructsIndexable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences",
                     Py_TYPE(self)->tp_name);
        return NULL;
    }

    len = STRUCT_LENGTH(self);

    if (offset < 0 || offset >= len) {
        PyErr_Format(PyExc_IndexError, "%.100s index out of range",
                     Py_TYPE(self)->tp_name);
        res = NULL;
    } else {
        Py_BEGIN_CRITICAL_SECTION(self);
        member = Py_TYPE(self)->tp_members + offset;
        res    = GET_STRUCT_FIELD(self, member);
        assert(res != NULL);

        Py_INCREF(res);
        Py_END_CRITICAL_SECTION();
    }

    return res;
}

static PyObject* _Nullable struct_sq_slice(PyObject* self, Py_ssize_t ilow,
                                           Py_ssize_t ihigh)
{
    PyObject*  result;
    Py_ssize_t i;

#ifndef NDEBUG
    Py_ssize_t len = STRUCT_LENGTH(self);
#endif
    assert(ilow >= 0);
    assert(ihigh <= len);

    result = PyTuple_New(ihigh - ilow);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    Py_BEGIN_CRITICAL_SECTION(self);

    for (i = ilow; i < ihigh; i++) {
        PyMemberDef* member = Py_TYPE(self)->tp_members + i;
        PyObject*    v      = GET_STRUCT_FIELD(self, member);
        assert(v != NULL);
        Py_INCREF(v);
        PyTuple_SET_ITEM(result, i - ilow, v);
    } // LCOV_BR_EXCL_LINE

    Py_END_CRITICAL_SECTION();
    return result;
}

static int
struct_sq_ass_item(PyObject* self, Py_ssize_t offset, PyObject* _Nullable newVal)
{
    Py_ssize_t   len;
    PyMemberDef* member;

    /* It is not necessary to test if sequences are writable and indexable,
     * both have been checked by our callers.
     */
    assert(PyObjC_StructsIndexable);
    assert(PyObjC_StructsWritable);

    if (newVal == NULL) {
        PyErr_Format(PyExc_TypeError, "Cannot delete item '%ld' in a %.100s instance",
                     offset, Py_TYPE(self)->tp_name);
        return -1;
    }

    len = STRUCT_LENGTH(self);

    if ((offset < 0) || (offset >= len)) {
        PyErr_Format(PyExc_IndexError, "%.100s index out of range",
                     Py_TYPE(self)->tp_name);
        return -1;
    }
    member = Py_TYPE(self)->tp_members + offset;

    Py_BEGIN_CRITICAL_SECTION(self);
    SET_STRUCT_FIELD(self, member, newVal);
    Py_END_CRITICAL_SECTION();
    return 0;
}

static int
struct_sq_ass_slice(PyObject* self, Py_ssize_t ilow, Py_ssize_t ihigh,
                    PyObject* _Nullable v)
{
    PyObject*  seq;
    Py_ssize_t i;

    if (v == NULL) {
        PyErr_Format(PyExc_TypeError, "Cannot delete items in instances of %.100s",
                     Py_TYPE(self)->tp_name);
        return -1;
    }

#ifndef NDEBUG
    Py_ssize_t len = STRUCT_LENGTH(self);
#endif
    assert(ilow >= 0);
    assert(ilow <= len);
    assert(ihigh >= 0);
    assert(ihigh <= len);

    seq = PyObjCSequence_Tuple(v, "Must assign sequence to slice");
    if (seq == NULL)
        return -1;

    if (PyTuple_GET_SIZE(seq) != ihigh - ilow) {
        Py_DECREF(seq);
        PyErr_Format(PyExc_TypeError,
                     "Slice assignment would change size of %.100s "
                     "instance",
                     Py_TYPE(self)->tp_name);
        return -1;
    }

    Py_BEGIN_CRITICAL_SECTION(self);
    for (i = ilow; i < ihigh; i++) {
        PyObject*    x;
        PyMemberDef* member = Py_TYPE(self)->tp_members + i;

        x = PyTuple_GET_ITEM(seq, i - ilow);
        assert(x != NULL);
        SET_STRUCT_FIELD(self, member, x);
    } // LCOV_BR_EXCL_LINE
    Py_DECREF(seq);
    Py_END_CRITICAL_SECTION();
    return 0;
}

static int
struct_sq_contains(PyObject* self, PyObject* value)
{
    int result = 0;

    if (!PyObjC_StructsIndexable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences",
                     Py_TYPE(self)->tp_name);
        return -1;
    }

    /* XXX: Consider shrinking the critical section here, to avoid running
     *      arbitrary code inside the section. That can result in a lot
     *      more locking though...
     */
    Py_BEGIN_CRITICAL_SECTION(self);
    for (PyMemberDef* member = Py_TYPE(self)->tp_members; member && member->name;
         member++) {
        int r;

        PyObject* cur = GET_STRUCT_FIELD(self, member);
        assert(cur != NULL);

        r = PyObject_RichCompareBool(cur, value, Py_EQ);
        if (r == -1) {
            result = -1;
            break;
        } else if (r) {
            result = 1;
            break;
        }
    }
    Py_END_CRITICAL_SECTION();
    return result;
}

static PyObject* _Nullable struct_reduce(PyObject* self)
{
    PyObject*  result;
    PyObject*  values;
    Py_ssize_t i, len;

    len    = STRUCT_LENGTH(self);
    values = PyTuple_New(len);
    if (values == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    Py_BEGIN_CRITICAL_SECTION(self);
    for (i = 0; i < len; i++) {
        PyObject* v = GET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + i);
        assert(v != NULL);
        Py_INCREF(v);
        PyTuple_SET_ITEM(values, i, v);
    } // LCOV_BR_EXCL_LINE
    Py_END_CRITICAL_SECTION();

    result = PyTuple_Pack(2, Py_TYPE(self), values);
    Py_CLEAR(values);
    return result;
}

static PyObject* _Nullable struct_sizeof(PyObject* self)
{
    return PyLong_FromSsize_t(Py_TYPE(self)->tp_basicsize);
}

static PyObject* _Nullable struct__copy__(PyObject* self)
{
    PyObject*    result;
    PyMemberDef* member = Py_TYPE(self)->tp_members;

    result = PyObject_GC_New(PyObject, Py_TYPE(self));
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    Py_BEGIN_CRITICAL_SECTION(self);
    while (member && member->name) {
        assert(member->type == T_OBJECT);
        *((PyObject**)(((char*)result) + member->offset)) = NULL;
        PyObject* t = GET_STRUCT_FIELD(self, member);
        assert(t != NULL);

        if (t != NULL) {
            SET_STRUCT_FIELD(result, member, t);
        }

        member++;
    } // LCOV_BR_EXCL_LINE
    Py_END_CRITICAL_SECTION();

    PyObject_GC_Track(result);
    return result;
}

static PyObject* _Nullable struct__deepcopy__(PyObject* self, PyObject* args,
                                              PyObject* kwds)
{
    static char* keywords[] = {"memo", NULL};
    PyObject*    memo;
    PyObject*    result;
    PyMemberDef* member = Py_TYPE(self)->tp_members;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &memo)) {
        return NULL;
    }

    result = PyObject_GC_New(PyObject, Py_TYPE(self));
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    while (member && member->name) {
        PyObject* t;
        assert(member->type == T_OBJECT);
        *((PyObject**)(((char*)result) + member->offset)) = NULL;

        Py_BEGIN_CRITICAL_SECTION(self);
        t = GET_STRUCT_FIELD(self, member);
        assert(t != NULL);
        Py_INCREF(t);
        Py_END_CRITICAL_SECTION();

        PyObject* v = PyObjC_deepcopy(t, memo);
        Py_DECREF(t);
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        SET_STRUCT_FIELD(result, member, v);
        Py_DECREF(v);

        member++;
    }

    PyObject_GC_Track(result);
    return result;
}

static PyObject* _Nullable struct_deepcopy(PyObject* self)
{
    return PyObjC_deepcopy(self, NULL);
}

static PyObject* _Nullable struct_replace_impl(const char* name, int deepcopy,
                                               PyObject* self, PyObject* _Nullable args,
                                               PyObject* _Nullable kwds)
{
    /* NOTE: This is a fairly inefficient implementation, first
     * perform a deep copy, then replace attributes. The deep copy
     * provides the nicest transition path to read-only structs:
     * the result of _replace is completely independent of the original.
     */
    PyObject*  result;
    Py_ssize_t pos = 0;
    PyObject*  key;
    PyObject*  value;

    if (args && PySequence_Length(args) != 0) {
        PyErr_Format(PyExc_TypeError, "%s called with positional arguments", name);
        return NULL;
    }

    if (deepcopy) {
        result = struct_deepcopy(self);
    } else {
        result = struct__copy__(self);
    }

    if (result == NULL) {
        return NULL;
    }

    if (kwds != NULL) {
        Py_BEGIN_CRITICAL_SECTION2(self, kwds);
        while (PyDict_Next(kwds, &pos, &key, &value)) {
            int r = PyObject_SetAttr(result, key, value);
            if (r == -1) {
                Py_DECREF(result);
                result = NULL;
                goto exit;
            }
        } // LCOV_BR_EXCL_LINE
    exit:
        (void)0;
        Py_END_CRITICAL_SECTION2();
    }

    return result;
}

static PyObject* _Nullable struct_replace(PyObject* self, PyObject* _Nullable args,
                                          PyObject* _Nullable kwds)
{
    return struct_replace_impl("_replace", 1, self, args, kwds);
}

static PyObject* _Nullable struct__replace__(PyObject* self, PyObject* _Nullable args,
                                             PyObject* _Nullable kwds)
{
    return struct_replace_impl("__replace__", 0, self, args, kwds);
}

static PyObject* _Nullable struct_asdict(PyObject* self)
{
    PyObject*    result;
    PyMemberDef* member = Py_TYPE(self)->tp_members;
    int          r;

    result = PyDict_New();
    if (result == NULL) {
        return NULL; // LCOV_EXCL_LINE
    }

    Py_BEGIN_CRITICAL_SECTION(self);
    while (member && member->name) {
        PyObject* t;
        assert(member->type == T_OBJECT);

        t = GET_STRUCT_FIELD(self, member);
        assert(t != NULL);

        PyObject* py_name = PyUnicode_FromString(member->name);
        if (py_name == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_CLEAR(result);
            goto exit;
            // LCOV_EXCL_STOP
        }

        r = PyDict_SetItem(result, py_name, t);

        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_CLEAR(result);
            Py_DECREF(py_name);
            goto exit;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(py_name);
        member++;
    } // LCOV_BR_EXCL_LINE
exit:
    (void)0;
    Py_END_CRITICAL_SECTION();

    return result;
}

static PyObject* _Nullable struct_mp_subscript(PyObject* self, PyObject* item)
{
    if (!PyObjC_StructsIndexable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences",
                     Py_TYPE(self)->tp_name);
        return NULL;
    }

    if (PyIndex_Check(item)) {
        Py_ssize_t i;
        i = PyNumber_AsSsize_t(item, PyExc_IndexError);

        if (i == -1 && PyErr_Occurred()) {
            return NULL;
        }

        if (i < 0) {
            i += STRUCT_LENGTH(self);
        }
        return struct_sq_item(self, i);

    } else if (PySlice_Check(item)) {
        Py_ssize_t start, stop, step, slicelength, cur, i;
        PyObject*  result;
        PyObject*  it;

        if (PySlice_Unpack(item, &start, &stop, &step) < 0) {
            return NULL;
        }
        slicelength = PySlice_AdjustIndices(STRUCT_LENGTH(self), &start, &stop, step);
        if (slicelength <= 0) {
            return PyTuple_New(0);

        } else if (step == 1) {
            return struct_sq_slice(self, start, stop);

        } else {
            result = PyTuple_New(slicelength);
            if (result == NULL) {
                return NULL; // LCOV_EXCL_LINE
            }

            for (cur = start, i = 0; i < slicelength; cur += step, i++) {
                it = struct_sq_item(self, cur);
                PyTuple_SET_ITEM(result, i, it);
            }
            return result;
        }

    } else {
        PyErr_Format(PyExc_TypeError, "Struct indices must be integers, not %.100s",
                     Py_TYPE(item)->tp_name);
        return NULL;
    }
}

static int
struct_mp_ass_subscript(PyObject* self, PyObject* item, PyObject* _Nullable value)
{
    if (!PyObjC_StructsIndexable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences",
                     Py_TYPE(self)->tp_name);
        return -1;
    }
    if (!PyObjC_StructsWritable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are read-only",
                     Py_TYPE(self)->tp_name);
        return -1;
    }

    if (PyIndex_Check(item)) {
        Py_ssize_t i = PyNumber_AsSsize_t(item, PyExc_IndexError);

        if (i == -1 && PyErr_Occurred()) {
            return -1;
        }

        if (i < 0) {
            i += STRUCT_LENGTH(self);
        }
        return struct_sq_ass_item(self, i, value);
    } else if (PySlice_Check(item)) {
        Py_ssize_t start, stop, step, slicelength;

        if (PySlice_Unpack(item, &start, &stop, &step) < 0) {
            return -1;
        }
        slicelength = PySlice_AdjustIndices(STRUCT_LENGTH(self), &start, &stop, step);

        if (step == 1) {
            return struct_sq_ass_slice(self, start, stop, value);
        }

        if (value == NULL) {
            PyErr_Format(PyExc_TypeError, "Cannot delete items in instances of %.100s",
                         Py_TYPE(self)->tp_name);
            return -1;
        }

        PyObject* seq = PyObjCSequence_Tuple(value, "must assign sequence to slice");
        if (seq == NULL)
            return -1;

        if (PyTuple_GET_SIZE(seq) != slicelength) {
            Py_DECREF(seq);
            PyErr_Format(PyExc_TypeError,
                         "slice assignment would change size of %.100s "
                         "instance",
                         Py_TYPE(self)->tp_name);
            return -1;
        }

        Py_ssize_t cur, i;
        for (cur = start, i = 0; i < slicelength; cur += step, i++) {
            int r = struct_sq_ass_item(self, cur, PyTuple_GET_ITEM(seq, i));
            if (r == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(seq);
                return -1;
                // LCOV_EXCL_STOP
            }
        } // LCOV_BR_EXCL_LINE

        Py_DECREF(seq);
        return 0;

    } else {
        PyErr_Format(PyExc_TypeError, "Struct indices must be integers, not %.100s",
                     Py_TYPE(item)->tp_name);
        return -1;
    }
}

static PySequenceMethods struct_as_sequence = {
    .sq_length   = struct_sq_length,
    .sq_item     = struct_sq_item,
    .sq_ass_item = struct_sq_ass_item,
    .sq_contains = struct_sq_contains,
};

static PyMappingMethods struct_as_mapping = {
    .mp_length        = struct_sq_length,
    .mp_subscript     = struct_mp_subscript,
    .mp_ass_subscript = struct_mp_ass_subscript,
};

static PyMethodDef struct_methods[] = {
    {
        .ml_name  = "__reduce__",
        .ml_meth  = (PyCFunction)struct_reduce,
        .ml_flags = METH_NOARGS,
    },
    {
        .ml_name  = "copy",
        .ml_meth  = (PyCFunction)struct_deepcopy,
        .ml_flags = METH_NOARGS,
        .ml_doc   = "Return a copy of the struct",
    },
    {
        .ml_name  = "__sizeof__",
        .ml_meth  = (PyCFunction)struct_sizeof,
        .ml_flags = METH_NOARGS,
    },
    /* NamedTuple interface */
    {.ml_name  = "_asdict",
     .ml_meth  = (PyCFunction)struct_asdict,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "Return dict representation of the object"},
    {.ml_name  = "_replace",
     .ml_meth  = (PyCFunction)struct_replace,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = "Return a copy with some fields replaced by other values"},
    {.ml_name  = "__copy__",
     .ml_meth  = (PyCFunction)struct__copy__,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "Return a shallow copy"},
    {.ml_name  = "__deepcopy__",
     .ml_meth  = (PyCFunction)struct__deepcopy__,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = "Return a deep copy"},
    {.ml_name  = "__replace__",
     .ml_meth  = (PyCFunction)struct__replace__,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = "Return a copy with some fields replaced by other values"},

    {NULL, NULL, 0, NULL}};

/*
 * Special methods
 */

static int
struct_setattro(PyObject* self, PyObject* name, PyObject* _Nullable value)
{
    if (!PyObjC_StructsWritable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are read-only",
                     Py_TYPE(self)->tp_name);
        return -1;
    }
    if (value == NULL) {
        PyErr_Format(PyExc_TypeError, "Cannot delete attributes of %.100s",
                     Py_TYPE(self)->tp_name);
        return -1;
    }
    return PyObject_GenericSetAttr(self, name, value);
}

static void
struct_dealloc(PyObject* self)
{
    PyMemberDef* member = Py_TYPE(self)->tp_members;

    PyObject_GC_UnTrack(self);

    while (member && member->name) {
        Py_CLEAR(*(PyObject**)(((char*)self) + member->offset));
        member++;
    }

    PyObject_GC_Del(self);
}

static PyObject* _Nullable struct_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
    PyObject*    result;
    PyMemberDef* member = type->tp_members;
    int          r;

    result = PyObject_GC_New(PyObject, type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    while (member && member->name) {
        assert(member->type == T_OBJECT);
        *((PyObject**)(((char*)result) + member->offset)) = Py_None;
        Py_INCREF(Py_None);
        member++;
    }
    PyObject_GC_Track(result);

    r = type->tp_init(result, args, kwds);
    if (r == -1) {
        Py_DECREF(result);
        return NULL;
    }
    return result;
}

static int
LOCATE_MEMBER(PyTypeObject* type, const char* name)
{
    int          i = 0;
    PyMemberDef* member;

    for (i = 0, member = type->tp_members; member->name != NULL; i++, member++) {
        if (strcmp(member->name, name) == 0) {
            return i;
        }
    }
    return -1;
}

static int
set_defaults(PyObject* self, const char* typestr)
{
    Py_ssize_t i = 0;
    int        r;
    PyObject*  v;

    while (*typestr != _C_STRUCT_E && *typestr++ != '=')
        ;
    while (typestr && *typestr != _C_STRUCT_E) {
        const char* next;

        /* The encoding cannot have embedded field names,
         * those were removed during type creation
         */
        assert(*typestr != '"');
        next = PyObjCRT_SkipTypeSpec(typestr);
        if (next == NULL) { // LCOV_BR_EXCL_LINE
            /* Should never happen, the signature was
             * already parsed during type creation.
             */
            return -1; // LCOV_EXCL_LINE
        }
        switch (*typestr) {
#ifdef _C_BOOL
        case _C_BOOL:
            v = Py_False;
            Py_INCREF(Py_False);
            break;
#endif
        case _C_NSBOOL:
            v = Py_False;
            Py_INCREF(Py_False);
            break;

        case _C_CHAR_AS_TEXT: {
            char ch = 0;
            v       = PyUnicode_FromStringAndSize(&ch, 1);
        } break;

        case _C_UNICHAR: {
            char buffer[2] = {0, 0};
            v              = PyUnicode_FromStringAndSize(buffer, 1);
        } break;

        case _C_CHAR_AS_INT:
        case _C_CHR:
        case _C_UCHR:
        case _C_SHT:
        case _C_USHT:
        case _C_INT:
        case _C_UINT:
        case _C_LNG:
        case _C_ULNG:
        case _C_LNG_LNG:
        case _C_ULNG_LNG:
            v = PyLong_FromLong(0);
            break;

        case _C_FLT:
        case _C_DBL:
            v = PyFloat_FromDouble(0.0);
            break;

        case _C_STRUCT_B:
            v = PyObjC_CreateRegisteredStruct(typestr, next - typestr, NULL, NULL);
            if (v != NULL) {
                /* call init */
                r = Py_TYPE(v)->tp_init(v, NULL, NULL);
                if (r == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(v);
                    return -1;
                    // LCOV_EXCL_STOP
                }

            } else if (!PyErr_Occurred()) {
                /* this is a struct-type without a struct
                 * wrapper. Default to None
                 */
                v = Py_None;
                Py_INCREF(Py_None);
            }

            break;

        default:
            v = Py_None;
            Py_INCREF(Py_None);
        }

        if (v == NULL) { // LCOV_BR_EXCL_LINE
            return -1;   // LCOV_EXCL_LINE
        }

        r = PyObjC_SetStructField(self, i++, v);
        Py_DECREF(v);
        if (r < 0) {   // LCOV_BR_EXCL_LINE
            return -1; // LCOV_EXCL_LINE
        }
        typestr = next;
    } // LCOV_BR_EXCL_LINE

    return 0;
}

static void
struct_init(ffi_cif* cif __attribute__((__unused__)), void* retval,
            void* _Nullable* _Nonnull cargs, void* _Nonnull userdata)
{
    PyObject* _Nullable self = *(PyObject**)cargs[0];
    PyObject* _Nullable args = *(PyObject**)cargs[1];
    PyObject* _Nullable kwds = *(PyObject**)cargs[2];
    const char* typestr      = (char*)userdata;
    Py_ssize_t  setUntil     = -1;
    int         r;

    if (self == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        *(int**)retval = 0;
        return;
        // LCOV_EXCL_STOP
    }

    if (args != NULL && !PyTuple_Check(args)) { // LCOV_BR_EXCL_LINE
        /* Assertion error */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError, "%.100s() argument tuple is not a tuple",
                     Py_TYPE(self)->tp_name);
        *(int*)retval = -1;
        return;
        // LCOV_EXCL_STOP
    }

    if (kwds != NULL && !PyDict_Check(kwds)) { // LCOV_BR_EXCL_LINE
        /* Assertion error */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError, "%.100s() keyword dict is not a dict",
                     Py_TYPE(self)->tp_name);
        *(int*)retval = -1;
        return;
        // LCOV_EXCL_STOP
    }

    r = set_defaults(self, typestr);
    if (r != 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        *(int*)retval = r;
        return;
        // LCOV_EXCL_STOP
    }

    if (args != NULL) {
        Py_ssize_t i, len;

        len = PyTuple_GET_SIZE(args);
        if (len > STRUCT_LENGTH(self)) {
            PyErr_Format(PyExc_TypeError,
                         "%.100s() takes at most %ld %sarguments (%ld given)",
                         Py_TYPE(self)->tp_name, STRUCT_LENGTH(self),
                         kwds ? "non-keyword " : "", len);
            *(int*)retval = -1;
            return;
        }
        for (i = 0; i < len; i++) {
            PyObject* v = PyTuple_GET_ITEM(args, i);

            SET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + i, v);
        }
        setUntil = len - 1;
    }

    if (kwds != NULL) {
        PyObject*  key;
        PyObject*  value;
        Py_ssize_t pos = 0;

        while (PyDict_Next(kwds, &pos, &key, &value)) {
            if (!PyUnicode_Check(key)) {
                PyErr_Format(PyExc_TypeError, "%.100s() keywords must be strings",
                             Py_TYPE(self)->tp_name);
                *(int*)retval = -1;
                return;
            }

            const char* k_bytes = PyUnicode_AsUTF8(key);
            if (k_bytes == NULL) {
                *(int*)retval = -1;
                return;
            }

            Py_ssize_t off = LOCATE_MEMBER(Py_TYPE(self), k_bytes);
            if (off == -1) {
                PyErr_Format(PyExc_TypeError, "%.100s() does not have argument %.100s",
                             Py_TYPE(self)->tp_name, k_bytes);
                *(int*)retval = -1;
                return;
            }

            if (off <= setUntil) {
                PyErr_Format(PyExc_TypeError,
                             "%.100s() got multiple values for keyword "
                             "argument '%.100s'",
                             Py_TYPE(self)->tp_name, k_bytes);
                *(int*)retval = -1;
                return;
            }

            SET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + off, value);
        }
    }

    *(int*)retval = 0;
    return;
}

static initproc _Nullable make_init(const char* _typestr)
{
    ffi_closure* cl = NULL;
    void*        codeloc;
    const char*  typestr_copy;

    typestr_copy = PyObjCUtil_Strdup(_typestr);
    if (typestr_copy == NULL) {
        return NULL; // LCOV_EXCL_LINE
    }

    assert(init_cif != NULL);

    if (alloc_prepped_closure( // LCOV_BR_EXCL_LINE
            &cl, init_cif, &codeloc, (void*)struct_init, (char*)typestr_copy)
        == -1) {
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_Error, "Cannot create libffi closure");
        PyMem_Free((void*)typestr_copy);
        return NULL;
        // LCOV_EXCL_STOP
    }

    return (initproc)codeloc;
}

static Py_hash_t
struct_hash(PyObject* self)
{
    PyErr_Format(PyExc_TypeError, "%.100s objects are unhashable",
                 Py_TYPE(self)->tp_name);
    return -1;
}

static PyObject* _Nullable struct_richcompare(PyObject* self, PyObject* other, int op)
{
    Py_ssize_t self_len, other_len, i, len;
    int        cmp;
    PyObject*  self_cur;
    PyObject*  other_cur;

    if (Py_TYPE(self) == Py_TYPE(other)) {
        /* Other has same type, shortcut comparisons to avoid
         * treating "other" as a generic sequence
         */

        len = STRUCT_LENGTH(self);

        Py_BEGIN_CRITICAL_SECTION2(self, other);
        for (i = 0; i < len; i++) {
            int k;

            self_cur  = GET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + i);
            other_cur = GET_STRUCT_FIELD(other, Py_TYPE(other)->tp_members + i);
            assert(self_cur != NULL);
            assert(other_cur != NULL);

            k = PyObject_RichCompareBool(self_cur, other_cur, Py_EQ);
            if (k < 0) {
                Py_EXIT_CRITICAL_SECTION2();
                return NULL;
            }

            if (!k) {
                /* Not equal, result is the comparison of the last
                 * item, we can do better for '==' and '!='.
                 */
                if (op == Py_EQ) {
                    Py_EXIT_CRITICAL_SECTION2();
                    Py_RETURN_FALSE;
                } else if (op == Py_NE) {
                    Py_EXIT_CRITICAL_SECTION2();
                    Py_RETURN_TRUE;
                }
                Py_EXIT_CRITICAL_SECTION2();
                return PyObject_RichCompare(self_cur, other_cur, op);
            }
        }
        Py_END_CRITICAL_SECTION2();

        /* All items are equal, compare using sizes */
        switch (op) {
        case Py_LT:
        case Py_NE:
        case Py_GT:
            Py_RETURN_FALSE;

        case Py_LE:
        case Py_EQ:
        case Py_GE:
            Py_RETURN_TRUE;

        default:
            /* Should never happen */
            // LCOV_EXCL_START
            PyErr_SetString(PyExc_TypeError, "Invalid comparison");
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    if (!PySequence_Check(other)) {
        if (op == Py_EQ) {
            Py_RETURN_FALSE;

        } else if (op == Py_NE) {
            Py_RETURN_TRUE;

        } else {
            PyErr_Format(PyExc_TypeError, "Cannot compare instances of %.100s and %.100s",
                         Py_TYPE(self)->tp_name, Py_TYPE(other)->tp_name);
            return NULL;
        }

    } else if (!PyObjC_StructsIndexable) {
        if (op == Py_EQ) {
            Py_RETURN_FALSE;

        } else if (op == Py_NE) {
            Py_RETURN_TRUE;

        } else {
            PyErr_Format(PyExc_TypeError, "Cannot compare instances of %.100s and %.100s",
                         Py_TYPE(self)->tp_name, Py_TYPE(other)->tp_name);
            return NULL;
        }
    }

    self_len  = STRUCT_LENGTH(self);
    other_len = PySequence_Length(other);
    len       = self_len;
    if (other_len < len) {
        len = other_len;
    }

    if (self_len != other_len && (op == Py_EQ || op == Py_NE)) {
        /* Shortcut comparison for non-equals lengths */
        if (op == Py_EQ) {
            Py_RETURN_FALSE;

        } else {
            Py_RETURN_TRUE;
        }
    }

    for (i = 0; i < len; i++) {
        int k;

        Py_BEGIN_CRITICAL_SECTION(self);
        self_cur = GET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + i);
        Py_END_CRITICAL_SECTION();
        assert(self_cur != NULL);
        other_cur = PySequence_GetItem(other, i);
        if (other_cur == NULL) // LCOV_BR_EXCL_LINE
            return NULL;       // LCOV_EXCL_LINE

        k = PyObject_RichCompareBool(self_cur, other_cur, Py_EQ);
        if (k < 0) {
            Py_DECREF(other_cur);
            return NULL;
        }

        if (!k) {
            /* Not equal, result is the comparison of the last
             * item, we can do better for '==' and '!='.
             */
            PyObject* v;

            if (op == Py_EQ) {
                Py_RETURN_FALSE;
            } else if (op == Py_NE) {
                Py_RETURN_TRUE;
            }
            v = PyObject_RichCompare(self_cur, other_cur, op);
            Py_DECREF(other_cur);
            return v;
        }
        Py_DECREF(other_cur);
    }

    /* All items are equal, compare using sizes */
    switch (op) {
    case Py_LT:
        cmp = self_len < other_len;
        break;
    case Py_LE:
        cmp = self_len <= other_len;
        break;
    case Py_EQ:
        cmp = self_len == other_len;
        break;
    case Py_NE:
        cmp = self_len != other_len;
        break;
    case Py_GE:
        cmp = self_len >= other_len;
        break;
    case Py_GT:
        cmp = self_len > other_len;
        break;
    default:
        /* Should never happen */
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "Invalid comparison");
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (cmp) {
        Py_RETURN_TRUE;

    } else {
        Py_RETURN_FALSE;
    }
}

static int
struct_traverse(PyObject* self, visitproc visit, void* _Nullable arg)
{
    PyMemberDef* member;
    PyObject*    v;
    int          err = 0;

    Py_BEGIN_CRITICAL_SECTION(self);
    for (member = Py_TYPE(self)->tp_members; member && member->name; member++) {
        v = GET_STRUCT_FIELD(self, member);
        if (v == NULL) // LCOV_BR_EXCL_LINE
            continue;  // LCOV_EXCL_LINE
        err = visit(v, arg);
        if (err) { // LCOV_BR_EXCL_LINE
            break; // LCOV_EXCL_LINE
        }
    }
    Py_END_CRITICAL_SECTION();
    return err;
}

static int
struct_clear(PyObject* self)
{
    PyMemberDef* member;

    Py_BEGIN_CRITICAL_SECTION(self);
    for (member = Py_TYPE(self)->tp_members; member && member->name; member++) {
        /* Maintain the invariant that struct fields are not NULL.
         *
         * The CPython documentation says that fields should be set to
         * NULL, but the primary reason is to ensure that there are no
         * reference cycles and Py_None cannot be part of such a cycle.
         */
        SET_STRUCT_FIELD(self, member, Py_None);
    }
    Py_END_CRITICAL_SECTION();
    return 0;
}

static PyObject* _Nullable struct_repr(PyObject* self)
{
    Py_ssize_t   i, len;
    PyObject*    cur;
    PyMemberDef* member;

    len = STRUCT_LENGTH(self);
    if (len == 0) {
        return PyUnicode_FromFormat("<%.100s>", Py_TYPE(self)->tp_name);
    }

    i = Py_ReprEnter(self);
    if (i < 0) { // LCOV_BR_EXCL_LINE
        /* Can only happen when hitting the recursion limit */
        return NULL; // LCOV_EXCL_LINE

    } else if (i != 0) {
        /* Self-recursive struct */
        return PyUnicode_FromFormat("<%.100s ...>", Py_TYPE(self)->tp_name);
    }

    cur = PyUnicode_FromFormat("<%.100s", Py_TYPE(self)->tp_name);

    member = Py_TYPE(self)->tp_members;
    while (member->name != NULL) {
        PyObject* v;

        PyUnicode_Append(&cur, PyUnicode_FromFormat(" %.100s=", member->name));
        if (cur == NULL) // LCOV_BR_EXCL_LINE
            goto done;   // LCOV_EXCL_LINE

        Py_BEGIN_CRITICAL_SECTION(self);
        v = GET_STRUCT_FIELD(self, member);
        Py_END_CRITICAL_SECTION();
        assert(v != NULL);

        PyObject* repr = PyObject_Repr(v);
        if (repr == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_CLEAR(cur);
            goto done;
            // LCOV_EXCL_STOP
        }
        PyUnicode_Append(&cur, repr);
        Py_DECREF(repr);
        if (cur == NULL) // LCOV_BR_EXCL_LINE
            goto done;   // LCOV_EXCL_LINE
        member++;
    } // LCOV_BR_EXCL_LINE

    PyUnicode_Append(&cur, PyUnicode_FromString(">"));

done:
    Py_ReprLeave(self);
    return cur;
}

PyTypeObject StructBase_Type = {
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "objc._structwrapper",
    .tp_basicsize                          = sizeof(PyObject),
    .tp_itemsize                           = 0,
};

struct StructTypeObject {
    PyTypeObject base;
    Py_ssize_t   pack; /* struct packing, -1 for default packing */
};

/*
 * A template for the type object
 */
static struct StructTypeObject StructTemplate_Type = {
    .base =
        {
            PyVarObject_HEAD_INIT(NULL, 0).tp_name = "objc.StructTemplate",
            .tp_basicsize                          = sizeof(PyObject),
            .tp_itemsize                           = 0,
            .tp_dealloc                            = struct_dealloc,
            .tp_repr                               = struct_repr,
            .tp_as_sequence                        = &struct_as_sequence,
            .tp_as_mapping                         = &struct_as_mapping,
            .tp_hash                               = struct_hash,
            .tp_getattro                           = PyObject_GenericGetAttr,
            .tp_setattro                           = struct_setattro,
            .tp_flags       = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
            .tp_traverse    = struct_traverse,
            .tp_clear       = struct_clear,
            .tp_richcompare = struct_richcompare,
            .tp_methods     = struct_methods,
            .tp_new         = struct_new,
        },
    .pack = -1};

PyObject*
PyObjC_MakeStructType(const char* name, const char* _Nullable doc, Py_ssize_t numFields,
                      const char* _Nonnull* _Nonnull fieldnames, const char* typestr,
                      Py_ssize_t pack)
{
    struct StructTypeObject* result;
    PyMemberDef*             members;
    PyObject*                fields;
    Py_ssize_t               i;

    if (*typestr != _C_STRUCT_B) {
        PyErr_SetString(PyExc_ValueError, "invalid signature: not a struct encoding");
        return NULL;
    }

    fields = PyTuple_New(numFields);
    if (fields == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    members = PyMem_Malloc(sizeof(PyMemberDef) * (numFields + 1));
    if (members == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(fields);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < numFields; i++) {
        PyObject* nm = PyUnicode_FromString(fieldnames[i]);
        if (nm == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(fields);
            PyMem_Free(members);
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyTuple_SET_ITEM(fields, i, nm);
        nm                = NULL;
        members[i].name   = (char*)fieldnames[i];
        members[i].type   = T_OBJECT;
        members[i].offset = sizeof(PyObject) + i * sizeof(PyObject*);
        members[i].flags  = 0; /* A read-write field */
        members[i].doc    = NULL;
    } // LCOV_BR_EXCL_LINE
    members[numFields].name = NULL;

    result = PyMem_Malloc(sizeof(struct StructTypeObject));
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(fields);
        PyMem_Free(members);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    *result              = StructTemplate_Type;
    result->base.tp_name = (char*)name;
    result->base.tp_doc  = (char*)doc;
    result->base.tp_dict = PyDict_New();

    if (result->base.tp_dict == NULL) {
        // LCOV_EXCL_START
        Py_DECREF(fields);
        PyMem_Free(members);
        PyMem_Free(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_SET_REFCNT(result, 1);
    result->base.tp_members   = members;
    result->base.tp_basicsize = sizeof(PyObject) + (numFields * sizeof(PyObject*));
    if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
            result->base.tp_dict, PyObjCNM__fields, fields)
        == -1) {
        // LCOV_EXCL_START
        Py_DECREF(fields);
        PyMem_Free(members);
        PyMem_Free(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

#if PY_VERSION_HEX >= 0x030a0000
    if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
            result->base.tp_dict, PyObjCNM___match_args__, fields)
        == -1) {
        // LCOV_EXCL_START
        Py_DECREF(fields);
        PyMem_Free(members);
        PyMem_Free(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
#endif

    Py_CLEAR(fields);

    result->base.tp_init = make_init(typestr);
    if (result->base.tp_init == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(members);
        PyMem_Free(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    result->pack = pack;

    result->base.tp_base = &StructBase_Type;
    Py_INCREF(result->base.tp_base);

    if (PyType_Ready((PyTypeObject*)result) == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(result);
        PyMem_Free(members);
        return NULL;
        // LCOV_EXCL_STOP
    }

    return (PyObject*)result;
}

/*
 * This is the start of PyObjC specific code
 */

/* The registry is initialized in PyObjCStruct_Init, which is
 * called before any function in this file is called.
 *
 * The lock is needed to get consistent updates to the registry
 * dict.
 */

#ifdef Py_GIL_DISABLED
PyMutex registry_mutex = {0};
#endif
static PyObject* _Nonnull structRegistry = (PyObject* _Nonnull)NULL;

int
PyObjC_DropRegisteredStruct(PyObject* key)
{
    int r;
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_mutex);
#endif
    r = PyDict_DelItem(structRegistry, key);
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif
    return r;
}

PyObject* _Nullable PyObjC_FindRegisteredStruct(const char* signature, Py_ssize_t len)
{
    PyObject* type;
    PyObject* v;

    assert(structRegistry != NULL);

    v = PyUnicode_FromStringAndSize(signature, len);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    if (PyDict_GetItemRef(structRegistry, v, &type) != 1) {
        Py_DECREF(v);
        return NULL;
    }
    Py_DECREF(v);

    return type;
}

PyObject* _Nullable PyObjC_CreateRegisteredStruct(
    const char* signature, Py_ssize_t len, const char* _Nullable* _Nullable objc_encoding,
    Py_ssize_t* _Nullable ppack)
{
    PyTypeObject* type;
    PyObject*     result;
    PyObject*     v;
    PyMemberDef*  member;
    int           r;

    assert(structRegistry != NULL);

    if (ppack != NULL) {
        *ppack = -1;
    }

    v = PyUnicode_FromStringAndSize(signature, len);

    r = PyDict_GetItemRef(structRegistry, v, (PyObject**)&type);

    if (r != 1) {
        Py_DECREF(v);
        return NULL;
    }
    Py_DECREF(v);

    member = type->tp_members;

    result = PyObject_GC_New(PyObject, type);
    if (result == NULL) {
        // LCOV_EXCL_START
        Py_DECREF(type);
        PyErr_Clear();
        return NULL;
        // LCOV_EXCL_STOP
    }

    while (member && member->name) {
        assert(member->type == T_OBJECT);
        *((PyObject**)(((char*)result) + member->offset)) = Py_None;
        Py_INCREF(Py_None);
        member++;
    }

    PyObject_GC_Track(result);

    if (objc_encoding) {
        /*
         * The structRegistry only contains struct wrapper types
         * which by construction always have a bytes __typestr__
         * attribute.
         *
         * The code below guards against getting invalid values
         * in case someone uses Python's introspection facilities
         * to find the registry dict and add an invalid value.
         */
        PyObject* typestr;

        switch ( // LCOV_BR_EXCL_LINE
            PyDict_GetItemRef(type->tp_dict, PyObjCNM___typestr__, &typestr)) {
        case -1:
            // LCOV_EXCL_START
            Py_DECREF(type);
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        case 0:
            // LCOV_EXCL_START
            if (objc_encoding != NULL) {
                *objc_encoding = signature;
            }
            break;
            // LCOV_EXCL_STOP

        case 1:
            if (!PyBytes_Check(typestr)) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_SetString(PyExc_TypeError, "__typestr__ not a bytes object");
                Py_DECREF(type);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }

            /* Setting ``*objc_encoding`` effectively returns
             * a borrowed reference.
             *
             * XXX: This might be unsafe when the struct registry
             * is updated concurrently with a new type.
             */
            *objc_encoding = PyBytes_AsString(typestr);
            Py_DECREF(typestr);
        }
    } // LCOV_BR_EXCL_LINE

    if (ppack != NULL) {
        *ppack = ((struct StructTypeObject*)type)->pack;
    }
    Py_DECREF(type);

    return result;
}

PyObject* _Nullable PyObjC_RegisterStructType(const char* signature, const char* name,
                                              const char* _Nullable doc,
                                              Py_ssize_t numFields,
                                              const char* _Nonnull* _Nullable fieldnames,
                                              Py_ssize_t pack)
{
    PyObject* structType;
    PyObject* v;
    int       r;
    int       freeNames = 0;

    if (numFields == -1) {
        /* Don't use fieldnames, but extract the names from the type signature. */
        const char* sigcur = signature;
        const char* fieldstart;
        char*       sigtmp;

        if (*sigcur != _C_STRUCT_B) {
            PyErr_SetString(PyExc_ValueError, "invalid signature: not a struct encoding");
            return NULL;
        }

        while (*sigcur && *sigcur != _C_STRUCT_E && *sigcur != '=')
            sigcur++;

        if (!*sigcur || *sigcur == _C_STRUCT_E) {
            PyErr_SetString(PyExc_ValueError,
                            "invalid signature: not a complete struct encoding");
            return NULL;
        }

        fieldstart = ++sigcur;
        numFields  = 0;

        /* First pass: Count the number of fields, and in passing
         *             check the validity of the encoding.
         */
        while (*sigcur != _C_STRUCT_E) {
            numFields++;
            if (*sigcur == '\0') {
                PyErr_SetString(PyExc_ValueError,
                                "invalid signature: not a complete struct encoding");
                return NULL;
            }
            if (*sigcur == '"') {
                sigcur++;
                sigcur = strchr(sigcur, '"');
                if (sigcur == NULL) {
                    PyErr_SetString(PyExc_ValueError,
                                    "invalid signature: embedded field name without end");
                    return NULL;
                }
                sigcur++;

            } else {
                PyErr_SetString(
                    PyExc_ValueError,
                    "invalid signature: not all fields have an embedded name");
                return NULL;
            }

            sigcur = PyObjCRT_NextField(sigcur);
            if (sigcur == NULL) {
                return NULL;
            }
        }

        /* Second pass: actually create the array of field names */
        fieldnames = PyMem_Malloc((numFields + 1) * sizeof(char*));
        numFields  = 0;

        sigcur = fieldstart;
        while (*sigcur != _C_STRUCT_E) {
            if (*sigcur == '"') {
                char* end;

                sigcur++;
                end = strchr(sigcur, '"');
                assert(end != NULL);

                fieldnames[numFields] = PyMem_Malloc(end - sigcur + 1);
                memcpy((char*)fieldnames[numFields], sigcur, end - sigcur);
                ((char*)fieldnames[numFields])[end - sigcur] = '\0';
                sigcur                                       = end + 1;
            } // LCOV_BR_EXCL_LINE
            numFields++;
            sigcur = PyObjCRT_NextField(sigcur);
            assert(sigcur != NULL);
        }
        fieldnames[numFields] = NULL;
        freeNames             = 1;

        /*
         * The signature string still contains embedded field names,
         * remove those.
         */
        sigtmp = PyMem_Malloc(strlen(signature) + 20);
        if (sigtmp == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            return NULL;
            // LCOV_EXCL_STOP
        }
        if (PyObjCRT_RemoveFieldNames(sigtmp, signature) == NULL) { // LCOV_BR_EXCL_LINE
            /* This should never fail, we've just scanned the field
             * names and would have found any problems.
             */
            // LCOV_EXCL_START
            PyMem_Free(sigtmp);
            return NULL;
            // LCOV_EXCL_STOP
        }
        signature = sigtmp;
    } else {
        assert(fieldnames);
    }

    structType = PyObjC_MakeStructType(name, doc, numFields, fieldnames, signature, pack);
    if (structType == NULL) {
        if (freeNames) { // LCOV_BR_EXCL_LINE
            /* This should never happen unless the system
             * runs out of memory.  The other failure reasons
             * are related to an invalid signature, and that
             * has already been checked when building "fieldnames"
             */

            // LCOV_EXCL_START
            int i;
            PyMem_Free((char*)signature);
            for (i = 0; i < numFields; i++) {
                PyMem_Free((char*)fieldnames[i]);
            }
            PyMem_Free(fieldnames);
            // LCOV_EXCL_STOP
        } // LCOV_EXCL_LINE
        return NULL;
    }

    v = PyBytes_FromString(signature);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(structType);
        return NULL;
        // LCOV_EXCL_STOP
    }

    r = PyDict_SetItem(((PyTypeObject*)structType)->tp_dict, PyObjCNM___typestr__, v);
    Py_DECREF(v);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(structType);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (pack != -1) {
        /* Store custom struct packing as an attribute of the type
         * object, to be able to fetch it when depythonifying the object.
         */
        v = PyLong_FromLong(pack);
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(structType);
            return NULL;
            // LCOV_EXCL_STOP
        }
        r = PyDict_SetItem(((PyTypeObject*)structType)->tp_dict, PyObjCNM___struct_pack__,
                           v);
        Py_DECREF(v);
        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(structType);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_mutex);
#endif
    PyObject* py_signature = PyUnicode_FromString(signature);
    if (py_signature == NULL) { // LCOV_BR_EXCL_LINE
        /* This leaks some memory, but we cannot safely
         * deallocate the type
         */
        // LCOV_EXCL_START
        structType = NULL;
        goto exit;
        // LCOV_EXCL_STOP
    }

    r = PyDict_SetItem(structRegistry, py_signature, structType);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        /* This leaks some memory, but we cannot safely
         * deallocate the type
         */
        // LCOV_EXCL_START
        Py_DECREF(py_signature);
        structType = NULL;
        goto exit;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(py_signature);

    /* Register again using the typecode used in the ObjC runtime */
    if (PyObjC_RemoveInternalTypeCodes((char*)signature) == -1) { // LCOV_BR_EXCL_LINE
        /* We've validated the type signature earlier, the
         * call should never fail.
         */
        // LCOV_EXCL_START
        structType = NULL;
        goto exit;
        // LCOV_EXCL_STOP
    }

    py_signature = PyUnicode_FromString(signature);
    if (py_signature == NULL) { // LCOV_BR_EXCL_LINE
        /* This leaks some memory, but we cannot safely
         * deallocate the type
         */
        structType = NULL; // LCOV_EXCL_LINE
        goto exit;         // LCOV_EXCL_LINE
    }

    r = PyDict_SetItem(structRegistry, py_signature, structType);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_signature);
        structType = NULL;
        // LCOV_EXCL_STOP
        goto exit; // LCOV_EXCL_LINE
    }
    Py_DECREF(py_signature);

exit:
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif

    return structType;
}

int
PyObjC_RegisterStructAlias(const char* signature, PyObject* structType)
{
    char buf[1024];
    int  r;
    int  retval = 0;

    if (strlen(signature) > 1023) {
        PyErr_SetString(PyExc_ValueError, "typestr too long");
        return -1;
    }
    if (PyObjCRT_RemoveFieldNames(buf, signature) == NULL) {
        return -1;
    }

    if (!PyObject_HasAttr(structType, PyObjCNM___typestr__)) {
        PyErr_SetString(PyExc_TypeError, "struct type is not valid");
        return -1;
    }
    /* XXX: This should check that the two structs have a
     * compatible encoding (some number of fields, compatible types)
     */

    assert(structRegistry != NULL);

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&registry_mutex);
#endif
    PyObject* py_buf = PyUnicode_FromString(buf);
    if (py_buf == NULL) { // LCOV_BR_EXCL_LINE
        retval = -1;      // LCOV_EXCL_LINE
        goto exit;        // LCOV_EXCL_LINE
    }

    r = PyDict_SetItem(structRegistry, py_buf, structType);
    if (r == -1) {         // LCOV_BR_EXCL_LINE
        Py_DECREF(py_buf); // LCOV_EXCL_LINE
        retval = -1;       // LCOV_EXCL_LINE
        goto exit;         // LCOV_EXCL_LINE
    }
    Py_DECREF(py_buf);

    /* Register again using the typecode used in the ObjC runtime */
    if (PyObjC_RemoveInternalTypeCodes(buf) == -1) { // LCOV_BR_EXCL_LINE
        retval = -1;                                 // LCOV_EXCL_LINE
        goto exit;                                   // LCOV_EXCL_LINE
    }

    py_buf = PyUnicode_FromString(buf);
    if (py_buf == NULL) { // LCOV_BR_EXCL_LINE
        retval = -1;      // LCOV_EXCL_LINE
        goto exit;        // LCOV_EXCL_LINE
    }
    r = PyDict_SetItem(structRegistry, py_buf, structType);
    if (r == -1) {         // LCOV_BR_EXCL_LINE
        Py_DECREF(py_buf); // LCOV_EXCL_LINE
        retval = -1;       // LCOV_EXCL_LINE
        goto exit;         // LCOV_EXCL_LINE
    }
    Py_DECREF(py_buf);

exit:
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&registry_mutex);
#endif

    return retval;
}

int
PyObjC_SetStructField(PyObject* self, Py_ssize_t offset, PyObject* newVal)
{
    Py_ssize_t   len;
    PyMemberDef* member;

    assert(newVal != NULL);

    len = STRUCT_LENGTH(self);

    if ((offset < 0) || (offset >= len)) { // LCOV_BR_EXCL_LINE
        /* XXX: Assertion error */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_IndexError, "%.100s index out of range",
                     Py_TYPE(self)->tp_name);
        return -1;
        // LCOV_EXCL_STOP
    }
    member = Py_TYPE(self)->tp_members + offset;
    Py_BEGIN_CRITICAL_SECTION(self);
    SET_STRUCT_FIELD(self, member, newVal);
    Py_END_CRITICAL_SECTION();
    return 0;
}

PyObject* _Nullable StructAsTuple(PyObject* strval)
{
    Py_ssize_t i, len = STRUCT_LENGTH(strval);
    PyObject*  retval = PyTuple_New(len);
    if (retval == NULL) { // LCOV_BR_EXCL_LINE
        return 0;         // LCOV_EXCL_LINE
    }

    Py_BEGIN_CRITICAL_SECTION(strval);
    for (i = 0; i < len; i++) {
        PyObject* v;
        v = GET_STRUCT_FIELD(strval, Py_TYPE(strval)->tp_members + i);
        assert(v != NULL);
        PyTuple_SET_ITEM(retval, i, v);
        Py_INCREF(v);
    } // LCOV_BR_EXCL_LINE
    Py_END_CRITICAL_SECTION();
    return retval;
}

int
PyObjCStruct_Init(PyObject* module __attribute__((__unused__)))
{
    structRegistry = PyDict_New();
    if (structRegistry == NULL) { // LCOV_BR_EXCL_LINE
        return -1;                // LCOV_EXCL_LINE
    }

    PyObjCMethodSignature* signature =
        PyObjCMethodSignature_WithMetaData("i^v^v^v", NULL, YES);
    if (signature == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(structRegistry);
        structRegistry = (PyObject* _Nonnull)NULL;
        return -1;
        // LCOV_EXCL_STOP
    }

    ffi_cif* temp_cif = PyObjCFFI_CIFForSignature(signature);
    Py_CLEAR(signature);
    if (temp_cif == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(structRegistry);
        structRegistry = (PyObject* _Nonnull)NULL;
        return -1;
        // LCOV_EXCL_STOP
    }
    init_cif = temp_cif;

    return 0;
}

NS_ASSUME_NONNULL_END
