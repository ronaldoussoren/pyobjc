#ifndef PyObjC_MEMVIEW_H
#define PyObjC_MEMVIEW_H

NS_ASSUME_NONNULL_BEGIN

extern int PyObjCMemView_Check(PyObject* view);
extern PyObject* _Nullable PyObjCMemView_New(void);
extern Py_buffer* _Nullable PyObjCMemView_GetBuffer(PyObject* view);
extern int PyObjCMemView_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_MEMVIEW_H */
