NS_ASSUME_NONNULL_BEGIN

@interface OC_PythonNumber : NSNumber {
    PyObject* value;
}

+ (instancetype _Nullable)numberWithPythonObject:(PyObject*)value;
- (instancetype _Nullable)initWithPythonObject:(PyObject*)value;
- (void)dealloc;
- (PyObject*)__pyobjc_PythonObject__;
- (Class)classForArchiver;

@end

NS_ASSUME_NONNULL_END
