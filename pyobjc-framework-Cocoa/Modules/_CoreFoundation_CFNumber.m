NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable mod_CFNumberGetValue(PyObject* meth,
                                                PyObject* _Nonnull const* _Nonnull args,
                                                size_t nargs)
{
    CFNumberRef number;
    Py_ssize_t  type;
    union {
        SInt8     sint8;
        SInt16    sint16;
        SInt32    sint32;
        SInt64    sint64;
        Float32   float32;
        Float64   float64;
        char      charv;
        short     shortv;
        int       intv;
        long      longv;
        long long longlongv;
        float     floatv;
        double    doublev;
        CFIndex   indexv;
    } buf;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFNumberRef), args[0], &number) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &type) < 0) {
        return NULL;
    }
    if (args[2] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "Bad value for buffer");
        return NULL;
    }

    Boolean rv = FALSE;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFNumberGetValue(number, type, &buf);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (rv) {
        PyObject* n;
        switch (type) {
        case kCFNumberSInt8Type:
            n = PyObjC_ObjCToPython(@encode(SInt8), &buf.sint8);
            break;

        case kCFNumberSInt16Type:
            n = PyObjC_ObjCToPython(@encode(SInt16), &buf.sint16);
            break;

        case kCFNumberSInt32Type:
            n = PyObjC_ObjCToPython(@encode(SInt32), &buf.sint32);
            break;

        case kCFNumberSInt64Type:
            n = PyObjC_ObjCToPython(@encode(SInt64), &buf.sint64);
            break;

        case kCFNumberFloat32Type:
            n = PyObjC_ObjCToPython(@encode(Float32), &buf.float32);
            break;

        case kCFNumberFloat64Type:
            n = PyObjC_ObjCToPython(@encode(Float64), &buf.float64);
            break;

        case kCFNumberCharType:
            n = PyObjC_ObjCToPython(@encode(char), &buf.charv);
            break;

        case kCFNumberShortType:
            n = PyObjC_ObjCToPython(@encode(short), &buf.shortv);
            break;

        case kCFNumberIntType:
            n = PyObjC_ObjCToPython(@encode(int), &buf.intv);
            break;

        case kCFNumberLongType:
            n = PyObjC_ObjCToPython(@encode(long), &buf.longv);
            break;

        case kCFNumberLongLongType:
            n = PyObjC_ObjCToPython(@encode(long long), &buf.longlongv);
            break;

        case kCFNumberFloatType:
            n = PyObjC_ObjCToPython(@encode(float), &buf.floatv);
            break;

        case kCFNumberDoubleType:
            n = PyObjC_ObjCToPython(@encode(double), &buf.doublev);
            break;

        case kCFNumberCFIndexType:
            n = PyObjC_ObjCToPython(@encode(CFIndex), &buf.indexv);
            break;

        default:
            PyErr_SetString(PyExc_ValueError, "number type");
            return NULL;
        }

        return Py_BuildValue("NN", PyBool_FromLong(1), n);

    } else {
        return Py_BuildValue("NO", PyBool_FromLong(0), Py_None);
    }
}

static PyObject* _Nullable mod_CFNumberCreate(PyObject* meth,
                                              PyObject* _Nonnull const* _Nonnull args,
                                              size_t nargs)
{
    CFAllocatorRef allocator;
    Py_ssize_t     type;
    int            n;
    union {
        SInt8     sint8;
        SInt16    sint16;
        SInt32    sint32;
        SInt64    sint64;
        Float32   float32;
        Float64   float64;
        char      charv;
        short     shortv;
        int       intv;
        long      longv;
        long long longlongv;
        float     floatv;
        double    doublev;
        CFIndex   indexv;
    } buf;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &type) < 0) {
        return NULL;
    }

    switch (type) {
    case kCFNumberSInt8Type:
        n = PyObjC_PythonToObjC(@encode(SInt8), args[2], &buf.sint8);
        break;

    case kCFNumberSInt16Type:
        n = PyObjC_PythonToObjC(@encode(SInt16), args[2], &buf.sint16);
        break;

    case kCFNumberSInt32Type:
        n = PyObjC_PythonToObjC(@encode(SInt32), args[2], &buf.sint32);
        break;

    case kCFNumberSInt64Type:
        n = PyObjC_PythonToObjC(@encode(SInt64), args[2], &buf.sint64);
        break;

    case kCFNumberFloat32Type:
        n = PyObjC_PythonToObjC(@encode(Float32), args[2], &buf.float32);
        break;

    case kCFNumberFloat64Type:
        n = PyObjC_PythonToObjC(@encode(Float64), args[2], &buf.float64);
        break;

    case kCFNumberCharType:
        n = PyObjC_PythonToObjC(@encode(char), args[2], &buf.charv);
        break;

    case kCFNumberShortType:
        n = PyObjC_PythonToObjC(@encode(short), args[2], &buf.shortv);
        break;

    case kCFNumberIntType:
        n = PyObjC_PythonToObjC(@encode(int), args[2], &buf.intv);
        break;

    case kCFNumberLongType:
        n = PyObjC_PythonToObjC(@encode(long), args[2], &buf.longv);
        break;

    case kCFNumberLongLongType:
        n = PyObjC_PythonToObjC(@encode(long long), args[2], &buf.longlongv);
        break;

    case kCFNumberFloatType:
        n = PyObjC_PythonToObjC(@encode(float), args[2], &buf.floatv);
        break;

    case kCFNumberDoubleType:
        n = PyObjC_PythonToObjC(@encode(double), args[2], &buf.doublev);
        break;

    case kCFNumberCFIndexType:
        n = PyObjC_PythonToObjC(@encode(CFIndex), args[2], &buf.indexv);
        break;

    default:
        PyErr_SetString(PyExc_ValueError, "number type");
        return NULL;
    }

    if (n == -1) {
        return NULL;
    }

    CFNumberRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFNumberCreate(allocator, type, &buf);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(CFNumberRef), &rv);
    if (rv) {
        CFRelease(rv);
    }
    return result;
}

static int
setup_number(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFNumberGetValue, mod_CFNumberGetValue) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFNumberCreate, mod_CFNumberCreate) == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
