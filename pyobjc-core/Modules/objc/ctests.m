/*
 * This file contains some unittests for specific functions in the extension
 * module.
 *
 * The PyObjC unittest objc.test.test_ctests executes the tests in this file.
 */
#include "pyobjc.h"
#include "pyobjc-unittest.h"

#include <fcntl.h>
#include <simd/simd.h>

// LCOV_BR_EXCL_START
// LCOV_EXCL_START
//
struct empty {};

NS_ASSUME_NONNULL_BEGIN

#pragma clang diagnostic ignored "-Wunused-result"

struct Struct1 {
    int    f1;
    double f2;
};

struct Struct2 {
    int    f1;
    double f2;
    short  s[5];
};

struct Struct3 {
    char ch;
    int  i;
};

struct Struct4 {
    char      ch;
    long long i;
};

struct Struct5 {
    long i;
    char ch;
};

typedef struct Struct5 Struct5Array[2];

/* Helper stuff for TestNSInvoke */

static struct Struct2 invokeHelper = {0, 0, {0, 0, 0, 0, 0}};

@interface PyObjCTest_NSInvoke : NSObject {
}
- (void)methodWithMyStruct:(struct Struct2)val1 andShort:(short)val2;
@end

@implementation PyObjCTest_NSInvoke
- (void)methodWithMyStruct:(struct Struct2)val1 andShort:(short)val2
{
    (void)val2;
    invokeHelper = val1;
}
@end

BEGIN_UNITTEST(CheckNSInvoke)
/* This is not a 'real' unittest, but is used to disable a number of
 * other tests (in objc.test.test_methods2) when NSInvocation isn't
 * working correctly (MacOS X at least up to 10.2.6).
 */

PyObjCTest_NSInvoke* obj = [[PyObjCTest_NSInvoke alloc] init];
NSInvocation*        inv;
struct Struct2       v1 = {1, 2, {3, 4, 5, 6, 7}};
short                v2 = 8;

[obj methodWithMyStruct:v1 andShort:v2];
inv =
    [NSInvocation invocationWithMethodSignature:[obj methodSignatureForSelector:@selector
                                                     (methodWithMyStruct:andShort:)]];
[inv setTarget:obj];
[inv setSelector:@selector(methodWithMyStruct:andShort:)];
[inv setArgument:&v1 atIndex:2];
[inv setArgument:&v2 atIndex:3];

[inv invoke];
[obj release];
ASSERT_EQUALS(invokeHelper.f1, v1.f1, "%d");
ASSERT_EQUALS(invokeHelper.f2, v1.f2, "%g");
ASSERT_EQUALS(invokeHelper.s[0], v1.s[0], "%d");
ASSERT_EQUALS(invokeHelper.s[1], v1.s[1], "%d");
ASSERT_EQUALS(invokeHelper.s[2], v1.s[2], "%d");
ASSERT_EQUALS(invokeHelper.s[3], v1.s[3], "%d");
ASSERT_EQUALS(invokeHelper.s[4], v1.s[4], "%d");

END_UNITTEST

/* Note: VectorSize and VectorAlign
 *  (a) test the same set of types
 *  (b) test all vector/matrix types found in system frameworks
 *      that are wrapped in PyObjC.
 */
BEGIN_UNITTEST(VectorSize)
ASSERT_EQUALS(sizeof(vector_uchar16), PyObjCRT_SizeOfType("<16C>"), "%d");
ASSERT_EQUALS(sizeof(vector_short2), PyObjCRT_SizeOfType("<2s>"), "%d");
ASSERT_EQUALS(sizeof(vector_ushort2), PyObjCRT_SizeOfType("<2S>"), "%d");
ASSERT_EQUALS(sizeof(vector_ushort4), PyObjCRT_SizeOfType("<4S>"), "%d");
ASSERT_EQUALS(sizeof(vector_int2), PyObjCRT_SizeOfType("<2i>"), "%d");
ASSERT_EQUALS(sizeof(vector_uint3), PyObjCRT_SizeOfType("<3I>"), "%d");
ASSERT_EQUALS(sizeof(vector_float2), PyObjCRT_SizeOfType("<2f>"), "%d");
ASSERT_EQUALS(sizeof(vector_float3), PyObjCRT_SizeOfType("<3f>"), "%d");
ASSERT_EQUALS(sizeof(vector_float4), PyObjCRT_SizeOfType("<4f>"), "%d");
ASSERT_EQUALS(sizeof(vector_double2), PyObjCRT_SizeOfType("<2d>"), "%d");
ASSERT_EQUALS(sizeof(vector_double3), PyObjCRT_SizeOfType("<3d>"), "%d");
ASSERT_EQUALS(sizeof(vector_double4), PyObjCRT_SizeOfType("<4d>"), "%d");

Py_ssize_t n = PyObjCRT_SizeOfType("<4,4di");
FAIL_IF(n != -1);
PyErr_Clear();

n = PyObjCRT_SizeOfType("<d>");
FAIL_IF(n != -1);
PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(VectorAlign)
ASSERT_EQUALS(__alignof__(vector_uchar16), PyObjCRT_AlignOfType("<16C>"), "%d");
ASSERT_EQUALS(__alignof__(vector_short2), PyObjCRT_AlignOfType("<2s>"), "%d");
ASSERT_EQUALS(__alignof__(vector_ushort2), PyObjCRT_AlignOfType("<2S>"), "%d");
ASSERT_EQUALS(__alignof__(vector_ushort4), PyObjCRT_AlignOfType("<4S>"), "%d");
ASSERT_EQUALS(__alignof__(vector_int2), PyObjCRT_AlignOfType("<2i>"), "%d");
ASSERT_EQUALS(__alignof__(vector_uint3), PyObjCRT_AlignOfType("<3I>"), "%d");
ASSERT_EQUALS(__alignof__(vector_float2), PyObjCRT_AlignOfType("<2f>"), "%d");
ASSERT_EQUALS(__alignof__(vector_float3), PyObjCRT_AlignOfType("<3f>"), "%d");
ASSERT_EQUALS(__alignof__(vector_float4), PyObjCRT_AlignOfType("<4f>"), "%d");
ASSERT_EQUALS(__alignof__(vector_double2), PyObjCRT_AlignOfType("<2d>"), "%d");
ASSERT_EQUALS(__alignof__(vector_double3), PyObjCRT_AlignOfType("<3d>"), "%d");
ASSERT_EQUALS(__alignof__(vector_double4), PyObjCRT_AlignOfType("<4d>"), "%d");

