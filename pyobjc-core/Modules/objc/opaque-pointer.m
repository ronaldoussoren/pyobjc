/*
 * Generic support for opaque pointer types, such as NSZone*
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyObject_HEAD

    void* _Nullable pointer_value;
} OpaquePointerObject;

static PyMemberDef opaque_members[] = {
    {.name   = "__pointer__",
     .type   = T_LONG,
     .offset = offsetof(OpaquePointerObject, pointer_value),
     .flags  = READONLY,
     .doc    = "raw value of the pointer"},
    {
        .name = NULL /* SENTINEL */
    }};

static PyObject* _Nullable as_cobject(PyObject* self)
{
    if (((OpaquePointerObject*)self)->pointer_value == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return PyCapsule_New(((OpaquePointerObject*)self)->pointer_value, "objc.__opaque__",
                         NULL);
}

static PyObject* _Nullable as_ctypes_voidp(PyObject* self)
{
    return PyObjC_MakeCVoidP(((OpaquePointerObject*)self)->pointer_value);
}

static PyObject* _Nullable opaque_sizeof(PyObject* self)
{
    return PyLong_FromSsize_t(Py_TYPE(self)->tp_basicsize);
}

static PyMethodDef opaque_methods[] = {
    {.ml_name  = "__cobject__",
     .ml_meth  = (PyCFunction)as_cobject,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "get a CObject representing this object"},
    {.ml_name  = "__c_void_p__",
     .ml_meth  = (PyCFunction)as_ctypes_voidp,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "get a ctypes.void_p representing this object"},
    {
        .ml_name  = "__sizeof__",
        .ml_meth  = (PyCFunction)opaque_sizeof,
        .ml_flags = METH_NOARGS,
    },
    {
        .ml_name = NULL /* SENTINEL */
    }};

static PyObject* _Nullable opaque_new(PyTypeObject* type, PyObject* _Nullable args,
                                      PyObject* _Nullable kwds)
{
    static char* keywords[] = {"cobject", "c_void_p", NULL};
    PyObject*    cobject    = NULL;
    PyObject*    c_void_p   = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OO", keywords, &cobject, &c_void_p)) {
        return NULL;
    }

    if (cobject != NULL && c_void_p != NULL) {
        PyErr_SetString(PyExc_ValueError, "pass 'cobject' or 'c_void_p', not both");
        return NULL;
    }

    if (cobject != NULL) {
        OpaquePointerObject* result;
        void*                p;

        if (!PyCapsule_CheckExact(cobject)) {
            PyErr_SetString(PyExc_TypeError, "'cobject' argument is not a PyCapsule");
            return NULL;
        }

        p = PyCapsule_GetPointer(cobject, "objc.__opaque__");
        if (p == NULL && PyErr_Occurred()) {
            return NULL;
        }

        result = PyObject_New(OpaquePointerObject, type);
        if (result == NULL) {
            return NULL;
        }

        result->pointer_value = p;
        return (PyObject*)result;

    } else if (c_void_p != NULL) {
        OpaquePointerObject* result;
        void*                p;
        PyObject*            attrval;

        if (PyLong_Check(c_void_p)) {
            attrval = c_void_p;
            Py_INCREF(attrval);

        } else {
            attrval = PyObject_GetAttrString(c_void_p, "value");
            if (attrval == NULL) {
                return NULL;
            }
        }

        if (PyLong_Check(attrval)) {
            p = PyLong_AsVoidPtr(attrval);
            if (p == NULL && PyErr_Occurred()) {
                Py_DECREF(attrval);
                return NULL;
            }

        } else {
            PyErr_SetString(PyExc_ValueError, "c_void_p.value is not an integer");
            return NULL;
        }

        Py_DECREF(attrval);
        result = PyObject_New(OpaquePointerObject, type);
        if (result == NULL) {
            return NULL;
        }

        result->pointer_value = p;
        return (PyObject*)result;

    } else {
        PyErr_Format(PyExc_TypeError, "Cannot create %s objects", type->tp_name);
        return NULL;
    }
}

static void
opaque_dealloc(PyObject* self)
{
    PyObject_Del(self);
}

static int
opaque_traverse(PyObject* self __attribute__((__unused__)),
                visitproc visit __attribute__((__unused__)),
                void*     arg __attribute__((__unused__)))
{
#if PY_VERSION_HEX >= 0x03090000
    Py_VISIT(Py_TYPE(self));
#endif /* PY_VERSION_HEX >= 0x03090000 */
    return 0;
}

