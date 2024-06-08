#ifndef PyObjC_OPTION_H
#define PyObjC_OPTION_H

NS_ASSUME_NONNULL_BEGIN

extern BOOL PyObjC_Verbose;
extern BOOL PyObjC_UseKVO;
extern BOOL PyObjCPointer_RaiseException;
extern BOOL PyObjC_StructsIndexable;
extern BOOL PyObjC_StructsWritable;

extern int        PyObjC_DeprecationVersion;
extern Py_ssize_t PyObjC_MappingCount;
extern int        PyObjC_NSCoding_Version;
extern PyObject* _Nullable PyObjC_Encoder;
extern PyObject* _Nullable PyObjC_Decoder;
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

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OPTION_H */
