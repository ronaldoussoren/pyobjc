/*
 * Implementation of support type for informal protocols.
 *
 * See the module DOCSTR for more information.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

PyDoc_STRVAR(
    proto_cls_doc,
    "objc.informal_protocol(name, selector_list)\n" CLINIC_SEP "\n"
    "This class can be used to specify which methods are supported by an informal\n"
    "protocol. Instances of this type can by used while creating subclasses of \n"
    "objective-C classes to automatically specify method signatures et.al."
    "");

typedef struct {
    PyObject_HEAD

    /*  XXX: _Nullable because of dealloc impl, can this be avoided? */
    PyObject* name;
    PyObject* selectors;
} PyObjCInformalProtocol;

static PyObject* selToProtocolMapping = NULL;

/*
 * XXX: This type will never be deallocated once fully created:
 *      during creation the type is added as a value in
 *      selToProtocolMapping and hence the refcount will never
 *      drop to 0.
 */
static void
proto_dealloc(PyObject* object)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)object;
    Py_ssize_t              len  = PyTuple_GET_SIZE(self->selectors);
    Py_ssize_t              i;

    if (selToProtocolMapping) { // LCOV_BR_EXCL_LINE
        for (i = 0; i < len; i++) {
            PyObject*       cur;
            int             r;
            PyObjCSelector* tmp = (PyObjCSelector*)PyTuple_GET_ITEM(self->selectors, i);

            /* Remove method from the selector to protocol mapping,
             * but only if this protocol is registered for the selector.
             */
            cur = PyDict_GetItemStringWithError(selToProtocolMapping,
                                                (char*)sel_getName(tmp->sel_selector));
            if (cur == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                PyErr_WriteUnraisable(NULL);       // LCOV_EXCL_LINE
            } else if (cur == (PyObject*)self) {
                r = PyDict_DelItemString(selToProtocolMapping,
                                         sel_getName(tmp->sel_selector));
                if (r == -1) {                   // LCOV_BR_EXCL_LINE
                    PyErr_WriteUnraisable(NULL); // LCOV_EXCL_LINE
                }
            }
        }
    }
    PyObject_GC_UnTrack(object);
    Py_XDECREF(self->name);
    Py_XDECREF(self->selectors);
    PyObject_GC_Del(object);
}

static PyObject* _Nullable proto_repr(PyObject* object)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)object;

    return PyUnicode_FromFormat("<%s %R at %p>", Py_TYPE(self)->tp_name, self->name,
                                (void*)self);
}

static PyObject* _Nullable proto_new(PyTypeObject* type __attribute__((__unused__)),
                                     PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", "selectors", NULL};

    PyObjCInformalProtocol* result;
    PyObject*               name;
    PyObject*               selectors;
    Py_ssize_t              i, len;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "UO:informal_protocol", keywords, &name,
                                     &selectors)) {
        return NULL;
    }

    /* XXX: Use PySequence_Fast? */
    selectors = PySequence_Tuple(selectors);
    if (selectors == NULL) {
        return NULL;
    }

    len = PyTuple_GET_SIZE(selectors);
    for (i = 0; i < len; i++) {
        if (!PyObjCSelector_Check(PyTuple_GET_ITEM(selectors, i))) {
            PyErr_Format(PyExc_TypeError, "Item %" PY_FORMAT_SIZE_T "d is not a selector",
                         i);
            Py_DECREF(selectors);
            return NULL;
        }
    }

    result = (PyObjCInformalProtocol*)PyObject_GC_New(PyObjCInformalProtocol,
                                                      &PyObjCInformalProtocol_Type);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(selectors);
        return NULL;
        // LCOV_EXCL_STOP
    }

    result->name = name;
    Py_INCREF(name);
    result->selectors = selectors;
    PyObject_GC_Track((PyObject*)result);

    if (selToProtocolMapping == NULL) {
        selToProtocolMapping = PyDict_New();
        if (selToProtocolMapping == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    for (i = 0; i < len; i++) {
        PyObjCSelector* tmp = (PyObjCSelector*)PyTuple_GET_ITEM(selectors, i);

        if (PyDict_SetItemString( // LCOV_BR_EXL_LINE
                selToProtocolMapping, (char*)sel_getName(tmp->sel_selector),
                (PyObject*)result)
            == -1) {
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    return (PyObject*)result;
}

static int
proto_traverse(PyObject* _self, visitproc visit, void* _Nullable arg)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)_self;
    Py_VISIT(self->name);
    Py_VISIT(self->selectors);
    return 0;
}

static PyMemberDef proto_members[] = {
    {
        .name   = "__name__",
        .type   = T_OBJECT,
        .offset = offsetof(PyObjCInformalProtocol, name),
        .flags  = READONLY,
    },
    {
        .name   = "selectors",
        .type   = T_OBJECT,
        .offset = offsetof(PyObjCInformalProtocol, selectors),
        .flags  = READONLY,
    },
    {
        .name = NULL /* SENTINEL */
    }};

PyTypeObject PyObjCInformalProtocol_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.informal_protocol",
    .tp_basicsize                                  = sizeof(PyObjCInformalProtocol),
    .tp_itemsize                                   = 0,
    .tp_dealloc                                    = proto_dealloc,
    .tp_repr                                       = proto_repr,
    .tp_getattro                                   = PyObject_GenericGetAttr,
    .tp_flags    = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    .tp_doc      = proto_cls_doc,
    .tp_traverse = proto_traverse,
    .tp_members  = proto_members,
    .tp_new      = proto_new,
};

