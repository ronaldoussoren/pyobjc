/*
 * This file contains an implementation for a proxy class for python
 * objects that conform to the 'sequence' protocol.
 */
#ifndef OC_PythonArray_h
#define OC_PythonArray_h

#import <Foundation/NSArray.h>
#include "Python.h"

@interface OC_PythonArray : NSMutableArray
{
	PyObject* value;
}
+newWithPythonObject:(PyObject*)value;
-initWithPythonObject:(PyObject*)value;
-(PyObject*)pyObject;
-(void)dealloc;

-(int)count;
-objectAtIndex:(int)idx;
-(void)replaceObjectAtIndex:(int)idx withObject:newValue;

@end /* OC_PythonArray class interface */

#endif /* OC_PythonArray_h */
