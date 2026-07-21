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
    if (packedGlyphs == NULL) {
        PyObjC_FreeCArray(bufCode, &view);
        Py_XDECREF(buffer);
        PyErr_NoMemory();
        return NULL;
    }

    NSInteger result = -1;
    Py_BEGIN_ALLOW_THREADS
        @try {
            result = NSConvertGlyphsToPackedGlyphs(glBuf, count, packing, packedGlyphs);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    PyObjC_FreeCArray(bufCode, &view);
    Py_XDECREF(buffer);

    if (PyErr_Occurred()) {
        free(packedGlyphs);
        return NULL;
    }

    if (result == 0) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* pyRes;

    if (result == 0) {
        pyRes = Py_BuildValue("Ns#", PyObjC_ObjCToPython(@encode(NSInteger), &result),
                              packedGlyphs, result - 1);
    } else {
        pyRes = Py_BuildValue("Ns#", PyObjC_ObjCToPython(@encode(NSInteger), &result),
                              packedGlyphs, result);
    }

    free(packedGlyphs);
    return pyRes;
}

#pragma clang diagnostic pop

static int
setup_nsfont(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(NSConvertGlyphsToPackedGlyphs,
                                      m_NSConvertGlyphsToPackedGlyphs)
        == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
