/*
 * This file contains some unittests for specific functions in the extension 
 * module. 
 *
 * The PyObjC unittest objc.test.test_ctests executes the tests in this file.
 *
 * TODO:
 * - check PyObjCRT_SizeOfType
 * - check PyObjCRT_AlignOfType
 * - check pythonify_c_value
 * - check depythonify_c_value
 *
 * All at least for structured types, the basic types have fairly trivial 
 * implementations.
 *
 * This currently only tests a number of problematic structs.
 */
#include "pyobjc-api.h"
#include "pyobjc-unittest.h"

#import <Foundation/NSInvocation.h>

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

#ifndef GNU_RUNTIME


BEGIN_UNITTEST(CheckNSInvoke)
	/* This is not a 'real' unittest, but is used to disable a number of
	 * other tests (in objc.test.test_methods2) when NSInvocation isn't
	 * working correctly (MacOS X at least upto 10.2.6).
	 * [Panther previews also have this problem]
	 *
	 * GNUstep is even worse, this test causes a crash of the interpreter,
	 */
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
	ASSERT_EQUALS(invokeHelper.f1, v1.f1, "%d");
	ASSERT_EQUALS(invokeHelper.f2, v1.f2, "%g");
	ASSERT_EQUALS(invokeHelper.s[0], v1.s[0], "%d");
	ASSERT_EQUALS(invokeHelper.s[1], v1.s[1], "%d");
	ASSERT_EQUALS(invokeHelper.s[2], v1.s[2], "%d");
	ASSERT_EQUALS(invokeHelper.s[3], v1.s[3], "%d");
	ASSERT_EQUALS(invokeHelper.s[4], v1.s[4], "%d");

END_UNITTEST

#else

BEGIN_UNITTEST(CheckNSInvoke)
	/* Force failure, see comment above */
	ASSERT_EQUALS(0, 1, "%d");
END_UNITTEST

#endif


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

END_UNITTEST


BEGIN_UNITTEST(FillStruct1)

	PyObject* input;
	struct Struct1 output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	PyTuple_SET_ITEM(input, 0, PyInt_FromLong(1));
	PyTuple_SET_ITEM(input, 1, PyFloat_FromDouble(2));
	
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
	PyTuple_SET_ITEM(v, 0, PyInt_FromLong(10));
	PyTuple_SET_ITEM(v, 1, PyInt_FromLong(11));
	PyTuple_SET_ITEM(v, 2, PyInt_FromLong(12));
	PyTuple_SET_ITEM(v, 3, PyInt_FromLong(13));
	PyTuple_SET_ITEM(v, 4, PyInt_FromLong(14));

	PyTuple_SET_ITEM(input, 0, PyInt_FromLong(1));
	PyTuple_SET_ITEM(input, 1, PyFloat_FromDouble(2));
	PyTuple_SET_ITEM(input, 2, v);
	
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

	PyTuple_SET_ITEM(input, 0,  PyString_FromStringAndSize("\001", 1));
	PyTuple_SET_ITEM(input, 1, PyInt_FromLong(2));
	
	r = PyObjC_PythonToObjC(@encode(struct Struct3), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.ch, '\001',    "%d");
	ASSERT_EQUALS(output.i, 2,  "%d");

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
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 1), Float);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GET_ITEM(output, 1)), 2.0, "%g");

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
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 1), Float);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 2), Tuple);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GET_ITEM(output, 1)), 2.0, "%g");

	tup = PyTuple_GET_ITEM(output, 2);
	ASSERT_EQUALS(PyTuple_GET_SIZE(tup), 5, "%d");

	v = PyTuple_GET_ITEM(tup, 0);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 3, "%d");

	v = PyTuple_GET_ITEM(tup, 1);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 4, "%d");

	v = PyTuple_GET_ITEM(tup, 2);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 5, "%d");

	v = PyTuple_GET_ITEM(tup, 3);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 6, "%d");

	v = PyTuple_GET_ITEM(tup, 4);
	ASSERT_ISINSTANCE(v, Int);
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
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 1), Int);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 1)), 2, "%d");

END_UNITTEST

#ifdef _C_BOOL

BEGIN_UNITTEST(TestSizeOfBool)

	// Code in libffi_support.m depends on this equality.
	ASSERT_EQUALS(sizeof(bool), sizeof(int), "%d");

END_UNITTEST

#endif

BEGIN_UNITTEST(TestTypeCode)
	
	/* These are manually defined on some platforms */
	ASSERT_EQUALS(@encode(long long)[0], 'q', "%c");
	ASSERT_EQUALS(@encode(unsigned long long)[0], 'Q', "%c");

#if defined(MACOSX) &&  MAC_OS_X_VERSION_MAX_ALLOWED > MAC_OS_X_VERSION_10_1
	ASSERT_EQUALS(@encode(bool)[0], 'B', "%c");
#endif

END_UNITTEST

BEGIN_UNITTEST(TestSimplifySignature)
	/* Make sure PyObjCRT_SimplifySignature works */
	char b[1024];

	PyObjCRT_SimplifySignature("@1234@0:{_NSPoint=ff}02i22", b, sizeof(b));
	ASSERT_STREQUALS("@@:{_NSPoint=ff}i", b);

	PyObjCRT_SimplifySignature("@@:{_NSPoint=ff}i", b, sizeof(b));
	ASSERT_STREQUALS("@@:{_NSPoint=ff}i", b);
END_UNITTEST


static PyMethodDef unittest_methods[] = {
	TESTDEF(CheckNSInvoke),

	TESTDEF(StructSize),	
	TESTDEF(StructAlign),	
	TESTDEF(FillStruct1),	
	TESTDEF(FillStruct2),	
	TESTDEF(FillStruct3),	
	TESTDEF(ExtractStruct1),	
	TESTDEF(ExtractStruct2),	
	TESTDEF(ExtractStruct3),	
#ifdef _C_BOOL
	TESTDEF(TestSizeOfBool),	
#endif
	TESTDEF(TestTypeCode),	
	TESTDEF(TestSimplifySignature),	
	{ 0, 0, 0, 0 }
};

void initctests(void);
void initctests(void)
{
	PyObject* m;

	m = Py_InitModule4("ctests", unittest_methods, NULL,
			                        NULL, PYTHON_API_VERSION);


	PyObjC_ImportAPI(m);
}
