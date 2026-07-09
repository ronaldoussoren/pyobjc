#ifndef PyObjC_UNICODE_H
#define PyObjC_UNICODE_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* PyObjCUnicode_Type;
#define PyObjCUnicode_Check(obj) Py_IS_TYPE((obj), (PyTypeObject*)PyObjCUnicode_Type)

extern PyObject* _Nullable PyObjCUnicode_New(NSString* value);
extern int PyObjCUnicode_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_UNICODE_H */
