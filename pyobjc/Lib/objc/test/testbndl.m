/*
 * This file implements a (number of) class(es) that are used to test
 * method calling with PyObjC (both python -> ObjC and back)
 */
#import <Foundation/Foundation.h>

#include <Python.h>
#include <pyobjc-api.h>

struct dummy
{
	int f1;
	int f2;
};

struct dummy2
{
	int array[100];
};



@interface OC_TestClass1 : NSObject
{
}

/* Reset the test counter */
+ (void)clsReset;
- (void)reset;


/* Test return values, return various values */
+ (long long)longlongClsFunc;
+ (unsigned long long)ulonglongClsFunc;
+ (long)longClsFunc;
+ (unsigned long)ulongClsFunc;
+ (int)intClsFunc;
+ (unsigned int)uintClsFunc;
+ (short)shortClsFunc;
+ (unsigned short)ushortClsFunc;
+ (char)charClsFunc;
+ (unsigned char)ucharClsFunc;
+ (float)floatClsFunc;
+ (double)doubleClsFunc;

- (long long)longlongFunc;
- (unsigned long long)ulonglongFunc;
- (long)longFunc;
- (unsigned long)ulongFunc;
- (int)intFunc;
- (unsigned int)uintFunc;
- (short)shortFunc;
- (unsigned short)ushortFunc;
- (char)charFunc;
- (unsigned char)ucharFunc;
- (float)floatFunc;
- (double)doubleFunc;

/* returns of complex values */
- (struct dummy)dummyFunc;
- (struct dummy2)dummy2Func;

@end

@implementation OC_TestClass1

#define ARRAYSIZE(a) (sizeof(a)/sizeof(a[0]))
static int g_idx = 0;
static unsigned long long g_ulonglongs[] = {
	0, 42, (1LL << 63)
};
static unsigned long g_ulongs[] = {
	0, 42, (1 << 30)
};
static long long g_longlongs[] = {
	-(1LL << 60), -42, 0, 42, (1LL << 60)
};
static long g_longs[] = {
	-(1 << 30), -42, 0, 42, (1 << 30)
};
static int g_ints[] = {
	-(1 << 30), -42, 0, 42, (1 << 30)
};
static unsigned int g_uints[] = {
	0, 42, 1 << 30
};
static short g_shorts[] = {
	-(1 << 14), -42, 0, 42, (1 << 14)
};
static unsigned short g_ushorts[] = {
	0, 42, 1 << 14
};
static char g_chars[] = {
	-128, 0, 127
};
static unsigned char g_uchars[] = {
	0, 128, 255
};
static float g_floats[] = {
	0.128, 1.0, 42.0, 1e10
};
static double g_doubles[] = {
	0.128, 1.0, 42.0, 1e10
};

+ (void)clsReset
{
	g_idx = 0;
}

+ (long long)longlongClsFunc;
{
	if (g_idx > ARRAYSIZE(g_longlongs)) g_idx = 0;
	return g_longlongs[g_idx++];
}

+ (unsigned long long)ulonglongClsFunc
{
	if (g_idx > ARRAYSIZE(g_ulonglongs)) g_idx = 0;
	return g_ulonglongs[g_idx++];
}

+ (long)longClsFunc;
{
	if (g_idx > ARRAYSIZE(g_longs)) g_idx = 0;
	return g_longs[g_idx++];
}

+ (unsigned long)ulongClsFunc
{
	if (g_idx > ARRAYSIZE(g_ulongs)) g_idx = 0;
	return g_ulongs[g_idx++];
}

+ (int)intClsFunc;
{
	if (g_idx > ARRAYSIZE(g_ints)) g_idx = 0;
	return g_ints[g_idx++];
}

+ (unsigned int)uintClsFunc
{
	if (g_idx > ARRAYSIZE(g_uints)) g_idx = 0;
	return g_uints[g_idx++];
}

