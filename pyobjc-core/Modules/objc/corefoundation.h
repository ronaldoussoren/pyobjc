#ifndef PyObjC_COREFOUNDATION_H
#define PyObjC_COREFOUNDATION_H

extern PyObject* PyObjC_NSCFTypeClass;

extern int PyObjCCFType_Setup(void);
extern PyObject* PyObjCCFType_New(char*, char*, CFTypeID);
extern PyObject* PyObjCCF_NewSpecial(char*, void*);
extern PyObject* PyObjCCF_NewSpecial2(CFTypeID, void*);
extern PyObject* PyObjC_TryCreateCFProxy(NSObject* value);

#endif /* PyObjC_COREFOUNDATION_H */
