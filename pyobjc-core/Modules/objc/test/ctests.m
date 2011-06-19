/*
 * This file contains some unittests for specific functions in the extension 
 * module. 
 *
 * The PyObjC unittest objc.test.test_ctests executes the tests in this file.
 */
#include "Python.h"
#include "pyobjc-api.h"
#include "pyobjc-compat.h"

#if PY_VERSION_HEX >= 0x03000000
#define PyInt_AsLong PyLong_AsLong
#endif
#include "pyobjc-unittest.h"


#include <fcntl.h>

#import <Foundation/Foundation.h>

struct Struct1 {
	int f1;
	double f2;
};

struct Struct2 {
	int f1;
	double f2;
	short s[5];
};

struct Struct3 {
	char ch;
	int  i;
};

struct Struct4 {
	char ch;
	long long i;
};

struct Struct5 {
	long i;
	char ch;
};

typedef struct Struct5 Struct5Array[2];



/* Helper stuff for TestNSInvoke */

static struct Struct2 invokeHelper = { 0, 0, { 0, 0, 0, 0, 0 } };

@interface PyObjCTest_NSInvoke : NSObject
{
}
-(void)methodWithMyStruct: (struct Struct2)val1 andShort:(short)val2;
@end

@implementation PyObjCTest_NSInvoke 
-(void)methodWithMyStruct: (struct Struct2)val1 andShort:(short)val2
{
	(void)val2;
	invokeHelper = val1;
}
@end

BEGIN_UNITTEST(CheckNSInvoke)
	/* This is not a 'real' unittest, but is used to disable a number of
	 * other tests (in objc.test.test_methods2) when NSInvocation isn't
	 * working correctly (MacOS X at least upto 10.2.6).
	 * [Panther previews also have this problem]
	 *
	 * Leopard is even worse, this test causes a crash of the interpreter when
         * running on PPC64.
	 */
#ifdef __ppc64__
	ASSERT_EQUALS(0, 1, "%d");
#endif

	PyObjCTest_NSInvoke* obj = [[PyObjCTest_NSInvoke alloc] init];
	NSInvocation* inv;
	struct Struct2 v1 = { 1, 2, { 3, 4, 5, 6, 7 } };
	short    v2 = 8;

	[obj methodWithMyStruct: v1 andShort: v2];
	inv = [NSInvocation invocationWithMethodSignature:
		[obj methodSignatureForSelector:@selector(methodWithMyStruct:andShort:)]];
	[inv setTarget: obj];
	[inv setSelector: @selector(methodWithMyStruct:andShort:)];
	[inv setArgument: &v1 atIndex: 2];
	[inv setArgument: &v2 atIndex: 3];

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


BEGIN_UNITTEST(StructSize)

	ASSERT_EQUALS(
	    sizeof(struct Struct1), PyObjCRT_SizeOfType(@encode(struct Struct1)),
	    "%d");

	ASSERT_EQUALS(
	    sizeof(struct Struct2), PyObjCRT_SizeOfType(@encode(struct Struct2)),
	    "%d");

	ASSERT_EQUALS(
	    sizeof(struct Struct3), PyObjCRT_SizeOfType(@encode(struct Struct3)),
	    "%d");

	ASSERT_EQUALS(
	    sizeof(struct Struct4), PyObjCRT_SizeOfType(@encode(struct Struct4)),
	    "%d");

	ASSERT_EQUALS(
	    sizeof(NSRect), PyObjCRT_SizeOfType(@encode(NSRect)), "%d");

END_UNITTEST

BEGIN_UNITTEST(StructAlign)

	ASSERT_EQUALS(
	    __alignof__(struct Struct1), 
	    PyObjCRT_AlignOfType(@encode(struct Struct1)),
	    "%d");

	ASSERT_EQUALS(
	    __alignof__(struct Struct2), 
	    PyObjCRT_AlignOfType(@encode(struct Struct2)),
	    "%d");

	ASSERT_EQUALS(
	    __alignof__(struct Struct3), 
	    PyObjCRT_AlignOfType(@encode(struct Struct3)),
	    "%d");

	ASSERT_EQUALS(
	    __alignof__(struct Struct4), 
	    PyObjCRT_AlignOfType(@encode(struct Struct4)),
	    "%d");

END_UNITTEST


