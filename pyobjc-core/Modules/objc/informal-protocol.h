#ifndef PyObjC_INFORMAL_PROTOCOL_H
#define PyObjC_INFORMAL_PROTOCOL_H
/*!
 * @header informal-protocol.h
 * @abstruct Support for informal protocols
 * @discussion
 * 	This module defines functions and types for working with informal 
 * 	protocols. 
 *
 * 	NOTE: We also use these functions when looking for the method signatures
 * 	declared in formal protocols, as we don't have specific support for
 * 	formal protocols.
 */

extern PyTypeObject PyObjCInformalProtocol_Type;
#define PyObjCInformalProtocol_Check(obj) PyObject_TypeCheck(obj, &PyObjCInformalProtocol_Type)

int PyObjCInformalProtocol_CheckClass(PyObject*, char*, PyObject*, PyObject*);
PyObject* PyObjCInformalProtocol_FindSelector(PyObject* obj, SEL selector, int isClassMethod);
int PyObjCInformalProtocol_Warnings(char* name, PyObject* clsdict, PyObject* protocols);
PyObject* PyObjCInformalProtocol_FindProtocol(SEL selector);

/* TODO: rename */
PyObject* findSelInDict(PyObject* clsdict, SEL selector);
int signaturesEqual(const char* sig1, const char* sig2);



#endif /* PyObjC_INFORMAL_PROTOCOL_H */
