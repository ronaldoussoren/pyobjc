#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonData

+ (instancetype _Nullable)dataWithPythonObject:(PyObject*)v
{
    return [[[self alloc] initWithPythonObject:v] autorelease];
}

- (instancetype _Nullable)initWithPythonObject:(PyObject*)v
{
#ifndef USE_STATIC_ANALYZER
    PyObjC_Assert(PyObject_CheckBuffer(v), nil);
#endif

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

- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_INCREF(value);
    return value;
}

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
        Py_XDECREF(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (NSUInteger)length
{
    NSUInteger rval;

    PyObjC_BEGIN_WITH_GIL
        OCReleasedBuffer* temp = [[OCReleasedBuffer alloc] initWithPythonBuffer:value
                                                                       writable:NO];
        if (temp == nil) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_Clear();
            PyObjC_GIL_RETURN(0);
        } // LCOV_EXCL_STOP
        rval = [temp length];
        [temp release];

    PyObjC_END_WITH_GIL
    return rval;
}

- (const void*)bytes
{
    void* rval;

    PyObjC_BEGIN_WITH_GIL
        if (PyBytes_CheckExact(value)) {
            /* Shortcut for bytes objects that avoid creating
             * an OCReleasedBuffer.
             */
            PyObjC_GIL_RETURN(PyBytes_AS_STRING(value));
        }

        OCReleasedBuffer* temp = [[OCReleasedBuffer alloc] initWithPythonBuffer:value
                                                                       writable:NO];
        if (temp == NULL) {           // LCOV_BR_EXCL_LINE
            PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE

        rval = [temp buffer];
        [temp autorelease];

    PyObjC_END_WITH_GIL
    return rval;
}

- (void*)mutableBytes
{
    void* rval;

    PyObjC_BEGIN_WITH_GIL
        OCReleasedBuffer* temp = [[OCReleasedBuffer alloc] initWithPythonBuffer:value
                                                                       writable:YES];
        if (temp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        rval = [temp buffer];
        [temp autorelease];

    PyObjC_END_WITH_GIL
    return rval;
}

- (Class)classForCoder
{
    if (PyBytes_CheckExact(value)) {
        return [NSData class];

    } else if (PyByteArray_CheckExact(value)) {
        return [NSMutableData class];

    } else {
        return [self class];
    }
}

- (Class _Nullable)classForKeyedArchiver
{
    return [self class];
}

- (void)encodeWithCoder:(NSCoder*)coder
{

    PyObjC_BEGIN_WITH_GIL
        @try {
            if (PyBytes_CheckExact(value)) {
                if ([coder allowsKeyedCoding]) {
                    [coder encodeInt32:3 forKey:@"pytype"];
                }
                [super encodeWithCoder:coder];
            } else if (PyByteArray_CheckExact(value)) {
                if ([coder allowsKeyedCoding]) {
                    [coder encodeInt32:4 forKey:@"pytype"];
                }
                [super encodeWithCoder:coder];
            } else {
                if ([coder allowsKeyedCoding]) {
                    [coder encodeInt32:2 forKey:@"pytype"];
                } else {
                    int v = 2;
                    [coder encodeValueOfObjCType:@encode(int) at:&v];
                }

                PyObjC_BEGIN_WITH_GIL
                    if (PyObjC_encodeWithCoder(value, coder) == -1) {
                        PyObjC_GIL_FORWARD_EXC();
                    } // LCOV_EXCL_LINE
                PyObjC_END_WITH_GIL
            }
        } @catch (NSException* exc) {
            PyObjC_LEAVE_GIL;
            @throw;
        }
    PyObjC_END_WITH_GIL
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
    int v;

    if ([coder allowsKeyedCoding]) {
        v = [coder decodeInt32ForKey:@"pytype"];

    } else {
#if  MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_13 && PyObjC_BUILD_RELEASE >= 1013
        /* Old deployment target, modern SDK */
        if (@available(macOS 10.13, *)) {
            [coder decodeValueOfObjCType:@encode(int) at:&v size:sizeof(v)];
        } else {
            CLANG_SUPPRESS
            [coder decodeValueOfObjCType:@encode(int) at:&v];
        }
#elif PyObjC_BUILD_RELEASE >= 1013
        /* Modern deployment target */
        [coder decodeValueOfObjCType:@encode(int) at:&v size:sizeof(v)];
#else
        /* Deployment target is ancient and SDK is old */
        [coder decodeValueOfObjCType:@encode(int) at:&v];
#endif

    }
    if (v == 1) { // LCOV_BR_EXCL_LINE
        /* Backward compatibility:
         * PyObjC up to version 3 used this type to archive instances of bytes
         */
        // LCOV_EXCL_START
        self = [super init];
        if (unlikely(self == nil))
            return nil;

        const void* bytes;
        NSUInteger  length;

        if ([coder allowsKeyedCoding]) {
            bytes = [coder decodeBytesForKey:@"pybytes" returnedLength:&length];

        } else {
            bytes = [coder decodeBytesWithReturnedLength:&length];
        }

        PyObjC_BEGIN_WITH_GIL
            value = PyBytes_FromStringAndSize(bytes, length);
            if (value == NULL) {
                @try {
                    [super release];
                } @catch (NSException* exc) {
                    PyObjC_LEAVE_GIL;
                    [exc raise];
                }
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

        PyObjC_END_WITH_GIL;
        return self;
        // LCOV_EXCL_STOP

    } else if (v == 2) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* decoded = PyObjC_decodeWithCoder(coder, self);
            if (decoded == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

            SET_FIELD(value, decoded);

            id actual = PyObjC_RegisterObjCProxy(value, self);
            if (actual == nil) {
                [self release];
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

            [self release];
            self = actual;

        PyObjC_END_WITH_GIL

        return self;

    } else if (v == 3) {
        return [super initWithCoder:coder];

    } else if (v == 4) {
        PyObjC_BEGIN_WITH_GIL
            value = PyByteArray_FromStringAndSize(NULL, 0);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

        PyObjC_END_WITH_GIL
        return [super initWithCoder:coder];

    } else {
        // LCOV_EXCL_START
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"decoding Python objects is not supported"
                                     userInfo:nil];
        // LCOV_EXCL_STOP
    }
    return self;
}

- (id)initWithData:(NSData*)data
{
    return [self initWithBytes:[data bytes] length:[data length]];
}

- (id)initWithBytes:(const void* _Nullable)bytes length:(NSUInteger)length
{
    PyObjC_BEGIN_WITH_GIL
        if (length > PY_SSIZE_T_MAX) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyExc_ValueError, "Trying to decode a too long data object");
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_STOP

        if (value != NULL && PyByteArray_CheckExact(value)) {
            if (PyByteArray_Resize(value, length) < 0) { // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC();                // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
            memcpy(PyByteArray_AS_STRING(value), bytes, length);
        } else {
            value = PyBytes_FromStringAndSize(bytes, length);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
        }
    PyObjC_END_WITH_GIL

    return self;
}

/* Ensure that we can be unarchived as a generic data object by pure ObjC
 * code.
 */
+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSData"];
}

@end /* implementation OC_PythonData */

NS_ASSUME_NONNULL_END