BEGIN_UNITTEST(FillStruct1)

	PyObject* input;
	struct Struct1 output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	PyTuple_SetItem(input, 0, PyInt_FromLong(1));
	PyTuple_SetItem(input, 1, PyFloat_FromDouble(2));
	
	r = PyObjC_PythonToObjC(@encode(struct Struct1), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.f1, 1, "%d");
	ASSERT_EQUALS(output.f2, 2.0, "%g");

END_UNITTEST

BEGIN_UNITTEST(FillStruct2)

	PyObject* input;
	PyObject* v;
	struct Struct2 output;
	int r;

	input = PyTuple_New(3);
	FAIL_IF(input == NULL);

	v = PyTuple_New(5);
	PyTuple_SetItem(v, 0, PyInt_FromLong(10));
	PyTuple_SetItem(v, 1, PyInt_FromLong(11));
	PyTuple_SetItem(v, 2, PyInt_FromLong(12));
	PyTuple_SetItem(v, 3, PyInt_FromLong(13));
	PyTuple_SetItem(v, 4, PyInt_FromLong(14));

	PyTuple_SetItem(input, 0, PyInt_FromLong(1));
	PyTuple_SetItem(input, 1, PyFloat_FromDouble(2));
	PyTuple_SetItem(input, 2, v);
	
	r = PyObjC_PythonToObjC(@encode(struct Struct2), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.f1, 1,    "%d");
	ASSERT_EQUALS(output.f2, 2.0,  "%g");
	ASSERT_EQUALS(output.s[0], 10, "%d");
	ASSERT_EQUALS(output.s[1], 11, "%d");
	ASSERT_EQUALS(output.s[2], 12, "%d");
	ASSERT_EQUALS(output.s[3], 13, "%d");
	ASSERT_EQUALS(output.s[4], 14, "%d");

END_UNITTEST

BEGIN_UNITTEST(FillStruct3)

	PyObject* input;
	struct Struct3 output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	PyTuple_SetItem(input, 0,  PyBytes_FromStringAndSize("\001", 1));
	PyTuple_SetItem(input, 1, PyInt_FromLong(2));
	
	r = PyObjC_PythonToObjC(@encode(struct Struct3), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.ch, '\001',    "%d");
	ASSERT_EQUALS(output.i, 2,  "%d");

END_UNITTEST

BEGIN_UNITTEST(FillStruct4)

	PyObject* input;
	struct Struct4 output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	PyTuple_SetItem(input, 0,  PyBytes_FromStringAndSize("\001", 1));
	PyTuple_SetItem(input, 1, PyInt_FromLong(500000));
	
	r = PyObjC_PythonToObjC(@encode(struct Struct4), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.ch, '\001',    "%d");
	ASSERT_EQUALS(output.i, 500000,  "%ll");

END_UNITTEST

BEGIN_UNITTEST(FillStruct5Array)

	PyObject* input;
	PyObject* v;
	Struct5Array output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	v = PyTuple_New(2);
	PyTuple_SetItem(v, 0, PyInt_FromLong(500000));
	PyTuple_SetItem(v, 1,  PyBytes_FromStringAndSize("\001", 1));
	PyTuple_SetItem(input, 0, v);

	v = PyTuple_New(2);
	PyTuple_SetItem(v, 0, PyInt_FromLong(1000000));
	PyTuple_SetItem(v, 1,  PyBytes_FromStringAndSize("\002", 1));
	PyTuple_SetItem(input, 1, v);
	
	r = PyObjC_PythonToObjC(@encode(Struct5Array), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output[0].ch, '\001',    "%d");
	ASSERT_EQUALS(output[0].i, 500000,  "%ll");
	ASSERT_EQUALS(output[1].ch, '\002',    "%d");
	ASSERT_EQUALS(output[1].i, 1000000,  "%ll");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct1) 

	struct Struct1 input;
	PyObject* output;

	input.f1 = 1;
	input.f2 = 2;

	output = PyObjC_ObjCToPython(@encode(struct Struct1), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Int);
