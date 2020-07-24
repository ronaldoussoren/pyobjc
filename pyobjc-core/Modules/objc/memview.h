#ifndef PyObjC_MEMVIEW_H
#define PyObjC_MEMVIEW_H

int       PyObjCMemView_Check(PyObject* view);
PyObject* PyObjCMemView_New(void);
Py_buffer* PyObjCMemView_GetBuffer(PyObject* view);

#endif /* PyObjC_MEMVIEW_H */
