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

static void
proto_dealloc(PyObject* object)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)object;
    PyObjC_UnregisterPythonProxy(self->objc, object);
    Py_TYPE(object)->tp_free(object);
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
        if (!PyObjCSelector_Check(sel)) {
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
        PyObject*   sel          = PySequence_Fast_GET_ITEM(selectors, i);
        SEL         theSel       = PyObjCSelector_GetSelector(sel);
        const char* theSignature = PyObjCSelector_GetNativeSignature(sel);

        if (unlikely(theSignature == NULL)) { // LCOV_BR_EXCL_LINE
            /* Should never happen, field cannot be NULL */
            goto error; // LCOV_EXCL_LINE
        }

        protocol_addMethodDescription(theProtocol, theSel, theSignature,
                                      (BOOL)PyObjCSelector_Required(sel),
                                      PyObjCSelector_IsClassMethod(sel) ? NO : YES);

#ifndef protocol_getMethodDescription
        /* See issue #17 */
        struct objc_method_description descr = protocol_getMethodDescription(
            theProtocol, theSel, (BOOL)PyObjCSelector_Required(sel),
            PyObjCSelector_IsClassMethod(sel) ? NO : YES);
        if (descr.name == NULL) {
            PyErr_Format(
                PyExc_RuntimeError,
                "Cannot find '%s' in newly constructed protocol (before registration)",
                sel_getName(theSel));
            goto error;
        }
#endif
    }
    objc_registerProtocol(theProtocol);

#ifndef protocol_getMethodDescription
    /* See issue #17 */
    for (i = 0; i < len; i++) {
        PyObject* sel    = PySequence_Fast_GET_ITEM(selectors, i);
        SEL       theSel = PyObjCSelector_GetSelector(sel);

        struct objc_method_description descr = protocol_getMethodDescription(
            theProtocol, theSel, (BOOL)PyObjCSelector_Required(sel),
            PyObjCSelector_IsClassMethod(sel) ? NO : YES);
        if (descr.name == NULL) {
            PyErr_Format(
                PyExc_RuntimeError,
                "Cannot find '%s' in newly constructed protocol (after registration)",
                sel_getName(theSel));
            goto error;
        }
    }
#endif

    result = (PyObjCFormalProtocol*)PyObject_New(PyObjCFormalProtocol,
                                                 &PyObjCFormalProtocol_Type);
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

    if (!PyArg_ParseTuple(args, "O!", &PyObjCFormalProtocol_Type, &protocol)) {
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

PyTypeObject PyObjCFormalProtocol_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.formal_protocol",
    .tp_basicsize                                  = sizeof(PyObjCFormalProtocol),
    .tp_itemsize                                   = 0,
    .tp_dealloc                                    = proto_dealloc,
    .tp_repr                                       = proto_repr,
    .tp_getattro                                   = PyObject_GenericGetAttr,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
    .tp_doc                                        = proto_cls_doc,
    .tp_methods                                    = proto_methods,
    .tp_getset                                     = proto_getset,
    .tp_new                                        = proto_new,
};

/*
 * Find information about a selector in the protocol.
 *
 * Return NULL if no information can be found, but does not set an
 * exception.
 */
const char* _Nullable PyObjCFormalProtocol_FindSelectorSignature(PyObject* object,
                                                                 SEL       selector,
                                                                 int       isClassMethod)
{
    PyObjCFormalProtocol*          self = (PyObjCFormalProtocol*)object;
    struct objc_method_description descr;

    descr = protocol_getMethodDescription(self->objc, selector, YES, !isClassMethod);
    if (descr.name != NULL) {
        return descr.types;
    }

    descr = protocol_getMethodDescription(self->objc, selector, NO, !isClassMethod);
    if (descr.name != NULL) {
        return descr.types;
    }

    return NULL;
}

