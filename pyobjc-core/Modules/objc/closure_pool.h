/*
 * Closure require special memory support on x86_64 and PPC64: execution must be
 * explicitly enabled for the memory used for closure.
 */
#ifndef PyObjC_CLOSURE_POOL
#define PyObjC_CLOSURE_POOL

#if defined(__x86_64__) && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_15

#define HAVE_CLOSURE_POOL 1

extern ffi_closure* PyObjC_ffi_closure_alloc(size_t size, void** code_loc);
extern int          PyObjC_ffi_closure_free(ffi_closure* cl);

#endif

#endif /* PyObjC_CLOSURE_POOL */
