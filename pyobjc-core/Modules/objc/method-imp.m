#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyObject_HEAD
    IMP                    imp;
    PyObjC_CallFunc        callfunc;
    PyObjCMethodSignature* signature;
    SEL                    selector;
    int                    flags;
#if PY_VERSION_HEX >= 0x03090000
    vectorcallfunc vectorcall;
#endif
    ffi_cif* _Nullable cif;
} PyObjCIMPObject;

ffi_cif* _Nullable PyObjCIMP_GetCIF(PyObject* self)
{
    PyObjC_Assert(PyObjCIMP_Check(self), NULL);

    ffi_cif* result;
    Py_BEGIN_CRITICAL_SECTION(self);
    result = ((PyObjCIMPObject*)self)->cif;
    Py_END_CRITICAL_SECTION();

    return result;
}

int
PyObjCIMP_SetCIF(PyObject* self, ffi_cif* _Nullable cif)
{
    PyObjC_Assert(PyObjCIMP_Check(self), -1);

    Py_BEGIN_CRITICAL_SECTION(self);
    ((PyObjCIMPObject*)self)->cif = cif;
    Py_END_CRITICAL_SECTION();

    return 0;
}

SEL _Nullable PyObjCIMP_GetSelector(PyObject* self)
{
    PyObjC_Assert(PyObjCIMP_Check(self), NULL);

    return ((PyObjCIMPObject*)self)->selector;
}

IMP _Nullable PyObjCIMP_GetIMP(PyObject* self)
{
    PyObjC_Assert(PyObjCIMP_Check(self), NULL);

    return ((PyObjCIMPObject*)self)->imp;
}

int
PyObjCIMP_GetFlags(PyObject* self)
{
    PyObjC_Assert(PyObjCIMP_Check(self), -1);

    return ((PyObjCIMPObject*)self)->flags;
}

PyObjCMethodSignature* _Nullable PyObjCIMP_GetSignature(PyObject* self)
{
    PyObjC_Assert(PyObjCIMP_Check(self), NULL);

    Py_INCREF(((PyObjCIMPObject*)self)->signature);
    return ((PyObjCIMPObject*)self)->signature;
}

/* ========================================================================= */

#if PY_VERSION_HEX < 0x030a0000
static PyObject* _Nullable imp_new(PyObject* self __attribute__((__unused__)),
                                   PyObject* args __attribute__((__unused__)),
                                   PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "cannot create 'objc.IMP' instances");
    return NULL;
}
#endif

static PyObject* _Nullable imp_vectorcall(PyObject* _self,
                                          PyObject* const* _Nullable args, size_t nargsf,
                                          PyObject* _Nullable kwnames)
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    PyObject*        pyself;
    PyObjC_CallFunc  execute = NULL;
    PyObject*        res;
    PyObject*        pyres;

    if (PyObjC_CheckNoKwnames(_self, kwnames) == -1) {
        return NULL;
    }

    /*
     * The PY_VECTORCALL_ARGUMENTS_OFFSET feature is not used by this function.
     * fetch the raw number of arguments to make it possible to ignore that flag
     * in the rest of the implementation.
     */
    nargsf = PyVectorcall_NARGS(nargsf);

    if (nargsf < 1) {
        PyErr_SetString(PyExc_TypeError, "Missing argument: self");
        return NULL;
    }
    PyObjC_Assert(args != NULL, NULL);

    pyself = args[0];
    PyObjC_Assert(pyself != NULL, NULL);

    execute = self->callfunc;

    pyres = res = execute((PyObject*)self, pyself, args + 1, nargsf - 1);

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

    if (pyres && PyObjCObject_Check(res)) {
        if (self->flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags |= PyObjCObject_kUNINITIALIZED;

        } else if (((PyObjCObject*)pyres)->flags & PyObjCObject_kUNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags &= ~PyObjCObject_kUNINITIALIZED;
            if (pyself && pyself != pyres && PyObjCObject_Check(pyself)
                && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(pyself);
            }
        }
    }

    return res;
}

