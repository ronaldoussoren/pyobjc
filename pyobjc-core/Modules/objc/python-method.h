#ifndef PyObjC_PYTHON_METHOD_H
#define PyObjC_PYTHON_METHOD_H

extern PyTypeObject PyObjCPythonMethod_Type;
#define PyObjCPythonMethod_Check(obj) PyObject_TypeCheck(obj, &PyObjCPythonMethod_Type)

extern PyObject* PyObjCPythonMethod_GetMethod(PyObject*);

#endif /* PyObjC_PYTHON_METHOD_H */

