#include "pyobjc.h"
/* XXX: Introduce OC_BuiltinPythonDate to support
 *      secure coding for builtin classes.
 */

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonDate

+ (instancetype _Nullable)dateWithPythonObject:(PyObject*)v
{
    OC_PythonDate* res;

    res = [[self alloc] initWithPythonObject:v];
    return [res autorelease];
}

- (id _Nullable)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil)) // LCOV_BR_EXCL_LINE
        return nil;            // LCOV_EXCL_LINE

    /*
     * First try the most direct way to get a timestamp from a
     * datetime.datetime object. If that fails fall back to using
     * ``value.strftime("%s")`` to fetch the same value (which works
     * with datetime.date).
     */
    PyObject* args[2] = {
        NULL,
        v,
    };
    PyObject* ts = PyObject_VectorcallMethod(PyObjCNM_timestamp, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    if (ts == NULL) {
        if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
            /* This would be a date object. Use strftime instead */
            PyErr_Clear();
            PyObject* fargs[3] = {NULL, v, PyObjCNM_date_format_string};
            PyObject* ts_str   = PyObject_VectorcallMethod(
                  PyObjCNM_strftime, fargs + 1, 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);

            if (ts_str == NULL) {
                return nil;
            }

            ts = PyFloat_FromString(ts_str);
            Py_DECREF(ts_str);
            if (ts == NULL) {
                return nil;
            }
        } else {
            return nil;
        }
    }
    PyObjC_Assert(ts != NULL, nil);
    if (depythonify_c_value(@encode(NSTimeInterval), ts, &timeSinceEpoch) == -1) {
        return nil;
    }

    /* Convert to Cocoa's epoch */
    timeSinceEpoch -= NSTimeIntervalSince1970;

    SET_FIELD_INCREF(value, v);
    return self;
}

- (NSDate*)initWithTimeIntervalSinceReferenceDate:(NSTimeInterval)seconds
{
    self = [self init];
    [self release];
    return (OC_PythonDate*)[[NSDate alloc]
        initWithTimeIntervalSinceReferenceDate:seconds];
}

- (NSTimeInterval)timeIntervalSinceReferenceDate
{
    return timeSinceEpoch;
}

- (PyObject*)__pyobjc_PythonObject__
{
    Py_INCREF(value);
    return value;
}

- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_INCREF(value);
    return value;
}

- (oneway void)release
{
    /* See comment in OC_PythonUnicode */
    if (unlikely(!Py_IsInitialized())) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [super release];
        return;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        @try {
            [super release];
        } @catch (NSException* exc) {
            PyObjC_LEAVE_GIL;
            [exc raise];
        }

    PyObjC_END_WITH_GIL
}

- (void)dealloc
{
    if (unlikely(!Py_IsInitialized())) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [super dealloc];
        return;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        PyObjC_UnregisterObjCProxy(value, self);
        Py_XDECREF(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    /*
     * XXX: somehow be compatible with default NSDate encodeWithCoder
     *      maybe: create a "real" NSDate with the same value,
     *      encode that. When restoring first recreate an NSDate,
     *      then recover the real value (for types 1 and 2 below)
     *
     * Use datetime API and use several "pytype" values:
     * 1. datetime.datetime (exact, with other keys to specify the value)
     * 2. datetime.date (exact, with other keys to specify the value)
     * 3. other (uses PyObjC_encodeWithCoder)
     *
     * As with other classes: non-keyed archives will roundtrip to
     * Cocoa clases for the exact types datetime.date and datetime.datetime.
     */
    if ([coder allowsKeyedCoding]) {
        [coder encodeInt32:3 forKey:@"pytype"];
    } else {
        int pytype = 3;
        [coder encodeValueOfObjCType:@encode(int) at:&pytype];
    }

    PyObjC_encodeWithCoder(value, coder);
}

/*
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
- (void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* v = id_to_python(other);

        SET_FIELD(value, v);

    PyObjC_END_WITH_GIL
}

- (id _Nullable)initWithCoder:(NSCoder*)coder
{
    value = NULL;

    /* See ``-encodeWithCoder:`` for an explanation about the
     * pytype values.
     */
    int pytype;
    if ([coder allowsKeyedCoding]) {
        pytype = [coder decodeInt32ForKey:@"pytype"];

    } else {
        [coder decodeValueOfObjCType:@encode(int) at:&pytype];
    }

    if (pytype != 3) { // LCOV_BR_EXCL
        // LCOV_EXCL_START
        [NSException raise:NSInvalidArgumentException
                    format:@"decoding Python data objects with ptype=%d is not supported",
                           pytype];
        // LCOV_EXCL_STOP
    }

    if (PyObjC_Decoder != NULL) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* cdr = id_to_python(coder);
            if (cdr == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            PyObject* setValue;
            PyObject* selfAsPython = PyObjCObject_New(self, 0, YES);
            if (selfAsPython == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
            setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

            PyObject* v = PyObjC_CallDecoder(cdr, setValue);

            Py_DECREF(cdr);
            Py_DECREF(setValue);
            Py_DECREF(selfAsPython);

            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            SET_FIELD(value, v);
            self = PyObjC_FindOrRegisterObjCProxy(value, self);

        PyObjC_END_WITH_GIL

        return self;

    } else {
        [NSException raise:NSInvalidArgumentException
                    format:@"decoding Python objects is not supported"];
        return nil;
    }
}

- (Class)classForCoder
{
    return [OC_PythonDate class];
}

+ (BOOL)supportsSecureCoding
{
    return NO;
}

@end /* implementation OC_PythonDate */

NS_ASSUME_NONNULL_END
