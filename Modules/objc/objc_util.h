#ifndef OBJC_UTIL
#define OBJC_UTIL

#include <Python.h>
#include <Foundation/NSException.h>

extern PyObject* ObjCExc_error;
extern PyObject* ObjCExc_noclass_error;
extern PyObject* ObjCExc_internal_error;
extern PyObject* PyObjCExc_ProtocolWarning;

int ObjCUtil_Init(PyObject* module);

extern PyObject* ObjC_class_extender;
int ObjC_AddConvenienceMethods(Class cls, PyObject* type_dict);
int  ObjC_UpdateConvenienceMethods(PyObject* cls);

void ObjCErr_Set(PyObject* exc, char* fmt, ...);
void ObjCErr_FromObjC(NSException* localException);
void ObjCErr_ToObjC(void);

PyObject* PyObjC_CallPython(id self, SEL selector, PyObject* arglist);

char* ObjC_strdup(const char* value);

#include <Foundation/NSMapTable.h>
extern NSMapTableKeyCallBacks ObjC_PointerKeyCallBacks;
extern NSMapTableValueCallBacks ObjC_PointerValueCallBacks;
extern NSMapTableKeyCallBacks ObjC_PyObjectKeyCallBacks;
extern NSMapTableValueCallBacks ObjC_PyObjectValueCallBacks;


#endif /* OBJC_UTIL */