#if PY_VERSION_HEX >= 0x03090000
static PyObject* _Nullable imp_vectorcall_simple(PyObject* _self,
                                                 PyObject* const* _Nullable args,
                                                 size_t nargsf,
                                                 PyObject* _Nullable kwnames)
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    PyObject*        pyself;
    PyObject*        res;
    PyObject*        pyres;

    PyObjC_Assert(self->signature->shortcut_signature, NULL);

    if (PyObjC_CheckNoKwnames(_self, kwnames) == -1) {
        return NULL;
    }

    /*
     * The PY_VECTORCALL_ARGUMENTS_OFFSET feature is not used by this function.
     * fetch the raw number of arguments to make it possible to ignore that flag
     * in the rest of the implementation.
     */
    nargsf = PyVectorcall_NARGS(nargsf);

    if (nargsf < 1) {
        PyErr_SetString(PyExc_TypeError, "Missing argument: self");
        return NULL;
    }

    PyObjC_Assert(args != NULL, NULL);

    pyself = args[0];
    PyObjC_Assert(pyself != NULL, NULL);

    pyres = res = PyObjCFFI_Caller_Simple(_self, pyself, args + 1, nargsf - 1);

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

    if (pyres && PyObjCObject_Check(res)) {
        if (self->flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags |= PyObjCObject_kUNINITIALIZED;

        } else if (((PyObjCObject*)pyres)->flags & PyObjCObject_kUNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags &= ~PyObjCObject_kUNINITIALIZED;
            if (pyself && pyself != pyres && PyObjCObject_Check(pyself)
                && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(pyself);
            }
        }
    }

    return res;
}
#endif

#if PY_VERSION_HEX < 0x03090000
static PyObject* _Nullable imp_call(PyObject* _self, PyObject* _Nullable args,
                                    PyObject* _Nullable kwds)
{
    if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
        return NULL;
    }
    return imp_vectorcall(_self, PyTuple_ITEMS(args), PyTuple_GET_SIZE(args), NULL);
}
#endif

static PyObject* _Nullable imp_repr(PyObject* _self)
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    return PyUnicode_FromFormat("<IMP %s at %p for %p>", sel_getName(self->selector),
                                self, self->imp);
}

static void
imp_dealloc(PyObject* _self)
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    Py_XDECREF(self->signature);
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(self);
#endif
    PyObject_Free(self);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

PyDoc_STRVAR(imp_signature_doc, "Objective-C signature for the IMP");

static PyObject* _Nullable imp_signature(PyObject* _self,
                                         void*     closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    PyObjC_Assert(self->signature != NULL, NULL);
    PyObjC_Assert(self->signature->signature != NULL, NULL);
    return PyBytes_FromString(self->signature->signature);
}

PyDoc_STRVAR(imp_selector_doc, "Objective-C name for the IMP");

static PyObject* _Nullable imp_selector(PyObject* _self,
                                        void*     closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    return PyBytes_FromString(sel_getName(self->selector));
}

PyDoc_STRVAR(imp_class_method_doc, "True if this is a class method, False otherwise");

