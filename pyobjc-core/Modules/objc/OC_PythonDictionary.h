/*!
 * @header OC_PythonDictionary.h
 * @abstract Objective-C proxy for Python dictionaries
 * @discussion
 *     This file defines the class that is used to proxy Python
 *     dictionaries to Objective-C.
 */

#import "pyobjc.h"
#import <Foundation/Foundation.h>

/*!
 * @class OC_PythonDictionary
 * @abstract Objective-C proxy for Python dictonaries
 * @discussion
 *      Instances of this class are used as proxies for Python dicts when 
 *      these are passed to Objective-C functions/methods. Because this class 
 *      is a subclass of NSMutableDictonary Python dictionaries can be used
 *      whereever instances of NSDictionary or NSMutableDictionary are expected.
 *
 *      NOTE: We currently only proxy real 'dict' objects this way, the generic
 *      PyMapping_* API is not flexible enough, and most sequence als implement
 *      the generic mapping interface to deal with slices.
 */
@interface OC_PythonDictionary : NSMutableDictionary
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
+(OC_PythonDictionary*)depythonifyObject:(PyObject*)object;


/*!
 * @method newWithPythonObject:
 * @abstract Create a new autoreleased proxy object
 * @param value  A Python dict
 * @result Returns an autoreleased proxy object for the Python dict
 *
 * The caller must own the GIL.
 */
+(OC_PythonDictionary*)dictionaryWithPythonObject:(PyObject*)value;

/*!
 * @method initWithPythonObject:
 * @abstract Initialize a proxy object
 * @param value  A Python dict
 * @result Returns self
 * @discussion
 *    Makes the proxy object a proxy for the specified Python dict.
 *
 *    The caller must own the GIL.
 */
-(OC_PythonDictionary*)initWithPythonObject:(PyObject*)value;

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
 * @abstract Find the number of elements in the dictionary
 * @result Returns the size of the wrapped Python dictionary
 */
- (NSUInteger)count;

/*
 * @method keyEnumerator
 * @abstract Enumerate all keys in the wrapped dictionary
 * @result Returns an NSEnumerator instance for iterating over the keys
 */
- (NSEnumerator*)keyEnumerator;

/*
 * @method setObject:forKey:
 * @param object An object
 * @param key    A key, must be hashable.
 */
- (void)setObject:(id)object forKey:(id)key;

/*
 * @method removeObjectForKey:
 * @param key A key, must be hashable
 */
- (void)removeObjectForKey:(id)key;

/*
 * @method objectForKey:
 * @param key A key
 * @result Returns the object corresponding with key, or nil.
 */
- (id)objectForKey:(id)key;

/*
 * XXX - document these, internal
 */
-(BOOL)wrappedKey:(id*)keyPtr value:(id*)valuePtr atPosition:(Py_ssize_t*)positionPtr;
-(int)depythonify:(PyObject*)v toId:(id*)datum;

/* These two are only present to *disable* coding, not implement it */
- (void)encodeWithCoder:(NSCoder*)coder;
-(id)initWithCoder:(NSCoder*)coder;

@end /* interface OC_PythonDictionary */
