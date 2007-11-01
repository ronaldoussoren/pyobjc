/*
 * This module is used in test_exceptions
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static NSString* addSomeUnicode(NSString* input)
{
	return [NSString stringWithFormat:@"%@%C%C", input, 0x1234, 0x2049];
}

@interface PyObjCTestExceptions : NSObject
{
}
-(void)raiseSimple;
-(void)raiseSimpleWithInfo;
-(void)raiseUnicodeName;
-(void)raiseUnicodeReason;
-(void)raiseUnicodeWithInfo;
@end

@implementation PyObjCTestExceptions

-(void)raiseSimple
{
	[NSException raise:@"SimpleException" format:@"hello world"];
}

-(void)raiseSimpleWithInfo
{
	[[NSException 	exceptionWithName:@"InfoException" 
			reason:@"Reason string"
			userInfo:[NSDictionary dictionaryWithObjectsAndKeys:
				@"value1", @"key1",
				@"value2", @"key2",
				NULL]] raise];
}

-(void)raiseUnicodeName;
{
	[NSException 	
		raise:addSomeUnicode(@"SimpleException") 
		format:@"hello world"];
}

-(void)raiseUnicodeReason;
{
	[NSException 
		raise:@"SimpleException" 
		format:addSomeUnicode(@"hello world")];
}

-(void)raiseUnicodeWithInfo
{
	[[NSException 	exceptionWithName:addSomeUnicode(@"InfoException")
			reason:addSomeUnicode(@"Reason string")
			userInfo:[NSDictionary dictionaryWithObjectsAndKeys:
				addSomeUnicode(@"value1"), 
					addSomeUnicode(@"key1"),
				addSomeUnicode(@"value2"), 
					addSomeUnicode(@"key2"),
				NULL]] raise];
}

@end


static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

void initexceptions(void);
void initexceptions(void)
{
	PyObject* m;

	m = Py_InitModule4("exceptions", mod_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	PyModule_AddObject(m, "PyObjCTestExceptions", 
		PyObjCClass_New([PyObjCTestExceptions class]));
}
