#ifndef PyOBJC_BLOCK_SUPPORT_H
#define PyOBJC_BLOCK_SUPPORT_H

typedef void (*_block_func_ptr)(void*, ...);
extern _block_func_ptr PyObjCBlock_GetFunction(void* block);
extern void* PyObjCBlock_Create(PyObjCMethodSignature* signature, PyObject* callable);
extern void PyObjCBlock_Release(void* _block);
extern int PyObjCBlock_Setup(void);
extern PyObject* PyObjCBlock_Call(PyObject* self, PyObject* args);


#endif /* PyOBJC_BLOCK_SUPPORT_H */
