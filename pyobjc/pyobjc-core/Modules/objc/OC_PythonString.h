/*!
 * @header OC_PythonString.h
 * @abstract Objective-C proxy class for Python str
 * @discussion
 *     This file defines the class that is used to represent Python str
 *     in Objective-C.
 */

#include "pyobjc.h"

/*!
 * @class       OC_PythonString
 * @abstract    Objective-C proxy class for Python str
 * @discussion  Instances of this class are used as proxies for Python 
 *              str when these are passed to Objective-C code.
 */
@interface OC_PythonString : NSString
{
	PyObject* value;
	id realObject;
}

/*!
 * @method newWithPythonObject:
 * @abstract Create a new OC_PythonString for a specific Python str
 * @param value A python str
 * @result Returns an autoreleased instance representing value
 *
 * Caller must own the GIL.
 */
+ stringWithPythonObject:(PyObject*)value;

/*!
 * @method initWithPythonObject:
 * @abstract Initialise a OC_PythonString for a specific Python str
 * @param value A python str
 * @result Returns self
 *
 * Caller must own the GIL.
 */
- initWithPythonObject:(PyObject*)value;

/*!
 * @method dealloc
 * @abstract Deallocate the object
 */
-(void)dealloc;

/*!
 * @abstract Access the wrapped Python str
 * @result Returns a new reference to the wrapped Python str.
 */
-(PyObject*)__pyobjc_PythonObject__;

/*!
 * @abstract Access the NSString* representing the str
 * @result Returns a backing NSString* object
 */
-(id)__realObject__;

/*
 * Primitive NSString methods
 *
 */
-(NSUInteger)length;
-(unichar)characterAtIndex:(NSUInteger)index;
-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange;

@end
