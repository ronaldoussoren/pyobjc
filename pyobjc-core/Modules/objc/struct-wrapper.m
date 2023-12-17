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
        return NULL;
    }

    member = Py_TYPE(self)->tp_members + offset;
    res    = GET_STRUCT_FIELD(self, member);
    PyObjC_Assert(res != NULL, NULL);

    Py_INCREF(res);
    return res;
}

static PyObject* _Nullable struct_sq_slice(PyObject* self, Py_ssize_t ilow,
                                           Py_ssize_t ihigh)
{
    PyObject*  result;
    Py_ssize_t i;

#ifdef PyObjC_DEBUG
    Py_ssize_t len = STRUCT_LENGTH(self);
#endif
    PyObjC_Assert(ilow >= 0, NULL);
    PyObjC_Assert(ihigh <= len, NULL);

    result = PyTuple_New(ihigh - ilow);
    if (result == NULL) {
        return NULL; // LCOV_EXCL_LINE
    }

    for (i = ilow; i < ihigh; i++) {
        PyMemberDef* member = Py_TYPE(self)->tp_members + i;
        PyObject*    v      = GET_STRUCT_FIELD(self, member);
        PyObjC_Assert(v != NULL, NULL);
        Py_INCREF(v);
        PyTuple_SET_ITEM(result, i - ilow, v);
    }
    return result;
}

static int
struct_sq_ass_item(PyObject* self, Py_ssize_t offset, PyObject* _Nullable newVal)
{
    Py_ssize_t   len;
    PyMemberDef* member;

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

    if (newVal == NULL) {
        PyErr_Format(PyExc_TypeError,
                     "Cannot delete item '%" PY_FORMAT_SIZE_T "d' in a %.100s instance",
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
    SET_STRUCT_FIELD(self, member, newVal);
    return 0;
}

static int
struct_sq_ass_slice(PyObject* self, Py_ssize_t ilow, Py_ssize_t ihigh, PyObject* v)
{
    PyObject*  seq;
    Py_ssize_t i;

    if (v == NULL) {
        PyErr_Format(PyExc_TypeError, "Cannot delete items in instances of %.100s",
                     Py_TYPE(self)->tp_name);
        return -1;
    }

#ifdef PyObjC_DEBUG
    Py_ssize_t len = STRUCT_LENGTH(self);
#endif
    PyObjC_Assert(ilow >= 0, -1);
    PyObjC_Assert(ilow <= len, -1);
    PyObjC_Assert(ihigh >= 0, -1);
    PyObjC_Assert(ihigh <= len, -1);

    seq = PySequence_Fast(v, "Must assign sequence to slice");
    if (seq == NULL)
        return -1;

    if (PySequence_Fast_GET_SIZE(seq) != ihigh - ilow) {
        Py_DECREF(seq);
        PyErr_Format(PyExc_TypeError,
                     "Slice assignment would change size of %.100s "
                     "instance",
                     Py_TYPE(self)->tp_name);
        return -1;
    }

    for (i = ilow; i < ihigh; i++) {
        PyObject*    x;
        PyMemberDef* member = Py_TYPE(self)->tp_members + i;

        x = PySequence_Fast_GET_ITEM(seq, i - ilow);
        PyObjC_Assert(x != NULL, -1);
        SET_STRUCT_FIELD(self, member, x);
    }
    Py_DECREF(seq);
    return 0;
}

static int
struct_sq_contains(PyObject* self, PyObject* value)
{

    if (!PyObjC_StructsIndexable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences",
                     Py_TYPE(self)->tp_name);
        return -1;
    }

    for (PyMemberDef* member = Py_TYPE(self)->tp_members; member && member->name;
         member++) {
        int       r;
        PyObject* cur = GET_STRUCT_FIELD(self, member);
        PyObjC_Assert(cur != NULL, -1);

        r = PyObject_RichCompareBool(cur, value, Py_EQ);
        if (r == -1) {
            return -1;
        } else if (r) {
            return 1;
        }
    }
    return 0;
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

    for (i = 0; i < len; i++) {
        PyObject* v = GET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + i);
        PyObjC_Assert(v != NULL, NULL);
        Py_INCREF(v);
        PyTuple_SET_ITEM(values, i, v);
    }

    result = Py_BuildValue("(OO)", Py_TYPE(self), values);
    Py_DECREF(values);
    return result;
}