Py_ssize_t n = PyObjCRT_AlignOfType("<4,4di");
FAIL_IF(n != -1);
PyErr_Clear();

n = PyObjCRT_AlignOfType("<d>");
FAIL_IF(n != -1);
PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(BitFieldSize)
struct bitfield1 {
    unsigned int first : 4;
};
struct bitfield2 {
    unsigned int first : 4;
    unsigned int second : 30;
};

ASSERT_EQUALS(sizeof(struct bitfield1), PyObjCRT_SizeOfType(@encode(struct bitfield1)),
              "%d");
ASSERT_EQUALS(sizeof(struct bitfield2), PyObjCRT_SizeOfType(@encode(struct bitfield2)),
              "%d");
END_UNITTEST

BEGIN_UNITTEST(StructSize)

ASSERT_EQUALS(sizeof(struct empty), PyObjCRT_SizeOfType(@encode(struct empty)), "%d");

ASSERT_EQUALS(sizeof(struct Struct1), PyObjCRT_SizeOfType(@encode(struct Struct1)), "%d");

ASSERT_EQUALS(sizeof(struct Struct2), PyObjCRT_SizeOfType(@encode(struct Struct2)), "%d");

ASSERT_EQUALS(sizeof(struct Struct3), PyObjCRT_SizeOfType(@encode(struct Struct3)), "%d");

ASSERT_EQUALS(sizeof(struct Struct4), PyObjCRT_SizeOfType(@encode(struct Struct4)), "%d");

ASSERT_EQUALS(sizeof(NSRect), PyObjCRT_SizeOfType(@encode(NSRect)), "%d");

Py_ssize_t r = PyObjCRT_SizeOfType("{p=!}");
FAIL_IF(r != -1);
PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(StructAlign)

ASSERT_EQUALS(__alignof__(struct empty), PyObjCRT_AlignOfType(@encode(struct empty)),
              "%d");

ASSERT_EQUALS(__alignof__(struct Struct1), PyObjCRT_AlignOfType(@encode(struct Struct1)),
              "%d");

ASSERT_EQUALS(__alignof__(struct Struct2), PyObjCRT_AlignOfType(@encode(struct Struct2)),
              "%d");

ASSERT_EQUALS(__alignof__(struct Struct3), PyObjCRT_AlignOfType(@encode(struct Struct3)),
              "%d");

ASSERT_EQUALS(__alignof__(struct Struct4), PyObjCRT_AlignOfType(@encode(struct Struct4)),
              "%d");

ASSERT_EQUALS(__alignof__(struct empty), PyObjCRT_AlignOfType("n{empty=}"), "%d");

Py_ssize_t r = PyObjCRT_AlignOfType("{p=!");
FAIL_IF(r != -1);
PyErr_Clear();

r = PyObjCRT_AlignOfType("(p=!");
FAIL_IF(r != -1);
PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(FillStruct1)

PyObject*      input;
struct Struct1 output;
int            r;

input = PyTuple_Pack(2, PyLong_FromLong(1), PyFloat_FromDouble(2));
FAIL_IF(input == NULL);

r = depythonify_c_value(@encode(struct Struct1), input, &output);
FAIL_IF(r < 0);

Py_DECREF(input);

ASSERT_EQUALS(output.f1, 1, "%d");
ASSERT_EQUALS(output.f2, 2.0, "%g");

END_UNITTEST

BEGIN_UNITTEST(FillStruct2)

PyObject*      input;
PyObject*      v;
struct Struct2 output;
int            r;

v = PyTuple_Pack(5, PyLong_FromLong(10), PyLong_FromLong(11), PyLong_FromLong(12),
                 PyLong_FromLong(13), PyLong_FromLong(14));
FAIL_IF(v == NULL);

input = PyTuple_Pack(3, PyLong_FromLong(1), PyFloat_FromDouble(2), v);
Py_CLEAR(v);
FAIL_IF(input == NULL);

r = depythonify_c_value(@encode(struct Struct2), input, &output);
FAIL_IF(r < 0);

Py_DECREF(input);

ASSERT_EQUALS(output.f1, 1, "%d");
ASSERT_EQUALS(output.f2, 2.0, "%g");
ASSERT_EQUALS(output.s[0], 10, "%d");
ASSERT_EQUALS(output.s[1], 11, "%d");
ASSERT_EQUALS(output.s[2], 12, "%d");
ASSERT_EQUALS(output.s[3], 13, "%d");
ASSERT_EQUALS(output.s[4], 14, "%d");

END_UNITTEST

BEGIN_UNITTEST(FillStruct3)

PyObject*      input;
struct Struct3 output;
int            r;

input = PyTuple_Pack(2, PyBytes_FromStringAndSize("\001", 1), PyLong_FromLong(2));
FAIL_IF(input == NULL);

r = depythonify_c_value(@encode(struct Struct3), input, &output);
FAIL_IF(r < 0);

Py_DECREF(input);

ASSERT_EQUALS(output.ch, '\001', "%d");
ASSERT_EQUALS(output.i, 2, "%d");

END_UNITTEST

BEGIN_UNITTEST(FillStruct4)

PyObject*      input;
struct Struct4 output;
int            r;

input = PyTuple_Pack(2, PyBytes_FromStringAndSize("\001", 1), PyLong_FromLong(500000));
FAIL_IF(input == NULL);

r = depythonify_c_value(@encode(struct Struct4), input, &output);
FAIL_IF(r < 0);

Py_DECREF(input);

ASSERT_EQUALS(output.ch, '\001', "%d");
ASSERT_EQUALS(output.i, 500000, "%ll");

END_UNITTEST

BEGIN_UNITTEST(FillStruct5Array)

PyObject*    input;
PyObject*    v1;
PyObject*    v2;
Struct5Array output;
int          r;

