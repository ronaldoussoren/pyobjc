#ifndef OBJC_UTIL
#define OBJC_UTIL

#include <Foundation/NSException.h>
#define THREADSTATE_AUTORELEASEPOOL "__threadstate_autoreleasepool"

extern PyObject* PyObjCExc_Error;
extern PyObject* PyObjCExc_NoSuchClassError;
extern PyObject* PyObjCExc_InternalError;
extern PyObject* PyObjCExc_UnInitDeallocWarning;
extern PyObject* PyObjCExc_ObjCRevivalWarning;
extern PyObject* PyObjCExc_LockError;

int PyObjCUtil_Init(PyObject* module);

void PyObjCErr_FromObjC(NSException* localException);
void PyObjCErr_ToObjC(void);

void PyObjCErr_ToObjCWithGILState(PyGILState_STATE* state);

NSException* PyObjCErr_AsExc(void);

PyObject* PyObjC_CallPython(id self, SEL selector, PyObject* arglist, BOOL* isAlloc, BOOL* isCFAlloc);

char* PyObjCUtil_Strdup(const char* value);

#include <Foundation/NSMapTable.h>
extern NSMapTableKeyCallBacks PyObjCUtil_PointerKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_PointerValueCallBacks;

extern NSMapTableKeyCallBacks PyObjCUtil_ObjCIdentityKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_ObjCValueCallBacks;

void    PyObjC_FreeCArray(int, void*);
int     PyObjC_PythonToCArray(BOOL, BOOL, const char*, PyObject*, void**, Py_ssize_t*, PyObject**);
PyObject* PyObjC_CArrayToPython(const char*, void*, Py_ssize_t);
PyObject* PyObjC_CArrayToPython2(const char*, void*, Py_ssize_t, bool already_retained, bool already_cfretained);
int     PyObjC_IsPythonKeyword(const char* word);


extern int PyObjCRT_SimplifySignature(char* signature, char* buf, size_t buflen);

int PyObjCObject_Convert(PyObject* object, void* pvar);
int PyObjCClass_Convert(PyObject* object, void* pvar);
int PyObjCSelector_Convert(PyObject* object, void* pvar);
int PyObjC_ConvertBOOL(PyObject* object, void* pvar);
int PyObjC_ConvertChar(PyObject* object, void* pvar);

#endif /* OBJC_UTIL */
