#ifndef PyObjC_INFORMAL_PROTOCOL_H
#define PyObjC_INFORMAL_PROTOCOL_H

extern PyTypeObject PyObjCInformalProtocol_Type;
#define PyObjCInformalProtocol_Check(obj) PyObject_TypeCheck(obj, &PyObjCInformalProtocol_Type)

int PyObjCInformalProtocol_CheckClass(PyObject*, char*, PyObject*, PyObject*);
PyObject* PyObjCInformalProtocol_FindSelector(PyObject* obj, SEL selector);
int PyObjCInformalProtocol_Warnings(char* name, PyObject* clsdict, PyObject* protocols);
PyObject* PyObjCInformalProtocol_FindProtocol(SEL selector);

#endif /* PyObjC_INFORMAL_PROTOCOL_H */