v1 = PyTuple_Pack(2, PyLong_FromLong(500000), PyBytes_FromStringAndSize("\001", 1));
FAIL_IF(v1 == NULL);
v2 = PyTuple_Pack(2, PyLong_FromLong(1000000), PyBytes_FromStringAndSize("\002", 1));
FAIL_IF(v2 == NULL);

input = PyTuple_Pack(2, v1, v2);
Py_CLEAR(v1);
Py_CLEAR(v2);
FAIL_IF(input == NULL);

r = depythonify_c_value(@encode(Struct5Array), input, &output);
FAIL_IF(r < 0);

Py_DECREF(input);

ASSERT_EQUALS(output[0].ch, '\001', "%d");
ASSERT_EQUALS(output[0].i, 500000, "%ll");
ASSERT_EQUALS(output[1].ch, '\002', "%d");
ASSERT_EQUALS(output[1].i, 1000000, "%ll");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct1)

struct Struct1 input;
PyObject*      output;

input.f1 = 1;
input.f2 = 2;

output = pythonify_c_value(@encode(struct Struct1), &input);
FAIL_IF(output == NULL);

ASSERT_ISINSTANCE(output, Tuple);
ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Float);
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GetItem(output, 1)), 2.0, "%g");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct2)

struct Struct2 input;
PyObject*      output;
PyObject*      tup;
PyObject*      v;

input.f1   = 1;
input.f2   = 2;
input.s[0] = 3;
input.s[1] = 4;
input.s[2] = 5;
input.s[3] = 6;
input.s[4] = 7;

output = pythonify_c_value(@encode(struct Struct2), &input);
FAIL_IF(output == NULL);

ASSERT_ISINSTANCE(output, Tuple);
ASSERT_EQUALS(PyTuple_GET_SIZE(output), 3, "%d");
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Float);
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 2), Tuple);
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GetItem(output, 1)), 2.0, "%g");

tup = PyTuple_GetItem(output, 2);
ASSERT_EQUALS(PyTuple_GET_SIZE(tup), 5, "%d");

v = PyTuple_GetItem(tup, 0);
ASSERT_ISINSTANCE(v, Long);
ASSERT_EQUALS(PyLong_AsLong(v), 3, "%d");

v = PyTuple_GetItem(tup, 1);
ASSERT_ISINSTANCE(v, Long);
ASSERT_EQUALS(PyLong_AsLong(v), 4, "%d");

v = PyTuple_GetItem(tup, 2);
ASSERT_ISINSTANCE(v, Long);
ASSERT_EQUALS(PyLong_AsLong(v), 5, "%d");

v = PyTuple_GetItem(tup, 3);
ASSERT_ISINSTANCE(v, Long);
ASSERT_EQUALS(PyLong_AsLong(v), 6, "%d");

v = PyTuple_GetItem(tup, 4);
ASSERT_ISINSTANCE(v, Long);
ASSERT_EQUALS(PyLong_AsLong(v), 7, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct3)

struct Struct3 input;
PyObject*      output;

input.ch = 1;
input.i  = 2;

output = pythonify_c_value(@encode(struct Struct3), &input);
FAIL_IF(output == NULL);

ASSERT_ISINSTANCE(output, Tuple);
ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Long);
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(output, 1)), 2, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct4)

struct Struct4 input;
PyObject*      output;

input.ch = 1;
input.i  = 500000;

output = pythonify_c_value(@encode(struct Struct4), &input);
FAIL_IF(output == NULL);

ASSERT_ISINSTANCE(output, Tuple);
ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Long);

ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(output, 1)), 500000, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct5Array)

Struct5Array input;
PyObject*    output;
PyObject*    v;

input[0].ch = 1;
input[0].i  = 500000;
input[1].ch = 2;
input[1].i  = 1000000;

output = pythonify_c_value(@encode(Struct5Array), &input);
FAIL_IF(output == NULL);

ASSERT_ISINSTANCE(output, Tuple);
ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");

v = PyTuple_GetItem(output, 0);
ASSERT_ISINSTANCE(v, Tuple);
ASSERT_ISINSTANCE(PyTuple_GetItem(v, 0), Long);
ASSERT_ISINSTANCE(PyTuple_GetItem(v, 1), Long);
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(v, 0)), 500000, "%d");
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(v, 1)), 1, "%d");

v = PyTuple_GetItem(output, 1);
ASSERT_ISINSTANCE(v, Tuple);
ASSERT_ISINSTANCE(PyTuple_GetItem(v, 0), Long);
ASSERT_ISINSTANCE(PyTuple_GetItem(v, 1), Long);
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(v, 0)), 1000000, "%d");
ASSERT_EQUALS(PyLong_AsLong(PyTuple_GetItem(v, 1)), 2, "%d");

END_UNITTEST

#ifdef _C_BOOL

BEGIN_UNITTEST(TestSizeOfBool)

ASSERT_EQUALS(sizeof(bool), sizeof(char), "%d");

END_UNITTEST

#endif

BEGIN_UNITTEST(TestTypeCode)

/* These are manually defined on some platforms */
ASSERT_EQUALS(@encode(long long)[0], 'q', "%c");
ASSERT_EQUALS(@encode(unsigned long long)[0], 'Q', "%c");
ASSERT_EQUALS(@encode(bool)[0], 'B', "%#x");

END_UNITTEST

BEGIN_UNITTEST(TestSimplifySignature)
/* Make sure PyObjCRT_SimplifySignature works */
char b[1024];
int  r;

r = PyObjCRT_SimplifySignature("@1234@0:{_NSPoint=ff}02i22", b, sizeof(b));
ASSERT(r != -1);
ASSERT_STREQUALS("@@:{_NSPoint=ff}i", b);

r = PyObjCRT_SimplifySignature("@@:{_NSPoint=ff}i", b, sizeof(b));
ASSERT(r != -1);
ASSERT_STREQUALS("@@:{_NSPoint=ff}i", b);
END_UNITTEST

BEGIN_UNITTEST(TestArrayCoding)
/*
 * According to the docs on Panther, valueForKey: on an array should
 * return [ o.valueForKey_(key) for o in anArray ].
 * On MacOS X 10.2 it doesn't.
 *
 * This test was added to make sure PyObjC is not at fault :-), the
 * test is also used to avoid giving false positives in the unittests
 * for key-value coding.
 */

