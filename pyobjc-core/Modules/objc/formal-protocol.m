/*
 * Implementation of support type for formal protocols.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

PyDoc_STRVAR(
    proto_cls_doc,
    "objc.formal_protocol(name, supers, selector_list)\n" CLINIC_SEP "\n"
    "This class is used to proxy Objective-C formal protocols, and can also be \n"
    "used to define new formal protocols.\n"
    "");

typedef struct {
    PyObject_HEAD

    Protocol* objc;
} PyObjCFormalProtocol;

PyObject* PyObjCFormalProtocol_Type;

static void
proto_dealloc(PyObject* object)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    PyObjC_UnregisterPythonProxy(self->objc, object);
    PyTypeObject* tp = Py_TYPE(object);
    tp->tp_free(object);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

static PyObject* _Nullable proto_repr(PyObject* object)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    const char*           name;

    name = protocol_getName(self->objc);
    if (name == NULL)   // LCOV_BR_EXCL_LINE
        name = "<nil>"; // LCOV_EXCL_LINE

    return PyUnicode_FromFormat("<%s %s at %p>", Py_TYPE(self)->tp_name, name,
                                (void*)self);
}

static PyObject* _Nullable proto_get__class__(PyObject* object
                                              __attribute__((__unused__)),
                                              void* closure __attribute__((__unused__)))
{
    return PyObjCClass_New([Protocol class]);
}

static PyObject* _Nullable proto_get__name__(PyObject* object,
                                             void* closure __attribute__((__unused__)))
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    const char*           name = protocol_getName(self->objc);

    if (name == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    return PyUnicode_FromString(name);
}

static PyObject* _Nullable proto_new(PyTypeObject* type __attribute__((__unused__)),
                                     PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", "supers", "selectors", NULL};

    char*      name;
    PyObject*  supers;
    PyObject*  selectors;
    Py_ssize_t i, len;

    PyObjCFormalProtocol* result = NULL;
    Protocol*             theProtocol;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "sOO:formal_protocol", keywords, &name,
                                     &supers, &selectors)) {
        return NULL;
    }

    if (supers != Py_None) {
        supers = PySequence_Fast(
            supers, "supers need to be None or a sequence of objc.formal_protocols");
        if (supers == NULL) {
            return NULL;
        }

        len = PySequence_Fast_GET_SIZE(supers);

        for (i = 0; i < len; i++) {
            PyObject* v = PySequence_Fast_GET_ITEM(supers, i);
            if (!PyObjCFormalProtocol_Check(v)) {
                Py_DECREF(supers);
                PyErr_SetString(
                    PyExc_TypeError,
                    "supers need to be None or a sequence of objc.formal_protocols");
                return NULL;
            }
        }

    } else {
        Py_INCREF(supers);
    }

    selectors = PySequence_Fast(
        selectors, "selectors need to be a sequence of objc.selector instances");
    if (selectors == NULL) {
        Py_DECREF(supers);
        return NULL;
    }

    len = PySequence_Fast_GET_SIZE(selectors);
    for (i = 0; i < len; i++) {
        PyObject* sel = PySequence_Fast_GET_ITEM(selectors, i);
        if (PyTuple_Check(sel) && PyTuple_Size(sel) == 2) {
            /* Support for JSExportAs requires adding a tuple of two items
             * to the list of selectors.
             */
            if (!PyObjCSelector_Check(PyTuple_GET_ITEM(sel, 0))) {
                PyErr_SetString(PyExc_TypeError,
                                "Selectors is not a list of objc.selector instances");
                Py_DECREF(supers);
                return NULL;
            }
            if (!PyObjCSelector_Check(PyTuple_GET_ITEM(sel, 1))) {
                PyErr_SetString(PyExc_TypeError,
                                "Selectors is not a list of objc.selector instances");
                Py_DECREF(supers);
                return NULL;
            }

        } else if (!PyObjCSelector_Check(sel)) {
            PyErr_SetString(PyExc_TypeError,
                            "Selectors is not a list of objc.selector instances");
            Py_DECREF(supers);
            return NULL;
        }
    }

    theProtocol = objc_allocateProtocol(name);
    if (theProtocol == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        goto error;
        // LCOV_EXCL_STOP
    }

    if (supers != Py_None) {
        len = PySequence_Fast_GET_SIZE(supers);
        for (i = 0; i < len; i++) {
            PyObject* v = PySequence_Fast_GET_ITEM(supers, i);
            Protocol* p = PyObjCFormalProtocol_GetProtocol(v);
            if (unlikely(p == nil)) { // LCOV_BR_EXCL_LINE
                /* Should never happen because we've already checked that 'v'
                 *  is a formal protocol object.
                 */
                goto error; // LCOV_EXCL_LINE
            }
            protocol_addProtocol(theProtocol, p);
        }
    }

    len = PySequence_Fast_GET_SIZE(selectors);
    for (i = 0; i < len; i++) {
        PyObject* sel = PySequence_Fast_GET_ITEM(selectors, i);

        if (PyTuple_Check(sel)) {
            for (i = 0; i < PyTuple_GET_SIZE(sel); i++) {
                SEL         theSel = PyObjCSelector_GetSelector(PyTuple_GET_ITEM(sel, i));
                const char* theSignature =
                    PyObjCSelector_GetNativeSignature(PyTuple_GET_ITEM(sel, i));

                if (unlikely(theSignature == NULL)) { // LCOV_BR_EXCL_LINE
                    /* Should never happen, field cannot be NULL */
                    goto error; // LCOV_EXCL_LINE
                }

                protocol_addMethodDescription(
                    theProtocol, theSel, theSignature,
                    !!PyObjCSelector_Required(PyTuple_GET_ITEM(sel, i)),
                    PyObjCSelector_IsClassMethod(PyTuple_GET_ITEM(sel, i)) ? NO : YES);
            }

        } else {
            SEL         theSel       = PyObjCSelector_GetSelector(sel);
            const char* theSignature = PyObjCSelector_GetNativeSignature(sel);

            if (unlikely(theSignature == NULL)) { // LCOV_BR_EXCL_LINE
                /* Should never happen, field cannot be NULL */
                goto error; // LCOV_EXCL_LINE
            }

            protocol_addMethodDescription(theProtocol, theSel, theSignature,
                                          !!PyObjCSelector_Required(sel),
                                          PyObjCSelector_IsClassMethod(sel) ? NO : YES);
        }
    }
    objc_registerProtocol(theProtocol);

    result = (PyObjCFormalProtocol*)PyObject_New(
        PyObjCFormalProtocol, (PyTypeObject*)PyObjCFormalProtocol_Type);
    Py_DECREF(selectors);
    Py_DECREF(supers);

    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    result->objc = theProtocol;
    if (PyObjC_RegisterPythonProxy( // LCOV_BR_EXCL_LINE
            result->objc, (PyObject*)result)
        < 0) {
        // LCOV_EXCL_START
        Py_DECREF(result);
        goto error;
        // LCOV_EXCL_STOP
    }
    return (PyObject*)result;

