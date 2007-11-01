#ifndef PyObjC_FORMAL_PROTOCOL_H
#define PyObjC_FORMAL_PROTOCOL_H
/*!
 * @header formal-protocol.h
 * @abstruct Support for formal protocols (aka @protocol)
 * @discussion
 * 	This module defines functions and types for working with formal 
 * 	protocols. 
 *
 * 	NOTE: We also use these functions when looking for the method signatures
 * 	declared in formal protocols, as we don't have specific support for
 * 	formal protocols.
 */

extern PyTypeObject PyObjCFormalProtocol_Type;
#define PyObjCFormalProtocol_Check(obj) PyObject_TypeCheck(obj, &PyObjCFormalProtocol_Type)

int PyObjCFormalProtocol_CheckClass(PyObject*, char*, PyObject*, PyObject*, PyObject*);
const char* PyObjCFormalProtocol_FindSelectorSignature(PyObject* obj, SEL selector, int isClassMethod);
PyObject* PyObjCFormalProtocol_ForProtocol(Protocol* protocol);
Protocol* PyObjCFormalProtocol_GetProtocol(PyObject* protocol);

#endif /* PyObjC_FORMAL_PROTOCOL_H */