NSMutableDictionary* d;
NSMutableArray*      a;
NSObject*            v;
int                  haveException;

NSAutoreleasePool* p;

p = [[NSAutoreleasePool alloc] init];

d = [NSMutableDictionary dictionary];

[d setObject:@"foo" forKey:@"keyM"];

a = [NSMutableArray arrayWithObjects:d, nil];

@try {
    v             = [a valueForKey:@"keyM"];
    haveException = 0;
} @catch (NSObject* localException) { // LCOV_EXCL_LINE (see comment at start)
    v             = nil;
    haveException = 1;
}

[p release];

ASSERT(!haveException);
ASSERT(v != nil);
END_UNITTEST

BEGIN_UNITTEST(PythonListAsNSArray)
PyObject*       aList;
NSMutableArray* array;
NSArray*        array2;
int             r;

aList = Py_BuildValue("[iiiii]", 0, 1, 2, 3, 4);
FAIL_IF(aList == NULL);

r = depythonify_python_object(aList, &array);
FAIL_IF(r == -1);
FAIL_IF(array == nil);

/* Check length */
ASSERT_EQUALS(5, [array count], "%d");

/* Check basic element access */
ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);
ASSERT([[NSNumber numberWithInt:2] isEqual:[array objectAtIndex:2]]);
ASSERT([[NSNumber numberWithInt:3] isEqual:[array objectAtIndex:3]]);
ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

/* Check some other methods */
array2 = [array arrayByAddingObject:[NSNumber numberWithInt:5]];
FAIL_IF(array2 == nil);

ASSERT_EQUALS(6, [array2 count], "%d");
ASSERT_EQUALS(5, [array count], "%d");

ASSERT([[NSNumber numberWithInt:0] isEqual:[array2 objectAtIndex:0]]);
ASSERT([[NSNumber numberWithInt:1] isEqual:[array2 objectAtIndex:1]]);
ASSERT([[NSNumber numberWithInt:2] isEqual:[array2 objectAtIndex:2]]);
ASSERT([[NSNumber numberWithInt:3] isEqual:[array2 objectAtIndex:3]]);
ASSERT([[NSNumber numberWithInt:4] isEqual:[array2 objectAtIndex:4]]);
ASSERT([[NSNumber numberWithInt:5] isEqual:[array2 objectAtIndex:5]]);

ASSERT([array containsObject:[NSNumber numberWithInt:4]]);
ASSERT(![array containsObject:[NSNumber numberWithInt:10]]);

/* Mutating methods */
[array addObject:[NSNumber numberWithInt:5]];
ASSERT_EQUALS(6, [array count], "%d");
ASSERT([[NSNumber numberWithInt:5] isEqual:[array objectAtIndex:5]]);

[array removeLastObject];
ASSERT_EQUALS(5, [array count], "%d");
ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

[array insertObject:[NSNumber numberWithInt:6] atIndex:1];
ASSERT_EQUALS(6, [array count], "%d");
ASSERT([[NSNumber numberWithInt:6] isEqual:[array objectAtIndex:1]]);

[array removeObjectAtIndex:1];
ASSERT_EQUALS(5, [array count], "%d");
ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);

[array replaceObjectAtIndex:1 withObject:[NSNumber numberWithInt:7]];
ASSERT_EQUALS(5, [array count], "%d");
ASSERT([[NSNumber numberWithInt:7] isEqual:[array objectAtIndex:1]]);

END_UNITTEST

BEGIN_UNITTEST(PythonTupleAsNSArray)
PyObject* aTuple;
NSArray*  array;
NSArray*  array2;
int       r;

aTuple = Py_BuildValue("(iiiii)", 0, 1, 2, 3, 4);
FAIL_IF(aTuple == NULL);

r = depythonify_python_object(aTuple, &array);
FAIL_IF(r == -1);
FAIL_IF(array == nil);

/* Check length */
ASSERT_EQUALS(5, [array count], "%d");

/* Check basic element access */
ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);
ASSERT([[NSNumber numberWithInt:2] isEqual:[array objectAtIndex:2]]);
ASSERT([[NSNumber numberWithInt:3] isEqual:[array objectAtIndex:3]]);
ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

/* Check some other methods */
array2 = [array arrayByAddingObject:[NSNumber numberWithInt:5]];
ASSERT(array2 != nil);

ASSERT_EQUALS(6, [array2 count], "%d");
ASSERT_EQUALS(5, [array count], "%d");

ASSERT([[NSNumber numberWithInt:0] isEqual:[array2 objectAtIndex:0]]);
ASSERT([[NSNumber numberWithInt:1] isEqual:[array2 objectAtIndex:1]]);
ASSERT([[NSNumber numberWithInt:2] isEqual:[array2 objectAtIndex:2]]);
ASSERT([[NSNumber numberWithInt:3] isEqual:[array2 objectAtIndex:3]]);
ASSERT([[NSNumber numberWithInt:4] isEqual:[array2 objectAtIndex:4]]);
ASSERT([[NSNumber numberWithInt:5] isEqual:[array2 objectAtIndex:5]]);

ASSERT([array containsObject:[NSNumber numberWithInt:4]]);
ASSERT(![array containsObject:[NSNumber numberWithInt:10]]);

END_UNITTEST

BEGIN_UNITTEST(PythonDictAsNSDictionary)
// count, objectForKey:, keyEnumerator
// setObject:forKey: removeObjectForKey:
PyObject*            aDictionary;
NSMutableDictionary* dict;
NSEnumerator*        iter;
NSArray*             keys;
int                  r;

aDictionary = Py_BuildValue("{iiiiiiii}", 1, 2, 2, 4, 3, 6, 4, 8);
FAIL_IF(aDictionary == NULL);

r = depythonify_python_object(aDictionary, &dict);
FAIL_IF(r == -1);
FAIL_IF(dict == nil);

ASSERT_EQUALS(4, [dict count], "%d");
ASSERT([[dict objectForKey:[NSNumber numberWithInt:1]]
    isEqual:[NSNumber numberWithInt:2]]);

