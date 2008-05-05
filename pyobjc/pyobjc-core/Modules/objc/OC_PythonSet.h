#include "pyobjc.h"

@interface OC_PythonSet : NSMutableSet
{
	PyObject* value;
}

+ depythonifyObject:(PyObject*)object;
+ newWithPythonObject:(PyObject*)value;
- initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

@end
