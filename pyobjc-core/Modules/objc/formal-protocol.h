#ifndef PyObjC_FORMAL_PROTOCOL_H
#define PyObjC_FORMAL_PROTOCOL_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* PyObjCFormalProtocol_Type;
#define PyObjCFormalProtocol_Check(obj)                                                  \
    PyObject_TypeCheck(obj, (PyTypeObject*)PyObjCFormalProtocol_Type)

extern PyObject* _Nullable PyObjCFormalProtocol_ForProtocol(Protocol*);
extern Protocol* PyObjCFormalProtocol_GetProtocol(PyObject*) NS_RETURNS_NOT_RETAINED;

extern int PyObjCFormalProtocol_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FORMAL_PROTOCOL_H */