[dict setObject:[NSNumber numberWithInt:10] forKey:[NSNumber numberWithInt:5]];
ASSERT_EQUALS(5, [dict count], "%d");
ASSERT([[dict objectForKey:[NSNumber numberWithInt:5]]
    isEqual:[NSNumber numberWithInt:10]]);

[dict removeObjectForKey:[NSNumber numberWithInt:5]];
ASSERT_EQUALS(4, [dict count], "%d");

iter = [dict keyEnumerator];
ASSERT(iter != nil);

keys = [iter allObjects];
ASSERT_EQUALS(4, [keys count], "%d");
ASSERT([[keys objectAtIndex:0] isEqual:[NSNumber numberWithInt:1]]);
ASSERT([[keys objectAtIndex:1] isEqual:[NSNumber numberWithInt:2]]);
ASSERT([[keys objectAtIndex:2] isEqual:[NSNumber numberWithInt:3]]);
ASSERT([[keys objectAtIndex:3] isEqual:[NSNumber numberWithInt:4]]);

END_UNITTEST

BEGIN_UNITTEST(NSLogging)
/* This is a pretty lame test ...
 *
 * What this does is tests that the proxies of plain Python objects
 * can be logged. This used to be impossible up to (and including)
 * release 1.1!
 */
PyObject* o = (PyObject*)(Py_BuildValue("i", 10)->ob_type);
NSObject* value;
int       fd;
int       stderr_orig;
int       r;

r = depythonify_python_object(o, &value);
FAIL_IF(r == -1);
FAIL_IF(value == nil);

fd = open("/dev/null", O_WRONLY);
ASSERT((fd != -1));
stderr_orig = dup(2);
ASSERT(stderr_orig != -1);
r = dup2(fd, 2);
ASSERT(r != -1);
NSLog(@"%@", value);
r = dup2(stderr_orig, 2);
ASSERT(r != -1);
r = close(fd);
ASSERT(r != -1);
END_UNITTEST

BEGIN_UNITTEST(FillNSRect)

struct output {
    unsigned int before;
    NSRect       rect;
    unsigned int after;
};

PyObject*     input;
PyObject*     v;
PyObject*     t;
struct output output;
int           r;

output.before = 0xDEADBEEF;
output.after  = 0xBEEFDEAD;

v = PyTuple_Pack(2, PyLong_FromLong(10), PyLong_FromLong(11));
FAIL_IF(v == NULL);

t = PyTuple_Pack(2, PyLong_FromLong(20), PyLong_FromLong(21));
FAIL_IF(t == NULL);

input = PyTuple_Pack(2, v, t);
Py_CLEAR(v);
Py_CLEAR(t);
FAIL_IF(input == NULL);

r = depythonify_c_value(@encode(NSRect), input, &output.rect);
FAIL_IF(r < 0);

Py_DECREF(input);

ASSERT_EQUALS(output.rect.origin.x, 10, "%d");
ASSERT_EQUALS(output.rect.origin.y, 11, "%d");
ASSERT_EQUALS(output.rect.size.width, 20, "%d");
ASSERT_EQUALS(output.rect.size.height, 21, "%d");
ASSERT_EQUALS(output.before, 0xDEADBEEF, "%x");
ASSERT_EQUALS(output.after, 0xBEEFDEAD, "%x");

END_UNITTEST

BEGIN_UNITTEST(RemoveFieldNames)
char        buffer[2048];
const char* end;
size_t      i;

/* Simple type */
memset(buffer, '\xab', sizeof(buffer));
end = PyObjCRT_RemoveFieldNames(buffer, "i");
ASSERT(end != NULL);
ASSERT_STREQUALS(buffer, "i");
ASSERT_EQUALS(*end, '\0', "%c");
for (i = strlen(buffer) + 1; i < sizeof(buffer); i++) {
    ASSERT_EQUALS(buffer[i], '\xab', "%c");
}

/* Simple struct */
memset(buffer, '\xab', sizeof(buffer));
end = PyObjCRT_RemoveFieldNames(buffer, "{_NSPoint=\"x1\"f\"y2\"i}");
ASSERT(end != NULL);
ASSERT_STREQUALS(buffer, "{_NSPoint=fi}");
ASSERT_EQUALS(*end, '\0', "%c");
for (i = strlen(buffer) + 1; i < sizeof(buffer); i++) {
    ASSERT_EQUALS(buffer[i], '\xab', "%c");
}

memset(buffer, '\xab', sizeof(buffer));
end = PyObjCRT_RemoveFieldNames(buffer, "{_NSPoint=fi}");
ASSERT(end != NULL);
ASSERT_STREQUALS(buffer, "{_NSPoint=fi}");
ASSERT_EQUALS(*end, '\0', "%c");
for (i = strlen(buffer) + 1; i < sizeof(buffer); i++) {
    ASSERT_EQUALS(buffer[i], '\xab', "%c");
}

/* Simple array */
memset(buffer, '\xab', sizeof(buffer));
end = PyObjCRT_RemoveFieldNames(buffer, "[22f]");
ASSERT(end != NULL);
ASSERT_STREQUALS(buffer, "[22f]");
ASSERT_EQUALS(*end, '\0', "%c");
for (i = strlen(buffer) + 1; i < sizeof(buffer); i++) {
    ASSERT_EQUALS(buffer[i], '\xab', "%c");
}

memset(buffer, '\xab', sizeof(buffer));
end = PyObjCRT_RemoveFieldNames(buffer, "[22{_F=ii}]");
ASSERT(end != NULL);
ASSERT_STREQUALS(buffer, "[22{_F=ii}]");
ASSERT_EQUALS(*end, '\0', "%c");
for (i = strlen(buffer) + 1; i < sizeof(buffer); i++) {
    ASSERT_EQUALS(buffer[i], '\xab', "%c");
}

memset(buffer, '\xab', sizeof(buffer));
end = PyObjCRT_RemoveFieldNames(buffer, "[22{_F=\"ab\"d\"cd\"d}]");
ASSERT(end != NULL);
ASSERT_STREQUALS(buffer, "[22{_F=dd}]");
ASSERT_EQUALS(*end, '\0', "%c");
for (i = strlen(buffer) + 1; i < sizeof(buffer); i++) {
    ASSERT_EQUALS(buffer[i], '\xab', "%c");
}

