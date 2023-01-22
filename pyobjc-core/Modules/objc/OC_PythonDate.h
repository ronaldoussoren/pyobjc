NS_ASSUME_NONNULL_BEGIN

/* XXX: Cannot be PyObjC_FINAL_CLASS */
@interface OC_PythonDate : NSDate {
    NSTimeInterval timeSinceEpoch;
    PyObject*      value;
}

+ (instancetype _Nullable)dateWithPythonObject:(PyObject*)value;
- (instancetype _Nullable)initWithPythonObject:(PyObject*)value;
- (PyObject*)__pyobjc_PythonObject__;
@end

NS_ASSUME_NONNULL_END