static BOOL
signatures_proto_compatible(const char* type1, const char* type2)
{
    /* Ignore type modifiers */
    type1 = PyObjCRT_SkipTypeQualifiers(type1);
    type2 = PyObjCRT_SkipTypeQualifiers(type2);

    if (*type1 == _C_ARY_B) {
        if (type2[0] == _C_PTR) {
            type1++;
            while (isdigit(*type1))
                type1++;
            return signatures_proto_compatible(type1, type2 + 1);

        } else if (type2[0] == _C_ARY_B) {
            type1++;
            while (isdigit(*type1))
                type1++;
            type2++;
            while (isdigit(*type2))
                type2++;
            return signatures_proto_compatible(type1, type2);
        }
        return NO;
    }

    if (PyObjCRT_SizeOfType(type1) != PyObjCRT_SizeOfType(type2)) {
        return NO;
    }

    switch (*type1) {
    case _C_CHARPTR:
        if (*type2 == _C_CHARPTR) {
            return YES;

        } else if (*type2 == _C_PTR) {
            return signatures_proto_compatible("c", type2 + 1);

        } else {
            return NO;
        }

    case _C_PTR:
        if (*type2 == _C_CHARPTR) {
            return signatures_proto_compatible(type1 + 1, "c");
        }

        if (*type2 != _C_PTR) {
            return NO;
        }

        if (type1[1] == _C_VOID || type2[1] == _C_VOID) {
            return YES;
        }

        return PyObjC_signatures_compatible(type1 + 1, type2 + 1);

    case _C_CHR:
    case _C_BOOL:
    case _C_NSBOOL:
        switch (*type2) {
        case _C_CHR:
        case _C_BOOL:
        case _C_NSBOOL:
            return YES;
        }
        return NO;

    case _C_LNG:
    case _C_LNG_LNG:
        switch (*type2) {
        case _C_LNG:
        case _C_LNG_LNG:
            return YES;
        }
        return NO;

    case _C_ULNG:
    case _C_ULNG_LNG:
        switch (*type2) {
        case _C_ULNG:
        case _C_ULNG_LNG:
            return YES;
        }
        return NO;

    default: {
        const char* e1 = PyObjCRT_SkipTypeSpec(type1);
        if (e1 == NULL) {
            PyErr_Clear();
            return NO;
        }
        return strncmp(type1, type2, e1 - type1) == 0;
    }
    }
}

static int
do_verify(const char* protocol_name, struct objc_method_description* descr, BOOL is_class,
          BOOL is_required, char* name, PyObject* super_class, PyObject* clsdict,
          PyObject* metadict)
{
    PyObject* meth;
    if (is_class) {
        meth = PyObjC_FindSELInDict(metadict, descr->name);
        PyObjC_Assert(
            meth == NULL
                || (PyObjCSelector_Check(meth) && PyObjCSelector_IsClassMethod(meth)),
            -1);
    } else {
        meth = PyObjC_FindSELInDict(clsdict, descr->name);
        PyObjC_Assert(
            meth == NULL
                || (PyObjCSelector_Check(meth) && !PyObjCSelector_IsClassMethod(meth)),
            -1);
    }

    if (meth == NULL) {
        meth = PyObjCClass_FindSelector(super_class, descr->name, is_class);
        if (meth == NULL || !PyObjCSelector_Check(meth)) {
            PyErr_Clear();
            if (is_required) {
                if (is_class) {
                    meth = PyObjC_FindSELInDict(clsdict, descr->name);
                    if (meth != NULL) {
                        Py_DECREF(meth);
                        PyErr_Format(PyExc_TypeError,
                                     "class %s does not correctly implement protocol "
                                     "%s: method '%s' is not a class method",
                                     name, protocol_name, sel_getName(descr->name));
                        return -1;
                    }
                } else {
                    meth = PyObjC_FindSELInDict(metadict, descr->name);
                    if (meth != NULL) {
                        Py_DECREF(meth);
                        PyErr_Format(PyExc_TypeError,
                                     "class %s does not correctly implement protocol "
                                     "%s: method '%s' is not an instance method",
                                     name, protocol_name, sel_getName(descr->name));
                        return -1;
                    }
                }
                meth = PyObjCClass_FindSelector(super_class, descr->name, !is_class);
                if (meth != NULL) {
                    Py_DECREF(meth);
                    PyErr_Format(PyExc_TypeError,
                                 "class %s does not correctly implement protocol "
                                 "%s: method '%s' is not a %s method",
                                 name, protocol_name, sel_getName(descr->name),
                                 is_class ? "class" : "instance");
                    return -1;
                }

                PyErr_Format(PyExc_TypeError,
                             "class %s does not fully implement protocol "
                             "%s: no implementation for '%s'",
                             name, protocol_name, sel_getName(descr->name));
                return -1;
            } else {
                /* Method is not required, ignore */
                return 0;
            }
        }

        /* XXX: it is possible to trigger this for instance method, look into
         *      adjusting PyObjCClass_FindSelector: it can return a method object
         *      that does not match our request.
         */
        if (is_class) {
            if (!PyObjCSelector_IsClassMethod(meth)) {
                PyErr_Format(PyExc_TypeError,
                             "class %s does not correctly implement "
                             "protocol %s: method '%s' is not a "
                             "class method",
                             name, protocol_name, sel_getName(descr->name));
                return -1;
            }

        } else {
            if (PyObjCSelector_IsClassMethod(meth)) {
                PyErr_Format(PyExc_TypeError,
                             "class %s does not correctly implement "
                             "protocol %s: method '%s' is not an "
                             "instance method",
                             name, protocol_name, sel_getName(descr->name));
                return -1;
            }
        }
    }

    const char* sel_sig = PyObjCSelector_Signature(meth);
    if (sel_sig == NULL) { // LCOV_BR_EXCL_LINE
        return -1;         // LCOV_EXCL_LINE
    }
    if (PyObjCRT_SignaturesEqual(descr->types, sel_sig)) {
        return 0;
    }
    if (signatures_proto_compatible(descr->types, sel_sig)) {
        return 0;
    }

    PyErr_Format(PyExc_TypeError,
                 "class %s does not correctly implement "
                 "protocol %s: the signature for method '%s' "
                 "is %s instead of %s",
                 name, protocol_name, sel_getName(descr->name),
                 PyObjCSelector_Signature(meth), descr->types);
    return -1;
}

