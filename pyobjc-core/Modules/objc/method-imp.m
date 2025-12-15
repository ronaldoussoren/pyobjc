#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyObject_HEAD
    IMP                    imp;
    PyObjC_CallFunc        callfunc;
    PyObjCMethodSignature* signature;
    SEL                    selector;
    int                    flags;
    vectorcallfunc         vectorcall;
    ffi_cif* _Nullable cif;
} PyObjCIMPObject;

ffi_cif* _Nullable PyObjCIMP_GetCIF(PyObject* self)
{
    assert(PyObjCIMP_Check(self));

    ffi_cif* result;
    Py_BEGIN_CRITICAL_SECTION(self);
    result = ((PyObjCIMPObject*)self)->cif;
    Py_END_CRITICAL_SECTION();

    return result;
}

int
PyObjCIMP_SetCIF(PyObject* self, ffi_cif* _Nullable cif)
{
    assert(PyObjCIMP_Check(self));

    Py_BEGIN_CRITICAL_SECTION(self);
    ((PyObjCIMPObject*)self)->cif = cif;
    Py_END_CRITICAL_SECTION();

    return 0;
}

SEL
PyObjCIMP_GetSelector(PyObject* self)
{
    assert(PyObjCIMP_Check(self));

    return ((PyObjCIMPObject*)self)->selector;
}

IMP _Nullable PyObjCIMP_GetIMP(PyObject* self)
{
    assert(PyObjCIMP_Check(self));

    return ((PyObjCIMPObject*)self)->imp;
}

int
PyObjCIMP_GetFlags(PyObject* self)
{
    assert(PyObjCIMP_Check(self));

    return ((PyObjCIMPObject*)self)->flags;
}

PyObjCMethodSignature* _Nullable PyObjCIMP_GetSignature(PyObject* self)
{
    assert(PyObjCIMP_Check(self));

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
    assert(args != NULL);

    pyself = args[0];
    assert(pyself != NULL);
    assert(self->callfunc != NULL);

    return self->callfunc((PyObject*)self, pyself, args + 1, nargsf - 1);
}

