/*
 * This module is used in test_exceptions
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static NSString* addSomeUnicode(NSString* input)
{
	return [NSString stringWithFormat:@"%@%C%C", input, (short)0x1234, (short)0x2049];
}

@interface PyObjCTestExceptions : NSObject
{
}
-(void)raiseSimple;
-(void)raiseSimpleWithInfo;
-(void)raiseUnicodeName;
-(void)raiseUnicodeReason;
-(void)raiseUnicodeWithInfo;
-(void)raiseAString;
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

-(void)raiseUnicodeName
{
	[NSException 	
		raise:addSomeUnicode(@"SimpleException") 
		format:@"hello world"];
}

-(void)raiseUnicodeReason
{
	[NSException 
		raise:@"SimpleException" 
		format:@"%@", addSomeUnicode(@"hello world")];
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

-(void)raiseAString
{
	@throw @"thrown string";
}

@end


static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"exceptions",
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

PyObject* PyInit_exceptions(void);

PyObject*
PyInit_exceptions(void)

#else

#define INITERROR() return
#define INITDONE() return

void initexceptions(void);

void
initexceptions(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("exceptions", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "PyObjCTestExceptions", 
		PyObjCClass_New([PyObjCTestExceptions class])) < 0) {
		INITERROR();
	}
	INITDONE();
}