/* Nested struct */
memset(buffer, '\xab', sizeof(buffer));
end = PyObjCRT_RemoveFieldNames(
    buffer, "[22{_F=\"ab\"{_G=\"x\"f\"y\"f}\"cd\"{_G=\"x\"f\"y\"f}}]");
ASSERT(end != NULL);
ASSERT_STREQUALS(buffer, "[22{_F={_G=ff}{_G=ff}}]");
ASSERT_EQUALS(*end, '\0', "%c");
for (i = strlen(buffer) + 1; i < sizeof(buffer); i++) {
    ASSERT_EQUALS(buffer[i], '\xab', "%c");
}

END_UNITTEST

BEGIN_UNITTEST(UnicodeFunctions)
PyObject* unicode = PyUnicode_FromString("hello world");
int       ok;
ASSERT(unicode != NULL);

ok = PyObjC_is_ascii_string(unicode, "hello world");
ASSERT(ok);

ok = PyObjC_is_ascii_string(unicode, "hello");
ASSERT(!ok);

ok = PyObjC_is_ascii_string(unicode, "hello world!");
ASSERT(!ok);

ok = PyObjC_is_ascii_prefix(unicode, "hello world", 11);
ASSERT(ok);

ok = PyObjC_is_ascii_prefix(unicode, "hello worlk", 11);
ASSERT(!ok);

ok = PyObjC_is_ascii_prefix(unicode, "hello worlk", 10);
ASSERT(ok);

ok = PyObjC_is_ascii_prefix(unicode, "hello", 5);
ASSERT(ok);

ok = PyObjC_is_ascii_prefix(unicode, "hello world!", 12);
ASSERT(!ok);

Py_CLEAR(unicode);

unicode = PyUnicode_FromString("Straße");
ASSERT(unicode != NULL);
ok = PyObjC_is_ascii_prefix(unicode, "hello", 5);
ASSERT(!ok);

ok = PyObjC_is_ascii_string(unicode, "hello");
ASSERT(!ok);

Py_CLEAR(unicode);

END_UNITTEST

BEGIN_UNITTEST(DecimalSize)
long encoded_size = (long)PyObjCRT_SizeOfType(@encode(NSDecimal));
long actual_size  = (long)sizeof(NSDecimal);

ASSERT_EQUALS(encoded_size, actual_size, "%ld");

END_UNITTEST

BEGIN_UNITTEST(DecimalAlign)
long encoded_align = (long)PyObjCRT_AlignOfType(@encode(NSDecimal));
long actual_align  = (long)__alignof__(NSDecimal);

ASSERT_EQUALS(encoded_align, actual_align, "%ld");
END_UNITTEST

BEGIN_UNITTEST(MemView)
PyObject* view = PyObjCMemView_New();

ASSERT(view != NULL);
ASSERT(PyObjCMemView_Check(view));
ASSERT(!PyObjCMemView_Check(Py_True));

Py_buffer* buf = PyObjCMemView_GetBuffer(view);
ASSERT(buf);
ASSERT(!buf->obj);
ASSERT(!PyErr_Occurred());

buf = PyObjCMemView_GetBuffer(Py_True);
ASSERT(!buf);
ASSERT(PyErr_Occurred());
PyErr_Clear();

PyObject* repr = PyObject_Repr(view);
ASSERT(repr);
ASSERT(PyObjC_is_ascii_string(repr, "objc.memview object"));

Py_DECREF(view);
END_UNITTEST

BEGIN_UNITTEST(ReleasedBuffer)
PyObject*         v;
OCReleasedBuffer* buf;

v = PyBytes_FromString("hello world\n");
ASSERT(v);

buf = [[OCReleasedBuffer alloc] initWithPythonBuffer:v writable:NO];
ASSERT(buf);
if (![buf buffer]) {
    [buf release];
    ASSERT(0);
}

if (strncmp([buf buffer], "hello", 5) != 0) {
    [buf release];
    ASSERT(0);
}

[buf release];

buf = [[OCReleasedBuffer alloc] initWithPythonBuffer:v writable:YES];
if (buf) {
    [buf release];
    ASSERT(!buf);
}
ASSERT(PyErr_Occurred());
PyErr_Clear();

v = PyByteArray_FromStringAndSize("hello", 5);
ASSERT(v);
buf = [[OCReleasedBuffer alloc] initWithPythonBuffer:v writable:NO];
ASSERT(buf);
if (![buf buffer]) {
    Py_CLEAR(v);
    [buf release];
    ASSERT(0);
}
if (strncmp([buf buffer], "hello", 5) != 0) {
    Py_CLEAR(v);
    [buf release];
    ASSERT(0);
}

[buf release];

buf = [[OCReleasedBuffer alloc] initWithPythonBuffer:v writable:YES];
ASSERT(buf);
if (![buf buffer]) {
    Py_CLEAR(v);
    [buf release];
    ASSERT(0);
}
if (strncmp([buf buffer], "hello", 5) != 0) {
    Py_CLEAR(v);
    [buf release];
    ASSERT(0);
}
Py_CLEAR(v);
[buf release];

END_UNITTEST

BEGIN_UNITTEST(AlwaysFails)
ASSERT(0 == 1);
END_UNITTEST

BEGIN_UNITTEST(InvalidObjCPointer)

/* Invalid type encodings
 *
 * XXX: This tests are artificial, but at least
 *      ensure that some error paths are hit.
 */
PyObject* p = PyObjCPointer_New(&p, "^{foo=");
ASSERT(PyErr_Occurred());
ASSERT(!p);
PyErr_Clear();

p = PyObjCPointer_New(&p, "{foo=");
ASSERT(PyErr_Occurred());
ASSERT(!p);
PyErr_Clear();

p = PyObjCPointer_New(&p, "X");
ASSERT(PyErr_Occurred());
ASSERT(!p);
PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(InvalidRegistryUsage)
PyObject* bytes = PyBytes_FromString("hello");
if (bytes == NULL) {
    return NULL;
}

