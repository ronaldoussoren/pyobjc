#ifndef OBJC_UTIL
#define OBJC_UTIL

#include <Foundation/NSException.h>
#define THREADSTATE_AUTORELEASEPOOL "__threadstate_autoreleasepool"

extern PyObject* PyObjCExc_Error;
extern PyObject* PyObjCExc_NoSuchClassError;
extern PyObject* PyObjCExc_InternalError;
extern PyObject* PyObjCExc_UnInitDeallocWarning;

int PyObjCUtil_Init(PyObject* module);

void PyObjCErr_FromObjC(NSException* localException);
void PyObjCErr_ToObjC(void);

void PyObjCErr_ToObjCWithGILState(PyGILState_STATE* state);

NSException* PyObjCErr_AsExc(void);

PyObject* PyObjC_CallPython(id self, SEL selector, PyObject* arglist, int* isAlloc);

char* PyObjCUtil_Strdup(const char* value);

#include <Foundation/NSMapTable.h>
extern NSMapTableKeyCallBacks PyObjCUtil_PointerKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_PointerValueCallBacks;

extern NSMapTableKeyCallBacks PyObjCUtil_ObjCIdentityKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_ObjCValueCallBacks;

void    PyObjC_FreeCArray(int, void*);
int     PyObjC_PythonToCArray(const char*, PyObject*, PyObject*, void**, int*);
PyObject* PyObjC_CArrayToPython(const char*, void*, int);
int     PyObjC_IsPythonKeyword(const char* word);


extern int PyObjCRT_SimplifySignature(char* signature, char* buf, size_t buflen);

int PyObjCObject_Convert(PyObject* object, void* pvar);
int PyObjCClass_Convert(PyObject* object, void* pvar);
int PyObjCSelector_Convert(PyObject* object, void* pvar);
int PyObjC_ConvertBOOL(PyObject* object, void* pvar);
int PyObjC_ConvertChar(PyObject* object, void* pvar);

#endif /* OBJC_UTIL */
