#ifndef PyObjC_MEMVIEW_H
#define PyObjC_MEMVIEW_H

NS_ASSUME_NONNULL_BEGIN

int       PyObjCMemView_Check(PyObject* view);
PyObject* _Nullable PyObjCMemView_New(void);
Py_buffer* _Nullable PyObjCMemView_GetBuffer(PyObject* view);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_MEMVIEW_H */
