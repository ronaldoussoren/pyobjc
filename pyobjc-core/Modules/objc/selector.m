/*
 * Implementation of 'native' and 'python' selectors
 */
#include "pyobjc.h"

#include <objc/Object.h>

NS_ASSUME_NONNULL_BEGIN

PyObject* PyObjCSelector_Type;
PyObject* PyObjCNativeSelector_Type;
PyObject* PyObjCPythonSelector_Type;

static char* _Nullable pysel_default_signature(SEL selector, PyObject* callable);
static PyObject* _Nullable pysel_new(PyTypeObject* type, PyObject* _Nullable args,
                                     PyObject* _Nullable kwds);

/*
 * Base type for objective-C selectors
 *
 * selectors are callable objects with the following attributes:
 * - 'signature': The objective-C signature of the method
 * - 'selector': The name in the objective-C runtime
 */

PyObjCMethodSignature* _Nullable PyObjCSelector_GetMetadata(PyObject* _self)
{
    PyObjC_Assert(PyObjCSelector_Check(_self), NULL);

    PyObjCSelector* self = (PyObjCSelector*)_self;

    if (self->sel_methinfo != NULL && self->sel_mappingcount != PyObjC_MappingCount) {
        Py_CLEAR(self->sel_methinfo);
    }

    if (self->sel_methinfo == NULL) {
        self->sel_methinfo = PyObjCMethodSignature_ForSelector(
            self->sel_class, (self->sel_flags & PyObjCSelector_kCLASS_METHOD) != 0,
            self->sel_selector, self->sel_python_signature,
            PyObjCNativeSelector_Check(self));

        if (self->sel_methinfo == NULL)
            return NULL;

        if (PyObjCPythonSelector_Check(_self)) {
            Py_ssize_t i;

            ((PyObjCPythonSelector*)_self)->numoutput = 0;
            for (i = 0; i < Py_SIZE(((PyObjCPythonSelector*)_self)->base.sel_methinfo);
                 i++) {
                if (((PyObjCPythonSelector*)_self)->base.sel_methinfo->argtype[i]->type[0]
                    == _C_OUT) {
                    ((PyObjCPythonSelector*)_self)->numoutput++;
                }
            }
        }
    }

    return self->sel_methinfo;
}

PyDoc_STRVAR(sel_metadata_doc,
             "__metadata__()\n" CLINIC_SEP
             "\nReturn a dict that describes the metadata for this method, including "
             "metadata for the 2 hidden ObjC parameters (self and _sel) ");
static PyObject* _Nullable sel_metadata(PyObject* self)
{
    int                    r;
    PyObjCMethodSignature* mi = PyObjCSelector_GetMetadata(self);
    if (mi == NULL) {
        return NULL;
    }

    PyObject* result = PyObjCMethodSignature_AsDict(mi);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    r = PyDict_SetItemString(
        result, "classmethod",
        (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kCLASS_METHOD) ? Py_True
                                                                            : Py_False);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    r = PyDict_SetItemString(result, "hidden",
                             (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kHIDDEN)
                                 ? Py_True
                                 : Py_False);

    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
        r = PyDict_SetItemString(result, "return_uninitialized_object", Py_True);
        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }
    return result;
}

static PyMethodDef sel_methods[] = {{.ml_name  = "__metadata__",
                                     .ml_meth  = (PyCFunction)sel_metadata,
                                     .ml_flags = METH_NOARGS,
                                     .ml_doc   = sel_metadata_doc},
                                    {
                                        .ml_name = NULL /* SENTINEL */
                                    }};

PyDoc_STRVAR(base_self_doc, "'self' object for bound methods, None otherwise");

