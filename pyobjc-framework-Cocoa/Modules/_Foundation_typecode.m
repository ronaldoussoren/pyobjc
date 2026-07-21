/*
 * Some code that deals with HFSTypeCodes.
 *
 * Needed for backward compatibility with earlier versions of PyObjC.
 */

NS_ASSUME_NONNULL_BEGIN

static int
GetOSType(PyObject* v, OSType* pr)
{
    uint32_t tmp;
    if (!PyBytes_Check(v) || PyBytes_Size(v) != 4) {
        PyErr_SetString(PyExc_TypeError, "OSType arg must be byte string of 4 chars");
        return -1;
    }
    memcpy((char*)&tmp, PyBytes_AsString(v), 4);
    *pr = (OSType)ntohl(tmp);
    return 0;
}

static PyObject* _Nullable objc_NSFileTypeForHFSTypeCode(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    PyObject* result;
    NSString* oc_result;
    OSType    hfsTypeCode;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    if (PyLong_Check(args[0])) {
        hfsTypeCode = PyLong_AsInt(args[0]);
        if (PyErr_Occurred()) {
            return NULL;
        }
    } else if (GetOSType(args[0], &hfsTypeCode) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            oc_result = NSFileTypeForHFSTypeCode(hfsTypeCode);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            oc_result = NULL;
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    result = PyObjC_IdToPython(oc_result);
    return result;
}

static int
setup_typecode(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(NSFileTypeForHFSTypeCode,
                                      objc_NSFileTypeForHFSTypeCode)
        == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
