#ifndef PyObjC_PYTHON_METHOD_H
#define PyObjC_PYTHON_METHOD_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjCPythonMethod_Type;
#define PyObjCPythonMethod_Check(obj) PyObject_TypeCheck(obj, &PyObjCPythonMethod_Type)

extern PyObject* _Nullable PyObjCPythonMethod_GetMethod(PyObject*);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_PYTHON_METHOD_H */
