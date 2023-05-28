#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonSet

+ (instancetype _Nullable)setWithPythonObject:(PyObject*)v
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
    if (value == NULL) {
        PyErr_SetString(PyObjCExc_Error, "OC_PythonSet without a value");
        return NULL;
    }
    PyObjC_Assert(value != NULL, ((PyObject* _Nonnull)NULL));
    Py_INCREF(value);
    return value;
}

- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_XINCREF(value);
    return value;
}

+ (BOOL)supportsSecureCoding
{
    return NO;
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
        } @catch (NSObject* exc) {
            PyObjC_LEAVE_GIL;
            @throw;
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
        Py_CLEAR(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

/* NSCoding support */

- (Class)classForCoder
{
    if (PyFrozenSet_CheckExact(value)) {
        return [NSSet class];
    } else if (PyAnySet_CheckExact(value)) {
        return [NSMutableSet class];
    } else {
        return [OC_PythonSet class];
    }
}

- (Class _Nullable)classForKeyedArchiver
{
    return [OC_PythonSet class];
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    int code;
    if (PyAnySet_CheckExact(value)) {
        if (PyFrozenSet_CheckExact(value)) {
            code = 1;
        } else {
            code = 2;
        }

        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:code forKey:@"pytype"];
        }

        [super encodeWithCoder:coder];

    } else {
        code = 3;

        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:code forKey:@"pytype"];
        } else {
            [coder encodeValueOfObjCType:@encode(int) at:&code];
        }

        PyObjC_encodeWithCoder(value, coder);
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

- (id)initWithObjects:(const id*)objects count:(NSUInteger)cnt
{
    NSUInteger i;
    PyObjC_BEGIN_WITH_GIL
        for (i = 0; i < cnt; i++) {
            PyObject* cur;

            if (objects[i] == [NSNull null]) {
                cur = Py_None;
                Py_INCREF(Py_None);
            } else {
                cur = id_to_python(objects[i]);
                if (cur == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }
            }

            if (PySet_Add(value, cur) < 0) {
                Py_DECREF(cur);
                PyObjC_GIL_FORWARD_EXC();
            }
            Py_DECREF(cur);
        }

    PyObjC_END_WITH_GIL
    return self;
}

- (id _Nullable)initWithCoder:(NSCoder*)coder
{
    int code;

    if ([coder allowsKeyedCoding]) {
        code = [coder decodeInt32ForKey:@"pytype"];

    } else {
        [coder decodeValueOfObjCType:@encode(int) at:&code];
    }

    if (code == 1) {
        PyObjC_BEGIN_WITH_GIL
            /* This is safe: PySet_Add can be used
             * with frozenset instances.
             */
            value = PyFrozenSet_New(NULL);
        PyObjC_END_WITH_GIL

        return [super initWithCoder:coder];

    } else if (code == 2) {
        PyObjC_BEGIN_WITH_GIL
            value = PySet_New(NULL);
        PyObjC_END_WITH_GIL

        return [super initWithCoder:coder];
    }

    /* Else: code 3 == set-like class or 0 == no code (older archives) */

    if (PyObjC_Decoder != NULL) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* cdr = id_to_python(coder);
            PyObject* setValue;
            PyObject* selfAsPython;
            PyObject* v;

            if (cdr == NULL) {            // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            }

            selfAsPython = PyObjCObject_New(self, 0, YES);
            if (selfAsPython == NULL) {   // LCOV_BR_EXCL_LINE
                PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
            }
            setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

            v = PyObjC_CallDecoder(cdr, setValue);
            Py_DECREF(cdr);
            Py_DECREF(setValue);
            Py_DECREF(selfAsPython);

            if (v == NULL)
                PyObjC_GIL_FORWARD_EXC();

            SET_FIELD(value, v);

            self = PyObjC_FindOrRegisterObjCProxy(value, self);
        PyObjC_END_WITH_GIL

        return self;

    } else {
        // LCOV_EXCL_START
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"decoding Python objects is not supported"
                                     userInfo:nil];
        // LCOV_EXCL_STOP
    }
}

/*
 * Implementation of the NSMutableSet interface
 */
- (id)copyWithZone:(NSZone* _Nullable)zone
{
    NSObject* result;

    (void)zone;
    if (PyObjC_CopyFunc != NULL && PyObjC_CopyFunc != Py_None) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* tmp = PyObjC_CallCopyFunc(value);
            if (tmp == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            if (depythonify_python_object(tmp, &result) == -1) {
                Py_DECREF(tmp);
                PyObjC_GIL_FORWARD_EXC();
            }
            Py_DECREF(tmp);

        PyObjC_END_WITH_GIL

        [result retain];
        return result;

    } else {
        @throw [NSException exceptionWithName:NSInvalidArgumentException
                                       reason:@"cannot copy python set"
                                     userInfo:nil];
    }
}

- (id)mutableCopyWithZone:(NSZone* _Nullable)zone
{
    NSObject* result;

    (void)zone;
    PyObjC_BEGIN_WITH_GIL

        PyObject* tmp = PySet_New(value);
        if (tmp == NULL) {            // LCOV_BR_EXCL_LINE
            PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
        }

        if (depythonify_python_object(tmp, &result) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(tmp);
            PyObjC_GIL_FORWARD_EXC();
            // LCOV_EXCL_STOP
        }
        Py_DECREF(tmp);

    PyObjC_END_WITH_GIL

    [result retain];
    return result;
}