+ (short)shortClsFunc
{
	if (g_idx > ARRAYSIZE(g_shorts)) g_idx = 0;
	return g_shorts[g_idx++];
}

+ (unsigned short)ushortClsFunc
{
	if (g_idx > ARRAYSIZE(g_ushorts)) g_idx = 0;
	return g_ushorts[g_idx++];
}

+ (char)charClsFunc;
{
	if (g_idx > ARRAYSIZE(g_chars)) g_idx = 0;
	return g_chars[g_idx++];
}

+ (unsigned char)ucharClsFunc;
{
	if (g_idx > ARRAYSIZE(g_uchars)) g_idx = 0;
	return g_uchars[g_idx++];
}

+ (float)floatClsFunc;
{
	if (g_idx > ARRAYSIZE(g_floats)) g_idx = 0;
	return g_floats[g_idx++];
}

+ (double)doubleClsFunc;
{
	if (g_idx > ARRAYSIZE(g_doubles)) g_idx = 0;
	return g_doubles[g_idx++];
}

- (void)reset
{
	g_idx = 0;
}

- (long long)longlongFunc;
{
	if (g_idx > ARRAYSIZE(g_longlongs)) g_idx = 0;
	return g_longlongs[g_idx++];
}

- (unsigned long long)ulonglongFunc
{
	if (g_idx > ARRAYSIZE(g_ulonglongs)) g_idx = 0;
	return g_ulonglongs[g_idx++];
}

- (long)longFunc;
{
	if (g_idx > ARRAYSIZE(g_longs)) g_idx = 0;
	return g_longs[g_idx++];
}

- (unsigned long)ulongFunc
{
	if (g_idx > ARRAYSIZE(g_ulongs)) g_idx = 0;
	return g_ulongs[g_idx++];
}

- (int)intFunc;
{
	if (g_idx > ARRAYSIZE(g_ints)) g_idx = 0;
	return g_ints[g_idx++];
}

- (unsigned int)uintFunc
{
	if (g_idx > ARRAYSIZE(g_uints)) g_idx = 0;
	return g_uints[g_idx++];
}

- (short)shortFunc
{
	if (g_idx > ARRAYSIZE(g_shorts)) g_idx = 0;
	return g_shorts[g_idx++];
}

- (unsigned short)ushortFunc
{
	if (g_idx > ARRAYSIZE(g_ushorts)) g_idx = 0;
	return g_ushorts[g_idx++];
}

- (char)charFunc;
{
	if (g_idx > ARRAYSIZE(g_chars)) g_idx = 0;
	return g_chars[g_idx++];
}

- (unsigned char)ucharFunc;
{
	if (g_idx > ARRAYSIZE(g_uchars)) g_idx = 0;
	return g_uchars[g_idx++];
}

- (float)floatFunc;
{
	if (g_idx > ARRAYSIZE(g_floats)) g_idx = 0;
	return g_floats[g_idx++];
}

- (double)doubleFunc;
{
	if (g_idx > ARRAYSIZE(g_doubles)) g_idx = 0;
	return g_doubles[g_idx++];
}

- (struct dummy)dummyFunc
{
	struct dummy res;

	res.f1 = -1;
	res.f2 = +1;

	return res;
}

- (struct dummy2)dummy2Func
{
	struct dummy2 res;

	res.array[0]  = 1;
	res.array[1]  = 2;
	res.array[2]  = 3;
	res.array[3]  = 4;

	return res;
}

@end



static PyMethodDef no_methods[] = {
	{ 0, 0, 0, 0 }
};


/* Python glue */
void inittestbndl(void)
{
	PyObject* m;

	m = Py_InitModule4("testbndl", no_methods, 
		NULL, NULL, PYTHON_API_VERSION);
	if (!m) return;

	if (ObjC_ImportModule(m) < 0) return;

	PyModule_AddObject(m, "OC_TestClass1", 
		ObjCClass_New([OC_TestClass1 class]));
}
