#ifndef PyObjC_OPTION_H
#define PyObjC_OPTION_H

NS_ASSUME_NONNULL_BEGIN

#if Py_GIL_DISABLED
#define PyObjC_ATOMIC _Atomic
#else
#define PyObjC_ATOMIC
#endif

extern PyObjC_ATOMIC BOOL PyObjC_Verbose;
extern PyObjC_ATOMIC BOOL PyObjC_UseKVO;
extern PyObjC_ATOMIC BOOL PyObjCPointer_RaiseException;
extern PyObjC_ATOMIC BOOL PyObjC_StructsIndexable;
extern PyObjC_ATOMIC BOOL PyObjC_StructsWritable;

extern PyObjC_ATOMIC int        PyObjC_DeprecationVersion;
extern PyObjC_ATOMIC Py_ssize_t PyObjC_MappingCount;

extern PyObject* _Nullable PyObjC_ClassExtender;
extern PyObject* _Nullable PyObjC_MakeBundleForClass;
extern PyObject* _Nullable PyObjC_NSNumberWrapper;
extern PyObject* _Nullable PyObjC_transformAttribute;
extern PyObject* _Nullable PyObjC_processClassDict;
extern PyObject* _Nullable PyObjC_setDunderNew;
extern PyObject* _Nullable PyObjC_genericNewClass;

extern int PyObjC_SetupOptions(PyObject* m);

extern int PyObjC_encodeWithCoder(PyObject* pyObject, NSCoder* coder) __attribute__((warn_unused_result));
extern PyObject* _Nullable  PyObjC_decodeWithCoder(NSCoder* coder, id self) __attribute__((warn_unused_result));
extern PyObject* _Nullable PyObjC_Copy(PyObject* arg) __attribute__((warn_unused_result));
extern int PyObjC_GetKey(PyObject* object, id key, id _Nullable *_Nonnull value) __attribute__((warn_unused_result));
extern int PyObjC_SetKey(PyObject* object, id key, id value) __attribute__((warn_unused_result));
extern int PyObjC_GetKeyPath(PyObject* object, id keypath, id _Nullable* _Nonnull value) __attribute__((warn_unused_result));
extern int PyObjC_SetKeyPath(PyObject* object, id keypath, id value) __attribute__((warn_unused_result));
extern bool PyObjC_IsBuiltinDate(PyObject* object);
extern bool PyObjC_IsBuiltinDatetime(PyObject* object);
extern int PyObjC_IsDictLike(PyObject* object);
extern int PyObjC_IsListLike(PyObject* object);
extern int PyObjC_IsSetLike(PyObject* object);
extern int PyObjC_IsDateLike(PyObject* object);
extern int PyObjC_IsPathLike(PyObject* object);
extern PyObject* _Nullable PyObjC_DateFromTimestamp(double timestamp);
extern PyObject* _Nullable PyObjC_DatetimeFromTimestamp(double timestamp, id tzinfo);
extern PyObject* _Nullable PyObjC_GetCallableDocString(PyObject* callable, void* _Nullable closure);
extern PyObject* _Nullable PyObjC_GetCallableSignature(PyObject* callable, void* _Nullable closure);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OPTION_H */
