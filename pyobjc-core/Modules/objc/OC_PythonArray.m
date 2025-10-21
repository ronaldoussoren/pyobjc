#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonArray

+ (OC_PythonArray* _Nullable)arrayWithPythonObject:(PyObject*)v
{
    return [[[self alloc] initWithPythonObject:v] autorelease];
}

- (id _Nullable)initWithPythonObject:(PyObject*)v
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
    if (likely(value)) {
        Py_INCREF(value);
        return value;
    } else {
        Py_RETURN_NONE;
    }
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

        /* XXX: This is different from other proxies
         *      to make it easier to hit a race in
         *      proxy-registry.m for testing.
         *
         *      With the current implementation of
         *      proxy-registry (using weak refs) either
         *      order works correctly.
         */
        PyObjC_UnregisterObjCProxy(value, self);
        Py_XDECREF(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (NSUInteger)count
{
    Py_ssize_t result;

    PyObjC_BEGIN_WITH_GIL
        result = PySequence_Length(value);
        if (result < 0) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

    PyObjC_END_WITH_GIL

    /* CPython ensures that 'result' is >= 0 */
    return result;
}

- (id)objectAtIndex:(NSUInteger)idx
{
    PyObject* v;
    id        result;
    int       err;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(idx > PY_SSIZE_T_MAX)) {
            PyErr_SetString(PyExc_IndexError, "out of range");
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        v = PySequence_GetItem(value, (Py_ssize_t)idx);
        if (unlikely(v == NULL)) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (v == Py_None) {
            result = NSNull_null;

        } else {
            err = depythonify_python_object(v, &result);
            if (unlikely(err == -1)) {
                Py_CLEAR(v);
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }
        Py_CLEAR(v);

    PyObjC_END_WITH_GIL

    return result;
}

- (void)replaceObjectAtIndex:(NSUInteger)idx withObject:newValue
{
    PyObject* v;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(idx > PY_SSIZE_T_MAX)) {
            PyErr_SetString(PyExc_IndexError, "out of range");
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (unlikely(newValue == NSNull_null)) {
            Py_INCREF(Py_None);
            v = Py_None;

        } else {
            v = id_to_python(newValue);
            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        if (PySequence_SetItem(value, idx, v) < 0) {
            Py_DECREF(v);
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        Py_DECREF(v);

    PyObjC_END_WITH_GIL;
}

- (void)addObject:(id)anObject
{
    PyObject* v;
    PyObject* w;

    PyObjC_BEGIN_WITH_GIL

        if (unlikely(anObject == NSNull_null)) {
            Py_INCREF(Py_None);
            v = Py_None;
        } else {
            v = id_to_python(anObject);
            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }
        PyObject* args[3] = {NULL, value, v};

        w = PyObject_VectorcallMethod(PyObjCNM_append, args + 1,
                                      2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(v);
        if (unlikely(w == NULL)) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE
        Py_DECREF(w);

    PyObjC_END_WITH_GIL;
}

- (void)insertObject:(id)anObject atIndex:(NSUInteger)idx
{
    PyObject* v;
    PyObject* w;

    if (unlikely(idx > PY_SSIZE_T_MAX)) {
        PyObjC_BEGIN_WITH_GIL
            PyErr_SetString(PyExc_IndexError, "No such index");
            PyObjC_GIL_FORWARD_EXC();
        PyObjC_END_WITH_GIL // LCOV_EXCL_LINE
    } // LCOV_EXCL_LINE

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(anObject == NSNull_null)) {
            Py_INCREF(Py_None);
            v = Py_None;
        } else {
            v = id_to_python(anObject);
            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        PyObject* args[4] = {NULL, value, NULL, v};
        args[2]           = PyLong_FromUnsignedLong(idx);
        if (args[2] == NULL) {        // LCOV_BR_EXCL_LINE
            PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE

        w = PyObject_VectorcallMethod(PyObjCNM_insert, args + 1,
                                      3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(v);
        Py_DECREF(args[2]);

        if (unlikely(w == NULL)) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE
        Py_DECREF(w);

    PyObjC_END_WITH_GIL;
}

- (void)removeLastObject
{
    int        r;
    Py_ssize_t idx;

    PyObjC_BEGIN_WITH_GIL
        idx = PySequence_Length(value);
        if (unlikely(idx == -1)) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (unlikely(idx == 0)) {
            PyErr_SetString(PyExc_ValueError, "pop empty sequence");
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        r = PySequence_DelItem(value, idx - 1);
        if (unlikely(r == -1)) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

    PyObjC_END_WITH_GIL;
}

- (void)removeObjectAtIndex:(NSUInteger)idx
{
    int r;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(idx > PY_SSIZE_T_MAX)) {
            PyErr_SetString(PyExc_IndexError, "No such index");
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        r = PySequence_DelItem(value, (Py_ssize_t)idx);
        if (unlikely(r == -1)) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

    PyObjC_END_WITH_GIL;
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    /*
     * Instances of 'list' and 'tuple' are encoded directly,
     * for other sequences use the generic pickle support code.
     */
    if (PyTuple_CheckExact(value)) {
        /* Encode tuples as type 4 with an explicit length, this allows
         * us to create the tuple during decoding instead of having to
         * create a temporary list. This is needed to get full support
         * for encoding all datastructures, and is needed to pass the
         * unittests for pickle in python2.7.
         *
         * NOTE: older versions used type 1 and no length.
         */
        Py_ssize_t size = PyTuple_Size(value);

        if ([coder allowsKeyedCoding]) {
            if (size > INT_MAX) { // LCOV_BR_EXCL_LINE
                /* Excluded from coverage tests because this would require creating
                 * rather huge tuples, with corresponding memory usage.
                 */
                // LCOV_EXCL_START
                [coder encodeInt32:5 forKey:@"pytype"];
                [coder encodeInt64:(int64_t)PyTuple_Size(value) forKey:@"pylength"];
                // LCOV_EXCL_STOP

            } else { // LCOV_EXCL_LINE
                [coder encodeInt32:4 forKey:@"pytype"];
                [coder encodeInt32:(int32_t)PyTuple_Size(value) forKey:@"pylength"];
            }
        }
        /* Else: When using a non-keyed archiver delegate to superclass unconditionally */

        [super encodeWithCoder:coder];

    } else if (PyList_CheckExact(value)) {
        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:2 forKey:@"pytype"];
        }
        /* Else: When using a non-keyed archiver delegate to superclass unconditionally */

        [super encodeWithCoder:coder];

    } else {
        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:3 forKey:@"pytype"];

        } else {
            int v = 3;
            [coder encodeValueOfObjCType:@encode(int) at:&v];
        }

        PyObjC_BEGIN_WITH_GIL
            if (PyObjC_encodeWithCoder(value, coder) == -1) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        PyObjC_END_WITH_GIL
    }
}

- (Class)classForCoder
{
    if (PyTuple_CheckExact(value)) {
        return [NSArray class];

    } else if (PyList_CheckExact(value)) {
        return [NSMutableArray class];

    } else {
        return [OC_PythonArray class];
    }
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_PythonArray class];
}

- (id)initWithObjects:(const id _Nonnull[])objects count:(NSUInteger)count
{
    /* initWithObjects:count: is primarily present to support the NSCoding
     * protocol of NSArray.
     */
    NSUInteger i;

    if (count > 0 && objects == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [self release];
        return nil;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        if (PyTuple_CheckExact(value) // LCOV_BR_EXCL_LINE
            && (NSUInteger)PyTuple_Size(value) == count) {
            for (i = 0; i < count; i++) {
                PyObject* v;

                if (objects[i] == NSNull_null) {
                    v = Py_None;
                    Py_INCREF(Py_None);

                } else {
                    v = id_to_python(objects[i]);
                    if (v == NULL) {
                        PyObjC_GIL_FORWARD_EXC();
                    } // LCOV_EXCL_LINE
                }

                /* XXX: Can this every be true? */
                if (PyTuple_GET_ITEM(value, i) != NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    /* use temporary object to avoid race condition */
                    PyObject* t = PyTuple_GET_ITEM(value, i);
                    PyTuple_SET_ITEM(value, i, NULL);
                    Py_DECREF(t);
                    // LCOV_EXCL_STOP
                } // LCOV_EXCL_LINE
                PyTuple_SET_ITEM(value, i, v);
            }
        } else {

            for (i = 0; i < count; i++) {
                PyObject* v;
                int       r;

                if (objects[i] == NSNull_null) {
                    v = Py_None;
                    Py_INCREF(Py_None);

                } else {
                    v = id_to_python(objects[i]);
                    if (v == NULL) {
                        PyObjC_GIL_FORWARD_EXC();
                    } // LCOV_EXCL_LINE
                }

                r = PyList_Append(value, v);
                if (r == -1) {                // LCOV_BR_EXCL_LINE
                    PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
                } // LCOV_EXCL_LINE

                Py_DECREF(v);
            }
        }

    PyObjC_END_WITH_GIL
    return self;
}

/*
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
- (void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        /* XXX: What if "other" cannot be proxied? */
        PyObject* v = id_to_python(other);
        SET_FIELD(value, v);

    PyObjC_END_WITH_GIL
}

- (id _Nullable)initWithCoder:(NSCoder*)coder
{
    PyObject*       t;
    int             code;
    Py_ssize_t      size;
    OC_PythonArray* tmpVal;

    if ([coder allowsKeyedCoding]) {
        code = [coder decodeInt32ForKey:@"pytype"];

    } else {
#if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_13 && PyObjC_BUILD_RELEASE >= 1013
        /* Old deployment target, modern SDK */
        if (@available(macOS 10.13, *)) {
            [coder decodeValueOfObjCType:@encode(int) at:&code size:sizeof(code)];
        } else {
            CLANG_SUPPRESS
            [coder decodeValueOfObjCType:@encode(int) at:&code];
        }
#elif PyObjC_BUILD_RELEASE >= 1013
        /* Modern deployment target */
        [coder decodeValueOfObjCType:@encode(int) at:&code size:sizeof(code)];
#else
        /* Deployment target is ancient and SDK is old */
        [coder decodeValueOfObjCType:@encode(int) at:&code];
#endif
    }

    switch (code) { // LCOV_BR_EXCL_LINE
    case 1:
        /* This code was used by some previous versions of PyObjC
         * (before 2.2) and is kept around for backward compatibility.
         *
         * Excluded from coverage testing because I don't have
         * old archives that can be used for testing.
         */
        // LCOV_EXCL_START
        PyObjC_BEGIN_WITH_GIL
            value = PyList_New(0);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

        PyObjC_END_WITH_GIL

        tmpVal = [super initWithCoder:coder];
        if (tmpVal == nil) {
            return nil;
        }
        assert(tmpVal == self);
        self = tmpVal;

        PyObjC_BEGIN_WITH_GIL
            t     = value;
            value = PyList_AsTuple(t);
            Py_DECREF(t);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
        PyObjC_END_WITH_GIL
        return self;
        // LCOV_EXCL_STOP

    case 2:
        PyObjC_BEGIN_WITH_GIL
            value = PyList_New(0);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

        PyObjC_END_WITH_GIL

        tmpVal = [super initWithCoder:coder];
        assert(tmpVal == self);
        return tmpVal;

    case 3:
        PyObjC_BEGIN_WITH_GIL
            value = PyList_New(0);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

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

    case 4:
        /* tuple with less than MAX_INT elements */
        if ([coder allowsKeyedCoding]) {
            size = [coder decodeInt32ForKey:@"pylength"];

        } else {
            int isize;
#if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_13 && PyObjC_BUILD_RELEASE >= 1013
            /* Old deployment target, modern SDK */
            if (@available(macOS 10.13, *)) {
                [coder decodeValueOfObjCType:@encode(int) at:&isize size:sizeof(isize)];
            } else {
                CLANG_SUPPRESS
                [coder decodeValueOfObjCType:@encode(int) at:&isize];
            }
#elif PyObjC_BUILD_RELEASE >= 1013
            /* Modern deployment target */
            [coder decodeValueOfObjCType:@encode(int) at:&isize size:sizeof(isize)];
#else
            /* Deployment target is ancient and SDK is old */
            [coder decodeValueOfObjCType:@encode(int) at:&isize];
#endif
            size = isize;
        }

        PyObjC_BEGIN_WITH_GIL
            value = PyTuple_New(size);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

        PyObjC_END_WITH_GIL

        tmpVal = [super initWithCoder:coder];
        assert(tmpVal == self);
        return tmpVal;

    case 5:
        /* tuple with more than MAX_INT elements */
        /* Excluded from coverage check because testing this would
         * require creating too large tuples, with corresponding memory use
         */
        // LCOV_EXCL_START
        if ([coder allowsKeyedCoding]) {
            size = [coder decodeInt64ForKey:@"pylength"];
        } else {
#if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_13 && PyObjC_BUILD_RELEASE >= 1013
            /* Old deployment target, modern SDK */
            if (@available(macOS 10.13, *)) {
                [coder decodeValueOfObjCType:@encode(long long)
                                          at:&size
                                        size:sizeof(size)];
            } else {
                CLANG_SUPPRESS
                [coder decodeValueOfObjCType:@encode(long long) at:&size];
            }
#elif PyObjC_BUILD_RELEASE >= 1013
            /* Modern deployment target */
            [coder decodeValueOfObjCType:@encode(long long) at:&size size:sizeof(size)];
#else
            /* Deployment target is ancient and SDK is old */
            [coder decodeValueOfObjCType:@encode(long long) at:&size];
#endif
        }

        PyObjC_BEGIN_WITH_GIL
            value = PyTuple_New(size);
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            }

        PyObjC_END_WITH_GIL
        tmpVal = [super initWithCoder:coder];
        assert(tmpVal == self);
        return tmpVal;
        // LCOV_EXCL_STOP

    default:
        // LCOV_EXCL_START
        [self release];
        @throw [NSException
            exceptionWithName:NSInvalidArgumentException
                       reason:[NSString
                                  stringWithFormat:
                                      @"Cannot decode OC_PythonArray with type-id %d",
                                      code]
                     userInfo:nil];
        // LCOV_EXCL_STOP
    }
}

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunused-parameter"

- (id)copyWithZone:(NSZone* _Nullable)zone
{
    NSObject* result;
    PyObjC_BEGIN_WITH_GIL

        PyObject* copy = PyObjC_Copy(value);
        if (copy == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (depythonify_python_object(copy, &result) == -1) {
            Py_DECREF(copy);
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        Py_DECREF(copy);

    PyObjC_END_WITH_GIL

    [result retain];
    return result;
}

- (id)mutableCopyWithZone:(NSZone* _Nullable)zone
{
    NSObject* result;
    PyObjC_BEGIN_WITH_GIL
        PyObject* copy = PySequence_List(value);
        if (copy == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (depythonify_python_object(copy, &result) == -1) { // LCOV_BR_EXCL_LINE
            /* Should never fail, 'copy' is an instance of PyList_Type */
            // LCOV_EXCL_START
            Py_DECREF(copy);
            PyObjC_GIL_FORWARD_EXC();
            // LCOV_EXCL_STOP
        } // LCOV_EXCL_LINE

        Py_DECREF(copy);

    PyObjC_END_WITH_GIL

    [result retain];
    return result;
}
#pragma clang diagnostic pop

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSArray"];
}

@end /* implementation OC_PythonArray */

NS_ASSUME_NONNULL_END
