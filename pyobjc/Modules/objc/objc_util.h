#ifndef OBJC_UTIL
#define OBJC_UTIL

#include <Foundation/NSException.h>

extern PyObject* ObjCExc_error;
extern PyObject* ObjCExc_noclass_error;
extern PyObject* ObjCExc_internal_error;

int ObjCUtil_Init(PyObject* module);

extern PyObject* ObjC_class_extender;
int ObjC_AddConvenienceMethods(Class cls, PyObject* type_dict);
int  ObjC_UpdateConvenienceMethods(PyObject* cls);

void ObjCErr_Set(PyObject* exc, char* fmt, ...);
void PyObjCErr_FromObjC(NSException* localException);
void PyObjCErr_ToObjC(void);
void PyObjCErr_ToObjCWithGILState(PyGILState_STATE* state);

PyObject* PyObjC_CallPython(id self, SEL selector, PyObject* arglist, int* isAlloc);

char* ObjC_strdup(const char* value);

#include <Foundation/NSMapTable.h>
extern NSMapTableKeyCallBacks ObjC_PointerKeyCallBacks;
extern NSMapTableValueCallBacks ObjC_PointerValueCallBacks;


//extern NSMapTableKeyCallBacks ObjC_PyObjectKeyCallBacks;
//extern NSMapTableValueCallBacks ObjC_PyObjectValueCallBacks;
//

void    PyObjC_FreeCArray(int, void*);
int     PyObjC_PythonToCArray(const char*, PyObject*, PyObject*, void**, int*);
PyObject* PyObjC_CArrayToPython(const char*, void*, int);

#endif /* OBJC_UTIL */
