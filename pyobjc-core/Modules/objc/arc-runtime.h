/*
 * See the clang documentation for more information
 * about the definitions in thise file, in particular
 * <http://clang.llvm.org/docs/AutomaticReferenceCounting.html>
 *
 * These should be available in the 64-bit runtime
 * when deploying for OSX 10.7 or later, and using a new
 * enough SDK.
 */
#ifndef PyObjC_ARC_RUNTIME_H
#define PyObjC_ARC_RUNTIME_H

#if defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1007

#define HAVE_ARC_RUNTIME 1

extern id objc_autorelease(id value);
extern void objc_autoreleasePoolPop(void* pool);
extern void* objc_autoreleasePoolPush(void);

extern id objc_autoreleaseReturnValue(id value);
extern void objc_copyWeak(id* dest, id* src);
extern void objc_destroyWeak(id* object);
extern void objc_initWeak(id* object, id value);
extern id objc_loadWeak(id* object);
extern id objc_loadWeakRetained(id* object);
extern void objc_moveWeak(id* dest, id* src);
extern void objc_release(id value);
extern id objc_retain(id value);
extern id objc_retainAutorelease(id value);
extern id objc_retainAutoreleaseReturnValue(id value);
extern id objc_retainAutoreleasedReturnValue(id value);
extern id objc_retainBlock(id value);
extern id objc_storeStrong(id* object, id value);
extern id objc_storeWeak(id* object, id value);


#else

#undef HAVE_ARC_RUNTIME

#endif


#endif /* PyObjC_ARC_RUNTIME_H */