int r = PyObjC_AddToRegistry(bytes, bytes, bytes, bytes);
Py_DECREF(bytes);
ASSERT(r == -1);

PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(MethodSignatureString)
PyObjCMethodSignature* sig = PyObjCMethodSignature_WithMetaData("@@:d", NULL, NO);
FAIL_IF(sig == NULL);

PyObject* repr = PyObject_Str((PyObject*)sig);
Py_DECREF(sig);
FAIL_IF(repr == NULL);
if (!PyUnicode_Check(repr)) {
    Py_DECREF(repr);
    FAIL_IF(1);
}
Py_DECREF(repr);
END_UNITTEST

BEGIN_UNITTEST(ValidEncoding)
FAIL_IF(!PyObjCRT_IsValidEncoding("@", 1));
FAIL_IF(PyObjCRT_IsValidEncoding("@", 0));

FAIL_IF(!PyObjCRT_IsValidEncoding("<23f>", 5));
FAIL_IF(PyObjCRT_IsValidEncoding("<23f>", 3));
FAIL_IF(PyObjCRT_IsValidEncoding("<23f>", 4));

FAIL_IF(!PyObjCRT_IsValidEncoding("[23{a=ff}]", 10));
FAIL_IF(PyObjCRT_IsValidEncoding("[23{a=ff}]", 9));
FAIL_IF(PyObjCRT_IsValidEncoding("[23{a=ff}]", 8));
FAIL_IF(PyObjCRT_IsValidEncoding("[23{a=ff}]", 5));
FAIL_IF(PyObjCRT_IsValidEncoding("[23{a=ff}]", 3));

FAIL_IF(!PyObjCRT_IsValidEncoding("{a=ff}", 6));
FAIL_IF(PyObjCRT_IsValidEncoding("{a=ff}", 5));
FAIL_IF(PyObjCRT_IsValidEncoding("{a=ff}", 4));
FAIL_IF(PyObjCRT_IsValidEncoding("{a=ff}", 3));
FAIL_IF(PyObjCRT_IsValidEncoding("{a=ff}", 2));
FAIL_IF(PyObjCRT_IsValidEncoding("{a=ff}", 1));

FAIL_IF(!PyObjCRT_IsValidEncoding("n^{a=i}", 7));
FAIL_IF(PyObjCRT_IsValidEncoding("n^{a=i}", 5));
FAIL_IF(PyObjCRT_IsValidEncoding("n^{a=i}", 2));
FAIL_IF(PyObjCRT_IsValidEncoding("n^{a=i}", 1));
FAIL_IF(PyObjCRT_IsValidEncoding("n^{a=!}", 7));

FAIL_IF(PyObjCRT_IsValidEncoding("{a=\"f\"i}", 8));

FAIL_IF(!PyObjCRT_IsValidEncoding("<2f>", 4));
FAIL_IF(PyObjCRT_IsValidEncoding("<2f", 3));
FAIL_IF(PyObjCRT_IsValidEncoding("<2f>", 3));
FAIL_IF(PyObjCRT_IsValidEncoding("<2ff>", 5));

FAIL_IF(!PyObjCRT_IsValidEncoding("[2f]", 4));
FAIL_IF(PyObjCRT_IsValidEncoding("[2!]", 4));

FAIL_IF(PyObjCRT_IsValidEncoding("(p=ii)", 6));

END_UNITTEST

static int
exception_text_contains(const char* text)
{
    PyObject* type;
    PyObject* value;
    PyObject* traceback;

    PyErr_Fetch(&type, &value, &traceback);
    if (type == NULL && value == NULL && traceback == NULL) {
        /* No exception */
        return 0;
    }

    PyErr_NormalizeException(&type, &value, &traceback);

    PyObject* repr = PyObject_Repr(value);

    Py_CLEAR(type);
    Py_CLEAR(value);
    Py_CLEAR(traceback);
    if (repr == NULL) {
        PyErr_Clear();
        return 0;
    }

    PyObject* expected = PyUnicode_FromString(text);
    if (expected == NULL) {
        Py_CLEAR(repr);
        PyErr_Clear();
        return 0;
    }

    int r = PySequence_Contains(repr, expected);
    if (r == -1) {
        Py_CLEAR(repr);
        Py_CLEAR(expected);
        PyErr_Clear();
        return 0;
    }

    if (r) {
        Py_CLEAR(repr);
        Py_CLEAR(expected);
        return 1;
    }

    PyErr_Format(PyExc_ValueError, "%R does not contain %R", repr, expected);
    Py_CLEAR(expected);
    Py_CLEAR(repr);

    return 0;
}

BEGIN_UNITTEST(CheckArgCount)
/* C test because it hitting the error paths in regular tests
 * is not possible.
 *
 * Also: currently only the core only * uses the this to check
 * the number of arguments in functions with a fixed number
 * of arguments.
 */
int       r;
PyObject* callable = Py_None;

r = PyObjC_CheckArgCount(callable, 1, 1, 1);
FAIL_IF(r == -1);
FAIL_IF(PyErr_Occurred());

r = PyObjC_CheckArgCount(callable, 1, 3, 2);
FAIL_IF(r == -1);
FAIL_IF(PyErr_Occurred());

r = PyObjC_CheckArgCount(callable, 1, 1, 2);
FAIL_IF(r != -1);
FAIL_IF(!exception_text_contains("None expected 1 arguments, got 2"));

r = PyObjC_CheckArgCount(callable, 1, 3, 4);
FAIL_IF(r != -1);
FAIL_IF(!exception_text_contains("None expected between 1 and 3 arguments, got 4"));

END_UNITTEST

BEGIN_UNITTEST(NoKwNames)
/* C test because it hitting the error paths in regular tests
 * is not possible.
 */
int       r;
PyObject* callable = Py_None;
PyObject* kwnames;

r = PyObjC_CheckNoKwnames(callable, NULL);
FAIL_IF(r == -1);
FAIL_IF(PyErr_Occurred());

kwnames = PyList_New(0);
if (kwnames == NULL) {
    goto error;
}

r = PyObjC_CheckNoKwnames(callable, kwnames);
Py_CLEAR(kwnames);
FAIL_IF(r == -1);
FAIL_IF(PyErr_Occurred());

