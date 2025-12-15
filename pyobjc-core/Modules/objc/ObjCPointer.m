/* Copyright (c) 1996,97 by Lele Gaifax. All Rights Reserved
 * With various updates by Ronald Oussoren and others ((C) 2002-2021)
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

NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyObject_HEAD

    void*     ptr;
    PyObject* typestr;
} PyObjCPointer;

void* _Nullable PyObjCPointer_Ptr(PyObject* obj)
{
    /* The only caller checks the type as well */
    assert(PyObjCPointer_Check(obj));

    return ((PyObjCPointer*)(obj))->ptr;
}

static void
ptr_dealloc(PyObject* _self)
{
    PyObjCPointer* self = (PyObjCPointer*)_self;
    Py_XDECREF(self->typestr);
    PyTypeObject* tp = Py_TYPE(self);
    PyObject_Free((PyObject*)self);
    Py_DECREF(tp);
}

static PyMemberDef ptr_members[] = {{
                                        .name   = "typestr",
                                        .type   = T_OBJECT,
                                        .offset = offsetof(PyObjCPointer, typestr),
                                        .flags  = READONLY,
                                    },
                                    {
                                        .name   = "pointerAsInteger",
                                        .type   = T_LONG,
                                        .offset = offsetof(PyObjCPointer, ptr),
                                        .flags  = READONLY,
                                    },
                                    {
                                        .name = NULL /* SENTINEL */
                                    }};

PyDoc_STRVAR(ptr_doc, "Wrapper around a Objective-C Pointer");

static PyType_Slot ptr_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&ptr_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_members, .pfunc = (void*)&ptr_members},
    {.slot = Py_tp_doc, .pfunc = (void*)&ptr_doc},

    {0, NULL} /* sentinel */
};

static PyType_Spec ptr_spec = {
    .name      = "objc.PyObjCPointer",
    .basicsize = sizeof(PyObjCPointer),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .slots = ptr_slots,
};

PyObject* PyObjCPointer_Type = (PyObject* _Nonnull)NULL;

PyObject* _Nullable PyObjCPointer_New(void* p, const char* t)
{
    Py_ssize_t size = PyObjCRT_SizeOfType(t);
    if (size == -1) {
        return NULL;
    }

    const char* typeend = PyObjCRT_SkipTypeSpec(t);
    if (typeend == NULL) {
        return NULL;
    }

    // The loop below should never be used in practice because
    // the signature passed in has already be cleaned from
    // spurious digits.
    //
    // The loop is left in just in case...
    while (unlikely(isdigit(typeend[-1]))) { // LCOV_BR_EXCL_LINE
        typeend--;                           // LCOV_EXCL_LINE
    }
    PyObjCPointer* self;

    if (PyObjCPointer_RaiseException) {
        return PyErr_Format(PyObjCExc_UnknownPointerError, "pointer of type %s", t);
    }

    if (PyErr_WarnFormat(PyObjCExc_ObjCPointerWarning, 0,
                         "PyObjCPointer created: at %p of type %s", p, t)
        == -1) {
        return NULL;
    }

    self = PyObject_NEW(PyObjCPointer, (PyTypeObject*)PyObjCPointer_Type);
    if (unlikely(self == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;              // LCOV_EXCL_LINE
    }

    self->typestr = PyBytes_FromStringAndSize((char*)t, typeend - t);
    self->ptr     = p;

    if (unlikely(self->typestr == NULL)) { // LCOV_BR_EXCL_LINE
        Py_DECREF(self);                   // LCOV_EXCL_LINE
        return NULL;                       // LCOV_EXCL_LINE
    }

    return (PyObject*)self;
}

int
PyObjCPointer_Setup(PyObject* module)
{
    PyObject* tmp = PyType_FromSpec(&ptr_spec);
    if (unlikely(tmp == NULL)) { // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE
    }
    PyObjCPointer_Type = tmp;

    int r = PyModule_AddObject(module, "ObjCPointer", PyObjCPointer_Type);
    if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
        return -1;           // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCPointer_Type);
    return 0;
}

NS_ASSUME_NONNULL_END
