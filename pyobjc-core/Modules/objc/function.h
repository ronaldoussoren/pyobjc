#ifndef PyObjC_FUNCTION_H
#define PyObjC_FUNCTION_H

extern PyTypeObject PyObjCFunc_Type;

#define PyObjCFunction_Check(value) \
	PyObject_TypeCheck(value, &PyObjCFunc_Type)

extern PyObject*
PyObjCFunc_New(PyObject* name, void* func, const char* signature, PyObject* doc, PyObject* meta);

extern PyObject* 
PyObjCFunc_WithMethodSignature(PyObject* name, void* func, PyObjCMethodSignature* signature);

extern PyObjCMethodSignature*
PyObjCFunc_GetMethodSignature(PyObject* func);

#endif /* PyObjC_FUNCTION_H */
