#ifndef OC_PythonArray_h
#define OC_PythonArray_h

/*!
 * @header OC_PythonArray.h 
 * @abstract Objective-C proxy class for Python sequences
 * @discussion
 *     This file defines the class that is used to represent Python sequences
 *     in Objective-C.
 */

#import <Foundation/NSArray.h>

/*!
 * @class       OC_PythonArray
 * @abstract    Objective-C proxy class for Python sequences
 * @discussion  Instances of this class are used as proxies for Python 
 * 	        sequences when these are passed to Objective-C code. Because 
 * 	        this class is a subclass of NSMutableArray Python sequences 
 * 	        can be used everywhere where NSArray or NSMutableArray objects 
 * 	        are expected.
 */
@interface OC_PythonArray : NSMutableArray
{
	PyObject* value;
}

/*!
 * @method newWithPythonObject:
 * @abstract Create a new OC_PythonArray for a specific Python sequence
 * @param value A python sequence
 * @result Returns an autoreleased instance representing value
 */
+ newWithPythonObject:(PyObject*)value;

/*!
 * @method initWithPythonObject:
 * @abstract Initialise a OC_PythonArray for a specific Python sequence
 * @param value A python sequence
 * @result Returns self
 */
- initWithPythonObject:(PyObject*)value;

/*!
 * @method dealloc
 * @abstract Deallocate the object
 */
-(void)dealloc;

/*!
 * @method dealloc
 * @abstract Access the wrapped Python sequence
 * @result  Returns a new reference to the wrapped Python sequence.
 */
-(PyObject*)__pyobjc_PythonObject__;

/*!
 * @method count
 * @result  Returns the length of the wrapped Python sequence
 */
-(int)count;

/*!
 * @method objectAtIndex:
 * @param idx An index
 * @result  Returns the object at the specified index in the wrapped Python
 *          sequence
 */
- (id)objectAtIndex:(int)idx;

/*!
 * @method replaceObjectAtIndex:withObject:
 * @abstract Replace the current value at idx by the new value
 * @discussion This method will raise an exception when the wrapped Python
 *             sequence is immutable.
 * @param idx An index
 * @param newValue A replacement value
 */
-(void)replaceObjectAtIndex:(int)idx withObject:newValue;

@end

#endif /* OC_PythonArray_h */
