#ifndef PyObjC_FORMAL_PROTOCOL_H
#define PyObjC_FORMAL_PROTOCOL_H

extern PyTypeObject PyObjCFormalProtocol_Type;
#define PyObjCFormalProtocol_Check(obj) PyObject_TypeCheck(obj, &PyObjCFormalProtocol_Type)

extern int PyObjCFormalProtocol_CheckClass(PyObject*, char*, PyObject*, PyObject*, PyObject*);
extern const char* PyObjCFormalProtocol_FindSelectorSignature(PyObject*, SEL, int);
extern PyObject* PyObjCFormalProtocol_ForProtocol(Protocol*);
extern Protocol* PyObjCFormalProtocol_GetProtocol(PyObject*);

#endif /* PyObjC_FORMAL_PROTOCOL_H */
