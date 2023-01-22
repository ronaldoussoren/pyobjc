/*!
 * @header OC_PythonArray.h
 * @abstract Objective-C proxy class for Python sequences
 * @discussion
 *     This file defines the class that is used to represent Python sequences
 *     in Objective-C.
 */

#import "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/*!
 * @class       OC_PythonArray
 * @abstract    Objective-C proxy class for Python sequences
 * @discussion  Instances of this class are used as proxies for Python
 *              sequences when these are passed to Objective-C code. Because
 *              this class is a subclass of NSMutableArray Python sequences
 *              can be used everywhere where NSArray or NSMutableArray objects
 *              are expected.
 */
/* XXX: Cannot be PyObjC_FINAL_CLASS */
@interface OC_PythonArray : NSMutableArray {
    PyObject* value;
}

/*!
 * @method arrayWithPythonObject:
 * @abstract Create a new OC_PythonArray for a specific Python sequence
 * @param value A python sequence
 * @result Returns an autoreleased instance representing value
 *
 * Caller must own the GIL.
 */
+ (instancetype _Nullable)arrayWithPythonObject:(PyObject*)value;

/*!
 * @method initWithPythonObject:
 * @abstract Initialise a OC_PythonArray for a specific Python sequence
 * @param value A python sequence
 * @result Returns self
 *
 * Caller must own the GIL.
 */
- (instancetype _Nullable)initWithPythonObject:(PyObject*)value;

/*!
 * @method dealloc
 * @abstract Deallocate the object
 */
- (void)dealloc;

/*!
 * @method dealloc
 * @abstract Access the wrapped Python sequence
 * @result  Returns a new reference to the wrapped Python sequence.
 */
- (PyObject*)__pyobjc_PythonObject__;

/*!
 * @method count
 * @result  Returns the length of the wrapped Python sequence
 */
- (NSUInteger)count;

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
- (void)replaceObjectAtIndex:(NSUInteger)idx withObject:(id)newValue;

/*!
 * @method addObject:
 * @abstract Append an object
 * @param anObject The object that will be append
 */
- (void)addObject:(id)anObject;

/*!
 * @method insertObject:atIndex:
 * @abstract Insert an object at the specified index
 * @param anObject The object to insert
 * @param idx  The index
 */
- (void)insertObject:(id)anObject atIndex:(NSUInteger)idx;

/*!
 * @method removeLastObject
 * @abstract Remove the last object of the sequence
 */
- (void)removeLastObject;

/*!
 * @method removeObjectAtIndex:
 * @abstract Remove a specific item
 * @param idx Which object should be removed
 */
- (void)removeObjectAtIndex:(NSUInteger)idx;

/*
 * @method encodeWithCoder:
 * @abstract Encode a python sequence to an NSCoder
 * @param coder The coder to use
 */
- (void)encodeWithCoder:(NSCoder*)coder;

/*
 * @method initWithCoder:
 * @abstract Restore a python sequence from an NSCoder
 * @param coder The coder to use
 */
- (id _Nullable)initWithCoder:(NSCoder*)coder;

@end

NS_ASSUME_NONNULL_END
