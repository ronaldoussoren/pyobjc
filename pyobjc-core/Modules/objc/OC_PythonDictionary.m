/*
 * NOTE: the implementation uses PyDict_* APIs whenever possible and falls
 * back to the generic PyObject_* APIs otherwise. We don't use the PyMapping_*
 * APIs because those are incomplete(!).
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/*
 * OC_PythonDictionaryEnumerator - Enumerator for Python dictionaries
 *
 * This class implements an NSEnumerator for proxied Python dictionaries.
 */
PyObjC_FINAL_CLASS @interface OC_PythonDictionaryEnumerator : NSEnumerator {
    OC_PythonDictionary* value;
    Py_ssize_t           pos;
    BOOL                 valid;
}
+ (instancetype _Nullable)enumeratorWithWrappedDictionary:(OC_PythonDictionary*)value;
- (id _Nullable)initWithWrappedDictionary:(OC_PythonDictionary*)value;
- (void)dealloc;
- (id _Nullable)nextObject;

@end /* interface OC_PythonDictionaryEnumerator */

@implementation OC_PythonDictionaryEnumerator

+ (instancetype _Nullable)enumeratorWithWrappedDictionary:(OC_PythonDictionary*)v
{
    return [[[self alloc] initWithWrappedDictionary:v] autorelease];
}

- (id _Nullable)initWithWrappedDictionary:(OC_PythonDictionary*)v
{
    self = [super init];
    if (unlikely(self == nil)) // LCOV_BR_EXCL_LINE
        return nil;            // LCOV_EXCL_LINE

    value = [v retain];
    valid = YES;
    pos   = 0;
    return self;
}

- (void)dealloc
{
    [value release];
    [super dealloc];
}

