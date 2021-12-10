#ifndef PyObjC_FUNCTION_H
#define PyObjC_FUNCTION_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjCFunc_Type;
#define PyObjCFunction_Check(value) PyObject_TypeCheck(value, &PyObjCFunc_Type)

extern PyObject* _Nullable PyObjCFunc_New(PyObject*, void*, const char*,
                                          PyObject* _Nullable, PyObject*);
extern PyObject* _Nullable PyObjCFunc_WithMethodSignature(PyObject* _Nullable, void*,
                                                          PyObjCMethodSignature*);
extern PyObjCMethodSignature* _Nullable PyObjCFunc_GetMethodSignature(PyObject*);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FUNCTION_H */
