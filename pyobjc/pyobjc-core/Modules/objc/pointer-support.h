#ifndef PyObjC_POINTER_SUPPORT_H
#define  PyObjC_POINTER_SUPPORT_H

extern PyTypeObject PyObjCZoneWrapper_Type;

typedef PyObject* (*PyObjCPointerWrapper_ToPythonFunc)(void*);
typedef int (*PyObjCPointerWrapper_FromPythonFunc)(PyObject*, void*);

int PyObjCPointerWrapper_Register(
	const char*, PyObjCPointerWrapper_ToPythonFunc pythonify,
	PyObjCPointerWrapper_FromPythonFunc depythonify);

int PyObjCPointerWrapper_RegisterID(const char*);

int PyObjCPointerWrapper_RegisterCF(const char*);
PyObject* PyObjCPointerWrapper_ToPython(const char*, void*);

int PyObjCPointerWrapper_FromPython(const char*, PyObject*, void*);
int PyObjCPointerWrapper_Init(void);
int PyObjCPointerWrapper_HaveWrapper(const char*);

#endif /* PyObjC_POINTER_SUPPORT_H */
