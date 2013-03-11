/*
 * Implementation of support type for informal protocols.
 *
 * See the module DOCSTR for more information.
 */
#include "pyobjc.h"

PyDoc_STRVAR(proto_cls_doc,
"objc.informal_protocol(name, selector_list)\n"
"\n"
"This class can be used to specify which methods are supported by an informal\n"
"protocol. Instances of this type can by used while creating subclasses of \n"
"objective-C classes to automaticly specify method signatures et.al."
"");

typedef struct {
    PyObject_HEAD

    PyObject* name;
    PyObject* selectors;
} PyObjCInformalProtocol;


static PyObject* selToProtocolMapping = NULL;

static void
proto_dealloc(PyObject* object)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)object;
    /*
     * For some reason this code causes a crash, while it should
     * be the reverse of the code in proto_new.
     */
    Py_ssize_t len = PyTuple_Size(self->selectors);
    Py_ssize_t i;

    if (selToProtocolMapping) {
        for (i = 0; i < len; i++) {
            PyObjCSelector* tmp =
                (PyObjCSelector*)PyTuple_GET_ITEM(
                    self->selectors, i);

            PyDict_DelItemString(selToProtocolMapping,
                sel_getName(tmp->sel_selector));
        }
    }

    Py_CLEAR(self->name);
    Py_CLEAR(self->selectors);
    Py_TYPE(object)->tp_free(object);
}

static PyObject*
proto_repr(PyObject* object)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)object;
    PyObject* b = NULL;

    if (PyUnicode_Check(self->name)) {
        b = PyUnicode_AsEncodedString(self->name, NULL, NULL);

#if PY_MAJOR_VERSION == 2
    } else if (PyString_Check(self->name)) {
        b = self->name; Py_INCREF(b);
#endif

    } else {
        b = PyBytes_FromString("<null>");
    }

    if (b == NULL) {
        return NULL;
    }

    PyObject* r = PyText_FromFormat("<%s %s at %p>", Py_TYPE(self)->tp_name, PyBytes_AsString(b), (void*)self);
    Py_XDECREF(b);
    return r;
}

static PyObject*
proto_new(PyTypeObject* type __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", "selectors", NULL };

    PyObjCInformalProtocol* result;
    PyObject* name;
    PyObject* selectors;
    Py_ssize_t i, len;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO:informal_protocol",
            keywords, &name, &selectors)) {
        return NULL;
    }

    if (PyUnicode_Check(name)) {
        /* pass */

#if PY_MAJOR_VERSION == 2
    } else if (PyString_Check(name)) {
        /* pass */
#endif

    } else {
        PyErr_SetString(PyExc_TypeError,
            "Name must be a string");
        return NULL;
    }

    selectors = PySequence_Tuple(selectors);
    if (selectors == NULL) {
        return NULL;
    }

    result = (PyObjCInformalProtocol*)PyObject_New(PyObjCInformalProtocol, &PyObjCInformalProtocol_Type);
    if (result == NULL) {
        return NULL;
    }

    result->name = name;
    Py_INCREF(name);
    result->selectors = selectors;

    len = PyTuple_GET_SIZE(selectors);
    for (i = 0; i < len; i++) {
        if (!PyObjCSelector_Check(
                PyTuple_GET_ITEM(selectors, i))) {
            PyErr_Format(PyExc_TypeError,
                "Item %"PY_FORMAT_SIZE_T"d is not a selector", i);
            Py_DECREF(result);
            return NULL;
        }
    }

    if (selToProtocolMapping == NULL) {
        selToProtocolMapping = PyDict_New();
        if (selToProtocolMapping == NULL) {
            Py_DECREF(result);
            return NULL;
        }
    }

    for (i = 0; i < len; i++) {
        PyObjCSelector* tmp =
            (PyObjCSelector*)PyTuple_GET_ITEM(selectors, i);

        PyDict_SetItemString(selToProtocolMapping,
            (char*)sel_getName(tmp->sel_selector),
            (PyObject*)result);
    }

    return (PyObject*)result;
}

static int
proto_traverse(PyObject* _self, visitproc visit, void* arg)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)_self;
    Py_VISIT(self->name);
    Py_VISIT(self->selectors);
    return 0;
}

static PyMemberDef proto_members[] = {
    {
        "__name__",
        T_OBJECT,
        offsetof(PyObjCInformalProtocol, name),
        READONLY,
        NULL
    },
    {
        "selectors",
        T_OBJECT,
        offsetof(PyObjCInformalProtocol, selectors),
        READONLY,
        NULL
    },

    { 0, 0, 0, 0, 0 }
};

PyTypeObject PyObjCInformalProtocol_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.informal_protocol",
    .tp_basicsize   = sizeof(PyObjCInformalProtocol),
    .tp_itemsize    = 0,
    .tp_dealloc     = proto_dealloc,
    .tp_repr        = proto_repr,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = proto_cls_doc,
    .tp_traverse    = proto_traverse,
    .tp_members     = proto_members,
    .tp_new         = proto_new,
};

