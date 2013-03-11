/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 * With various updates by Ronald Oussoren and others ((C) 2002, 2003)
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * Created Mon Oct 28 12:38:18 1996.
 *
 */

#include "pyobjc.h"


typedef struct
{
    PyObject_VAR_HEAD

    void *ptr;
    PyObject *type;
    char contents[1];
} PyObjCPointer;


void*
PyObjCPointer_Ptr(PyObject* obj)
{
    if (!PyObjCPointer_Check(obj)) {
        PyErr_SetString(PyExc_TypeError, "Unexpected type");
        return NULL;
    }
    return ((PyObjCPointer*)(obj))->ptr;
}

static void
PyObjCPointer_dealloc (PyObject* _self)
{
    PyObjCPointer* self = (PyObjCPointer*)_self;
    Py_CLEAR (self->type);
    PyObject_Free((PyObject*)self);
}

PyDoc_STRVAR(PyObjCPointer_unpack_doc,
    "Unpack the pointed value accordingly to its type.\n"
    "obj.unpack() -> value");

static PyObject *
PyObjCPointer_unpack (PyObject* _self)
{
    PyObjCPointer* self = (PyObjCPointer*)_self;

    if (PyErr_WarnEx(
        PyExc_DeprecationWarning,
            "Using ObjCPointer is deprecated, unpack will be removed in PyObjC 3.1",
            1) < 0) {

        return NULL;
    }

    if (self->ptr) {
        const char *type = PyBytes_AS_STRING(self->type);

        if (*type == _C_VOID) {
            PyErr_SetString (PyObjCExc_Error,
                "Cannot dereference a pointer to void");
            return NULL;
        } else {
            return pythonify_c_value(type, self->ptr);
        }
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}

static PyMethodDef PyObjCPointer_methods[] =
{
    {
        "unpack",
        (PyCFunction)PyObjCPointer_unpack,
        METH_NOARGS,
        PyObjCPointer_unpack_doc
    },
    { 0, 0, 0, 0 }
};

static PyMemberDef PyObjCPointer_members[] = {
    {
        "type",
        T_OBJECT,
        offsetof(PyObjCPointer, type),
        READONLY,
        NULL
    },
    {
        "pointerAsInteger",
        T_INT,
        offsetof(PyObjCPointer, ptr),
        READONLY,
        NULL
    },
    { 0, 0, 0, 0, 0 }
};

PyTypeObject PyObjCPointer_Type =
{
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "PyObjCPointer",
    .tp_basicsize   = sizeof (PyObjCPointer),
    .tp_itemsize    = sizeof (char),
    .tp_dealloc     = PyObjCPointer_dealloc,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = "Wrapper around a Objective-C Pointer",
    .tp_methods     = PyObjCPointer_methods,
    .tp_members     = PyObjCPointer_members,
};

PyObject *
PyObjCPointer_New(void *p, const char *t)
{
    Py_ssize_t size = PyObjCRT_SizeOfType (t);
    const char *typeend = PyObjCRT_SkipTypeSpec (t);
    PyObjCPointer *self;

    if (PyObjCPointer_RaiseException) {
        PyErr_Format(PyObjCExc_UnknownPointerError,
            "pointer of type %s", t);
        return NULL;
    }
    NSLog(@"PyObjCPointer created: at %p of type %s", p, t);

    if (size == -1) {
        return NULL;
    }
    if (typeend == NULL) {
        return NULL;
    }

    self = PyObject_NEW_VAR(PyObjCPointer, &PyObjCPointer_Type, size);
    if (self == NULL) {
        return NULL;
    }

    self->type = PyBytes_FromStringAndSize ((char *) t, typeend-t);

    if (size && p) {
        memcpy ((self->ptr = self->contents), p, size);
    } else {
        self->ptr = p;
    }

    return (PyObject*)self;
}