error:
    // LCOV_EXCL_START
    Py_DECREF(selectors);
    Py_DECREF(supers);

    return NULL;
    // LCOV_EXCL_STOP
}

static PyObject* _Nullable proto_name(PyObject* object)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    const char*           name = protocol_getName(self->objc);

    if (name == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    return PyUnicode_FromString(name);
}

static PyObject* _Nullable proto_conformsTo_(PyObject* object, PyObject* _Nullable args)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    PyObject*             protocol;
    Protocol*             objc_protocol;

    if (!PyArg_ParseTuple(args, "O!", PyObjCFormalProtocol_Type, &protocol)) {
        return NULL;
    }

    objc_protocol = PyObjCFormalProtocol_GetProtocol(protocol);
    if (objc_protocol == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;             // LCOV_EXCL_LINE
    }

    if (protocol_conformsToProtocol(self->objc, objc_protocol)) {
        Py_INCREF(Py_True);
        return Py_True;
    } else {
        Py_INCREF(Py_False);
        return Py_False;
    }
}

static int
append_method_list(PyObject* lst, Protocol* protocol, BOOL isRequired, BOOL isInstance)
{
    struct objc_method_description* methods;
    unsigned int                    method_count, i;

    methods = protocol_copyMethodDescriptionList(protocol, isRequired, isInstance,
                                                 &method_count);
    if (!methods) {
        return 0;
    }

    for (i = 0; i < method_count; i++) {
        char buf[512];
        PyObjCRT_SimplifySignature(methods[i].types, buf, sizeof(buf));
        PyObject* item =
            Py_BuildValue("{sysysO}", "selector", sel_getName(methods[i].name), "typestr",
                          buf, "required", isRequired ? Py_True : Py_False);
        if (item == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            free(methods);
            return -1;
            // LCOV_EXCL_STOP
        }
        if (PyList_Append(lst, item) < 0) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(item);
            free(methods);
            return -1;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(item);
    } // LCOV_BR_EXCL_LINE: always non-empty

    free(methods);
    return 0;
}

static PyObject* _Nullable instanceMethods(PyObject* object)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    int                   r;

    PyObject* result = PyList_New(0);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    r = append_method_list(result, self->objc, YES, YES);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    r = append_method_list(result, self->objc, NO, YES);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    return result;
}

static PyObject* _Nullable classMethods(PyObject* object)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    int                   r;

    PyObject* result = PyList_New(0);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    r = append_method_list(result, self->objc, YES, NO);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    r = append_method_list(result, self->objc, NO, NO);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    return result;
}

static PyObject* _Nullable descriptionForInstanceMethod_(PyObject* object, PyObject* sel)
{
    PyObjCFormalProtocol*          self      = (PyObjCFormalProtocol*)object;
    SEL                            aSelector = NULL;
    struct objc_method_description descr;

    if (depythonify_c_value(@encode(SEL), sel, &aSelector) == -1)
        return NULL;

    descr = protocol_getMethodDescription(self->objc, aSelector, YES, YES);
    if (descr.name == NULL) {
        descr = protocol_getMethodDescription(self->objc, aSelector, NO, YES);
    }

    if (descr.name == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    } else {
        char buf[512];
        PyObjCRT_SimplifySignature(descr.types, buf, sizeof(buf));
        return Py_BuildValue("(yy)", sel_getName(descr.name), buf);
    }
}

