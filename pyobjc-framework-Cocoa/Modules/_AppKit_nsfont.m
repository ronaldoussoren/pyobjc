NS_ASSUME_NONNULL_BEGIN

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

static PyObject* _Nullable m_NSConvertGlyphsToPackedGlyphs(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    NSGlyph*                glBuf;
    int                     bufCode;
    PyObject*               buffer = NULL;
    Py_buffer               view;
    NSInteger               count;
    Py_ssize_t              c;
    NSMultibyteGlyphPacking packing;
    char*                   packedGlyphs;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (args[3] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "packedGlyphs argument must be None");
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(NSInteger), args[1], &count) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(NSMultibyteGlyphPacking), args[2], &packing) == -1) {
        return NULL;
    }

    c       = count;
    bufCode = PyObjC_PythonToCArray(NO, NO, @encode(NSGlyph), args[0], (void**)&glBuf, &c,
                                    &buffer, &view);
    if (bufCode == -1) {
        return NULL;
    }
    count = c;

    packedGlyphs = malloc(count * 4 + 1);
    if (packedGlyphs == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjC_FreeCArray(bufCode, &view);
        Py_XDECREF(buffer);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    NSInteger result = -1;
    Py_BEGIN_ALLOW_THREADS
        @try {
            result = NSConvertGlyphsToPackedGlyphs(glBuf, count, packing, packedGlyphs);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    PyObjC_FreeCArray(bufCode, &view);
    Py_XDECREF(buffer);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        free(packedGlyphs); // LCOV_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* pyRes;

    pyRes = Py_BuildValue("Ns#", PyObjC_ObjCToPython(@encode(NSInteger), &result),
                          packedGlyphs, result);

    free(packedGlyphs);
    return pyRes;
}

#pragma clang diagnostic pop

static int
setup_nsfont(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(NSConvertGlyphsToPackedGlyphs,
                                      m_NSConvertGlyphsToPackedGlyphs)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
