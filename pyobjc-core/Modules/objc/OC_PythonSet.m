#include "pyobjc.h"


@implementation OC_PythonSet

+ (instancetype)setWithPythonObject:(PyObject*)v
{
    OC_PythonSet* res;

    res = [[OC_PythonSet alloc] initWithPythonObject:v];
    [res autorelease];
    return res;
}

- (id)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil)) return nil;

    SET_FIELD_INCREF(value, v);
    return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
    Py_INCREF(value);
    return value;
}

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_INCREF(value);
    return value;
}

-(BOOL)supportsWeakPointers {
    return YES;
}

-(oneway void)release
{
    /* See comment in OC_PythonUnicode */
    PyObjC_BEGIN_WITH_GIL
        [super release];

    PyObjC_END_WITH_GIL
}

-(void)dealloc
{
    PyObjC_BEGIN_WITH_GIL
        PyObjC_UnregisterObjCProxy(value, self);
        Py_XDECREF(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}


/* NSCoding support */

-(Class)classForCoder
{
    if (PyAnySet_CheckExact(value)) {
        return [NSSet class];
    } else {
        return [OC_PythonSet class];
    }
}

-(Class)classForKeyedArchiver
{
    return [OC_PythonSet class];
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    int code;
    if (PyAnySet_CheckExact(value)) {
        if (PyFrozenSet_Check(value)) {
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
-(void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* v = PyObjC_IdToPython(other);

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
                    cur = PyObjC_IdToPython(objects[i]);
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

- (id)initWithCoder:(NSCoder*)coder
{
    int code;

    if ([coder allowsKeyedCoding]) {
        code = [coder decodeInt32ForKey:@"pytype"];

    } else {
        [coder decodeValueOfObjCType:@encode(int) at:&code];
    }

    if (code == 1) {
        value = PyFrozenSet_New(NULL);
        return [super initWithCoder:coder];
    } else if (code == 2) {
        value = PySet_New(NULL);
        return [super initWithCoder:coder];
    }

    /* Else: code 3 == set-like class or 0 == no code (older archives) */

    if (PyObjC_Decoder != NULL) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* cdr = PyObjC_IdToPython(coder);
            PyObject* setValue;
            PyObject* selfAsPython;
            PyObject* v;

            if (cdr == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            selfAsPython = PyObjCObject_New(self, 0, YES);
            setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

            v = PyObject_CallFunction(PyObjC_Decoder, "OO", cdr, setValue);
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


/*
 * Implementation of the NSMutableSet interface
 */
-(id)copyWithZone:(NSZone*)zone
{
    NSObject* result;

    (void)zone;
    if (PyObjC_CopyFunc != NULL) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* tmp = PyObject_CallFunction(PyObjC_CopyFunc, "O", value);
            if (tmp == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            result = PyObjC_PythonToId(tmp);
            Py_DECREF(tmp);
            if (PyErr_Occurred()) {
                PyObjC_GIL_FORWARD_EXC();
            }

            [result retain];

        PyObjC_END_WITH_GIL

        return result;

    } else {
        [NSException raise:NSInvalidArgumentException
                    format:@"cannot copy python set"];
        return nil;
    }
}

-(id)mutableCopyWithZone:(NSZone*)zone
{
    NSObject* result;

    (void)zone;
    PyObjC_BEGIN_WITH_GIL

        PyObject* tmp = PySet_New(value);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        result = PyObjC_PythonToId(tmp);
        Py_DECREF(tmp);
        if (PyErr_Occurred()) {
            PyObjC_GIL_FORWARD_EXC();
        }

        [result retain];

    PyObjC_END_WITH_GIL

    return result;
}

-(NSArray*)allObjects
{
    NSArray* result;

    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp = PySequence_List(value);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        result = (NSArray*)PyObjC_PythonToId(tmp);
        Py_DECREF(tmp);
        if (PyErr_Occurred()) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL

    return result;
}

-(NSObject*)anyObject
{
    NSObject* result;

    PyObjC_BEGIN_WITH_GIL

        if (PySet_Size(value) == 0) {
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

            result = PyObjC_PythonToId(v);
            Py_DECREF(v);
            if (PyErr_Occurred()) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

    PyObjC_END_WITH_GIL

    return result;
}

-(BOOL)containsObject:(id)anObject
{
    int r;
    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp;

        if (anObject == [NSNull null]) {
            tmp = Py_None;
            Py_INCREF(Py_None);
        } else {
            tmp = PyObjC_IdToPython(anObject);
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

    return r?YES:NO;
}

-(NSUInteger)count
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

-(NSEnumerator*)objectEnumerator
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
 * iteration is basicly the only way to fetch the requested object
 */
-(id)member:(id)anObject
{
    NSObject* result = nil;

    PyObjC_BEGIN_WITH_GIL
        int r;
        PyObject* tmpMember;

        if (anObject == [NSNull null]) {
            tmpMember = Py_None;
            Py_INCREF(Py_None);

        } else {
            tmpMember = PyObjC_IdToPython(anObject);
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
                        result = PyObjC_PythonToId(v);
                        if (PyErr_Occurred()) {
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

-(void)removeAllObjects
{
    PyObjC_BEGIN_WITH_GIL
        if (PyFrozenSet_CheckExact(value)) {
            PyErr_SetString(PyExc_TypeError,
                "Cannot mutate a frozenstring");
            PyObjC_GIL_FORWARD_EXC();
        }

        if (PyAnySet_Check(value)) {
            int r = PySet_Clear(value);\
            if (r == -1) {
                PyObjC_GIL_FORWARD_EXC();
            }
        } else {
            /* Assume an object that conforms to
             * the set interface
             */
             PyObject* r;

             r = PyObject_CallMethod(value, "clear", NULL);
             if (r == NULL) {
                 PyObjC_GIL_FORWARD_EXC();
             }
             Py_DECREF(r);
        }
    PyObjC_END_WITH_GIL
}

-(void)removeObject:(id)anObject
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp = PyObjC_IdToPython(anObject);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (PyFrozenSet_CheckExact(value)) {
            PyErr_SetString(PyExc_TypeError,
                "Cannot mutate a frozenstring");
            PyObjC_GIL_FORWARD_EXC();
        }

        if (PyAnySet_Check(value)) {
            int r = PySet_Discard(value, tmp);
            Py_DECREF(tmp);
            if (r == -1) {
                PyObjC_GIL_FORWARD_EXC();
            }

        } else {
             PyObject* r;

             r = PyObject_CallMethod(value, "discard", "O", tmp);
             Py_DECREF(tmp);
             if (r == NULL) {
                 PyObjC_GIL_FORWARD_EXC();
             }
             Py_DECREF(r);
        }

    PyObjC_END_WITH_GIL
}

-(void)addObject:(id)anObject
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* tmp = PyObjC_IdToPython(anObject);
        if (tmp == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (PyFrozenSet_CheckExact(value)) {
            PyErr_SetString(PyExc_TypeError,
                "Cannot mutate a frozenstring");
            PyObjC_GIL_FORWARD_EXC();
        }

        if (PyAnySet_Check(value)) {
            int r = PySet_Add(value, tmp);
            Py_DECREF(tmp);
            if (r == -1) {
                PyObjC_GIL_FORWARD_EXC();
            }

        } else {
             PyObject* r;

             r = PyObject_CallMethod(value, "add", "O", tmp);
             Py_DECREF(tmp);
             if (r == NULL) {
                 PyObjC_GIL_FORWARD_EXC();
             }
             Py_DECREF(r);
        }

    PyObjC_END_WITH_GIL
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSSet"];
}

@end