static PyObject* _Nullable struct_sizeof(PyObject* self)
{
    return PyLong_FromSsize_t(Py_TYPE(self)->tp_basicsize);
}

static PyObject* _Nullable struct_copy(PyObject* self)
{
    PyObject*    result;
    PyMemberDef* member = Py_TYPE(self)->tp_members;

    result = PyObject_GC_New(PyObject, Py_TYPE(self));
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    while (member && member->name) {
        PyObjC_Assert(member->type == T_OBJECT, NULL);
        *((PyObject**)(((char*)result) + member->offset)) = NULL;
        PyObject* t = GET_STRUCT_FIELD(self, member);
        PyObjC_Assert(t != NULL, NULL);

        if (t != NULL) {
            /*
             * XXX: Maybe change to unconditional (vector) call, with fallback
             * to current behaviour on attributeerror?
             *
             * XXX: Consider using ``__copy__`` instead.
             */

            /* "t" is a borrowed reference, make sure this reference
             * stays alive while we're working with it even if
             * "__pyobjc_copy__" does something nasty.
             */
            Py_INCREF(t);
            PyObject* m = PyObject_GetAttrString(t, "__pyobjc_copy__");
            if (m == NULL) {
                PyErr_Clear();
                SET_STRUCT_FIELD(result, member, t);
            } else {
                PyObject* args[1] = {NULL};
                PyObject* c       = PyObject_Vectorcall(
                    m, args + 1, 0 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
                Py_DECREF(m);
                if (c == NULL) {
                    Py_DECREF(t);
                    Py_DECREF(result);
                    return NULL;
                }
                SET_STRUCT_FIELD(result, member, c);
                Py_DECREF(c);
            }
            Py_DECREF(t);
        }

        member++;
    }

    PyObject_GC_Track(result);
    return result;
}

static PyObject* _Nullable struct_replace(PyObject* self, PyObject* _Nullable args,
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
        PyErr_SetString(PyExc_TypeError, "_replace called with positional arguments");
        return NULL;
    }

    result = struct_copy(self);
    if (result == NULL) {
        return NULL;
    }

    if (kwds != NULL) {
        while (PyDict_Next(kwds, &pos, &key, &value)) {
            int r = PyObject_SetAttr(result, key, value);
            if (r == -1) {
                Py_DECREF(result);
                return NULL;
            }
        }
    }

    return result;
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

    while (member && member->name) {
        PyObject* t;
        PyObjC_Assert(member->type == T_OBJECT, NULL);

        t = GET_STRUCT_FIELD(self, member);
        PyObjC_Assert(t != NULL, NULL);
        r = PyDict_SetItemString(result, member->name, t);

        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        member++;
    }

    return result;
}

