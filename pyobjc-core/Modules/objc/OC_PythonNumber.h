#include "pyobjc.h"

@interface OC_PythonNumber : NSNumber
{
	PyObject* value;
#if 0
	union {
		long long 		as_longlong;
		unsigned long long 	as_ulonglong;
		double    		as_double;
	}	c_value;
#endif
}

+ newWithPythonObject:(PyObject*)value;
- initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

@end
