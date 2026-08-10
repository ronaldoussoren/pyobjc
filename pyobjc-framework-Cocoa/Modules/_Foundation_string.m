/*
 * The metadata system is rich enough to describe the two methods, but
 * these manual bindings are slightly nicer to use: They automatically
 * resize the output buffer to the correct length instead of returning
 * a buffer that's padded with NUL bytes.
 */

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable call_NSString_getCString_maxLength_range_remainingRange_(
    PyObject* method, PyObject* self, PyObject* _Nonnull const* _Nonnull arguments,
    size_t nargs)
{
    NSRange           aRange;
    NSRange           leftoverRange;
    NSRange*          leftoverPtr;
    char*             buf;
    NSUInteger        maxLength;
    struct objc_super super;
    PyObject*         res;
    PyObject *        buf1, *buf2;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1) {
        return NULL;
    }
    buf1 = arguments[0];
    if (PyObjC_PythonToObjC(@encode(NSUInteger), arguments[1], &maxLength) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(NSRange), arguments[2], &aRange)) {
        return NULL;
    }
    buf2 = arguments[3];

    if (buf1 != Py_None) {
        PyErr_SetString(PyExc_ValueError, "output buffer must be None");
        return NULL;
    }
    if (buf2 != Py_None && buf2 != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "range buffer must be None or NULL");
        return NULL;
    }
    if (buf2 == PyObjC_NULL) {
        leftoverPtr = NULL;
    } else {
        leftoverPtr = &leftoverRange;
    }

    buf = malloc(maxLength + 1);
    if (buf == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            ((void (*)(struct objc_super*, SEL, void*, NSInteger, NSRange,
                       NSRange*))objc_msgSendSuper)(
                &super, @selector(getCString:maxLength:range:remainingRange:), buf,
                maxLength, aRange, leftoverPtr);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        free(buf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    res = PyTuple_New(2);
    if (res == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        free(buf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyTuple_SET_ITEM(res, 0, PyBytes_FromString(buf));
    free(buf);

    if (leftoverPtr != NULL) {
        PyObject* rangeObj = PyObjC_ObjCToPython(@encode(NSRange), &leftoverRange);
        if (rangeObj == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(res);
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyTuple_SET_ITEM(res, 1, rangeObj);
    } else {
        PyTuple_SET_ITEM(res, 1, PyObjC_NULL);
    }
    return res;
}

static PyObject* _Nullable call_NSString_getCString_maxLength_(
    PyObject* method, PyObject* self, PyObject* _Nonnull const* _Nonnull arguments,
    size_t nargs)
{
    char*             buf;
    NSUInteger        maxLength;
    struct objc_super super;
    PyObject*         res;
    PyObject*         py_buf;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1) {
        return NULL;
    }
    py_buf = arguments[0];
    if (PyObjC_PythonToObjC(@encode(NSUInteger), arguments[1], &maxLength) == -1) {
        return NULL;
    }

    if (py_buf != Py_None) {
        PyErr_SetString(PyExc_ValueError, "buffer must be None");
        return NULL;
    }

    buf = malloc(maxLength + 1);
    if (buf == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            ((void (*)(struct objc_super*, SEL, void*, NSUInteger))objc_msgSendSuper)(
                &super, @selector(getCString:maxLength:), buf, maxLength);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        free(buf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* Note that this assumes the string doesn't contain NUL bytes */
    res = PyBytes_FromString(buf);
    free(buf);
    return res;
}

static int
setup_nssstring(PyObject* m __attribute__((__unused__)))
{
    Class classNSString = objc_lookUpClass("NSString");
    if (classNSString == NULL) { // LCOV_BR_EXCL_LINE
        return 0;                // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(
            classNSString, @selector(getCString:maxLength:range:remainingRange:),
            call_NSString_getCString_maxLength_range_remainingRange_,
            PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(classNSString, @selector(getCString:maxLength:),
                                     call_NSString_getCString_maxLength_,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

NS_ASSUME_NONNULL_END