static void
opaque_from_c(ffi_cif* cif __attribute__((__unused__)), void* retval, void** args,
              void* userdata)
{
    void*                pointer_value = *(void**)args[0];
    PyTypeObject*        opaque_type   = (PyTypeObject*)userdata;
    OpaquePointerObject* result;

    result = PyObject_New(OpaquePointerObject, opaque_type);
    if (result == NULL) {
        *(PyObject**)retval = NULL;
        return;
    }

    result->pointer_value = pointer_value;
    *(PyObject**)retval   = (PyObject*)result;
}

static void
opaque_to_c(ffi_cif* cif __attribute__((__unused__)), void* retval, void** args,
            void* userdata)
{
    PyObject*     obj         = *(PyObject**)args[0];
    void*         pObj        = *(void**)args[1];
    PyTypeObject* opaque_type = (PyTypeObject*)userdata;

    if (!PyObject_TypeCheck((obj), opaque_type)) {
        *(void**)pObj = (void*)0xDEADBEEF; /* force errors */
        PyErr_Format(PyExc_TypeError, "Need instance of %s, got instance of %s",
                     opaque_type->tp_name, Py_TYPE(obj)->tp_name);
        *(int*)retval = -1;
        return;
    }

    *(void**)pObj = ((OpaquePointerObject*)obj)->pointer_value;
    *(int*)retval = 0;
}

/*
 * Usage:
 *     PyDict_SetItemString(moduleDict, "NSZonePointer",
 *         PyObjCCreateOpaquePointerType(
 *             "Foundation.NSZonePointer",
 *             @encode(NSZone*),
 *             NSZonePointer_doc));
 */
PyObject* _Nullable PyObjCCreateOpaquePointerType(const char* name, const char* typestr,
                                                  const char* _Nullable docstr)
{
    static const char convert_cif_signature[] = {_C_INT, _C_PTR,  _C_VOID,
                                                 _C_PTR, _C_VOID, 0};
    static const char new_cif_signature[]     = {_C_PTR, _C_VOID, _C_PTR, _C_VOID, 0};
    static ffi_cif*   convert_cif             = NULL;
    static ffi_cif*   new_cif                 = NULL;

    /* XXX: 'name' should be copied, see BPO 45315 */
    PyObject*                           newType   = NULL;
    PyObjCPointerWrapper_ToPythonFunc   from_c    = NULL;
    PyObjCPointerWrapper_FromPythonFunc to_c      = NULL;
    ffi_closure*                        cl_to_c   = NULL;
    ffi_closure*                        cl_from_c = NULL;
    ffi_status                          rv;
    int                                 r;
    PyObject*                           v       = NULL;
    PyObject*                           w       = NULL;
    void*                               codeloc = NULL;
    char*                               dot;
    char                                buf[256];

    if (new_cif == NULL) {
        PyObjCMethodSignature* signature;
        signature = PyObjCMethodSignature_WithMetaData(new_cif_signature, NULL, NO);
        if (signature == NULL) {
            return NULL;
        }
        new_cif = PyObjCFFI_CIFForSignature(signature);
        Py_DECREF(signature);
        if (new_cif == NULL) {
            return NULL;
        }
    }

    if (convert_cif == NULL) {
        PyObjCMethodSignature* signature;
        signature = PyObjCMethodSignature_WithMetaData(convert_cif_signature, NULL, YES);
        if (signature == NULL) {
            return NULL;
        }
        convert_cif = PyObjCFFI_CIFForSignature(signature);
        Py_DECREF(signature);
        if (convert_cif == NULL) {
            return NULL;
        }
    }

    PyType_Slot opaque_slots[] = {
        {
            .slot  = Py_tp_dealloc,
            .pfunc = (void*)opaque_dealloc,
        },
        {
            .slot  = Py_tp_new,
            .pfunc = (void*)opaque_new,
        },
        {
            .slot  = Py_tp_members,
            .pfunc = (void*)opaque_members,
        },
        {
            .slot  = Py_tp_methods,
            .pfunc = (void*)opaque_methods,
        },
        {
            .slot  = Py_tp_traverse,
            .pfunc = (void*)opaque_traverse,
        },
        {
            /* Must be next to last */
            .slot  = Py_tp_doc,
            .pfunc = (void*)docstr,
        },

        {.slot = 0, .pfunc = NULL} /* Sentinel */
    };

    if (docstr == NULL) {
        /* Set slot with Py_tp_doc to NULL */
        PyType_Slot* docslot = opaque_slots + 5;
        if (docslot->slot != Py_tp_doc) {
            PyErr_SetString(PyExc_RuntimeError, "tp_doc not in expected slot");
            goto error_cleanup;
        }
        docslot->slot = 0;
    }

    dot = strchr(name, '.');
    if (dot == NULL) {
        if (strlen(name) > sizeof(buf) - sizeof("objc.")) {
            PyErr_SetString(PyExc_ValueError, "dotless name is too long");
            goto error_cleanup;
        }
        strcpy(buf, "objc.");
        strcpy(buf + 5, name);
    }

    PyType_Spec opaque_spec = {
        .name      = dot != NULL ? name : buf,
        .basicsize = sizeof(OpaquePointerObject),
        .itemsize  = 0,
        .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
        .slots     = opaque_slots,
    };

    newType = PyType_FromSpec(&opaque_spec);
    if (newType == NULL) {
        goto error_cleanup;
    }

    w = PyBytes_FromString(typestr);
    if (w == NULL) {
        goto error_cleanup;
    }

    if (PyObject_SetAttrString(newType, "__typestr__", w) == -1) {
        Py_CLEAR(newType);
        goto error_cleanup;
    }
    Py_CLEAR(w);

#ifdef HAVE_CLOSURE_POOL

#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) {
        cl_to_c = ffi_closure_alloc(sizeof(*cl_to_c), &codeloc);
    } else