static PyObject* _Nullable struct_mp_subscript(PyObject* self, PyObject* item)
{
    if (!PyObjC_StructsIndexable) {
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences 7",
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
        PyErr_Format(PyExc_TypeError, "Instances of '%.100s' are not sequences 8",
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

        PyObject* seq = PySequence_Fast(value, "must assign sequence to slice");
        if (seq == NULL)
            return -1;

        if (PySequence_Fast_GET_SIZE(seq) != slicelength) {
            Py_DECREF(seq);
            PyErr_Format(PyExc_TypeError,
                         "slice assignment would change size of %.100s "
                         "instance",
                         Py_TYPE(self)->tp_name);
            return -1;
        }

        Py_ssize_t cur, i;
        for (cur = start, i = 0; i < slicelength; cur += step, i++) {
            int r = struct_sq_ass_item(self, cur, PySequence_Fast_GET_ITEM(seq, i));
            if (r == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(seq);
                return -1;
                // LCOV_EXCL_STOP
            }
        }

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
        .ml_meth  = (PyCFunction)struct_copy,
        .ml_flags = METH_NOARGS,
        .ml_doc   = "Return a copy of the struct",
    },
    {
        .ml_name  = "__pyobjc_copy__",
        .ml_meth  = (PyCFunction)struct_copy,
        .ml_flags = METH_NOARGS,
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
        PyObjC_Assert(member->type == T_OBJECT, NULL);
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
        PyObjC_Assert(*typestr != '"', -1);
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
            v = PyBool_FromLong(0);
            break;
#endif
        case _C_NSBOOL:
            v = PyBool_FromLong(0);
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
    }

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
                         "%.100s() takes at most %" PY_FORMAT_SIZE_T
                         "d %sarguments (%" PY_FORMAT_SIZE_T "d given)",
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
    static ffi_cif* init_cif = NULL;
    ffi_closure*    cl       = NULL;
    void*           codeloc;
    const char*     typestr_copy;

    typestr_copy = PyObjCUtil_Strdup(_typestr);
    if (typestr_copy == NULL) {
        return NULL; // LCOV_EXCL_LINE
    }

    if (init_cif == NULL) {
        PyObjCMethodSignature* signature =
            PyObjCMethodSignature_WithMetaData("i^v^v^v", NULL, YES);
        if (signature == NULL) {
            return NULL; // LCOV_EXCL_LINE
        }
        init_cif = PyObjCFFI_CIFForSignature(signature);
        Py_DECREF(signature);
        if (init_cif == NULL) {
            // LCOV_EXCL_START
            PyMem_Free((void*)typestr_copy);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

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

        for (i = 0; i < len; i++) {
            int k;

            self_cur  = GET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + i);
            other_cur = GET_STRUCT_FIELD(other, Py_TYPE(other)->tp_members + i);
            PyObjC_Assert(self_cur != NULL, NULL);
            PyObjC_Assert(other_cur != NULL, NULL);

            k = PyObject_RichCompareBool(self_cur, other_cur, Py_EQ);
            if (k < 0) {
                return NULL;
            }

            if (!k) {
                /* Not equal, result is the comparison of the last
                 * item, we can do better for '==' and '!='.
                 */
                PyObject* v;

                if (op == Py_EQ) {
                    Py_INCREF(Py_False);
                    return Py_False;
                } else if (op == Py_NE) {
                    Py_INCREF(Py_True);
                    return Py_True;
                }
                v = PyObject_RichCompare(self_cur, other_cur, op);
                return v;
            }
        }

        /* All items are equal, compare using sizes */
        switch (op) {
        case Py_LT:
        case Py_NE:
        case Py_GT:
            Py_INCREF(Py_False);
            return Py_False;

        case Py_LE:
        case Py_EQ:
        case Py_GE:
            Py_INCREF(Py_True);
            return Py_True;

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
            Py_INCREF(Py_False);
            return Py_False;

        } else if (op == Py_NE) {
            Py_INCREF(Py_True);
            return Py_True;

        } else {
            PyErr_Format(PyExc_TypeError, "Cannot compare instances of %.100s and %.100s",
                         Py_TYPE(self)->tp_name, Py_TYPE(other)->tp_name);
            return NULL;
        }

    } else if (!PyObjC_StructsIndexable) {
        if (op == Py_EQ) {
            Py_INCREF(Py_False);
            return Py_False;

        } else if (op == Py_NE) {
            Py_INCREF(Py_True);
            return Py_True;

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
            Py_INCREF(Py_False);
            return Py_False;

        } else {
            Py_INCREF(Py_True);
            return Py_True;
        }
    }

    for (i = 0; i < len; i++) {
        int k;

        self_cur = GET_STRUCT_FIELD(self, Py_TYPE(self)->tp_members + i);
        PyObjC_Assert(self_cur != NULL, NULL);
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
                Py_INCREF(Py_False);
                return Py_False;
            } else if (op == Py_NE) {
                Py_INCREF(Py_True);
                return Py_True;
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
        Py_INCREF(Py_True);
        return Py_True;

    } else {
        Py_INCREF(Py_False);
        return Py_False;
    }
}

static int
struct_traverse(PyObject* self, visitproc visit, void* _Nullable arg)
{
    PyMemberDef* member;
    PyObject*    v;
    int          err;

    for (member = Py_TYPE(self)->tp_members; member && member->name; member++) {
        v = GET_STRUCT_FIELD(self, member);
        if (v == NULL) // LCOV_BR_EXCL_LINE
            continue;  // LCOV_EXCL_LINE
        err = visit(v, arg);
        if (err)
            return err;
    }
    return 0;
}

static int
struct_clear(PyObject* self)
{
    PyMemberDef* member;

    for (member = Py_TYPE(self)->tp_members; member && member->name; member++) {
        /* Maintain the invariant that struct fields are not NULL.
         *
         * The CPython documentation says that fields should be set to
         * NULL, but the primary reason is to ensure that there are no
         * reference cycles and Py_None cannot be part of such a cycle.
         */
        SET_STRUCT_FIELD(self, member, Py_None);
    }
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

        v = GET_STRUCT_FIELD(self, member);
        PyObjC_Assert(v != NULL, NULL);

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
    }

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
PyObjC_MakeStructType(const char* name, const char* _Nullable doc,
                      initproc _Nullable tpinit, Py_ssize_t                  numFields,
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
    }
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
    if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
            result->base.tp_dict, "_fields", fields)
        == -1) {
        // LCOV_EXCL_START
        Py_DECREF(fields);
        PyMem_Free(members);
        PyMem_Free(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

#if PY_VERSION_HEX >= 0x030a0000
    if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
            result->base.tp_dict, "__match_args__", fields)
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

    if (tpinit) {
        result->base.tp_init = tpinit;

    } else {
        result->base.tp_init = make_init(typestr);
        if (result->base.tp_init == NULL) {
            PyMem_Free(members);
            PyMem_Free(result);
            return NULL;
        }
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

static PyObject* structRegistry = NULL;

PyObject* _Nullable PyObjC_FindRegisteredStruct(const char* signature, Py_ssize_t len)
{
    PyObject* type;
    PyObject* v;

    if (structRegistry == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;              // LCOV_EXCL_LINE
    }

    v = PyUnicode_FromStringAndSize(signature, len);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    type = PyDict_GetItemWithError(structRegistry, v);
    Py_DECREF(v);
    if (type == NULL) {
        return NULL;
    }

    Py_INCREF(type);
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

    if (structRegistry == NULL)
        return NULL;

    if (ppack != NULL) {
        *ppack = -1;
    }

    v = PyUnicode_FromStringAndSize(signature, len);

    type = (PyTypeObject*)PyDict_GetItemWithError(structRegistry, v);
    Py_DECREF(v);
    if (type == NULL) {
        return NULL;
    }

    member = type->tp_members;

    result = PyObject_GC_New(PyObject, type);
    if (result == NULL) {
        // LCOV_EXCL_START
        PyErr_Clear();
        return NULL;
        // LCOV_EXCL_STOP
    }

    while (member && member->name) {
        PyObjC_Assert(member->type == T_OBJECT, NULL);
        *((PyObject**)(((char*)result) + member->offset)) = Py_None;
        Py_INCREF(Py_None);
        member++;
    }

    PyObject_GC_Track(result);

    if (objc_encoding) {
        PyObject* typestr = PyDict_GetItemStringWithError(type->tp_dict, "__typestr__");
        if (typestr == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        if (typestr != NULL) {
            if (!PyBytes_Check(typestr)) {
                PyErr_SetString(PyExc_TypeError, "__typestr__ not a bytes object");
                Py_DECREF(result);
                return NULL;
            }
            *objc_encoding = PyBytes_AsString(typestr);

        } else {
            /* XXX: Can this ever happen? */
            *objc_encoding = signature;
        }
    }

    if (ppack != NULL) {
        *ppack = ((struct StructTypeObject*)type)->pack;
    }

    return result;
}

PyObject* _Nullable PyObjC_RegisterStructType(const char* signature, const char* name,
                                              const char* _Nullable doc,
                                              initproc _Nullable tpinit,
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

            if (*sigcur == _C_STRUCT_E)
                break;
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
                PyObjC_Assert(end != NULL, NULL);

                fieldnames[numFields] = PyMem_Malloc(end - sigcur + 1);
                memcpy((char*)fieldnames[numFields], sigcur, end - sigcur);
                ((char*)fieldnames[numFields])[end - sigcur] = '\0';
                sigcur                                       = end + 1;
            }
            numFields++;
            sigcur = PyObjCRT_NextField(sigcur);
            PyObjC_Assert(sigcur != NULL, NULL);
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
        PyObjC_Assert(fieldnames, NULL);
    }

    structType =
        PyObjC_MakeStructType(name, doc, tpinit, numFields, fieldnames, signature, pack);
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
        }
        return NULL;
    }

    v = PyBytes_FromString(signature);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(structType);
        return NULL;
        // LCOV_EXCL_STOP
    }

    r = PyDict_SetItemString(((PyTypeObject*)structType)->tp_dict, "__typestr__", v);
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
        r = PyDict_SetItemString(((PyTypeObject*)structType)->tp_dict, "__struct_pack__",
                                 v);
        Py_DECREF(v);
        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(structType);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    if (structRegistry == NULL) {
        structRegistry = PyDict_New();
        if (structRegistry == NULL) { // LCOV_BR_EXCL_LINE
            /* This leaks some memory, but we cannot safely
             * deallocate the type
             *
             * XXX: Why is that?
             */
            return NULL; // LCOV_EXCL_LINE
        }
    }

    r = PyDict_SetItemString(structRegistry, signature, structType);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        /* This leaks some memory, but we cannot safely
         * deallocate the type
         */
        return NULL; // LCOV_EXCL_LINE
    }

    /* Register again using the typecode used in the ObjC runtime */
    if (PyObjC_RemoveInternalTypeCodes((char*)signature) == -1) { // LCOV_BR_EXCL_LINE
        /* We've validated the type signature earlier, the
         * call should never fail.
         */
        return NULL; // LCOV_EXCL_LINE
    }
    r = PyDict_SetItemString(structRegistry, signature, structType);
    if (r == -1) {   // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    return structType;
}