static PyObject* _Nullable imp_vectorcall_simple(PyObject* _self,
                                                 PyObject* const* _Nullable args,
                                                 size_t nargsf,
                                                 PyObject* _Nullable kwnames)
{
    PyObject* pyself;

    assert(((PyObjCIMPObject*)_self)->signature->shortcut_signature);

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

    assert(args != NULL);

    pyself = args[0];
    assert(pyself != NULL);

    return PyObjCFFI_Caller_Simple(_self, pyself, args + 1, nargsf - 1);
}

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
    assert(self->signature != NULL);
    assert(self->signature->signature != NULL);
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
static PyObject* _Nullable imp_is_alloc(PyObject* self __attribute__((__unused__)),
                                        void*     closure __attribute__((__unused__)))
{
    if (PyErr_Warn(PyObjCExc_DeprecationWarning, "isAlloc is always false") < 0) {
        return NULL;
    }

    Py_RETURN_FALSE;
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

    if (unlikely(result == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                // LCOV_EXCL_LINE
    }

    if (((PyObjCIMPObject*)self)->flags & PyObjCSelector_kCLASS_METHOD) {
        r = PyDict_SetItem(result, PyObjCNM_classmethod, Py_True);

    } else {
        r = PyDict_SetItem(result, PyObjCNM_classmethod, Py_False);
    }

    if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
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

static PyMemberDef imp_members[] = {{
                                        .name   = "__vectorcalloffset__",
                                        .type   = T_PYSSIZET,
                                        .offset = offsetof(PyObjCIMPObject, vectorcall),
                                        .flags  = READONLY,
                                    },
                                    {
                                        .name = NULL /* SENTINEL */
                                    }};

static PyType_Slot imp_slots[] = {
    {.slot = Py_tp_repr, .pfunc = (void*)&imp_repr},
    {.slot = Py_tp_dealloc, .pfunc = (void*)&imp_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_getset, .pfunc = (void*)&imp_getset},
    {.slot = Py_tp_methods, .pfunc = (void*)&imp_methods},
    {.slot = Py_tp_call, .pfunc = (void*)&PyVectorcall_Call},
    {.slot = Py_tp_members, .pfunc = (void*)&imp_members},

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
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_HAVE_VECTORCALL,
#endif
    .slots = imp_slots,
};

PyObject* PyObjCIMP_Type;

static PyObject* _Nullable PyObjCIMP_New(IMP imp, SEL selector, PyObjC_CallFunc callfunc,
                                         PyObjCMethodSignature* signature, int flags)
{
    PyObjCIMPObject* result;

    assert(callfunc != NULL);
    assert(signature != NULL);

    result = PyObject_New(PyObjCIMPObject, (PyTypeObject*)PyObjCIMP_Type);
    if (unlikely(result == NULL)) // LCOV_BR_EXCL_LINE
        return NULL;              // LCOV_EXCL_LINE

    result->imp       = imp;
    result->selector  = selector;
    result->callfunc  = callfunc;
    result->signature = signature;
    result->cif       = NULL;
    Py_INCREF(signature);

    result->flags = flags;

    if (likely(signature->shortcut_signature
               && (callfunc == PyObjCFFI_Caller))) { // LCOV_BR_EXCL_LINE
        assert(signature->shortcut_signature);
        result->vectorcall = imp_vectorcall_simple;
    } else {
        result->vectorcall = imp_vectorcall;
    }
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

    assert(args != NULL);

    sel = args[0];

    if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
        return NULL;
    }

    if (unlikely(!PyObjCClass_Check(self))) { // LCOV_BR_EXCL_LINE
        /* AFAIK it is not possible to get an unbound objc.selector
         * for a class method.
         */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError,
                     "Expecting instance of 'objc.objc_class' as 'self', "
                     "got '%s'",
                     Py_TYPE(self)->tp_name);
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = ((IMP (*)(Class, SEL, SEL))objc_msgSend)( // LCOV_BR_EXCL_LINE
                PyObjCClass_GetClass(self),                    // LCOV_BR_EXCL_LINE
                PyObjCSelector_GetSelector(method),            // LCOV_BR_EXCL_LINE
                selector);

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
            retval = NULL;                      // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (unlikely(retval == NULL)) { // LCOV_BR_EXCL_LINE
        /* AFAIK the method in practice never returns NULL */
        // LCOV_EXCL_START
        if (unlikely(PyErr_Occurred())) {
            return NULL;
        }
        Py_RETURN_NONE;
        // LCOV_EXCL_STOP
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

    PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(attr);
    if (unlikely(methinfo == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                  // LCOV_EXCL_LINE
    }

    PyObjC_CallFunc call_func =
        PyObjCSelector_GetCallFunc((PyObjCNativeSelector*)attr, methinfo);
    if (call_func == NULL) {
        Py_DECREF(attr);
        Py_DECREF(methinfo);
        return NULL;
    }

    res = PyObjCIMP_New(retval, selector, call_func, methinfo,
                        PyObjCSelector_GetFlags(attr));
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

    assert(args != NULL);

    sel = args[0];

    if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
        return NULL;
    }

    if (PyObjCClass_Check(self)) {
        super.receiver = (Class _Nonnull)PyObjCClass_GetClass(self);

    } else {
        super.receiver = PyObjCObject_GetObject(self);
    }
    super.super_class = (Class _Nonnull)object_getClass(super.receiver);

    Py_BEGIN_ALLOW_THREADS
        @try {
            retval = ((IMP (*)(struct objc_super*, SEL,     // LCOV_BR_EXCL_LINE
                               SEL))objc_msgSendSuper)(     // LCOV_BR_EXCL_LINE
                &super, PyObjCSelector_GetSelector(method), // LCOV_BR_EXCL_LINE
                selector);                                  // LCOV_BR_EXCL_LINE

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
            retval = NULL;                      // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (unlikely(retval == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (likely(PyErr_Occurred())) {
            return NULL;
        }
        Py_RETURN_NONE;
        // LCOV_EXCL_STOP
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

    PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(attr);
    if (unlikely(methinfo == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(attr);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObjC_CallFunc call_func =
        PyObjCSelector_GetCallFunc((PyObjCNativeSelector*)attr, methinfo);
    if (call_func == NULL) {
        Py_DECREF(attr);
        Py_DECREF(methinfo);
        return NULL;
    }

    res = PyObjCIMP_New(retval, selector, call_func, methinfo,
                        PyObjCSelector_GetFlags(attr));
    Py_DECREF(attr);
    Py_DECREF(methinfo);
    return res;
}

int
PyObjCIMP_SetUp(PyObject* module)
{
    int r;

    PyObjCIMP_Type = PyType_FromSpec(&imp_spec);
    if (unlikely(PyObjCIMP_Type == NULL)) { // LCOV_BR_EXCL_LINE
        return -1;                          // LCOV_EXCL_LINE
    }

    if (unlikely(PyModule_AddObject(module, "IMP", PyObjCIMP_Type)
                 == -1)) { // LCOV_BR_EXCL_LINE
        return -1;         // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCIMP_Type);

    r = PyObjC_RegisterMethodMapping(nil, @selector(instanceMethodForSelector:),
                                     call_instanceMethodForSelector_,
                                     PyObjCUnsupportedMethod_IMP);
    if (unlikely(r == -1)) // LCOV_BR_EXCL_LINE
        return -1;         // LCOV_EXCL_LINE

    r = PyObjC_RegisterMethodMapping(nil, @selector(methodForSelector:),
                                     call_methodForSelector_,
                                     PyObjCUnsupportedMethod_IMP);
    if (unlikely(r == -1)) // LCOV_BR_EXCL_LINE
        return -1;         // LCOV_EXCL_LINE

    return 0;
}

NS_ASSUME_NONNULL_END
