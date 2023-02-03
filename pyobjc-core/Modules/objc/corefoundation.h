#ifndef PyObjC_COREFOUNDATION_H
#define PyObjC_COREFOUNDATION_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* PyObjC_NSCFTypeClass;

extern int PyObjCCFType_Setup(PyObject* module);
extern PyObject* _Nullable PyObjCCFType_New(char*, char*, CFTypeID);
extern PyObject* _Nullable PyObjCCF_NewSpecialFromTypeEncoding(char*, void*);
extern PyObject* _Nullable PyObjCCF_NewSpecialFromTypeID(CFTypeID, void*);
extern PyObject* _Nullable PyObjC_TryCreateCFProxy(NSObject* value);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_COREFOUNDATION_H */
