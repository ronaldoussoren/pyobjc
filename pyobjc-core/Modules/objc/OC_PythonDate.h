NS_ASSUME_NONNULL_BEGIN

@interface OC_PythonDate : NSDate {
    PyObject* value;
    NSDate*   oc_value;
}

+ (instancetype _Nullable)dateWithPythonObject:(PyObject*)value;
- (instancetype _Nullable)initWithPythonObject:(PyObject*)value;
- (void)dealloc;
- (PyObject*)__pyobjc_PythonObject__;

/* Implementation of the NSDate interface */
- (NSTimeInterval)timeIntervalSinceReferenceDate;

/* NSCoding support */
- (void)encodeWithCoder:(NSCoder*)coder;
- (id _Nullable)initWithCoder:(NSCoder*)coder;

@end

NS_ASSUME_NONNULL_END
