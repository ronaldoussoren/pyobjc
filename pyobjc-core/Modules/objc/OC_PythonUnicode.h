/*!
 * @header OC_PythonUnicode.h
 * @abstract Objective-C proxy class for Python unicode
 * @discussion
 *     This file defines the class that is used to represent Python unicode
 *     in Objective-C.
 */

NS_ASSUME_NONNULL_BEGIN

/*!
 * @class       OC_PythonUnicode
 * @abstract    Objective-C proxy class for Python unicode
 * @discussion  Instances of this class are used as proxies for Python
 *              unicode when these are passed to Objective-C code.
 */
/* XXX: Cannot be PyObjC_FINAL_CLASS */
@interface OC_PythonUnicode : NSString {
    PyObject* value;
    id        realObject;
}

/*!
 * @method newWithPythonObject:
 * @abstract Create a new OC_PythonUnicode for a specific Python unicode
 * @param value A python unicode
 * @result Returns an autoreleased instance representing value
 *
 * Caller must own the GIL.
 */
+ (id _Nullable)unicodeWithPythonObject:(PyObject*)value;

/*!
 * @method initWithPythonObject:
 * @abstract Initialise a OC_PythonUnicode for a specific Python unicode
 * @param value A python unicode
 * @result Returns self
 *
 * Caller must own the GIL.
 */
- (id _Nullable)initWithPythonObject:(PyObject*)value;

/*!
 * @method dealloc
 * @abstract Deallocate the object
 */
- (void)dealloc;

/*!
 * @abstract Access the wrapped Python unicode
 * @result Returns a new reference to the wrapped Python unicode.
 */
- (PyObject*)__pyobjc_PythonObject__;

/*
 * Primitive NSString methods
 *
 */
- (NSUInteger)length;
- (unichar)characterAtIndex:(NSUInteger)index;
- (void)getCharacters:(unichar*)buffer range:(NSRange)aRange;

@end

NS_ASSUME_NONNULL_END