static PyObject*
base_self(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    if (self->sel_self) {
        Py_INCREF(self->sel_self);
        return self->sel_self;
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}

PyDoc_STRVAR(base_signature_doc, "Objective-C signature for the method");

static PyObject* _Nullable base_signature(PyObject* self,
                                          void*     closure __attribute__((__unused__)))
{
    PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(self);
    if (methinfo == NULL) {
        return NULL;
    }

    return PyBytes_FromString(methinfo->signature);
}

PyDoc_STRVAR(base_native_signature_doc, "original Objective-C signature for the method");

static PyObject*
base_native_signature(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    if (self->sel_native_signature == NULL) {
        /* XXX: When can this be NULL? */
        Py_INCREF(Py_None);
        return Py_None;
    }

    return PyBytes_FromString(self->sel_native_signature);
}

static int
base_signature_setter(PyObject* _self, PyObject* newVal,
                      void* closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    char*                 t;

    if (newVal == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete 'signature'");
        return -1;
    }

    if (!PyBytes_Check(newVal)) {
        PyErr_SetString(PyExc_TypeError, "signature must be byte string");
        return -1;
    }

    t = PyObjCUtil_Strdup(PyBytes_AsString(newVal));
    if (t == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return -1;
        // LCOV_EXCL_STOP
    }

    PyMem_Free((char*)self->base.sel_python_signature);
    self->base.sel_python_signature = t;

    if (self->base.sel_methinfo != NULL) {
        /* Native selector was changed, ensure the metadata gets updated */
        Py_CLEAR(self->base.sel_methinfo);
    }
    return 0;
}

PyDoc_STRVAR(base_hidden_doc,
             "If True the method is not directly accessible as an object attribute");

static PyObject*
base_hidden(PyObject* _self, void* closure __attribute__((__unused__)))
{
    return PyBool_FromLong(((PyObjCSelector*)_self)->sel_flags & PyObjCSelector_kHIDDEN);
}
static int
base_hidden_setter(PyObject* _self, PyObject* newVal,
                   void* closure __attribute__((__unused__)))
{
    if (newVal == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete 'isHidden'");
        return -1;
    }

    if (PyObject_IsTrue(newVal)) {
        ((PyObjCSelector*)_self)->sel_flags |= PyObjCSelector_kHIDDEN;
    } else {
        ((PyObjCSelector*)_self)->sel_flags &= ~PyObjCSelector_kHIDDEN;
    }
    return 0;
}

PyDoc_STRVAR(base_selector_doc, "Objective-C name for the method");

static PyObject*
base_selector(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    return PyBytes_FromString(sel_getName(self->sel_selector));
}

PyDoc_STRVAR(base_name_doc, "Name for the method");

static PyObject* _Nullable base_name(PyObject* _self,
                                     void*     closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    char            buf[2048];
    const char*     name;

    name = PyObjC_SELToPythonName(self->sel_selector, buf, sizeof(buf));
    if (name == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    return PyUnicode_FromString(name);
}

PyDoc_STRVAR(base_class_doc, "Objective-C Class that defines the method");
static PyObject* _Nullable base_class(PyObject* _self,
                                      void*     closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    if (self->base.sel_class != nil) {
        return PyObjCClass_New(self->base.sel_class);
    }

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(base_class_method_doc, "True if this is a class method, False otherwise");

static PyObject*
base_class_method(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    return PyBool_FromLong(0 != (self->base.sel_flags & PyObjCSelector_kCLASS_METHOD));
}

PyDoc_STRVAR(base_required_doc, "True if this is a required method, False otherwise");

static PyObject*
base_required(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    return PyBool_FromLong(0 != (self->base.sel_flags & PyObjCSelector_kREQUIRED));
}

static PyGetSetDef base_getset[] = {{
                                        .name = "isHidden",
                                        .get  = base_hidden,
                                        .set  = base_hidden_setter,
                                        .doc  = base_hidden_doc,
                                    },
                                    {
                                        .name = "isRequired",
                                        .get  = base_required,
                                        .doc  = base_required_doc,
                                    },
                                    {
                                        .name = "isClassMethod",
                                        .get  = base_class_method,
                                        .doc  = base_class_method_doc,
                                    },
                                    {
                                        .name = "definingClass",
                                        .get  = base_class,
                                        .doc  = base_class_doc,
                                    },
                                    {
                                        .name = "__objclass__",
                                        .get  = base_class,
                                        .doc  = base_class_doc,
                                    },
                                    {
                                        .name = "signature",
                                        .get  = base_signature,
                                        .set  = base_signature_setter,
                                        .doc  = base_signature_doc,
                                    },
                                    {
                                        .name = "native_signature",
                                        .get  = base_native_signature,
                                        .doc  = base_native_signature_doc,
                                    },
                                    {
                                        .name = "self",
                                        .get  = base_self,
                                        .doc  = base_self_doc,
                                    },
                                    {
                                        .name = "selector",
                                        .get  = base_selector,
                                        .doc  = base_selector_doc,
                                    },
                                    {
                                        .name = "__name__",
                                        .get  = base_name,
                                        .doc  = base_name_doc,
                                    },
                                    {
                                        .name = NULL /* SENTINEL */
                                    }};

static void
sel_dealloc(PyObject* object)
{
    PyObjCSelector* self = (PyObjCSelector*)object;
    Py_XDECREF(self->sel_self);
    self->sel_self = NULL;
    Py_XDECREF(self->sel_methinfo);
    self->sel_methinfo = NULL;

    PyMem_Free((char*)self->sel_python_signature);

    if (self->sel_native_signature != NULL) {
        PyMem_Free((char*)self->sel_native_signature);
        self->sel_native_signature = NULL;
    }
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(object);
#endif
    PyObject_Del(object);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

PyDoc_STRVAR(base_selector_type_doc,
             "selector(function, [, selector] [, signature] [, isClassMethod=0]\n"
             "    [, isRequired=True]) -> selector\n"
             "\n"
             "Return an Objective-C method from a function. The other arguments \n"
             "specify attributes of the Objective-C method.\n"
             "\n"
             "function:\n"
             "  A function object with at least one argument. The first argument will\n"
             "  be used to pass 'self'. This argument may be None when defining an\n"
             "  informal_protocol object. The function must not be a ``staticmethod``\n"
             "  instance. \n"
             "\n"
             "selector:\n"
             "  The name of the Objective-C method. The default value of this\n"
             "  attribute is the name of the function, with all underscores replaced\n"
             "  by colons.\n"
             "\n"
             "signature:\n"
             "  Method signature for the Objective-C method. This should be a raw\n"
             "  Objective-C method signature, including specifications for 'self' and\n"
             "  '_cmd'. The default value a signature that describes a method with\n"
             "  arguments of type 'id' and a return-value of the same type.\n"
             "\n"
             "isClassMethod:\n"
             "  True if the method is a class method, false otherwise. The default is \n"
             "  False, unless the function is an instance of ``classmethod``.\n"
             "\n"
             "isRequired:\n"
             "  True if this is a required method in an informal protocol, False\n"
             "  otherwise. The default value is 'True'. This argument is only used\n"
             "  when defining an 'informal_protocol' object.\n");
static PyType_Slot sel_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&sel_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&base_selector_type_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&sel_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&base_getset},
    {.slot = Py_tp_new, .pfunc = (void*)&pysel_new},

    {0, NULL} /* sentinel */
};

static PyType_Spec sel_spec = {
    .name      = "objc.selector",
    .basicsize = sizeof(PyObjCSelector),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_BASETYPE,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_BASETYPE,
#endif
    .slots = sel_slots,
};

/*
 * Selector type for 'native' selectors (that is, selectors that are not
 * implemented as python methods)
 */
static PyObject*
objcsel_repr(PyObject* _self)
{
    PyObjCNativeSelector* sel = (PyObjCNativeSelector*)_self;
    PyObject*             rval;
    if (sel->base.sel_self == NULL) {
        rval = PyUnicode_FromFormat("<unbound native-selector %s in %s>",
                                    sel_getName(sel->base.sel_selector),
                                    class_getName(sel->base.sel_class));

    } else {
        rval =
            PyUnicode_FromFormat("<native-selector %s of %R>",
                                 sel_getName(sel->base.sel_selector), sel->base.sel_self);
    }

    return rval;
}

static PyObject*
objcsel_richcompare(PyObject* a, PyObject* b, int op)
{
    if (op == Py_EQ || op == Py_NE) {
        if (PyObjCNativeSelector_Check(a) && PyObjCNativeSelector_Check(b)) {

            PyObjCNativeSelector* sel_a = (PyObjCNativeSelector*)a;
            PyObjCNativeSelector* sel_b = (PyObjCNativeSelector*)b;
            int                   same  = 1;

            if (sel_a->base.sel_selector != sel_b->base.sel_selector) {
                same = 0;
            }
            if (sel_a->base.sel_class != sel_b->base.sel_class) {
                same = 0;
            }
            if (sel_a->base.sel_self != sel_b->base.sel_self) {
                same = 0;
            }
            if ((op == Py_EQ && !same) || (op == Py_NE && same)) {
                Py_INCREF(Py_False);
                return Py_False;
            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }

        } else {
            if (op == Py_EQ) {
                Py_INCREF(Py_False);
                return Py_False;

            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }
        }

    } else {
        if (PyObjCSelector_Check(a) && PyObjCSelector_Check(b)) {
            SEL sel_a = PyObjCSelector_GET_SELECTOR(a);
            SEL sel_b = PyObjCSelector_GET_SELECTOR(b);

            int r = strcmp(sel_getName(sel_a), sel_getName(sel_b));
            switch (op) { // LCOV_BR_EXCL_LINE
            case Py_LT:
                return PyBool_FromLong(r < 0);
            case Py_LE:
                return PyBool_FromLong(r <= 0);
            case Py_GT:
                return PyBool_FromLong(r > 0);
            case Py_GE:
                return PyBool_FromLong(r >= 0);
            } // LCOV_EXCL_LINE
        }

        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }
}

static void
objcsel_dealloc(PyObject* obj)
{
    if (((PyObjCNativeSelector*)obj)->sel_cif != NULL) {
        PyObjCFFI_FreeCIF(((PyObjCNativeSelector*)obj)->sel_cif);
    }
    sel_dealloc(obj);
}

#if PY_VERSION_HEX >= 0x03090000
static PyObject* _Nullable objcsel_vectorcall_simple(
    PyObject* _self, PyObject* _Nonnull const* _Nonnull args, size_t nargsf,
    PyObject* _Nullable kwnames)
{
    PyObjCNativeSelector*  self   = (PyObjCNativeSelector*)_self;
    PyObject*              pyself = self->base.sel_self;
    PyObject*              res;
    PyObject*              pyres;
    PyObjCMethodSignature* methinfo;

    if (PyObjC_CheckNoKwnames(_self, kwnames) == -1) {
        return NULL;
    }
    if (pyself == NULL) {
        if (PyVectorcall_NARGS(nargsf) < 1) {
            PyErr_SetString(PyExc_TypeError, "Missing argument: self");
            return NULL;
        }

        pyself = args[0];
        PyObjC_Assert(pyself != NULL, NULL);

        args   = args + 1;
        nargsf = PyVectorcall_NARGS(nargsf) - 1;
    }

    methinfo = PyObjCSelector_GetMetadata(_self);
    if (methinfo == NULL) {
        return NULL;
    }

    if (version_is_deprecated(methinfo->deprecated)) {
        char  buf[128];
        Class cls = PyObjCSelector_GetClass(_self);
        SEL   sel = PyObjCSelector_GetSelector(_self);

        snprintf(buf, 128, "%c[%s %s] is a deprecated API (macOS %d.%d)",
                 PyObjCSelector_IsClassMethod(_self) ? '+' : '-', class_getName(cls),
                 sel_getName(sel), methinfo->deprecated / 100,
                 methinfo->deprecated % 100);
        if (PyErr_Warn(PyObjCExc_DeprecationWarning, buf) < 0) {
            return NULL;
        }
    }
    if (!(self->base.sel_flags & PyObjCSelector_kCLASS_METHOD)) {
        /*
         * Class methods should always be bound, therefore we only
         * have to validate the type of self for instance methods.
         */
        PyObjC_Assert(self->base.sel_class != Nil, NULL);
        PyObject* myClass = PyObjCClass_New(self->base.sel_class);
        if (myClass == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;       // LCOV_EXCL_LINE
        }

        if (!(PyObject_IsInstance(pyself, myClass)
              || (PyUnicode_Check(pyself)
                  && PyObjC_class_isSubclassOf(self->base.sel_class,
                                               [NSString class])))) {

            Py_DECREF(myClass);
            PyErr_Format(PyExc_TypeError,
                         "Expecting instance of %s as self, got one "
                         "of %s",
                         class_getName(self->base.sel_class), Py_TYPE(pyself)->tp_name);
            return NULL;
        }
        Py_DECREF(myClass);
    }

    pyres = res = PyObjCFFI_Caller_SimpleSEL((PyObject*)self, pyself, args, nargsf);
    if (pyres != NULL && PyTuple_Check(pyres) && PyTuple_GET_SIZE(pyres) >= 1
        && PyTuple_GET_ITEM(pyres, 0) == pyself) {

        pyres = pyself;
    }

    if (PyObjCObject_Check(pyself)
        && (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED)) {
        if (pyself != pyres && !PyErr_Occurred()) {
            PyObjCObject_ClearObject(pyself);
        }
    }

    if (pyres && PyObjCObject_Check(pyres)) {
        if (self->base.sel_flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags |= PyObjCObject_kUNINITIALIZED;
        } else if (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED) {
            ((PyObjCObject*)pyself)->flags &= ~PyObjCObject_kUNINITIALIZED;
            if (self->base.sel_self && self->base.sel_self != pyres
                && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(self->base.sel_self);
            }
        }
    }
    return res;
}
#endif

static PyObject* _Nullable objcsel_vectorcall(PyObject* _self,
                                              PyObject* _Nonnull const* _Nonnull args,
                                              size_t nargsf, PyObject* _Nullable kwnames)
{
    /* XXX: Need logic to reset sel_call_func and sel_vectocall when
     * the methodinfo changes, both here and in the "simple" variant.
     * This way extensions can register a new call_func even after the
     * method has been resolved.
     */

    PyObjCNativeSelector*  self    = (PyObjCNativeSelector*)_self;
    PyObject*              pyself  = self->base.sel_self;
    PyObjC_CallFunc        execute = NULL;
    PyObject*              res;
    PyObject*              pyres;
    PyObjCMethodSignature* methinfo;

    if (PyObjC_CheckNoKwnames(_self, kwnames) == -1) {
        return NULL;
    }

    if (pyself == NULL) {
        /* XXX: Fold this into execution of callfunc, that also checks for bound/unbound
         */
        if (PyVectorcall_NARGS(nargsf) < 1) {
            PyErr_SetString(PyExc_TypeError, "Missing argument: self");
            return NULL;
        }

        pyself = args[0];
        if (pyself == NULL) {
            return NULL;
        }
    }

    methinfo = PyObjCSelector_GetMetadata(_self);
    if (methinfo == NULL) {
        return NULL;
    }

    if (version_is_deprecated(methinfo->deprecated)) {
        char  buf[128];
        Class cls = PyObjCSelector_GetClass(_self);
        SEL   sel = PyObjCSelector_GetSelector(_self);

        assert(cls);
        assert(sel);

        snprintf(buf, 128, "%c[%s %s] is a deprecated API (macOS %d.%d)",
                 PyObjCSelector_IsClassMethod(_self) ? '+' : '-', class_getName(cls),
                 sel_getName(sel), methinfo->deprecated / 100,
                 methinfo->deprecated % 100);
        if (PyErr_Warn(PyObjCExc_DeprecationWarning, buf) < 0) {
            return NULL;
        }
    }

    if (self->sel_call_func) {
        execute = self->sel_call_func;
    } else {
        PyObjC_Assert(self->base.sel_class != NULL, NULL);

        execute = PyObjC_FindCallFunc(self->base.sel_class, self->base.sel_selector,
                                      self->base.sel_methinfo->signature);
        if (execute == NULL)
            return NULL;
        self->sel_call_func = execute;
#if PY_VERSION_HEX >= 0x03090000
        /* Update the vectorcall slot when a faster call is possible */
        if (methinfo->shortcut_signature && execute == PyObjCFFI_Caller) {
            PyObjC_Assert(methinfo->shortcut_signature, NULL);
            self->base.sel_vectorcall = objcsel_vectorcall_simple;
        }
#endif
    }

    /* XXX: The if statement below can be simplified, both cases are mostly the same */
    if (self->base.sel_self != NULL) {
        pyres = res = execute((PyObject*)self, self->base.sel_self, args,
                              PyVectorcall_NARGS(nargsf));
        if (pyres != NULL && PyTuple_Check(pyres) && PyTuple_GET_SIZE(pyres) >= 1
            && PyTuple_GET_ITEM(pyres, 0) == pyself) {

            pyres = pyself;
        }

        if (PyObjCObject_Check(self->base.sel_self)
            && (((PyObjCObject*)self->base.sel_self)->flags
                & PyObjCObject_kUNINITIALIZED)) {
            if (self->base.sel_self != pyres && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(self->base.sel_self);
            }
        }

    } else {
        PyObject* myClass;

        PyObjC_Assert(self->base.sel_class != Nil, NULL);

        myClass = PyObjCClass_New(self->base.sel_class);
        if (myClass == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;       // LCOV_EXCL_LINE
        }
        if (!(PyObject_IsInstance(pyself, myClass)
              || (PyUnicode_Check(pyself)
                  && PyObjC_class_isSubclassOf(self->base.sel_class,
                                               [NSString class])))) {

            Py_DECREF(myClass);
            PyErr_Format(PyExc_TypeError,
                         "Expecting instance of %s as self, got one "
                         "of %s",
                         class_getName(self->base.sel_class), Py_TYPE(pyself)->tp_name);
            return NULL;
        }
        Py_DECREF(myClass);

        pyres = res =
            execute((PyObject*)self, pyself, args + 1, PyVectorcall_NARGS(nargsf) - 1);
        if (pyres != NULL && PyTuple_Check(pyres) && PyTuple_GET_SIZE(pyres) > 1
            && PyTuple_GET_ITEM(pyres, 0) == pyself) {
            pyres = pyself;
        }

        if (PyObjCObject_Check(pyself)
            && (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED)) {
            if (pyself != pyres && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(pyself);
            }
        }
    }

    if (pyres && PyObjCObject_Check(pyres)) {
        if (self->base.sel_flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags |= PyObjCObject_kUNINITIALIZED;
        } else if (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED) {
            ((PyObjCObject*)pyself)->flags &= ~PyObjCObject_kUNINITIALIZED;
            if (self->base.sel_self && self->base.sel_self != pyres
                && !PyErr_Occurred()) {
                /* XXX: This needs documentation, the logic is not 100% rigorous */
                PyObjCObject_ClearObject(self->base.sel_self);
            }
        }
    }

    return res;
}

#if PY_VERSION_HEX < 0x03090000
static PyObject* _Nullable objcsel_call(PyObject* _self, PyObject* _Nullable args,
                                        PyObject* _Nullable kwds)
{
    if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
        return NULL;
    }

    return objcsel_vectorcall(_self, PyTuple_ITEMS(args), PyTuple_GET_SIZE(args), NULL);
}
#endif

static PyObject* _Nullable objcsel_descr_get(PyObject* _self, PyObject* _Nullable obj,
                                             PyObject* _Nullable class)
{
    PyObjCNativeSelector* meth = (PyObjCNativeSelector*)_self;
    PyObjCNativeSelector* result;

    if (meth->base.sel_self != NULL || obj == Py_None) {
        Py_INCREF(meth);
        return (PyObject*)meth;
    }

    if (class != nil && PyType_Check(class)
        && PyType_IsSubtype((PyTypeObject*)class, &PyObjCClass_Type)) {
        class = PyObjCClass_ClassForMetaClass(class);
    }

    /* Bind 'self' */
    if (meth->base.sel_flags & PyObjCSelector_kCLASS_METHOD) {
        obj = class;
    } else {
        if (obj && PyObjCClass_Check(obj)) {
            obj = NULL;
        }
    }
    result = PyObject_New(PyObjCNativeSelector, (PyTypeObject*)PyObjCNativeSelector_Type);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    result->base.sel_selector         = meth->base.sel_selector;
    result->base.sel_flags            = meth->base.sel_flags;
    result->base.sel_class            = meth->base.sel_class;
    result->base.sel_methinfo         = NULL;
    result->base.sel_python_signature = (const char* _Nonnull)NULL;
    result->base.sel_native_signature = (const char* _Nonnull)NULL;
    result->base.sel_mappingcount     = meth->base.sel_mappingcount;
    result->base.sel_self             = NULL;
    result->sel_cif                   = NULL;
#if PY_VERSION_HEX >= 0x03090000
    result->base.sel_vectorcall = objcsel_vectorcall;
#endif
    result->sel_call_func = meth->sel_call_func;

    const char* tmp = PyObjCUtil_Strdup(meth->base.sel_python_signature);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
    result->base.sel_python_signature = tmp;

    tmp = PyObjCUtil_Strdup(meth->base.sel_native_signature);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
    result->base.sel_native_signature = tmp;

    if (meth->sel_call_func == NULL) {
        if (class_isMetaClass(meth->base.sel_class)) {
            PyObject* metaclass_obj = PyObjCClass_New(meth->base.sel_class);
            if (metaclass_obj == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }
            PyObject* class_obj = PyObjCClass_ClassForMetaClass(metaclass_obj);
            Py_CLEAR(metaclass_obj);

            if (class_obj == NULL) {
                Py_DECREF(result);
                return NULL;
            }

            /* PyObjCClass_ClassForMetaClass will only return a class proxy for a non-Nil
             * class */
            meth->sel_call_func = PyObjC_FindCallFunc(
                (Class _Nonnull)PyObjCClass_GetClass(class_obj), meth->base.sel_selector,
                meth->base.sel_methinfo->signature);
            Py_CLEAR(class_obj);

        } else {
            meth->sel_call_func =
                PyObjC_FindCallFunc(meth->base.sel_class, meth->base.sel_selector,
                                    meth->base.sel_methinfo->signature);
        }
        if (meth->sel_call_func == NULL) {
            Py_DECREF(result);
            return NULL;
        }
    }

    if (meth->base.sel_methinfo != NULL) {
        result->base.sel_methinfo = meth->base.sel_methinfo;
        Py_INCREF(result->base.sel_methinfo);
    } else {
        result->base.sel_methinfo = PyObjCSelector_GetMetadata((PyObject*)meth);
        if (result->base.sel_methinfo) {
            Py_INCREF(result->base.sel_methinfo);
        } else {
            PyErr_Clear();
        }
    }

#if PY_VERSION_HEX >= 0x03090000
    /* XXX: 'sel_methinfo' should probably be _Nonnull */
    if (result->base.sel_methinfo && result->base.sel_methinfo->shortcut_signature
        && result->sel_call_func == PyObjCFFI_Caller) {
        result->base.sel_vectorcall = objcsel_vectorcall_simple;
    } else {
        result->base.sel_vectorcall = objcsel_vectorcall;
    }
#endif

    result->base.sel_self = obj;
    if (result->base.sel_self) {
        Py_INCREF(result->base.sel_self);
    }

    return (PyObject*)result;
}

static PyGetSetDef objcsel_getset[] = {{
                                           .name = "__doc__",
                                           .get  = PyObjC_callable_docstr_get,
                                           .doc  = "The document string for a method",
                                       },
                                       {
                                           .name = "__signature__",
                                           .get  = PyObjC_callable_signature_get,
                                           .doc  = "inspect.Signature for a method",
                                       },
                                       {
                                           .name = NULL /* SENTINEL */
                                       }};

#if PY_VERSION_HEX >= 0x03090000
static PyMemberDef objcsel_members[] = {
    {
        .name   = "__vectorcalloffset__",
        .type   = T_PYSSIZET,
        .offset = offsetof(PyObjCNativeSelector, base.sel_vectorcall),
        .flags  = READONLY,
    },
    {
        .name = NULL /* SENTINEL */
    }};
#endif

static PyType_Slot objcsel_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&objcsel_dealloc},
    {.slot = Py_tp_repr, .pfunc = (void*)&objcsel_repr},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_richcompare, .pfunc = (void*)&objcsel_richcompare},
    {.slot = Py_tp_getset, .pfunc = (void*)&objcsel_getset},
    {.slot = Py_tp_descr_get, .pfunc = (void*)&objcsel_descr_get},