#else
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
#endif
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Float);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GetItem(output, 1)), 2.0, "%g");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct2) 

	struct Struct2 input;
	PyObject* output;
	PyObject* tup;
	PyObject* v;

	input.f1 = 1;
	input.f2 = 2;
	input.s[0] = 3;
	input.s[1] = 4;
	input.s[2] = 5;
	input.s[3] = 6;
	input.s[4] = 7;

	output = PyObjC_ObjCToPython(@encode(struct Struct2), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 3, "%d");
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Int);
#else
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
#endif
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Float);
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 2), Tuple);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GetItem(output, 1)), 2.0, "%g");

	tup = PyTuple_GetItem(output, 2);
	ASSERT_EQUALS(PyTuple_GET_SIZE(tup), 5, "%d");

	v = PyTuple_GetItem(tup, 0);
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(v, Int);
#else
	ASSERT_ISINSTANCE(v, Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(v), 3, "%d");

	v = PyTuple_GetItem(tup, 1);
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(v, Int);
#else
	ASSERT_ISINSTANCE(v, Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(v), 4, "%d");

	v = PyTuple_GetItem(tup, 2);
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(v, Int);
#else
	ASSERT_ISINSTANCE(v, Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(v), 5, "%d");

	v = PyTuple_GetItem(tup, 3);
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(v, Int);
#else
	ASSERT_ISINSTANCE(v, Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(v), 6, "%d");

	v = PyTuple_GetItem(tup, 4);
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(v, Int);
#else
	ASSERT_ISINSTANCE(v, Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(v), 7, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct3) 

	struct Struct3 input;
	PyObject* output;

	input.ch = 1;
	input.i = 2;

	output = PyObjC_ObjCToPython(@encode(struct Struct3), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Int);
#else
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(output, 1)), 2, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct4) 

	struct Struct4 input;
	PyObject* output;

	input.ch = 1;
	input.i = 500000;

	output = PyObjC_ObjCToPython(@encode(struct Struct4), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Int);
#ifdef __LP64__
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Int);
#else
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Long);
#endif
#else
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 0), Long);
	ASSERT_ISINSTANCE(PyTuple_GetItem(output, 1), Long);
#endif

	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(output, 1)), 500000, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct5Array) 

	Struct5Array input;
	PyObject* output;
	PyObject* v;

	input[0].ch = 1;
	input[0].i = 500000;
	input[1].ch = 2;
	input[1].i = 1000000;

	output = PyObjC_ObjCToPython(@encode(Struct5Array), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");

	v = PyTuple_GetItem(output, 0);
	ASSERT_ISINSTANCE(v, Tuple);
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 1), Int);
#else
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 0), Long);
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 1), Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(v, 0)), 500000, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(v, 1)), 1, "%d");

	v = PyTuple_GetItem(output, 1);
	ASSERT_ISINSTANCE(v, Tuple);
#if PY_VERSION_HEX < 0x03000000
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 1), Int);
#else
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 0), Long);
	ASSERT_ISINSTANCE(PyTuple_GetItem(v, 1), Long);
#endif
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(v, 0)), 1000000, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GetItem(v, 1)), 2, "%d");

END_UNITTEST

#ifdef _C_BOOL

BEGIN_UNITTEST(TestSizeOfBool)

	/* Code in libffi_support.m depends on this equality. */
#if defined(__ppc__) || defined(__ppc64__)
	ASSERT_EQUALS(sizeof(bool), sizeof(int), "%d");

#else
	ASSERT_EQUALS(sizeof(bool), sizeof(char), "%d");
#endif

END_UNITTEST

#endif

BEGIN_UNITTEST(TestTypeCode)
	
	/* These are manually defined on some platforms */
	ASSERT_EQUALS(@encode(long long)[0], 'q', "%c");
	ASSERT_EQUALS(@encode(unsigned long long)[0], 'Q', "%c");

#if defined(MACOSX) &&  MAC_OS_X_VERSION_MAX_ALLOWED > MAC_OS_X_VERSION_10_1
	ASSERT_EQUALS(@encode(bool)[0], 'B', "%#x");
#endif

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
	NSMutableArray* a;
	NSObject* v;
	int haveException;

	NSAutoreleasePool* p;

	p = [[NSAutoreleasePool alloc] init];

	d = [NSMutableDictionary dictionary];

	[d setObject:@"foo" forKey:@"keyM"];

	a = [NSMutableArray arrayWithObjects: d, nil];

	NS_DURING
		v = [a valueForKey:@"keyM"];	
		haveException = 0;
	NS_HANDLER
		v = nil;
		haveException = 1;
	NS_ENDHANDLER

	[p release];

	ASSERT(!haveException);
END_UNITTEST


