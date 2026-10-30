#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable obj_new(PyTypeObject* type,
                                   PyObject* _Nullable args __attribute__((__unused__)),
                                   PyObject* _Nullable kwds __attribute__((__unused__)))
{
    return PyErr_Format(PyExc_TypeError, "Cannot create instances of %s", type->tp_name);
}

static PyObject* _Nullable obj_richcompare(PyObject* a, PyObject* b, int op)
{
    if (op == Py_EQ || op == Py_NE) {
        if (PyObjCBoundSelector_Check(a) && PyObjCBoundSelector_Check(b)) {

            PyObjCBoundSelector* sel_a = (PyObjCBoundSelector*)a;
            PyObjCBoundSelector* sel_b = (PyObjCBoundSelector*)b;
            int                  same  = 1;
            int                  r;

            assert(sel_a->sel_self != NULL);
            assert(sel_a->sel_selector != NULL);

            if (sel_a->sel_self != sel_b->sel_self)
                same = 0;

            r = PyObject_RichCompareBool(sel_a->sel_selector, sel_b->sel_selector, Py_EQ);
            if (r == -1) {
                return NULL;
            } else if (r == 0) {
                same = 0;
            }

            if ((op == Py_EQ && !same) || (op == Py_NE && same)) {
                Py_RETURN_FALSE;
            } else {
                Py_RETURN_TRUE;
            }

        } else {
            if (op == Py_EQ) {
                Py_RETURN_FALSE;

            } else {
                Py_RETURN_TRUE;
            }
        }

    } else {
        Py_RETURN_NOTIMPLEMENTED;
    }
}

static Py_hash_t
obj_hash(PyObject* o)
{
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)o;
    Py_hash_t            h    = 0;

    if (self->sel_self) {
        h ^= PyObject_Hash(self->sel_self);
    }
    h ^= PyObject_Hash(self->sel_selector);

    return h == -1 ? -2 : h;
}

static void
obj_dealloc(PyObject* _self)
{
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;

    PyObject_GC_UnTrack(_self);

    /* Don't use CLEAR because the invariant
     * is that the attributes are not NULL
     */
    Py_DECREF(self->sel_self);
    self->sel_self = (PyObject* _Nonnull)NULL;
    Py_DECREF(self->sel_selector);
    self->sel_selector = (PyObject* _Nonnull)NULL;

    PyObject_GC_Del(_self);
}

static int
obj_clear(PyObject* _self)
{
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;

    PyObject_GC_UnTrack(_self);

    /* Set the "cleared" fields to Py_None, that
     * way the invariant that fields are non-null
     * is maintained.
     *
     * 'None' cannot be part of a reference cycle.
     */
    PyObject* tmp;
    tmp            = self->sel_self;
    self->sel_self = Py_None;
    Py_INCREF(Py_None);
    Py_DECREF(tmp);

    tmp                = self->sel_selector;
    self->sel_selector = Py_None;
    Py_INCREF(Py_None);
    Py_DECREF(tmp);
    return 0;
}

static int
obj_traverse(PyObject* _self, visitproc visit, void* _Nullable arg)
{
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;
    Py_VISIT(self->sel_self);
    Py_VISIT(self->sel_selector);
    return 0;
}

static PyObject* _Nullable forward_getter(PyObject* _self, void* closure)
{
    assert(closure != NULL);

    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;
    return PyObject_GetAttrString(self->sel_selector, (const char*)closure);
}

static PyObject*
obj_get_self(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;
    Py_INCREF(self->sel_self);
    return self->sel_self;
}

static PyObject*
obj_get_func(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;
    Py_INCREF(self->sel_selector);
    return self->sel_selector;
}

static PyGetSetDef obj_getset[] = {
    {.name    = "isHidden",
     .get     = forward_getter,
     .doc     = "If True the method is not directly accessible as an object attribute",
     .closure = "isHidden"},
    {.name    = "isRequired",
     .get     = forward_getter,
     .doc     = "True if this is a required method, False otherwise",
     .closure = "isRequired"},
    {.name    = "isClassMethod",
     .get     = forward_getter,
     .doc     = "True if this is a class method, False otherwise",
     .closure = "isClassMethod"},
    {.name    = "definingClass",
     .get     = forward_getter,
     .doc     = "Objective-C Class that defines the method",
     .closure = "definingClass"},
    {.name    = "__objclass__",
     .get     = forward_getter,
     .doc     = "Objective-C Class that defines the method",
     .closure = "__objclass__"},
    {.name    = "signature",
     .get     = forward_getter,
     .doc     = "Objective-C signature for the method",
     .closure = "signature"},
    {.name    = "native_signature",
     .get     = forward_getter,
     .doc     = "original Objective-C signature for the method",
     .closure = "native_signature"},
    {.name    = "selector",
     .get     = forward_getter,
     .doc     = "Objective-C name for the method",
     .closure = "selector"},
    {.name    = "__name__",
     .get     = forward_getter,
     .doc     = "Name for the method",
     .closure = "__name__"},
    {.name    = "__doc__",
     .get     = forward_getter,
     .doc     = "documentation string for a method",
     .closure = "__doc__"},
    {.name    = "__signature__",
     .get     = forward_getter,
     .doc     = "inspect.Signature for a method",
     .closure = "__signature__"},
    {.name = "callable",
     .get  = forward_getter,
     .doc = "Returns the python 'function' that implements this method (for bound python "
            "selectors).",
     .closure = "callable"},

    {
        .name = "self",
        .get  = obj_get_self,
        .doc  = "the bound 'self'",
    },
    {
        .name = "__self__",
        .get  = obj_get_self,
        .doc  = "the bound 'self'",
    },
    {
        .name = "__func__",
        .get  = obj_get_func,
        .doc  = "the selector value that was bound to 'self' ",
    },
    {
        .name = NULL /* SENTINEL */
    }};

