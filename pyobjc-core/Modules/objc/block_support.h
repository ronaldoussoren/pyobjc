#ifndef PyOBJC_BLOCK_SUPPORT_H
#define PyOBJC_BLOCK_SUPPORT_H

NS_ASSUME_NONNULL_BEGIN

typedef void (*_block_func_ptr)(void*, ...);
extern _block_func_ptr PyObjCBlock_GetFunction(void* block);
extern const char* _Nullable PyObjCBlock_GetSignature(void* _block);
extern void* _Nullable PyObjCBlock_Create(PyObjCMethodSignature* signature,
                                          PyObject*              callable)
    __attribute__((__warn_unused_result__));
extern int PyObjCBlock_Setup(PyObject* module) __attribute__((__warn_unused_result__));
extern PyObject* _Nullable PyObjCBlock_Call(PyObject* self, PyObject* args)
    __attribute__((__warn_unused_result__));

NS_ASSUME_NONNULL_END

#endif /* PyOBJC_BLOCK_SUPPORT_H */