BEGIN_UNITTEST(PythonListAsNSArray)
	PyObject* aList;
	NSMutableArray* array;
	NSArray* array2;
	
	aList = Py_BuildValue("[iiiii]", 0, 1, 2, 3, 4);
	FAIL_IF(aList == NULL);

	array = PyObjC_PythonToId(aList);
	FAIL_IF(array == nil);

	/* Check lenght */
	ASSERT_EQUALS(5, [array count], "%d");	

	/* Check basic element access */
	ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);
	ASSERT([[NSNumber numberWithInt:2] isEqual:[array objectAtIndex:2]]);
	ASSERT([[NSNumber numberWithInt:3] isEqual:[array objectAtIndex:3]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

	/* Check some other methods */
	array2 = [array arrayByAddingObject: [NSNumber numberWithInt:5]];
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
	[array addObject: [NSNumber numberWithInt:5]];
	ASSERT_EQUALS(6, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:5] isEqual:[array objectAtIndex:5]]);

	[array removeLastObject];
	ASSERT_EQUALS(5, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

	[array insertObject: [NSNumber numberWithInt:6] atIndex: 1];
	ASSERT_EQUALS(6, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:6] isEqual:[array objectAtIndex:1]]);

	[array removeObjectAtIndex: 1];
	ASSERT_EQUALS(5, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);

	[array replaceObjectAtIndex: 1 withObject: [NSNumber numberWithInt:7]];
	ASSERT_EQUALS(5, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:7] isEqual:[array objectAtIndex:1]]);

END_UNITTEST

