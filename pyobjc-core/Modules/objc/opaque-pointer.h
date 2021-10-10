#ifndef PyObjC_OPAQUE_POINTER_H
#define PyObjC_OPAQUE_POINTER_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* _Nullable PyObjCCreateOpaquePointerType(const char* name,
                                                         const char* typestr,
                                                         const char* _Nullable docstr);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OPAQUE_POINTER_H */
