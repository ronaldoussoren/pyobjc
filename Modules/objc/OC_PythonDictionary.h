/*
 * This file contains an implementation for a proxy class for python
 * objects that conform to the 'mapping' protocol.
 */
#ifndef OC_PythonDictionary_h
#define OC_PythonDictionary_h

#import <Foundation/NSDictionary.h>
#include "Python.h"

@interface OC_PythonDictionary : NSMutableDictionary
{
	PyObject* value;
}
+newWithPythonObject:(PyObject*)value;
-initWithPythonObject:(PyObject*)value;
-(PyObject*)pyObject;
-(void)dealloc;

-(int)count;
-keyEnumerator;
-(void)setObject:o forKey:k;
-(void)removeObjectForKey:k;
-objectForKey:k;

@end /* OC_PythonDictionary class interface */

#endif /* OC_PythonDictionary_h */
