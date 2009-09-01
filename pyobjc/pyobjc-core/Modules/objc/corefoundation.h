#ifndef PyObjC_COREFOUNDATION_H
#define PyObjC_COREFOUNDATION_H

extern PyObject* PyObjC_NSCFTypeClass;

extern int PyObjCCFType_Setup(void);
extern PyObject* PyObjCCFType_New(char* name, char* encoding, CFTypeID typeID);
extern PyObject* PyObjCCF_NewSpecial(char* encoding, void* datum);
extern PyObject* PyObjCCF_NewSpecial2(CFTypeID typeid, void* datum);


#endif /* PyObjC_COREFOUNDATION_H */
