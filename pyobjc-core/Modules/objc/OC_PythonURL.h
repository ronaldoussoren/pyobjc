NS_ASSUME_NONNULL_BEGIN

PyObjC_FINAL_CLASS @interface OC_PythonURL : NSURL {
    PyObject* value;
}

+ (instancetype _Nullable)URLWithPythonObject:(PyObject*)value;
- (id _Nullable)initWithPythonObject:(PyObject*)value;
- (PyObject*)__pyobjc_PythonObject__;

@end

NS_ASSUME_NONNULL_END