/*
 * Find information about a selector in the protocol.
 *
 * Return NULL if no information can be found, but does not set an
 * exception.
 */
PyObject*
PyObjCInformalProtocol_FindSelector(PyObject* obj, SEL selector, int isClassMethod)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;
    Py_ssize_t i, len;
    PyObject* cur;
    PyObject* seq;

    if (!PyObjCInformalProtocol_Check(obj)) {
        PyErr_Format(PyExc_TypeError,
            "First argument is not an 'objc.informal_protocol' "
            "but '%s'", Py_TYPE(obj)->tp_name);
        return 0;
    }

    seq = PySequence_Fast(self->selectors,"selector list not a sequence?");
    if (seq == NULL) {
        return 0;
    }

    len = PySequence_Fast_GET_SIZE(seq);
    for (i = 0; i < len; i++) {
        cur = PySequence_Fast_GET_ITEM(self->selectors, i);
        if (cur == NULL) {
            continue;
        }

        if (PyObjCSelector_Check(cur)) {
            int class_sel = (
                PyObjCSelector_GetFlags(cur)
                & PyObjCSelector_kCLASS_METHOD) != 0;

            if ((isClassMethod && !class_sel)
                    || (!isClassMethod && class_sel)) {
                continue;
            }

            if (sel_isEqual(PyObjCSelector_GetSelector(cur), selector)) {
                Py_DECREF(seq);
                return cur;
            }
        }
    }

    Py_DECREF(seq);
    return NULL;
}


/*
 * Verify that 'cls' conforms to the informal protocol
 */
int
PyObjCInformalProtocol_CheckClass(
    PyObject* obj, char* name, PyObject* super_class, PyObject* clsdict)
{
    PyObjCInformalProtocol* self = (PyObjCInformalProtocol*)obj;
    Py_ssize_t i, len;
    PyObject* cur;
    PyObject* seq;

    if (!PyObjCInformalProtocol_Check(obj)) {
        PyErr_Format(PyExc_TypeError,
            "First argument is not an 'objc.informal_protocol' "
            "but '%s'", Py_TYPE(obj)->tp_name);
        return 0;
    }

    if (!PyObjCClass_Check(super_class)) {
        PyErr_Format(PyExc_TypeError,
            "Third argument is not an 'objc.objc_class' but "
            "'%s'", Py_TYPE(super_class)->tp_name);
        return 0;
    }

    if (!PyDict_Check(clsdict)) {
        PyErr_Format(PyExc_TypeError,
            "Fourth argument is not a 'dict' but '%s'",
            Py_TYPE(clsdict)->tp_name);
        return 0;
    }

    seq = PySequence_Fast(self->selectors, "selector list not a sequence");
    if (seq == NULL) {
        return 0;
    }

    len = PySequence_Fast_GET_SIZE(seq);
    for (i = 0; i < len; i++) {
        SEL sel;
        PyObject* m;

        cur = PySequence_Fast_GET_ITEM(seq, i);
        if (cur == NULL) {
            continue;
        }

        if (!PyObjCSelector_Check(cur)) {
            continue;
        }

        sel = PyObjCSelector_GetSelector(cur);

        m = PyObjC_FindSELInDict(clsdict, sel);
        if (m == NULL) {
            m = PyObjCClass_FindSelector(super_class, sel, PyObjCSelector_IsClassMethod(cur));
        }

        if (m == NULL || !PyObjCSelector_Check(m)) {
            Py_XDECREF(m);
            if (PyObjCSelector_Required(cur)) {
                PyErr_Format(PyExc_TypeError,
                    "class %s does not fully implement "
                    "protocol %S: no implementation for %s",
                    name,
                    self->name,
                    sel_getName(sel));
                Py_DECREF(seq);
                return 0;

            } else {
                PyErr_Clear();
            }

        } else {
            if (!PyObjCRT_SignaturesEqual(PyObjCSelector_Signature(m),
                PyObjCSelector_Signature(cur)) != 0) {

                PyErr_Format(PyExc_TypeError,
                    "class %s does not correctly implement "
                    "protocol %S: "
                    "the signature for method %s is "
                    "%s instead of %s",
                    name,
                    self->name,
                    sel_getName(sel),
                    PyObjCSelector_Signature(m),
                    PyObjCSelector_Signature(cur)
                );

                Py_DECREF(seq);
                Py_DECREF(m);
                return 0;
            }
            Py_DECREF(m);
        }
    }
    Py_DECREF(seq);
    return 1;
}

PyObject*
PyObjCInformalProtocol_FindProtocol(SEL selector)
{
    PyObject* item;

    if (selToProtocolMapping == NULL) return NULL;

    item = PyDict_GetItemString(selToProtocolMapping, (char*)sel_getName(selector));
    if (item != NULL) {
        return item;
    }

    PyErr_Clear();
    return NULL;
}