BEGIN_UNITTEST(PythonTupleAsNSArray)
	PyObject* aTuple;
	NSArray* array;
	NSArray* array2;

	aTuple = Py_BuildValue("(iiiii)", 0, 1, 2, 3, 4);
	FAIL_IF(aTuple == NULL);

	array = PyObjC_PythonToId(aTuple);
	FAIL_IF(array == nil);

	/* Check lenght */
	ASSERT_EQUALS(5, [array count], "%d");	

	/* Check basic element access */
	ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);
	ASSERT([[NSNumber numberWithInt:2] isEqual:[array objectAtIndex:2]]);
	ASSERT([[NSNumber numberWithInt:3] isEqual:[array objectAtIndex:3]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

	/* Check some other methods */
	array2 = [array arrayByAddingObject: [NSNumber numberWithInt:5]];
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
	PyObject* aDictionary;
	NSMutableDictionary* dict;
	NSEnumerator* iter;
	NSArray* keys;

	aDictionary = Py_BuildValue(
		"{iiiiiiii}",
		1, 2, 
		2, 4, 
		3, 6,
		4, 8
	);
	FAIL_IF(aDictionary == NULL);

	dict = PyObjC_PythonToId(aDictionary);
	FAIL_IF(dict == nil);

	ASSERT_EQUALS(4, [dict count], "%d");
	ASSERT([
		[dict objectForKey:[NSNumber numberWithInt:1]] 
			isEqual: [NSNumber numberWithInt: 2]]);

	[dict setObject: [NSNumber numberWithInt:10]
	      forKey: [NSNumber numberWithInt:5]];
	ASSERT_EQUALS(5, [dict count], "%d");
	ASSERT([
		[dict objectForKey:[NSNumber numberWithInt:5]] 
			isEqual: [NSNumber numberWithInt: 10]]);

	[dict removeObjectForKey: [NSNumber numberWithInt:5]];
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
	 * can be logged. This used to be impossible upto (and including)
	 * release 1.1!
	 */
	PyObject* o = (PyObject*)(Py_BuildValue("i", 10)->ob_type);
	NSObject* value;
	int fd;
	int stderr_orig;
	int r;

	value = PyObjC_PythonToId(o);
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
		NSRect rect;
		unsigned int after;
	};


	PyObject* input;
	PyObject* v;
	PyObject* t;
	struct output output;
	int r;

	output.before = 0xDEADBEEF;
	output.after = 0xBEEFDEAD;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	v= PyTuple_New(2);
	PyTuple_SetItem(v, 0, PyInt_FromLong(10));
	PyTuple_SetItem(v, 1, PyInt_FromLong(11));

	t= PyTuple_New(2);
	PyTuple_SetItem(t, 0, PyInt_FromLong(20));
	PyTuple_SetItem(t, 1, PyInt_FromLong(21));

	PyTuple_SetItem(input, 0, v);
	PyTuple_SetItem(input, 1, t);
	
	r = PyObjC_PythonToObjC(@encode(NSRect), input, &output.rect);
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
	char buffer[2048];
	const char* end;
	size_t i;

	/* Simple type */
	memset(buffer, '\xab', sizeof(buffer));
	end = PyObjCRT_RemoveFieldNames(buffer, "i");
	ASSERT(end != NULL);
	ASSERT_STREQUALS(buffer, "i");
	ASSERT_EQUALS(*end, '\0', "%c");
	for (i = strlen(buffer)+1; i < sizeof(buffer);i++) {
		ASSERT_EQUALS(buffer[i], '\xab', "%c");
	}

	/* Simple struct */
	memset(buffer, '\xab', sizeof(buffer));
	end = PyObjCRT_RemoveFieldNames(buffer, "{_NSPoint=\"x1\"f\"y2\"i}");
	ASSERT(end != NULL);
	ASSERT_STREQUALS(buffer, "{_NSPoint=fi}");
	ASSERT_EQUALS(*end, '\0', "%c");
	for (i = strlen(buffer)+1; i < sizeof(buffer);i++) {
		ASSERT_EQUALS(buffer[i], '\xab', "%c");
	}

	memset(buffer, '\xab', sizeof(buffer));
	end = PyObjCRT_RemoveFieldNames(buffer, "{_NSPoint=fi}");
	ASSERT(end != NULL);
	ASSERT_STREQUALS(buffer, "{_NSPoint=fi}");
	ASSERT_EQUALS(*end, '\0', "%c");
	for (i = strlen(buffer)+1; i < sizeof(buffer);i++) {
		ASSERT_EQUALS(buffer[i], '\xab', "%c");
	}

	/* Simple array */
	memset(buffer, '\xab', sizeof(buffer));
	end = PyObjCRT_RemoveFieldNames(buffer, "[22f]");
	ASSERT(end != NULL);
	ASSERT_STREQUALS(buffer, "[22f]");
	ASSERT_EQUALS(*end, '\0', "%c");
	for (i = strlen(buffer)+1; i < sizeof(buffer);i++) {
		ASSERT_EQUALS(buffer[i], '\xab', "%c");
	}

	memset(buffer, '\xab', sizeof(buffer));
	end = PyObjCRT_RemoveFieldNames(buffer, "[22{_F=ii}]");
	ASSERT(end != NULL);
	ASSERT_STREQUALS(buffer, "[22{_F=ii}]");
	ASSERT_EQUALS(*end, '\0', "%c");
	for (i = strlen(buffer)+1; i < sizeof(buffer);i++) {
		ASSERT_EQUALS(buffer[i], '\xab', "%c");
	}

	memset(buffer, '\xab', sizeof(buffer));
	end = PyObjCRT_RemoveFieldNames(buffer, "[22{_F=\"ab\"d\"cd\"d}]");
	ASSERT(end != NULL);
	ASSERT_STREQUALS(buffer, "[22{_F=dd}]");
	ASSERT_EQUALS(*end, '\0', "%c");
	for (i = strlen(buffer)+1; i < sizeof(buffer);i++) {
		ASSERT_EQUALS(buffer[i], '\xab', "%c");
	}

	/* Nested struct */
	memset(buffer, '\xab', sizeof(buffer));
	end = PyObjCRT_RemoveFieldNames(buffer, "[22{_F=\"ab\"{_G=\"x\"f\"y\"f}\"cd\"{_G=\"x\"f\"y\"f}}]");
	ASSERT(end != NULL);
	ASSERT_STREQUALS(buffer, "[22{_F={_G=ff}{_G=ff}}]");
	ASSERT_EQUALS(*end, '\0', "%c");
	for (i = strlen(buffer)+1; i < sizeof(buffer);i++) {
		ASSERT_EQUALS(buffer[i], '\xab', "%c");
	}

END_UNITTEST

BEGIN_UNITTEST(UnicodeFunctions)
	PyObject* unicode = PyUnicode_FromString("hello world");
	int ok;

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
	ASSERT(ok);

END_UNITTEST

static PyMethodDef mod_methods[] = {
	TESTDEF(CheckNSInvoke),

	TESTDEF(StructSize),
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
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"ctests",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit_ctests(void);

PyObject*
PyInit_ctests(void)

#else

#define INITERROR() return
#define INITDONE() return

void initctests(void);

void
initctests(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("ctests", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	INITDONE();
}
