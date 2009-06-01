#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OCTestBlock : NSObject {}

#if PyObjC_BUILD_RELEASE >= 1006

-(int(^)(void))getIntBlock;
-(double(^)(double,double))getFloatBlock;
-(void)callIntBlock:(void(^)(int))block withValue:(int)value;
-(double)callDoubleBlock:(double(^)(double, double))block withValue:(double)v1 andValue:(double)v2;
#endif

@end

@implementation OCTestBlock

#if PyObjC_BUILD_RELEASE >= 1006

-(int(^)(void))getIntBlock
{
	return ^{ return 42; };
}

-(double(^)(double,double))getFloatBlock
{
	return ^(double a, double b) { return a + b; };
}

-(void)callIntBlock:(void(^)(int))block withValue:(int)value
{
	block(value);
}

-(double)callDoubleBlock: (double(^)(double, double))block withValue:(double)v1 andValue:(double)v2
{
	return block(v1, v2);
}
#endif

@end


static PyMethodDef NULL_methods[] = {
	        { 0, 0, 0, 0 }
};

void initblock(void);
void initblock(void)
{
	PyObject* m;

	m = Py_InitModule4("block", NULL_methods,
		NULL, NULL, PYTHON_API_VERSION);

	if (PyObjC_ImportAPI(m) < 0) return;

	PyModule_AddObject(m, "OCTestBlock",
	    PyObjCClass_New([OCTestBlock class]));
}
