#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonNumber

+ (instancetype _Nullable)numberWithPythonObject:(PyObject*)v
{
    return [[[self alloc] initWithPythonObject:v] autorelease];
}

- (instancetype _Nullable)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil)) // LCOV_BR_EXCL_LINE
        return nil;            // LCOV_EXCL_LINE

    SET_FIELD_INCREF(value, v);
    return self;
}

- (PyObject*)__pyobjc_PythonObject__
{
    Py_INCREF(value);
    return value;
}

// LCOV_EXCL_START
/* PythonTransient is used in the implementation of
 * methods written in Python, OC_Python* classes
 * don't have such methods.
 */
- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_INCREF(value);
    return value;
}
// LCOV_EXCL_STOP

+ (BOOL)supportsSecureCoding
{
    return NO;
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
        Py_CLEAR(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (const char*)objCType
{
    PyObjC_BEGIN_WITH_GIL
        if (PyFloat_Check(value)) {
            PyObjC_GIL_RETURN(@encode(double));
        } else { // LCOV_EXCL_LINE
            (void)PyLong_AsLongLong(value);
            if (!PyErr_Occurred()) {
                PyObjC_GIL_RETURN(@encode(long long));
            } // LCOV_EXCL_LINE
            PyErr_Clear();
            (void)PyLong_AsUnsignedLongLong(value);
            if (!PyErr_Occurred()) {
                PyObjC_GIL_RETURN(@encode(unsigned long long));
            } // LCOV_EXCL_LINE
            PyErr_Clear();
        }
    PyObjC_END_WITH_GIL

    /* Wrap on overflow */
    return @encode(long long);
}

- (void)getValue:(void*)buffer
{
    const char* encoded = [self objCType];
    int         r;
    PyObjC_BEGIN_WITH_GIL
        r = depythonify_c_value(encoded, value, buffer);
        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE
    PyObjC_END_WITH_GIL
}

- (BOOL)boolValue
{
    int r;
    PyObjC_BEGIN_WITH_GIL
        r = PyObject_IsTrue(value);
        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE
    PyObjC_END_WITH_GIL

    return !!r;
}

- (char)charValue
{
    return (char)[self longLongValue];
}

- (NSDecimal)decimalValue
{
    NSDecimal result;
    int       r;

    PyObjC_BEGIN_WITH_GIL
        r = PyObjC_number_to_decimal(value, &result);

        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

    PyObjC_END_WITH_GIL

    return result;
}

- (double)doubleValue
{
    PyObjC_BEGIN_WITH_GIL
        if (PyFloat_Check(value)) {
            PyObjC_GIL_RETURN(PyFloat_AsDouble(value));
        } // LCOV_EXCL_LINE
    PyObjC_END_WITH_GIL
    return (double)[self longLongValue];
}

- (float)floatValue
{
    return (float)[self doubleValue];
}

- (NSInteger)integerValue
{
    return (NSInteger)[self longLongValue];
}

- (int)intValue
{
    return (int)[self longLongValue];
}

- (long)longValue
{
    return (long)[self longLongValue];
}

- (short)shortValue
{
    return (short)[self longLongValue];
}

- (unsigned char)unsignedCharValue
{
    return (unsigned char)[self unsignedLongLongValue];
}

- (NSUInteger)unsignedIntegerValue
{
    return (NSUInteger)[self unsignedLongLongValue];
}

- (unsigned int)unsignedIntValue
{
    return (unsigned int)[self unsignedLongLongValue];
}

- (unsigned long)unsignedLongValue
{
    return (unsigned long)[self unsignedLongLongValue];
}

- (unsigned short)unsignedShortValue
{
    return (unsigned short)[self unsignedLongLongValue];
}

- (long long)longLongValue
    /* Disable float-cast-overflow checking when running
     * with undefined behaviour sanitizer. The float cast
     * below can result in undefined behaviour but is
     * necessary to match Cocoa semantics.
     */
    __attribute__((no_sanitize("float-cast-overflow")))
{
    long long result;

    PyObjC_BEGIN_WITH_GIL
        if (PyFloat_Check(value)) {
            double float_result = PyFloat_AsDouble(value);
            result              = (long long)float_result;
        } else {
            result = PyLong_AsUnsignedLongLongMask(value);
        }
    PyObjC_END_WITH_GIL
    return result;
}

- (unsigned long long)unsignedLongLongValue
    /* Disable float-cast-overflow checking when running
     * with undefined behaviour sanitizer. The float cast
     * below can result in undefined behaviour but is
     * necessary to match Cocoa semantics.
     */
    __attribute__((no_sanitize("float-cast-overflow")))
{
    unsigned long long result;

    PyObjC_BEGIN_WITH_GIL
        if (PyLong_Check(value)) {
            result = PyLong_AsUnsignedLongLongMask(value);
        } else if (PyFloat_Check(value)) {
            double temp = PyFloat_AsDouble(value);
            if (temp < 0) {
                /* Conversion of negative numbers to
                 * unsigned long long is undefined behaviour,
                 * the code below seems to get the behaviour
                 * we'd like: casting to unsigned long long
                 * behaves similar to casting a signed integer
                 * to unsigned.
                 */
                long long t = (long long)temp;
                result      = (unsigned long long)t;
            } else {
                result = (unsigned long long)temp;
            }
        } else {
            // LCOV_EXCL_START
            @throw [NSException
                exceptionWithName:NSInvalidArgumentException
                           reason:@"Cannot determine objective-C type of this number"
                         userInfo:nil];
            // LCOV_EXCL_STOP
        }
    PyObjC_END_WITH_GIL

    return result;
}

- (NSString*)description
{
    return [self stringValue];
}

- (NSString*)stringValue
{
    PyObject* repr;
    NSString* result = nil;

    PyObjC_BEGIN_WITH_GIL
        repr = PyObject_Repr(value);
        if (repr == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (depythonify_python_object(repr, &result) == -1) {
            Py_DECREF(repr);
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE
        Py_DECREF(repr);
    PyObjC_END_WITH_GIL
    return result;
}

/* NSCoding support */

- (void)encodeWithCoder:(NSCoder*)coder
{
    int use_super = 0;

    PyObjC_BEGIN_WITH_GIL
        if (PyFloat_CheckExact(value)) {
            /* Float is a C double and can be roundtripped using
             * NSNumber.
             */
            use_super = 1;
        } else if (PyLong_CheckExact(value)) {
            /* Encode using super() when the value
             * fits in a long long or unsigned long long,
             * otherwise use the pickle protocol.
             *
             * Logic needs to match that in classForArchiver.
             */
            (void)PyLong_AsLongLong(value);
            if (!PyErr_Occurred()) {
                use_super = 1;
            } else {
                PyErr_Clear();

                (void)PyLong_AsUnsignedLongLong(value);
                if (!PyErr_Occurred()) {
                    use_super = 1;
                } else {
                    PyErr_Clear();
                }
            }
        }
    PyObjC_END_WITH_GIL

    if (use_super) {
        [super encodeWithCoder:coder];
    } else {
        PyObjC_BEGIN_WITH_GIL
            if (PyObjC_encodeWithCoder(value, coder) == -1) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        PyObjC_END_WITH_GIL
    }
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
    PyObjC_BEGIN_WITH_GIL
        PyObject* decoded = PyObjC_decodeWithCoder(coder, self);
        if (decoded == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        SET_FIELD(value, decoded);

        id actual = PyObjC_RegisterObjCProxy(value, self);
        [self release];
        self = actual;

    PyObjC_END_WITH_GIL

    return self;
}

- (BOOL)isEqualToValue:(NSValue*)other
{
    return [self compare:(NSNumber*)other] == NSOrderedSame;
}

- (NSComparisonResult)compare:(NSNumber*)number
{
    /* Rely on -[NSNumber compare:] when the other value
     * is a number and we're not a python int that doesn't
     * fit into a 'long long'.
     *
     * In all other cases use Python's comparison semantics.
     */
    if ([number isKindOfClass:[NSNumber class]]
        && ![number isKindOfClass:[OC_PythonNumber class]]) {
        int use_super = 0;

        PyObjC_BEGIN_WITH_GIL
            if (PyLong_Check(value)) {
                PY_LONG_LONG r;
                r = PyLong_AsLongLong(value);
                if (r == -1 && PyErr_Occurred()) {
                    PyErr_Clear();
                } else { // LCOV_EXCL_LINE
                    use_super = 1;
                }
            }

        PyObjC_END_WITH_GIL;

        if (use_super) {
            return [super compare:number];
        }
    }

    NSComparisonResult rv;
    PyObjC_BEGIN_WITH_GIL
        PyObject* other = id_to_python(number);
        int       r, ok;

        if (other == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        ok = PyObjC_Cmp(value, other, &r);
        Py_DECREF(other);
        if (ok == -1) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (r < 0) {
            rv = NSOrderedAscending;
        } else if (r > 0) {
            rv = NSOrderedDescending;
        } else {
            rv = NSOrderedSame;
        }

    PyObjC_END_WITH_GIL
    return rv;
}

#define COMPARE_METHOD(NAME, OPERATOR)                                                   \
    -(BOOL)NAME : (NSObject* _Nullable)number                                            \
    {                                                                                    \
        BOOL rv;                                                                         \
        PyObjC_BEGIN_WITH_GIL                                                            \
            PyObject* other = id_to_python(number);                                      \
            int       r;                                                                 \
            if (other == NULL) {                                                         \
                PyObjC_GIL_FORWARD_EXC();                                                \
            } /* LCOV_EXCL_LINE */                                                       \
                                                                                         \
            r = PyObject_RichCompareBool(value, other, OPERATOR);                        \
            Py_DECREF(other);                                                            \
            if (r == -1) {                                                               \
                PyObjC_GIL_FORWARD_EXC();                                                \
            } /* LCOV_EXCL_LINE */                                                       \
                                                                                         \
            if (r) {                                                                     \
                rv = YES;                                                                \
            } else { /* LCOV_EXCL_LINE */                                                \
                rv = NO;                                                                 \
            }                                                                            \
                                                                                         \
        PyObjC_END_WITH_GIL                                                              \
        return rv;                                                                       \
    }

COMPARE_METHOD(isEqualTo, Py_EQ)
COMPARE_METHOD(isNotEqualTo, Py_NE)
COMPARE_METHOD(isGreaterThan, Py_GT)
COMPARE_METHOD(isGreaterThanOrEqualTo, Py_GE)
COMPARE_METHOD(isLessThan, Py_LT)
COMPARE_METHOD(isLessThanOrEqualTo, Py_LE)

- (BOOL)isEqualToNumber:(NSNumber*)number
{
    return [self isEqualTo:number];
}

- (Class)classForArchiver
{
    Class result;
    PyObjC_BEGIN_WITH_GIL
        @try {
            if (PyFloat_CheckExact(value)) {
                /* Float is a C double and can be roundtripped using
                 * NSNumber.
                 */
                result = [NSNumber class];
            } else if (PyLong_CheckExact(value)) {
                /* If the value fits inside a long long or
                 * unsigned long long encode as an NSNumber,
                 * else encode as OC_PythonNumber.
                 *
                 * The logic below needs to match that in
                 * encodeWithCoder:
                 */
                (void)PyLong_AsLongLong(value);
                if (!PyErr_Occurred()) {
                    result = [NSNumber class];
                } else { // LCOV_EXCL_LINE
                    PyErr_Clear();

                    (void)PyLong_AsUnsignedLongLong(value);
                    if (!PyErr_Occurred()) {
                        result = [NSNumber class];
                    } else { // LCOV_EXCL_LINE
                        PyErr_Clear();

                        result = [self class];
                    }
                }
            } else { // LCOV_EXCL_LINE
                result = [self class];
            }

            // LCOV_EXCL_START
        } @catch (NSObject* exc) {
            PyObjC_LEAVE_GIL;
            @throw;
        }
        // LCOV_EXCL_STOP
    PyObjC_END_WITH_GIL
    return result;
} // LCOV_EXCL_LINE

- (Class _Nullable)classForKeyedArchiver
{
    return [self classForArchiver];
}

- (Class)classForCoder
{
    return [self classForArchiver];
}

- (id)copy
{
    return [self copyWithZone:NULL];
}

- (id)copyWithZone:(NSZone* _Nullable)__attribute__((__unused__)) zone
{
    id result;
    PyObjC_BEGIN_WITH_GIL
        if (PyLong_CheckExact(value) || PyFloat_CheckExact(value)
            || Py_TYPE(value) == &PyBool_Type) {
            /* The value is immutable, no need to copy */
            result = self;
        } else {
            /* The value might be mutable, perform a copy */
            PyObject* copied = PyObjC_Copy(value);
            if (copied == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

            if (depythonify_python_object(copied, &result) == -1) {
                Py_CLEAR(copied);
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
            Py_CLEAR(copied);
        }

        /* The result of copy should have +1 retainCount */
        [result retain];

    PyObjC_END_WITH_GIL

    return result;
}

@end

NS_ASSUME_NONNULL_END
