/*!
 * @header OC_PythonDictionary.h
 * @abstract Objective-C proxy for Python dictionaries
 * @discussion
 *     This file defines the class that is used to proxy Python
 *     dictionaries to Objective-C.
 */

NS_ASSUME_NONNULL_BEGIN

/*!
 * @class OC_PythonDictionary
 * @abstract Objective-C proxy for Python dictionaries
 * @discussion
 *      Instances of this class are used as proxies for Python dicts when
 *      these are passed to Objective-C functions/methods. Because this class
 *      is a subclass of NSMutableDictonary Python dictionaries can be used
 *      wherever instances of NSDictionary or NSMutableDictionary are expected.
 *
 *      NOTE: We currently only proxy real 'dict' objects this way, the generic
 *      PyMapping_* API is not flexible enough, and most sequence also implement
 *      the generic mapping interface to deal with slices.
 */
/* XXX: Cannot be PyObjC_FINAL_CLASS */
@interface OC_PythonDictionary : NSMutableDictionary {
    PyObject* value;
}

+ (instancetype _Nullable)dictionaryWithPythonObject:(PyObject*)value;
- (instancetype _Nullable)initWithPythonObject:(PyObject*)value;
- (void)dealloc;
- (PyObject*)__pyobjc_PythonObject__;
- (NSUInteger)count;
- (NSEnumerator*)keyEnumerator;
- (void)setObject:(id)object forKey:(id)key;
- (void)removeObjectForKey:(id)key;
- (id _Nullable)objectForKey:(id)key;
- (void)encodeWithCoder:(NSCoder*)coder;
- (id _Nullable)initWithCoder:(NSCoder*)coder;

@end /* interface OC_PythonDictionary */

NS_ASSUME_NONNULL_END