PyDoc_STRVAR(obj_metadata_doc,
             "__metadata__()\n" CLINIC_SEP
             "\nReturn a dict that describes the metadata for this method, including "
             "metadata for the 2 hidden ObjC parameters (self and _sel) ");
static PyObject*
obj_metadata(PyObject* _self)
{
    PyObjCBoundSelector* self   = (PyObjCBoundSelector*)_self;
    PyObject*            args[] = {NULL, self->sel_selector};

    return PyObject_VectorcallMethod(PyObjCNM___metadata__, args + 1,
                                     1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
}

static PyMethodDef obj_methods[] = {{.ml_name  = "__metadata__",
                                     .ml_meth  = (PyCFunction)obj_metadata,
                                     .ml_flags = METH_NOARGS,
                                     .ml_doc   = obj_metadata_doc},
                                    {
                                        .ml_name = NULL /* SENTINEL */
                                    }};

static PyObject* _Nullable obj_vectorcall(PyObject* _self,
                                          PyObject* _Nonnull const* _Nonnull args,
                                          size_t nargsf, PyObject* _Nullable kwnames)
{
    /* Forward the call to the real selector, inserting 'self'.
     *
     * Note that performance is not too critical here, most method
     * calls will never use a bound selector object.
     */
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;

    if (nargsf & PY_VECTORCALL_ARGUMENTS_OFFSET) {
        ((PyObject**)args)[-1] = self->sel_self;
        return PyObject_Vectorcall(self->sel_selector, args - 1,
                                   PyVectorcall_NARGS(nargsf) + 1, kwnames);
    } else {
        PyObject** new_args =
            PyObject_Malloc(sizeof(PyObject*) * (PyVectorcall_NARGS(nargsf) + 1));
        if (new_args == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            return NULL;
            // LCOV_EXCL_STOP
        }

        new_args[0] = self->sel_self;
        memcpy(new_args + 1, args, sizeof(PyObject*) * PyVectorcall_NARGS(nargsf));
        PyObject* result = PyObject_Vectorcall(self->sel_selector, new_args,
                                               PyVectorcall_NARGS(nargsf) + 1, kwnames);

        PyMem_Free(new_args);
        return result;
    }
}

static PyObject*
obj_repr(PyObject* _self)
{
    PyObjCBoundSelector* self = (PyObjCBoundSelector*)_self;
    return PyUnicode_FromFormat("<objc.bound_selector self=%R selector=%R>",
                                self->sel_self, self->sel_selector);
}

PyObject* _Nullable PyObjCBoundSelector_New(PyObject* self, PyObjCSelector* selector)
{
    assert(self != NULL);
    assert(selector != NULL);

    PyObjCBoundSelector* result =
        PyObject_GC_New(PyObjCBoundSelector, (PyTypeObject*)PyObjCBoundSelector_Type);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    result->sel_self       = self;
    result->sel_selector   = (PyObject*)selector;
    result->sel_vectorcall = obj_vectorcall;

    Py_INCREF(self);
    Py_INCREF(selector);

    PyObject_GC_Track((PyObject*)result);

    return (PyObject*)result;
}

PyObject* PyObjCBoundSelector_Type;

static PyMemberDef obj_members[] = {
    {
        .name   = "__vectorcalloffset__",
        .type   = T_PYSSIZET,
        .offset = offsetof(PyObjCBoundSelector, sel_vectorcall),
        .flags  = READONLY,
    },
    {
        .name = NULL /* SENTINEL */
    }};

static PyType_Slot obj_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&obj_dealloc},
    {.slot = Py_tp_clear, .pfunc = (void*)&obj_clear},
    {.slot = Py_tp_traverse, .pfunc = (void*)&obj_traverse},
    {.slot = Py_tp_repr, .pfunc = (void*)&obj_repr},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    //{.slot = Py_tp_doc, .pfunc = (void*)&obj_doc},
    {.slot = Py_tp_getset, .pfunc = (void*)&obj_getset},
    {.slot = Py_tp_members, .pfunc = (void*)&obj_members},
    {.slot = Py_tp_methods, .pfunc = (void*)&obj_methods},
    {.slot = Py_tp_call, .pfunc = (void*)&PyVectorcall_Call},
    {.slot = Py_tp_hash, .pfunc = (void*)&obj_hash},
    {.slot = Py_tp_richcompare, .pfunc = (void*)&obj_richcompare},
    {.slot = Py_tp_new, .pfunc = (void*)&obj_new},
    {0, NULL} /* sentinel */
};

static PyType_Spec obj_spec = {
    .name      = "objc.bound_selector",
    .basicsize = sizeof(PyObjCBoundSelector),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
                 | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_VECTORCALL | Py_TPFLAGS_HAVE_GC,
    .slots     = obj_slots,
};

int
PyObjCBoundSelector_Setup(PyObject* module)
{
    PyObject* tmp = PyType_FromSpecWithBases(&obj_spec, PyObjCSelector_Type);
    if (unlikely(tmp == NULL)) { // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE
    }
    PyObjCBoundSelector_Type = tmp;

    if (unlikely(PyModule_AddObject( // LCOV_BR_EXCL_LINE
                     module, "bound_selector", PyObjCBoundSelector_Type)
                 == -1)) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCBoundSelector_Type);
    return 0;
}

NS_ASSUME_NONNULL_END
