#ifndef OC_PythonDictionary_h
#define OC_PythonDictionary_h

#import <Foundation/NSDictionary.h>

/*
 * OC_PythonDictionary - Objective-C proxy for Python dictonaries
 *
 * Instances of this class are used as proxies for Python dicts when these
 * are passed to Objective-C functions/methods. Because this class is
 * a subclass of NSMutableDictonary Python dictionaries can be used
 * whereever instances of NSDictionary or NSMutableDictionary are expected.
 *
 * NOTE: We currently only proxy real 'dict' objects this way, the generic
 * PyMapping_* API is not flexible enough!
 */
@interface OC_PythonDictionary : NSMutableDictionary
{
	PyObject* value;
}
+newWithPythonObject:(PyObject*)value;
-initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;

-(int)count;
-keyEnumerator;
-(void)setObject:o forKey:k;
-(void)removeObjectForKey:k;
-objectForKey:k;

@end /* interface OC_PythonDictionary */

#endif /* OC_PythonDictionary_h */
