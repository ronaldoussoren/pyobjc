#ifndef PyObjC_FUNCTION_CALL_H
#define PyObjC_FUNCTION_CALL_H

NS_ASSUME_NONNULL_BEGIN

typedef PyObject* _Nullable (*PyObjC_FunctionCallFunc)(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs);

extern int PyObjC_InitFunctionCallRegistry(void);

extern int PyObjCRegister_FunctionCaller(void*                   func,
                                         PyObjC_FunctionCallFunc call_to_objc);
extern int PyObjC_RegisterFunctionSignatureMapping(char*                   signature,
                                                   PyObjC_FunctionCallFunc call_to_objc);
extern PyObjC_FunctionCallFunc _Nullable PyObjC_FindFunctionCaller(void*       function,
                                                                   const char* signature);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FUNCTION_CALL_H */