#if PY_VERSION_HEX >= 0x03090000
    {.slot = Py_tp_members, .pfunc = (void*)&objcsel_members},
    {.slot = Py_tp_call, .pfunc = (void*)&PyVectorcall_Call},
#else
    {.slot = Py_tp_call, .pfunc = (void*)&objcsel_call},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec objcsel_spec = {
    .name      = "objc.native_selector",
    .basicsize = sizeof(PyObjCNativeSelector),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_HAVE_VECTORCALL,

#elif PY_VERSION_HEX >= 0x03090000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_HAVE_VECTORCALL,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = objcsel_slots,
};

PyObject*
PyObjCSelector_FindNative(PyObject* self, const char* name)
{
    SEL       sel = PyObjCSelector_DefaultSelector(name);
    PyObject* retval;

    NSMethodSignature* methsig;
    char               buf[2048];

    if (PyObjCObject_Check(self)) {
        PyObject* hidden = PyObjCClass_HiddenSelector((PyObject*)Py_TYPE(self), sel, NO);
        if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;                          // LCOV_EXCL_LINE
        }
        if (PyObjCObject_IsMagic(self) || hidden) {
            PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
            return NULL;
        }

    } else {
        if (PyObjCClass_HiddenSelector(self, sel, YES)) {
            PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
            return NULL;
        } else if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;               // LCOV_EXCL_LINE
        }
    }

    if (name[0] == '_' && name[1] == '_') {
        /* No known Objective-C class has methods whose name
         * starts with '__' or '_:'. This allows us to shortcut
         * lookups for special names, which speeds up tools like
         * pydoc.
         */
        PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
        return NULL;
    }

    if (PyObjCClass_Check(self)) {
        Class cls = PyObjCClass_GetClass(self);

        if (!cls) {
            PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
            return NULL;
        }

        if (strcmp(class_getName(cls), "_NSZombie") == 0
            || strcmp(class_getName(cls), "_CNZombie_") == 0) {
            PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
            return NULL;
        }

        if (
#ifndef __LP64__
            strcmp(class_getName(cls), "Object") == 0 ||
#endif /* !__LP64__ */
            strcmp(class_getName(cls), "NSProxy") == 0) {
            if (sel == @selector(methodSignatureForSelector:)) {
                PyErr_Format(PyExc_AttributeError, "Accessing %s.%s is not supported",
                             class_getName(cls), name);
                return NULL;
            }
        }

        @try {
            if ((class_getClassMethod(cls, @selector(respondsToSelector:)) != NULL) &&
                [cls respondsToSelector:sel]) {
                methsig = [cls methodSignatureForSelector:sel];
                retval  = PyObjCSelector_NewNative(
                    cls, sel,
                    /* XXX: Check if VVV is NULL */
                    PyObjC_NSMethodSignatureToTypeString(methsig, buf, sizeof(buf)), 1);
            } else if ((class_getClassMethod(cls, @selector(methodSignatureForSelector:))
                        != NULL)
                       && nil
                              != (methsig =
                                      [(NSObject*)cls methodSignatureForSelector:sel])) {
                retval = PyObjCSelector_NewNative(
                    cls, sel,
                    /* XXX: Check if VVV is NULL */
                    PyObjC_NSMethodSignatureToTypeString(methsig, buf, sizeof(buf)), 1);
            } else {
                PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
                retval = NULL;
            }

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
            retval = NULL;
        }

        return retval;

    } else if (PyObjCObject_Check(self)) {
        id object;

        object = PyObjCObject_GetObject(self);

        @try {
            if (nil != (methsig = [object methodSignatureForSelector:sel])) {
                PyObjCNativeSelector* res;

                res = (PyObjCNativeSelector*)PyObjCSelector_NewNative(
                    object_getClass(object), sel,
                    /* XXX: Check if VVV is NULL */
                    PyObjC_NSMethodSignatureToTypeString(methsig, buf, sizeof(buf)), 0);
                if (res != NULL) {
                    /* Bind the method to self */
                    res->base.sel_self = self;
                    Py_INCREF(res->base.sel_self);
                }
                retval = (PyObject*)res;
            } else {
                PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
                retval = NULL;
            }

        } @catch (NSObject* localException) {
            PyErr_Format(PyExc_AttributeError, "No attribute %s", name);
            retval = NULL;
        }

        return retval;

    } else {
        PyErr_SetString(PyExc_RuntimeError, "PyObjCSelector_FindNative called on plain "
                                            "python object");
        return NULL;
    }
}

