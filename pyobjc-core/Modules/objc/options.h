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

extern PyObject* _Nullable PyObjC_CopyFunc;
extern PyObject* _Nullable PyObjC_ClassExtender;
extern PyObject* _Nullable PyObjC_MakeBundleForClass;
extern PyObject* _Nullable PyObjC_NSNumberWrapper;
extern PyObject* _Nullable PyObjC_CallableDocFunction;
extern PyObject* _Nullable PyObjC_CallableSignatureFunction;
extern PyObject* _Nullable PyObjC_getKey;
extern PyObject* _Nullable PyObjC_setKey;
extern PyObject* _Nullable PyObjC_getKeyPath;
extern PyObject* _Nullable PyObjC_setKeyPath;
extern PyObject* _Nullable PyObjC_transformAttribute;
extern PyObject* _Nullable PyObjC_processClassDict;
extern PyObject* _Nullable PyObjC_setDunderNew;
extern PyObject* _Nullable PyObjC_genericNewClass;

extern PyObject* _Nullable PyObjC_DictLikeTypes;
extern PyObject* _Nullable PyObjC_ListLikeTypes;
extern PyObject* _Nullable PyObjC_SetLikeTypes;
extern PyObject* _Nullable PyObjC_DateLikeTypes;
extern PyObject* _Nullable PyObjC_PathLikeTypes;

extern PyObject* _Nullable PyObjC_DateTime_Date_Type;
extern PyObject* _Nullable PyObjC_DateTime_DateTime_Type;

extern int PyObjC_SetupOptions(PyObject* m);

extern int PyObjC_encodeWithCoder(PyObject* pyObject, NSCoder* coder) __attribute__((warn_unused_result));
extern PyObject* _Nullable  PyObjC_decodeWithCoder(NSCoder* coder, id self) __attribute__((warn_unused_result));

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OPTION_H */
