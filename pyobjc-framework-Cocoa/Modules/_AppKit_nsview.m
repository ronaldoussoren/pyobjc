NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable call_NSView_getRectsBeingDrawn_count_(
    PyObject* method, PyObject* self, PyObject* _Nonnull const* _Nonnull arguments,
    size_t nargs)
{
    PyObject*         result;
    struct objc_super super;
    PyObject*         v;
    NSRect*           rects;
    PyObject *        arg1, *arg2;
    NSInteger         count;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1) {
        return NULL;
    }
    arg1 = arguments[0];
    arg2 = arguments[1];

    if (arg1 != Py_None) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }
    if (arg2 != Py_None) {
        PyErr_SetString(PyExc_ValueError, "count must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            ((void (*)(struct objc_super*, SEL, NSRect**, NSInteger*))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), &rects, &count);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    v = PyObjC_CArrayToPython("{_NSRect={_NSPoint=dd}{_NSSize=dd}}", rects, count);
    if (v == NULL)   // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE

    result = Py_BuildValue("Oi", v, count);
    Py_XDECREF(v);

    return result;
}

static int
setup_nsview(PyObject* m __attribute__((__unused__)))
{
    Class classNSView = objc_lookUpClass("NSView");
    if (classNSView == NULL) { // LCOV_BR_EXCL_LINE
        return 0;              // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(classNSView, @selector(getRectsBeingDrawn:count:),
                                     call_NSView_getRectsBeingDrawn_count_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

NS_ASSUME_NONNULL_END
