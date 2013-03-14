#include "pyobjc.h"
#import "OC_PythonArray.h"

@implementation OC_PythonArray

+ (OC_PythonArray*)arrayWithPythonObject:(PyObject*)v
{
    OC_PythonArray* res;

    res = [[OC_PythonArray alloc] initWithPythonObject:v];
    return [res autorelease];
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
    if (likely(value)) {
        Py_INCREF(value);
        return value;
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
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
        Py_CLEAR(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

-(NSUInteger)count
{
    Py_ssize_t result;

    PyObjC_BEGIN_WITH_GIL
        result = PySequence_Length(value);
        if (result < 0 && PyErr_Occurred()) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL

    if (unlikely(result < 0)) {
        return 0;
    }

    return result;
}

-(id)objectAtIndex:(NSUInteger)idx
{
    PyObject* v;
    id result;
    int err;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(idx > PY_SSIZE_T_MAX)) {
            PyErr_SetString(PyExc_IndexError, "out of range");
            PyObjC_GIL_FORWARD_EXC();
        }

        v = PySequence_GetItem(value, (Py_ssize_t)idx);
        if (unlikely(v == NULL)) {
            PyObjC_GIL_FORWARD_EXC();
        }

        err = depythonify_c_value(@encode(id), v, &result);
        if (unlikely(err == -1)) {
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_CLEAR(v);

    PyObjC_END_WITH_GIL

    if (result == nil) {
        result = [NSNull null];
    }
    return result;
}


-(void)replaceObjectAtIndex:(NSUInteger)idx withObject:newValue
{
    PyObject* v;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(idx > PY_SSIZE_T_MAX)) {
            PyErr_SetString(PyExc_IndexError, "out of range");
            PyObjC_GIL_FORWARD_EXC();
        }

        if (unlikely(newValue == [NSNull null])) {
            Py_INCREF(Py_None);
            v = Py_None;

        } else {
            v = PyObjC_IdToPython(newValue);
            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        if (PySequence_SetItem(value, idx, v) < 0) {
            Py_DECREF(v);
            PyObjC_GIL_FORWARD_EXC();
        }

        Py_DECREF(v);

    PyObjC_END_WITH_GIL;
}

-(void)getObjects:(id*)buffer inRange:(NSRange)range
{
    unsigned int i;

    for (i = 0; i < range.length; i++) {
        buffer[i] = [self objectAtIndex:i+range.location];
    }
}

-(void)addObject:(id)anObject
{
    PyObject* v;
    PyObject* w;

    PyObjC_BEGIN_WITH_GIL

        if (unlikely(anObject == [NSNull null])) {
            Py_INCREF(Py_None);
            v = Py_None;

        } else {
            v = PyObjC_IdToPython(anObject);
            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        w = PyObject_CallMethod(value, "append", "N", v);
        if (unlikely(w == NULL)) {
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(w);

    PyObjC_END_WITH_GIL;
}

-(void)insertObject:(id)anObject atIndex:(NSUInteger)idx
{
    Py_ssize_t theIndex;
    PyObject* v;
    PyObject* w;

    if (unlikely(idx > PY_SSIZE_T_MAX)) {
        PyObjC_BEGIN_WITH_GIL
            PyErr_SetString(PyExc_IndexError, "No such index");
            PyObjC_GIL_FORWARD_EXC();
        PyObjC_END_WITH_GIL
    }
    theIndex = idx;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(anObject == [NSNull null])) {
            Py_INCREF(Py_None);
            v = Py_None;

        } else {
            v = PyObjC_IdToPython(anObject);
            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        w = PyObject_CallMethod(value, "insert", "nN", theIndex, v);
        if (unlikely(w == NULL)) {
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(w);

    PyObjC_END_WITH_GIL;
}

-(void)removeLastObject
{
    int r;
    Py_ssize_t idx;

    PyObjC_BEGIN_WITH_GIL
        idx = PySequence_Length(value);
        if (unlikely(idx == -1)) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (unlikely(idx == 0)) {
            PyErr_SetString(PyExc_ValueError, "pop empty sequence");
            PyObjC_GIL_FORWARD_EXC();
        }

        r = PySequence_DelItem(value, idx-1);
        if (unlikely(r == -1)) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL;
}

-(void)removeObjectAtIndex:(NSUInteger)idx
{
    int r;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(idx > PY_SSIZE_T_MAX)) {
            PyErr_SetString(PyExc_IndexError, "No such index");
            PyObjC_GIL_FORWARD_EXC();
        }

        r = PySequence_DelItem(value, (Py_ssize_t)idx);
        if (unlikely(r == -1)) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL;
}

-(void)encodeWithCoder:(NSCoder*)coder
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
            if (size > INT_MAX) {
                [coder encodeInt32:5 forKey:@"pytype"];
                [coder encodeInt64:(int64_t)PyTuple_Size(value) forKey:@"pylength"];

            } else {
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

        PyObjC_encodeWithCoder(value, coder);
    }
}

-(Class)classForCoder
{
    if (value == NULL || PyTuple_CheckExact(value)) {
        return [NSArray class];

    } else if (PyList_CheckExact(value)) {
        return [NSMutableArray class];

    } else {
        return [OC_PythonArray class];
    }
}

-(Class)classForKeyedArchiver
{
    return [OC_PythonArray class];
}

-(id)initWithObjects:(NSObject**)objects count:(NSUInteger)count
{
    /* initWithObjects:count: is primarily present to support the NSCoding
     * protocol of NSArray.
     */
    NSUInteger i;
    PyObjC_BEGIN_WITH_GIL
        if (PyTuple_CheckExact(value) && (NSUInteger)PyTuple_Size(value) == count) {
            for  (i = 0; i < count; i++) {
                PyObject* v;

                if (objects[i] == [NSNull null]) {
                    v = Py_None; Py_INCREF(Py_None);

                } else {
                    v = PyObjC_IdToPython(objects[i]);

                }

                if (v == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                if (PyTuple_GET_ITEM(value, i) != NULL) {
                    /* use temporary object to avoid race condition */
                    PyObject* t = PyTuple_GET_ITEM(value, i);
                    PyTuple_SET_ITEM(value, i, NULL);
                    Py_DECREF(t);
                }
                PyTuple_SET_ITEM(value, i, v);
            }

        } else {

            for  (i = 0; i < count; i++) {
                PyObject* v;
                int r;

                if (objects[i] == [NSNull null]) {
                    v = Py_None; Py_INCREF(Py_None);

                } else {
                    v = PyObjC_IdToPython(objects[i]);
                }

                if (v == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                r = PyList_Append(value,  v);
                if (r == -1) {
                    PyObjC_GIL_FORWARD_EXC();
                }

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
-(void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* v = PyObjC_IdToPython(other);
        SET_FIELD(value, v);

    PyObjC_END_WITH_GIL
}

-(id)initWithCoder:(NSCoder*)coder
{
    PyObject* t;
    int code;
    Py_ssize_t size;

    if ([coder allowsKeyedCoding]) {
        code = [coder decodeInt32ForKey:@"pytype"];

    } else {
        [coder decodeValueOfObjCType:@encode(int) at:&code];
    }

    switch (code) {
    case 1:
          /* This code was created by some previous versions of PyObjC
           * (before 2.2) and is kept around for backward compatibilty.
           */
          PyObjC_BEGIN_WITH_GIL
              value = PyList_New(0);
              if (value == NULL){
                  PyObjC_GIL_FORWARD_EXC();
              }

          PyObjC_END_WITH_GIL

          [super initWithCoder:coder];

          PyObjC_BEGIN_WITH_GIL
              t = value;
              value = PyList_AsTuple(t);
              Py_DECREF(t);
              if (value == NULL) {
                PyObjC_GIL_FORWARD_EXC();
              }
          PyObjC_END_WITH_GIL
          return self;

    case 2:
          PyObjC_BEGIN_WITH_GIL
              value = PyList_New(0);
              if (value == NULL) {
                  PyObjC_GIL_FORWARD_EXC();
              }

          PyObjC_END_WITH_GIL

          [super initWithCoder:coder];
          return self;

    case 3:
        PyObjC_BEGIN_WITH_GIL
            value = PyList_New(0);
            if (value == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

        PyObjC_END_WITH_GIL

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
                if (selfAsPython == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");
                Py_DECREF(selfAsPython);

                if (setValue == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                v = PyObject_CallFunction(PyObjC_Decoder, "NN", cdr, setValue);

                if (v == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                SET_FIELD(value, v);

                self = PyObjC_FindOrRegisterObjCProxy(value, self);

            PyObjC_END_WITH_GIL

            return self;
        }

    case 4:
          /* tuple with less than MAX_INT elements */
          if ([coder allowsKeyedCoding]) {
              size = [coder decodeInt32ForKey:@"pylength"];

          } else {
              int isize;
              [coder decodeValueOfObjCType:@encode(int) at:&isize];
              size = isize;
          }

          PyObjC_BEGIN_WITH_GIL
              value = PyTuple_New(size);
              if (value == NULL){
                  PyObjC_GIL_FORWARD_EXC();
              }

          PyObjC_END_WITH_GIL

          [super initWithCoder:coder];
          return self;

    case 5:
          /* tuple with more than MAX_INT elements */
#ifdef __LP64__
          if ([coder allowsKeyedCoding]) {
              size = [coder decodeInt64ForKey:@"pylength"];
          } else {
              [coder decodeValueOfObjCType:@encode(long long) at:&size];
          }

          PyObjC_BEGIN_WITH_GIL
              value = PyTuple_New(size);
              if (value == NULL){
                  PyObjC_GIL_FORWARD_EXC();
              }

          PyObjC_END_WITH_GIL
          [super initWithCoder:coder];
          return self;
#else
          [NSException raise:NSInvalidArgumentException
                      format:@"decoding tuple with more than INT_MAX elements in 32-bit"];
          [self release];
          return nil;
#endif

    default:
        [self release];
        [NSException raise:NSInvalidArgumentException
                    format:@"Cannot decode OC_PythonArray with type-id %d", code];
        return nil;
    }
}


-(id)copyWithZone:(NSZone*)zone
{
    if (PyObjC_CopyFunc) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* copy = PyObject_CallFunctionObjArgs(PyObjC_CopyFunc, value, NULL);

            if (copy == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            NSObject* result = PyObjC_PythonToId(copy);
            Py_DECREF(copy);

            if (PyErr_Occurred()) {
                PyObjC_GIL_FORWARD_EXC();
            }

            [result retain];

            PyObjC_GIL_RETURN(result);

        PyObjC_END_WITH_GIL

    } else {
        return [super copyWithZone:zone];
    }
}

-(id)mutableCopyWithZone:(NSZone*)zone
{
    if (PyObjC_CopyFunc) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* copy = PySequence_List(value);
            if (copy == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            NSObject* result = PyObjC_PythonToId(copy);
            Py_DECREF(copy);

            if (PyErr_Occurred()) {
                PyObjC_GIL_FORWARD_EXC();
            }

            [result retain];
            PyObjC_GIL_RETURN(result);

        PyObjC_END_WITH_GIL
    } else {
        return [super mutableCopyWithZone:zone];
    }
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSArray"];
}


@end /* implementation OC_PythonArray */