int
PyObjC_RegisterStructAlias(const char* signature, PyObject* structType)
{
    char buf[1024];
    int  r;

    if (strlen(signature) > 1023) {
        PyErr_SetString(PyExc_ValueError, "typestr too long");
        return -1;
    }
    if (PyObjCRT_RemoveFieldNames(buf, signature) == NULL) {
        return -1;
    }

    if (!PyObject_HasAttrString(structType, "__typestr__")) {
        PyErr_SetString(PyExc_TypeError, "struct type is not valid");
        return -1;
    }
    /* XXX: This should check that the two structs have a
     * compatible encoding (some number of fields, compatible types)
     */

    if (structRegistry == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        structRegistry = PyDict_New();
        if (structRegistry == NULL) { // LCOV_BR_EXCL_LINE
            return -1;                // LCOV_EXCL_LINE
        }
        // LCOV_EXCL_STOP
    }

    r = PyDict_SetItemString(structRegistry, buf, structType);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    /* Register again using the typecode used in the ObjC runtime */
    if (PyObjC_RemoveInternalTypeCodes(buf) == -1) { // LCOV_BR_EXCL_LINE
        return -1;                                   // LCOV_EXCL_LINE
    }
    r = PyDict_SetItemString(structRegistry, buf, structType);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

int
PyObjC_SetStructField(PyObject* self, Py_ssize_t offset, PyObject* newVal)
{
    Py_ssize_t   len;
    PyMemberDef* member;

    PyObjC_Assert(newVal != NULL, -1);

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
    SET_STRUCT_FIELD(self, member, newVal);
    return 0;
}

PyObject* _Nullable StructAsTuple(PyObject* strval)
{
    Py_ssize_t i, len = STRUCT_LENGTH(strval);
    PyObject*  retval = PyTuple_New(len);
    if (retval == NULL) {
        return 0; // LCOV_EXCL_LINE
    }

    for (i = 0; i < len; i++) {
        PyObject* v;
        v = GET_STRUCT_FIELD(strval, Py_TYPE(strval)->tp_members + i);
        PyObjC_Assert(v != NULL, NULL);
        PyTuple_SET_ITEM(retval, i, v);
        Py_INCREF(v);
    }
    return retval;
}

NS_ASSUME_NONNULL_END
