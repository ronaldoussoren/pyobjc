#ifndef PyObjC_INFORMAL_PROTOCOL_H
#define PyObjC_INFORMAL_PROTOCOL_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjCInformalProtocol_Type;
#define PyObjCInformalProtocol_Check(obj)                                                \
    PyObject_TypeCheck(obj, &PyObjCInformalProtocol_Type)

extern int PyObjCInformalProtocol_CheckClass(PyObject*, char*, PyObject*, PyObject*);
extern PyObject* _Nullable PyObjCInformalProtocol_FindSelector(PyObject*, SEL, int);
extern int PyObjCInformalProtocol_Warnings(char*, PyObject*, PyObject*);
extern PyObject* _Nullable PyObjCInformalProtocol_FindProtocol(SEL);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_INFORMAL_PROTOCOL_H */