static PyObject* _Nullable descriptionForClassMethod_(PyObject* object, PyObject* sel)
{
    PyObjCFormalProtocol*          self      = (PyObjCFormalProtocol*)object;
    SEL                            aSelector = NULL;
    struct objc_method_description descr;

    if (depythonify_c_value(@encode(SEL), sel, &aSelector) == -1)
        return NULL;

    descr = protocol_getMethodDescription(self->objc, aSelector, YES, NO);
    if (descr.name == NULL) {
        descr = protocol_getMethodDescription(self->objc, aSelector, NO, NO);
    }
    if (descr.name == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    } else {
        char buf[256];
        PyObjCRT_SimplifySignature(descr.types, buf, sizeof(buf));
        return Py_BuildValue("(yy)", sel_getName(descr.name), buf);
    }
}

static PyMethodDef proto_methods[] = {
    {
        .ml_name  = "name",
        .ml_meth  = (PyCFunction)proto_name,
        .ml_flags = METH_NOARGS,
        .ml_doc   = "name()\n" CLINIC_SEP "\nReturn the  protocol name",
    },
    {.ml_name  = "conformsTo_",
     .ml_meth  = (PyCFunction)proto_conformsTo_,
     .ml_flags = METH_VARARGS,
     .ml_doc   = "conformsTo_(other)\n" CLINIC_SEP "\n"
                 "Does this protocol conform to another protocol"},
    {.ml_name  = "descriptionForInstanceMethod_",
     .ml_meth  = (PyCFunction)descriptionForInstanceMethod_,
     .ml_flags = METH_O,
     .ml_doc   = "descriptionForInstanceMethod_(selector)\n" CLINIC_SEP
               "\nDescription for an instance method in the protocol"},
    {.ml_name  = "descriptionForClassMethod_",
     .ml_meth  = (PyCFunction)descriptionForClassMethod_,
     .ml_flags = METH_O,
     .ml_doc   = "descriptionForClassMethod_(selector)\n" CLINIC_SEP
               "\nDescription for a class method in the protocol"},
    {.ml_name  = "instanceMethods",
     .ml_meth  = (PyCFunction)instanceMethods,
     .ml_flags = METH_NOARGS,
     .ml_doc =
         "instanceMethods()\n" CLINIC_SEP "\nList of instance methods in this protocol"},
    {.ml_name  = "classMethods",
     .ml_meth  = (PyCFunction)classMethods,
     .ml_flags = METH_NOARGS,
     .ml_doc = "classMethods()\n" CLINIC_SEP "\nList of class methods in this protocol"},
    {
        .ml_name = NULL /* SENTINEL */
    }};

static PyGetSetDef proto_getset[] = {{
                                         .name = "__class__",
                                         .get  = (getter)proto_get__class__,
                                     },
                                     {
                                         .name = "__name__",
                                         .get  = (getter)proto_get__name__,
                                     },
                                     {
                                         .name = NULL /* SENTINEL */
                                     }};

static PyType_Slot proto_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&proto_dealloc},
    {.slot = Py_tp_repr, .pfunc = (void*)&proto_repr},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&proto_cls_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&proto_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&proto_getset},
    {.slot = Py_tp_new, .pfunc = (void*)&proto_new},
    {0, NULL} /* sentinel */
};

static PyType_Spec proto_spec = {
    .name      = "objc.formal_protocol",
    .basicsize = sizeof(PyObjCFormalProtocol),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = proto_slots,
};

PyObject* _Nullable PyObjCFormalProtocol_ForProtocol(Protocol* protocol)
{
    PyObjCFormalProtocol* result;

    PyObjC_Assert(protocol != NULL, NULL);

    result = (PyObjCFormalProtocol*)PyObject_New(
        PyObjCFormalProtocol, (PyTypeObject*)PyObjCFormalProtocol_Type);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    result->objc = protocol;
    PyObjC_RegisterPythonProxy(result->objc, (PyObject*)result);
    return (PyObject*)result;
}

Protocol* _Nullable PyObjCFormalProtocol_GetProtocol(PyObject* object)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;

    PyObjC_Assert(PyObjCFormalProtocol_Check(self), NULL);

    return self->objc;
}

int
PyObjCFormalProtocol_Setup(PyObject* module)
{
    PyObjCFormalProtocol_Type = PyType_FromSpec(&proto_spec);
    if (PyObjCFormalProtocol_Type == NULL) { // LCOV_BR_EXCL_LINE
        return -1;                           // LCOV_EXCL_LINE
    }

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "formal_protocol", PyObjCFormalProtocol_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCFormalProtocol_Type);

    return 0;
}

NS_ASSUME_NONNULL_END
