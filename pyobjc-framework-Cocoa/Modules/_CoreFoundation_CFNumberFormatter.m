static PyObject*
mod_CFNumberFormatterGetValueFromString(PyObject* self __attribute__((__unused__)),
                                        PyObject* args)
{
    PyObject*            py_formatter;
    CFNumberFormatterRef formatter;
    Py_ssize_t           type;
    PyObject*            py_string;
    CFStringRef          string;
    PyObject*            py_range;
    CFRange              range;
    PyObject*            py_buf;
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

    if (!PyArg_ParseTuple(args, "OOOnO", &py_formatter, &py_string, &py_range, &type,
                          &py_buf)) {
        return NULL;
    }
    if (py_buf != Py_None) {
        PyErr_SetString(PyExc_ValueError, "Bad value for buffer");
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFNumberFormatterRef), py_formatter, &formatter)
        < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFStringRef), py_string, &string) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFRange), py_range, &range) < 0) {
        return NULL;
    }

    Boolean rv = FALSE;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFNumberFormatterGetValueFromString(formatter, string, &range, type,
                                                     &buf);

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

        return Py_BuildValue("NNN", PyBool_FromLong(1),
                             PyObjC_ObjCToPython(@encode(CFRange), &range), n);

    } else {
        /* The weird formatting of the string literal is here to
         * silence a codespell warning
         */
        return Py_BuildValue("NO"
                             "O",
                             PyBool_FromLong(0), Py_None, Py_None);
    }
}

static PyObject*
mod_CFNumberFormatterCreateStringWithValue(PyObject* self __attribute__((__unused__)),
                                           PyObject* args)
{
    PyObject*            py_allocator;
    CFAllocatorRef       allocator;
    PyObject*            py_formatter;
    CFNumberFormatterRef formatter;
    Py_ssize_t           type;
    PyObject*            py_value;
    int                  n;
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

    if (!PyArg_ParseTuple(args, "OOnO", &py_allocator, &py_formatter, &type, &py_value)) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFNumberFormatterRef), py_formatter, &formatter)
        < 0) {
        return NULL;
    }

    switch (type) {
    case kCFNumberSInt8Type:
        n = PyObjC_PythonToObjC(@encode(SInt8), py_value, &buf.sint8);
        break;

    case kCFNumberSInt16Type:
        n = PyObjC_PythonToObjC(@encode(SInt16), py_value, &buf.sint16);
        break;

    case kCFNumberSInt32Type:
        n = PyObjC_PythonToObjC(@encode(SInt32), py_value, &buf.sint32);
        break;

    case kCFNumberSInt64Type:
        n = PyObjC_PythonToObjC(@encode(SInt64), py_value, &buf.sint64);
        break;

    case kCFNumberFloat32Type:
        n = PyObjC_PythonToObjC(@encode(Float32), py_value, &buf.float32);
        break;

    case kCFNumberFloat64Type:
        n = PyObjC_PythonToObjC(@encode(Float64), py_value, &buf.float64);
        break;

    case kCFNumberCharType:
        n = PyObjC_PythonToObjC(@encode(char), py_value, &buf.charv);
        break;

    case kCFNumberShortType:
        n = PyObjC_PythonToObjC(@encode(short), py_value, &buf.shortv);
        break;

    case kCFNumberIntType:
        n = PyObjC_PythonToObjC(@encode(int), py_value, &buf.intv);
        break;

    case kCFNumberLongType:
        n = PyObjC_PythonToObjC(@encode(long), py_value, &buf.longv);
        break;

    case kCFNumberLongLongType:
        n = PyObjC_PythonToObjC(@encode(long long), py_value, &buf.longlongv);
        break;

    case kCFNumberFloatType:
        n = PyObjC_PythonToObjC(@encode(float), py_value, &buf.floatv);
        break;

    case kCFNumberDoubleType:
        n = PyObjC_PythonToObjC(@encode(double), py_value, &buf.doublev);
        break;

    case kCFNumberCFIndexType:
        n = PyObjC_PythonToObjC(@encode(CFIndex), py_value, &buf.indexv);
        break;

    default:
        PyErr_SetString(PyExc_ValueError, "number type");
        return NULL;
    }

    if (n == -1) {
        return NULL;
    }

    CFStringRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFNumberFormatterCreateStringWithValue(allocator, formatter, type, &buf);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(CFStringRef), &rv);
    if (rv) {
        CFRelease(rv);
    }
    return result;
}

#define COREFOUNDATION_NUMBERFORMATTER_METHODS                                           \
    {"CFNumberFormatterCreateStringWithValue",                                           \
     (PyCFunction)mod_CFNumberFormatterCreateStringWithValue, METH_VARARGS, NULL},       \
        {"CFNumberFormatterGetValueFromString",                                          \
         (PyCFunction)mod_CFNumberFormatterGetValueFromString, METH_VARARGS, NULL},