static PyObject*
imp_class_method(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;

    if ((self->flags & PyObjCSelector_kCLASS_METHOD) != 0) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

PyDoc_STRVAR(
    imp_is_alloc_doc,
    "True if this is method returns a a freshly allocated object (uninitialized)\n"
    "\n"
    "NOTE: This field is used by the implementation.");
static PyObject*
imp_is_alloc(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    if ((self->flags & PyObjCSelector_kRETURNS_UNINITIALIZED) != 0) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyGetSetDef imp_getset[] = {{
                                       .name = "isAlloc",
                                       .get  = imp_is_alloc,
                                       .doc  = imp_is_alloc_doc,
                                   },
                                   {
                                       .name = "isClassMethod",
                                       .get  = imp_class_method,
                                       .doc  = imp_class_method_doc,
                                   },
                                   {
                                       .name = "signature",
                                       .get  = imp_signature,
                                       .doc  = imp_signature_doc,
                                   },
                                   {
                                       .name = "selector",
                                       .get  = imp_selector,
                                       .doc  = imp_selector_doc,
                                   },
                                   {
                                       .name = "__name__",
                                       .get  = imp_selector,
                                       .doc  = imp_selector_doc,
                                   },
                                   {
                                       .name = "__signature__",
                                       .get  = PyObjC_GetCallableSignature,
                                       .doc  = "inspect.Signature for an IMP",
                                   },
                                   {
                                       .name = NULL /* SENTINEL */
                                   }};

static PyObject* _Nullable imp_metadata(PyObject* self)
{
    PyObject* result = PyObjCMethodSignature_AsDict(((PyObjCIMPObject*)self)->signature);
    int       r;

    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    if (((PyObjCIMPObject*)self)->flags & PyObjCSelector_kCLASS_METHOD) {
        r = PyDict_SetItem(result, PyObjCNM_classmethod, Py_True);

    } else {
        r = PyDict_SetItem(result, PyObjCNM_classmethod, Py_False);
    }

    if (r == -1) {         // LCOV_BR_EXCL_LINE
        Py_DECREF(result); // LCOV_EXCL_LINE
        return NULL;       // LCOV_EXCL_LINE
    }

    if (((PyObjCIMPObject*)self)->flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
        r = PyDict_SetItem(result, PyObjCNM_return_unitialized_object, Py_True);
        if (r == -1) {         // LCOV_BR_EXCL_LINE
            Py_DECREF(result); // LCOV_EXCL_LINE
            return NULL;       // LCOV_EXCL_LINE
        }
    }

    return result;
}

static PyMethodDef imp_methods[] = {{
                                        .ml_name  = "__metadata__",
                                        .ml_meth  = (PyCFunction)imp_metadata,
                                        .ml_flags = METH_NOARGS,
                                        .ml_doc   = "Return metadata for the method",
                                    },
                                    {
                                        .ml_name = NULL /* SENTINEL */
                                    }};

#if PY_VERSION_HEX >= 0x03090000
static PyMemberDef imp_members[] = {{
                                        .name   = "__vectorcalloffset__",
                                        .type   = T_PYSSIZET,
                                        .offset = offsetof(PyObjCIMPObject, vectorcall),
                                        .flags  = READONLY,
                                    },
                                    {
                                        .name = NULL /* SENTINEL */
                                    }};

#endif

static PyType_Slot imp_slots[] = {
    {.slot = Py_tp_repr, .pfunc = (void*)&imp_repr},
    {.slot = Py_tp_dealloc, .pfunc = (void*)&imp_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_getset, .pfunc = (void*)&imp_getset},
    {.slot = Py_tp_methods, .pfunc = (void*)&imp_methods},
#if PY_VERSION_HEX >= 0x03090000
    {.slot = Py_tp_call, .pfunc = (void*)&PyVectorcall_Call},
    {.slot = Py_tp_members, .pfunc = (void*)&imp_members},
#else
    {.slot = Py_tp_call, .pfunc = (void*)&imp_call},
#endif
#if PY_VERSION_HEX < 0x030a0000
    {.slot = Py_tp_new, .pfunc = (void*)&imp_new},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec imp_spec = {
    .name      = "objc.IMP",
    .basicsize = sizeof(PyObjCIMPObject),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION | Py_TPFLAGS_HAVE_VECTORCALL,
#elif PY_VERSION_HEX >= 0x03090000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_HAVE_VECTORCALL,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = imp_slots,
};

PyObject* PyObjCIMP_Type;

static PyObject* _Nullable PyObjCIMP_New(IMP imp, SEL selector, PyObjC_CallFunc callfunc,
                                         PyObjCMethodSignature* signature, int flags)
{
    PyObjCIMPObject* result;

    PyObjC_Assert(callfunc != NULL, NULL);
    PyObjC_Assert(signature != NULL, NULL);

    result = PyObject_New(PyObjCIMPObject, (PyTypeObject*)PyObjCIMP_Type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    result->imp       = imp;
    result->selector  = selector;
    result->callfunc  = callfunc;
    result->signature = signature;
    result->cif       = NULL;
    Py_INCREF(signature);

    result->flags = flags;

#if PY_VERSION_HEX >= 0x03090000
    if (signature && signature->shortcut_signature && (callfunc == PyObjCFFI_Caller)) {
        PyObjC_Assert(signature->shortcut_signature, NULL);
        result->vectorcall = imp_vectorcall_simple;
    } else {
        result->vectorcall = imp_vectorcall;
    }
#endif
    return (PyObject*)result;
}

/* ========================================================================= */

static PyObject* _Nullable call_instanceMethodForSelector_(
    PyObject* method, PyObject* self, PyObject* const* _Nullable args, size_t nargs)
{
    PyObject* sel;
    SEL       selector;
    IMP       retval;
    PyObject* attr;
    PyObject* res;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    PyObjC_Assert(args != NULL, NULL);

    sel = args[0];

    if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
        return NULL;
    }

    if (!PyObjCClass_Check(self)) {
        PyErr_Format(PyExc_TypeError,
                     "Expecting instance of 'objc.objc_class' as 'self', "
                     "got '%s'",
                     Py_TYPE(self)->tp_name);
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = ((IMP(*)(Class, SEL, SEL))objc_msgSend)(
                PyObjCClass_GetClass(self), PyObjCSelector_GetSelector(method), selector);

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            retval = NULL;
        }
    Py_END_ALLOW_THREADS

    if (retval == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }
        Py_RETURN_NONE;
    }

    attr = PyObjCClass_FindSelector(self, selector, NO);
    if (attr == NULL) {
        return NULL;
    }

    /*
     * XXX: what if the method is implemented in Python. We should be able to deal with
     * that!!!
     */

    if (!PyObjCNativeSelector_Check(attr)) {
        PyErr_Format(PyExc_TypeError, "Cannot locate Python representation of %s",
                     sel_getName(selector));
        return NULL;
    }

    if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
        ((PyObjCNativeSelector*)attr)->sel_call_func = PyObjC_FindCallFunc(
            ((PyObjCNativeSelector*)attr)->base.sel_class,
            ((PyObjCNativeSelector*)attr)->base.sel_selector,
            ((PyObjCNativeSelector*)attr)->base.sel_methinfo->signature);
        if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
            return NULL;
        }
    }

    PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(attr);
    if (methinfo == NULL) {
        return NULL;
    }

    res = PyObjCIMP_New(retval, selector, ((PyObjCNativeSelector*)attr)->sel_call_func,
                        methinfo, PyObjCSelector_GetFlags(attr));
    Py_DECREF(attr);
    Py_DECREF(methinfo);
    return res;
}