- (NSArray*)allObjects
{
    NSArray* result;

    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp = PySequence_List(value);
        if (tmp == NULL) {            // LCOV_BR_EXCL_LINE
            PyObjC_GIL_FORWARD_EXC(); // LCOV_EXCL_LINE
        }

        if (depythonify_python_object( // LCOV_BR_EXCL_LINE
                tmp, &result)
            == -1) {
            // LCOV_EXCL_START
            Py_DECREF(tmp);
            PyObjC_GIL_FORWARD_EXC();
            // LCOV_EXCL_STOP
        }

        Py_DECREF(tmp);

    PyObjC_END_WITH_GIL

    return result;
}

- (NSObject* _Nullable)anyObject
{
    NSObject* result;

    PyObjC_BEGIN_WITH_GIL

        if (PyObject_Size(value) == 0) {
            result = nil;
        } else {
            PyObject* tmp;
            PyObject* v;

            tmp = PyObject_GetIter(value);
            if (tmp == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            v = PyIter_Next(tmp);
            Py_DECREF(tmp);
            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            if (depythonify_python_object(v, &result) == -1) {
                Py_DECREF(v);
                PyObjC_GIL_FORWARD_EXC();
            }

            Py_DECREF(v);
        }

    PyObjC_END_WITH_GIL

    return result;
}

- (BOOL)containsObject:(id)anObject
{
    int r;
    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp;

        if (anObject == [NSNull null]) { /* XXX: NSNull_null */
            tmp = Py_None;
            Py_INCREF(Py_None);
        } else {
            tmp = id_to_python(anObject);
            if (tmp == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        r = PySequence_Contains(value, tmp);
        Py_DECREF(tmp);
        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL

    return r ? YES : NO;
}

- (NSUInteger)count
{
    Py_ssize_t result;

    PyObjC_BEGIN_WITH_GIL
        result = PySequence_Size(value);
        if (result == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL

    return (NSUInteger)result;
}

- (NSEnumerator*)objectEnumerator
{
    NSEnumerator* result;
    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp = PyObject_GetIter(value);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        result = [OC_PythonEnumerator enumeratorWithPythonObject:tmp];
        Py_DECREF(tmp);

    PyObjC_END_WITH_GIL

    return result;
}

/* It seems impossible to create an efficient implementation of this method,
 * iteration is basically the only way to fetch the requested object
 */
- (id _Nullable)member:(id)anObject
{
    NSObject* result = nil;

    PyObjC_BEGIN_WITH_GIL
        int       r;
        PyObject* tmpMember;

        if (anObject == [NSNull null]) { /* NSNull_null */
            tmpMember = Py_None;
            Py_INCREF(Py_None);

        } else {
            tmpMember = id_to_python(anObject);
            if (tmpMember == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        r = PySequence_Contains(value, tmpMember);
        if (r == -1) {
            Py_DECREF(tmpMember);
            PyObjC_GIL_FORWARD_EXC();
        }

        if (!r) {
            Py_DECREF(tmpMember);
            result = nil;

        } else {
            /* This sucks, we have to iterate over the contents of the
             * set to find the object we need...
             */
            PyObject* tmp = PyObject_GetIter(value);
            PyObject* v;

            if (tmp == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            while ((v = PyIter_Next(tmp)) != NULL) {
                r = PyObject_RichCompareBool(v, tmpMember, Py_EQ);
                if (r == -1) {
                    Py_DECREF(tmp);
                    Py_DECREF(tmpMember);
                    PyObjC_GIL_FORWARD_EXC();
                }

                if (r) {
                    /* Found the object */
                    if (v == Py_None) {
                        result = [NSNull null];
                    } else {
                        if (depythonify_python_object(v, &result) == -1) {
                            Py_DECREF(tmp);
                            Py_DECREF(tmpMember);
                            PyObjC_GIL_FORWARD_EXC();
                        }
                    }
                    break;
                }
            }

            Py_DECREF(tmp);
            Py_DECREF(tmpMember);
        }

    PyObjC_END_WITH_GIL
    return result;
}

- (void)removeAllObjects
{
    PyObjC_BEGIN_WITH_GIL
        /* Assume an object that conforms to
         * the set interface
         */

        if (PyFrozenSet_CheckExact(value)) {
            PyErr_SetString(PyExc_TypeError, "Cannot mutate a frozenset");
            PyObjC_GIL_FORWARD_EXC();
        }

        PyObject* args[3] = {NULL, value};
        PyObject* r       = PyObject_VectorcallMethod(PyObjCNM_clear, args + 1,
                                                      1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        if (r == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(r);

    PyObjC_END_WITH_GIL
}

- (void)removeObject:(id)anObject
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp = id_to_python(anObject);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (PyFrozenSet_CheckExact(value)) {
            PyErr_SetString(PyExc_TypeError, "Cannot mutate a frozenset");
            PyObjC_GIL_FORWARD_EXC();
        }

        PyObject* args[3] = {NULL, value, tmp};
        PyObject* r       = PyObject_VectorcallMethod(PyObjCNM_discard, args + 1,
                                                      2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(tmp);
        if (r == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(r);

    PyObjC_END_WITH_GIL
}

- (void)addObject:(id)anObject
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp = id_to_python(anObject);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (PyFrozenSet_CheckExact(value)) {
            PyErr_SetString(PyExc_TypeError, "Cannot mutate a frozenset");
            PyObjC_GIL_FORWARD_EXC();
        }

        PyObject* args[3] = {NULL, value, tmp};
        PyObject* r       = PyObject_VectorcallMethod(PyObjCNM_add, args + 1,
                                                      2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(tmp);
        if (r == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(r);

    PyObjC_END_WITH_GIL
}

+ (NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSSet"];
}

@end

NS_ASSUME_NONNULL_END