PyObject*
PyObjCSelector_NewNative(Class class, SEL selector, const char* signature,
                         int class_method)
{
    PyObjCNativeSelector* result;
    const char*           native_signature = signature;

    if (signature == NULL) {
        /* XXX: Once all callers have been updated: make this an assertion */
        PyErr_Format(PyExc_RuntimeError, "PyObjCSelector_NewNative: nil signature for %s",
                     sel_getName(selector));
        return NULL;
    }

    result = PyObject_New(PyObjCNativeSelector, (PyTypeObject*)PyObjCNativeSelector_Type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    result->base.sel_self         = NULL;
    result->base.sel_class        = class;
    result->base.sel_flags        = 0;
    result->base.sel_mappingcount = 0;
    result->base.sel_methinfo     = NULL;
    result->base.sel_methinfo     = NULL;
#if PY_VERSION_HEX >= 0x03090000
    result->base.sel_vectorcall = objcsel_vectorcall;
#endif
    result->sel_call_func             = NULL;
    result->sel_cif                   = NULL;
    result->base.sel_python_signature = (const char* _Nonnull)NULL;
    result->base.sel_native_signature = (const char* _Nonnull)NULL;

    result->base.sel_selector = selector;

    Py_ssize_t len = strlen(signature) + 1;
    char*      tmp = PyMem_Malloc(len);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (PyObjCRT_SimplifySignature(signature, tmp, len) == -1) {
        /* In some cases the runtime contains signatures that
         * PyObjC cannot parse. Copy those as-is for easier introspection.
         */
        PyErr_Clear();
        strcpy(tmp, signature);
    }

    result->base.sel_python_signature = tmp;
    result->base.sel_native_signature = PyObjCUtil_Strdup(native_signature);
    if ( // LCOV_BR_EXCL_LINE
        result->base.sel_native_signature == NULL) {
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (class_method) {
        result->base.sel_flags |= PyObjCSelector_kCLASS_METHOD;
    }
    if (sel_isEqual(selector, @selector(alloc))
        || sel_isEqual(selector, @selector(allocWithZone:))) {
        result->base.sel_flags |= PyObjCSelector_kRETURNS_UNINITIALIZED;
    }
    result->base.sel_methinfo = PyObjCSelector_GetMetadata((PyObject*)result);
    if (result->base.sel_methinfo == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    return (PyObject*)result;
}

static char gSheetMethodSignature[] = {_C_VOID, _C_ID,  _C_SEL,  _C_ID,
                                       _C_INT,  _C_PTR, _C_VOID, 0};

#if PY_VERSION_HEX >= 0x03090000
/* XXX: Reorder code to take away need for forward declaration */
static PyObject* _Nullable pysel_vectorcall(PyObject* _self,
                                            PyObject* _Nonnull const* _Nonnull args,
                                            size_t nargsf, PyObject* _Nullable kwnames);
#endif

PyObject*
PyObjCSelector_New(PyObject* callable, SEL selector, const char* _Nullable signature,
                   int class_method, Class _Nullable cls)
{
    PyObjCPythonSelector* result;

    /*
     * XXX: Investigate using the python helper in objc._transform instead of
     *      replicating part of the logic here.
     */
    if (signature == NULL && PyObjCPythonSelector_Check(callable)) {
        signature = PyObjCUtil_Strdup(
            ((PyObjCPythonSelector*)callable)->base.sel_python_signature);

    } else if (signature == NULL) {
        const char* selname = sel_getName(selector);
        size_t      len     = strlen(selname);
        if (len > 30
            && strcmp(selname + len - 30, "DidEnd:returnCode:contextInfo:") == 0) {
            /* XXX: This is a bit too magic...
             *      Consider moving this logic to a python helper.
             */
            signature = PyObjCUtil_Strdup(gSheetMethodSignature);
        } else {
            signature = pysel_default_signature(selector, callable);
        }
    } else {
        signature = PyObjCUtil_Strdup(signature);
    }
    if (signature == NULL) // LCOV_BR_EXCL_LINE
        return NULL;       // LCOV_EXCL_LINE

    result = PyObject_New(PyObjCPythonSelector, (PyTypeObject*)PyObjCPythonSelector_Type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    result->base.sel_self  = NULL;
    result->base.sel_class = cls;
    result->base.sel_flags = 0;
    result->base.sel_methinfo =
        (PyObjCMethodSignature* _Nonnull)NULL; /* We might not know the class right now */
    result->callable = (PyObject* _Nonnull)NULL;
    result->argcount = 0;

    result->base.sel_selector         = selector;
    result->base.sel_python_signature = signature;
    char* tmp                         = PyObjCUtil_Strdup(signature);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
    result->base.sel_native_signature = tmp;
#if PY_VERSION_HEX >= 0x03090000
    result->base.sel_vectorcall = pysel_vectorcall;
#endif

    if (PyObjC_RemoveInternalTypeCodes((char*)result->base.sel_native_signature) == -1) {
        Py_DECREF(result);
        return NULL;
    }

    if (PyObjCPythonSelector_Check(callable)) {
        /* XXX: Should this be supported at all? */
        callable = ((PyObjCPythonSelector*)callable)->callable;
    }

    if (PyObjC_is_pyfunction(callable)) {
        result->argcount = PyObjC_num_arguments(callable);
        if (result->argcount == -1) {
            Py_DECREF(result);
            return NULL;
        }

    } else if (PyMethod_Check(callable)) {
        /* XXX: Can PyMethod_Self ever be NULL? */
        /*      if it cannot: Drop this case */
        if (PyMethod_Self(callable) == NULL) {
            result->argcount = PyObjC_num_arguments(callable);
            if (result->argcount == -1) {
                Py_DECREF(result);
                return NULL;
            }

        } else {
            result->argcount = PyObjC_num_arguments(callable) - 1;
            if (result->argcount == -2) {
                Py_DECREF(result);
                return NULL;
            }
        }

    } else if (PyObjC_is_pymethod(callable)) {
        result->argcount = PyObjC_num_arguments(callable) - 1;
        if (result->argcount == -2) {
            Py_DECREF(result);
            return NULL;
        }

    } else if (callable == Py_None) {
        result->argcount = 0;

    } else {
        result->argcount = 0;
        const char* s    = sel_getName(selector);
        while ((s = strchr(s, ':')) != NULL) {
            result->argcount++;
            s++;
        }
    }

    if (class_method) {
        result->base.sel_flags |= PyObjCSelector_kCLASS_METHOD;
    }
    if (sel_isEqual(selector, @selector(alloc))
        || sel_isEqual(selector, @selector(allocWithZone:))) {
        result->base.sel_flags |= PyObjCSelector_kRETURNS_UNINITIALIZED;
    }

    result->callable = callable;
    Py_INCREF(result->callable);

    return (PyObject*)result;
}

/*
 * Selector type for python selectors (that is, selectors that are
 * implemented as python methods)
 *
 * This one can be allocated from python code.
 */

static Py_hash_t
pysel_hash(PyObject* o)
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)o;
    Py_hash_t             h    = 0;

    if (self->base.sel_self) {
        h ^= PyObject_Hash(self->base.sel_self);
    }
    h ^= (long)(self->base.sel_class);
    h ^= PyObject_Hash(self->callable);

    return h;
}

static PyObject* _Nullable pysel_richcompare(PyObject* a, PyObject* b, int op)
{
    if (op == Py_EQ || op == Py_NE) {
        if (PyObjCPythonSelector_Check(a) && PyObjCPythonSelector_Check(b)) {
            PyObjCPythonSelector* sel_a = (PyObjCPythonSelector*)a;
            PyObjCPythonSelector* sel_b = (PyObjCPythonSelector*)b;
            int                   same  = 1;
            int                   r;

            if (sel_a->base.sel_selector != sel_b->base.sel_selector) {
                same = 0;
            }
            if (sel_a->base.sel_class != sel_b->base.sel_class) {
                same = 0;
            }
            if (sel_a->base.sel_self != sel_b->base.sel_self) {
                same = 0;
            }
            r = PyObject_RichCompareBool(sel_a->callable, sel_b->callable, Py_EQ);
            if (r == -1) {
                return NULL;
            }
            if (!r) {
                same = 0;
            }

            if ((op == Py_EQ && !same) || (op == Py_NE && same)) {
                Py_INCREF(Py_False);
                return Py_False;
            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }

        } else {
            if (op == Py_EQ) {
                Py_INCREF(Py_False);
                return Py_False;
            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }
        }
    } else {
        if (PyObjCSelector_Check(a) && PyObjCSelector_Check(b)) {
            SEL sel_a = PyObjCSelector_GET_SELECTOR(a);
            SEL sel_b = PyObjCSelector_GET_SELECTOR(b);

            int r = strcmp(sel_getName(sel_a), sel_getName(sel_b));
            switch (op) {
            case Py_LT:
                return PyBool_FromLong(r < 0);
            case Py_LE:
                return PyBool_FromLong(r <= 0);
            case Py_GT:
                return PyBool_FromLong(r > 0);
            case Py_GE:
                return PyBool_FromLong(r >= 0);
            }
        }
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }
}

static PyObject*
pysel_repr(PyObject* _self)
{
    PyObjCPythonSelector* sel = (PyObjCPythonSelector*)_self;
    PyObject*             rval;

    if (sel->base.sel_self == NULL) {
        if (sel->base.sel_class) {
            rval = PyUnicode_FromFormat("<unbound selector %s of %s at %p>",
                                        sel_getName(sel->base.sel_selector),
                                        class_getName(sel->base.sel_class), sel);

        } else {
            rval = PyUnicode_FromFormat("<unbound selector %s at %p>",
                                        sel_getName(sel->base.sel_selector), sel);
        }

    } else {
        rval =
            PyUnicode_FromFormat("<selector %s of %R>",
                                 sel_getName(sel->base.sel_selector), sel->base.sel_self);
    }
    return rval;
}

/*
 * Combined implementation for pysel_call (Python 3.8 and earlier)
 * and pysel_vectorcall (Python 3.9 and later). For most other types
 * the call implementation just forwards to the vectorcall implementation,
 * that's not done here because python selectors support keyword arguments.
 *
 * This does result in some preprocessor logic below, the additional complexity
 * is not too bad though.
 */
static PyObject* _Nullable
#if PY_VERSION_HEX < 0x03090000
    pysel_call(PyObject* _self, PyObject* _Nullable args, PyObject* _Nullable kwargs)
#else
    pysel_vectorcall(PyObject* _self, PyObject* _Nonnull const* _Nonnull args,
                     size_t    nargsf, PyObject* _Nullable kwnames)
#endif
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
    PyObject*             result;

    if (self->callable == NULL) {
        PyErr_Format(PyExc_TypeError, "Calling abstract methods with selector %s",
                     sel_getName(self->base.sel_selector));
        return NULL;
    }

    if (!PyObjC_is_pymethod(self->callable)) {
        if (self->base.sel_self == NULL) {
            PyObject* self_arg;
#if PY_VERSION_HEX < 0x03090000
            if (PyTuple_GET_SIZE(args) < 1) {
#else
            if (PyVectorcall_NARGS(nargsf) < 1) {
#endif
                PyErr_SetString(PyObjCExc_Error, "need self argument");
                return NULL;
            }

#if PY_VERSION_HEX < 0x03090000
            self_arg = PyTuple_GET_ITEM(args, 0);
#else
            self_arg = args[0];
#endif

            if (!PyObjCObject_Check(self_arg) && !PyObjCClass_Check(self_arg)) {
                PyErr_Format(PyExc_TypeError,
                             "Expecting an Objective-C class or "
                             "instance as self, got a %s",
                             Py_TYPE(self_arg)->tp_name);
                return NULL;
            }
        }

        /* normal function code will perform other checks */
    }

    /*
     * Assume callable will check arguments
     */
    if (self->base.sel_self == NULL) {
#if PY_VERSION_HEX < 0x03090000
        result = PyObject_Call(self->callable, args, kwargs);
#else
        result = PyObject_Vectorcall(self->callable, args, nargsf, kwnames);
#endif

    } else {
#if PY_VERSION_HEX < 0x03090000
        Py_ssize_t argc        = PyTuple_Size(args);
        PyObject*  actual_args = PyTuple_New(argc + 1);
        Py_ssize_t i;

        if (actual_args == NULL) {
            return NULL;
        }

        Py_INCREF(self->base.sel_self);
        PyTuple_SetItem(actual_args, 0, self->base.sel_self);

        for (i = 0; i < argc; i++) {
            PyObject* v = PyTuple_GET_ITEM(args, i);
            Py_XINCREF(v);
            PyTuple_SET_ITEM(actual_args, i + 1, v);
        }

        result = PyObject_Call(self->callable, actual_args, kwargs);
        Py_DECREF(actual_args);
#else

        if (nargsf & PY_VECTORCALL_ARGUMENTS_OFFSET) {
            /* We're allowed to use args[-1]; */
            PyObject* tmp          = args[-1];
            ((PyObject**)args)[-1] = self->base.sel_self;

            result                 = PyObject_Vectorcall(self->callable, args - 1,
                                                         PyVectorcall_NARGS(nargsf) + 1, kwnames);
            ((PyObject**)args)[-1] = tmp;
        } else {
            /* Need to insert the self argument, but cannot use the args array for that
             * Allocate a new array that's 2 larger, that way we can use
             * PY_VECTORCALL_ARGUMENTS_OFFSET when performing the call.
             */
            PyObject** temp_args =
                malloc((PyVectorcall_NARGS(nargsf) + 2) * sizeof(PyObject*));
            if (temp_args == NULL) {
                PyErr_NoMemory();
                return NULL;
            }
            temp_args[0] = Py_None;
            temp_args[1] = self->base.sel_self;
            memcpy(temp_args + 2, args, PyVectorcall_NARGS(nargsf) * sizeof(PyObject*));

            result = PyObject_Vectorcall(self->callable, temp_args + 1,
                                         (PyVectorcall_NARGS(nargsf) + 1)
                                             | PY_VECTORCALL_ARGUMENTS_OFFSET,
                                         kwnames);
            free(temp_args);
        }
#endif
    }

    if (result && (self->base.sel_self) && (PyObjCObject_Check(self->base.sel_self))
        && ((PyObjCObject*)self->base.sel_self)->flags & PyObjCObject_kUNINITIALIZED) {

        ((PyObjCObject*)self->base.sel_self)->flags &= ~PyObjCObject_kUNINITIALIZED;
    }

    return result;
}

static char*
pysel_default_signature(SEL selector, PyObject* callable)
{
    Py_ssize_t  arg_count;
    char*       result;
    const char* selname = sel_getName(selector);

    if (selname == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "Cannot extract string from selector");
        return NULL;
        // LCOV_EXCL_STOP
    }

    arg_count = 0;

    selname = strchr(selname, ':');
    while (selname) {
        arg_count++;
        selname = strchr(selname + 1, ':');
    }

    /* arguments + return-type + selector */
    result = PyMem_Malloc(arg_count + 4);
    if (result == 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* We want: v@:@... (final sequence of arg_count-1 @-chars) */
    memset(result, _C_ID, arg_count + 3);
    result[2]             = _C_SEL;
    result[arg_count + 3] = '\0';

    if (!PyObjC_returns_value(callable)) {
        result[0] = _C_VOID;
        if (PyErr_Occurred()) {
            PyMem_Free(result);
            return NULL;
        }
    }

    return result;
}

static SEL _Nullable pysel_default_selector(PyObject* callable)
{
    char      buf[1024];
    char*     cur;
    PyObject* name = PyObject_GetAttrString(callable, "__name__");

    if (name == NULL)
        return NULL;

    if (PyUnicode_Check(name)) {
        PyObject* bytes = PyUnicode_AsEncodedString(name, NULL, NULL);
        if (bytes == NULL) {
            return NULL;
        }
        strncpy(buf, PyBytes_AS_STRING(bytes), sizeof(buf) - 1);
        Py_DECREF(bytes);

    } else {
        return NULL;
    }

    if (buf[strlen(buf) - 1] != '_') {
        /* Method name doesn't end with an underscore,
         * the default selector cannot be a multi-segment
         * one. Hence don't try to translate.
         */
        return sel_registerName(buf);
    }

    cur = strchr(buf, '_');
    while (cur != NULL) {
        *cur = ':';
        cur  = strchr(cur, '_');
    }
    return sel_registerName(buf);
}

SEL
PyObjCSelector_DefaultSelector(const char* methname)
{
    char       buf[1024];
    char*      cur;
    Py_ssize_t ln;

    strncpy(buf, methname, sizeof(buf) - 1);
    ln = strlen(buf);

    cur = buf + ln;
    if (cur - buf > 3) {
        if (cur[-1] != '_') {
            return sel_registerName(buf);
        }

        if (cur[-1] == '_' && cur[-2] == '_') {
            cur[-2] = '\0';
            if (PyObjC_IsPythonKeyword(buf)) {
                return sel_registerName(buf);
            }
            cur[-2] = '_';
        }
    }

    /* Skip leading underscores, '_doFoo_' is probably '_doFoo:' in
     * Objective-C, not ':doFoo:'.
     *
     * Also if the name starts and ends with two underscores, return
     * it unmodified. This avoids mangling of Python's special methods.
     *
     * Also don't rewrite two underscores between name elements, such
     * as '__pyobjc__setItem_' -> '__pyobjc__setitem:'
     *
     * Also: when the name starts with two capital letters and an underscore
     * don't replace the underscore, the 'XX_' prefix is a common way to
     * namespace selectors.
     *
     * Both are heuristics and could be the wrong choice, but either
     * form is very unlikely to exist in ObjC code.
     */
    cur = buf;

    if (ln > 5) {
        if (cur[0] == '_' && cur[1] == '_' && cur[ln - 1] == '_' && cur[ln - 2] == '_') {
            return sel_registerName(buf);
        }
    }

    while (*cur == '_') {
        cur++;
    }

    if (isupper(cur[0]) && isupper(cur[1]) && cur[2] == '_') {
        cur += 3;
    }

    /* Replace all other underscores by colons */
    cur = strchr(cur, '_');
    while (cur != NULL) {
        if (cur[1] == '_' && cur[2] && cur[2] != '_' && cur[-1] != '_') {
            /* Don't translate double underscores between
             * name elements.
             *
             * NOTE: cur[-1] is save because we've skipped leading
             * underscores earlier in this function.
             */
            cur += 2;
        } else {
            *cur = ':';
        }
        cur = strchr(cur, '_');
    }
    return sel_registerName(buf);
}

static PyObject* _Nullable pysel_new(PyTypeObject* type __attribute__((__unused__)),
                                     PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"function",   "selector", "signature", "isClassMethod",
                               "isRequired", "isHidden", NULL};
    PyObjCPythonSelector* result;
    PyObject*             callable;
    char*                 signature = NULL;
    char*                 selector  = NULL;
    SEL                   objc_selector;
    int                   class_method = 0;
    int                   required     = 1;
    int                   hidden       = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|yyiii", keywords, &callable,
                                     &selector, &signature, &class_method, &required,
                                     &hidden)) {
        return NULL;
    }

    if (signature != NULL) {
        /* Check if the signature string is valid */
        const char* cur;

        cur = signature;
        while (*cur != '\0') {
            cur = PyObjCRT_SkipTypeSpec(cur);
            if (cur == NULL) {
                PyErr_SetString(PyExc_ValueError, "invalid signature");
                return NULL;
            }
        }
    }

    if (callable != Py_None && !PyCallable_Check(callable)) {
        PyErr_SetString(PyExc_TypeError, "argument 'method' must be callable");
        return NULL;
    }

    if (PyObject_TypeCheck(callable, &PyClassMethod_Type)) {
        /* Special treatment for 'classmethod' instances */
        PyObject* tmp =
            PyObject_CallMethod(callable, "__get__", "OO", Py_None, &PyList_Type);
        if (tmp == NULL) {
            return NULL;
        }

        if (PyObjC_is_pyfunction(tmp)) {
            /* A 'staticmethod' instance, cannot convert */
            Py_DECREF(tmp);
            PyErr_SetString(PyExc_TypeError, "cannot use staticmethod as the "
                                             "callable for a selector.");
            return NULL;
        }

        callable = PyObject_GetAttrString(tmp, "__func__");
        Py_DECREF(tmp);
        if (callable == NULL) {
            return NULL;
        }

    } else {
        Py_INCREF(callable);
    }

    if (selector == NULL) {
        objc_selector = pysel_default_selector(callable);
        if (objc_selector == NULL) {
            return NULL;
        }
    } else {
        objc_selector = sel_registerName(selector);
    }

    result = (PyObjCPythonSelector*)PyObjCSelector_New(callable, objc_selector, signature,
                                                       class_method, nil);
    Py_DECREF(callable);
    if (!result) {
        return NULL;
    }

    if (required) {
        result->base.sel_flags |= PyObjCSelector_kREQUIRED;
    }

    if (hidden) {
        result->base.sel_flags |= PyObjCSelector_kHIDDEN;
    }
    return (PyObject*)result;
}

