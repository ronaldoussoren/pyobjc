#ifndef OBJC_UTIL
#define OBJC_UTIL

#include <Foundation/NSException.h>

extern PyObject* ObjCExc_error;
extern PyObject* ObjCExc_noclass_error;
extern PyObject* ObjCExc_internal_error;
extern PyObject* PyObjCExc_NoProtocol;

int ObjCUtil_Init(PyObject* module);

void PyObjCErr_FromObjC(NSException* localException);
void PyObjCErr_ToObjC(void);

#define PyObjCErr_ToObjCWithGILState(state) PyObjCErr_ToObjCWithGILState_(state, __FUNCTION__)
void PyObjCErr_ToObjCWithGILState_(PyGILState_STATE* state, const char* __function__);

PyObject* PyObjC_CallPython(id self, SEL selector, PyObject* arglist, int* isAlloc);

char* PyObjCUtil_Strdup(const char* value);

#include <Foundation/NSMapTable.h>
extern NSMapTableKeyCallBacks PyObjCUtil_PointerKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_PointerValueCallBacks;


//extern NSMapTableKeyCallBacks ObjC_PyObjectKeyCallBacks;
//extern NSMapTableValueCallBacks ObjC_PyObjectValueCallBacks;
//

void    PyObjC_FreeCArray(int, void*);
int     PyObjC_PythonToCArray(const char*, PyObject*, PyObject*, void**, int*);
PyObject* PyObjC_CArrayToPython(const char*, void*, int);
int     PyObjC_IsPythonKeyword(const char* word);

#endif /* OBJC_UTIL */
