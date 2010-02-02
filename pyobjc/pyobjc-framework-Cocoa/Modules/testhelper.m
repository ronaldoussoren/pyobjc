#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>



@interface PyObjC_TestClass3 : NSObject
{
}
+createAHostWithAddress:(NSString*)address;
+makeACopy:source;
+makeDataWithBytes:(Class)cls method:(int)i;
+makeDictFromClass:(Class)cls method:(int)i;
+getBytes:(NSData*)data;
+keyValue:(int)idx forObject: value key: id;
+(void)setKeyValue:(int)idx forObject: object key: key value: value;
@end

@implementation PyObjC_TestClass3

+createAHostWithAddress:(NSString*)address
{
	return [NSHost hostWithAddress:address];
}

+getBytes:(NSData*)data
{
	const void* bytes = [data bytes];

	if (bytes == NULL) {
		return nil;
	} else {
		return [NSData dataWithBytes:bytes length:[data length]];
	}
}


+makeDataWithBytes:(Class)cls method:(int)i
{
	if (i == 0) {
		return [cls dataWithBytes:"hello world" length:sizeof("hello world")-1];
	} else {
		id o = [cls alloc];
		return [o initWithBytes:"hello world" length:sizeof("hello world")-1];
	}
}

+makeDictFromClass:(Class)cls method:(int)i
{
	id objects[4];
	id keys[4];

	objects[0] = [[NSObject alloc] init];
	objects[1] = [[NSObject alloc] init];
	objects[2] = [[NSObject alloc] init];
	objects[3] = [[NSObject alloc] init];

	keys[0] = [[NSObject alloc] init];
	keys[1] = [[NSObject alloc] init];
	keys[2] = [[NSObject alloc] init];
	keys[3] = [[NSObject alloc] init];

	if (i == 0) {
		return [cls 
				dictionaryWithObjects:objects 
				forKeys:keys count:4];
	} else {
		return [[cls alloc] 
				initWithObjects:objects 
				forKeys:keys count:4];
	}
}


+makeACopy:source
{
	id theCopy;
	id pool;

	/* Copy the source, bracketed by the creation and
	 * destruction of an autorelease pool. This should
	 * cause a core-dump if the copy is not a 'new'
	 * object.
	 */
	pool = [[NSAutoreleasePool alloc] init];
	theCopy = [source copy];
	[pool release];
	pool = nil;
	
	return theCopy;
}

+keyValue:(int)idx forObject: object key: key
{
	switch (idx) {
	case 0: return [object valueForKey: key];
	case 1: return [object valueForKeyPath: key];
	case 2: return [object storedValueForKey: key];
	case 3: return [object valuesForKeys: key];
	}
	return nil;
}

+(void)setKeyValue:(int)idx forObject: object key: key value: value
{
	switch (idx) {
	case 0: [object takeValue: value forKey: key]; break;
	case 1: [object takeValue: value forKeyPath: key]; break;
	case 2: [object takeStoredValue: value forKey: key]; break;
	case 3: [object takeValuesFromDictionary: value]; break;
#if defined (MAC_OS_X_VERSION_10_3) && (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3)

	case 4: [object setValue: value forKey: key]; break;
	case 5: [object setValue: value forKeyPath: key]; break;
	case 6: [object setValuesForKeysWithDictionary: value]; break;
#endif
	}
}

+(NSObject*)createObservedOfClass:(Class)class observer:(NSObject*)obj keyPath:(NSString*)path
{
#if defined (MAC_OS_X_VERSION_10_3) && (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3)
	NSObject* o = [[class alloc] init];
	[o addObserver:obj
	   forKeyPath:path
	   options:NSKeyValueObservingOptionNew|NSKeyValueObservingOptionOld
	   context:0];
	return o;
#else
	/* Use arguments */
	int i;
	i = (int)&class; i = (int)&obj; i = (int)&path;
	return nil;
#endif
}
@end

@interface PyObjC_TestClass4 : NSObject
{
	id returnObject;
}
- (void)encodeWithCoder:(NSCoder*)coder;
- (void)runThread:(id)object;
- (id)returnObject;

+ (int)fetchInt:(NSCoder*)coder;
+ (double)fetchDouble:(NSCoder*)coder;
+ (NSData*)fetchData:(NSCoder*)coder;
+ (NSArray*)fetchArray:(NSCoder*)coder;
@end

@interface NSObject (IKnowWhatImDoing)
- call;
@end

@implementation PyObjC_TestClass4
-(int)_privateMethodWithArg:(float)arg
{
	return (int)arg;
}

- (void)runThread:(id)object
{
	NSObject* pool = [[NSAutoreleasePool alloc] init];
	returnObject = [object call];
	[returnObject retain];
	[pool release];
}

- (id)returnObject;
{
	return returnObject;
}

- (void)encodeWithCoder:(NSCoder*)coder
{
	double d = 1.5;
	int iArray[] = { 3,4,5,6};
	[coder encodeValueOfObjCType:@encode(double) at:&d];
	[coder encodeArrayOfObjCType:@encode(int) count:4 at:iArray];
	[coder encodeBytes:"hello world" length:11];
}

+ (int)fetchInt:(NSCoder*)coder
{
	int i;
	[coder decodeValueOfObjCType:@encode(int) at:&i];
	return i;
}

+ (double)fetchDouble:(NSCoder*)coder
{
	double i;
	[coder decodeValueOfObjCType:@encode(double) at:&i];
	return i;
}

+ (NSData*)fetchData:(NSCoder*)coder
{
	void* data;
	NSUInteger length;

	data = [coder decodeBytesWithReturnedLength:&length];
	return [NSData dataWithBytes:data length:length];
}

+ (NSArray*)fetchArray:(NSCoder*)coder
{
	int data[10];

	[coder decodeArrayOfObjCType:@encode(int) count:10 at:data];
	return [NSArray arrayWithObjects:
			[NSNumber numberWithInt:data[0]],
			[NSNumber numberWithInt:data[1]],
			[NSNumber numberWithInt:data[2]],
			[NSNumber numberWithInt:data[3]],
			[NSNumber numberWithInt:data[4]],
			[NSNumber numberWithInt:data[5]],
			[NSNumber numberWithInt:data[6]],
			[NSNumber numberWithInt:data[7]],
			[NSNumber numberWithInt:data[8]],
			[NSNumber numberWithInt:data[9]],
			nil];
}

+ (NSString*) fetchObjectDescription: (NSObject*) value
{
	return [value description];
}

@end

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};



/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"testhelper",
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

PyObject* PyInit_testhelper(void);

PyObject*
PyInit_testhelper(void)

#else

#define INITERROR() return
#define INITDONE() return

void inittesthelper(void);

void
inittesthelper(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("testhelper", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	PyModule_AddObject(m, "PyObjC_TestClass3",
		PyObjCClass_New([PyObjC_TestClass3 class]));
	PyModule_AddObject(m, "PyObjC_TestClass4",
		PyObjCClass_New([PyObjC_TestClass4 class]));

	INITDONE();
}