static PyObject* _Nullable pysel_descr_get(PyObject* _meth, PyObject* _Nullable obj,
                                           PyObject* _Nullable class)
{
    PyObjCPythonSelector* meth = (PyObjCPythonSelector*)_meth;
    PyObjCPythonSelector* result;

    if (meth->base.sel_self != NULL || obj == Py_None) {
        Py_INCREF(meth);
        return (PyObject*)meth;
    }

    /* Bind 'self' */
    if (meth->base.sel_flags & PyObjCSelector_kCLASS_METHOD) {
        if (unlikely(class == NULL)) {
            PyErr_SetString(PyExc_TypeError, "class is NULL");
            return NULL;
        }
        obj = class;

        if (PyType_Check(obj)
            && PyType_IsSubtype((PyTypeObject*)obj, &PyObjCClass_Type)) {
            obj = PyObjCClass_ClassForMetaClass(obj);
        }
    }

    result = PyObject_New(PyObjCPythonSelector, (PyTypeObject*)PyObjCPythonSelector_Type);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    result->base.sel_self             = NULL;
    result->base.sel_methinfo         = NULL;
    result->base.sel_selector         = meth->base.sel_selector;
    result->base.sel_class            = meth->base.sel_class;
    result->base.sel_python_signature = (const char* _Nonnull)NULL;
    result->base.sel_native_signature = (const char* _Nonnull)NULL;
    result->argcount                  = 0;
    result->numoutput                 = 0;
#if PY_VERSION_HEX >= 0x03090000
    result->base.sel_vectorcall = pysel_vectorcall;
#endif

    const char* tmp = PyObjCUtil_Strdup(meth->base.sel_python_signature);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
    result->base.sel_python_signature = tmp;

    if (meth->base.sel_native_signature) {
        result->base.sel_native_signature =
            PyObjCUtil_Strdup(meth->base.sel_native_signature);
        if (result->base.sel_native_signature == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }

    } else {
        result->base.sel_native_signature = NULL;
    }

    result->base.sel_methinfo = PyObjCSelector_GetMetadata((PyObject*)meth);
    if (result->base.sel_methinfo == NULL) {
        PyErr_Clear();
    } else {
        Py_INCREF(result->base.sel_methinfo);
    }
    result->argcount  = meth->argcount;
    result->numoutput = meth->numoutput;

    result->base.sel_self  = obj;
    result->base.sel_flags = meth->base.sel_flags;
    result->callable       = meth->callable;

    if (result->base.sel_self) {
        Py_INCREF(result->base.sel_self);
    }

    if (result->callable) {
        Py_INCREF(result->callable);
    }

    return (PyObject*)result;
}

