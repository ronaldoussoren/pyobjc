#ifndef PyObjC_PythonEnumerator_H
#define PyObjC_PythonEnumerator_H

NS_ASSUME_NONNULL_BEGIN

PyObjC_FINAL_CLASS @interface OC_PythonEnumerator : NSEnumerator {
    PyObject* value;
    BOOL      valid;
}

+ (instancetype)enumeratorWithPythonObject:(PyObject*)object;
- (id)initWithPythonObject:(PyObject*)object;

@end

NS_ASSUME_NONNULL_END

#endif /* PyObjC_PythonEnumerator_H */
