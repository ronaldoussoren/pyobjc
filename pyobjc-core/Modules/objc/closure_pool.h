/*
 * Closure require special memmory support on x86_64 and PPC64: executation must be
 * explicitly enabled for the memory used for closure.
 */
#ifndef PyObjC_CLOSURE_POOL
#define PyObjC_CLOSURE_POOL

extern ffi_closure* PyObjC_malloc_closure(void);
extern int PyObjC_free_closure(ffi_closure* cl);


#endif /* PyObjC_CLOSURE_POOL */
