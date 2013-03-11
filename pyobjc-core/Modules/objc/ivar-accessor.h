#ifndef PyObjC_IVAR_ACCESSOR_H
#define PyObjC_IVAR_ACCESSOR_H

extern PyObject* PyObjCIvar_Info(PyObject* self, PyObject* arg);
extern PyObject* PyObjCIvar_Set(PyObject* self, PyObject* args, PyObject* kwds);
extern PyObject* PyObjCIvar_Get(PyObject* self, PyObject* args, PyObject* kwds);

#endif /* PyObjC_IVAR_ACCESSOR_H */