- (id _Nullable)nextObject
{
    id        key = nil;
    int       rv;
    PyObject* pykey = NULL;

    PyObjC_BEGIN_WITH_GIL
        PyObject* dct = [value __pyobjc_PythonObject__];

        Py_BEGIN_CRITICAL_SECTION(dct);

        rv = PyDict_Next(dct, &pos, &pykey, NULL);
        if (rv) {
            Py_XINCREF(pykey);
            valid = YES;
        } else {
            valid = NO;
        }

        Py_END_CRITICAL_SECTION();

        if (!rv) {
            key = nil;

        } else if (pykey == Py_None) {
            key = NSNull_null;
            Py_DECREF(pykey);

        } else {
            if (depythonify_c_value(@encode(id), pykey, &key) == -1) {
                Py_DECREF(dct);
                Py_DECREF(pykey);
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
            Py_DECREF(pykey);
        }

        Py_DECREF(dct);

    PyObjC_END_WITH_GIL

    return key;
}

@end // implementation OC_PythonDictionaryEnumerator

@implementation OC_PythonDictionary

+ (instancetype _Nullable)dictionaryWithPythonObject:(PyObject*)v
{
    assert(v != NULL);
    return [[[self alloc] initWithPythonObject:v] autorelease];
}

- (instancetype _Nullable)initWithPythonObject:(PyObject*)v
{
    assert(v != NULL);
    self = [super init];
    if (unlikely(self == nil)) // LCOV_BR_EXCL_LINE
        return nil;            // LCOV_EXCL_LINE

    SET_FIELD_INCREF(value, v);
    return self;
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
        Py_DECREF(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (PyObject*)__pyobjc_PythonObject__
{
    assert(value != NULL);
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
    assert(value != NULL);
    *cookie = 0;
    Py_INCREF(value);
    return value;
}
// LCOV_EXCL_STOP

- (NSUInteger)count
{
    Py_ssize_t result;
    if (value == NULL) { // LCOV_BR_EXCL_LINE
        return 0;        // LCOV_EXCL_LINE
    }

    PyObjC_BEGIN_WITH_GIL
        if (likely(PyDict_CheckExact(value))) {
            result = PyDict_Size(value);
        } else {
            result = PyObject_Length(value);
        }

    PyObjC_END_WITH_GIL

    if (sizeof(Py_ssize_t) > sizeof(NSUInteger)) {
        if (result > (Py_ssize_t)NSUIntegerMax) {
            return NSUIntegerMax;
        }
    }

    return result;
}

- (id _Nullable)objectForKey:key
{
    PyObject* v;
    PyObject* k;
    id        result;

    if (value == NULL) { // LCOV_BR_EXCL_LINE
        return nil;      // LCOV_EXCL_LINE
    }

    PyObjC_BEGIN_WITH_GIL

        if (unlikely(key == NSNull_null)) {
            Py_INCREF(Py_None);
            k = Py_None;
        } else {
            k = id_to_python(key);
            if (k == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        if (likely(PyDict_CheckExact(value))) {
            int r = PyDict_GetItemRef(value, k, &v);
            switch (r) {
            case -1:
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            case 0:
                PyObjC_GIL_RETURN(nil);
            case 1:
                break;
            }

        } else {
            v = PyObject_GetItem(value, k);
            if (v == nil) {
                if (PyErr_ExceptionMatches(PyExc_KeyError)) {
                    PyErr_Clear();
                    PyObjC_GIL_RETURN(nil);
                } // LCOV_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        Py_DECREF(k);

        if (v == Py_None) {
            result = NSNull_null;

        } else if (unlikely(depythonify_python_object(v, &result) == -1)) {
            Py_DECREF(v);
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE
        Py_DECREF(v);

    PyObjC_END_WITH_GIL

    return result;
}

- (void)setObject:(id)val forKey:(id)key
{
    PyObject* v    = NULL;
    PyObject* k    = NULL;
    id        null = NSNull_null;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(val == null)) {
            Py_INCREF(Py_None);
            v = Py_None;
        } else { // LCOV_EXCL_LINE
            v = id_to_python(val);
            if (unlikely(v == NULL)) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        if (unlikely(key == nil)) {
            Py_INCREF(Py_None);
            k = Py_None;
        } else if (unlikely(key == null)) {
            Py_INCREF(Py_None);
            k = Py_None;

        } else {
            k = id_to_python(key);
            if (k == NULL) {
                Py_XDECREF(v);
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        if (likely(PyDict_CheckExact(value))) {
            if (unlikely(PyDict_SetItem(value, k, v) < 0)) {
                Py_XDECREF(v);
                Py_XDECREF(k);
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

        } else {
            if (unlikely(PyObject_SetItem(value, k, v) < 0)) {
                Py_XDECREF(v);
                Py_XDECREF(k);
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        Py_DECREF(v);
        Py_DECREF(k);

    PyObjC_END_WITH_GIL
}

- (void)removeObjectForKey:(id)key
{
    PyObject* k;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(key == NSNull_null)) {
            Py_INCREF(Py_None);
            k = Py_None;
        } else {
            k = id_to_python(key);
            if (unlikely(k == NULL)) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }

        if (PyDict_CheckExact(value)) {
            if (unlikely(PyDict_DelItem(value, k) < 0)) {
                Py_DECREF(k);
                if (PyErr_ExceptionMatches(PyExc_KeyError)) {
                    PyObjC_LEAVE_GIL;
                    @throw [NSException exceptionWithName:NSInvalidArgumentException
                                                   reason:@"key does not exist"
                                                 userInfo:@{@"key" : key}];
                }
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

        } else {
            if (unlikely(PyObject_DelItem(value, k) < 0)) {
                Py_DECREF(k);
                if (PyErr_ExceptionMatches(PyExc_KeyError)) {
                    PyObjC_LEAVE_GIL;
                    @throw [NSException exceptionWithName:NSInvalidArgumentException
                                                   reason:@"key does not exist"
                                                 userInfo:@{@"key" : key}];
                }
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
        }
        Py_DECREF(k);

    PyObjC_END_WITH_GIL
}

- (NSEnumerator*)keyEnumerator
{
    if (value && PyDict_CheckExact(value)) {
        return [OC_PythonDictionaryEnumerator enumeratorWithWrappedDictionary:self];

    } else {
        NSEnumerator* result = nil;
        PyObjC_BEGIN_WITH_GIL
            PyObject* args[2] = {NULL, value};

            PyObject* keys = PyObject_VectorcallMethod(
                PyObjCNM_keys, args + 1, 1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
            if (keys == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

            PyObject* iter = PyObject_GetIter(keys);
            Py_DECREF(keys);
            if (iter == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE

            result = [OC_PythonEnumerator enumeratorWithPythonObject:iter];

        PyObjC_END_WITH_GIL
        return result;
    }
}

- (id)initWithObjects:(const id _Nonnull[])objects
              forKeys:(const id<NSCopying> _Nonnull[])keys
                count:(NSUInteger)count
{
    /* This implementation is needed for our support for the NSCoding
     * protocol, NSDictionary's initWithCoder: will call this method.
     */
    NSUInteger i;

    if (count > 0 && (keys == NULL || objects == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        [self release];
        return nil;
        // LCOV_EXCL_STOP
    }

    PyObjC_BEGIN_WITH_GIL
        for (i = 0; i < count; i++) {
            PyObject* k;
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

            if (keys[i] == NSNull_null) {
                k = Py_None;
                Py_INCREF(Py_None);

            } else { // LCOV_EXCL_LINE
                k = id_to_python(keys[i]);
                if (k == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                } // LCOV_EXCL_LINE
                if (PyObjCUnicode_Check(k)) {
                    PyObject* k2 = PyObject_Str(k);
                    if (k2 == NULL) { // LCOV_BR_EXCL_LINE
                        // LCOV_EXCL_START
                        Py_DECREF(k);
                        PyObjC_GIL_FORWARD_EXC();
                        // LCOV_EXCL_STOP
                    } // LCOV_EXCL_LINE
                    PyUnicode_InternInPlace(&k2);
                    Py_DECREF(k);
                    k = k2;
                }
            }

            r = PyDict_SetItem(value, k, v);
            Py_DECREF(k);
            Py_DECREF(v);

            if (r == -1) {
                PyObjC_GIL_FORWARD_EXC();
            } // LCOV_EXCL_LINE
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
        PyObject* v = id_to_python(other);

        if (v != NULL) {
            SET_FIELD(value, v);
        }
    PyObjC_END_WITH_GIL
}

- (id _Nullable)initWithCoder:(NSCoder*)coder
{
    int code;
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
        PyObjC_BEGIN_WITH_GIL
            value = PyDict_New();
            if (value == NULL) {          // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

        PyObjC_END_WITH_GIL

        self = [super initWithCoder:coder];
        return self;

    case 2:
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

    default:
        // LCOV_EXCL_START
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"decoding Python objects is not supported"
                                     userInfo:nil];
        // LCOV_EXCL_STOP
    }
}

- (Class)classForCoder
{
    if (value && PyDict_CheckExact(value)) { // LCOV_BR_EXCL_LINE
        return [NSMutableDictionary class];
    } else {
        return [OC_PythonDictionary class];
    }
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_PythonDictionary class];
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSDictionary"];
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    if (PyDict_CheckExact(value)) {
        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:1 forKey:@"pytype"];
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
}

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

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunused-parameter"
- (id)mutableCopyWithZone:(NSZone* _Nullable)zone
{
    NSObject* result;

    PyObjC_BEGIN_WITH_GIL
        PyObject* copy = PyDict_New();
        if (copy == NULL) {           // LCOV_BR_EXCL_LINE
            PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE

        int r = PyDict_Update(copy, value);
        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        } // LCOV_EXCL_LINE

        if (depythonify_python_object( // LCOV_BR_EXCL_LINE
                copy, &result)
            == -1) {
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

@end /* interface OC_PythonDictionary */

NS_ASSUME_NONNULL_END