/*
 * Find information about a selector in the protocol.
 *
 * Return NULL if no information can be found, but does not set an
 * exception.
 */
PyObject* _Nullable PyObjCInformalProtocol_FindSelector(PyObject* obj, SEL selector,
                                                        int isClassMethod)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;
    Py_ssize_t              i, len;
    PyObject*               cur;

    PyObjC_Assert(PyObjCInformalProtocol_Check(obj), NULL);
    PyObjC_Assert(PyTuple_Check(self->selectors), NULL);

    len = PyTuple_GET_SIZE(self->selectors);
    for (i = 0; i < len; i++) {
        cur = PyTuple_GET_ITEM(self->selectors, i);
        if (cur == NULL) { // LCOV_BR_EXCL_LINE
            continue;      // LCOV_EXCL_LINE
        }

        if (PyObjCSelector_Check(cur)) {
            int class_sel =
                (PyObjCSelector_GetFlags(cur) & PyObjCSelector_kCLASS_METHOD) != 0;

            if ((isClassMethod && !class_sel) || (!isClassMethod && class_sel)) {
                continue;
            }

            if (sel_isEqual(PyObjCSelector_GetSelector(cur), selector)) {
                return cur;
            }
        }
    }

    return NULL;
}

/*
 * Verify that 'cls' conforms to the informal protocol
 */
int
PyObjCInformalProtocol_CheckClass(PyObject* obj, char* name, PyObject* super_class,
                                  PyObject* clsdict)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;
    Py_ssize_t              i, len;
    PyObject*               cur;

    PyObjC_Assert(PyObjCInformalProtocol_Check(obj), -1);
    PyObjC_Assert(PyObjCClass_Check(super_class), -1);
    PyObjC_Assert(PyDict_Check(clsdict), -1);
    PyObjC_Assert(PyTuple_Check(self->selectors), -1);

    len = PyTuple_GET_SIZE(self->selectors);
    for (i = 0; i < len; i++) {
        SEL       sel;
        PyObject* m;

        cur = PyTuple_GET_ITEM(self->selectors, i);
        if (cur == NULL) { // LCOV_BR_EXCL_LINE
            continue;      // LCOV_EXCL_LINE
        }

        PyObjC_Assert(PyObjCSelector_Check(cur), -1);

        sel = PyObjCSelector_GetSelector(cur);

        m = PyObjC_FindSELInDict(clsdict, sel);
        if (m == NULL) {
            m = PyObjCClass_FindSelector(super_class, sel,
                                         PyObjCSelector_IsClassMethod(cur));
        }

        if (m == NULL || !PyObjCSelector_Check(m)) {
            Py_XDECREF(m);
            if (PyObjCSelector_Required(cur)) {
                PyErr_Format(PyExc_TypeError,
                             "class %s does not fully implement "
                             "protocol %S: no implementation for %s",
                             name, self->name, sel_getName(sel));
                return -1;

            } else {
                PyErr_Clear();
            }

        } else {
            const char* l_sig = PyObjCSelector_Signature(m);
            const char* r_sig = PyObjCSelector_Signature(cur);
            if (l_sig == NULL || r_sig == NULL) {
                return -1;
            }
            if (!PyObjCRT_SignaturesEqual(l_sig, r_sig)) {

                PyErr_Format(PyExc_TypeError,
                             "class %s does not correctly implement "
                             "protocol %S: "
                             "the signature for method %s is "
                             "%s instead of %s",
                             name, self->name, sel_getName(sel),
                             PyObjCSelector_Signature(m), PyObjCSelector_Signature(cur));

                Py_DECREF(m);
                return -1;
            }
            Py_DECREF(m);
        }
    }
    return 0;
}

PyObject* _Nullable PyObjCInformalProtocol_FindProtocol(SEL selector)
{
    if (selToProtocolMapping == NULL)
        return NULL;

    return PyDict_GetItemStringWithError(selToProtocolMapping,
                                         (char*)sel_getName(selector));
}

NS_ASSUME_NONNULL_END
