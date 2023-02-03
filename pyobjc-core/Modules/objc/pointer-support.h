#ifndef PyObjC_POINTER_SUPPORT_H
#define PyObjC_POINTER_SUPPORT_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjCZoneWrapper_Type;

typedef PyObject* _Nullable (*PyObjCPointerWrapper_ToPythonFunc)(void* _Nonnull);
typedef int (*PyObjCPointerWrapper_FromPythonFunc)(PyObject*, void* _Nonnull);

extern int PyObjCPointerWrapper_Register(const char* type_name, const char*,
                                         PyObjCPointerWrapper_ToPythonFunc   pythonify,
                                         PyObjCPointerWrapper_FromPythonFunc depythonify);

extern int PyObjCPointerWrapper_RegisterID(const char* name, const char*);
extern PyObject* _Nullable PyObjCPointer_GetIDEncodings(void);

extern int PyObjCPointerWrapper_RegisterCF(const char*);
extern PyObject* _Nullable PyObjCPointerWrapper_ToPython(const char*, const void*);

extern int PyObjCPointerWrapper_FromPython(const char*, PyObject*, void*);
extern int PyObjCPointerWrapper_Init(PyObject*);
extern int PyObjCPointerWrapper_HaveWrapper(const char*);

extern const char* _Nullable PyObjCPointerWrapper_Describe(const char* signature);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_POINTER_SUPPORT_H */