static void
pysel_dealloc(PyObject* obj)
{
    if (((PyObjCPythonSelector*)obj)->callable != NULL) {
        /* This open codes Py_CLEAR to avoid a nullabity warning */
        PyObject* tmp                          = ((PyObjCPythonSelector*)obj)->callable;
        ((PyObjCPythonSelector*)obj)->callable = (PyObject* _Nonnull)NULL;
        Py_DECREF(tmp);
    }
    sel_dealloc(obj);
}

PyDoc_STRVAR(pysel_get_callable_doc,
             "Returns the python 'function' that implements this method.\n"
             "\n");
static PyObject*
pysel_get_callable(PyObject* _self, void* _Nullable closure __attribute__((__unused__)))
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
    Py_INCREF(self->callable);
    return self->callable;
}

PyDoc_STRVAR(pysel_docstring_doc, "The document string for a method");
static PyObject* _Nullable pysel_docstring(PyObject* _self, void* _Nullable closure
                                           __attribute__((__unused__)))
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;

    return PyObject_GetAttrString(self->callable, "__doc__");
}

static PyGetSetDef pysel_getset[] = {{
                                         .name = "callable",
                                         .get  = pysel_get_callable,
                                         .doc  = pysel_get_callable_doc,
                                     },
                                     {
                                         .name = "__doc__",
                                         .get  = pysel_docstring,
                                         .doc  = pysel_docstring_doc,
                                     },
                                     {
                                         .name = "__signature__",
                                         .get  = PyObjC_callable_signature_get,
                                         .doc  = "inspect.Signaturefor a method",
                                     },
                                     {
                                         .name = NULL /* SENTINEL */
                                     }};

