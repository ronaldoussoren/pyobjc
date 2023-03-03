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
    PyObjC_Assert(PyObjCPointer_Check(obj), NULL);

    return ((PyObjCPointer*)(obj))->ptr;
}

#if PY_VERSION_HEX < 0x030a0000
static PyObject* _Nullable ptr_new(PyObject* self __attribute__((__unused__)),
                                   PyObject* args __attribute__((__unused__)),
                                   PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "cannot create 'objc.PyObjCPointer' instances");
    return NULL;
}
#endif

static void
ptr_dealloc(PyObject* _self)
{
    PyObjCPointer* self = (PyObjCPointer*)_self;
    Py_XDECREF(self->typestr);
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(self);
#endif
    PyObject_Free((PyObject*)self);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
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
#if PY_VERSION_HEX < 0x030a0000
    {.slot = Py_tp_new, .pfunc = (void*)&ptr_new},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec ptr_spec = {
    .name      = "objc.PyObjCPointer",
    .basicsize = sizeof(PyObjCPointer),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
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

    while (isdigit(typeend[-1])) {
        typeend--;
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
    if (self == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    self->typestr = PyBytes_FromStringAndSize((char*)t, typeend - t);
    self->ptr     = p;

    if (self->typestr == NULL) { // LCOV_BR_EXCL_LINE
        Py_DECREF(self);         // LCOV_EXCL_LINE
        return NULL;             // LCOV_EXCL_LINE
    }

    return (PyObject*)self;
}

int
PyObjCPointer_Setup(PyObject* module)
{
    PyObject* tmp = PyType_FromSpec(&ptr_spec);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }
    PyObjCPointer_Type = tmp;

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "ObjCPointer", PyObjCPointer_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCPointer_Type);
    return 0;
}

NS_ASSUME_NONNULL_END
