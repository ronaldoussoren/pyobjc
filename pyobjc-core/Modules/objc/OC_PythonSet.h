#include "pyobjc.h"

@interface OC_PythonSet : NSMutableSet
{
	PyObject* value;
}

+ (instancetype)depythonifyObject:(PyObject*)object;
+ (instancetype)setWithPythonObject:(PyObject*)value;
- (id)initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

@end