#if PY_VERSION_HEX >= 0x03090000
static PyMemberDef pysel_members[] = {
    {
        .name   = "__vectorcalloffset__",
        .type   = T_PYSSIZET,
        .offset = offsetof(PyObjCPythonSelector, base.sel_vectorcall),
        .flags  = READONLY,
    },
    {
        .name = NULL /* SENTINEL */
    }};
#endif

static PyType_Slot pysel_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&pysel_dealloc},
    {.slot = Py_tp_repr, .pfunc = (void*)&pysel_repr},
    {.slot = Py_tp_hash, .pfunc = (void*)&pysel_hash},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_richcompare, .pfunc = (void*)&pysel_richcompare},
    {.slot = Py_tp_getset, .pfunc = (void*)&pysel_getset},
    {.slot = Py_tp_descr_get, .pfunc = (void*)pysel_descr_get},
#if PY_VERSION_HEX >= 0x03090000
    {.slot = Py_tp_members, .pfunc = (void*)&pysel_members},
    {.slot = Py_tp_call, .pfunc = (void*)&PyVectorcall_Call},
#else
    {.slot = Py_tp_call, .pfunc = (void*)&pysel_call},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec pysel_spec = {
    .name      = "objc.python_selector",
    .basicsize = sizeof(PyObjCPythonSelector),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_HAVE_VECTORCALL,

#elif PY_VERSION_HEX >= 0x03090000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_HAVE_VECTORCALL,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = pysel_slots,
};