#endif
    {
        cl_to_c = PyObjC_ffi_closure_alloc(sizeof(*cl_to_c), &codeloc);
    }
#else
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

    cl_to_c = ffi_closure_alloc(sizeof(*cl_to_c), &codeloc);

#pragma clang diagnostic pop
#endif
    if (cl_to_c == NULL) {
        goto error_cleanup;
    }

#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) {
        rv = ffi_prep_closure_loc(cl_to_c, convert_cif, opaque_to_c, newType, codeloc);
    } else
#endif
    {
#ifdef __arm64__
        rv = FFI_BAD_ABI;
#else
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        rv = ffi_prep_closure(cl_to_c, convert_cif, opaque_to_c, newType);

#pragma clang diagnostic pop
#endif
    }
    if (rv != FFI_OK) {
        PyErr_Format(PyExc_RuntimeError, "Cannot create FFI closure: %d", rv);
        goto error_cleanup;
    }
    Py_INCREF(newType); /* Store reference, hence INCREF */

    to_c = (PyObjCPointerWrapper_FromPythonFunc)codeloc;

#ifdef HAVE_CLOSURE_POOL
#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) {
        cl_from_c = ffi_closure_alloc(sizeof(*cl_from_c), &codeloc);
    } else
#endif
    {
        cl_from_c = PyObjC_ffi_closure_alloc(sizeof(*cl_from_c), &codeloc);
    }
#else
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
    cl_from_c = ffi_closure_alloc(sizeof(*cl_from_c), &codeloc);
#pragma clang diagnostic pop
#endif
    if (cl_from_c == NULL) {
        goto error_cleanup;
    }

#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) {
        rv = ffi_prep_closure_loc(cl_from_c, new_cif, opaque_from_c, newType, codeloc);
    } else
#endif
    {
#ifdef __arm64__
        rv = FFI_BAD_ABI;
#else
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        rv = ffi_prep_closure(cl_from_c, new_cif, opaque_from_c, newType);

#pragma clang diagnostic pop
#endif
    }
    if (rv != FFI_OK) {
        PyErr_Format(PyExc_RuntimeError, "Cannot create FFI closure: %d", rv);
        Py_XDECREF(newType);
        goto error_cleanup;
    }
    Py_INCREF(newType); /* Store reference, hence INCREF */

    from_c = (PyObjCPointerWrapper_ToPythonFunc)codeloc;

    r = PyObjCPointerWrapper_Register(name, typestr, from_c, to_c);
    if (r == -1) {
        Py_XDECREF(newType);
        Py_XDECREF(newType);
        goto error_cleanup;
    }

    return (PyObject*)newType;

error_cleanup:

#ifdef HAVE_CLOSURE_POOL
#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) {
        if (cl_to_c) {
            ffi_closure_free(cl_to_c);
        }

        if (cl_from_c) {
            ffi_closure_free(cl_from_c);
        }
    } else
#endif
    {
        if (cl_to_c) {
            PyObjC_ffi_closure_free(cl_to_c);
        }

        if (cl_from_c) {
            PyObjC_ffi_closure_free(cl_from_c);
        }
    }
#else
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
    if (cl_to_c) {
        ffi_closure_free(cl_to_c);
    }

    if (cl_from_c) {
        ffi_closure_free(cl_from_c);
    }
#pragma clang diagnostic pop
#endif
    Py_XDECREF(newType);
    Py_XDECREF(v);
    Py_XDECREF(w);
    return NULL;
}

NS_ASSUME_NONNULL_END
