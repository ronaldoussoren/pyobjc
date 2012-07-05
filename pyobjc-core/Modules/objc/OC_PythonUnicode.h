/*!
 * @header OC_PythonUnicode.h
 * @abstract Objective-C proxy class for Python unicode
 * @discussion
 *     This file defines the class that is used to represent Python unicode
 *     in Objective-C.
 */

#include "pyobjc.h"

/*!
 * @class       OC_PythonUnicode
 * @abstract    Objective-C proxy class for Python unicode
 * @discussion  Instances of this class are used as proxies for Python 
 *              unicode when these are passed to Objective-C code.
 */
@interface OC_PythonUnicode : NSString
{
	PyObject* value;
	id realObject;

#ifdef PyObjC_STR_CACHE_IMP
	/* Cache IMPs for proxied methods, for slightly better efficiency */
	NSUInteger (*imp_length)(id, SEL);
	unichar (*imp_charAtIndex)(id, SEL, NSUInteger);
	void (*imp_getCharacters)(id, SEL, unichar*, NSRange);
#endif /* PyObjC_STR_CACHE_IMP */
}

/*!
 * @method newWithPythonObject:
 * @abstract Create a new OC_PythonUnicode for a specific Python unicode
 * @param value A python unicode
 * @result Returns an autoreleased instance representing value
 *
 * Caller must own the GIL.
 */
+(id)unicodeWithPythonObject:(PyObject*)value;

/*!
 * @method initWithPythonObject:
 * @abstract Initialise a OC_PythonUnicode for a specific Python unicode
 * @param value A python unicode
 * @result Returns self
 *
 * Caller must own the GIL.
 */
-(id)initWithPythonObject:(PyObject*)value;

/*!
 * @method dealloc
 * @abstract Deallocate the object
 */
-(void)dealloc;

/*!
 * @abstract Access the wrapped Python unicode
 * @result Returns a new reference to the wrapped Python unicode.
 */
-(PyObject*)__pyobjc_PythonObject__;

/*
 * Primitive NSString methods
 *
 */
-(NSUInteger)length;
-(unichar)characterAtIndex:(NSUInteger)index;
-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange;

@end