const char* _Nullable PyObjCSelector_Signature(PyObject* obj)
{
    PyObjC_Assert(PyObjCSelector_Check(obj), NULL);
    return ((PyObjCSelector*)obj)->sel_python_signature;
}

Class _Nullable PyObjCSelector_GetClass(PyObject* sel)
{
    PyObjC_Assert(PyObjCSelector_Check(sel), Nil);

    return ((PyObjCNativeSelector*)sel)->base.sel_class;
}

SEL
PyObjCSelector_GetSelector(PyObject* sel)
{
    return ((PyObjCSelector*)sel)->sel_selector;
}

int
PyObjCSelector_Required(PyObject* obj)
{
    PyObjC_Assert(PyObjCSelector_Check(obj), -1);

    return (((PyObjCSelector*)obj)->sel_flags & PyObjCSelector_kREQUIRED) != 0;
}

int
PyObjCSelector_IsClassMethod(PyObject* obj)
{
    PyObjC_Assert(PyObjCSelector_Check(obj), -1);

    return (PyObjCSelector_GetFlags(obj) & PyObjCSelector_kCLASS_METHOD) != 0;
}

int
PyObjCSelector_IsHidden(PyObject* obj)
{
    PyObjC_Assert(PyObjCSelector_Check(obj), -1);

    return (PyObjCSelector_GetFlags(obj) & PyObjCSelector_kHIDDEN) != 0;
}

int
PyObjCSelector_GetFlags(PyObject* obj)
{
    PyObjC_Assert(PyObjCSelector_Check(obj), -1);

    return ((PyObjCSelector*)obj)->sel_flags;
}

PyObject* _Nullable PyObjCSelector_Copy(PyObject* selector)
{
    if (PyObjCPythonSelector_Check(selector)) {
        return pysel_descr_get(selector, NULL, NULL);

    } else if (PyObjCNativeSelector_Check(selector)) {
        return objcsel_descr_get(selector, NULL, NULL);

    } else {
        PyErr_SetString(PyExc_TypeError, "copy non-selector");
        return NULL;
    }
}

int
PyObjCSelector_Setup(PyObject* module)
{
    PyObject* tmp = PyType_FromSpec(&sel_spec);
    if (tmp == NULL) {
        return -1;
    }
    PyObjCSelector_Type = tmp;

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "selector", PyObjCSelector_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCSelector_Type);

#if PY_VERSION_HEX < 0x030a0000
    PyObject* bases = PyTuple_New(1);
    if (bases == NULL) {
        return -1;
    }
    PyTuple_SET_ITEM(bases, 0, PyObjCSelector_Type);
    Py_INCREF(PyObjCSelector_Type);
#endif

    tmp = PyType_FromSpecWithBases(&pysel_spec,
#if PY_VERSION_HEX >= 0x030a0000
                                   PyObjCSelector_Type);
#else
                                   bases);
#endif
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
#if PY_VERSION_HEX <= 0x03090000
        Py_CLEAR(bases);
#endif
        return -1; // LCOV_EXCL_LINE
    }
    PyObjCPythonSelector_Type = tmp;

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "python_selector", PyObjCPythonSelector_Type) == -1) {
#if PY_VERSION_HEX <= 0x03090000
        Py_CLEAR(bases);
#endif
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCPythonSelector_Type);

    tmp = PyType_FromSpecWithBases(&objcsel_spec,
#if PY_VERSION_HEX >= 0x030a0000
                                   PyObjCSelector_Type);
#else
                                   bases);
    Py_CLEAR(bases);
#endif
    if (tmp == NULL) {
        return -1;
    }
    PyObjCNativeSelector_Type = tmp;

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "native_selector", PyObjCNativeSelector_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCNativeSelector_Type);

    /* Make it impossible to subclass objc.selector, other than the two subtypes
     * created in this function.
     */
    ((PyTypeObject*)PyObjCSelector_Type)->tp_flags &= ~Py_TPFLAGS_BASETYPE;
    return 0;
}

NS_ASSUME_NONNULL_END
