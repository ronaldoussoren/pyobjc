#include "pyobjc.h"

@interface OC_PythonNumber : NSNumber
{
	PyObject* value;
}

+ (instancetype)numberWithPythonObject:(PyObject*)value;
- (id)initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

@end
