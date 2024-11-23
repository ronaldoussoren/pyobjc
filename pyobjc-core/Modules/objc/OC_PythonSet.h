NS_ASSUME_NONNULL_BEGIN

/* XXX: Cannot be PyObjC_FINAL_CLASS */
@interface OC_PythonSet : NSMutableSet {
    PyObject* value;
}

+ (instancetype _Nullable)setWithPythonObject:(PyObject*)value;
- (id _Nullable)initWithPythonObject:(PyObject*)value;
- (void)dealloc;
- (PyObject* _Nullable)__pyobjc_PythonObject__;

@end

NS_ASSUME_NONNULL_END
