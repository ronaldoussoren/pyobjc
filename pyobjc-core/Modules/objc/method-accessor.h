#ifndef PyObjC_METHOD_ACCESSOR_H
#define PyObjC_METHOD_ACCESSOR_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjCMethodAccessor_Type;
extern PyObject* _Nullable PyObjCMethodAccessor_New(PyObject* base, int class_method);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_METHOD_ACCESSOR_H */
