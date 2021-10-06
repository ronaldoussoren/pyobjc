/*
 * Some code that deals with HFSTypeCodes.
 *
 * Needed for backward compatibility with earlier versions of PyObjC.
 */
/* inline definition of PyMac_GetOSType pymactoolbox.h doesn't work in 64-bit mode */

static int
PyMac_GetOSType(PyObject* v, OSType* pr)
{
    uint32_t tmp;
    if (!PyBytes_Check(v) || PyBytes_Size(v) != 4) {
        PyErr_SetString(PyExc_TypeError, "OSType arg must be byte string of 4 chars");
        return 0;
    }
    memcpy((char*)&tmp, PyBytes_AsString(v), 4);
    *pr = (OSType)ntohl(tmp);
    return 1;
}

PyObject*
PyMac_BuildOSType(OSType t)
{
    uint32_t tmp = htonl((uint32_t)t);
    return PyBytes_FromStringAndSize((char*)&tmp, 4);
}

PyDoc_STRVAR(objc_NSFileTypeForHFSTypeCode_doc,
             "NSString *NSFileTypeForHFSTypeCode(OSType hfsTypeCode);");
static PyObject*
objc_NSFileTypeForHFSTypeCode(PyObject* self __attribute__((__unused__)), PyObject* args,
                              PyObject* kwds)
{
    static char* keywords[] = {"hfsTypeCode", NULL};
    PyObject*    result;
    NSString*    oc_result;
    OSType       hfsTypeCode;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "i:NSFileTypeForHFSTypeCode", keywords,
                                     &hfsTypeCode)) {
        PyErr_Clear();
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSFileTypeForHFSTypeCode",
                                         keywords, PyMac_GetOSType, &hfsTypeCode)) {
            return NULL;
        }
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

PyDoc_STRVAR(objc_NSHFSTypeCodeFromFileType_doc,
             "OSType NSHFSTypeCodeFromFileType(NSString *fileType);");
static PyObject*
objc_NSHFSTypeCodeFromFileType(PyObject* self __attribute__((__unused__)), PyObject* args,
                               PyObject* kwds)
{
    static char* keywords[] = {"hfsTypeCode", NULL};
    NSString*    fileType;
    OSType       hfsTypeCode;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&:NSHFSTypeCodeFromFileType", keywords,
                                     PyObjCObject_Convert, &fileType)) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            hfsTypeCode = NSHFSTypeCodeFromFileType(fileType);
        } @catch (NSException* localException) {
            hfsTypeCode = 0;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred())
        return NULL;

    return PyMac_BuildOSType(hfsTypeCode);
}

#define FOUNDATION_TYPECODE_METHODS                                                      \
    {"NSFileTypeForHFSTypeCode", (PyCFunction)objc_NSFileTypeForHFSTypeCode,             \
     METH_VARARGS | METH_KEYWORDS, objc_NSFileTypeForHFSTypeCode_doc},                   \
        {"NSHFSFTypeCodeFromFileType", (PyCFunction)objc_NSHFSTypeCodeFromFileType,      \
         METH_VARARGS | METH_KEYWORDS, objc_NSHFSTypeCodeFromFileType_doc},
