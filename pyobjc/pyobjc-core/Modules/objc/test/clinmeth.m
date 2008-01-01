/*
 * Helper classes for test_clinmeth
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface PyObjC_ClsInst1 : NSObject
{
}
-(int)instance;
-(int)both;
+(int)both;
+(int)clsmeth;
@end

@implementation PyObjC_ClsInst1

-(int)instance
{
	return 1;
}

-(int)both
{
	return 2;
}

+(int)both
{
	return 3;
}

+(int)clsmeth
{
	return 4;
}
@end


@interface PyObjC_ClsInst2 : PyObjC_ClsInst1
{
}
-(int)instance;
-(int)both;
+(int)both;
+(int)clsmeth;
@end

@implementation PyObjC_ClsInst2

-(int)instance
{
	return 10;
}

-(int)both
{
	return 20;
}

+(int)both
{
	return 30;
}

+(int)clsmeth
{
	return 40;
}
@end



static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initclinmeth(void);
void initclinmeth(void)
{
	PyObject* m;

	m = Py_InitModule4("clinmeth", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "PyObjC_ClsInst1", 
		PyObjCClass_New([PyObjC_ClsInst1 class]));
	PyModule_AddObject(m, "PyObjC_ClsInst2", 
		PyObjCClass_New([PyObjC_ClsInst2 class]));
}
