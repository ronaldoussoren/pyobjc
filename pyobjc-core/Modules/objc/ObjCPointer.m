/* Copyright (c) 1996,97 by Lele Gaifax. All Rights Reserved
 * With various updates by Ronald Oussoren and others ((C) 2002-2017)
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
    PyObject_HEAD

    void *ptr;
    PyObject *type;
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

static PyMemberDef PyObjCPointer_members[] = {
    {
        .name   = "type",
        .type   = T_OBJECT,
        .offset = offsetof(PyObjCPointer, type),
        .flags  = READONLY,
    },
    {
        .name   = "pointerAsInteger",
        .type   = T_LONG,
        .offset = offsetof(PyObjCPointer, ptr),
        .flags  = READONLY,
    },
    {
        .name   = NULL  /* SENTINEL */
    }
};

PyTypeObject PyObjCPointer_Type =
{
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "PyObjCPointer",
    .tp_basicsize   = sizeof (PyObjCPointer),
    .tp_itemsize    = 0,
    .tp_dealloc     = PyObjCPointer_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = "Wrapper around a Objective-C Pointer",
    .tp_members     = PyObjCPointer_members,
};

PyObject *
PyObjCPointer_New(void *p, const char *t)
{
    Py_ssize_t size = PyObjCRT_SizeOfType (t);
    const char *typeend = PyObjCRT_SkipTypeSpec (t);
    while (isdigit(typeend[-1])) {
        typeend --;
    }
    PyObjCPointer *self;

    if (PyObjCPointer_RaiseException) {
        PyErr_Format(PyObjCExc_UnknownPointerError,
            "pointer of type %s", t);
        return NULL;
    }

#if PY_MAJOR_VERSION == 3
    if (PyErr_WarnFormat(PyObjCExc_ObjCPointerWarning, 0, "PyObjCPointer created: at %p of type %s", p, t) == -1) {
    	return NULL;
    }
#else
    char buf[256];
    snprintf(buf, 256, "PyObjCPointer created: at %p of type %s", p, t);
    if (PyErr_Warn(PyObjCExc_ObjCPointerWarning, buf) == -1) {
    	return NULL;
    }
#endif

    if (size == -1) {
        return NULL;
    }
    if (typeend == NULL) {
        return NULL;
    }

    self = PyObject_NEW(PyObjCPointer, &PyObjCPointer_Type);
    if (self == NULL) {
        return NULL;
    }

    self->type = PyBytes_FromStringAndSize ((char *) t, typeend-t);
    self->ptr = p;

    return (PyObject*)self;
}
