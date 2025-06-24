/*
 * Closure require special memory support on x86_64 and PPC64: execution must be
 * explicitly enabled for the memory used for closure.
 */
#ifndef PyObjC_CLOSURE_POOL
#define PyObjC_CLOSURE_POOL

#import <Foundation/Foundation.h>

#ifndef MAC_OS_X_VERSION_10_15
#define MAC_OS_X_VERSION_10_15 101500
#endif

#if defined(__x86_64__) && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_15

#ifndef NS_ASSUME_NONNULL_BEGIN
/*
 * Old compiler without nullability support
 */
#define NS_ASSUME_NONNULL_BEGIN
#define NS_ASSUME_NONNULL_END
#define _Nullable
#define _Nonnull
#endif /* !NS_ASSUME_NONNULL_BEGIN */

NS_ASSUME_NONNULL_BEGIN

#define HAVE_CLOSURE_POOL 1

extern ffi_closure* _Nullable PyObjC_ffi_closure_alloc(
    size_t size, void* _Nullable* _Nonnull code_loc);
extern int PyObjC_ffi_closure_free(ffi_closure* cl);

NS_ASSUME_NONNULL_END

#endif

#endif /* PyObjC_CLOSURE_POOL */
