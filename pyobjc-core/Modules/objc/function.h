#ifndef PyObjC_FUNCTION_H
#define PyObjC_FUNCTION_H

extern PyTypeObject PyObjCFunc_Type;
#define PyObjCFunction_Check(value) PyObject_TypeCheck(value, &PyObjCFunc_Type)

extern PyObject* PyObjCFunc_New(PyObject*, void*, const char*, PyObject*, PyObject*);
extern PyObject* PyObjCFunc_WithMethodSignature(PyObject*, void*, PyObjCMethodSignature*);
extern PyObjCMethodSignature* PyObjCFunc_GetMethodSignature(PyObject*);

#endif /* PyObjC_FUNCTION_H */