static int
do_check(const char* protocol_name, Protocol* protocol, char* name, PyObject* super_class,
         PyObject* clsdict, PyObject* metadict)
{
    int      r;
    unsigned idx;

    unsigned   parentCount;
    Protocol** parents = protocol_copyProtocolList(protocol, &parentCount);
    if (parents) {
        for (idx = 0; idx < parentCount; idx++) {
            r = do_check(protocol_name, parents[idx], name, super_class, clsdict,
                         metadict);
            if (r == -1) {
                free(parents);
                return r;
            }
        }
        free(parents);
    }

    unsigned int                    methCount;
    struct objc_method_description* methinfo;

    methCount = 0;
    methinfo  = protocol_copyMethodDescriptionList(protocol, YES, YES, &methCount);
    if (methinfo) {
        for (idx = 0; idx < methCount; idx++) {
            if (do_verify(protocol_name, methinfo + idx, NO, YES, name, super_class,
                          clsdict, metadict)
                == -1) {
                free(methinfo);
                return -1;
            }
        }
        free(methinfo);
    }

    methinfo = protocol_copyMethodDescriptionList(protocol, NO, YES, &methCount);
    if (methinfo) {
        for (idx = 0; idx < methCount; idx++) {
            if (do_verify(protocol_name, methinfo + idx, NO, NO, name, super_class,
                          clsdict, metadict)
                == -1) {
                free(methinfo);
                return -1;
            }
        }
        free(methinfo);
    }

    methinfo = protocol_copyMethodDescriptionList(protocol, YES, NO, &methCount);
    if (methinfo) {
        for (idx = 0; idx < methCount; idx++) {
            if (do_verify(protocol_name, methinfo + idx, YES, YES, name, super_class,
                          clsdict, metadict)
                == -1) {
                free(methinfo);
                return -1;
            }
        }
        free(methinfo);
    }

    methinfo = protocol_copyMethodDescriptionList(protocol, NO, NO, &methCount);
    if (methinfo) {
        for (idx = 0; idx < methCount; idx++) {
            if (do_verify(protocol_name, methinfo + idx, YES, NO, name, super_class,
                          clsdict, metadict)
                == -1) {
                free(methinfo);
                return -1;
            }
        }
        free(methinfo);
    }

    return 0;
}

int
PyObjCFormalProtocol_CheckClass(PyObject* obj, char* name, PyObject* super_class,
                                PyObject* clsdict, PyObject* metadict)
{
    PyObjCFormalProtocol* self = (PyObjCFormalProtocol*)obj;

    PyObjC_Assert(PyObjCFormalProtocol_Check(obj), -1);
    PyObjC_Assert(PyObjCClass_Check(super_class), -1);
    PyObjC_Assert(PyDict_Check(clsdict), -1);

    return do_check(protocol_getName(self->objc), self->objc, name, super_class, clsdict,
                    metadict);
}

PyObject* _Nullable PyObjCFormalProtocol_ForProtocol(Protocol* protocol)
{
    PyObjCFormalProtocol* result;

    PyObjC_Assert(protocol != NULL, NULL);

    result = (PyObjCFormalProtocol*)PyObject_New(PyObjCFormalProtocol,
                                                 &PyObjCFormalProtocol_Type);
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

NS_ASSUME_NONNULL_END
