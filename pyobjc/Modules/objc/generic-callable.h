#ifndef PyObjC_CALLABLE_H
#define PyObjC_CALLABLE_H

typedef int (*)PyObjC_FUNCTION();


#define PyObjCCallable_Check(o) ((o)->ob_type == &PyObjCCallable_Type)

extern PyObject* PyObjCCallable_New(
		PyObjC_FUNCTION func, const char* signature);

extern PyObjC_FUNCTION PyObjCCallable_GetFunction(PyObject* callable);
extern const char* PyObjCCallable_GetSignature(PyObject* callable);

#endif /* PyObjC_CALLABLE_H */
