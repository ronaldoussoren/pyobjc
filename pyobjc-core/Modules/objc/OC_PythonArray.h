/*!
 * @header OC_PythonArray.h 
 * @abstract Objective-C proxy class for Python sequences
 * @discussion
 *     This file defines the class that is used to represent Python sequences
 *     in Objective-C.
 */

#import "pyobjc.h"
#import <Foundation/Foundation.h>

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
 * @method depythonifyObject:
 * @abstract Create a new instance when appropriate
 * @param value A python object
 * @result Returns an autoreleased value or nil. Might set error in latter case.
 *
 * Caller must own the GIL
 */
+ depythonifyObject:(PyObject*)object;


/*!
 * @method newWithPythonObject:
 * @abstract Create a new OC_PythonArray for a specific Python sequence
 * @param value A python sequence
 * @result Returns an autoreleased instance representing value
 *
 * Caller must own the GIL.
 */
+ newWithPythonObject:(PyObject*)value;

/*!
 * @method initWithPythonObject:
 * @abstract Initialise a OC_PythonArray for a specific Python sequence
 * @param value A python sequence
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
 * @method dealloc
 * @abstract Access the wrapped Python sequence
 * @result  Returns a new reference to the wrapped Python sequence.
 */
-(PyObject*)__pyobjc_PythonObject__;

/*!
 * @method count
 * @result  Returns the length of the wrapped Python sequence
 */
-(NSUInteger)count;

/*!
 * @method objectAtIndex:
 * @param idx An index
 * @result  Returns the object at the specified index in the wrapped Python
 *          sequence
 */
- (id)objectAtIndex:(NSUInteger)idx;

/*!
 * @method replaceObjectAtIndex:withObject:
 * @abstract Replace the current value at idx by the new value
 * @discussion This method will raise an exception when the wrapped Python
 *             sequence is immutable.
 * @param idx An index
 * @param newValue A replacement value
 */
-(void)replaceObjectAtIndex:(NSUInteger)idx withObject:newValue;

/*!
 * @method getObjects:inRange:
 * @abstract Fetch objects in the specified range
 * @discussion The output buffer must have enough space to contain all
 *             requested objects, the range must be valid.
 *
 *             This method is not documented in the NSArray interface, but
 *             is used by Cocoa on MacOS X 10.3 when an instance of this
 *             class is used as the value for -setObject:forKey: in
 *             NSUserDefaults.
 * @param buffer  The output buffer
 * @param range   The range of objects to fetch.
 */
-(void)getObjects:(id*)buffer inRange:(NSRange)range;

/*!
 * @method addObject:
 * @abstract Append an object
 * @param anObject The object that will be append
 */
-(void)addObject:(id)anObject;

/*!
 * @method insertObject:atIndex:
 * @abstract Insert an object at the specified index
 * @param anObject The object to insert
 * @param idx  The index
 */
-(void)insertObject:(id)anObject atIndex:(NSUInteger)idx;

/*!
 * @method removeLastObject
 * @abstract Remove the last object of the sequence
 */
-(void)removeLastObject;

/*!
 * @method removeObjectAtIndex:
 * @abstract Remove a specific item
 * @param idx Which object should be removed
 */
-(void)removeObjectAtIndex:(NSUInteger)idx;

/* These two are only present to *disable* coding, not implement it */
- (void)encodeWithCoder:(NSCoder*)coder;
- initWithCoder:(NSCoder*)coder;

@end
