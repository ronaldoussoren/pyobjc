#ifndef PyObjC_FUNCTION_H
#define PyObjC_FUNCTION_H

extern PyTypeObject PyObjCFunc_Type;

PyObject*
PyObjCFunc_New(PyObject* name, void* func, const char* signature, PyObject* doc);

#endif /* PyObjC_FUNCTION_H */
