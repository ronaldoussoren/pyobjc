/*
 * This file implements a (number of) class(es) that are used to test
 * method calling with PyObjC (both python -> ObjC and back)
 */
#import <Foundation/Foundation.h>

#include <Python.h>
#include <pyobjc-api.h>
#include <objc/objc-runtime.h>


struct dummy
{
	int f1;
	short f2;
};

struct dummy2
{
	int array[4];
};


struct s1 {
	int    i;
	double d;
};


struct complexStruct
{
	/*  0 */ char	 	ch;
	/*  1 */ unsigned char uch;
	/*  4 */ int		i1;	
	/*  8 */ unsigned int	u;
	/* 12 */ short 		s;
	/* 20 */ double		d;
	/* 28 */ struct s1	sub1[2];
	/* 60 */ int		i2;
	/* 62 */ unsigned short us;
	/* 64 */ char* 		str;
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
+ (char*)charpClsFunc;
+ (id)idClsFunc;

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
- (char*)charpFunc;
- (id)idFunc;
- (NSPoint)nspointFunc;

/* returns of complex values */
- (struct dummy)dummyFunc;
- (struct dummy2)dummy2Func;
/* TODO: Nested structs, unions, strings */

/* argument passing for simple types */
- (long long)longlongArg:(long long)arg;
- (unsigned long long)ulonglongArg:(unsigned long long)arg;
- (long)longArg:(long)arg;
- (unsigned long)ulongArg:(unsigned long)arg;
- (int)intArg:(int)arg;
- (unsigned int)uintArg:(unsigned int)arg;
- (short)shortArg:(short)arg;
- (unsigned short)ushortArg:(unsigned short)arg;
- (char)charArg:(char)arg;
- (unsigned char)ucharArg:(unsigned char)arg;
- (float)floatArg:(float)arg;
- (double)doubleArg:(double)arg;
- (char*)charpArg:(char*)arg;
- (id)idArg:(id)arg;

/* argument passing for complex values */
- (struct dummy)dummyArg:(struct dummy)arg;
- (struct dummy2)dummy2Arg:(struct dummy2)arg;
/* TODO: Nested structs, unions, strings */

/* in, out and in-out arguments */
- (char)passInChar:(char*)arg;
- (void)passOutChar:(char*)arg;
- (void)passInOutChar:(char*)arg;
- (short)passInShort:(short*)arg;
- (void)passOutShort:(short*)arg;
- (void)passInOutShort:(short*)arg;
- (int)passInInt:(int*)arg;
- (void)passOutInt:(int*)arg;
- (void)passInOutInt:(int*)arg;
- (long)passInLong:(long*)arg;
- (void)passOutLong:(long*)arg;
- (void)passInOutLong:(long*)arg;
- (long long)passInLongLong:(long long*)arg;
- (void)passOutLongLong:(long long*)arg;
- (void)passInOutLongLong:(long long*)arg;
- (unsigned char)passInUChar:(unsigned char*)arg;
- (void)passOutUChar:(unsigned char*)arg;
- (void)passInOutUChar:(unsigned char*)arg;
- (unsigned short)passInUShort:(unsigned short*)arg;
- (void)passOutUShort:(unsigned short*)arg;
- (void)passInOutUShort:(unsigned short*)arg;
- (unsigned int)passInUInt:(unsigned int*)arg;
- (void)passOutUInt:(unsigned int*)arg;
- (void)passInOutUInt:(unsigned int*)arg;
- (unsigned long)passInULong:(unsigned long*)arg;
- (void)passOutULong:(unsigned long*)arg;
- (void)passInOutULong:(unsigned long*)arg;
- (unsigned long long)passInULongLong:(unsigned long long*)arg;
- (void)passOutULongLong:(unsigned long long*)arg;
- (void)passInOutULongLong:(unsigned long long*)arg;
- (float)passInFloat:(float*)arg;
- (void)passOutFloat:(float*)arg;
- (void)passInOutFloat:(float*)arg;
- (double)passInDouble:(double*)arg;
- (void)passOutDouble:(double*)arg;
- (void)passInOutDouble:(double*)arg;
- (char*)passInCharp:(char**)arg;
- (void)passOutCharp:(char**)arg;
- (void)passInOutCharp:(char**)arg;
- (id)passInID:(id*)arg;
- (void)passOutID:(id*)arg;
- (void)passInOutID:(id*)arg;

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

static char* g_charps[] = {
	"hello",
	"world",
	"foobar"
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

+ (char*)charpClsFunc;
{
	if (g_idx > ARRAYSIZE(g_charps)) g_idx = 0;
	return g_charps[g_idx++];
}

+ (id)idClsFunc;
{
	if (g_idx > 3) g_idx = 0;
	
	switch (g_idx ++) {
	case 0: return [NSArray array];
	case 1: return [NSHost hostWithAddress:@"127.0.0.1"];
	case 2: return [NSMutableDictionary dictionary];
	case 3: return NULL;
	}
	return NULL;
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

- (char*)charpFunc;
{
	if (g_idx > ARRAYSIZE(g_charps)) g_idx = 0;
	return g_charps[g_idx++];
}

- (id)idFunc;
{
	if (g_idx > 3) g_idx = 0;
	
	switch (g_idx ++) {
	case 0: return [NSArray array];
	case 1: return [NSHost hostWithAddress:@"127.0.0.1"];
	case 2: return [NSMutableDictionary dictionary];
	case 3: return NULL;
	}
	return NULL;
}

- (NSPoint)nspointFunc
{
	NSPoint p = { 1.0, 2.0 };
	return p;
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

/*
 *
 * Simple, single, pass by value arguments. We return the argument after
 * modifying it. This should help to uncover cases where the bridge returns
 * the first argument instead of the real return value.
 */

- (long long)longlongArg:(long long)arg
{
	return arg / 2;
}

- (unsigned long long)ulonglongArg:(unsigned long long)arg
{
	return arg / 2;
}

- (long)longArg:(long)arg
{
	return arg / 2;
}

- (unsigned long)ulongArg:(unsigned long)arg
{
	return arg / 2;
}

- (int)intArg:(int)arg
{
	return arg / 2;
}

- (unsigned int)uintArg:(unsigned int)arg
{
	return arg / 2;
}

- (short)shortArg:(short)arg
{
	return arg / 2;
}

- (unsigned short)ushortArg:(unsigned short)arg
{
	return arg / 2;
}

- (char)charArg:(char)arg
{
	return arg / 2;
}

- (unsigned char)ucharArg:(unsigned char)arg
{
	return arg / 2;
}

- (float)floatArg:(float)arg
{
	return arg / 2;
}

- (double)doubleArg:(double)arg
{
	return arg / 2;
}

- (char*)charpArg:(char*)arg
{
static 	char buf[1024];
	int len = strlen(arg);
	int i;

	for (i = 0; i < len; i++) {
		buf[len - i - 1] = arg[i];
	}
	buf[len] = 0;

	return buf;
}

- (id)idArg:(id)arg
{
	id temp;

	if (arg == NULL) {
		temp = [NSNull null];
	} else {
		temp = arg;
	}
	return [NSArray arrayWithObject:temp];
}

- (struct dummy)dummyArg:(struct dummy)arg
{
	struct dummy result;

	result.f1 = arg.f1 * 2;
	result.f2 = arg.f2 * 2;

	return result;
}

- (struct dummy2) dummy2Arg:(struct dummy2)arg
{
	struct dummy2 result = { {-1, -1, -1, -1} };

	result.array[0] = arg.array[3] * 2;
	result.array[1] = arg.array[2] * 2;
	result.array[2] = arg.array[1] * 2;
	result.array[3] = arg.array[0] * 2;

	return result;
}

- (char)passInChar:(char*)arg;
{
	return *arg + 9;
}

- (void)passOutChar:(char*)arg;
{
	if (g_idx > ARRAYSIZE(g_ints)) g_idx = 0;
	*arg = g_chars[g_idx++];
}

- (void)passInOutChar:(char*)arg;
{
	*arg += 42;
}

- (unsigned char)passInUChar:(unsigned char*)arg;
{
	return *arg + 9;
}

- (void)passOutUChar:(unsigned char*)arg;
{
	if (g_idx > ARRAYSIZE(g_uchars)) g_idx = 0;
	*arg = g_uchars[g_idx++];
}

- (void)passInOutUChar:(unsigned char*)arg;
{
	*arg += 42;
}

- (short)passInShort:(short*)arg;
{
	return *arg + 9;
}

- (void)passOutShort:(short*)arg;
{
	if (g_idx > ARRAYSIZE(g_shorts)) g_idx = 0;
	*arg = g_shorts[g_idx++];
}

- (void)passInOutShort:(short*)arg;
{
	*arg += 42;
}

- (unsigned short)passInUShort:(unsigned short*)arg;
{
	return *arg + 9;
}

- (void)passOutUShort:(unsigned short*)arg;
{
	if (g_idx > ARRAYSIZE(g_ushorts)) g_idx = 0;
	*arg = g_ushorts[g_idx++];
}

- (void)passInOutUShort:(unsigned short*)arg;
{
	*arg += 42;
}

- (int)passInInt:(int*)arg;
{
	return *arg + 9;
}

- (void)passOutInt:(int*)arg;
{
	if (g_idx > ARRAYSIZE(g_ints)) g_idx = 0;
	*arg = g_ints[g_idx++];
}

- (void)passInOutInt:(int*)arg;
{
	*arg += 42;
}

- (unsigned int)passInUInt:(unsigned int*)arg;
{
	return *arg + 9;
}

- (void)passOutUInt:(unsigned int*)arg;
{
	if (g_idx > ARRAYSIZE(g_uints)) g_idx = 0;
	*arg = g_uints[g_idx++];
}

- (void)passInOutUInt:(unsigned int*)arg;
{
	*arg += 42;
}

- (long)passInLong:(long*)arg;
{
	return *arg + 9;
}

- (void)passOutLong:(long*)arg;
{
	if (g_idx > ARRAYSIZE(g_longs)) g_idx = 0;
	*arg = g_longs[g_idx++];
}

- (void)passInOutLong:(long*)arg;
{
	*arg += 42;
}

- (unsigned long)passInULong:(unsigned long*)arg;
{
	return *arg + 9;
}

- (void)passOutULong:(unsigned long*)arg;
{
	if (g_idx > ARRAYSIZE(g_ulongs)) g_idx = 0;
	*arg = g_ulongs[g_idx++];
}

- (void)passInOutULong:(unsigned long*)arg;
{
	*arg += 42;
}

- (long long)passInLongLong:(long long*)arg;
{
	return *arg + 9;
}

- (void)passOutLongLong:(long long*)arg;
{
	if (g_idx > ARRAYSIZE(g_longlongs)) g_idx = 0;
	*arg = g_longlongs[g_idx++];
}

- (void)passInOutLongLong:(long long*)arg;
{
	*arg += 42;
}

- (unsigned long long)passInULongLong:(unsigned long long*)arg;
{
	return *arg + 9;
}

- (void)passOutULongLong:(unsigned long long*)arg;
{
	if (g_idx > ARRAYSIZE(g_ulonglongs)) g_idx = 0;
	*arg = g_ulonglongs[g_idx++];
}

- (void)passInOutULongLong:(unsigned long long*)arg;
{
	*arg += 42;
}

- (float)passInFloat:(float*)arg;
{
	return *arg * 9;
}

- (void)passOutFloat:(float*)arg;
{
	if (g_idx > ARRAYSIZE(g_floats)) g_idx = 0;
	*arg = g_floats[g_idx++];
}

- (void)passInOutFloat:(float*)arg;
{
	*arg *= 42;
}

- (double)passInDouble:(double*)arg;
{
	return *arg * 9;
}

- (void)passOutDouble:(double*)arg;
{
	if (g_idx > ARRAYSIZE(g_doubles)) g_idx = 0;
	*arg = g_doubles[g_idx++];
}

- (void)passInOutDouble:(double*)arg;
{
	*arg *= 42;
}

- (char*)passInCharp:(char**)arg;
{
	/* Yes this is leaking, but we're only testing method calling */
	int len = strlen(*arg);
	char* res = malloc(len * 2 + 1);
	char* p;
	char* q;

	for (p = *arg, q = res; *p; p++) {
		*q ++ = *p;
		*q ++ = *p;
	}
	*q = 0;
	return res;
}

- (void)passOutCharp:(char**)arg;
{
	if (g_idx > ARRAYSIZE(g_charps)) g_idx = 0;
	*arg = g_charps[g_idx++];
}

- (void)passInOutCharp:(char**)arg;
{
	/* Yes this is leaking, but we're only testing method calling */
	int len = strlen(*arg);
	char* res = malloc(len * 2 + 1);
	char* p;
	char* q;

	for (p = *arg, q = res; *p; p++) {
		*q ++ = *p;
		*q ++ = *p;
	}
	*q = 0;
	*arg = res;
}

- (id)passInID:(id*)arg;
{
	id temp;

	if (*arg == NULL) {
		temp = [NSNull null];
	} else {
		temp = *arg;
	}
	return [NSArray arrayWithObject:temp];
}

- (void)passOutID:(id*)arg;
{
	if (g_idx > 3) g_idx = 0;
	
	switch (g_idx ++) {
	case 0: *arg = [NSArray array]; break;
	case 1: *arg = [NSHost hostWithAddress:@"127.0.0.1"]; break;
	case 2: *arg = [NSMutableDictionary dictionary]; break;
	case 3: *arg = NULL; break;
	}
}

- (void)passInOutID:(id*)arg;
{
	id temp;

	if (*arg == NULL) {
		temp = [NSNull null];
	} else {
		temp = *arg;
	}
	*arg = [NSArray arrayWithObject:temp];
}

@end




/*
 * Testing of calling into python
 *
 * This is *very* incomplete at the moment, we need 'call' and 'invoke' 
 * versions for all methods in OC_TestClass1 (both class and instance methods)
 */

@interface OC_TestClass2: NSObject
{
}

/* "plain" calls */
-(char)callInstanceCharFuncOf:(OC_TestClass1*)arg;
-(unsigned char)callInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg;

-(short)callInstanceShortFuncOf:(OC_TestClass1*)arg;
-(unsigned short)callInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg;

-(int)callInstanceIntFuncOf:(OC_TestClass1*)arg;
-(unsigned int)callInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg;

-(long)callInstanceLongFuncOf:(OC_TestClass1*)arg;
-(unsigned long)callInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg;

-(long long)callInstanceLongLongFuncOf:(OC_TestClass1*)arg;
-(unsigned long long)callInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg;

-(float)callInstanceFloatFuncOf:(OC_TestClass1*)arg;
-(double)callInstanceDoubleFuncOf:(OC_TestClass1*)arg;

-(id)callInstanceIdFuncOf:(OC_TestClass1*)arg;
-(struct dummy)callInstanceDummyFuncOf:(OC_TestClass1*)arg;
-(struct dummy2)callInstanceDummy2FuncOf:(OC_TestClass1*)arg;
-(NSPoint)callInstanceNSPointFuncOf:(OC_TestClass1*)arg;

/* "NSInvocation" calls */
-(char)invokeInstanceCharFuncOf:(OC_TestClass1*)arg;
-(unsigned char)invokeInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg;

-(short)invokeInstanceShortFuncOf:(OC_TestClass1*)arg;
-(unsigned short)invokeInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg;

-(int)invokeInstanceIntFuncOf:(OC_TestClass1*)arg;
-(unsigned int)invokeInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg;

-(long)invokeInstanceLongFuncOf:(OC_TestClass1*)arg;
-(unsigned long)invokeInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg;

-(long long)invokeInstanceLongLongFuncOf:(OC_TestClass1*)arg;
-(unsigned long long)invokeInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg;

-(float)invokeInstanceFloatFuncOf:(OC_TestClass1*)arg;
-(double)invokeInstanceDoubleFuncOf:(OC_TestClass1*)arg;

-(id)invokeInstanceIdFuncOf:(OC_TestClass1*)arg;
-(struct dummy)invokeInstanceDummyFuncOf:(OC_TestClass1*)arg;
-(struct dummy2)invokeInstanceDummy2FuncOf:(OC_TestClass1*)arg;
-(NSPoint)invokeInstanceNSPointFuncOf:(OC_TestClass1*)arg;

@end


#define SETUP_INVOCATION(inv, target, selector) \
	inv = [NSInvocation invocationWithMethodSignature: \
		[arg methodSignatureForSelector:selector]]; \
	[inv setTarget:target]; \
	[inv setSelector:selector]; 

@implementation OC_TestClass2 

-(char)callInstanceCharFuncOf:(OC_TestClass1*)arg
{
	return [arg charFunc];
}

-(unsigned char)callInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg
{
	return [arg ucharFunc];
}

-(short)callInstanceShortFuncOf:(OC_TestClass1*)arg
{
	return [arg shortFunc];
}

-(unsigned short)callInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg
{
	return [arg ushortFunc];
}

-(int)callInstanceIntFuncOf:(OC_TestClass1*)arg
{
	return [arg intFunc];
}

-(unsigned int)callInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg
{
	return [arg uintFunc];
}

-(long)callInstanceLongFuncOf:(OC_TestClass1*)arg
{
	return [arg longFunc];
}

-(unsigned long)callInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg
{
	return [arg ulongFunc];
}

-(char)invokeInstanceCharFuncOf:(OC_TestClass1*)arg
{
	char res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(charFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(unsigned char)invokeInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg
{
	unsigned char res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(ucharFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(short)invokeInstanceShortFuncOf:(OC_TestClass1*)arg
{
	short res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(shortFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(unsigned short)invokeInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg
{
	unsigned short res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(ushortFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(int)invokeInstanceIntFuncOf:(OC_TestClass1*)arg
{
	int res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(intFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(unsigned int)invokeInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg
{
	unsigned int res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(uintFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(long)invokeInstanceLongFuncOf:(OC_TestClass1*)arg
{
	long res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(longFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(unsigned long)invokeInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg
{
	unsigned long res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(ulongFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(long long)callInstanceLongLongFuncOf:(OC_TestClass1*)arg
{
	return [arg longlongFunc];
}

-(unsigned long long)callInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg
{
	return [arg ulonglongFunc];
}

-(float)callInstanceFloatFuncOf:(OC_TestClass1*)arg
{
	return [arg floatFunc];
}


-(double)callInstanceDoubleFuncOf:(OC_TestClass1*)arg
{
	return [arg doubleFunc];
}

-(id)callInstanceIdFuncOf:(OC_TestClass1*)arg
{
	return [arg idFunc];
}

-(struct dummy)callInstanceDummyFuncOf:(OC_TestClass1*)arg
{
	return [arg dummyFunc];
}

-(struct dummy2)callInstanceDummy2FuncOf:(OC_TestClass1*)arg
{
	return [arg dummy2Func];
}

-(NSPoint)callInstanceNSPointFuncOf:(OC_TestClass1*)arg
{
	return [arg nspointFunc];
}


-(long long)invokeInstanceLongLongFuncOf:(OC_TestClass1*)arg
{
	long long res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(longlongFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(unsigned long long)invokeInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg
{
	unsigned long long res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(ulonglongFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(float)invokeInstanceFloatFuncOf:(OC_TestClass1*)arg
{
	float res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(floatFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(double)invokeInstanceDoubleFuncOf:(OC_TestClass1*)arg
{
	double res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(doubleFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(id)invokeInstanceIdFuncOf:(OC_TestClass1*)arg
{
	id res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(idFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(struct dummy)invokeInstanceDummyFuncOf:(OC_TestClass1*)arg
{
	struct dummy res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(dummyFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(struct dummy2)invokeInstanceDummy2FuncOf:(OC_TestClass1*)arg
{
	struct dummy2 res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(dummyFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
	return res;
}

-(NSPoint)invokeInstanceNSPointFuncOf:(OC_TestClass1*)arg
{
	NSPoint res;
	NSInvocation* inv;

	SETUP_INVOCATION(inv, arg, @selector(nspointFunc))
	
	[arg forwardInvocation:inv];
	[inv getReturnValue:&res];
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
	PyModule_AddObject(m, "OC_TestClass2", 
		ObjCClass_New([OC_TestClass2 class]));
	
}
