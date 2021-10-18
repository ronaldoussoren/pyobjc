#ifndef PyObjC_UNICODE_H
#define PyObjC_UNICODE_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjCUnicode_Type;
#define PyObjCUnicode_Check(obj) PyObject_TypeCheck(obj, &PyObjCUnicode_Type)

extern PyObject* _Nullable PyObjCUnicode_New(NSString* value);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_UNICODE_H */
