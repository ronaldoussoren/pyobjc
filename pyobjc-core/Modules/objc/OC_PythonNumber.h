#include "pyobjc.h"

@interface OC_PythonNumber : NSNumber
{
    PyObject* value;
}

+(instancetype)numberWithPythonObject:(PyObject*)value;
-(instancetype)initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

@end
