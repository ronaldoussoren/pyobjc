#ifndef PyObjC_BLOCK_AS_IMP_H
#define PyObjC_BLOCK_AS_IMP_H

NS_ASSUME_NONNULL_BEGIN

extern IMP _Nullable blockimpForSignature(SEL sel, const char* typestr,
                                          PyObject*              callable,
                                          PyObjCMethodSignature* methinfo);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_BLOCK_AS_IMP_H */