static PyObject* _Nullable call_methodForSelector_(PyObject* method, PyObject* self,
                                                   PyObject* const* _Nullable args,
                                                   size_t nargs)
{
    PyObject*         sel;
    SEL               selector;
    struct objc_super super;
    IMP               retval;
    PyObject*         attr;
    PyObject*         res;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    PyObjC_Assert(args != NULL, NULL);

    sel = args[0];

    if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
        return NULL;
    }

    if (PyObjCClass_Check(self)) {
        super.receiver = (Class _Nonnull)PyObjCClass_GetClass(self);

    } else {
        super.receiver = (id _Nonnull)PyObjCObject_GetObject(self);
    }
    super.super_class = (Class _Nonnull)object_getClass(super.receiver);

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = ((IMP(*)(struct objc_super*, SEL, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), selector);

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            retval = NULL;
        }
    Py_END_ALLOW_THREADS

    if (retval == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }
        Py_RETURN_NONE;
    }

    if (PyObjCClass_Check(self)) {
        attr = PyObjCClass_FindSelector(self, selector, YES);

    } else {
        attr = PyObjCObject_FindSelector(self, selector);
    }

    if (attr == NULL) {
        return NULL;
    }

    /* FIXME:  We should be able to deal with Python methods as well */

    if (!PyObjCNativeSelector_Check(attr)) {
        PyErr_Format(PyExc_TypeError, "Cannot locate Python representation of %s",
                     sel_getName(selector));
        return NULL;
    }

    /* FIXME: there should be a function for retrieving the call function */
    if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
        ((PyObjCNativeSelector*)attr)->sel_call_func = PyObjC_FindCallFunc(
            ((PyObjCNativeSelector*)attr)->base.sel_class,
            ((PyObjCNativeSelector*)attr)->base.sel_selector,
            ((PyObjCNativeSelector*)attr)->base.sel_methinfo->signature);
        if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
            return NULL;
        }
    }

    PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(attr);
    if (methinfo == NULL) {
        Py_DECREF(attr);
        return NULL;
    }

    res = PyObjCIMP_New(retval, selector, ((PyObjCNativeSelector*)attr)->sel_call_func,
                        methinfo, PyObjCSelector_GetFlags(attr));
    Py_DECREF(attr);
    Py_DECREF(methinfo);
    return res;
}

int
PyObjCIMP_SetUp(PyObject* module)
{
    int r;

    PyObjCIMP_Type = PyType_FromSpec(&imp_spec);
    if (PyObjCIMP_Type == NULL) { // LCOV_BR_EXCL_LINE
        return -1;                // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(module, "IMP", PyObjCIMP_Type) == -1) { // LCOV_BR_EXCL_LINE
        return -1;                                                 // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCIMP_Type);

    r = PyObjC_RegisterMethodMapping(nil, @selector(instanceMethodForSelector:),
                                     call_instanceMethodForSelector_,
                                     PyObjCUnsupportedMethod_IMP);
    if (r == -1)   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    r = PyObjC_RegisterMethodMapping(nil, @selector(methodForSelector:),
                                     call_methodForSelector_,
                                     PyObjCUnsupportedMethod_IMP);
    if (r == -1)   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    return 0;
}

NS_ASSUME_NONNULL_END
