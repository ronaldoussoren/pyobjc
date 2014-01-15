#ifndef PyObjC_INFORMAL_PROTOCOL_H
#define PyObjC_INFORMAL_PROTOCOL_H

extern PyTypeObject PyObjCInformalProtocol_Type;
#define PyObjCInformalProtocol_Check(obj) PyObject_TypeCheck(obj, &PyObjCInformalProtocol_Type)

extern int PyObjCInformalProtocol_CheckClass(PyObject*, char*, PyObject*, PyObject*);
extern PyObject* PyObjCInformalProtocol_FindSelector(PyObject*, SEL, int);
extern int PyObjCInformalProtocol_Warnings(char*, PyObject*, PyObject*);
extern PyObject* PyObjCInformalProtocol_FindProtocol(SEL);

#endif /* PyObjC_INFORMAL_PROTOCOL_H */
