#ifndef PyObjC_PARSEXML_H
#define PyObjC_PARSEXML_H

int PyObjCXML_Init(void);
PyObject* PyObjC_SetSetupCFClasses(PyObject* self, PyObject* arg);
PyObject* PyObjC_SetStructConvenience(PyObject* self, PyObject* arg);
int PyObjC_ProcessXML(char* data, int length, PyObject* globalDict, const char* dylibPath, const char* framework, PyObject* inlineTab);


#endif /* PyObjC_PARSEXML_H */
