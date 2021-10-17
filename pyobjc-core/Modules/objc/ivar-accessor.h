#ifndef PyObjC_IVAR_ACCESSOR_H
#define PyObjC_IVAR_ACCESSOR_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* _Nullable PyObjCIvar_Info(PyObject* self, PyObject* arg);
extern PyObject* _Nullable PyObjCIvar_Set(PyObject* self, PyObject* _Nullable args,
                                          PyObject* _Nullable kwds);
extern PyObject* _Nullable PyObjCIvar_Get(PyObject* self, PyObject* _Nullable args,
                                          PyObject* _Nullable kwds);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_IVAR_ACCESSOR_H */