kwnames = PyList_New(0);
if (kwnames == NULL) {
    goto error;
}
if (PyList_Append(kwnames, Py_None) == -1) {
    goto error;
}

r = PyObjC_CheckNoKwnames(callable, kwnames);
Py_CLEAR(kwnames);
FAIL_IF(r != -1);
FAIL_IF(!exception_text_contains("None does not accept keyword arguments"));

r = PyObjC_CheckNoKwnames(callable, callable);
Py_CLEAR(kwnames);
FAIL_IF(r != -1);
PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(PyObjC_NSMethodSignatureToTypeString_Errors)
char               buffer[2048];
char*              result;
NSMethodSignature* sig = [NSURL
    instanceMethodSignatureForSelector:@selector
    (initByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:)];
ASSERT(sig != nil);

result = PyObjC_NSMethodSignatureToTypeString(sig, buffer, 0);
ASSERT(result == NULL);
ASSERT(PyErr_Occurred());
PyErr_Clear();

result = PyObjC_NSMethodSignatureToTypeString(sig, buffer, 4);
ASSERT(result == NULL);
ASSERT(PyErr_Occurred());
PyErr_Clear();

END_UNITTEST

BEGIN_UNITTEST(SkippingTypeSpec)
/* Some tests for 'PyObjCRT_SkipTypeSpec' that hit edge cases that
 * aren't hit in regular code.
 */
const char* ts;
const char* end;
ts = "\"name\"id";

end = PyObjCRT_SkipTypeSpec(ts);
ASSERT(end != NULL);
ASSERT(*end == 'i');
ASSERT(!PyErr_Occurred());

ts  = "@?<v@?@\"BAAssetPack\"@\"NSError\">24f";
end = PyObjCRT_SkipTypeSpec(ts);
ASSERT(end != NULL);
ASSERT(*end == 'f');
ASSERT(!PyErr_Occurred());

ts  = "@?<v@?@\"BAAssetPack\"X\"NSError\">24f";
end = PyObjCRT_SkipTypeSpec(ts);
ASSERT(end == NULL);
ASSERT(PyErr_Occurred());
FAIL_IF(!exception_text_contains("Unhandled type"));
PyErr_Clear();

ts  = "@?<v@?@\"BAAssetPack\"@\"NSError\"";
end = PyObjCRT_SkipTypeSpec(ts);
ASSERT(end == NULL);
ASSERT(PyErr_Occurred());
FAIL_IF(!exception_text_contains("invalid block encoding"));
PyErr_Clear();

END_UNITTEST

static PyMethodDef mod_methods[] = {TESTDEF(CheckNSInvoke),

                                    TESTDEF(VectorSize),
                                    TESTDEF(VectorAlign),
                                    TESTDEF(StructSize),
                                    TESTDEF(BitFieldSize),
                                    TESTDEF(StructAlign),
                                    TESTDEF(FillStruct1),
                                    TESTDEF(FillStruct2),
                                    TESTDEF(FillStruct3),
                                    TESTDEF(FillStruct4),
                                    TESTDEF(FillStruct5Array),
                                    TESTDEF(ExtractStruct1),
                                    TESTDEF(ExtractStruct2),
                                    TESTDEF(ExtractStruct3),
                                    TESTDEF(ExtractStruct4),
                                    TESTDEF(ExtractStruct5Array),
#ifdef _C_BOOL
                                    TESTDEF(TestSizeOfBool),
#endif
                                    TESTDEF(TestTypeCode),
                                    TESTDEF(TestSimplifySignature),
                                    TESTDEF(TestArrayCoding),
                                    TESTDEF(PythonListAsNSArray),
                                    TESTDEF(PythonTupleAsNSArray),
                                    TESTDEF(PythonDictAsNSDictionary),
                                    TESTDEF(NSLogging),
                                    TESTDEF(FillNSRect),
                                    TESTDEF(RemoveFieldNames),
                                    TESTDEF(UnicodeFunctions),
                                    TESTDEF(DecimalSize),
                                    TESTDEF(DecimalAlign),
                                    TESTDEF(MemView),
                                    TESTDEF(ReleasedBuffer),
                                    TESTDEF(AlwaysFails),
                                    TESTDEF(InvalidObjCPointer),
                                    TESTDEF(InvalidRegistryUsage),
                                    TESTDEF(MethodSignatureString),
                                    TESTDEF(ValidEncoding),
                                    TESTDEF(CheckArgCount),
                                    TESTDEF(NoKwNames),
                                    TESTDEF(PyObjC_NSMethodSignatureToTypeString_Errors),
                                    TESTDEF(SkippingTypeSpec),
                                    {0, 0, 0, 0}};

int
PyObjC_init_ctests(PyObject* m)
{
    PyObject* d = PyDict_New();
    if (d == NULL) {
        return -1; // LCOV_EXCL_LINE
    }

    PyMethodDef* cur;
    for (cur = mod_methods; cur->ml_name != NULL; cur++) {
        PyObject* meth = PyCFunction_NewEx(cur, NULL, NULL);
        if (meth == NULL) { // LCOV_BR_EXCL_LINE
            Py_DECREF(d);   // LCOV_EXCL_LINE
            return -1;      // LCOV_EXCL_LINE
        }

        PyObject* key = PyUnicode_FromString(cur->ml_name);
        if (key == NULL) {   // LCOV_BR_EXCL_LINE
            Py_DECREF(d);    // LCOV_EXCL_LINE
            Py_DECREF(meth); // LCOV_EXCL_LINE
            return -1;
        }
        if (PyDict_SetItem(d, key, meth) < 0) { // LCOV_BR_EXCL_LINE
            Py_DECREF(d);                       // LCOV_EXCL_LINE
            Py_DECREF(meth);                    // LCOV_EXCL_LINE
            Py_DECREF(key);                     // LCOV_EXCL_LINE
            return -1;                          // LCOV_EXCL_LINE
        }
        Py_DECREF(meth);
        Py_DECREF(key);
    }

    return PyModule_AddObject(m, "_ctests", d);
}

// LCOV_BR_EXCL_STOP
// LCOV_EXCL_STOP

NS_ASSUME_NONNULL_END
