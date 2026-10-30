/*
 * Manual wrapper for varadic functions for CFCalendar.
 *
 * These functions have a non-printf format string. Because all variadic
 * arguments are integers and the number of arguments is trivially derived
 * from the format string these implementations are fairly trivial.
 */
NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable mod_CFCalendarAddComponents(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFCalendarRef  calendar;
    CFAbsoluteTime at;
    CFOptionFlags  flags;
    char*          componentDesc;
    int            params[20];
    Boolean        result;
    int            r;

    if (nargs < 4) {
        PyErr_Format(PyExc_TypeError, "Expecting at least 4 arguments, got %ld", nargs);
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFCalendarRef), args[0], &calendar);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFAbsoluteTime), args[1], &at);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFOptionFlags), args[2], &flags);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(char*), args[3], &componentDesc);
    if (r == -1) {
        return NULL;
    }

    if ((size_t)nargs != 4 + strlen(componentDesc)) {
        PyErr_Format(PyExc_TypeError, "Expecting %ld arguments, got %ld",
                     4 + strlen(componentDesc), nargs);
        return NULL;
    }
    if (nargs > 4 + 20) {
        PyErr_SetString(PyExc_TypeError,
                        "At most 20 characters supported in componentDesc");
        return NULL;
    }

    Py_ssize_t i, len;

    len = strlen(componentDesc);
    for (i = 0; i < len; i++) {
        r = PyObjC_PythonToObjC(@encode(int), args[4 + i], params + i);
        if (r == -1) {
            return NULL;
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CFCalendarAddComponents(calendar, &at, flags, componentDesc,
                                             params[0], params[1], params[2], params[3],
                                             params[4], params[5], params[6], params[7],
                                             params[8], params[9]);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return Py_BuildValue("ON", result ? Py_True : Py_False,
                         PyObjC_ObjCToPython(@encode(CFAbsoluteTime), &at));
}

static PyObject* _Nullable mod_CFCalendarComposeAbsoluteTime(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFCalendarRef  calendar;
    CFAbsoluteTime at;
    char*          componentDesc;
    int            params[20];
    Boolean        result;
    int            r;

    if (nargs < 3) {
        PyErr_Format(PyExc_TypeError, "Expecting at least 3 arguments, got %ld", nargs);
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFCalendarRef), args[0], &calendar);
    if (r == -1) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'at' must be None");
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(char*), args[2], &componentDesc);
    if (r == -1) {
        return NULL;
    }

    if ((size_t)nargs != 3 + strlen(componentDesc)) {
        PyErr_Format(PyExc_TypeError, "Expecting %ld arguments, got %ld",
                     3 + strlen(componentDesc), nargs);
        return NULL;
    }
    if (nargs > 3 + 20) {
        PyErr_SetString(PyExc_TypeError,
                        "At most 20 characters supported in componentDesc");
        return NULL;
    }

    Py_ssize_t i, len;

    len = strlen(componentDesc);
    for (i = 0; i < len; i++) {
        r = PyObjC_PythonToObjC(@encode(int), args[3 + i], params + i);
        if (r == -1) {
            return NULL;
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CFCalendarComposeAbsoluteTime(
                calendar, &at, componentDesc, params[0], params[1], params[2], params[3],
                params[4], params[5], params[6], params[7], params[8], params[9]);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return Py_BuildValue("ON", result ? Py_True : Py_False,
                         PyObjC_ObjCToPython(@encode(CFAbsoluteTime), &at));
}

static PyObject* _Nullable mod_CFCalendarDecomposeAbsoluteTime(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFCalendarRef  calendar;
    CFAbsoluteTime at;
    char*          componentDesc;
    int            params[20];
    Boolean        result;
    int            r;

    if (nargs < 3) {
        PyErr_Format(PyExc_TypeError, "Expecting at least 3 arguments, got %ld", nargs);
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFCalendarRef), args[0], &calendar);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFAbsoluteTime), args[1], &at);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(char*), args[2], &componentDesc);
    if (r == -1) {
        return NULL;
    }

    if (strlen(componentDesc) > 20) {
        PyErr_SetString(PyExc_TypeError,
                        "At most 20 characters supported in componentDesc");
        return NULL;
    }

    if (nargs != 3) {
        if ((size_t)nargs != 3 + strlen(componentDesc)) {
            PyErr_Format(PyExc_TypeError, "Expecting %ld arguments, got %ld",
                         3 + strlen(componentDesc), nargs);
            return NULL;
        }

        Py_ssize_t i, len;

        len = strlen(componentDesc);
        for (i = 0; i < len; i++) {
            if (args[i + 3] != Py_None) {
                PyErr_SetString(PyExc_ValueError, "placeholder must be None");
                return NULL;
            }
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CFCalendarDecomposeAbsoluteTime(
                calendar, at, componentDesc, &params[0], &params[1], &params[2],
                &params[3], &params[4], &params[5], &params[6], &params[7], &params[8],
                &params[9]);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* rv = PyTuple_New(1 + strlen(componentDesc));
    if (rv == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;  // LCOV_EXCL_LINE
    }

    PyObject* b = PyBool_FromLong(result);
    if (b == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }
    PyTuple_SET_ITEM(rv, 0, b);

    Py_ssize_t i, len;
    len = strlen(componentDesc);
    for (i = 0; i < len; i++) {
        PyObject* v = PyLong_FromLong(params[i]);
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(rv);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(rv, i + 1, v);
    }
    return rv;
}

static PyObject* _Nullable mod_CFCalendarGetComponentDifference(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFCalendarRef  calendar;
    CFAbsoluteTime startingAt;
    CFAbsoluteTime resultAt;
    CFOptionFlags  options;
    char*          componentDesc;
    int            params[20];
    Boolean        result;
    int            r;

    if (nargs < 5) {
        PyErr_Format(PyExc_TypeError, "Expecting at least 5 arguments, got %ld", nargs);
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFCalendarRef), args[0], &calendar);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFAbsoluteTime), args[1], &startingAt);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFAbsoluteTime), args[2], &resultAt);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(CFOptionFlags), args[3], &options);
    if (r == -1) {
        return NULL;
    }

    r = PyObjC_PythonToObjC(@encode(char*), args[4], &componentDesc);
    if (r == -1) {
        return NULL;
    }

    if (strlen(componentDesc) > 20) {
        PyErr_SetString(PyExc_TypeError,
                        "At most 20 characters supported in componentDesc");
        return NULL;
    }

    if (nargs != 5) {
        if ((size_t)nargs != 5 + strlen(componentDesc)) {
            PyErr_Format(PyExc_TypeError, "Expecting %ld arguments, got %ld",
                         3 + strlen(componentDesc), nargs);
            return NULL;
        }

        Py_ssize_t i, len;

        len = strlen(componentDesc);
        for (i = 0; i < len; i++) {
            if (args[5 + i] != Py_None) {
                PyErr_SetString(PyExc_ValueError, "placeholder must be None");
                return NULL;
            }
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CFCalendarGetComponentDifference(
                calendar, startingAt, resultAt, options, componentDesc, &params[0],
                &params[1], &params[2], &params[3], &params[4], &params[5], &params[6],
                &params[7], &params[8], &params[9]);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* rv = PyTuple_New(1 + strlen(componentDesc));
    if (rv == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;  // LCOV_EXCL_LINE
    }

    PyObject* b = PyBool_FromLong(result);
    if (b == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }
    PyTuple_SET_ITEM(rv, 0, b);

    Py_ssize_t i, len;
    len = strlen(componentDesc);
    for (i = 0; i < len; i++) {
        PyObject* v = PyLong_FromLong(params[i]);
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(rv);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(rv, i + 1, v);
    }
    return rv;
}

static int
setup_calendar(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFCalendarAddComponents,
                                      mod_CFCalendarAddComponents)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFCalendarComposeAbsoluteTime,
                                      mod_CFCalendarComposeAbsoluteTime)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFCalendarDecomposeAbsoluteTime,
                                      mod_CFCalendarDecomposeAbsoluteTime)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFCalendarGetComponentDifference,
                                      mod_CFCalendarGetComponentDifference)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
