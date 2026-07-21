/*
 * Manual wrappers for CFBitVector
 */
NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable mod_CFBitVectorCreate(PyObject* meth,
                                                 PyObject* _Nonnull const* _Nonnull args,
                                                 size_t nargs)
{
    Py_buffer      view;
    Py_ssize_t     count;
    CFAllocatorRef allocator;
    CFBitVectorRef vector;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[2], &count) < 0) {
        return NULL;
    }

    PyObject*  buf;
    void*      bytes;
    int        r;
    Py_ssize_t byteCount;

    if (count == -1) {
        byteCount = -1;
    } else {
        byteCount = count / 8;
    }

    r = PyObjC_PythonToCArray(NO, NO, "z", args[1], &bytes, &byteCount, &buf, &view);
    if (r == -1) {
        return NULL;
    }

    if (count == -1) {
        count = byteCount * 8;
    }

    vector = CFBitVectorCreate(allocator, bytes, count);

    PyObjC_FreeCArray(r, &view);
    Py_XDECREF(buf);

    PyObject* result = PyObjC_ObjCToPython(@encode(CFBitVectorRef), &vector);
    if (vector) {
        CFRelease(vector);
    }
    return result;
}

static PyObject* _Nullable mod_CFBitVectorGetBits(PyObject* meth,
                                                  PyObject* _Nonnull const* _Nonnull args,
                                                  size_t nargs)
{
    CFBitVectorRef vector;
    CFRange        range;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFBitVectorRef), args[0], &vector) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFRange), args[1], &range) < 0) {
        return NULL;
    }
    if (args[2] != Py_None) {
        PyErr_Format(PyExc_ValueError, "argument 3: expecting None, got %R", args[2]);
        return NULL;
    }

    PyObject* buffer = PyBytes_FromStringAndSize(NULL, (range.length + 7) / 8);
    if (buffer == NULL) {
        return NULL;
    }
    memset(PyBytes_AsString(buffer), 0, (range.length + 7) / 8);

    CFBitVectorGetBits(vector, range, (unsigned char*)PyBytes_AsString(buffer));
    return buffer;
}

static int
setup_bitvector(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFBitVectorCreate, mod_CFBitVectorCreate) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFBitVectorGetBits, mod_CFBitVectorGetBits) == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
