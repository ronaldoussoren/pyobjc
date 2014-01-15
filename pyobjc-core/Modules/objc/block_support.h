#ifndef PyOBJC_BLOCK_SUPPORT_H
#define PyOBJC_BLOCK_SUPPORT_H

typedef void (*_block_func_ptr)(void*, ...);
extern _block_func_ptr PyObjCBlock_GetFunction(void* block) __attribute__((__nonnull__(1)));
extern const char* PyObjCBlock_GetSignature(void* _block) __attribute__((__nonnull__(1)));
extern void* PyObjCBlock_Create(PyObjCMethodSignature* signature, PyObject* callable) __attribute__((__nonnull__(1,2))) __attribute__((__warn_unused_result__));
extern void PyObjCBlock_Release(void* _block) __attribute__((__nonnull__(1)));
extern int PyObjCBlock_Setup(void) __attribute__((__warn_unused_result__));
extern PyObject* PyObjCBlock_Call(PyObject* self, PyObject* args) __attribute__((__nonnull__(1,2))) __attribute__((__warn_unused_result__));


#endif /* PyOBJC_BLOCK_SUPPORT_H */
