#ifndef PyObjC_POINTER_SUPPORT_H
#define  PyObjC_POINTER_SUPPORT_H

extern PyTypeObject PyObjCZoneWrapper_Type;

typedef PyObject* (*PyObjCPointerWrapper_ToPythonFunc)(void*);
typedef int (*PyObjCPointerWrapper_FromPythonFunc)(PyObject*, void*);

int PyObjCPointerWrapper_Register(
	const char*, PyObjCPointerWrapper_ToPythonFunc pythonify,
	PyObjCPointerWrapper_FromPythonFunc depythonify);

PyObject* PyObjCPointerWrapper_ToPython(const char*, void*);

int PyObjCPointerWrapper_FromPython(const char*, PyObject*, void*);
int PyObjCPointerWrapper_Init(void);

#endif /* PyObjC_POINTER_SUPPORT_H */
